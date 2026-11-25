---
title: [TST-561] AI 生成测试用例的现状、边界与落地路径
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-561：AI 生成测试用例的现状、边界与落地路径

**答**：
- 结论：AI 擅长「从需求/接口生成初稿、补边界与异常场景、改造存量用例」，不擅长「理解隐含业务规则、判断优先级、保证正确性」——定位是「副驾」不是「司机」。
- 落地路径：① 从低风险、边界清晰的模块试点；② 生成后必须过「三检」（编译/去重/覆盖）与人工评审；③ 用采纳率与逃逸缺陷度量效果，逐步扩面。
- 追问钩子：AI 生成的用例跑挂了算谁的？——生成物一律视为「待评审草稿」，合入门禁不降低；质量责任始终在提交的人，AI 只是提效工具。

```javascript
// AI 生成用例的入库闸门：三检（可编译/不重复/有断言）
function aiCaseGate(generated, existingNames) {
  const checks = {
    compilable: c => typeof c.code === 'string' && c.code.includes('expect('),
    unique: c => !existingNames.has(c.name),
    hasAssert: c => (c.code.match(/expect\(/g) || []).length >= 1,
  };
  return generated.map(c => ({ name: c.name,
    pass: Object.values(checks).every(fn => fn(c)),
    failed: Object.entries(checks).filter(([, fn]) => !fn(c)).map(([k]) => k),
  }));
}
```
