# amore-plus

> 基于 Jinja2 方言的极简博客主题（Gridea-Pro 兼容），聚焦阅读体验。支持明/暗双主题、阅读进度、闪念热力图与多评论系统接入。

## 功能

- 首页：站点简介、头像/Logo、地理位置、格言、明/暗主题切换、社交链接与 RSS
- 内容页：博客列表、文章页，含阅读进度条
- 导航：归档、分类、标签、友链、关于、404
- 闪念（memos）：时间线列表 + GitHub 风格年热力图 + 客户端分页
- 主题：明/暗双主题（首次按 `defaultTheme`，之后记忆访客选择）、可配强调色
- 评论：Valine / Waline / Gitalk / Disqus，由 `partials/comments.html` 选择接入
- SEO：`global-seo` / `index-seo` 片段；可选 Google Analytics
- 扩展：自定义 CSS / 自定义 JS

## 安装

本主题为纯静态资源，无运行时依赖：

```bash
# 可选：本地做 HTML / 样式静态检查
npm install -g htmlhint prettier stylelint   # 或项目内用 npx 调用
```

## 运行

将 `src/` 整体放入宿主平台（Gridea-Pro）主题目录并启用：

```bash
cp -r src "<GRIDEA_HOME>/themes/amore-plus"
```

随后在 Gridea-Pro 客户端「主题」中启用 `amore-plus`，并在主题设置中填写 `src/config.json` 定义的各项（站点 Logo、地理位置、格言、社交链接等）。

## 测试 / 检查

主题本身无独立单元测试——模板由宿主平台在渲染期解析。本地可做静态结构检查：

```bash
npx htmlhint 'src/templates/**/*.html'      # HTML 结构（模板含平台专有变量，仅查静态结构）
npx prettier --check 'src/**/*.{html,css,js}'
```

功能正确性以「启用主题后各页面可正常渲染」为准。

## 目录结构

- `src/` — 主题源码（模板 + 静态资源 + 设置定义）
  - `src/config.json` — 主题元信息与设置定义（名称/版本/作者/25 项 `customConfig`，含 9 项 Giscus 评论设置），是配置与版本号的唯一事实源
  - `src/templates/` — 页面模板（首页/博客/文章/归档/分类/标签/友链/关于/404/闪念），均 `{% extends "base.html" %}`
  - `src/templates/partials/` — 复用片段：`head` / `header` / `footer` / `scripts` / `comments` / 各评论系统 / `global-seo` / `index-seo` / `reading-progress` 等
  - `src/assets/styles/` — `main.css`、`icons.css`、`lib/remixicon.woff2`
  - `src/assets/lib/` — 第三方脚本（vendored）`Valine.min.js`
  - `src/assets/media/images/` — `favicon.ico`、`avatar.jpg`、`zuobiao.svg`、`preview.png`
- `tests/` — 测试（当前为空；主题无独立单元测试，正确性由宿主平台渲染验证）
- `docs/` — 项目自己的文档（使用指南、参考、教程……）
- `docs/engineering/` — 模板预置的工程协作文档（架构 / 配置 / 完成定义 / 发版 / ADR）
- `scripts/` — 辅助脚本（当前为空）

## 开发约定

- 分支：`main` 为保护分支，功能走 `feature/<名称>`。
- 提交与本地检查：见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE)。
