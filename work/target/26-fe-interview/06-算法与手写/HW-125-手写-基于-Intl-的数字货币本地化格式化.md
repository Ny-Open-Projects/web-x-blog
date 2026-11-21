---
title: [HW-125] 手写多币种格式化——Intl.NumberFormat 复用、大额缩写与币种符号位置本地化
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：金额本地化三坑：每次 new Intl.NumberFormat 昂贵（必须模块级缓存）；币种符号位置随 locale（$1,234 vs 1.234 US$）；大额缩写（¥1.2万 vs $1.2M）规则不同。封装一个复用缓存 + 缩写策略的格式化器。

```javascript
const fmtCache = new Map();                           // key: locale|currency|opts → 复用实例（性能核心）
function fmt(locale, currency, opts = {}) {
  const key = `${locale}|${currency}|${JSON.stringify(opts)}`;
  if (!fmtCache.has(key)) fmtCache.set(key, new Intl.NumberFormat(locale, {
    style: 'currency', currency, ...opts,
  }));
  return fmtCache.get(key);
}
const CNY = fmt('zh-CN', 'CNY');
CNY.format(12345.6);          // "¥12,345.60"
// 大额缩写：中文万/亿 与 英文 K/M/B 规则不同——分语言实现
const CNY_SHORT = fmt('zh-CN', 'CNY', { notation: 'compact', compactDisplay: 'long' });
CNY_SHORT.format(123456);     // "¥12.35万"
const USD_SHORT = fmt('en-US', 'USD', { notation: 'compact' });
USD_SHORT.format(123456);     // "$123K"
// 分单位安全（ALG-200）：输入永远是分（整数），格式化前除以 100 用字符串转或 BigInt 避免精度
function fmtFen(locale, currency, fen) {
  return fmt(locale, currency, { minimumFractionDigits: 2 }).format(Number(fen) / 100);
}
```

**评分点**：
- Intl.NumberFormat 实例模块级缓存（每次实例化的开销是本题性能核心）。
- 币种符号位置随 locale、缩写规则分语言（万/亿 vs K/M）。
- 与分单位金额模型衔接（fmtFen 入参是分）。
- 能说出 notation: compact 与 compactDisplay 差异。
