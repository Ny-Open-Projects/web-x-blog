---
title: [MP-111] 微信/支付宝/抖音小程序的 API 差异怎么用一个映射层抹平？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-111：微信/支付宝/抖音小程序的 API 差异怎么用一个映射层抹平？
**答**：
- 三端命名规律：微信 `wx.*`，支付宝 `my.*`，抖音 `tt.*`；支付/登录/分享等核心 API 参数结构也有差异（如支付字段 `timeStamp` vs `time_stamp`）。
- 统一做法：封装 **platform adapter**，业务只调 `uniPayment()`/`uniLogin()`，适配层内部按 `process.env`（Taro）或条件编译（uni-app）分发到各端实现。
- 差异映射要维护成表：API 名、参数差异、返回差异、是否需要权限/资质，作为适配层单测的依据。
- 抹平不了的能力（如某些端没有的组件）必须显式抛错或降级，不能静默失败。

```javascript
// 平台适配层：支付与登录的差异收敛
const platform = typeof wx !== 'undefined' ? 'wechat' : typeof my !== 'undefined' ? 'alipay' : 'douyin'

function uniLogin() {
  if (platform === 'wechat') return wx.login()
  if (platform === 'alipay') return my.getAuthCode({ scopes: 'auth_base' }) // 返回 authCode
  return tt.login()
}
function uniPay(order) {
  if (platform === 'wechat') return wx.requestPayment({
    timeStamp: order.timeStamp, nonceStr: order.nonceStr,
    package: order.package, signType: order.signType, paySign: order.paySign
  })
  if (platform === 'alipay') return my.tradePay({ tradeNO: order.tradeNO }) // 支付宝用 tradeNO
  return tt.pay({ orderInfo: order.orderInfo })                            // 抖音用 orderInfo
}
```
