---
title: [MFW-838] 多层 CDN（边缘 POP → 区域 → 源站）下 ISR 失效怎么传播并确认
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-838：多层 CDN（边缘 POP → 区域 → 源站）下 ISR 失效怎么传播并确认

**答**：
- 结论：失效必须从源站向下广播到每一层并收集 ack；只有全部 ack 才算完成，否则某层仍可能返回旧页。
- 落地：失效请求带失效版本号，各层记录并更新；源站聚合 ack，超时层重试/告警；客户端用版本号校验是否拿到最新。
- 追问钩子：为什么不用简单 purge？——purge 无确认、易被并发回填重新污染；版本号可校验。

```javascript
async function invalidateAll(layers, version) {
  const results = await Promise.allSettled(
    layers.map(l => l.invalidate(version))          // 源→区域→边缘
  );
  const acks = results.map((r, i) => ({
    layer: layers[i].name,
    ok: r.status === 'fulfilled'
  }));
  if (!acks.every(a => a.ok)) {
    alert('部分层级失效失败: ' + acks.filter(a => !a.ok).map(a => a.layer));
  }
  return { version, acks, complete: acks.every(a => a.ok) };
}
// 各层用版本号校验，拒绝旧版本回填
function shouldServe(cachedVersion, reqVersion) {
  return cachedVersion >= reqVersion;              // 低于请求版本 → 回源
}
```
