---
title: [SOFT-698] 手写 qaBudget：陈述实际用时→问答剩余时间分配、问题数预算、超时截断话术？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-698：手写 qaBudget：陈述实际用时→问答剩余时间分配、问题数预算、超时截断话术

**需求与边界**：
- 实现 qaBudget(total, used)。
- 边界要求：① 问答时长 = 总时长-实际陈述用时（含缓冲 1 分钟）；② 问题数预算按“每答 90 秒”估（给评委预期）；③ 陈述超时压缩问答时给“截断话术”（答辩人主动声明“问答时间紧，我每答控制在 60 秒”）；④ 剩余 <5 分钟时建议“只答 must 类问题”策略。

**答**：
```javascript
function qaBudget(totalMin, usedMin, { buffer = 1 } = {}) {
  const qa = +(totalMin - usedMin - buffer).toFixed(1);
  if (qa <= 0)
    return { emergency: true,
      action: '陈述已超时——立即进入总结，问答改为会后书面' };
  const questions = Math.floor(qa * 60 / 90);        // 每答90秒
  const out = { qaMin: qa, questionBudget: questions,
    perAnswerSec: qa * 60 / Math.max(questions, 1) };
  if (usedMin > totalMin * 0.8)
    out.overtime = { statement: '陈述超时（规划15min用了' + usedMin + '）',
      tactic: `问答压缩：每答${Math.min(60, out.perAnswerSec)}秒内，优先答技术深度与贡献边界类` };
  if (qa < 5)
    out.mustOnly = '剩余不足5分钟：只答must问题（设计取舍/贡献边界/数据口径），其余致谢转书面';
  return out;
}
```

**评分点**:
- 实时按陈述用时动态分配问答（时间轴的下半场管理）。
- 超时截断话术与 must-only 策略（时间不足时的降级路径明确）。

