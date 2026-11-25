---
title: [NODE-830] 笔试题——实现静默降级与前端联动（降级标记的 UI 语义）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-830：手写降级联动

**需求与边界**：
- 需求：降级标记的前端联动（SCN-NODE-690）——① 降级标记协议（X-Degraded 头 + body 标记——SCN-NODE-690）；② 前端语义映射（降级类型 → UI 行为——隐藏实时性 UI/展示陈旧标注）；③ 降级的告警联动（前端降级率上报——SCN-NODE-690 聚合）；④ 静默分级（部分字段降级 vs 全页降级——不同 UI 处理）。
- 边界：① 陈旧数据的展示（stale 标注——SCN-联想-675）；② 降级 UI 的差异化（推荐降级——静态推荐不影响下单；价格降级——禁用下单按钮——语义敏感度分级）；③ 降级恢复的联动（恢复通知——SCN-NODE-690）。

**答**：
```javascript
// BFF 侧
res.setHeader('X-Degraded', 'recommend:cache;price:default');   // 降级清单（SCN-NODE-690）
res.json({ data, _degraded: { recommend: 'stale', price: 'default' } });
// 前端联动（语义映射）
const UI_ACTIONS = {
  recommend: { stale: 'show-static-badge' },           // 推荐：陈旧标注即可
  price: { default: 'disable-order-button' },          // 价格：禁用下单（语义敏感）
};
app.interceptors.response.use((resp) => {
  const deg = resp.headers['x-degraded'];
  if (deg) deg.split(';').forEach(d => applyUiAction(...d.split(':')));   // 语义映射
  return resp;
});
// 前端降级率上报（SCN-NODE-690 聚合闭环）
telemetry.push({ type: 'CLIENT_DEGRADED', degradations: deg });
```

**评分点**:
- 降级清单协议（header + body 双通道——SCN-NODE-690）。
- UI 语义映射分级（推荐 vs 价格——语义敏感度差异）。
- 前端降级率上报（聚合闭环——SCN-NODE-690）。
- 陈旧标注（SCN-联想-675）。
