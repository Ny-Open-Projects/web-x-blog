---
title: [V3-480] watch 性能面：deep、immediate 与任务时机
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## V3-480：watch 性能面：deep、immediate 与任务时机

**答**：
- deep watch 的成本：依赖追踪遍历整个对象（getter 递归 reactive）——大对象 deep watch 每次变更都要全量 traverse（触发全部子依赖收集）；改用「明确路径 watch（() => obj.a.b）」
- watch vs watchEffect 任务语义：两者回调默认走「pre」时机（组件更新前）——回调里改状态会引发同轮二次更新；flush: 'post' 放更新后（读 DOM 安全）；flush: 'sync' 同步（高频状态慎用，配合节流）
- 批量触发：watch 回调默认批合并（同 tick 多次变更只触发一次，最后一次值）——sync 模式失去这层合并，是性能反模式的高发点
- 大对象变更监听的替代：watch 层数有限的「影子快照」（JSON 摘要 hash 比对）或「手动事件上报」——比 deep traverse 便宜数量级
- stop 时机：组件卸载自动停止（setup 内注册的）；全局/跨组件注册的必须手动 stop——泄漏排查点

```javascript
// 反模式
watch(bigObject, handler, { deep: true });   // 全量 traverse
// 正解: 精确路径
watch(() => bigObject.value.selectedId, handler);
// 批量+后置: 依赖 DOM 的回调
watchEffect(onCleanup => { measureDom(); }, { flush: 'post' });
```
