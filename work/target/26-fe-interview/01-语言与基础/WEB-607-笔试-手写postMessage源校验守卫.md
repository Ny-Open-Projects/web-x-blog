---
title: [WEB-607] 笔试：手写 postMessage 安全守卫
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 安全]
type: 笔试题
---

## WEB-607：笔试：手写 postMessage 安全守卫

**答**：实现 `SafePost`：① `listen(handlers)`：注册 message 监听，强制校验 `event.origin` 在白名单、消息带约定 token 字段、来源 `event.source` 与注册时传入的窗口一致；② 三项任一不通过直接丢弃并计数（审计用）；③ `send(targetWin, targetOrigin, msg)`：发送时 targetOrigin 必须是具体 origin（禁止 `'*'`）；④ 消息结构带 `__id`/`__ts`，接收侧丢弃 10s 前的旧消息（防重放）。写出核心实现。

```javascript
class SafePost {
  constructor(allowedOrigins, token) {
    this.origins = new Set(allowedOrigins); this.token = token;
    this.handlers = new Map(); this.rejected = 0; this.sources = new Set();
  }
  registerSource(win) { this.sources.add(win); }
  listen(handlers) {
    addEventListener('message', (e) => {
      if (!this.origins.has(e.origin)) { this.rejected++; return; }        // 1. origin 白名单
      if (e.data?.__token !== this.token) { this.rejected++; return; }     // 2. 应用层 token
      if (this.sources.size && !this.sources.has(e.source)) { this.rejected++; return; } // 3. 来源窗口
      if (Date.now() - (e.data.__ts || 0) > 10_000) { this.rejected++; return; }         // 4. 防重放
      const h = this.handlers.get(e.data.__type) || handlers[e.data.__type];
      h?.(e.data.payload, e);
    });
  }
  send(targetWin, targetOrigin, type, payload) {
    if (targetOrigin === '*' || !this.origins.has(targetOrigin)) throw new Error('unsafe origin');
    targetWin.postMessage({ __type: type, __token: this.token, __ts: Date.now(), payload }, targetOrigin);
  }
}
```

**评分点**：
- 四重校验：origin 白名单 / 应用 token / 来源窗口 / 时间窗防重放
- 发送侧禁止 '*'，明确 targetOrigin 通配符的风险
- 拒绝计数可审计，异常来源可追查
- 能解释为什么仅靠 origin 校验不够（嵌入式页面被 XSS 后 origin 相同）
