---
title: [ZSM-244] Web Components 组件的内部状态怎么和外层框架互通
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-244：Web Components 组件的内部状态怎么和外层框架互通

**答**：
- 标准通道三条：attributes（字符串）、properties（任意值，框架按 setProperty 传）、CustomEvent（组件对外抛事件），状态只在这些边界进出，WC 内部自治
- 复杂对象用 property 传（attribute 只能字符串），频繁变化的内部状态用事件 + property 回传，避免 DOM attribute 每次序列化
- 与全局 store 的桥：WC 可以直接 import vanilla store（构建时耦合），或通过 property 注入 store 实例（运行时解耦，微前端友好）
- React 19 已支持把对象按 property 传给自定义元素；老版本 React 需要 ref + setProperty 兜底

```javascript
class UserCard extends HTMLElement {
  set user(v) { this._user = v; this.render() }          // property 通道
  get user() { return this._user }
  connectedCallback() { this.addEventListener('click', () =>
    this.dispatchEvent(new CustomEvent('user-selected', { detail: this._user, bubbles: true })))
  }
}
// Vue/React：监听 user-selected + 传 :user prop 即完成桥接
```
