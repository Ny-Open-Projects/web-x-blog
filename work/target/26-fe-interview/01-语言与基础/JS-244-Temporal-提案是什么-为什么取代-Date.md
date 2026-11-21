---
title: [JS-244] Temporal 提案是什么：为什么取代 Date
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-244：Temporal 提案：为什么取代 Date

**答**：
- Date 的历史债：月份从 0 起、无时区模型（只有 UTC 与本地）、不可变性与可变性混乱、解析不可靠
- Temporal 的核心类型：PlainDate/PlainTime（无时区）、ZonedDateTime（带时区）、Instant（绝对时刻）、Duration——「时间点、日历时间、时间段」分层清晰
- 能力亮点：任意时区换算正确、日历系统（非公历）、日期运算（加月不溢出）、格式化与解析标准化
- 现状（2026）：Chrome/Edge 已实验落地，推进中；生产仍以 date-fns/dayjs/Temporal polyfill 为主
- 面试话术：举一个 Date 的坑（月份 0 起或时区换算错误）+ Temporal 的对应解法即可

```javascript
// Date 的坑：月份从 0 起
new Date(2026, 10, 19);  // 这是 11 月不是 10 月！
// Temporal：明确且不可变
Temporal.PlainDate.from('2026-11-19').add({ months: 1 }); // 2026-12-19
Temporal.ZonedDateTime.from('2026-11-19T10:00[Asia/Shanghai]')
  .withTimeZone('America/New_York'); // 正确换算到纽约时间
```
