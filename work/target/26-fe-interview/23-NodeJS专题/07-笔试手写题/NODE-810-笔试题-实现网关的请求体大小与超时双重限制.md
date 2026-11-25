---
title: [NODE-810] 笔试题——实现网关的请求体与超时双重限制（流式拦截）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-810：手写双重限制

**需求与边界**：
- 需求：请求体/超时限制（SCN-NODE-666/642）——① content-length 预检（超限立即 413）；② 流式中途超限断开（无 content-length 的 chunked——流中计数，SCN-NODE-666）；③ 请求总超时（慢上传/慢连接断开——socket 超时）；④ 限流的先置（超限请求不消耗下游——网关层拦截）。
- 边界：① 预检不可信（伪造 content-length 小值实际大——流中计数兜底）；② 断开的错误语义（413 vs 网络错误——客户端可区分）；③ 大上传的例外路由（文件上传白名单——SCN-NODE-666 直传分离）。

**答**：
```javascript
function bodyGuard({ maxBytes = 1e6, timeoutMs = 15_000 } = {}) {
  return (req, res, next) => {
    const cl = +req.headers['content-length'];
    if (cl > maxBytes) return res.status(413).end();   // 预检（SCN-NODE-666）
    let bytes = 0;
    req.on('data', (c) => {                            // 流中计数兜底（伪造 cl 防御）
      bytes += c.length;
      if (bytes > maxBytes) { req.destroy(); res.status(413).end(); }   // 中途断开
    });
    req.setTimeout(timeoutMs, () => {                  // 慢上传/慢连接（SCN-NODE-642）
      req.destroy(); res.status(408).end();
    });
    next();
  };
}
// 上传例外路由（直传分离——SCN-NODE-666）
router.post('/upload', skip(bodyGuard), ossDirectSign);
```

**评分点**:
- 预检 + 流中计数双兜底（伪造 content-length 防御——SCN-NODE-666）。
- 413/408 语义区分（客户端可行动）。
- socket 超时（慢连接清理——SCN-NODE-642）。
- 上传白名单路由（直传分离——SCN-NODE-666）。
