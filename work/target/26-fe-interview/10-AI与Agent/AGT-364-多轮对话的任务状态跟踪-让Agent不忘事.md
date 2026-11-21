---
title: [AGT-364] 任务状态跟踪——长会话中 Agent 怎么不忘事？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-364：多轮会话里用户提到多个待办，Agent 怎么跟踪不遗漏？

**答**:
- 显式任务簿：把会话中的待办/承诺抽取为结构化任务列表（对象：事项/负责人/状态/时间），每轮更新——"任务簿"作为结构化上下文常驻（比藏在对话历史里可靠得多，AGT-363 保留优先级的工程化）。
- 更新触发：新承诺出现（"我回头给你"→入簿）、状态变更（完成后勾选并复述确认）、收尾检查（"还有什么没处理的吗"→Agent 对照任务簿盘点——主动盘点是体验亮点）。
- 指代与归属：任务簿条目保留原始出处（哪一轮谁说的——可回溯），模糊指代在入簿时即解析（"那个事"→具体事项名，解析不了问用户）。
- 跨会话衔接：未完成任务跨会话保留（进入记忆系统 AGT-223），新会话开始时提示未结事项——任务簿是工作记忆与长期记忆的衔接层。

```javascript
function taskBookUpdate(book, utterance, round) {
  const events = extract(utterance, { newTodo: true,
    done: true, delegate: true });
  events.forEach(e => book.apply(e, { ref: round,
    owner: e.owner, ddl: e.when }));
  return book;   // 结构化常驻上下文
}
// 收尾：'对照任务簿盘点未结事项' 主动触发。
// 未结任务跨会话 → 入长期记忆。
```
