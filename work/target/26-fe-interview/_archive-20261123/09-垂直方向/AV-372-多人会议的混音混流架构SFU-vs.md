---
title: [AV-372] 多人会议的混音/混流架构（SFU vs MCU）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-372：多人会议的混音/混流架构（SFU vs MCU）

**答**：
- SFU：转发不转码，各端自己拉多路/订阅层——CPU 成本低，主流方案。
- MCU：服务端混流成一路——客户端简单但服务端转码贵，适合电话接入场景。
- 混合：SFU 转发 + 服务端录制/推流时才混流（按需）。

```javascript
// SFU 订阅策略
function subscribeStrategy(peers, { maxDownstreams = 6 } = {}) {
  const active = [...peers].sort((a, b) => b.speaking - a.speaking)
    .slice(0, maxDownstreams);                       // 活跃说话人优先
  return {
    subscribe: active.map(p => ({ id: p.id,
      layer: p.bandwidth > 2000 ? 'high' : 'low' })),
    pause: peers.filter(p => !active.includes(p))
      .map(p => ({ id: p.id, action: 'pause', avatar: true })),
  };
}
```
