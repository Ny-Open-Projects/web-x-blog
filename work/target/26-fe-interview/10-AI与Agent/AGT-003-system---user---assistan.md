---
title: [AGT-003] system / user / assistant 消息角色各是什么？多轮对话的上下文要怎么维护？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-003：system / user / assistant 消息角色各是什么？多轮对话的上下文要怎么维护？
**答**：
- `system` 设定人设与规则，权重最高；`user` 是用户输入；`assistant` 是模型历史回复；工具场景还有 `tool` 角色。
- 模型无状态：多轮对话必须在每轮请求中把完整 messages 历史重新带上。
- 每轮结束要把 assistant 回复也 push 进历史，否则模型会"失忆"。
- 上下文要封装成会话对象管理，配合截断/摘要策略（见 AGT-004、AGT-036）防止无限增长。

```typescript
// 用会话类封装多轮上下文：每轮自动带上全部历史
class Conversation {
  private messages: ChatMessage[] = [];

  constructor(systemPrompt: string) {
    this.messages.push({ role: 'system', content: systemPrompt });
  }

  async send(userInput: string): Promise<string> {
    this.messages.push({ role: 'user', content: userInput });
    const reply = await chat(this.messages); // chat 见 AGT-001
    this.messages.push({ role: 'assistant', content: reply });
    return reply;
  }

  history(): ChatMessage[] {
    return [...this.messages];
  }
}

const conv = new Conversation('你是前端面试官，一次只问一个问题');
await conv.send('开始面试');          // 第 1 轮
await conv.send('渲染层和合成层的区别'); // 第 2 轮已包含第 1 轮上下文
```
