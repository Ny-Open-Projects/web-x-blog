---
title: [AIC-213] 规则文件改了但 AI 行为没变化，可能是什么原因？如何排查？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-213：规则文件改了但 AI 行为没变化，可能是什么原因？如何排查？
**答**：
- 规则文件缓存：IDE 重启或重新加载窗口；确认规则文件保存生效。
- 匹配未命中：glob 写错路径、agent 类 description 与任务无关——用规则引用面板确认是否被选中。
- 会话历史污染：长会话里模型已形成惯性，开新会话验证。
- 同主题规则被更早注入的规则覆盖，合并顺序问题。

```javascript
// 排查脚本思路：模拟一次请求并输出实际注入的规则
function debugInjection(filePath: string, task: string) {
  const picked = selectRules(filePath, task); // always + glob + agent
  console.table(picked.map(r => ({ name: r.name, via: r.via, tokens: est(r.body) })));
  if (!picked.some(r => r.name === 'expected-rule')) {
    console.warn('目标规则未被注入：检查 globs 路径或 description 语义');
  }
}
r
```
