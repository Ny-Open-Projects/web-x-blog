---
title: [ARC-087] 开放平台的第三方接入 JS SDK 如何设计（安全域）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-087：开放平台的第三方接入 JS SDK 如何设计（安全域）？
**答**：
- 模型：第三方页面嵌入我们的 JS SDK，SDK 与我们的 iframe/服务通信。安全边界靠 iframe 沙箱 + postMessage 白名单（origin 校验）+ 受控 API 面。
- 三方凭据：第三方拿 client_id，敏感操作走 OAuth 授权码流程，SDK 内不出现长期 secret。
- API 设计：显式授权每个能力（`authorize(scope)`），回调通过消息签名 + 时间戳防重放。

```typescript
// 开放平台 SDK：iframe 沙箱 + postMessage 白名单协议
class OpenSdk {
  private allowedOrigins = ['https://open.corp.com'];
  private pending = new Map<string, (v: unknown) => void>();

  constructor(private clientId: string) {
    window.addEventListener('message', e => {                 // 收消息：先验 origin
      if (!this.allowedOrigins.includes(e.origin)) return;    // 白名单校验，防伪造
      const { reqId, result } = e.data;
      this.pending.get(reqId)?.(result);
      this.pending.delete(reqId);
    });
  }
  private rpc(method: string, payload: unknown): Promise<unknown> {
    return new Promise(resolve => {
      const reqId = crypto.randomUUID();
      this.pending.set(reqId, resolve);
      this.iframe!.contentWindow!.postMessage(                // 发消息：指定目标 origin，不用 *
        { sdk: this.clientId, reqId, method, payload, ts: Date.now(), sig: sign(method, payload) },
        'https://open.corp.com',
      );
    });
  }
  authorize(scope: string) { return this.rpc('oauth.authorize', { scope, redirect: location.origin }); } // OAuth 授权码
  pay(order: OrderDto)    { return this.rpc('pay.create', order); }
  getUser()               { return this.rpc('user.info', null); }
}
// 安全要点：iframe sandbox 属性限权；消息带 ts+sig 防重放；API 按.scope 审计与限流
```

---

## 十、低代码与平台化（ARC-088 ~ ARC-100）
