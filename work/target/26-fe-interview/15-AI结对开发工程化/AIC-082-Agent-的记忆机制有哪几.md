---
title: [AIC-082] 编码 Agent 的「记忆」有哪几层？会话记忆、项目记忆、规则记忆分别怎么管理？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-082：编码 Agent 的「记忆」有哪几层？会话记忆、项目记忆、规则记忆分别怎么管理？
**答**：
- 三层记忆：会话记忆（当前对话上下文，易膨胀易丢失）、项目记忆（跨会话持久，如 agent 自动维护的 NOTES.md/任务清单）、规则记忆（团队级约束，规则文件，只读强约束）。
- 会话记忆管理：长会话定期压缩成摘要（AIC-162 思路），摘要只保留「决策与未完成事项」，丢实现细节——细节可从代码里重读。
- 项目记忆管理：让 agent 每完成一个任务把「关键决策 + 遗留问题」写进固定文件，下次会话开头读取；要有清理机制否则记忆文件无限膨胀。
- 层级冲突原则：规则记忆 > 项目记忆 > 会话记忆——会话中 agent 临时说「我觉得可以跳过测试」不能覆盖规则文件的「必须测试」。
- 追问钩子：记忆的真正难点是「遗忘」——过时的项目记忆比没有记忆更危险，项目记忆要带时间戳与失效条件。

```javascript
// 项目记忆的读写规范
function loadMemory(dir) {
  const notes = read(`${dir}/AGENT_NOTES.md`);
  const stale = notes.match(/updated:\s*(\d{4}-\d{2}-\d{2})/)?.[1];
  return { content: notes, staleDays: diffDays(stale, today()),
    warning: staleDays > 30 ? '项目记忆超过 30 天未更新，先核实再信任' : null };
}
function saveMemory(dir, { decisions, todos }) {
  append(`${dir}/AGENT_NOTES.md`, `\n## ${today()}\n决策：${decisions}\n待办：${todos}\n`);
}
```
