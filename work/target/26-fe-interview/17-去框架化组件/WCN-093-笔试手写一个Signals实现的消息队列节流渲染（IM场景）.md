---
title: [WCN-093] 笔试：手写 IM 消息流的 Signals 节流渲染（高频消息合并 + 虚拟窗口）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-093：笔试：手写 IM 消息流的 Signals 节流渲染

**题目**：IM 场景：① socket 高频推送 `messages` 数组；② 渲染层要求：消息以 100ms 批次合并（同一批只渲染一次）；③ `visibleWindow` computed：只渲染最近 50 条（旧消息进"查看更多"）；④ 未读数 signal：不在底部（用户上翻）时新消息计入未读；⑤ 消息 id 去重（重连可能重推）；⑥ 组件销毁断开 socket 并停止渲染订阅。

**答**：

```javascript
import { createSignal, computed, effect, untrack } from './mini.js';

export function createImFeed(socket, container) {
  const [messages, setMessages] = createSignal([]);   // 全量（近 200 条）
  const [atBottom, setAtBottom] = createSignal(true);
  const [unread, setUnread] = createSignal(0);
  let buffer = [], flushTimer;

  function push(batch) {                              // socket 批量到达
    buffer.push(...batch);
    if (!flushTimer) {
      flushTimer = setTimeout(() => {                 // 100ms 合并批次
        flushTimer = null;
        const seen = new Set(untrack(messages).map((m) => m.id));
        const fresh = buffer.filter((m) => !seen.has(m.id));
        buffer = [];
        if (!fresh.length) return;
        setMessages([...untrack(messages), ...fresh].slice(-200)); // 上限截断
        if (!untrack(atBottom)) setUnread(untrack(unread) + fresh.length);
      }, 100);
    }
  }

  const visibleWindow = computed(() => messages().slice(-50));   // 只渲染尾部 50
  const stop = effect(() => {
    renderList(container, visibleWindow());
    if (untrack(atBottom)) setUnread(0);            // 底部时未读清零
  });
  container.addEventListener('scroll', () =>
    setAtBottom(container.scrollHeight - container.scrollTop - container.clientHeight < 40));

  socket.on('messages', push);
  return {
    unread, visibleWindow,
    destroy() { socket.off('messages', push); clearTimeout(flushTimer); stop(); },
  };
}
function renderList(container, msgs) { /* keyed 渲染近 50 条 */ }
```

**评分点**：
- 100ms 批次合并：高频消息不逐条渲染（性能核心）。
- id 去重（重连重推容错）；消息上限截断防内存膨胀。
- visibleWindow computed + keyed 渲染（只渲染尾部窗口）。
- 未读数只在"不在底部"时累加，回底自动清零（untrack 防误依赖）。
- destroy 清理 socket 监听与定时器。
