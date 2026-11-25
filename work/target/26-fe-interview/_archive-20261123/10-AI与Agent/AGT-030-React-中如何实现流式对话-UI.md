---
title: [AGT-030] React 中如何实现流式对话 UI？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-030：React 中如何实现流式对话 UI？
**答**：
- 流式期间每个 delta 都 setState 会造成大量重渲染，用 ref 保存最新消息数组，节流（如 requestAnimationFrame 或 50ms）后批量 flush。
- 发送期间锁定输入或显示停止按钮，防止并发多路流互相覆盖。
- 流结束后把最终内容写回状态，保证与后端一致。
- 请求一律走后端代理 `/api/chat`，前端不接触 API Key。

```jsx
// React 流式对话：ref 持有最新数据，节流 setState 减少重渲染
import { useRef, useState } from 'react';

export function Chat() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);
  const [streaming, setStreaming] = useState(false);
  const messagesRef = useRef(messages);

  function flush() {
    setMessages([...messagesRef.current]);
  }

  async function send(text: string) {
    messagesRef.current = [
      ...messagesRef.current,
      { role: 'user', content: text },
      { role: 'assistant', content: '' }, // 先占位，流式填充
    ];
    flush();
    setStreaming(true);

    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: messagesRef.current.slice(0, -1) }),
    });
    const last = () => messagesRef.current[messagesRef.current.length - 1];
    let pending = false;
    await parseSSE(res.body, (delta) => {           // parseSSE 见 AGT-002
      last().content += delta;
      if (!pending) {
        pending = true;
        setTimeout(() => { pending = false; flush(); }, 50); // 50ms 节流
      }
    });
    flush();
    setStreaming(false);
  }

  return (
    <div>
      {messages.map((m, i) => (
        <div key={i} className={m.role}>{m.content}</div>
      ))}
      {streaming && <span className="cursor">▍</span>}
      <input
        placeholder="输入消息，回车发送"
        onKeyDown={(e) => {
          if (e.key === 'Enter' && e.currentTarget.value && !streaming) {
            send(e.currentTarget.value);
            e.currentTarget.value = '';
          }
        }}
      />
    </div>
  );
}
```
