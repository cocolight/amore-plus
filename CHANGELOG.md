# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 与
[语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Added

- 新增 Giscus 评论支持（基于 GitHub Discussions）：新增 `src/templates/partials/giscus.html`，由 `comments.html` 在 `commentSetting.commentPlatform == 'Giscus'` 时引用；`src/config.json` 的 `customConfig` 新增 9 项 Giscus 设置（仓库 / repoId / 分类 / categoryId / 映射 / 表情回应 / 输入框位置 / 语言 / 主题）；启用后加载 `giscus.app/client.js` 渲染评论区，并对容器宽度与溢出做 CSS 约束 + 容器缩进 + ResizeObserver 防御脚本。
- 首次将主题源码 `src/`（模板 / 样式 / 资源 / `config.json`）纳入版本控制（此前未被提交）。

### Changed

- 补全 AI 约束文档占位：AGENTS.md（§0 项目描述 / §2 常用命令 / §8 单一事实源坐标）、README.md、ROADMAP.md、CONTRIBUTING.md、docs/engineering/architecture.md；明确主题为 Gridea-Pro 兼容静态主题、无独立单元测试、版本号与设置键事实源为 `src/config.json`。
- 修正文档平台表述：将早期误写的「Halo 兼容」更正为「Gridea-Pro 兼容」（主题使用 Jinja2/Pongo2 方言，实际运行于 Gridea-Pro，非 Halo）。

### Fixed

-

### Removed

-
