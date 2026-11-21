---
title: [WCN-104] WCN 与宿主框架的数据流桥接模式有哪些？单向数据流如何在事件边界上保持？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-104：WCN 与宿主框架的数据流桥接模式有哪些？单向数据流如何在事件边界上保持？

**答**：
- 入（宿主 → WC）：attribute（字符串配置）、property（对象/函数）、context（环境注入）、slot（内容投影，含具名插槽）。
- 出（WC → 宿主）：CustomEvent（detail 只读负载）、暴露方法（命令式 API：`el.open()`）、受控 property（宿主写回）。
- 单向流保持：WC 内部绝不修改传入的对象引用——深拷贝入参或把"变更意图"作为事件抛回宿主，由宿主决定新状态再回传；受控组件遵守"值由宿主下发、事件只上报"。
- 事件回环防护：宿主 setState → 回写 property → WC setter 相等短路 return（不再次派发事件），这是跨框架桥接最容易出 bug 的点。
- 共享状态方案：跨宿主的业务状态（购物车）放模块级 Signals store，WC 与各框架各自订阅同一 store——避免事件桥风暴。

```javascript
// 受控回环防护示例（WC 侧）
class TagInput extends HTMLElement {
  #value = [];
  set value(v) {
    const arr = Array.isArray(v) ? [...v] : [];
    if (arr.join() === this.#value.join()) return;  // 回环短路
    this.#value = arr;
    this.#render();
  }
  get value() { return this.#value; }
  #add(tag) {
    const next = [...this.#value, tag];
    this.#value = next;            // 内部先更新视图
    this.#render();
    this.dispatchEvent(new CustomEvent('tag-add', {
      bubbles: true, composed: true, detail: { value: next }, // 只上报，不改宿主对象
    }));
  }
  #render() { /* 渲染 this.#value */ }
}
```
