#!/usr/bin/env python3
"""
把 Gridea 构建产物（默认 www/）转成 GitHub Pages 可直接发布的结构。

Gridea 生成的站点使用根绝对路径（/styles/、/post …），适合部署在域名根目录。
仓库的 Pages 挂在 /amore-plus/ 子路径下，因此需要在每个页面插入
<base href="/amore-plus/">，让根绝对路径正确解析。

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


def convert(src, dst):
    if not os.path.isdir(src):
        raise SystemExit(f"源目录不存在：{src}")

    os.makedirs(dst, exist_ok=True)
    html_count = 0
    asset_count = 0

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
                if "<base" not in html:
                    # 插到 <head> 之后，保证优先于后续的相对路径解析
                    html, n = re.subn(
                        r"(<head[^>]*>)",
                        r'\1\n    <base href="' + BASE + '" />',
                        html,
                        count=1,
                        flags=re.I,
                    )
                    if n == 0:
                        raise SystemExit(f"未找到 <head>：{s}")
                with open(d, "w", encoding="utf-8") as fh:
                    fh.write(html)
                html_count += 1
            else:
                with open(s, "rb") as fsrc, open(d, "wb") as fdst:
                    fdst.write(fsrc.read())
                asset_count += 1

    # Pages 需要 .nojekyll，避免 Jekyll 把站点内的模板语法当 Liquid 解析
    open(os.path.join(dst, ".nojekyll"), "w").close()

    print(f"源目录  {src}")
    print(f"输出到  {dst}")
    print(f"页面 {html_count} 个，资源 {asset_count} 个，base 前缀 {BASE}")
    print("已写入 .nojekyll")


if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "www")
    b = sys.argv[2] if len(sys.argv) > 2 else os.path.join(REPO, "docs")
    convert(a, b)
