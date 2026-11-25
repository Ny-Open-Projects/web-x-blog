---
title: [AGT-497] 笔试题——实现前端 Agent SDK（流式订阅+取消+错误类型化）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-497：手写 SDK：流式订阅 API、取消、错误类型化、自动重连

**需求与边界**：
- 输入：会话 id、回调；输出：SDK 对象（subscribe/cancel/状态）。
- 边界要求：① 事件订阅 API（on 按类型分发）；② cancel 级联（前端流+服务端）；③ 错误类型化（可重试/致命/权限，调用方可分支处理）；④ 断线自动重连（指数退避+seq 续传）+ 最终失败回调。

**答**：
```javascript
class AgentSDK {
  constructor({ convId, transport }) {
    this.convId = convId; this.t = transport;
    this.handlers = new Map();
    this.retry = 0; this.cancelled = false;
  }
  on(type, fn) {                                 // 类型化订阅
    (this.handlers.get(type) ?? this.handlers.set(type, [])
      .get(type)).push(fn);
    return () => this.off(type, fn);             // 退订函数
  }
  emit(type, payload) {
    (this.handlers.get(type) ?? [])
      .forEach(fn => { try { fn(payload); }
        catch (e) { console.error('handler error', e); } });
  }
  async start() {
    try {
      await this.t.connect(this.convId, {
        lastEventId: this.lastSeq,
        onEvent: (ev) => {
          this.lastSeq = ev.seq;
          this.emit(ev.type, ev.payload);
        },
        onClose: () => this.reconnect(),         // 断线重连
      });
      this.retry = 0;
    } catch (e) {
      this.emit('error', typedError(e));         // 类型化错误
    }
  }
  async reconnect() {
    if (this.cancelled) return;
    if (++this.retry > 5) {
      this.emit('error', { type: 'fatal',
        code: 'CONNECTION_LOST',
        recoverable: false });                   // 最终失败
      return;
    }
    await sleep(2 ** this.retry * 500);
    return this.start();                         // 续传 lastSeq
  }
  async cancel() {                               // 级联取消
    this.cancelled = true;
    this.t.close();
    await this.t.postCancel(this.convId);        // 服务端级联
    this.emit('cancelled', { convId: this.convId });
  }
}
const typedError = (e) => e.code === 401
  ? { type: 'auth', recoverable: false }
  : e.code === 429 ? { type: 'rate_limit',
      recoverable: true, retryAfter: e.headers?.retryAfter }
  : { type: 'unknown', recoverable: true };
// 调用方：sdk.on('delta', render); sdk.on('error', e =>
//   e.type === 'rate_limit' ? retryLater(e.retryAfter) : showError(e));
```

**评分点**:
- 类型化订阅/退订 API + handler 异常隔离（不互相拖垮）。
- 错误类型化（auth/rate_limit/unknown + recoverable），调用方可分支处理。
- 重连指数退避+上限+seq 续传，最终失败显式回调。
- cancel 级联（本地流+服务端）。
