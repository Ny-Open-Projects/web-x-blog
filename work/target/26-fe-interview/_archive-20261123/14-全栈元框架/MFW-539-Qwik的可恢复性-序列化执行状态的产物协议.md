---
title: [MFW-539] Qwik 可恢复性：序列化执行状态的产物协议
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-539：Qwik 可恢复性：序列化执行状态

**答**:
- 可恢复性 vs 水合：传统水合 = client 重执行全部组件代码重建状态（昂贵）；Qwik = **状态序列化进 HTML**（组件状态/事件监听器的 QRL 引用）——client「恢复」：HTML 直接可用（无需执行组件代码）——交互触发时才按需加载对应 QRL chunk（事件处理器级 lazy——比岛级更细）。
- QRL 协议：事件监听 = `on:click="chunk-file#symbolName"` 引用（HTML 属性内嵌 chunk 路径 + 导出符号）——点击时：动态 import chunk → 调 symbol——「执行单元 = 事件处理器」而非「页面」。
- 产物形态：每组件/事件一个微 chunk（构建器符号级切分 RBL-938 目录切分的极致）；状态序列化（Qwik 序列化器：组件 props/state 到 HTML script 内嵌——循环引用/类实例支持有限制）。
- 代价：序列化格式约束（组件 state 必须可序列化——闭包状态不可恢复需映射）；调试体验（代码全碎成微 chunk——堆栈/网络面板噪声）。
- 追问钩子：为什么 Qwik 的「事件级 lazy」比「岛级 lazy」（Astro）更激进且更难？——岛级 = 组件边界（数个/页）；事件级 = 交互边界（数十个/页）——chunk 数量爆炸（微 chunk 的 HTTP/2 多路复用下可行）；「lazy 粒度 = 用户交互的最小单元」——粒度选择与交互概率分布相关：低交互内容页 Qwik 优、高交互应用岛级/常规 SPA 更简单——交互密度决定架构。

```html
<!-- Qwik 产物：状态内嵌 + 事件引用 -->
<div q:container="paused">
  <button on:click="chunk-abc#handleAdd" q:id="b1">Add</button>
  <script type="qwik/json">{"refs":{"b1":{"count":3}}}</script>   <!-- 状态序列化 -->
</div>
<!-- 点击时：import('chunk-abc').then(m => m.handleAdd(state)) —— 事件级按需 -->
<!-- 对比水合：React 需要执行 Counter 组件函数重建 vdom+state -->
<!-- Qwik：HTML 即状态，组件代码只在交互时加载 -->
```
