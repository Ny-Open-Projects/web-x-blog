---
title: [TST-747] AI 做「日志异常检测」辅助性能归因的思路与陷阱
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-747：AI 做「日志异常检测」辅助性能归因的思路与陷阱

**答**：
- 结论：日志异常检测能快速缩小归因范围，但陷阱是「正常变更引起日志模式变化」被误判为异常，需结合发布事件做上下文抑制。
- 思路：日志模板化（把变量抽成占位符）后统计模板频率，突增/突降的模板作为异常信号。
- 陷阱：日志量随流量波动、采样率变化、新增日志打点都会造成假异常，要先归一化再检测。
- 追问钩子：异常检测告警太多被静音，如何恢复有效性？

```javascript
// 日志模板化 + 频率突增检测
function templatize(line) {
  return line.replace(/\d+/g, '<N>').replace(/[0-9a-f]{8,}/gi, '<ID>');
}
function detectBurst(baseline, current, factor) {
  const out = [];
  for (const [tpl, cnt] of Object.entries(current)) {
    const base = baseline[tpl] || 0;
    if (cnt > base * factor && cnt > 10) out.push({ tpl, base, current: cnt });
  }
  return out;
}
console.log(detectBurst(
  { 'user <N> login': 5 },
  { 'user <N> login': 200 }, 3
)); // 突增
```
