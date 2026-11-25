---
title: [DP-402] 案例：IM 聊天的模式组合
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-402：IM 聊天的模式组合

**答**：
- IM 的模式全景：观察者（消息推送订阅）、状态机（消息状态：sending→sent→failed→confirmed；连接状态机：connecting→open→reconnecting）、队列（离线消息补拉）、策略（消息渲染策略：文本/图片/系统消息分型）、享元（消息气泡复用——虚拟列表）
- 可靠性组合：seq 序号（去重排序）+ ack（确认）+ 补拉（断线增量）——三层保证消息不丢不重
- 消息状态机驱动 UI：转圈（sending）/双勾（confirmed）/红色感叹号（failed 可点击重发）——状态即 UI
- 会话列表的排序策略：置顶 > 未读 > 最后消息时间——策略可配置（产品决策）
- 深水点：消息的「乐观渲染」——发送即显示（pending 态）+ 服务端确认校正（id 替换 tempId）——乐观 UI 在 IM 的标准应用

```javascript
// 消息状态机
const MSG_STATES = {
  sending: { on: { ack: 'sent', fail: 'failed' } },
  failed: { on: { resend: 'sending' } },
};
// 乐观渲染: sendMessage → tempId 消息入列(pending) → ack 后替换 id
// 补拉: 重连后 fetch(after=lastSeq) → 按序合并去重
```
