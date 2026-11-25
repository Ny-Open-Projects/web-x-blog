---
title: [AGT-046] 流式渲染的 token 到达速率高于渲染速率怎么办？背压如何处理？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-046：流式渲染的 token 到达速率高于渲染速率怎么办？背压如何处理？
**答**：
- 高速流下每个 delta 都 setState 会造成每秒上百次重渲染，主线程阻塞、掉帧、markdown 频繁全量重 parse。
- 方案：delta 只追加进缓冲区，`requestAnimationFrame` 每帧最多 flush 一次到 state（时间片节流同理，流结束时必须补一次完整 flush）。
- 解析与渲染分离：markdown 重解析纳入同一节流批次，避免「每个 token 全文重 parse」。
- 滚动跟随要处理用户手势冲突：用户上滑查看历史时暂停自动滚到底，回到底部再恢复。

```typescript
// 背压：delta 进缓冲，rAF 定频刷进 React state
function useStreamedText(stream: StreamManager, sessionId: string) {
  const [text, setText] = useState('');
  const bufRef = useRef('');
  const rafRef = useRef(0);
  const stickRef = useRef(true); // 是否自动跟随滚动

  useEffect(() => stream.subscribe(() => {
    const s = stream.get(sessionId);
    if (!s) return;
    bufRef.current = s.text;
    if (!rafRef.current) {
      rafRef.current = requestAnimationFrame(() => {
        rafRef.current = 0;
        setText(bufRef.current);   // 每帧最多一次 setState
      });
    }
  }), [sessionId]);

  useEffect(() => () => cancelAnimationFrame(rafRef.current), []);
  return { text, stickRef };
}

// 滚动容器：用户上滑暂停跟随，回到底部恢复
function onScroll(e: React.UIEvent<HTMLDivElement>, stickRef: React.RefObject<boolean>) {
  const el = e.currentTarget;
  stickRef.current = el.scrollHeight - el.scrollTop - el.clientHeight < 40;
}
```
