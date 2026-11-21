---
title: [R19-268] useDeferredValue 用于受控输入的完整模式是什么？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-268：useDeferredValue 用于受控输入的完整模式？
**答**：
- 输入 value（Sync）+ deferredValue = useDeferredValue(value)：重计算（过滤大列表）用 deferred 值，输入框本身用原值——打字永远流畅。
- 行为：value 高优更新 → 输入即时回显；deferred 重渲染可中断，新输入到来时作废旧计算。
- isStale：useDeferredValue 第二参数返回 isStale 时可给列表加「计算中」样式（React 19 新签名）。
- 与防抖的对比：防抖是「时间维度延迟」，deferredValue 是「优先级维度让路」——后者不引入人为延迟，交互更连贯。
- 坑：列表渲染本身很慢（单帧 >16ms）时 deferredValue 也救不了，得先虚拟化。
