---
title: [NODE-422] Node 服务的请求取消（AbortSignal 传播）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-422：请求取消传播
**答**:
- 为什么：客户端取消（页面关闭/切换）后服务端继续算完是纯浪费（CPU/连接/下游配额）；取消应沿调用链传播到底（DB 查询/下游 HTTP/渲染）。
- 实现：请求入口创建 AbortController → AbortSignal 存 ALS 上下文（NODE-421）→ 所有下游调用挂 signal（fetch signal、pg query signal、Koa ctx.req aborted 监听）；任一环节 abort 级联取消全部。
- 下游传播：HTTP 客户端把 signal 转为对下游的连接关闭（下游也感知取消，形成端到端传播链）；BFF 超时预算（NODE-377 deadline）与 signal 合并（AbortSignal.any([reqSignal, timeoutSignal])）。
- 细节：取消后的清理（finally 释放资源）、取消是正常流量（不计错误率，统计取消率指标——取消率突增可能是前端 bug）；幂等无关（取消不会导致重复写——已提交的事务回滚或完成）。
- 框架配合：Koa 的 ctx.req.on('close')；Express 4 需手动监听 close 事件。
```javascript
app.use((req, res, next) => {
  const ac = new AbortController();
  req.on('close', () => ac.abort(new RequestCancelled()));      // 客户端断开
  als.run({ signal: ac.signal, reqId: genId() }, next);
});
// service 层
async function getGoods(id) {
  const { signal } = als.getStore();
  return fetch(downstreamUrl(id), { signal: AbortSignal.any([signal, AbortSignal.timeout(2000)]) });
}
```
