---
title: [HW-149] 手写多时区时间显示——Intl.DateTimeFormat timeZone 复用与相对时间降级链
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-149：手写多时区时间显示——Intl.DateTimeFormat timeZone 复用与相对时间降级链
**答**：IM/跨境协作的多时区显示：① Intl.DateTimeFormat 实例按 locale+timeZone 缓存（HW-125 同款纪律）；② 相对时间（3 分钟前）用 Intl.RelativeTimeFormat 分档；③ 降级链：同日→时刻、同年→月日、跨年→完整日期（本地化格式自动正确）。

```javascript
const dtfCache = new Map();
function fmt(locale, timeZone, opts) {
  const key = `${locale}|${timeZone}|${JSON.stringify(opts ?? {})}`;
  return dtfCache.get(key) ?? dtfCache.set(key,
    new Intl.DateTimeFormat(locale, { timeZone, ...opts })).get(key);
}
function smartDate(ts, locale = navigator.language, tz) {
  const now = Date.now();
  const diffMin = (now - ts) / 60000;
  if (diffMin < 1) return new Intl.RelativeTimeFormat(locale).format(-0, 'second');
  if (diffMin < 60) return new Intl.RelativeTimeFormat(locale).format(-Math.floor(diffMin), 'minute');
  const d = new Date(ts), n = new Date();
  const sameYear = d.getFullYear() === n.getFullYear();
  const sameDay = d.toDateString() === n.toDateString();
  if (sameDay) return fmt(locale, tz, { hour: '2-digit', minute: '2-digit' }).format(d);       // 同日：时刻
  if (sameYear) return fmt(locale, tz, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }).format(d);
  return fmt(locale, tz, { year: 'numeric', month: 'short', day: 'numeric' }).format(d);      // 跨年：全日期
}
// smartDate(todayTs) => "14:32"；smartDate(lastMonthTs) => "10月8日 09:15"；跨年 => "2024年12月30日"
// 实例缓存（Intl 构造昂贵）；RelativeTimeFormat 分档（秒/分/时/天）自动本地化（"3分钟前" vs "3 min ago"）
```

**评分点**：
- DateTimeFormat 实例缓存；timeZone 参数显式（服务端 UTC 时间戳 + 本地/指定时区渲染）。
- 相对时间分档（RelativeTimeFormat）与降级链（同日/同年/跨年）。
- locale 参数化（跟随用户或指定）。
- 能说出 Intl 实例化的开销与复用收益（HW-125 同源）。
