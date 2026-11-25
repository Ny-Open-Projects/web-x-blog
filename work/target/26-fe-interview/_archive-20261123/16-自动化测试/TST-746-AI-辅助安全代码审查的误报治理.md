---
title: [TST-746] AI 辅助「安全代码审查」的误报治理——人机协同机制
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-746：AI 辅助「安全代码审查」的误报治理——人机协同机制

**答**：
- 结论：AI 审查误报高会耗尽人工信任，机制上要「AI 只提名不定罪 + 反馈闭环持续优化」。
- AI 输出按置信度分层，高置信度进人工复核队列，低置信度只记录不打扰；人工判定结果回流为训练/规则样本。
- 建立「误报库」：同一模式被人工标误报后，后续相同指纹自动降权。
- 追问钩子：人工复核也疲劳了开始无脑点「通过」，如何发现？

```javascript
// 误报降权：相同指纹被标误报后降低优先级
function reprioritize(findings, falsePositiveFps, fpOf) {
  return findings.map(f => {
    const fp = fpOf(f);
    const downgraded = falsePositiveFps.has(fp);
    return { ...f, priority: downgraded ? 'low' : f.priority, fp };
  }).sort((a, b) => (a.priority === 'high' ? -1 : 1) - (b.priority === 'high' ? -1 : 1));
}
console.log(reprioritize(
  [{ id: '1', file: 'a.js', rule: 'XSS', priority: 'high' }],
  new Set(['a.js:XSS']),
  f => `${f.file}:${f.rule}`
)); // priority 降为 low
```
