---
title: [AIC-610] IM 消息模块多人同时找 AI 改代码，怎么避免对话污染？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-610：IM 消息模块多人同时找 AI 改代码，怎么避免对话污染？

**答**：
- 结论先行：**核心是「会话隔离 + 文件锁 + 单一真相源」**。多人共享一个 AI 会话 = 灾难，因为上下文会串台；正确做法是每人独立会话，但共享同一份仓库规则与任务看板。
- 会话隔离：每个开发者/每个任务一个独立会话，禁止把别人的对话历史复制进自己的会话（AIC-482 多会话冲突预检）。AI 的 memory 文件按人/任务分目录，不全局共享。
- 文件级互斥：同一时刻只有一个会话能修改某文件——用「软锁」（任务看板声明 owner + 文件范围）或 git worktree 物理隔离（AIC-318 多 Agent 冲突）。IM 消息模块的消息列表、输入框、表情面板拆给不同人，边界要在任务卡里写死。
- 单一真相源：AI 编码规范、IM 协议类型定义、消息状态机放在仓库里（rules + 类型文件），所有人/会话读同一份，避免「各自问 AI 得出不同实现」。
- 追问钩子：为什么 git worktree 比「约定谁改哪个文件」更可靠？——约定依赖人的记忆和自觉，worktree 是物理隔离，从机制上杜绝冲突；代价是合并成本，换来的是零冲突保证。

```typescript
type Task = { id: string; owner: string; files: string[]; worktree?: string };

// 多会话冲突预检：同一文件不能被两个进行中任务占用
function precheckConflicts(tasks: Task[]): { taskId: string; conflicts: string[] }[] {
  const ownerByFile = new Map<string, string>();
  const conflicts = new Map<string, Set<string>>();
  for (const t of tasks) {
    for (const f of t.files) {
      if (ownerByFile.has(f)) {
        if (!conflicts.has(t.id)) conflicts.set(t.id, new Set());
        conflicts.get(t.id).add(`${f} <- ${ownerByFile.get(f)}`);
      } else {
        ownerByFile.set(f, t.owner);
      }
    }
  }
  return [...conflicts.entries()].map(([taskId, set]) => ({ taskId, conflicts: [...set] }));
}

const tasks: Task[] = [
  { id: 'T1', owner: 'alice', files: ['msg/list.tsx', 'msg/item.tsx'] },
  { id: 'T2', owner: 'bob', files: ['msg/list.tsx', 'msg/input.tsx'] }, // 冲突 list.tsx
];
console.log(precheckConflicts(tasks)[0].conflicts[0].includes('msg/list.tsx')); // true
```
