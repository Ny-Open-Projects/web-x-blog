---
title: [TST-658] 安全回归测试如何融入日常 CI 而不拖慢节奏？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-658：安全回归测试如何融入日常 CI 而不拖慢节奏？

**答**：
- 结论：分层——PR 跑轻量静态规则（秒级），nightly 跑动态扫描与依赖审计（分钟级）。
- 安全基线用「新增问题」判定：只卡本次引入的高危，存量问题走专项治理。
- 高危漏洞触发阻断并自动开 issue，附带复现步骤与修复建议。
- 追问钩子：扫描器报了一个高危但业务说误报，你的裁决流程是什么？

```javascript
function securityGate(current, baseline) {
  const newHigh = current.filter(f =>
    f.sev === 'high' && !baseline.some(b => b.fingerprint === f.fingerprint));
  return {
    newHigh: newHigh.length,
    verdict: newHigh.length ? 'block' : 'pass',
    issues: newHigh.map(f => ({ ...f, autoOpenIssue: true })),
  };
}
```
