---
title: [NODE-440] Node 服务的 API 废弃（deprecation）完整流程如何执行？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-440：API 废弃完整流程
**答**:
- 流程五步：公告（变更日志 + 直接通知活跃调用方 NODE-427 调用方清单）、响应头标注（Deprecation + Sunset + Link 替代方案）、流量监控（该 route 调用量曲线与调用方分布——等谁迁移一目了然）、清零确认（调用方逐一确认迁移完成，零流量宽限 2 周）、下线（410 Gone + 下线公告）。
- 给迁移的工具：新接口先于旧接口废弃上线（并存期 ≥ 一个迁移周期）、迁移文档（新旧字段映射表）、调用方 codemod（可自动化时）、沙箱验证（NODE-399）。
- 内部 API vs 开放 API：内部（迁移周期周级，强制 deadline——内部没有理由拖着）；开放（月级+，遵守公告期承诺，NODE-397 契约治理）。
- 强制力设计：内部 API 到 deadline 后硬下线（每次宽限都在训练拖延期）——但要走豁免通道给确实困难的调用方（ARC-435 例外机制）。
- 度量：废弃完成周期、下线时残留调用（应趋近 0）、因废弃引发的事故（理想为 0）。
```javascript
// 废弃响应头 + 流量监控
router.use('/v1/goods', (ctx, next) => {
  ctx.set('Deprecation', 'true');
  ctx.set('Sunset', 'Wed, 01 Jan 2027 00:00:00 GMT');
  ctx.set('Link', '</v2/goods>; rel="successor-version"');
  flowCounter.inc('v1.goods', { caller: ctx.caller.svc });       // 调用方分布监控
  return next();
});
```
