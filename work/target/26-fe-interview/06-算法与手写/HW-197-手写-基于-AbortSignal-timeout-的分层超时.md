---
title: [HW-197] 手写分层超时——AbortSignal.timeout/connect 超时/总预算三层（连接快超时+响应慢超时）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-197：手写分层超时——AbortSignal.timeout/connect 超时/总预算三层（连接快超时+响应慢超时）
**答**：fetch 无原生连接超时，分层实现：① AbortSignal.timeout(ms)（响应总超时）；② 连接超时模拟（fetch 后短窗内未到 response headers 即 abort——用 fetch 的 read 第一块判断；简化版用双 timer：connectTimeout 先到则 abort）；③ 多请求总预算（PER-328）。AbortSignal.any 组合信号（业务取消 + 超时）。

```javascript
async function fetchWithTimeouts(url, { connectMs = 5000, responseMs = 15000, signal } = {}) {
  const connectCtrl = new AbortController();
  const respCtrl = AbortSignal.timeout(responseMs);       // 响应总超时（原生，Chrome 103+）
  const onAbort = () => connectCtrl.abort('connect-timeout');
  const connectTimer = setTimeout(onAbort, connectMs);    // 连接超时（headers 未到 = 连接/首字节问题）
  const signals = [connectCtrl.signal, respCtrl, ...(signal ? [signal] : [])];
  const combined = AbortSignal.any?.(signals) ?? signals[0];
  try {
    const res = await fetch(url, { signal: combined });
    clearTimeout(connectTimer);                           // headers 已到：连接成功，只留响应超时
    return res;
  } catch (e) {
    clearTimeout(connectTimer);
    const reason = e.message?.includes('connect-timeout') || combined.reason === 'connect-timeout'
      ? 'connect-timeout' : respCtrl.aborted ? 'response-timeout' : 'cancelled';
    throw Object.assign(new Error(reason), { timeoutType: reason });   // 超时类型区分（诊断友好）
  }
}
// 分层语义：
// connectMs：连接+首字节（网络层问题——DNS/TCP/服务端首响应）
// responseMs：响应总时长（下载大 payload 也算在内）
// timeoutType 区分 connect-timeout/response-timeout/cancelled —— 监控按类型聚合（DNS 问题 vs 服务器慢）
// AbortSignal.any 组合（业务取消 + 两层超时）；无 any 的 polyfill 用 HW-109 #combine
```

**评分点**：
- 连接超时与响应超时分层的语义（headers 前 vs 总时长）——本题核心。
- AbortSignal.timeout + AbortSignal.any 组合。
- timeoutType 区分（诊断友好）——监控按类型聚合。
- clearTimeout 的清理纪律（连接成功后解除连接计时）。
