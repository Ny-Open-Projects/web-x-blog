---
title: [JS-382] 并发场景的 Error 边界：组件树与任务树
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-382：并发场景的 Error 边界：组件树与任务树

**答**：
- 两棵树的错误边界：组件树（React Error Boundary 隔离渲染崩溃）与任务树（异步任务失败不影响其他任务）——并发场景两棵树都要有边界，异步错误不会自动进 Error Boundary
- 异步错误进边界的通路：错误先同步抛出（在事件回调/渲染周期内 setState 错误）或用「错误桥」（error callback → 父组件 state → 触发 boundary）——async 任务的 catch 里主动上报边界
- 任务树隔离实现：并行任务的错误不互相传染（allSettled 语义）、单个任务失败给局部降级 UI（卡片级 error slot）——「一卡崩全页崩」是并发错误处理的反面教材
- 重试与边界结合：边界捕获后展示重试按钮，重试只重放失败任务（不是整页 reload）——需要任务引用保留
- 上报归因：错误按「组件域 + 任务名」聚合，并发错误要带时间线上下文（当时有哪些任务在跑）——定位并发 bug 的关键线索

```javascript
class TaskBoundary {
  #listeners = new Set();
  run(name, task) {
    return task().catch((e) => {
      report({ name, error: e, concurrent: activeTasks() });   // 归因上下文
      this.#listeners.forEach(fn => fn(name, e));              // 通知 UI 边界
      throw e;                                                  // 语义保留
    });
  }
  onError(fn) { this.#listeners.add(fn); return () => this.#listeners.delete(fn); }
}
// UI: <Card error={errors.recommend ? <Retry onClick={retryOnly('recommend')}/> : null}>
```

**追问**：

1. React 18 并发渲染下，Error Boundary 还能兜住所有渲染错误吗？ → 能兜渲染期同步错误，但被 transition 丢弃的渲染不会触发；异步数据错误仍要经过错误桥手动抛进渲染。
2. TaskBoundary 里 catch 后又 `throw e`，不会制造 unhandledrejection 吗？ → 会，若调用方不再 catch 就会；要么返回降级值不抛，要么明确约定由上层统一 catch，二选一。
3. 只重放失败任务，怎么保证副作用不重复？ → 任务必须幂等或带幂等键，重试前检查该任务是否已成功；写操作尤其要防止「已提交但响应丢失」时再提交一次。
