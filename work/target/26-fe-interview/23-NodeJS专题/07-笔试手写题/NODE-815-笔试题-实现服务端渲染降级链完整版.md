---
title: [NODE-815] 笔试题——实现 SSR 降级链完整版（缓存→降级渲染→CSR）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-815：手写 SSR 降级链

**需求与边界**：
- 需求：SSR 三级降级链（SCN-NODE-756/711）——① 缓存降级（last good HTML——SCN-NODE-669 fallback 语义）；② 简化渲染（去动态组件的降级渲染——渲染减负）；③ CSR 兜底（SPA fallback——可用性保底）；④ 降级原因标记（SCN-NODE-690 可观测）。
- 边界：① 降级链的触发条件分离（缓存过期/渲染超时/渲染崩溃——不同原因不同级）；② last good 的时效标注（缓存 HTML 带 generatedAt——SCN-联想-675 陈旧标注）；③ 降级率看板（SCN-NODE-690 聚合）。

**答**：
```javascript
async function renderWithChain(req) {
  const strategies = [
    { name: 'cache', run: () => lastGoodCache.get(req.url), cond: () => lastGoodCache.has(req.url) },
    { name: 'lite-render', run: () => renderLite(req),    // 降级渲染（去重组件）
      cond: () => renderingBacklog() < threshold },      // 渲染池有余量才试
    { name: 'csr', run: () => csrFallback(req), cond: () => true },   // 兜底
  ];
  for (const s of strategies) {
    if (!s.cond()) continue;
    try {
      const html = await s.run();
      res.setHeader('X-SSR-DEGRADED', s.name);         // 降级标记（SCN-NODE-690）
      if (s.name !== 'cache' && lastGoodCache.set) lastGoodCache.set(req.url, html);
      telemetry.push({ type: 'SSR_CHAIN', level: s.name });   // 降级率看板（SCN-NODE-690）
      return html;
    } catch (e) { logger.warn({ strategy: s.name, err: e }); continue; }   // 链式尝试
  }
  throw new Error('ALL_STRATEGIES_FAILED');
}
```

**评分点**:
- 三级降级链（cache→lite-render→CSR——SCN-NODE-756 体系化）。
- 条件触发分离（缓存过期/池余量——不同原因不同级）。
- last good 时效标注（SCN-联想-675 陈旧可见）。
- 降级率看板（SCN-NODE-690 聚合）。
