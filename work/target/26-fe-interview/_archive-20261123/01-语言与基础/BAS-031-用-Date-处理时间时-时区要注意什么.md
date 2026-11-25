---
title: [BAS-031] 用 Date 处理时间时，时区要注意什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-031：用 Date 处理时间时，时区要注意什么？
**答**：
- `new Date('2026-01-01')`（ISO 日期）按 UTC 零点解析；`new Date('2026/01/01')` 按本地时区解析，在东八区两者相差 8 小时。
- getHours 是本地时区，getUTCHours 是 UTC；展示前必须明确数据是本地时间还是 UTC。
- 跨端传输用时间戳或 ISO 字符串，展示交给 dayjs 等库，禁止手写字符串拼日期。

```javascript
new Date('2026-01-01').getHours();    // 8：UTC 零点在东八区是本地 8 点
new Date('2026/01/01').getHours();    // 0：按本地时区解析
new Date('2026-01-01').toISOString(); // '2026-01-01T00:00:00.000Z'
Date.now();                           // 时间戳与时区无关，传输首选
```
