---
title: [NODE-743] 笔试题——实现健康探针三件套（liveness/readiness/startup）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-743：手写健康探针

**需求与边界**：
- 需求：三探针（SCN-NODE-664）——① liveness 极简（进程自响应 + ELD——不查依赖）；② readiness（依赖检查带超时 + 优雅关闭期间返回 503——SCN-NODE-722 联动）；③ startup（慢启动保护——预热完成前不放流量）；④ 依赖检查缓存（每次探针不都查——短 TTL 缓存依赖状态）。
- 边界：① 探针超时独立（500ms——不被慢依赖拖死）；② readiness 手动摘流（运维接口——POST /readyz/off 触发摘流——发布前摘流，SCN-NODE-638）；③ 依赖状态变化事件（摘流/恢复的日志）。

**答**：
```javascript
const state = { ready: false, manualOff: false, warmed: false };
app.get('/healthz', (req, res) => {                    // liveness：极简 + ELD
  if (eldP99() > 5000) return res.status(500).end();   // 事件循环僵死（SCN-NODE-721）
  res.status(200).end();
});
app.get('/readyz', async (req, res) => {
  if (state.manualOff || !state.ready) return res.status(503).end();   // 手动/未就绪
  const deps = await checkDepsCached({ timeout: 500, ttl: 5000 });   // 依赖检查带缓存
  res.status(deps.ok ? 200 : 503).end();               // 依赖挂 → 摘流不重启（SCN-NODE-664）
});
app.post('/readyz/off', internalOnly, (req, res) => {  // 手动摘流（发布前）
  state.manualOff = true; audit({ action: 'drain' }); res.end();
});
// startup：预热完成后 ready
warmup().then(() => { state.warmed = true; state.ready = true; });
```

**评分点**:
- liveness 极简（不查依赖 + ELD 僵死检测——SCN-NODE-664 语义正确）。
- readiness 依赖检查带缓存与超时（探针不被慢依赖拖死）。
- 手动摘流接口（发布前摘流——SCN-NODE-638 preStop 配合）。
- startup 预热保护（慢启动不误杀）。
