---
title: [OPT-086] 大组件怎么拆分？memo 边界应该划在哪？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-086：大组件怎么拆分？memo 边界应该划在哪？

**答**：
- 拆分目标不是"代码短"而是**建立重渲染隔离墙**：把易变区域和稳定区域分开，memo 放在隔离墙上，变化被限制在墙内。
- 边界判断法：拿 Profiler 的 commit 结果，重渲染频率相同的组件归一个区域；高频区和低频区之间就是 memo 边界。
- memo 生效前提：props 引用稳定（useCallback/useMemo/稳定 key 传基本值），否则 memo 只增加比较成本。
- 与其到处 React.memo，不如先用"状态下沉"让变化天然隔离——memo 是补墙工具，不是第一手段。

```jsx
// 一一对应：大组件按重渲染频率拆分 + memo 边界
// 反例：一个巨型组件，聊天消息（高频滚动加载）与底部输入框互相拖累
// function ChatRoom() { ... 消息列表 + 侧栏 + 输入框 全在一处 ... }

// 拆分：三个区域独立，边界放在变化频率差异最大的地方
function ChatRoom({ roomId }) {
  const [draft, setDraft] = useState(''); // 高频：每键一次
  const messages = useMessages(roomId);   // 中频：新消息到达

  return (
    <div className="room">
      {/* 稳定区：roomId 不变就永不重渲，memo 建墙 */}
      <RoomSidebar memo roomId={roomId} />

      {/* 中频区：新消息才重渲，行级再 memo */}
      <MessageList messages={messages} />

      {/* 高频区：draft 状态下沉在此，输入不波及其他区域 */}
      <Composer draft={draft} onChange={setDraft} onSend={sendMessage} />
    </div>
  );
}

// 隔离墙实现：props 全为基本值或稳定引用时 memo 才有效
const RoomSidebar = React.memo(function RoomSidebar({ roomId }) {
  return <aside>{/* 用户列表，低频 */}</aside>;
});

const MessageList = React.memo(function MessageList({ messages }) {
  return (
    <ul>
      {messages.map((m) => (
        <MessageItem key={m.id} id={m.id} text={m.text} />
      ))}
    </ul>
  );
});
// MessageItem 只接基本值 props：任何一条新消息到达，只有新行 mount，旧行被 memo 跳过
const MessageItem = React.memo(({ id, text }) => <li data-id={id}>{text}</li>);
```
