---
title: [NODE-385] Node 服务的读写分离与主从延迟处理如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-385：读写分离与主从延迟处理
**答**:
- 基础架构：写走主库、读走从库（连接池按读写分两个，路由在 repository 层声明式标注 read/write，不靠猜测）。
- 写后读一致性：用户提交后立即查看的场景（下单后看订单）必须读主库——实现：写操作后在会话/请求上下文标记"读主窗口"（几秒内读全走主库，NODE-292 AsyncLocalStorage 天然适配请求级上下文）；或 GTID 等待（PG：等待从库回放到位点）。
- 从库选择：多从库就近/负载均衡；从库故障自动剔除（健康检查）；只读账号防误写。
- 延迟监控：复制延迟指标（秒级）进监控；延迟超阈值自动把更多读流量切回主库（保护一致性优先于读扩展）。
- 数据不一致的用户感知设计：涉账场景不做"乐观读从库"（ARC-460），文案给"处理中"状态而非旧数据。
```javascript
// 请求级读写路由（AsyncLocalStorage）
const als = new AsyncLocalStorage();
function withMasterWindow(fn) { return als.run({ readMaster: true, until: Date.now() + 5000 }, fn); }
function pickPool() {
  const ctx = als.getStore();
  return (ctx?.readMaster && Date.now() < ctx.until) || isCriticalOp() ? master : replica();
}
// 写操作后：withMasterWindow(() => renderOrderPage(id))   // 写后 5s 内读主
```
