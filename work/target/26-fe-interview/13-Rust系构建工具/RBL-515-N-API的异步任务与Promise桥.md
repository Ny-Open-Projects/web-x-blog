---
title: [RBL-515] N-API 的异步任务与 Promise 桥：build 的取消怎么实现
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-515：N-API 的异步任务与 Promise 桥：build 的取消怎么实现

**答**:
- JS 侧 `await build()` 的 Promise 从哪来：napi-rs 的 `async fn` 导出自动创建 Promise（AsyncTask 模式）——Rust 侧 tokio 任务完成 → resolve；panic/Err → reject。
- **取消的难点**：Promise 本身不可取消（JS 语义）——取消语义要在 Rust 侧实现：`buildWithHandle()` 返回 `{ promise, cancel() }`——cancel 设置 AtomicBool 取消标志，tokio 任务在协作点（每模块转换后）检查标志提前退出；JS 侧 promise 仍会 resolve（返回 `{ cancelled: true }`）而非 reject（语义区分「取消」与「失败」）。
- 协作式取消纪律：Rust 取消只能在「检查点」生效——长循环（逐模块转换）要显式插入检查（每 N 个任务检查一次），细粒度检查点过多有开销，粗粒度取消延迟大——折中按「模块」为检查粒度。
- 取消的资源清理：被取消的编译要回滚中间状态（半成品的 chunk/缓存写入）——事务式清理（临时目录 + rename 提交）保证「取消不留脏数据」（ZSM-524 事务语义同构）。
- 追问钩子：为什么不用 worker_threads 里直接 terminate？——terminate 会丢 Rust 侧状态（内存泄漏风险），协作式取消是唯一安全的模式。

```javascript
// N-API 异步任务的取消模式
// Rust 侧（概念）
// pub struct BuildHandle { cancel: Arc<AtomicBool> }
// pub fn buildWithHandle(opts) -> Handle {
//   let cancel = Arc::new(AtomicBool::new(false));
//   let promise = spawn_blocking(move || {
//     for (i, module) in modules.iter().enumerate() {
//       if cancel.load(Relaxed) { return Ok(Cancelled); }   // 协作检查点：每模块
//       transform(module);
//     }
//     Ok(Done(artifacts))
//   });
//   Handle { promise, cancel_fn: cancel }
// }

// JS 侧
class BuildHandle {
  constructor(promise, cancelFn) { this.promise = promise; this.cancelFn = cancelFn }
  cancel() { this.cancelFn() }                 // 设置取消标志，promise resolve {cancelled:true}
}

async function build() {
  const handle = native.buildWithHandle(options)
  process.on('SIGINT', () => handle.cancel())  // Ctrl+C 优雅取消：不留脏数据
  const result = await handle.promise
  if (result.cancelled) { cleanupTmpDir() }    // 事务式清理：取消不留脏数据
}
// 铁律：Promise 不可取消（JS 语义）→ 取消在 Rust 侧协作式实现
// terminate 不可用：丢状态 + 内存泄漏 → 协作检查点是唯一安全模式
```
