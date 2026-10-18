# Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 与
[语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Added

- 新增文章目录（TOC）功能：新增 `src/templates/partials/toc.html` 并由 `post.html` 引用；文章页 `body` 加 `post-page` 类（宽度放宽至 1100px），文章与 TOC 包进 `.post-layout` flex 容器，桌面端 TOC 为右侧 sticky 侧栏、≤768px 隐藏；`scripts.html` 新增 TOC 生成脚本：遍历正文 `.mod-post__entry` 的 `h2`/`h3` 自动生成锚点 `toc-heading-N`、渲染目录列表，滚动时高亮当前章节，文章无 `h2`/`h3` 时自动隐藏 TOC（已通过本地 Gridea-Pro 渲染验证）。
- 新增 Giscus 评论支持（基于 GitHub Discussions）：新增 `src/templates/partials/giscus.html`，由 `comments.html` 在 `commentSetting.commentPlatform == 'Giscus'` 时引用；`src/config.json` 的 `customConfig` 新增 9 项 Giscus 设置（仓库 / repoId / 分类 / categoryId / 映射 / 表情回应 / 输入框位置 / 语言 / 主题）；启用后加载 `giscus.app/client.js` 渲染评论区，并对容器宽度与溢出做 CSS 约束 + 容器缩进 + ResizeObserver 防御脚本。
- 首次将主题源码 `src/`（模板 / 样式 / 资源 / `config.json`）纳入版本控制（此前未被提交）。

### Changed

- 补全 AI 约束文档占位：AGENTS.md（§0 项目描述 / §2 常用命令 / §8 单一事实源坐标）、README.md、ROADMAP.md、CONTRIBUTING.md、docs/engineering/architecture.md；明确主题为 Gridea-Pro 兼容静态主题、无独立单元测试、版本号与设置键事实源为 `src/config.json`。
- 修正文档平台表述：将早期误写的「Halo 兼容」更正为「Gridea-Pro 兼容」（主题使用 Jinja2/Pongo2 方言，实际运行于 Gridea-Pro，非 Halo）。

### Fixed

- 修复文章目录（TOC）高亮不随动的问题：`partials/scripts.html` 原以固定 `top <= 100` 阈值判定当前章节且 `activeIndex` 初值为 0，导致滚动到首个标题之前时错误高亮首项（表现为「目录卡住不随动」）、末章节距文档末尾不足阈值时永远无法激活。现改为按「阅读线」（`max(80, 视口高 22%)`）判定、`activeIndex` 初值 `-1` 表示未进入任何章节而不高亮任何项、滚到文档底部时强制高亮末项；`scroll` 监听加 `requestAnimationFrame` 节流与变化短路，并补 `resize` / `hashchange` 重算。（已通过本地 Gridea-Pro 渲染验证）
- 新增长目录面板自动跟随：当目录项多于可视高度时，文章滚动切换焦点项会带动目录面板自身滚动，使焦点项尽量保持在面板中心高度（近距 ≤120px 瞬时定位、远距平滑滚动）；用户手动翻目录后自动让位，文章再次滚动即恢复跟随。实现上只改 `panel.scrollTop` 而非 `scrollIntoView`（后者会连带滚动外层页面把正文顶走），并为 `.toc-aside` 加 `overscroll-behavior: contain` 防止翻目录时连带滚动正文。（已通过本地 Gridea-Pro 渲染验证）

### Removed

-
