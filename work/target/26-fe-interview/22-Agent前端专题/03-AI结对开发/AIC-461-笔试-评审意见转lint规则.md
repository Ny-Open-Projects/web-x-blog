---
title: [AIC-461] 笔试：把重复出现的评审意见自动转化为 lint 规则候选。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-461：笔试：把重复出现的评审意见自动转化为 lint 规则候选。
**答**：意见记录 `[{message, times}]`。规则候选条件：出现 ≥ 5 次且 message 可映射到静态模式（含「匹配/模式/正则」关键词并给出 pattern 字段）。输出 `{promotable, keepInKB}` 与可执行的规则配置片段。

```javascript
function promote(messages) {
  const promotable = [], keepInKB = [];
  for (const m of messages.sort((a, b) => b.times - a.times)) {
    const canLint = m.times >= 5 && m.pattern;
    if (canLint) promotable.push({
      rule: `no-${m.id}`,
      config: { pattern: m.pattern, message: m.message, severity: 'warn' },
    });
    else keepInKB.push({ id: m.id, times: m.times,
      reason: m.times < 5 ? '频次不足' : '语义类意见无法静态化' });
  }
  return { promotable, keepInKB };
}
console.log(promote([
  { id: 'hex', message: '禁止硬编码颜色', times: 9, pattern: '#[0-9a-fA-F]{3,8}' },
  { id: 'arch', message: '应使用 hooks 层消费数据', times: 12 },
])); // hex 可转 lint；arch 留知识库

```

**评分点**：
- 双条件（频次 + 可静态化）判定——高频但语义类意见留知识库。
- pattern 缺失的降级 keepInKB（不能凭空造规则）。
- promotable 输出 eslint 风格配置片段。
- 排序按 times 降序。
