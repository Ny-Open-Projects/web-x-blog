---
title: [R19-004] useOptimistic 的原理和适用场景？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-004：useOptimistic 的原理和适用场景？
**答**：
- 让 UI 在异步操作完成前先展示"乐观结果"，操作失败时自动回滚到真实数据。
- 传给它的更新函数是纯函数，基于当前真实 state 计算乐观视图。
- 在 action 内调用 addOptimistic 后立即渲染乐观值，await 真实请求结束后自动切回服务端数据。
- 适合点赞、评论、发送消息等"大概率成功、允许短暂不一致"的操作。

```jsx
import { useOptimistic } from 'react';

function MessageList({ messages, sendMessage }) {
  const [optimisticMessages, addOptimisticMessage] = useOptimistic(
    messages,
    (current, newText) => [...current, { id: 'tmp', text: newText, sending: true }]
  );

  async function handleSend(formData) {
    const text = formData.get('text');
    addOptimisticMessage(text); // 立即显示，失败自动回滚
    await sendMessage(text);
  }

  return (
    <>
      {optimisticMessages.map((m) => (
        <p key={m.id}>{m.sending ? m.text + '（发送中）' : m.text}</p>
      ))}
      <form action={handleSend}>
        <input name="text" />
      </form>
    </>
  );
}
```
