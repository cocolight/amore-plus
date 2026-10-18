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
| 9 | 文章目录（TOC） | feature/post-toc | done | 2 | `post.html` 引用 `partials/toc.html`；文章页渲染出目录节点（`id="toc"` 或 `.toc`），由正文 `h2`/`h3` 标题自动生成锚点且可点击跳转 |
| 10 | Giscus 评论支持 | feature/giscus | done | 6 | `partials/giscus.html` 存在并被 `comments.html` 引用；`src/config.json` 的 `customConfig` 新增 Giscus 设置（`giscusRepo`/`giscusCategory` 等）；启用后页面加载 `giscus.app` 脚本并渲染评论区 |
| 11 | Gitalk 评论支持（Gridea-Pro 适配） | feature/gitalk | planned | 6 | `comments.html` 的 Gitalk 分支大小写修正为 `'Gitalk'`（与 `'Giscus'` 一致）；`partials/gitalk.html` 数据源由已失效的 `commentSetting.gitalkSetting.*` 子对象改为 Gridea-Pro 扁平化后的 `commentSetting` 顶层字段（`clientId`/`clientSecret`/`repository`/`owner`，具体字段名以 Gridea-Pro 渲染注入为准）；本地 Gridea-Pro 选 Gitalk 后评论区正常渲染 |
| 12 | Disqus 评论支持（Gridea-Pro 适配） | feature/disqus | planned | 6 | `comments.html` 的 Disqus 分支大小写修正为 `'Disqus'`（与 `'Giscus'` 一致）；`partials/disqus.html` 数据源由已失效的 `commentSetting.disqusSetting.*` 子对象改为 Gridea-Pro 扁平化后的 `commentSetting` 顶层字段（`shortname`/`apikey`/`api`，具体字段名以 Gridea-Pro 渲染注入为准）；本地 Gridea-Pro 选 Disqus 后评论区正常渲染 |
| 13 | Valine 评论支持（Gridea-Pro 适配） | feature/valine | planned | 6 | `comments.html` 的 Valine 分支已为 `'Valine'`（与 Gridea-Pro 一致，无需改大小写）；`partials/valine.html` 数据源 `commentSetting.appId`/`appKey`/`serverURLs` 须与 Gridea-Pro 实际注入字段核对（若注入为 `commentSetting.valineSetting.*` 层则改读对应层，保留 `theme_config` 兜底）；`valine.html` 硬编码的博主昵称 `MASTER_NICK`（当前 `"Amore"`）改为与站点名一致或模板变量；本地 Gridea-Pro 选 Valine 后评论区正常渲染 |
| 14 | Waline 评论支持（Gridea-Pro 适配） | feature/waline | planned | 6 | `comments.html` 的 Waline 分支已为 `'Waline'`（与 Gridea-Pro 一致，无需改大小写）；`partials/waline.html` 数据源 `commentSetting.serverURLs` 须与 Gridea-Pro 实际注入字段核对（若注入为 `commentSetting.walineSetting.*` 层则改读对应层，保留 `theme_config` 兜底）；本地 Gridea-Pro 选 Waline 后评论区正常渲染 |
| 15 | 阅读进度改为顶部细线 | feature/reading-progress-top | planned | 2 | 将 `partials/reading-progress.html` 由右侧 SVG 圆环浮窗（含「阅读进度」「0%」文字）改为页面顶部一根细线：`main.css` 加固定置顶样式（`position: fixed; top: 0; left: 0; width: 100%; height` 极小，约 3–4px，深色模式仍可见）；细线颜色用淡蓝或淡绿（具体色值实现时定，可复用站点强调色）；进度以「填充宽度 0→100%」表示（如 `transform: scaleX(p)` 或 width 百分比），无文字标签；`partials/scripts.html` 滚动逻辑改为更新细线宽度而非 SVG 圆环；本地 Gridea-Pro 渲染验证：滚动时细线从 0 逐渐填满、置顶且不遮挡正文 |
| 16 | 目录随动与高亮鲁棒性优化 | feature/toc-scroll-sync | in-progress | 9 | `partials/scripts.html` 的 TOC 高亮逻辑由「固定 100px 阈值 + `activeIndex` 初值 0」改为按「阅读线」（视口高度约 20%–25%）判定当前章节：① 滚动到第一个 `h2`/`h3` 之前时不高亮任何项（原实现因 `activeIndex` 初值为 0 会错误高亮首项，表现为目录「不随动」）；② 滚到页面底部、末章节距文档末尾不足阈值高度时强制高亮最后一项（避免末项永远无法激活）；③ scroll 监听改用 `requestAnimationFrame` 节流，并补 `resize` 重算（现有实现每次 scroll 都遍历全部标题读 `getBoundingClientRect()`，长文章易掉帧，且窗口尺寸变化后判定失效）；本地 Gridea-Pro 验证：文章开头目录无高亮、逐段滚动高亮跟随当前章节、滚到底部高亮停在末项、调整窗口尺寸后仍正确 |
