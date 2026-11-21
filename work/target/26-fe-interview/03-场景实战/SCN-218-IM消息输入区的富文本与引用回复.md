---
title: [SCN-218] IM 输入区——引用回复与富文本混排的交互设计？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-218：IM 输入区的引用回复、@提醒、表情混排怎么设计？

**答**:
- 引用回复：长按/右键消息→引用→输入框上方显示引用预览条（可取消）；发送时消息体带 replyTo（serverId+摘要快照——引用的消息被撤回后仍可显示摘要），渲染为嵌套引用块。
- @提醒：输入 @ 弹成员选择面板（群大时分片搜索）、@某人高亮渲染与点击跳转资料卡、"@所有人"权限控制；@我消息在会话列表红点升级（@标记）。
- 富文本混排：文本+表情+话题标签统一为分段文本模型（segments: [{type: text/emoji/mention/topic}]），渲染各自组件化（emoji 图片渲染、mention 高亮、topic 链接），纯文本兜底（复制出去是可读文本）。
- 输入状态联动：typing 状态广播（对方"正在输入"提示，节流 3s 一次、5s 无输入停止）、草稿保存（切换会话草稿保留，SCN 创作者草稿同源思想）。

```javascript
function buildMessage(input) {
  const segments = parseInput(input);        // 解析为分段模型
  return {
    type: 'rich',
    segments,                                // text/emoji/mention/topic
    replyTo: currentReply ? { serverId: currentReply.serverId,
      digest: digestOf(currentReply) } : null,
    mentions: segments.filter(s => s.type === 'mention')
      .map(s => s.userId),
  };
}
// 渲染：segments.map(s => byType(s))；
// mention 点击 → 资料卡；topic 点击 → 话题页。
// typing：input 事件节流 3s → ws.send({type:'typing'})，
//   5s 无输入 → send({type:'typing_stop'})。
```
