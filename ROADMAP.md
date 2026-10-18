# amore-plus 功能清单（ROADMAP）

> 状态取值：`planned` / `in-progress` / `done` / `dropped`。
> 「验收标准」须**可判定**（能被命令或明确检查验证），AI 助手据此判断功能是否完成。

| # | 功能 | 分支 | 状态 | 依赖 | 验收标准 |
|---|------|------|------|------|----------|
| 1 | 主题骨架与首页 | feature/theme-base | done | - | `src/templates/index.html` 与 `base.html` 存在且可被宿主平台解析；首页含站点名/简介/社交链接 |
| 2 | 内容页（博客/文章）与阅读进度 | feature/content | done | 1 | `blog.html`/`post.html` 存在；`partials/reading-progress.html` 被引用 |
| 3 | 导航（归档/分类/标签/友链/关于/404） | feature/nav | done | 1 | `archives.html`/`categories.html`/`category.html`/`tags.html`/`tag.html`/`links.html`/`about.html`/`404.html` 均存在 |
| 4 | 闪念与热力图 | feature/memos | done | 1 | `memos.html` 存在；含热力图渲染与每页 20 条分页脚本 |
| 5 | 明/暗双主题与强调色 | feature/theme | done | 1 | `index.html` 主题切换逻辑存在；`config.json` 含 `defaultTheme`/`accentColor` |
| 6 | 评论系统接入 | feature/comments | done | 1 | `partials/comments.html` + `valine`/`waline`/`gitalk`/`disqus` 四套片段存在 |
| 7 | SEO 与统计分析 | feature/seo | done | 1 | `global-seo.html`/`index-seo.html` 存在；`ga` 配置项可注入 GA |
| 8 | 主题设置面板 | feature/settings | done | 1 | `src/config.json` 的 `customConfig` 含 16 项设置定义 |
| 9 | 文章目录（TOC） | feature/post-toc | planned | 2 | `post.html` 引用 `partials/toc.html`；文章页渲染出目录节点（`id="toc"` 或 `.toc`），由正文 `h2`/`h3` 标题自动生成锚点且可点击跳转 |
| 10 | Giscus 评论支持 | feature/giscus | done | 6 | `partials/giscus.html` 存在并被 `comments.html` 引用；`src/config.json` 的 `customConfig` 新增 Giscus 设置（`giscusRepo`/`giscusCategory` 等）；启用后页面加载 `giscus.app` 脚本并渲染评论区 |
