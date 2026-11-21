---
title: [DP-232] 源码识别：Intl API 设计中的适配器与本地化策略？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-232：源码识别：Intl API 设计中的适配器与本地化策略？
**答**：
- 策略（内置）：Intl.* 的 locale 参数就是"策略选择器"——同接口不同语言实现由浏览器内置策略分发（CLDR 数据），开发者零适配。
- 适配器（应用侧）：应用把自定义数据源（自家文案表/汇率表）适配成 Intl 消费格式——Intl.NumberFormat 只有固定币种表，自定义单位用 useGrouping 组合。
- 备忘录（应用侧优化）：Intl 实例构造昂贵，按 (locale, options) 键缓存——DP-254 思想，面试常考。
- 识别要点：Intl.DateTimeFormat 的 formatToParts 是"分解渲染"设计——把格式化结果拆成部件供 UI 定制（比字符串替换更稳）。

```javascript
// Intl 实例缓存（备忘录，应用侧）
const cache = new Map();
function cachedFmt(locale, opts) {
  const k = `${locale}|${JSON.stringify(opts)}`;
  return cache.get(k) ?? cache.set(k, new Intl.DateTimeFormat(locale, opts)).get(k)!;
}
// formatToParts：部件级适配
const parts = cachedFmt('zh-CN', { dateStyle: 'medium', timeStyle: 'short' }).formatToParts(new Date());
// → [{type:'year', value:'2026'}, {type:'literal', value:'/'}...] —— UI 可对 year 部分单独染色
// 自定义单位适配：Intl.NumberFormat(locale, { style: 'unit', unit: 'kilometer-per-hour' })
// 不支持的单位 → 应用层适配器：unitTable = { '元': n => `${n} 元` } 兜底
```
