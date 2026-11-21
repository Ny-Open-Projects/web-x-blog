---
title: [PER-842] 手写一个动态化 bundle 增量下载器：按模块 diff 增量、失败回退全量
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-842：手写一个动态化 bundle 增量下载器：按模块 diff 增量、失败回退全量

**答**：
- 需求：输入本地模块清单 [{id, hash}] 与远端清单 [{id, hash, url, size}]，计算需下载的变更模块（新增或 hash 不同）；逐个下载（并发 2），任一失败重试 2 次后放弃增量、回退为全量下载（远端 fullUrl）；完成输出报告（增量数/跳过数/是否回退）。
- 边界：远端清单无 fullUrl 时回退失败直接报错；下载大小超总预算（如 5MB）提前终止并回退全量（说明 diff 计算异常）；重复调用幂等（同 hash 跳过）。
- 评分点：diff 正确性；失败回退全量；预算提前终止。

```javascript
async function incrementalUpdate(local, remote, { conc = 2, budgetMB = 5, retries = 2 } = {}) {
  const localMap = new Map(local.map(m => [m.id, m.hash]));
  const changed = remote.filter(m => localMap.get(m.id) !== m.hash);
  const totalMB = changed.reduce((s, m) => s + (m.size || 0), 0) / 1048576;
  if (totalMB > budgetMB) return fullFallback(remote);         // diff 异常保护：回全量
  const results = { downloaded: [], skipped: remote.length - changed.length, fallback: false };
  const queue = [...changed];
  const worker = async () => {
    while (queue.length) {
      const m = queue.shift();
      for (let i = 0; i <= retries; i++) {
        try { await downloadFile(m.url); results.downloaded.push(m.id); break; }
        catch { if (i === retries) return fullFallback(remote, results); }   // 回退全量
      }
    }
  };
  await Promise.all(Array(conc).fill(worker));
  return results;
}
function fullFallback(remote, results) {                       // 全量下载
  if (!remote[0]?.fullUrl && !remote.fullUrl) throw new Error('no-full-url');
  return { ...results, fallback: true, action: 'download-all:' + (remote.fullUrl ?? '') };
}
```
