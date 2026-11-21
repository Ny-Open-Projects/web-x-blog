---
title: [HW-180] 手写列表本地化格式化——Intl.ListFormat（and/or 单元）与超长列表折叠（A, B 及其他 12 项）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：列表展示本地化（"A、B 和 C" vs "A, B, and C"）：Intl.ListFormat（conjunction/disjunction）自动处理连接词与顿号；超长列表折叠（显示前 3 + "及其他 N 项"，N 的文案本地化）；单元素/空列表边界。

```javascript
const lfCache = new Map();
function listFmt(locale, type = 'conjunction') {          // conjunction: 和 / disjunction: 或
  const key = `${locale}|${type}`;
  return lfCache.get(key) ?? lfCache.set(key, new Intl.ListFormat(locale, { type })).get(key);
}
function formatList(items, locale, { max = 3 } = {}) {
  if (!items.length) return locale.startsWith('zh') ? '暂无' : 'None';
  if (items.length === 1) return items[0];
  if (items.length <= max) return listFmt(locale).format(items);
  const shown = listFmt(locale).format(items.slice(0, max));
  const rest = items.length - max;
  const more = locale.startsWith('zh') ? `及其他 ${rest} 项` : ` and ${rest} more`;
  return shown + more;                                    // "张三、李四和王五及其他 12 项"
}
// formatList(['a','b','c'], 'zh') => "a、b 和 c"
// formatList(['a','b','c','d','e','f'], 'en') => "a, b, c and 3 more"
// disjunction 场景：筛选器"支持 A、B 或 C 格式"（type: 'disjunction' 自动 "或"）
// 实例缓存（HW-125 同源：Intl 构造昂贵）
```

**评分点**：
- ListFormat conjunction/disjunction 自动连接词（手写顿号/and 不本地化是反例）。
- 超长折叠（前 N + 本地化"及其他"）。
- 单元素/空边界。
- Intl 实例缓存。
