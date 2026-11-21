---
title: [WCN-123] Qwik 的 resumability 是怎么实现的？与水合（hydration）的本质区别是什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-123：Qwik 的 resumability 是怎么实现的？与水合的本质区别是什么？

**答**：
- 水合成本：传统 SSR 后客户端要重跑全部组件代码、重建事件监听与状态（执行量 ≈ 首次渲染），TBT（Total Blocking Time）高。
- resumability：服务端渲染时把"状态"序列化进 HTML（属性/自定义 script），把"事件处理器"拆成独立可懒加载的 QRL chunk（`on:click="chunk.js#handler"`）；客户端不重跑任何渲染逻辑，仅在事件发生时按需下载并执行对应闭包。
- 实现机制：Qwik loader（~1KB）做全局事件委托；编译器把组件代码切片为 qrl（懒加载导出引用）；状态序列化由 `useSignal/useStore` 声明参与。
- 事件恢复：点击按钮 → loader 从 HTML 属性定位 qrl → 动态 import → 执行；组件"从序列化现场恢复"，这就是 resume。
- 代价：代码切片数量大、框架心智较重、生态成熟度低于 React；适合内容/电商首屏敏感场景。

```html
<!-- Qwik 输出的 HTML（示意） -->
<button q:slot="btn" on:click="app-chunk.js#onClick[0]" q:id="b1">加入购物车</button>
<script type="qwik/json">
  {"refs":{"b1":{"count":"3"}},"objs":["3"]}
</script>
<!-- 点击时才下载 app-chunk.js 并恢复 count=3，无水合重跑 -->
```
