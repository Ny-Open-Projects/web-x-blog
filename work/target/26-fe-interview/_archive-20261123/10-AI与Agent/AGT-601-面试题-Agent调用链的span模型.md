---
title: [AGT-601] 一次 Agent 任务的可观测 trace 树怎么建模（root/span/属性），与普通 Web 请求 trace 有何不同？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-601：一次 Agent 任务的可观测 trace 树怎么建模（root/span/属性），与普通 Web 请求 trace 有何不同

**答**：
- Agent trace 是「树 + 环形」：root=任务，子 span=每轮 LLM 调用/工具执行/检索；与 Web trace 最大不同是时长不可预估（模型生成 2s~120s）且节点会动态派生（Agent 决定再调什么工具），所以 span 要支持运行时动态开闭而非静态拓扑。
- 属性分层：任务级（userId/任务类型/预算）、轮次级（模型/提示词版本/prompt_tokens）、工具级（工具名/参数摘要/结果摘要/耗时）。参数与结果只存摘要+引用（全量进对象存储按需取），防止 trace 库膨胀。
- trace 必须贯穿前端→网关→模型→工具（前端生成 traceId 一路透传），否则用户反馈无法下钻。

```javascript
// Agent span 模型
function createTaskTrace(task) {
  const root = span('agent.task', {
    'task.type': task.type, 'user.id': hashId(task.userId),
    'budget.tokens': task.budget,
  });
  return {
    llmTurn(turnIdx, meta) {
      return root.child('llm.turn', {
        'llm.model': meta.model, 'prompt.ver': meta.promptVer,
        'gen.tokens': meta.usage?.completionTokens,
      });
    },
    toolCall(turn, tc) {
      return turn.child(`tool.${tc.tool}`, {
        'tool.args.digest': digest(tc.args),    // 摘要，非全量
        'tool.result.ref': putBlob(tc.result),  // 全量进对象存储
      });
    },
  };
}
```

