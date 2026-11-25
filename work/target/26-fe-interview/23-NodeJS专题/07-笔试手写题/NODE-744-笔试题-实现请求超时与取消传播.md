---
title: [NODE-744] 笔试题——实现请求超时与取消传播（AbortController 贯穿）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-744：手写取消传播

**需求与边界**：
- 需求：客户端断开/超时的取消传播（SCN-NODE-642）——① 客户端断开感知（req close → abort）；② 下游调用继承 signal（AbortSignal.any 组合——客户端断开+超时双源）；③ 取消清理（handler 内监听 abort——清理在途工作）；④ 取消原因区分（client-disconnect vs timeout——监控分桶）。
- 边界：① AbortSignal.any（多源组合——Node 20）；② signal 透传到 DB 查询（pg query signal——DB 端也取消）；③ 取消后 handler 的 finally 清理（临时数据删除）。

**答**：
```javascript
app.get('/report', async (req, res) => {
  const clientGone = new AbortController();
  req.on('close', () => clientGone.abort('client-disconnect'));   // 客户端断开感知
  const timeout = AbortSignal.timeout(30_000);
  const signal = AbortSignal.any([clientGone.signal, timeout]);   // 双源组合（Node 20）
  try {
    const rows = await db.query('SELECT ...', { signal });       // DB 也取消（query cancel）
    const ext = await callDownstream({ signal });                // 下游也取消
    res.json(merge(rows, ext));
  } catch (e) {
    if (e.name === 'AbortError') {
      cleanup(req);                                              // finally 清理（临时数据）
      report({ type: signal.reason === 'client-disconnect' ? 'CLIENT_GONE' : 'TIMEOUT',
        reason: signal.reason });                                // 分桶监控
      if (!res.headersSent) res.status(499).end();               // 499 客户端断开
    } else throw e;
  }
});
```

**评分点**:
- 双源组合（客户端断开 + 超时——AbortSignal.any）。
- 取消传播到 DB（pg signal——DB 端查询也取消，资源回收）。
- 取消原因分桶监控（client-disconnect vs timeout——诊断分流）。
- handler finally 清理（临时数据不残留）。
