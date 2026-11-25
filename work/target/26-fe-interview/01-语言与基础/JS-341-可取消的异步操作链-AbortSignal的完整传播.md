---
title: [JS-341] 可取消的异步操作链：AbortSignal 的完整传播
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-341：可取消的异步操作链：AbortSignal 的完整传播

**答**：
- 取消要贯穿整条链：fetch（原生支持 signal）→ 自定义异步步骤（signal.throwIfAborted() / addEventListener('abort')）→ 池/队列（任务出队前检查）→ UI（卸载监听器）
- AbortSignal 组合：AbortSignal.any([...])（任一触发即取消）、AbortSignal.timeout(ms)（超时即取消）——多层取消源（组件卸载 + 用户取消 + 超时）合并为一条链
- 超时不是取消的替代：timeout 只断网络，业务已执行的服务端副作用不会回滚——写操作取消要配合幂等键
- 检查点模式：长计算切片间调用 signal.throwIfAborted()，把 AbortError 优雅上抛而不是悬挂
- 资源清理：abort 事件里清理关联资源（Worker terminate、临时 buffer 释放）——取消语义包含清理

```javascript
async function pipeline(items, signal) {
  for (const item of items) {
    signal.throwIfAborted();                    // 切片检查点
    const res = await fetch(item.url, { signal });
    await process(await res.arrayBuffer(), signal);
  }
}
const ctrl = new AbortController();
const sig = AbortSignal.any([
  ctrl.signal,
  AbortSignal.timeout(10_000),                  // 总超时
]);
try { await pipeline(items, sig); }
catch (e) { if (e.name === 'TimeoutError') retry(); else if (e.name !== 'AbortError') throw e; }
finally { ctrl.abort(); }                       // 无论成败, 清理链
```
