---
title: [AIC-091] 补全接受率（accept rate）能说明什么、不能说明什么？为什么它是最常被误读的指标？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-091：补全接受率（accept rate）能说明什么、不能说明什么？为什么它是最常被误读的指标？
**答**：
- 能说明：工具在当前代码风格/语言上的「贴合度」——接受率极低通常意味着补全确实没用，值得排查配置或上下文供给。
- 不能说明：生产力。接受一个 30 行补全不等于这 30 行正确可用；接受后被大改的比例（keystroke-after-accept）才是真实成本。
- 常见误读：管理层拿「接受率 40%」当「提效 40%」汇报——接受率是行为统计不是产出质量统计，两者没有换算关系。
- 更诚实的口径：接受后 10 分钟内未被修改的比例（留存补全率）、按语言/模块分层的接受率（前端补全在模板文件里通常虚高或虚低）。
- 追问钩子：正确用法是把接受率当「诊断信号」而不是「成绩单」——某目录接受率骤降，通常意味着该模块需要补 few-shot 或规则。

```javascript
// 接受率与留存补全率的双指标统计
function completionStats(events) {
  const shown = events.filter(e => e.type === 'shown').length;
  const accepted = events.filter(e => e.type === 'accepted').length;
  const retained = events.filter(e => e.type === 'accepted' && e.modifiedAfterMin(10) < 0.3).length;
  return {
    acceptRate: accepted / shown,
    retentionRate: retained / accepted,   // 接受后未大改的比例
    verdict: retained / accepted < 0.5 ? '补全质量存疑，检查上下文供给' : 'healthy',
  };
}
```
