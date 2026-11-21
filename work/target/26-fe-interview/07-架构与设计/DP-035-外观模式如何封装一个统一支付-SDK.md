---
title: [DP-035] 外观模式：如何封装一个统一支付 SDK？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-035：外观模式：如何封装一个统一支付 SDK？
**答**：
- 外观：为复杂子系统提供一致的高层入口，调用方不需要知道内部有多少模块、如何编排。
- 前端场景：支付 SDK（内部有渠道选择、风控、埋点、降级）、上报 SDK、地图 SDK。
- 与适配器区别：适配器解决"接口不兼容"，外观解决"子系统太复杂"，外观通常还会做流程编排。
- 收益：底层子系统可整体替换（如支付宝 SDK 换版本），业务侧只认识 `pay()`。

```javascript
// 复杂子系统：业务方不该直接碰这些
const riskApi = { check: (order) => order.amount < 100000 };     // 风控
const channelApi = {                                             // 渠道路由
  wechat: (o) => Promise.resolve(`wx_${o.orderId}`),
  alipay: (o) => Promise.resolve(`ali_${o.orderId}`),
};
const reportApi = { send: (e, d) => console.log('[report]', e, d) }; // 埋点

// 外观：统一入口 + 流程编排
class PaySDK {
  pay({ channel = 'wechat', ...order }) {
    reportApi.send('pay_start', { channel, orderId: order.orderId });
    if (!riskApi.check(order)) {                    // 编排1：风控
      reportApi.send('pay_blocked', { orderId: order.orderId });
      return Promise.reject(new Error('风控拦截'));
    }
    const fn = channelApi[channel] || channelApi.wechat; // 编排2：渠道分发（兜底策略）
    return fn(order).then((tradeNo) => {            // 编排3：调用渠道
      reportApi.send('pay_success', { tradeNo });   // 编排4：上报
      return tradeNo;
    }).catch((err) => {
      reportApi.send('pay_fail', { msg: String(err) });
      throw err;
    });
  }
}
// 业务方只需要认识一个入口
const paySDK = new PaySDK();
paySDK.pay({ orderId: 'A1', amount: 99 }).then(console.log); // [report] pay_start ... wx_A1
// 子系统升级（如渠道 API 换签名方式）不影响任何业务调用方
```
