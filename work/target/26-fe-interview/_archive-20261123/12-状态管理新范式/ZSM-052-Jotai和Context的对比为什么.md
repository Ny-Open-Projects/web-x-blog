---
title: [ZSM-052] Jotai 对比 React Context 解决了 Context 的哪些痛点？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-052：Jotai 对比 React Context 解决了 Context 的哪些痛点？
**答**：
- Context 是整值广播：value 任何字段变化，所有 useContext 消费者都重渲染，细粒度要拆 N 个 Provider。
- Context 不能做派生：派生值要么写进 value（计算地方难定），要么每个组件 useMemo；atom 派生链天然带缓存与依赖追踪。
- Context 无组件外访问、无异步、无跨树共享；atom 可组件外 get/set、异步 read、挂任意 Provider 子树或全局。
- Context 的合理地盘：低频的依赖注入（主题 class、i18n 实例），而不是高频数据流。

```javascript
// Context 拆到 12 个 Provider 才能细粒度，atom 只需按需声明
const wAtom = atom(1), hAtom = atom(1)
const areaAtom = atom(get => get(wAtom) * get(hAtom))
// w 变化时只有订阅 w 和 area 的组件渲染，订阅 h 的不动
```
