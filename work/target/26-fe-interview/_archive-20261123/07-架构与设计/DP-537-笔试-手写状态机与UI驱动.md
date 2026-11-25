---
title: [DP-537] 笔试：手写购物流程状态机
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-537：笔试：手写购物状态机

**题目**：实现下单流程状态机 `CheckoutMachine`：① 状态：idle → selecting → confirming → paying → paid/failed；② 每迁移的 guard：selecting→confirming 需「购物车非空+地址完整」——guard 组合多个条件；③ 不可逆点：paid 后只能退款不能回 paying（数据已变）——终态语义；④ 异步迁移：paying 状态的进入是异步的（prepay 请求）——迁移的异步 guard/action；⑤ 超时迁移：paying 超 15 分钟 → 自动 expired（超时守卫——定时器触发迁移）。写出实现。

```javascript
class CheckoutMachine {
  #state = 'idle'; #ctx = {}; #subs = new Set(); #timer = null;
  static GUARDS = {
    confirming: (ctx) => ctx.cart.length > 0 && !!ctx.address
      ? { pass: true } : { pass: false, reason: '购物车空或地址缺失' },
    paying: async (ctx) => {
      const prepay = await api.prepay(ctx.orderId);    // 异步 guard
      ctx.payParams = prepay;
      return { pass: true };
    },
  };
  async send(event, payload = {}) {
    const guard = CheckoutMachine.GUARDS?.[event];
    if (guard) {
      const ok = await guard({ ...this.#ctx, ...payload });
      if (!ok.pass) return { ok: false, reason: ok.reason };
    }
    const next = this.#next(event, payload);
    this.#ctx = { ...this.#ctx, ...payload };
    if (this.#state === 'paying')                      // 超时守卫
      this.#timer = setTimeout(() => this.send('timeout'), 15 * 60e3);
    if (this.#state === 'paid' || this.#state === 'expired') clearTimeout(this.#timer);
    this.#state = next;
    this.#subs.forEach((f) => f(this.#state, this.#ctx));
    return { ok: true, state: next };
  }
  #next(event, payload) { /* 迁移表查询 */ }
}
```

**评分点**：
- guard 组合多条件（购物车+地址——组合校验）
- 异步迁移（paying 的 prepay 预检——异步 guard）
- 不可逆点的终态语义（paid 不可回 paying）
- 超时迁移（paying 15 分钟自动 expired——定时器守卫）
