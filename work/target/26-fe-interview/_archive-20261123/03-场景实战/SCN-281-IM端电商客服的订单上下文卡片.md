---
title: [SCN-281] 电商客服 IM——订单上下文卡片与快捷操作？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-281：电商客服会话里嵌入订单卡片与快捷操作，怎么设计？

**答**:
- 结构化消息：卡片消息类型（订单卡：状态/商品缩略/金额/操作按钮），消息 schema 分型（text/card/image/quick_reply——客服 IM 消息协议化），渲染注册表按 type 分发。
- 快捷操作：卡片内操作（查看物流/申请退款/催发货）→ 直接调起对应业务流程（跳转或会话内表单），操作结果回填会话（系统消息"已为您提交退款申请"）——操作闭环在会话内。
- 上下文注入：进入客服自动带当前订单上下文（从商品/订单页进入时携带入口上下文，客服端可见"用户从订单 88 访问"）、历史订单选择（用户切换上下文卡片）。
- 状态同步：卡片数据的时效（订单状态变化→会话内卡片更新或插入更新系统消息）、敏感操作确认（退款类操作二次确认+结果通知）。

```javascript
const CARD_TYPES = { order: OrderCard, logistics: LogisticsCard,
  refund: RefundForm };
function renderMessage(msg) {
  const C = CARD_TYPES[msg.type];
  return C ? <C {...msg.payload} convId={msg.convId} />
    : <TextMsg {...msg} />;
}
// 订单卡操作：action: 'refund' → 打开会话内表单
//   → 提交 → ws 系统消息回填 "已提交退款"
// 上下文：enterChat({ orderId }) → 首条系统消息
//   "咨询订单：{order}"（客服端与用户端同步可见）。
```
