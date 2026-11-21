---
title: [AV-028] ICE 候选有哪几种类型？host/srflx/relay 怎么区分？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-028：ICE 候选有哪几种类型？host/srflx/relay 怎么区分？
**答**：
- host：本机网卡地址（局域网直连）；srflx（server reflexive）：STUN 发现的公网映射；relay：TURN 中继地址；还有 prflx（对等反射，打洞过程中产生）。
- 优先级：host > srflx > relay，ICE 按优先级配对尝试；同一局域网内 host 候选毫秒级连上。
- mDNS 隐私：Chrome 把 host 候选换成 `xxx.local` mDNS 名，跨网段解析不了就得依赖 srflx/relay。
- 排查技巧：`getStats` 中 `candidate-pair` 的 `localCandidateId` 指向实际使用的候选类型，relay 说明走了中继（有带宽成本）。

```javascript
// 枚举本端候选类型 + 从 getStats 确认实际链路
pc.addEventListener('icegatheringstatechange', async () => {
  if (pc.iceGatheringState !== 'complete') return;
  const stats = await pc.getStats();
  const types = [];
  stats.forEach((r) => {
    if (r.type === 'local-candidate') types.push(`${r.candidateType}: ${r.address ?? r.ip}`);
  });
  console.log('收集到的候选:', types);
  // ['host: 192.168.1.5', 'srflx: 203.0.113.7', 'relay: 198.51.100.9']

  // 找出当前生效的连接对
  let pair, localId;
  stats.forEach((r) => {
    if (r.type === 'candidate-pair' && r.state === 'succeeded' && r.nominated) pair = r;
  });
  const local = stats.get(pair.localCandidateId);
  console.log('实际链路类型:', local.candidateType); // host/srflx/relay
});
```
