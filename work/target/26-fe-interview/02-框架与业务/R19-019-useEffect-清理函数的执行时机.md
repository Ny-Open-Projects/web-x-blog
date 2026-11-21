---
title: [R19-019] useEffect 清理函数的执行时机？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-019：useEffect 清理函数的执行时机？
**答**：
- 依赖变化导致 effect 重跑前：先执行上一次的清理函数。
- 组件卸载时：执行最后一次的清理函数。
- 清理函数应与 effect 中的资源一一对应：订阅取消、定时器清除、连接断开。
- 开发模式 StrictMode 下会 mount-unmount-remount，清理函数写错会立刻暴露。

```jsx
function ChatRoom({ roomId }) {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const connection = createConnection(roomId);
    connection.on('message', (msg) => setMessages((prev) => [...prev, msg]));
    connection.connect();

    // 先 disconnect 旧的，再连接新的房间
    return () => connection.disconnect();
  }, [roomId]);

  return <p>房间 {roomId}，收到 {messages.length} 条消息</p>;
}
```
