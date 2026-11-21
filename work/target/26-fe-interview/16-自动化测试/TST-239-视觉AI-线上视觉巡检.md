---
title: [TST-239] 如何用视觉手段做「线上页面巡检」（监控而不是测试）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-239：如何用视觉手段做「线上页面巡检」（监控而不是测试）？
**答**：
- 定时对关键页面（首页/商详/结算）截图，与「健康基线」比 pHash/像素。
- 异常漂移告警（CDN 样式丢失/灰度发布异常/第三方脚本破坏布局）。
- 多地域多运营商拨测截图——覆盖 CDN 节点差异。
- 巡检告警分级：整页白屏/大面积异常立即呼人，小面积漂移进日报。

```javascript
// 线上巡检 job（每 15 分钟）
const shot = await capture('https://www.example.com', { viewport: desktop });
const d = hamming(await pHash(shot), await pHash(baseline));
if (d > 12) alertPager({ level: 'P1', reason: '视觉大幅漂移', distance: d });
r
```
