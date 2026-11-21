---
title: [AIC-202] Cursor 的 rules（.cursor/rules/*.mdc）在请求时是怎么被选中的？写错 description 会发生什么？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-202：Cursor 的 rules（.cursor/rules/*.mdc）在请求时是怎么被选中的？写错 description 会发生什么？
**答**：
- 三种匹配：alwaysApply 直注入、globs 按当前文件路径匹配、agent 类由模型根据 description 与任务语义匹配。
- agent 类规则的 description 是唯一的「路由键」，写得含糊会导致该注入时不注入、不该注入时乱注入。
- 调试方法：用 Cursor 的规则引用面板确认本次请求实际带了哪些规则，再反推 description 问题。
- 规则选中发生在请求前，消耗的是上下文窗口预算，所以每条规则要有存在价值。

```javascript
// 模拟 agent 类规则的语义匹配打分（说明 description 的作用）
function pickAgentRules(task: string, rules: Array<{ name: string; desc: string }>) {
  const kw = task.toLowerCase();
  return rules
    .map(r => ({ name: r.name,
      score: r.desc.toLowerCase().split(/\s+/)
        .filter(w => w.length > 2 && kw.includes(w)).length }))
    .filter(x => x.score > 0)
    .sort((a, b) => b.score - a.score).slice(0, 3)
    .map(x => x.name);
}
// desc: '执行数据库迁移与 schema 变更时使用' → 任务 '帮我把 users 表加一列头像'
// 也能命中，因为分词后有共同语义词；desc 写 '一些规范' 则永远打 0 分
r
```
