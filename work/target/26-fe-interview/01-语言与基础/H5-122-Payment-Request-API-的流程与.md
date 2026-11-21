---
title: [H5-122] Payment Request API 的流程与现状如何？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-122：Payment Request API 的流程与现状如何？
**答**：
- 模型：`new PaymentRequest(methodData, details, options)` → `canMakePayment()` 探测 → `show()` 弹出**浏览器/系统级支付面板**（Apple Pay、Google Pay、保存的卡）→ `paymentresponse` 回调交给服务端处理 → `complete('success'|'fail')` 收尾。
- 收益：免自绘收银台、复用系统级免密支付与卡管理、脱敏（商家拿不到完整卡号）；用户地址/联系方式可由浏览器代填（options.requestShipping/requestPayerEmail）。
- 现状：Apple Pay 场景强（Safari 必经之路），Chrome 系与 Google Pay 集成良好；部分平台已推荐直接用支付服务商 SDK（其底层仍可能走 Payment Request）。
- 必须在用户手势内 `show()`；`details` 金额变动（改地址重算运费）用 `paymentRequest.addEventListener('shippingaddresschange')`。
- 永远要有降级收银台：canMakePayment false 或 API 异常时回退到自建支付页。

```javascript
const methods = [
  { supportedMethods: 'basic-card' },                       // 通用卡
  // { supportedMethods: 'https://apple.com/apple-pay' },   // Apple Pay 配置对象
];

const details = {
  id: 'order-20261107-001',
  total: { label: '应付总额', amount: { currency: 'CNY', value: '199.00' } },
  displayItems: [
    { label: '机械键盘', amount: { currency: 'CNY', value: '189.00' } },
    { label: '运费', amount: { currency: 'CNY', value: '10.00' } },
  ],
};

const request = new PaymentRequest(methods, details, {
  requestShipping: false,
  requestPayerEmail: true,
});

checkoutBtn.addEventListener('click', async () => {
  if (!window.PaymentRequest || !(await request.canMakePayment())) {
    return location.href = '/checkout/fallback';            // 降级收银台
  }

  const response = await request.show();                    // 系统支付面板

  try {
    const { success } = await fetch('/api/pay', {
      method: 'POST',
      body: JSON.stringify(serializePayment(response)),
    }).then(r => r.json());
    await response.complete(success ? 'success' : 'fail');
    if (success) location.href = `/paid/${details.id}`;
  } catch {
    await response.complete('fail');
  }
});

// 收货地址变化重算运费：更新 details 再调 updateWith
request.addEventListener('shippingaddresschange', async (e) => {
  e.updateWith((async () => {
    const freight = await calcFreight(request.shippingAddress);
    details.displayItems[1].amount.value = freight;
    details.total.amount.value = String(189 + Number(freight));
    return details;
  })());
});
```
