---
title: [ARC-336] 笔试题：实现组件库的 Upload 分片上传组件？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-336：笔试题：实现组件库的 Upload 分片上传组件？
**答**：实现 Upload 分片上传核心：1) 文件分片（5MB/片）并发上传（并发上限 3）；2) 断点续传（上传前查已传分片）；3) 进度回调（按字节加权）；4) 全部完成后 merge 请求；5) 失败重试单片而非整体。
**评分点**：
- 分片与并发池实现正确（Promise 池上限 3）。
- 断点续传：已传分片跳过（服务端返回已传列表）。
- 进度计算按字节加权（分片大小不等时正确）。
- 单片失败重试（指数退避 2 次）不影响其他分片。
```tsx
async function uploadFile(file: File, { chunkSize = 5 << 20, concurrency = 3, onProgress }) {
  const chunks = Math.ceil(file.size / chunkSize);
  const hash = await fileHash(file);
  const uploaded = new Set(await api.get(`/upload/status?hash=${hash}`));  // 2) 断点续传
  let sent = [...uploaded].reduce((s, i) => s + Math.min(chunkSize, file.size - i * chunkSize), 0);
  const pending = Array.from({ length: chunks }, (_, i) => i).filter(i => !uploaded.has(i));
  const pool = [...pending];
  const retry = async (fn, n = 2) => { try { return await fn(); } catch (e) { return n ? retry(fn, n - 1) : Promise.reject(e); } };
  await Promise.all(Array.from({ length: Math.min(concurrency, pool.length) }, async () => {
    while (pool.length) {
      const i = pool.shift();
      const blob = file.slice(i * chunkSize, Math.min((i + 1) * chunkSize, file.size));
      await retry(() => api.post('/upload/chunk', { hash, index: i, blob }));
      sent += blob.size;
      onProgress?.(sent / file.size);                                     // 3) 字节加权进度
    }
  }));
  return api.post('/upload/merge', { hash, chunks });                     // 4) merge
}
// UI：<Upload beforeUpload={f => uploadFile(f, { onProgress: p => setPct(p) })}/>
```
