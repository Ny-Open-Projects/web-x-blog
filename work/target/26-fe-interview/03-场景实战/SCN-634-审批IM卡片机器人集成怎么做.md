---
title: [SCN-634] 审批与 IM 集成（卡片机器人）怎么设计？卡片状态怎么流转？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-634：审批与 IM 卡片集成怎么设计？
**答**：
- 卡片即入口：待办推 IM 卡片（标题/金额/摘要/关键按钮），点击按钮直接处理（简单场景）或跳详情（复杂场景）；卡片按钮的权限与时效校验在服务端（卡片可被转发）。
- 状态回写：审批完成后主动更新卡片（按钮变为结果状态「已通过 · 张三 · 12:30」），防止用户对过期卡片误操作；转发的卡片只读化。
- 快捷处理安全：卡片上直接同意仅限低金额场景，高金额按钮只跳详情页（移动生物识别后处理）；卡片 token 与会话绑定。
- 通知降噪：同一实例多事件（待办→催办→通过）更新同一张卡片而非发新卡。
- 追问钩子：卡片处理与 Web 处理的竞态——同一幂等键（instanceId+version），后到方收到「已被处理」友好提示并刷新卡片。

```javascript
// 卡片更新协议（服务端）
{
  cardId: instanceId,
  update: {
    state: 'PASSED',
    body: '已通过 · 张三 · 12:30',
    buttons: [],                                   // 清空操作按钮
  },
  readonly: true,                                  // 转发副本只读
}
// 点击卡片按钮
async function onCardAction(instanceId, action, cardToken) {
  try {
    await api.post(`/instance/${instanceId}/${action}`, { cardToken });  // 时效+会话绑定
  } catch (e) {
    if (e.code === 'ALREADY_DONE') return refreshCard(instanceId);       // 竞态友好提示
    if (e.code === 'CARD_EXPIRED') return openDetail(instanceId);        // 过期跳详情
  }
}
```
