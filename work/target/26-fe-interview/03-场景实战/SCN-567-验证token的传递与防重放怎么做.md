---
title: [SCN-567] 验证通过后的 token 传递与防重放怎么设计？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-567：验证 token 传递与防重放怎么设计？
**答**：
- 一次性令牌：验证通过换取短期（60~120 秒）一次性 token，绑定场景 + 用户 + 会话，业务请求携带，服务端消费即作废。
- 绑定语义：token 绑定本次业务参数摘要（如订单号），换订单不可复用——防止「A 单验证，B 单使用」。
- 传递规范：token 只进请求头/体，不进 URL；不写 localStorage（XSS 可窃取后重放窗口内滥用），放内存 + JS 变量。
- 重放防御：客户端防重（用后即删 + 单飞）+ 服务端防重（token 已消费返回特定错误码，前端引导重新验证）。
- 追问钩子：token 过期了但用户刚验证完——体验上给「验证已过期，请重新验证」明确提示并自动重新发起，而不是报系统错误。

```javascript
async function payWithVerify(order) {
  const { token } = await riskGuard('pay');       // 一次性 token，存内存
  try {
    return await api.post('/pay', {
      orderId: order.id,
      riskToken: token,
      bizDigest: sha256(JSON.stringify({ id: order.id, fen: order.amountFen })), // 参数绑定
    });
  } catch (e) {
    if (e.code === 'TOKEN_USED' || e.code === 'TOKEN_EXPIRED') {
      toast('验证已过期，正在重新验证');
      return payWithVerify(order);                // 重新走验证，不吞错误
    }
    throw e;
  }
}
```
