---
title: [MFW-238] 并发渲染下 Server 数据获取的取消传播
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## MFW-238：Server 数据获取的取消传播

**答**:
- 场景：用户快速导航（/a → /b），/a 的慢查询还在跑——服务端不取消则浪费 DB 资源（请求级浪费放大为容量问题）
- 机制现状：Next 的 RSC 渲染在客户端放弃后会中断流（连接关闭）——但 fetch 到 DB 的查询是否取消取决于调用链是否传 AbortSignal（pg/redis 驱动要显式接）
- 落地：数据函数签名统一收 `signal`（从请求 context 拿）→ 透传给 fetch（原生支持）与 DB 驱动（pg 的取消需单独通道——pg-query-流水线）
- 替代简化：短查询（<100ms）不值得取消传播（复杂度 > 收益）；只对慢查询（报表/聚合类）做取消——按查询分级投入

```javascript
// 分层取消
export async function getReport(id, signal) {
  return pg.query(sql, [id], { signal })       // 驱动支持则透传
}
// fetch 原生
fetch(url, { signal: getRequestSignal() })
// 分级：快查询不传 signal（省复杂度），慢查询必传
```
