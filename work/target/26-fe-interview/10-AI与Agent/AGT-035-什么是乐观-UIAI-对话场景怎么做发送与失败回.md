---
title: [AGT-035] 什么是乐观 UI？AI 对话场景怎么做发送与失败回滚？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-035：什么是乐观 UI？AI 对话场景怎么做发送与失败回滚？
**答**：
- 乐观 UI：用户消息不等服务器确认先上屏，把感知延迟降到零；生成中用占位气泡 + 光标动画。
- 每条消息带 status：sending → streaming → done / failed，失败时标记并可重试，而不是悄悄消失。
- 请求体从本地已确认的消息构造，失败的轮次不进入历史，重试时复用同一输入。
- assistant 失败时要区分"没生成任何内容"（可整体重试）与"生成一半断了"（可续写或保留已生成部分）。

```typescript
// 乐观 UI：消息先上屏，失败标记状态并提供重试
type MsgStatus = 'sending' | 'streaming' | 'done' | 'failed';

interface UIMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  status: MsgStatus;
}

async function sendMessageOptimistic(store: { messages: UIMessage[] }, text: string) {
  const userMsg: UIMessage = { id: crypto.randomUUID(), role: 'user', content: text, status: 'sending' };
  const replyMsg: UIMessage = { id: crypto.randomUUID(), role: 'assistant', content: '', status: 'streaming' };
  store.messages.push(userMsg, replyMsg); // 先渲染，不等响应

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        messages: store.messages
          .filter((m) => m.status === 'done' || m === userMsg)
          .map(({ role, content }) => ({ role, content })),
      }),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    userMsg.status = 'done';
    await parseSSE(res.body!, (delta) => { replyMsg.content += delta; });
    replyMsg.status = 'done';
  } catch {
    replyMsg.status = 'failed';
    replyMsg.content = '生成失败，点击重试';
  }
}
```

---

## 八、记忆与状态
