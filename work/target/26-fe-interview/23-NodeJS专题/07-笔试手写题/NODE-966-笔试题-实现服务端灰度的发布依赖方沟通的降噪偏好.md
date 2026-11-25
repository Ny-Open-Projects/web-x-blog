---
title: [NODE-966] 笔试题——实现沟通降噪偏好（事件分级×偏好矩阵）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-966：手写降噪偏好

**需求与边界**：
- 需求：降噪偏好矩阵（SCN-OPS-320/959）——① 事件分级×偏好矩阵（P0 穿透/P1 摘要/P2 忽略——SCN-OPS-959）；② 矩阵的生效（路由器消费——SCN-OPS-320）；③ 矩阵的审计（SCN-OPS-220）。
- 边界：① 关键事件穿透（SCN-OPS-612）；② 矩阵的默认值（SCN-OPS-612）；③ 矩阵的灰度（SCN-OPS-228）。

**答**：
```javascript
const PREF_MATRIX = {                                 // 事件×偏好（SCN-OPS-959）
  P0: { always: true, channels: ['im', 'sms'] },      // 穿透（SCN-OPS-612）
  P1: { digest: '1h' },
  P2: { digest: '1d' },
};
function routeEvent(event, consumer) {
  const pref = consumer.prefs[event.type] ?? PREF_MATRIX[event.sla];   // 矩阵消费
  if (pref.always) return sendNow(event, pref.channels);   // 穿透
  return digestBuffer(event, pref.digest);             // 摘要（SCN-OPS-320）
}
```

**评分点**:
- 事件×偏好矩阵（SCN-OPS-959）。
- P0 穿透（SCN-OPS-612）。
- 摘要分级（SCN-OPS-320）。
