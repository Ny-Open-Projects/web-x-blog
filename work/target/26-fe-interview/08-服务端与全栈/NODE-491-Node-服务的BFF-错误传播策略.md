---
title: [NODE-491] Node 服务的 BFF 错误传播策略（下游错误如何转译给前端）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-491：BFF 错误传播策略
**答**:
- 原则：前端不该感知下游细节（内部错误码/服务名/堆栈都不该透传）——BFF 是错误的"翻译层"：下游错误 → 业务语言错误（用户可懂 + 前端可处理）。
- 转译规则表：下游错误码 → BFF 统一错误码（NODE-321 映射表维护）+ 用户文案（NODE-410 错误信封）+ 前端处理指令（retryable/redirect/prompt——ARC-487 分层呈现的数据依据）。
- 聚合错误语义：多下游聚合失败（部分成功）——部分失败怎么表达：响应级（HTTP 200 + 数据带 degraded 标记，ARC-447 非关键降级）vs 请求级（关键下游失败 → 5xx）——分级规则显式（哪个下游失败算整体失败）。
- 错误溯源保留：对前端屏蔽细节但排障链路保留——错误事件上报（BFF 侧记录原始下游错误 + traceId），前端拿到的是 traceId 可供工单（ARC-533 排障打通）。
- 一致性：同类下游错误在不同接口的转译结果一致（映射表单源——避免 A 接口说"库存不足"B 接口说"系统繁忙"其实是同一个错）。
```javascript
// 错误转译映射
const translate = {
  'INV-001': { code: 'STOCK_OUT', msg: '该商品已被抢完', action: 'refresh' },
  'PAY-TIMEOUT': { code: 'PAY_TIMEOUT', msg: '支付结果确认中', action: 'poll', retryable: true },
  DEFAULT: { code: 'SERVICE_BUSY', msg: '开小差了，稍后再试', action: 'retry' }
};
function toFront(downstreamErr) {
  const t = translate[downstreamErr.code] ?? translate.DEFAULT;
  return { error: { ...t, traceId: downstreamErr.traceId } };    // 前端拿 traceId 供工单
}
```
