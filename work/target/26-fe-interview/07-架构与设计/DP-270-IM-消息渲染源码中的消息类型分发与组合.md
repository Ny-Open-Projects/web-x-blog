---
title: [DP-270] 源码识别：IM 消息渲染源码中的类型分发与组合？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-270：源码识别：IM 消息渲染源码中的类型分发与组合？
**答**:
- 策略注册表：消息类型 → 渲染器（text/image/file/card/revoke/system）Map 注册，新增类型注册即可——开放扩展。
- 组合模式：富消息（引用回复 + 图片 + 已读状态）由子渲染器组合（MessageBubble 里嵌套 ImageRenderer）。
- 状态机：消息生命周期（sending → sent → read → failed），气泡角标订阅状态变化。
- 识别要点：长列表性能——消息列表虚拟滚动（DP-217）+ 类型渲染器的 memo（props 不变不重渲）。

```tsx
// IM 消息渲染器注册表
const renderers = new Map<string, React.FC<{ msg: Msg }>>();
renderers.set('text', TextBubble).set('image', ImageBubble).set('card', CardBubble);
function MessageItem({ msg }) {
  const R = renderers.get(msg.type) ?? UnknownBubble;      // 兜底渲染器（策略缺省）
  return (
    <li data-id={msg.id} className={`msg msg-${msg.state}`}>   {/* 状态机：角标 */}
      {msg.reply && <QuoteBlock msg={msg.reply}/>}             {/* 组合：引用子渲染 */}
      <R msg={msg}/>
      <StateBadge state={msg.state}/>                          {/* 订阅 sending/sent/read */}
    </li>
  );
}
// 列表：const MemoItem = memo(MessageItem, (a, b) => a.msg === b.msg && a.msg.state === b.msg.state);
// 新类型：renderers.set('vote', VoteBubble) —— 零侵入扩展
```
