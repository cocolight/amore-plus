#!/usr/bin/env python3
"""
生成 amore-plus 主题的演示站点。

页面的 DOM 结构与类名取自 src/templates/ 下的真实模板，样式直接复用
src/assets/styles/main.css，因此演示站与主题实际渲染结果一致。

数据为示例内容，用于展示主题各页面在真实内容下的表现。
"""
import html
import json
import os
import shutil
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.normpath(os.path.join(ROOT, "..", "src"))

SITE = {
    "name": "amore-plus 演示站",
    "description": "示例站点，用于展示 amore-plus 主题的各页面与特性。内容均为示例数据。",
    "location": "中国 · 深圳",
    "quoteText": "最顶级的人才喜欢一起工作，而且他们是不能容忍平庸作品的。",
    "quoteAuthor": "史蒂夫 · 乔布斯",
    "footerInfo": "Powered by Gridea-Pro · 主题 <a href=\"https://github.com/cocolight/amore-plus\">amore-plus</a>",
    "domain": "cocolight.github.io/amore-plus",
}

MENUS = [
    ("首页", "index.html"),
    ("博客", "blog.html"),
    ("闪念", "memos.html"),
    ("归档", "archives.html"),
    ("分类", "categories.html"),
    ("标签", "tags.html"),
    ("友链", "links.html"),
    ("关于", "about.html"),
]

SOCIALS = [
    ("ri-github-line", "https://github.com/cocolight", "GitHub"),
    ("ri-twitter-line", "https://twitter.com/", "Twitter"),
    ("ri-weibo-line", "https://weibo.com/", "微博"),
    ("ri-zhihu-line", "https://www.zhihu.com/", "知乎"),
]

CATEGORIES = [
    {"name": "使用指南", "slug": "guide", "desc": "主题的安装、配置与使用说明。"},
    {"name": "技术笔记", "slug": "tech", "desc": "开发过程中遇到的问题与解法。"},
    {"name": "随笔", "slug": "essay", "desc": "不成体系的记录与思考。"},
]

TAGS = ["Gridea-Pro", "Pongo2", "前端", "主题", "GitHub", "折腾"]

# ---------------------------------------------------------------- 示例文章

POSTS = [
    {
        "title": "如何使用 amore-plus 主题",
        "slug": "how-to-use-amore-plus",
        "date": "2026-10-18",
        "cats": ["使用指南"],
        "tags": ["Gridea-Pro", "主题"],
        "top": True,
        "body": """
<blockquote>
<p>amore-plus 是一款面向 <strong>Gridea-Pro</strong> 的极简博客主题，聚焦阅读体验。无独立构建与运行时，由宿主平台在渲染期生成静态页面。</p>
</blockquote>

<h2 id="install">一、安装与启用</h2>
<p>本主题是纯静态资源，无运行时依赖。将 <code>src/</code> 目录复制到 Gridea-Pro 的主题目录即可：</p>
<pre><code># Linux / macOS
cp -r src ~/文档/blog_data/themes/amore-plus

# Windows（PowerShell）
Copy-Item -Recurse src "$env:USERPROFILE\\Documents\\Gridea Pro\\themes\\amore-plus"</code></pre>
<p>随后在 Gridea-Pro 客户端「主题」中启用 <code>amore-plus</code>，并在主题设置面板中填写各项配置。</p>

<h2 id="settings">二、主题设置</h2>
<p>主题提供 <strong>25 项</strong>可配置项，集中在 <code>config.json</code> 的 <code>customConfig</code>，按分组呈现：</p>
<table>
<thead><tr><th>分组</th><th>包含项</th></tr></thead>
<tbody>
<tr><td>基础设置</td><td>站点 Logo、站点图标、页脚信息</td></tr>
<tr><td>首页信息</td><td>地理位置、格言内容、格言作者</td></tr>
<tr><td>外观设置</td><td>默认主题（深色 / 浅色）、主题强调色</td></tr>
<tr><td>社交链接</td><td>GitHub、Twitter、微博、知乎、Facebook</td></tr>
<tr><td>统计分析</td><td>Google Analytics 跟踪 ID</td></tr>
<tr><td>Giscus 评论</td><td>仓库、repoId、分类、映射方式等 9 项</td></tr>
<tr><td>高级设置</td><td>自定义 CSS、自定义 JavaScript</td></tr>
</tbody>
</table>

<h3 id="accent">2.1 强调色如何生效</h3>
<p>「主题强调色」会影响链接、按钮、目录高亮条与顶部进度线。你可以在页面右上角切换明暗主题，观察颜色与对比度的变化。</p>

<h2 id="features">三、主要功能</h2>

<h3 id="toc">3.1 文章目录（TOC）</h3>
<p>正文中的 <code>h2</code> / <code>h3</code> 会被自动提取为右侧目录，点击可平滑跳转。滚动页面时目录会自动高亮当前章节并跟随滚动，无需手动翻动。</p>
<p>若某篇文章不含标题，目录会自动隐藏，不留空壳。</p>

<h3 id="progress">3.2 阅读进度</h3>
<p>页面顶部有一根细线（3px），颜色跟随强调色，随阅读进度从 0% 逐渐填充至满宽，不使用任何文字。</p>

<h3 id="theme">3.3 明暗双主题</h3>
<p>访客首次访问按「默认主题」设置显示；切换后的选择会记在浏览器本地，下次访问保持一致。</p>

<h3 id="memos">3.4 闪念与热力图</h3>
<p>支持短内容记录（memos），并以 GitHub 风格贡献热力图呈现，列表采用客户端分页。</p>

<h3 id="comments">3.5 评论系统</h3>
<p>支持 Giscus、Gitalk、Valine、Waline、Disqus 五套系统。为避免干扰阅读，闪念 / 友链 / 关于页不显示评论区。</p>

<h2 id="notes">四、使用须知</h2>
<p>本主题的模板使用 <strong>Pongo2（Django 风格）</strong> 方言，不是标准 Jinja2：</p>
<ul>
<li>默认值过滤器为 <code>{{ x|default:"" }}</code>（冒号语法，不接受第二个参数）</li>
<li>循环下标使用 <code>forloop.Counter0</code> 而非 <code>loop.index</code></li>
<li>向 JavaScript 字符串插值时，请加上 <code>|escapejs</code></li>
</ul>

<h2 id="links">五、获取主题</h2>
<p><a href="https://github.com/cocolight/amore-plus">GitHub 仓库：cocolight/amore-plus</a></p>
""",
    },
    {
        "title": "Pongo2 模板方言踩坑记录",
        "slug": "pongo2-dialect-notes",
        "date": "2026-10-18",
        "cats": ["技术笔记"],
        "tags": ["Pongo2", "Gridea-Pro", "前端"],
        "body": """
<p>Gridea-Pro 的模板引擎是 <strong>Pongo2</strong>，采用 Django 风格方言，并非标准 Jinja2。两者在过滤器语法上的差异足以让整页渲染静默失败。</p>

<h2 id="diff">语法差异</h2>
<h3 id="diff-default">1. 默认值过滤器</h3>
<p>正确的 Django 风格写法使用冒号：</p>
<pre><code>{{ theme_config.defaultTheme|default:"" }}</code></pre>
<p>而 Jinja2 风格的括号写法在此引擎下不被支持：</p>
<pre><code>{{ theme_config.defaultTheme|default('', true) }}</code></pre>

<h3 id="diff-loop">2. 循环下标</h3>
<p>循环变量使用 <code>forloop.Counter0</code>（从 0 开始），与 Jinja2 的 <code>loop.index</code> 不同。</p>

<h3 id="diff-escape">3. JavaScript 插值</h3>
<p>向 JS 字符串插值时需加 <code>|escapejs</code>，否则站点名中的引号或反斜杠会破坏脚本。</p>

<h2 id="fallback">失败的表现</h2>
<p>模板编译失败时不会抛出可见异常，而是整页降级为一个兜底页面，顶部显示「⚠️ 降级视图」提示。排查方向应是检查最近改动过的模板语法。</p>

<h2 id="verify">验证方式</h2>
<p>静态检查工具无法发现这类问题。唯一可靠的验证是重新构建后检查产物中降级提示的数量：</p>
<pre><code>grep -c "降级视图" output/post/&lt;slug&gt;/index.html   # 必须为 0</code></pre>
""",
    },
    {
        "title": "长目录文章的目录跟随交互",
        "slug": "toc-scroll-follow",
        "date": "2026-10-17",
        "cats": ["使用指南"],
        "tags": ["前端", "主题"],
        "body": """
<p>当一篇文章的章节较多时，右侧目录本身也会超出可视高度，需要随文章滚动同步跟随。</p>

<h2 id="problem">问题</h2>
<p>假设目录有 100 项，而面板高度只能显示 20 项。读者滚动到第 21、22 项时，若目录不动，就只能手动翻目录才能看到当前章节。</p>

<h2 id="solution">实现</h2>
<h3 id="solution-center">1. 焦点保持居中</h3>
<p>焦点项变化时，把面板滚动到使其位于面板中心高度。计算方式为焦点项中心与面板中心的偏差：</p>
<pre><code>delta = (linkCenter - panelCenter)
panel.scrollTop += delta</code></pre>

<h3 id="solution-instant">2. 近距瞬时，远距平滑</h3>
<p>逐节滚动多为小幅移动，采用瞬时定位更跟手；点击目录跳转多为大幅移动，采用平滑滚动更自然。阈值取 120px。</p>

<h3 id="solution-yield">3. 手动操作让位</h3>
<p>用户主动翻目录时暂停自动跟随，文章再次滚动即恢复。</p>

<h2 id="caution">一个必须避开的陷阱</h2>
<p>不能用 <code>element.scrollIntoView({block:'center'})</code>。它会连带滚动外层页面，把正文顶走。必须手动计算容器的 <code>scrollTop</code>。</p>

<h2 id="extra">其他细节</h2>
<h3 id="extra-gutter">滚动条留白</h3>
<p>面板需设置 <code>overscroll-behavior: contain</code>，避免翻到边缘时连带滚动正文。</p>
<h3 id="extra-short">短目录不处理</h3>
<p>当面板内容未溢出时不执行任何滚动逻辑，零开销。</p>
""",
    },
    {
        "title": "为什么选择极简的阅读界面",
        "slug": "why-minimal-reading",
        "date": "2026-10-16",
        "cats": ["随笔"],
        "tags": ["主题"],
        "body": """
<p>做这个主题时反复考虑过要不要加侧边栏、要不要放相关阅读、要不要做进度百分比数字。最后几乎都去掉了。</p>

<h2 id="keep">保留了什么</h2>
<p>与阅读直接相关的：明暗切换、目录、进度提示。其余一律不加。</p>

<h2 id="drop">去掉了什么</h2>
<h3 id="drop-number">1. 进度百分比数字</h3>
<p>数字本身不增加信息量。顶部一根线已经能表达同样的事，且不打断阅读节奏。</p>
<h3 id="drop-related">2. 相关阅读</h3>
<p>读者往下滚通常是为了继续读，不是为了跳走。把相关内容放在页面底部已足够。</p>

<h2 id="principle">取舍标准</h2>
<p>判断标准是：这个东西的存在，是否让读者更容易读到下一段。如果答案不明确，就不加。</p>
""",
    },
    {
        "title": "用 Gridea-Pro 写博客的日常流程",
        "slug": "gridea-daily-workflow",
        "date": "2026-10-15",
        "cats": ["技术笔记"],
        "tags": ["Gridea-Pro", "GitHub"],
        "body": """
<p>记录一下当前的写作与发布流程，便于日后回溯。</p>

<h2 id="write">写作</h2>
<p>文章以 Markdown 保存在本地数据目录，Gridea 在构建时渲染为静态页面。修改主题只需覆盖主题目录下的 <code>src/</code>，无需重启。</p>

<h2 id="preview">预览与验证</h2>
<p>本地预览默认在 <code>127.0.0.1:6606</code>。每次改完模板后重新构建，检查目标页是否出现降级提示。</p>
<pre><code>curl -s http://127.0.0.1:6606/post/&lt;slug&gt;/ | grep -c "降级视图"   # 应为 0</code></pre>

<h2 id="deploy">发布</h2>
<p>构建产物推送到 GitHub Pages 仓库，由 Pages 完成托管与分发。</p>

<h2 id="sync">仓库同步</h2>
<p>主题源码另有一个独立仓库。改动主题后需同步两处，否则线上与仓库会不一致。</p>
""",
    },
]

MEMOS = [
    ("2026-10-18", "把目录面板的跟随逻辑加了手动让位，用户翻目录时不再被抢回控制权。"),
    ("2026-10-18", "强调色改成跟随站点设置，链接和高亮条会一起变。"),
    ("2026-10-17", "评论区右侧贴边的问题，最后靠容器缩进解决，不是 CSS 规则缺失。"),
    ("2026-10-17", "Pongo2 的 default 过滤器用冒号，写成 Jinja2 风格会整页降级。"),
    ("2026-10-16", "把阅读进度从右侧圆环改成顶部细线，去掉了百分比数字。"),
    ("2026-10-15", "giscus 的 client.js 要放在容器内，否则 iframe 注不进去。"),
    ("2026-10-14", "闪念页、友链页、关于页本来都无条件引入评论区，需要去掉。"),
    ("2026-10-13", "长文章的目录要能自己滚动，否则读者得手动翻。"),
]

LINKS = [
    ("Gridea 官方主题仓库", "https://github.com/Gridea-Pro/gridea-pro-themes", "社区主题集合"),
    ("Gridea-Pro", "https://github.com/Gridea-Pro/gridea-pro", "静态博客生成器"),
    ("Pongo2", "https://github.com/flosch/pongo2", "Django 风格的 Go 模板引擎"),
    ("GitHub Pages", "https://pages.github.com/", "静态站点托管"),
]

ABOUT_BODY = """
<p>这是一个用于演示 <strong>amore-plus</strong> 主题的示例站点，所有内容均为示例数据。</p>

<h2 id="about-theme">关于主题</h2>
<p>amore-plus 是一款面向 Gridea-Pro 的极简博客主题，聚焦阅读体验。无独立构建与运行时，由宿主平台在渲染期生成静态页面。</p>
<ul>
<li>文章目录（TOC）：自动锚点、滚动高亮、长目录面板跟随</li>
<li>阅读进度：页面顶部细线，颜色跟随强调色</li>
<li>明暗双主题与可配强调色</li>
<li>闪念与 GitHub 风格热力图</li>
<li>五套评论系统适配</li>
</ul>

<h2 id="about-data">关于示例数据</h2>
<p>本站的文章、闪念、友链与统计信息均为演示用途，不代表真实内容。</p>

<h2 id="about-source">源码与更新</h2>
<p><a href="https://github.com/cocolight/amore-plus">https://github.com/cocolight/amore-plus</a></p>
"""

# ---------------------------------------------------------------- 模板片段

LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#28df99"/>
      <stop offset="100%" stop-color="#ef3982"/>
    </linearGradient>
  </defs>
  <circle cx="60" cy="60" r="52" fill="url(#g)"/>
  <text x="60" y="76" font-family="Segoe UI, PingFang SC, sans-serif" font-size="46" font-weight="bold"
        fill="#ffffff" text-anchor="middle">a+</text>
</svg>
"""


def esc(s):
    return html.escape(str(s), quote=True)


def head(title, body_class="", desc="", prefix="./"):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)} | {esc(SITE['name'])}</title>
<meta name="description" content="{esc(desc or SITE['description'])}">
<link rel="stylesheet" href="{prefix}assets/styles/main.css">
<link rel="stylesheet" href="{prefix}assets/styles/icons.css">
</head>
<body class="{body_class}">
<script>
(function () {{
    var saved = localStorage.getItem('theme');
    var theme = saved || 'light';
    if (theme === 'dark') {{ document.body.classList.add('dark-theme'); }}
}})();
</script>
"""


TOGGLE_BTN = """<span>
  <button id="theme-toggle-sun" class="tiptap-button theme-toggle-sun" aria-label="Switch to dark mode" onclick="toggleTheme()"><svg width="18" height="18" class="tiptap-button-icon" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="5" fill="currentColor"></circle><path d="M12 1C12.5523 1 13 1.44772 13 2V4C13 4.55228 12.5523 5 12 5C11.4477 5 11 4.55228 11 4V2C11 1.44772 11.4477 1 12 1Z" fill="currentColor"></path><path d="M12 19C12.5523 19 13 19.4477 13 20V22C13 22.5523 12.5523 23 12 23C11.4477 23 11 22.5523 11 22V20C11 19.4477 11.4477 19 12 19Z" fill="currentColor"></path><path d="M1 12C1 11.4477 1.44772 11 2 11H4C4.55228 11 5 11.4477 5 12C5 12.5523 4.55228 13 4 13H2C1.44772 13 1 12.5523 1 12Z" fill="currentColor"></path><path d="M20 11C19.4477 11 19 11.4477 19 12C19 12.5523 19.5523 13 20 13H22C22.5523 13 23 12.5523 23 12C23 11.4477 22.5523 11 22 11H20Z" fill="currentColor"></path></svg></button>
  <button id="theme-toggle-moon" class="tiptap-button theme-toggle-moon" aria-label="Switch to light mode" onclick="toggleTheme()"><svg width="18" height="18" class="tiptap-button-icon" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C10.0222 2 8.08879 2.58649 6.4443 3.6853C4.79981 4.78412 3.51809 6.3459 2.76121 8.17317C2.00433 10.0004 1.8063 12.0111 2.19215 13.9509C2.578 15.8907 3.53041 17.6725 4.92894 19.0711C6.32746 20.4696 8.10929 21.422 10.0491 21.8079C11.9889 22.1937 13.9996 21.9957 15.8268 21.2388C17.6541 20.4819 19.2159 19.2002 20.3147 17.5557C21.4135 15.9112 22 13.9778 22 12C22 11.5955 21.7564 11.2309 21.3827 11.0761C21.009 10.9213 20.5789 11.0069 20.2929 11.2929C19.287 12.2988 17.9226 12.864 16.5 12.864C15.0774 12.864 13.713 12.2988 12.7071 11.2929C11.7012 10.287 11.136 8.92261 11.136 7.5C11.136 6.07739 11.7012 4.71304 12.7071 3.70711C12.9931 3.42111 13.0787 2.99099 12.9239 2.61732C12.7691 2.24364 12.4045 2 12 2ZM7.55544 5.34824C8.27036 4.87055 9.05353 4.51389 9.87357 4.28778C9.39271 5.27979 9.13604 6.37666 9.13604 7.5C9.13604 9.45304 9.91189 11.3261 11.2929 12.7071C12.6739 14.0881 14.547 14.864 16.5 14.864C17.6233 14.864 18.7202 14.6073 19.7122 14.1264C19.4861 14.9465 19.1295 15.7296 18.6518 16.4446C17.7727 17.7602 16.5233 18.7855 15.0615 19.391C13.5997 19.9965 11.9911 20.155 10.4393 19.8463C8.88743 19.5376 7.46197 18.7757 6.34315 17.6569C5.21447 16.538 4.4624 15.1126 4.15372 13.5607C3.84504 12.0089 4.00347 10.4003 4.60897 8.93853C5.21447 7.47672 6.23985 6.22729 7.55544 5.34824Z" fill="currentColor"></path></svg></button>
</span>"""


def header(prefix="./"):
    menu = " · ".join(
        f'<a class="menu-item" href="{prefix}{link}">{esc(name)}</a>' for name, link in MENUS
    )
    return f"""<header class="mod-head">
<div class="mod-head__left"><div class="mod-head__logo">
<a href="{prefix}index.html"><img class="avatar" alt="avatar" src="{prefix}assets/media/logo.svg"></a>
</div></div>
<div class="mod-head__right">
{TOGGLE_BTN}
<div class="menu links">{menu}</div>
</div>
</header>"""


def footer(prefix="./"):
    menu = " · ".join(
        f'<a class="menu-item" href="{prefix}{link}">{esc(name)}</a>' for name, link in MENUS
    )
    return f"""<footer id="footer" class="footer">
<nav>{menu}</nav>
<div class="Copyright">Copyright &copy; <span class="current-year"></span> {esc(SITE['name'])}</div>
<div class="index_footer">{SITE['footerInfo']} · <a class="rss" href="#">RSS</a></div>
</footer>
<script>document.querySelector('.current-year').textContent = new Date().getFullYear();</script>"""


def progress_bar():
    return """<div class="reading-progress-bar" role="progressbar" aria-label="阅读进度" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">
<div class="reading-progress-bar__fill"></div>
</div>"""


def toc_aside():
    return """<aside class="toc-aside" id="toc" aria-label="文章目录">
<div class="toc-title">目录</div>
<nav class="toc-nav"><ul class="toc-list"></ul></nav>
</aside>"""


SITE_JS = """
function toggleTheme() {
  var body = document.getElementsByTagName('body')[0];
  if (body.classList.contains('dark-theme')) {
    body.classList.remove('dark-theme');
    localStorage.setItem('theme','light');
  } else {
    body.classList.add('dark-theme');
    localStorage.setItem('theme','dark');
  }
}
"""


def tail(extra=""):
    return f"<script>{SITE_JS}{extra}</script>\n</body>\n</html>\n"


PROGRESS_JS = """
(function(){
  var bar=document.querySelector('.reading-progress-bar'), fill=document.querySelector('.reading-progress-bar__fill');
  if(!bar||!fill) return;
  var ticking=false,last=-1;
  function set(r){ r=Math.min(1,Math.max(0,r)); if(Math.abs(r-last)<0.001) return; last=r;
    fill.style.transform='scaleX('+r+')'; bar.setAttribute('aria-valuenow',String(Math.round(r*100))); }
  function update(){ var se=document.scrollingElement||document.documentElement;
    var s=se.scrollHeight-window.innerHeight; set(s<=0?0:se.scrollTop/s); }
  function on(){ if(ticking) return; ticking=true; window.requestAnimationFrame(function(){update();ticking=false;}); }
  update(); window.addEventListener('scroll',on,{passive:true}); window.addEventListener('resize',on);
})();
"""

TOC_JS = """
(function(){
  var content=document.querySelector('.mod-post__entry'), list=document.querySelector('.toc-list'), aside=document.getElementById('toc');
  if(!content||!list||!aside) return;
  var hs=content.querySelectorAll('h2, h3');
  if(hs.length===0){ aside.style.display='none'; return; }
  var links=[];
  hs.forEach(function(h,i){ if(!h.id) h.id='toc-heading-'+i;
    var lv=h.tagName.toLowerCase()==='h3'?'toc-h3':'';
    var li=document.createElement('li'), a=document.createElement('a');
    a.href='#'+h.id; a.className='toc-link '+lv; a.textContent=h.textContent.trim();
    li.appendChild(a); list.appendChild(li); links.push(a); });
  var panel=aside, TH=120, userScrolled=false, active=-1, ticking=false;
  panel.addEventListener('wheel',function(){userScrolled=true;},{passive:true});
  function line(){ return Math.max(80, Math.round(window.innerHeight*0.22)); }
  function update(){ var L=line(), next=-1;
    hs.forEach(function(h,i){ if(h.getBoundingClientRect().top<=L) next=i; });
    var se=document.scrollingElement||document.documentElement;
    if(se.scrollTop+window.innerHeight>=se.scrollHeight-2) next=hs.length-1;
    if(next===active) return; active=next;
    links.forEach(function(l,i){ l.classList.toggle('active', i===active); }); }
  function follow(){ if(userScrolled||active<0) return;
    if(panel.scrollHeight<=panel.clientHeight) return;
    var lk=links[active]; if(!lk) return;
    var lr=lk.getBoundingClientRect(), pr=panel.getBoundingClientRect();
    var d=(lr.top+lr.height/2)-(pr.top+panel.clientHeight/2);
    var max=panel.scrollHeight-panel.clientHeight;
    var t=Math.max(0,Math.min(panel.scrollTop+d,max)), dist=t-panel.scrollTop;
    if(Math.abs(dist)<1) return;
    if(Math.abs(dist)<=TH) panel.scrollTop=t; else panel.scrollTo({top:t,behavior:'smooth'}); }
  function on(){ if(ticking) return; ticking=true;
    window.requestAnimationFrame(function(){ update(); follow(); ticking=false; }); }
  update(); follow();
  window.addEventListener('scroll',function(){ userScrolled=false; on(); },{passive:true});
  window.addEventListener('resize',on); window.addEventListener('hashchange',on);
})();
"""

# ---------------------------------------------------------------- 页面生成


def page_index():
    socials = "".join(
        f'<a href="{esc(u)}" target="_blank" rel="noopener" aria-label="{esc(name)}"><i class="{esc(ic)}"></i></a>'
        for ic, u, name in SOCIALS
    )
    menu = " · ".join(
        f'<a class="menu-item" href="{l}">{esc(n)}</a>' for n, l in MENUS
    )
    latest = POSTS[0]
    return head(SITE["name"], desc=SITE["description"]) + f"""<div class="wrapper">
<div class="main">
<div class="mod-index__logo"><a href="index.html"><img class="mod-index__logo" alt="avatar" src="./assets/media/logo.svg"></a></div>
<div class="container">
<div class="intro" style="line-height: 50px">
<h1 class="nickname">{esc(SITE['name'])}</h1>
<div class="description"><p>{esc(SITE['description'])}</p></div>
<div class="zuobiao"><i class="ico_map"></i>
{esc(SITE['location'])}
<span style="margin-left: 30px">{TOGGLE_BTN}</span>
</div><br>
<div style="line-height: 20px;font-size: 10pt;">
<p>" {esc(SITE['quoteText'])} "</p>
<p style="margin-left: 8rem;font-size: 8pt;">—— {esc(SITE['quoteAuthor'])}</p>
</div><br>
<div class="menu links">{menu}</div>
<div class="social-container">{socials}</div>
</div>
</div>
<footer id="footer" class="index_footer">
{SITE['footerInfo']} · <a class="rss" href="#"><i class="ri-rss-line"></i> RSS</a>
</footer>
</div>
</div>""" + tail()


def _post_list(items, prefix="./"):
    lis = "".join(
        f'<li class="post-item"><time class="mod-archive__time" datetime="{p["date"]}">{p["date"]}</time> '
        f'<span>&nbsp;&nbsp;&nbsp;</span><a href="{prefix}post/{p["slug"]}/index.html">'
        f'{"[置顶] " if p.get("top") else ""}{esc(p["title"])}</a></li>'
        for p in items
    )
    return f'<article class="mod-archive"><div class="mod-archive__item"><ul class="mod-archive__list">{lis}</ul></div></article>'


def page_blog():
    return (
        head("博客", desc="文章列表")
        + header()
        + _post_list(POSTS)
        + footer()
        + tail()
    )


def page_archives():
    years = {}
    for p in POSTS:
        years.setdefault(p["date"][:4], []).append(p)
    blocks = []
    for y in sorted(years, reverse=True):
        items = "".join(
            f'<li class="post-item"><time class="mod-archive__time" datetime="{p["date"]}">{p["date"]}</time> '
            f'<span>&nbsp;&nbsp;&nbsp;</span><a href="post/{p["slug"]}/index.html">{esc(p["title"])}</a></li>'
            for p in years[y]
        )
        blocks.append(
            f'<div class="mod-archive__item"><div class="mod-archive__year">{y}</div>'
            f'<ul class="mod-archive__list">{items}</ul></div>'
        )
    return (
        head("归档", desc="文章归档")
        + header()
        + f'<article class="mod-archive">{"".join(blocks)}</article>'
        + footer()
        + tail()
    )


def page_categories():
    items = "".join(
        f'<li class="post-item"><a href="category/{c["slug"]}/index.html">{esc(c["name"])}</a>'
        f'<span style="color: var(--text-muted);"> · {len([p for p in POSTS if c["name"] in p["cats"]])} 篇</span>'
        f'<div style="font-size: 10pt;color: var(--text-muted);">{esc(c["desc"])}</div></li>'
        for c in CATEGORIES
    )
    return (
        head("分类", desc="文章分类")
        + header()
        + f'<article class="mod-archive"><div class="mod-archive__item"><ul class="mod-archive__list">{items}</ul></div></article>'
        + footer()
        + tail()
    )


def page_tags():
    items = "".join(
        f'<li class="post-item"><a href="tag/{t}/index.html">{esc(t)}</a>'
        f'<span style="color: var(--text-muted);"> · {len([p for p in POSTS if t in p["tags"]])} 篇</span></li>'
        for t in TAGS
    )
    return (
        head("标签", desc="文章标签")
        + header()
        + f'<article class="mod-archive"><div class="mod-archive__item"><ul class="mod-archive__list">{items}</ul></div></article>'
        + footer()
        + tail()
    )


def page_links():
    items = "".join(
        f'<li><a href="{esc(u)}" target="_blank" rel="noopener" title="{esc(d)}">{esc(n)}</a>'
        f'<div style="font-size: 10pt;color: var(--text-muted);">{esc(d)}</div></li>'
        for n, u, d in LINKS
    )
    return (
        head("友链", desc="友情链接")
        + header()
        + f"""<article class="mod-post mod-post__type-post">
<header><h1 class="mod-post__title">友链</h1></header>
<div class="mod-post__entry wzulli">
<ul class="links-list">{items}</ul>
</div>
</article>"""
        + footer()
        + tail()
    )


def page_about():
    return (
        head("关于", desc="关于本站")
        + header()
        + f"""<article class="mod-post mod-post__type-post">
<header><h1 class="mod-post__title">关于</h1></header>
<div class="mod-post__entry wzulli">{ABOUT_BODY}
</div>
</article>"""
        + footer()
        + tail()
    )


def page_404():
    return (
        head("页面不存在")
        + header()
        + """<article class="mod-post mod-post__type-post">
<header><h1 class="mod-post__title">404</h1></header>
<div class="mod-post__entry wzulli">
<p>页面不存在或已被移动。</p>
<p><a href="index.html">返回首页</a></p>
</div>
</article>"""
        + footer()
        + tail()
    )


def page_memos():
    items = "".join(
        f'<li><time>{esc(d)}</time><p>{esc(t)}</p></li>' for d, t in MEMOS
    )
    # 贡献热力图：近 26 周的示例贡献
    cells = []
    for w in range(26):
        for d in range(7):
            lvl = (w * 7 + d) % 5
            cells.append(f'<td class="heat-{lvl}"></td>')
    rows = []
    for w in range(0, len(cells), 7):
        rows.append("<tr>" + "".join(cells[w:w + 7]) + "</tr>")
    heat = f'<table class="heatmap">{"".join(rows)}</table>'

    return (
        head("闪念", desc="闪念记录")
        + header()
        + f"""<article class="mod-post mod-post__type-post">
<header><h1 class="mod-post__title">闪念</h1></header>
<div class="mod-post__entry wzulli">
<h2>贡献热力图</h2>
{heat}
<h2>最近记录</h2>
<ul class="memos-list">{items}</ul>
</div>
</article>
<style>
.heatmap {{ border-collapse: separate; border-spacing: 3px; }}
.heatmap td {{ width: 12px; height: 12px; border-radius: 2px; background: var(--border-color); }}
.heatmap td.heat-0 {{ background: var(--border-color); }}
.heatmap td.heat-1 {{ background: rgba(40, 223, 153, 0.25); }}
.heatmap td.heat-2 {{ background: rgba(40, 223, 153, 0.45); }}
.heatmap td.heat-3 {{ background: rgba(40, 223, 153, 0.7); }}
.heatmap td.heat-4 {{ background: var(--accent-color); }}
.memos-list {{ list-style: none; padding: 0; }}
.memos-list li {{ border-left: solid 2px var(--accent-color); padding: 2px 0 2px 15px; margin-bottom: 18px; }}
.memos-list time {{ color: var(--text-muted); font-size: 10pt; }}
.memos-list p {{ margin: 4px 0 0 0; }}
</style>"""
        + footer()
        + tail()
    )


def page_post(p):
    # 文章位于 post/<slug>/，深度为 2
    prefix = "../../"
    cats = " · ".join(
        f'<a href="{prefix}category/{[c["slug"] for c in CATEGORIES if c["name"] == n][0]}/index.html" class="mod-post__category">{esc(n)}</a>'
        for n in p["cats"]
    )
    tags = "".join(f'<a href="{prefix}tag/{t}/index.html">{esc(t)}</a>' for t in p["tags"])
    return (
        head(p["title"], body_class="post-page", desc=p["title"], prefix=prefix)
        + header(prefix)
        + progress_bar()
        + f"""<div class="post-layout">
<article class="mod-post mod-post__type-post">
<header><h1 class="mod-post__title">{esc(p['title'])}</h1></header>
<div class="mod-post__meta">
<time datetime="{p['date']}">{p['date']}</time> • 示例文章 • {cats}
</div>
<div class="mod-post__entry wzulli">
{p['body'].strip()}
</div>
</article>
{toc_aside()}
</div>
<div class="mod-post__tags">相关标签：{tags}</div>
"""
        + footer(prefix)
        + tail(PROGRESS_JS + TOC_JS)
    )


def page_category(c):
    items = [p for p in POSTS if c["name"] in p["cats"]]
    return (
        head(c["name"], desc=c["desc"], prefix="../../")
        + header("../../")
        + f"""<article class="mod-post mod-post__type-post">
<header><h1 class="mod-post__title">分类：{esc(c['name'])}</h1></header>
<div class="mod-post__meta">{esc(c['desc'])}</div>
</article>"""
        + _post_list(items, "../../")
        + footer("../../")
        + tail()
    )


def page_tag(t):
    items = [p for p in POSTS if t in p["tags"]]
    return (
        head(t, desc=f"标签：{t}", prefix="../../")
        + header("../../")
        + f"""<article class="mod-post mod-post__type-post">
<header><h1 class="mod-post__title">标签：{esc(t)}</h1></header>
<div class="mod-post__meta">共 {len(items)} 篇</div>
</article>"""
        + _post_list(items, "../../")
        + footer("../../")
        + tail()
    )


def build(out):
    # 只清理由本脚本生成的页面与资源，保留 docs/engineering/ 等其他内容
    KEEP = {"engineering", ".nojekyll"}
    if os.path.isdir(out):
        for name in os.listdir(out):
            if name in KEEP:
                continue
            p = os.path.join(out, name)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    else:
        os.makedirs(out)

    # 样式与图标直接复用主题源文件
    os.makedirs(f"{out}/assets/styles/lib", exist_ok=True)
    os.makedirs(f"{out}/assets/media", exist_ok=True)
    for f in ("main.css", "icons.css"):
        src = f"{THEME}/assets/styles/{f}"
        if os.path.exists(src):
            shutil.copy(src, f"{out}/assets/styles/{f}")
    wf = f"{THEME}/assets/styles/lib/remixicon.woff2"
    if os.path.exists(wf):
        shutil.copy(wf, f"{out}/assets/styles/lib/remixicon.woff2")
    # favicon 与站标沿用主题自带资源
    os.makedirs(f"{out}/assets/media/images", exist_ok=True)
    for f in ("favicon.ico", "zuobiao.svg"):
        src = f"{THEME}/assets/media/images/{f}"
        if os.path.exists(src):
            shutil.copy(src, f"{out}/assets/media/images/{f}")

    # demo 站 logo（仓库自有，不属于主题源码）
    with open(f"{out}/assets/media/logo.svg", "w", encoding="utf-8") as fh:
        fh.write(LOGO_SVG)

    def w(rel, content):
        path = f"{out}/{rel}"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)

    w("index.html", page_index())
    w("blog.html", page_blog())
    w("archives.html", page_archives())
    w("categories.html", page_categories())
    w("tags.html", page_tags())
    w("memos.html", page_memos())
    w("links.html", page_links())
    w("about.html", page_about())
    w("404.html", page_404())

    for p in POSTS:
        w(f"post/{p['slug']}/index.html", page_post(p))
    for c in CATEGORIES:
        w(f"category/{c['slug']}/index.html", page_category(c))
    for t in TAGS:
        w(f"tag/{t}/index.html", page_tag(t))

    print(f"生成完成：{out}")
    print(f"页面数：{sum(len(fs) for _, _, fs in os.walk(out))} 个文件")


if __name__ == "__main__":
    import sys

    # 默认输出到 docs/ 根，使 GitHub Pages 根即演示站首页
    build(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "..", "docs"))
