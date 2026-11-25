---
title: [RBL-639] 构建器 API 的取消语义：AbortSignal 贯穿、幂等取消与资源回收
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-639：构建器 API 的取消语义：AbortSignal 贯穿、幂等取消与资源回收

**答**:
- 长构建必须可取消（用户改配置/关 dev server/CI 超时）——取消要**贯穿整条管线**：文件读取、transform 任务、插件钩子、写盘，每层都接受 AbortSignal；只在顶层 cancel 而底层继续跑的取消是假取消（资源照耗）。
- 取消的语义约定：1) 幂等——多次 cancel 与 cancel 后再 await 的行为一致（返回同一 AbortError）；2) 取消 ≠ 错误崩溃——构建结果标记 `{ status: 'cancelled' }`，已完成的模块缓存保留（取消不丢增量缓存）；3) 不可中断点的约定（rename 原子操作等）——cancel 期间到达的同步临界区要么跑完要么跳过，不允许半写。
- 资源回收：取消后要释放 in-flight 的 arena、关闭 watcher、终止 worker——显式生命周期（AbortSignal + finally 清理）比 GC 兜底可靠；dev server 场景每次 rebuild 是新 signal（上次构建取消）——「取消旧构建再起新构建」是 HMR 高频编辑下的标准流程（打断重跑）。
- Rust 侧协同：JS 的 signal → Rust 取消标志（原子 bool）→ rayon 任务在检查点退出；跨语言取消延迟要文档化（一个 transform 完成前无法中断是预期行为）。
- 追问钩子：为什么「取消时保留增量缓存」重要？——高频编辑场景（保存风暴）下取消是常态，若取消丢缓存则每次都是冷启动，增量编译的价值归零；取消的成本应该是「丢掉未完成的计算」而不是「丢掉已完成的一切」。

```javascript
// 贯穿式取消
async function buildWithCancel(config, signal) {
  const state = { status: 'running' };
  signal?.addEventListener('abort', () => { state.status = 'cancelled'; }, { once: true });
  try {
    const modules = await readModules(config, signal);        // 每层检查
    const transformed = await Promise.all(modules.map(m =>
      signal?.aborted ? Promise.reject(new DOMException('', 'AbortError')) : transform(m, signal)));
    if (signal?.aborted) throw new DOMException('', 'AbortError');
    const chunks = chunkify(transformed, config);
    return { status: 'success', chunks, cache: keepIncrementalCache() };  // 缓存保留
  } catch (e) {
    if (signal?.aborted) return { status: 'cancelled', cache: keepIncrementalCache() };
    throw e;                                                  // 真错误照常抛
  } finally {
    releaseArena(); closeWatchers();                          // 资源回收
  }
}

// HMR 打断重跑
let current;
function rebuildOnEdit(file) {
  current?.controller.abort();                                // 取消旧构建
  const controller = new AbortController();
  current = { controller, done: buildWithCancel(cfg, controller.signal) };
  return current.done;                                        // 新构建立即接管
}
```
