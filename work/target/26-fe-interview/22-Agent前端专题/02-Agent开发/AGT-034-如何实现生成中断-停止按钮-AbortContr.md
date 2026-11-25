---
title: [AGT-034] 如何实现生成中断（停止按钮）？AbortController 要注意什么？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-034：如何实现生成中断（停止按钮）？AbortController 要注意什么？
**答**：
- 每次生成创建一个 `AbortController`，停止按钮调 `abort()`，同时中断 fetch 与流读取，后端检测断连后也会停止继续消耗 token。
- abort 抛出的 `AbortError` 要与真实网络错误区分，主动中断不算失败、不弹错误提示。
- 发起新会话前先 abort 旧流，避免两路流并发写同一条消息。
- React 中组件卸载时也要 abort，防止对已卸载组件 setState。

```typescript
// 生成中断：AbortController 贯穿 fetch 与流读取
function createStreamingChat() {
  let controller: AbortController | null = null;

  function stop() {
    controller?.abort();
    controller = null;
  }

  async function start(messages: ChatMessage[], onDelta: (t: string) => void) {
    stop(); // 防止并发多路流
    controller = new AbortController();
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages }),
        signal: controller.signal, // abort 后 fetch 与 reader.read 都会中断
      });
      await parseSSE(res.body!, onDelta);
    } catch (err) {
      if ((err as Error).name !== 'AbortError') throw err; // 主动中断不算错误
    } finally {
      controller = null;
    }
  }

  return { start, stop };
}

const chat = createStreamingChat();
// 点击「停止生成」按钮时调用 chat.stop()
```
