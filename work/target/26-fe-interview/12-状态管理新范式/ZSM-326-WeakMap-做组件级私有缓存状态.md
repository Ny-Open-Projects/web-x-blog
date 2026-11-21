---
title: [ZSM-326] 什么时候用 WeakMap/WeakRef 存组件关联的状态
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-326：什么时候用 WeakMap/WeakRef 存组件关联的状态

**答**:
- 适用：以对象（DOM 节点/组件实例/SDK 实例）为 key 的私有附加数据——WeakMap 的 key 被回收时条目自动消失，无需手动清理，杜绝「实例销毁但缓存泄漏」
- 典型场景：给图表实例挂状态（WeakMap<ChartInstance, State>）、给 DOM 元素挂装饰器元数据、SDK 实例与内部回调映射
- 不适用：需要遍历/序列化/持久化的状态（Weak 不可枚举）；生命周期需要长于 key 的数据（会被提前回收）
- React 组件场景更常见替代：ref/useRef 管实例级数据；WeakMap 用于「实例由外部管理、无法挂在 ref 上」的场景

```javascript
const chartState = new WeakMap()
function renderChart(el, data) {
  const inst = echarts.init(el)
  chartState.set(inst, { dataVersion: 1, lastRange: null })   // 实例销毁自动清理
  return inst
}
function updateChart(inst, data) {
  const s = chartState.get(inst)
  if (!s) return                                              // 已被 GC 的实例直接跳过
  s.dataVersion++
}
```
