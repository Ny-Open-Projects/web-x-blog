---
title: [AIC-216] 两条 glob 规则同时命中同一文件且指令矛盾，模型行为不可预测，如何系统性消除？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-216：两条 glob 规则同时命中同一文件且指令矛盾，模型行为不可预测，如何系统性消除？
**答**：
- 检测层：CI 里对 glob 求交集，交集文件上做规则关键词冲突扫描（如「必须 X」vs「禁止 X」）。
- 声明层：规则里显式写优先级与例外说明，让模型有据可依。
- 结构层：合并矛盾规则为一条，用条件分支表述（在 X 场景用 A，否则用 B）。
- 验证层：把冲突场景加入评测集，防回归。

```javascript
function detectConflict(rules: Array<{ name: string; globs: string[]; body: string }>) {
  const conflicts = [];
  for (let i = 0; i < rules.length; i++)
    for (let j = i + 1; j < rules.length; j++) {
      const overlap = intersectGlobs(rules[i].globs, rules[j].globs);
      if (!overlap.length) continue;
      const must = /必须|只能/.exec(rules[i].body)?.[0];
      const ban = /禁止|不要/.exec(rules[j].body)?.[0];
      if (must && ban) conflicts.push({ a: rules[i].name, b: rules[j].name, overlap });
    }
  return conflicts; // CI 中非空即失败
}
r
```
