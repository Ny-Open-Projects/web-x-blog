---
title: [MFW-840] 笔试：手写分层失效传播与 ack 聚合器
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-840：笔试：手写分层失效传播与 ack 聚合器

**答**：
- 结论：向所有层广播失效版本，用 Promise.allSettled 避免单层失败阻塞其他；每层带重试与超时，聚合 ack 全部成功才算完成。
- 关键：失效必须带版本号，便于各层校验、防止旧版本并发回填重新污染。
- 追问钩子：某层持续失败怎么办？——告警 + 降级（该层停用缓存直通源站），而不是无限重试。

```javascript
async function propagateInvalidation(layers, version, { retries = 1, timeout = 2000 } = {}) {
  const results = await Promise.allSettled(layers.map(async layer => {
    for (let i = 0; i <= retries; i++) {
      try {
        await Promise.race([
          layer.invalidate(version),
          new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), timeout))
        ]);
        return { layer: layer.name, ok: true };
      } catch (e) {
        if (i === retries) return { layer: layer.name, ok: false, err: e.message };
      }
    }
  }));
  const acks = results.map(r => r.status === 'fulfilled' ? r.value : { ok: false });
  return { version, complete: acks.every(a => a.ok), acks };
}

// 自测
const layers = [
  { name: 'edge', invalidate: async v => {} },
  { name: 'region', invalidate: async v => {} },
];
propagateInvalidation(layers, 42).then(r => console.log(r.complete)); // true
```

**评分点**：
- 向所有层广播，用 allSettled 避免单层失败阻塞其他层
- 每层失败重试 + 超时控制（Promise.race）
- 聚合 ack，全部成功才 complete=true
- 失效带版本号以便校验、防旧版本回填；持续失败告警降级（加分）
