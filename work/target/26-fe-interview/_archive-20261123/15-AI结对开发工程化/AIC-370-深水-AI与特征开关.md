---
title: [AIC-370] AI 生成代码时如何正确使用 feature flag（而不是硬编码 if true）？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-370：AI 生成代码时如何正确使用 feature flag（而不是硬编码 if true）？
**答**：
- flag 规范进 rules：flag 命名（域.功能.变体）/默认值/过期日期必须声明。
- 生成即登记：AI 创建 flag 时同步登记到 flag 平台（名称/owner/过期），未登记的 flag 引用 lint 报错。
- 清理自动化：过期 flag AI 自动生成清理 PR（删分支逻辑），清理是常态工作。
- 测试要求：flag 两个分支都要有测试（或说明为什么只测默认分支）。

```javascript
const flagDiscipline = {
  declare: 'flag 必须带 owner + expiry（lint 校验）',
  register: 'AI 创建 flag → 同步登记平台 → 未登记报错',
  cleanup: '过期 → AI 自动生成清理 PR',
  test: '两分支各有测试或注明豁免理由',
};
r
```
