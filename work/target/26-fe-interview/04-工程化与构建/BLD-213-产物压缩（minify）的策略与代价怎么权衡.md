---
title: [BLD-213] 压缩（minify）的策略与代价怎么权衡？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-213：压缩怎么权衡？
**答**：
- 压缩层次：空白去除（快省 20%）→ 变量重命名（mangle，省 30%）→ 死代码消除（DCE）→ 高级优化（inline/常量传播——terser compress 开关，慢但再省 10~15%）。
- 代价：高级压缩拖慢构建 + 可能引入 bug（terser 的已知 edge case：副作用推断错误）——安全模式（compress 部分开关关掉）vs 体积。
- gzip/brotli 是另一层：minify 对 gzip 后体积的收益缩水（重复模式已被字典压缩）——但仍是净收益。
- 快速压缩选择：esbuild/swc minify 快 10~50×（构建提速），体积略逊 terser（~2%）——构建时长 vs 体积的权衡点。
- 追问钩子：为什么压缩选项的收益要用「gzip 后体积」评估而不是 raw——用户实际下载的是 gzip/brotli 流；mangle 对 raw 省 30% 对 gzip 可能只省 10%（压缩器已经消除了重复性）——体积优化决策必须看传输体积，这也是产物 diff 报告（SCN-ENG-290）带 gzip 列的原因。

```javascript
// terser 关键开关与代价
{ compress: { passes: 2, inline: 3, drop_console: true },   // passes↑慢
  mangle: true, format: { comments: false } }
// esbuild minify：快但略大
minify: 'esbuild'   // 构建时间优先时选它（体积差 ~2%）
```
