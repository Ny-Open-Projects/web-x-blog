---
title: [MFW-818] 边缘 KV 最终一致下用户从 A 区写、B 区读不到，read-repair 与单调读怎么配合
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-818：边缘 KV 最终一致下用户从 A 区写、B 区读不到，read-repair 与单调读怎么配合

**答**：
- 结论：两件事配合——读路径做 read-repair（多副本取最新版本并回填旧副本），会话层保证单调读（同一用户后续读不回退到更旧副本）。
- 落地：读时向 N 副本要版本取最大返回并写回落后副本；用户 cookie 记住「上次看到的最低版本」，低于它的副本不参与。
- 追问钩子：read-repair 与写 quorum 如何取舍？——写多读少用 quorum，读多写少用 read-repair。

```javascript
async function readRepair(key, replicas) {
  const results = await Promise.all(replicas.map(r => r.getWithVersion(key)));
  const latest = results.reduce((a, b) => b.version > a.version ? b : a);
  // 回填落后副本（异步，不阻塞返回）
  for (const r of replicas) {
    if (r.name !== latest.from && r.versionOf(key) < latest.version)
      r.set(key, latest.value, latest.version);
  }
  return latest;
}

// 单调读：cookie 记住最低版本，过滤回退副本
async function monotonicRead(req, key) {
  const seen = Number(req.cookies.get('min-version') || 0);
  const data = await readRepair(key, replicas.filter(r => r.versionOf(key) >= seen));
  // 响应写回更高的最低版本
  return { data, setCookie: Math.max(seen, data.version) };
}
```
