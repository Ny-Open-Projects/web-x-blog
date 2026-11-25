---
title: [BLD-284] SVG 的构建处理（sprite/内联/组件化）怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-284：SVG 构建怎么做？
**答**：
- 三种产物模式：sprite 合并（<use> 引用——图标量大重复使用）、独立文件（大 SVG 懒加载）、组件化（React/Vue 组件——需要 props 染色/动态路径）。
- 构建处理：SVG 清理（去掉注释/元数据/编辑器残留——体积与安全）、SVGO 压缩（谨慎——过度优化破坏视觉）、hash 命名。
- sprite 的权衡：sprite 合一文件（一次请求+浏览器缓存）vs 独立文件（按需加载）——图标使用分布决定（高频图标 sprite、低频独立）。
- 组件化的构建陷阱：每图标一个组件 → 每图标一个模块（tree-shake 友好——未用图标被摇掉，比 sprite 全量打包更省）。
- 追问钩子：为什么「图标组件化」在摇树下可能优于 sprite——sprite 是全量打包（引入 icon 库就带全部图标，即使只用 10 个）；组件化让未 import 的图标被摇除（按需）——图标数量大而使用率低时，组件化+摇树的产物体积显著小于 sprite；使用率高且集中的场景 sprite 的单请求优势才成立。

```javascript
// 组件化（摇树友好）
import { IconHome } from '@org/icons/react';          // 只打进用到的图标
// sprite（使用率高场景）
<svg><use href="#icon-home" /></svg>                   // sprite.svg 一次请求
// 清理 + 压缩
svgo --multipass --precision=2
```
