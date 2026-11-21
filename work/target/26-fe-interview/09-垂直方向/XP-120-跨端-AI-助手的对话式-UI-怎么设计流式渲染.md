---
title: [XP-120] 跨端 AI 助手的对话式 UI 怎么设计？流式渲染各端怎么适配？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-120：跨端 AI 助手的对话式 UI 怎么设计？流式渲染各端怎么适配？
**答**：
- 交互基座：**流式输出（SSE/WebSocket）→ 增量解析 → 渐进渲染**，配合打字机节奏节流（30-60ms flush）；必须支持**中断/重试/重新生成**三态。
- 流式 Markdown 难点：半截语法（未闭合代码块/表格）要按"前缀合法渲染"处理，代码块先渲染纯文本占位，闭合后高亮升级；消息列表只重渲染当前追加中的最后一条。
- 各端适配：Web/H5 直接流式 DOM 更新（markdown 增量渲染+代码高亮 worker）；RN FlatList `inverted` + `maintainVisibleContentPosition` 追底滚动；Flutter `CustomScrollView` + `anchor`/`centerKey` 反向列表，追加时防跳动。
- 性能红线：长会话虚拟化（只渲染视口消息）、代码块高亮异步化、图片公式懒渲染；打字机节流合并 setState，避免每 token 一帧。
- 状态机完备：pending/streaming/done/error/aborted 五态驱动 UI（停止按钮、重试按钮、错误卡），输入框在 streaming 中可编辑但发送排队或禁用需明确定义。

```jsx
// apps/mobile/ai/ChatScreen.jsx —— RN 流式对话：inverted 列表 + 追加节流
function useAiStream() {
  const [messages, setMessages] = useState([]);
  const bufferRef = useRef(''); const flushRef = useRef(null);

  const onChunk = (text) => {                       // SSE/WebSocket 增量回调
    bufferRef.current += text;
    if (!flushRef.current) {                        // 50ms 节流合并：不逐 token setState
      flushRef.current = setTimeout(() => {
        setMessages((ms) => {
          const last = ms[ms.length - 1];
          return [...ms.slice(0, -1), { ...last, content: last.content + bufferRef.current }];
        });
        bufferRef.current = ''; flushRef.current = null;
      }, 50);
    }
  };
  const abort = () => streamCtl?.abort();           // 中断：状态机切 aborted
  return { messages, onChunk, abort };
}

export function ChatScreen() {
  const { messages, onChunk, abort } = useAiStream();
  return (
    <FlashList                                     // XP-076：长会话必须虚拟化
      inverted                                     // 反转列表：新消息置顶，追底不跳动
      data={[...messages].reverse()}
      renderItem={({ item }) => <Bubble msg={item} />}
      ListFooterComponent={                        // inverted 后 footer 即"最新消息"区
        <Bubble typing streaming={messages.at(-1)?.state === 'streaming'} />}
    />
  );
}
// Bubble 内：半截代码块先按纯文本渲染，闭合后再高亮（前缀合法渲染）
// streaming 态显示停止按钮；error 态显示重试；输入框始终可编辑，发送排队
```
