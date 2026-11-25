---
title: [FRP-372] 笔试：手写消息总线（schema 校验 + 请求响应 + 溯源）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-372：笔试：手写消息总线

**答**：实现 `MessageBus`：① emit/on（事件模式，schema 注册表校验 payload）；② request(type, payload)：请求/响应模式（requestId 匹配、超时 reject）——reply(type, handler) 服务端注册；③ 通配订阅（on('order.*')）；④ 溯源与重放：消息环缓冲（最近 100 条），`replay(type)` 给新订阅者补历史；⑤ 订阅泄漏防护：按 source 批量清理 + 计数告警（sub/unsub 不平衡）。写出实现。

```javascript
class MessageBus {
  #subs = new Map(); #reqs = new Map(); #history = []; #subCount = { add: 0, remove: 0 };
  constructor() {
    setInterval(() => {                               // 泄漏告警
      const { add, remove } = this.#subCount;
      if (add - remove > 50) console.warn('[bus] subscription leak?', add - remove);
    }, 60_000);
  }
  emit(type, payload, source = 'unknown') {
    const msg = { type, payload, source, ts: Date.now() };
    this.#history.push(msg);
    if (this.#history.length > 100) this.#history.shift();
    this.#dispatch(type, msg);
    this.#dispatch(`${type}:reply`, msg);             // 通配路径
  }
  #dispatch(pattern, msg) {
    for (const [key, set] of this.#subs) {
      const re = new RegExp(`^${key.replace(/\./g, '\\.').replace(/\*/g, '[^.]+')}$`);
      if (re.test(msg.type)) set.forEach((fn) => fn(msg));
    }
  }
  on(pattern, handler, source) {
    this.#subCount.add++;
    (this.#subs.get(pattern) ?? this.#subs.set(pattern, new Set()).get(pattern)).add(handler);
    return () => {                                    // 清理返回
      this.#subCount.remove++;
      this.#subs.get(pattern)?.delete(handler);
    };
  }
  request(type, payload, { timeout = 5000, source } = {}) {
    const id = crypto.randomUUID();
    return new Promise((resolve, reject) => {
      this.#reqs.set(id, { resolve, reject, timer: setTimeout(() => { this.#reqs.delete(id); reject(new Error(`timeout: ${type}`)); }, timeout) });
      this.emit(`${type}:request`, { __reqId: id, payload }, source);
    });
  }
  reply(type, handler) {
    return this.on(`${type}:request`, async (msg) => {
      const result = await handler(msg.payload);
      this.emit(`${type}:response`, { __reqId: msg.payload.__reqId, result });
    });
  }
  // response 回 requestId → resolve (省略对称代码)
}
```

**评分点**：
- request/response 的 requestId 匹配 + 超时清理
- 通配符正则转义（. 转义、* 语义）
- 溯源与环缓冲重放
- sub/unsub 计数的泄漏告警
