---
title: [TST-737] 笔试：实现安全 payload 库的脱敏与分级访问控制器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-737：笔试：实现安全 payload 库的脱敏与分级访问控制器

**题目**：实现 `filterPayloads(payloads, role, reveal)`。payload 项 {id, level('low'|'mid'|'high'), value}。规则：high 仅 role='security' 可见；mid 需 role 为 'security' 或 'qa'；low 所有人可见。不可见时若 reveal=false 则剔除该项，若 reveal=true 则保留但 value 替换为 '[REDACTED]'。返回处理后数组。

**答**：
- 按等级与角色做可见性矩阵，逻辑清晰。
- reveal 控制是剔除还是脱敏保留，注意保留 id 用于占位。
- 不改变原数组，返回新数组。

```javascript
function filterPayloads(payloads, role, reveal) {
  const canSee = (level) =>
    level === 'low' ||
    (level === 'mid' && ['security', 'qa'].includes(role)) ||
    (level === 'high' && role === 'security');
  const out = [];
  for (const p of payloads) {
    if (canSee(p.level)) out.push({ ...p });
    else if (reveal) out.push({ ...p, value: '[REDACTED]' });
  }
  return out;
}
console.log(filterPayloads([
  { id: '1', level: 'high', value: '<script>' },
  { id: '2', level: 'low', value: 'a' },
], 'dev', true)); // 1 被 REDACTED，2 保留
```

**评分点**：
- 等级-角色可见性矩阵正确
- reveal 两种模式处理正确
- 不修改原数组
- 脱敏保留 id
