---
title: [RBL-428] 笔试：手写幂等发布 API
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-428：手写幂等发布 API
**答**：实现 `createReleaseApi(store)`：1) `release({ idempotencyKey, manifest, target })`：同 key 重放返回首次结果（不重复发布）；2) 状态机：pending→uploading→verifying→done/failed（状态可查询）；3) 断点续传：uploading 中断后同 key 重入从断点继续（已上传文件跳过——按 hash 对比）；4) 原子切换：verifying 通过后一次性切入口（切失败回滚指针）；5) 并发同 key：共享同一发布（不并发两次）；6) `status(key)` 查询。

```javascript
export function createReleaseApi(store, cdn) {
  const inflight = new Map()

  async function release({ idempotencyKey: key, manifest, target }) {
    const existing = store.get(key)
    if (existing?.status === 'done') return existing              // 幂等重放
    if (inflight.has(key)) return inflight.get(key)               // 并发共享

    const p = (async () => {
      const rec = store.get(key) ?? { key, status: 'pending', manifest, target, uploaded: {} }
      rec.status = 'uploading'
      for (const [path, content] of Object.entries(manifest.files)) {
        const hash = manifest.hashes[path]
        if (rec.uploaded[path] === hash) continue                 // 断点续传：已传跳过
        await cdn.put(path, content)
        rec.uploaded[path] = hash
        store.save(key, rec)                                      // 每文件持久化进度
      }
      rec.status = 'verifying'
      for (const [path, hash] of Object.entries(manifest.hashes))
        if ((await cdn.head(path)) !== hash) { rec.status = 'failed'; throw new Error(`verify fail: ${path}`) }
      const prevPointer = await cdn.getPointer(target)
      try {
        await cdn.switchPointer(target, manifest.version)         // 原子切入口
        rec.status = 'done'
      } catch (e) {
        await cdn.switchPointer(target, prevPointer)              // 切失败回滚
        rec.status = 'failed'
        throw e
      }
      store.save(key, rec)
      return rec
    })().finally(() => inflight.delete(key))

    inflight.set(key, p)
    return p
  }

  return { release, status: (key) => store.get(key)?.status ?? 'unknown' }
}
```
**评分点**：
- 幂等三层（done 重放返回 / 在途共享 / 断点续传按 hash 跳过）
- verify 后再切指针（产物全量就绪才可见——发布一致性）
- 切指针失败回滚 prevPointer（原子切换 + 回滚）
- 每文件进度持久化（中断重入无重复上传）
