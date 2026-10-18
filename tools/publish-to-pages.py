#!/usr/bin/env python3
"""
把 Gridea 构建产物（默认 www/）转成 GitHub Pages 可直接发布的结构。

Gridea 生成的站点面向域名根目录，全站使用根绝对路径（/styles/、/post …）。
仓库的 Pages 挂在 /amore-plus/ 子路径下，需要把这些路径改写为带前缀的形式。

注意：<base href="..."> 对以 / 开头的绝对路径无效（浏览器直接按站点根解析），
因此必须逐个重写 href/src，而不是依赖 <base>。

用法：
    python3 tools/publish-to-pages.py              # 处理 www/ 并输出到 docs/
    python3 tools/publish-to-pages.py <src> <dst>  # 指定源与目标目录
"""
import os
import re
import sys

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BASE = "/amore-plus/"

# 这些内容不属于站点产物，不应随 Pages 发布
SKIP_DIRS = {".git", ".github", ".workbuddy", "themes", "posts", "config", "static", "node_modules"}
SKIP_NAMES = {".DS_Store"}

# 站内导航项，已由站点自身提供，无需再加前缀
SELF = BASE.rstrip("/")  # /amore-plus


def rewrite(html):
    """把根绝对路径改写为带站点前缀的形式。"""
    def sub_attr(m):
        attr, quote, path = m.group(1), m.group(2), m.group(3)
        # 已是目标前缀，或指向站外资源，保持原样
        if path.startswith(BASE) or path.startswith(SELF + "/") or path == SELF:
            return m.group(0)
        # 外链（协议、锚点、mailto 等）
        if path.startswith(("#", "//", "http:", "https:", "mailto:", "tel:", "data:")):
            return m.group(0)
        if not path.startswith("/"):
            return m.group(0)
        return f"{attr}={quote}{BASE.rstrip('/')}{path}{quote}"

    # href="..." / src="..."
    html = re.sub(r'\b(href|src)=(["\'])(/[^"\']*)\2', sub_attr, html)
    # srcset="a.png 1x, b.png 2x"
    def sub_srcset(m):
        parts = []
        for seg in m.group(2).split(","):
            seg = seg.strip()
            if not seg:
                continue
            bits = seg.split(None, 1)
            url = bits[0]
            if url.startswith("/") and not url.startswith(BASE):
                url = BASE.rstrip("/") + url
            parts.append(url + ((" " + bits[1]) if len(bits) > 1 else ""))
        return f'{m.group(1)}="{", ".join(parts)}"'

    html = re.sub(r'\b(srcset)=(["\'])([^"\']+)\2', sub_srcset, html)
    return html


def convert(src, dst):
    if not os.path.isdir(src):
        raise SystemExit(f"源目录不存在：{src}")

    os.makedirs(dst, exist_ok=True)
    html_count = 0
    asset_count = 0
    rewritten = 0

    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel = os.path.relpath(root, src)
        target_dir = dst if rel == "." else os.path.join(dst, rel)
        os.makedirs(target_dir, exist_ok=True)

        for name in files:
            if name in SKIP_NAMES:
                continue
            s = os.path.join(root, name)
            d = os.path.join(target_dir, name)

            if name.endswith(".html"):
                with open(s, encoding="utf-8", errors="replace") as fh:
                    html = fh.read()
                new_html = rewrite(html)
                if new_html != html:
                    rewritten += 1
                # 旧的 <base> 注入若已存在则移除，避免与改写后的绝对路径混淆
                new_html = re.sub(r'\n?\s*<base\s+href="[^"]*"\s*/?>', "", new_html, flags=re.I)
                with open(d, "w", encoding="utf-8") as fh:
                    fh.write(new_html)
                html_count += 1
            else:
                with open(s, "rb") as fsrc, open(d, "wb") as fdst:
                    fdst.write(fsrc.read())
                asset_count += 1

    # Pages 需要 .nojekyll，避免 Jekyll 把站点内的模板语法当 Liquid 解析
    open(os.path.join(dst, ".nojekyll"), "w").close()

    print(f"源目录  {src}")
    print(f"输出到  {dst}")
    print(f"页面 {html_count} 个（改写 {rewritten} 个），资源 {asset_count} 个，前缀 {BASE}")
    print("已写入 .nojekyll")


if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "www")
    b = sys.argv[2] if len(sys.argv) > 2 else os.path.join(REPO, "docs")
    convert(a, b)
