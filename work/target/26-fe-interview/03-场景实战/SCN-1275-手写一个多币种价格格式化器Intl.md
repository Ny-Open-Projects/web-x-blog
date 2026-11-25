---
title: [SCN-1275] 手写一个多币种价格格式化器（Intl 精度与显示）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## SCN-1275：手写一个多币种价格格式化器（Intl 精度与显示）

**答**：
- 需求：implement PriceFormatter(locale)。format(amount, currency) 按 Intl 规则（JPY 0 位、其他 2 位）；convert(amount, rate, target) 换算并标注汇率时间；compare(a, b) 跨币种比较（先换算基准币）。
- 边界：rate 缺失抛错；金额负数（退款）格式正确；amount 非数字抛错。
- 评分点：Intl 格式；JPY 精度；汇率标注；跨币比较

```javascript
class PriceFormatter {
  constructor(locale = 'en') { this.locale = locale; }
  format(amount, currency) {
    if (typeof amount !== 'number' || Number.isNaN(amount))
      throw new Error('amount 必须为数字');
    const digits = currency === 'JPY' ? 0 : 2;
    return new Intl.NumberFormat(this.locale, { style: 'currency',
      currency, minimumFractionDigits: digits,
      maximumFractionDigits: digits }).format(amount);
  }
  convert(amount, rate, target) {
    if (!rate?.value) throw new Error('缺少汇率');
    return { amount: +(amount * rate.value).toFixed(2), currency: target,
      rateAt: rate.ts };
  }
  compare(a, b, rates) {
    const toUSD = x => x.currency === 'USD' ? x.amount
      : x.amount / rates[x.currency].value;
    return toUSD(a) - toUSD(b);
  }
}
```
