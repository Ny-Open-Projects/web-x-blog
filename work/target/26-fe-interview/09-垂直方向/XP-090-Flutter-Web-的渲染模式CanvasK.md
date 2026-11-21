---
title: [XP-090] Flutter Web 的渲染模式？CanvasKit 与 html 渲染器怎么选？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-090：Flutter Web 的渲染模式？CanvasKit 与 html 渲染器怎么选？
**答**：
- 历史三选：`html`（DOM 渲染，包小、文本可选中/SEO 稍好，但像素不一致、部分 API 缺失）、`canvaskit`（Skia wasm 自绘，像素级一致、性能好，多 ~1.5MB wasm 下载）、`skwasm`（WasmGC 多线程渲染，Flutter 3.22+ 实验转正方向）。
- 版本现状：Flutter 3.29 起 `--web-renderer` 参数移除，**canvaskit 成为唯一主渲染器**，html 渲染器进入移除流程——新项目不应再基于 html 模式做架构决策。
- 选型逻辑（对存量项目）：纯内容/官网类站点本就不该用 Flutter Web（用 Next.js/SSR）；**应用型后台、内嵌工具、桌面端复用** 才是 Flutter Web 的甜区，canvaskit 一致性收益大于首载体积代价。
- 优化配套：canvaskit 资源走国内 CDN 缓存、字体（Noto 默认字体较大）子集化 + 本地化托管、`flutter build web --wasm` 试 skwasm、SSR 骨架/预加载遮罩缓解首屏（与 XP-095 秒开思路同构）。
- 兼容代价：文本选择/无障碍/SEO 弱于 DOM 方案，a11y 需开启 semantics 并实测（与 XP-141 无障碍体系联动）；接入既有浏览器埋点需适配 canvas 事件模型。

```text
Flutter Web 渲染模式决策（2024+）
渲染器        实现          首载体积    一致性    文本选择/SEO    现状
html          DOM+CSS       小          差        好              3.29 起废弃
canvaskit     Skia wasm     +1.5MB 级   像素级    弱              当前唯一主渲染器
skwasm        WasmGC+线程   中          像素级    弱              --wasm 构建渐进可用

决策树：
  内容型站点 SEO/可访问性优先 → 不用 Flutter Web，回退 Next.js SSR
  应用型后台/工具/桌面同构复用 → canvaskit（默认）
  对首载体积敏感且浏览器支持 WasmGC → 试用 --wasm 的 skwasm
配套优化：
  CanvasKit wasm 与字体改走自建 CDN（默认 google 源国内不可控）
  首屏：骨架页 + canvaskit 资源 preconnect/prefetch（XP-095 同构思路）
  文本选择/无障碍：开启 semantics，重点页面 DOM 副本兜底（a11y 树上报）
```
