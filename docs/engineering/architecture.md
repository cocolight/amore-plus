# 架构与代码约定

> 项目：amore-plus。本文件说明「代码怎么组织」；
> 「什么时候算完成」见 [definition-of-done.md](definition-of-done.md)。

## 1. 目录结构

- `src/` — 主题源码（模板 + 静态资源 + 设置定义）
  - `src/config.json` — 主题元信息与设置定义（名称/版本/作者/16 项 `customConfig`），是配置与版本号的**唯一事实源**
  - `src/templates/` — 页面模板（首页/博客/文章/归档/分类/标签/友链/关于/404/闪念），均 `{% extends "base.html" %}`
  - `src/templates/partials/` — 复用片段：`head` / `header` / `footer` / `scripts` / `comments` / 各评论系统 / `global-seo` / `index-seo` / `reading-progress` / `post-list` / `post-pagination` / `post-tags`
  - `src/assets/styles/` — `main.css`、`icons.css`、`lib/remixicon.woff2`
  - `src/assets/lib/` — 第三方脚本（vendored）`Valine.min.js`
  - `src/assets/media/images/` — `favicon.ico`、`avatar.jpg`、`zuobiao.svg`、`preview.png`
- `tests/` — 测试（当前为空；主题无独立单元测试，正确性由宿主平台渲染验证）
- `docs/` — 项目文档（使用指南、参考等）
- `docs/engineering/` — 工程协作文档：架构 / 配置 / 完成定义 / 发版 / ADR
- `scripts/` — 辅助脚本（当前为空）

> 本项目是**静态主题**，无编译/打包步骤，也无分层业务代码；「源码」即模板与资源，由宿主平台在渲染期组装。

## 2. 分层与依赖方向

- 依赖方向单向：入口 → 业务逻辑 → 基础设施；底层不得反向依赖上层。
- 纯逻辑与 I/O 分离，便于单元测试（参考示例中把纯函数抽出的做法）。

## 3. 错误处理

主题运行在宿主平台渲染期，没有后端异常体系。统一策略是**缺省值优先 + 条件渲染**，避免空配置导致页面崩溃：

- 设置缺省：所有可选设置经 `|default:'…'` 提供回退值（如 `location` 默认「中国 · 深圳」、格言默认乔布斯语录、`avatar` 缺省回退到 `/media/images/avatar.jpg`）。
- 条件渲染：可选配置片段用 `{% if theme_config.x %}…{% endif %}` 包裹（如 `favicon`、`ga`、`customCss`、`customJs`、各社交链接），缺失即不输出对应 DOM/请求。
- 空数据分支：列表类模板对空集合显式分支（如 `memos.html` 的 `{% if memos and memos|length > 0 %}…{% else %}暂无闪念{% endif %}`）。
- 客户端脚本：JS 先做存在性 / `scrollHeight` 守卫再操作 DOM，避免空节点报错。

## 4. 日志

静态主题无服务端日志入口。约定：

- 调试信息仅通过浏览器 DevTools Console 输出，不进入生产页面。
- 第三方脚本（Valine / Waline 等）的报错交由各自控制台，主题不拦截、不吞没。
- 不向任何日志 / 第三方（GA 除外，且 GA 仅在配置了 `ga` 时加载）输出密钥或个人信息；`customJs` 由站长自行对其内容负责。

## 5. 依赖引入规则

- 新增依赖前先确认标准库无法满足；优先轻量、维护活跃的库。
- 新增依赖须在提交 / PR 说明理由，避免为小功能引入重依赖。

## 6. 密钥管理

- 密钥 / token / 私钥一律用环境变量或仓库外文件；`.env` 不入库。
- 提供 `.env.example` 作为占位示例。
