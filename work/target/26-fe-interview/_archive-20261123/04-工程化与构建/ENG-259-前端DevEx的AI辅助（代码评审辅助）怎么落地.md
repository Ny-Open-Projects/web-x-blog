---
title: [ENG-259] AI 辅助代码评审怎么落地才不添乱？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-259：AI 辅助评审怎么落地？
**答**：
- 定位：AI 做「第一层筛查」（lint 级问题/测试缺失/明显 bug 模式），人做「语义与架构判断」——AI 评审的价值是前置消化低价值意见，让人聚焦。
- 降噪设计：AI 意见分级（must-fix/consider/nit），must-fix 才要求作者响应；意见必须附代码位置与理由，禁止泛泛建议。
- 反馈闭环：评审意见的采纳率统计，采纳率低的意见类型自动降级或关闭——AI 评审不治理会退化成噪音机。
- 上下文注入：评审 prompt 带团队规范（ENG-214 规则）+ 相关模块的 ADR 摘要，让意见贴合团队约定。
- 追问钩子：为什么 AI 评审必须「意见分级」——没有分级时 AI 会输出 30 条 nit 淹没 1 条真 bug，作者开始无差别忽略 AI 意见，工具价值归零；分级维持信号噪声比是 AI 评审的生死线。

```javascript
// AI 评审输出协议
{ level: 'must-fix', line: 42,
  reason: '未处理竞态：连续调用会互相覆盖', fix: '使用 AbortController' },
{ level: 'nit', line: 8, reason: '命名可更语义化' }
// 降噪闭环
if (adoptionRate(level) < 0.2) disableRule(level);
```
