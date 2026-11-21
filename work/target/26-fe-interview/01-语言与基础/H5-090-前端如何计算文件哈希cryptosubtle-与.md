---
title: [H5-090] 前端如何计算文件哈希？crypto.subtle 与分块策略怎么做？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-090：前端如何计算文件哈希？crypto.subtle 与分块策略怎么做？
**答**：
- `crypto.subtle.digest('SHA-256', data)` 是标准选择：入参 `BufferSource`，返回 ArrayBuffer，hex 需自己转；**只在安全上下文（https/localhost）可用**。
- Web Crypto **没有 MD5**（MD5 已不安全），需要 MD5 的老接口场景用 js-spark-md5 等库按增量分块算。
- 大文件策略：分块增量哈希——全量 SHA-256 用 `subtle.digest` 前必须拼出完整 ArrayBuffer，大文件不可行；改用流式分块 + 秒传场景的抽样哈希（首尾 + 中间若干块）配合分片上传。
- 分片上传的断点续传：每片独立算 SHA-256 上报服务端校验，整体一致性由分片清单保证。
- 输出转换：`[...new Uint8Array(hash)].map(b => b.toString(16).padStart(2, '0')).join('')`。

```javascript
// 1) 标准姿势：小文件整体 SHA-256
async function sha256Hex(blob) {
  const buf = await blob.arrayBuffer();
  const hash = await crypto.subtle.digest('SHA-256', buf);
  return [...new Uint8Array(hash)]
    .map(b => b.toString(16).padStart(2, '0')).join('');
}

// 2) 大文件：分片逐块 SHA-256 + 清单（服务端聚合校验）
async function hashChunks(file, chunkSize = 8 * 1024 * 1024) {
  const list = [];
  for (let off = 0; off < file.size; off += chunkSize) {
    const hex = await sha256Hex(file.slice(off, off + chunkSize)); // Blob.slice 零拷贝
    list.push(hex);
  }
  return list;   // [hash1, hash2, ...] 供秒传/续传比对
}

// 3) 秒传探测：抽样哈希（首块 + 尾块 + 中块）快速比对
async function quickHash(file) {
  const sample = (a, b) => file.slice(a, b);
  const parts = [
    sample(0, 2 << 20),
    sample(Math.floor(file.size / 2), Math.floor(file.size / 2) + (2 << 20)), // 括号必须有：+ 优先级高于 <<
    sample(Math.max(0, file.size - (2 << 20)), file.size),
  ].filter(Boolean);
  const bufs = await Promise.all(parts.map(p => p.arrayBuffer()));
  const total = new Uint8Array(bufs.reduce((n, b) => n + b.byteLength, 0));
  bufs.reduce((o, b) => (total.set(new Uint8Array(b), o), o + b.byteLength), 0);
  return sha256Hex(new Blob([total]));
}

// 4) 环境守卫：非安全上下文直接降级到库实现
if (!window.isSecureContext || !crypto?.subtle) {
  console.warn('crypto.subtle 不可用，请引入 spark-md5 等降级方案');
}
```
