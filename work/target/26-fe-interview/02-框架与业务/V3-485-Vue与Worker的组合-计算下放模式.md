---
title: [V3-485] Vue 与 Worker 的组合：计算下放的三种模式
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## V3-485：Vue 与 Worker 的组合：计算下放的三种模式

**答**：
- 模式一（数据下发）：ref 数据变化 → debounced 发给 Worker 计算 → 结果回填另一个 ref——worker.onmessage 回 ref，响应式链路不变；适合大列表过滤/聚合
- 模式二（分页/增量）：Worker 维护全量数据与索引，主线程只拿查询结果——大数据集（10w 行表格）搜索/排序全在 Worker，主线程状态只有当前页
- 模式三（共享 SAB）：Worker 计算直接写 SharedArrayBuffer，主线程轮询/Atomics 读取——高频连续计算（音频可视化）避免消息序列化开销
- 响应式边界：Worker 内不能有 Vue 响应式（reactive 不可跨线程）——传递「原始数据」进 Worker、结果转回 ref；序列化成本是设计约束（传引用要 transferable/SAB）
- 组合模式：composable 封装（useWorker(computeFn, deps)）——watch(deps) 触发计算、AbortController 取消过期任务、缓存最近结果

```javascript
// useWorker composable
export function useWorkerCalc(workerUrl, sourceRef) {
  const result = ref(null);
  const w = new Worker(workerUrl);
  watch(debounceRef(sourceRef, 300), (v) => w.postMessage(v), { deep: false });
  w.onmessage = ({ data }) => result.value = data;
  onUnmounted(() => w.terminate());
  return result;   // 主线程消费侧保持响应式
}
```
