---
title: [V3-329] 手写：用 template + setText 实现一个 mini Vapor 组件
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-329：手写：用 template + setText 实现一个 mini Vapor 组件
**答**：不使用虚拟 DOM，实现 `template(html)` 克隆静态模板、`setText(el, getter)` 绑定动态文本；用它们实现一个计数器组件 setup，要求点击按钮更新计数显示。含边界：多次挂载互不影响。

```javascript
function template(html) {
  const holder = document.createElement('template')
  holder.innerHTML = html.trim()
  return () => holder.content.firstElementChild.cloneNode(true) // 每次调用克隆，互不影响
}
function setText(el, getter) {
  const update = () => { el.textContent = getter() }
  effect(update) // 依赖 getter 内响应式数据，变化时直接写 DOM
  update()
}
// 组件
const count = ref(0)
function App() {
  const el = template('<div><span>0</span><button>+1</button></div>')()
  setText(el.querySelector('span'), () => String(count.value))
  el.querySelector('button').addEventListener('click', () => count.value++)
  return el
}
```
**评分点**：
- template 必须每次 cloneNode，直接复用单节点会在多实例时互相污染（高频扣分点）。
- setText 通过 effect 建立响应式订阅，而非一次性赋值。
- 事件绑定在 setup 内完成，组件即 DOM，无 render/patch 环节。
