---
title: [WCN-284] Qwik 的 resumability（可恢复性）如何实现「零水合」？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-284：Qwik 的 resumability（可恢复性）如何实现「零水合」？
**答**：
- 序列化：应用状态（含闭包引用）序列化进 HTML（qwik/qrl 指针）——DOM 与状态一起下传。
- 恢复：交互事件触发时按需加载对应 chunk 并「恢复执行」（不重建组件树不重绑监听——监听在 HTML 上是全局委托）。
- 与水合对比：水合重执行组件树重建监听；Qwik 只加载事件处理函数。
- 代价：序列化格式复杂、调试心智变化、生态适配成本。

```javascript
<!-- Qwik 产物示意 -->
<button on:click="chunk-a.js#handler[0,1]" q:id="b1">Buy</button>
<script type="qwik/json">{"refs":{"b1":{"count":3}}}</script>
<!-- 点击才加载 chunk-a.js 并恢复闭包，无全树水合 -->
r
```
