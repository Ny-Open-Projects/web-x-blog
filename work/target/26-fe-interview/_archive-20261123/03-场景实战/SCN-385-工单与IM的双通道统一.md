---
title: [SCN-385] 客服双通道——IM 会话与工单的统一视图？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-385：客服 IM 会话与工单系统的统一视图怎么设计？

**答**:
- 会话与工单的关系模型：会话产生工单（IM 内一键转工单——上下文带过去 SCN-219）、工单关联会话（工单详情可见历史会话）、同一客户多触点统一（电话/IM/邮件工单归一客户视图——客户 360）。
- 统一工作台：客服工作台（左：当前会话/工单列表，中：对话/工单详情，右：客户 360+知识库——三栏布局），切换成本（会话转工单不丢上下文、工单回会话继续聊）。
- 状态一致性：会话结束与工单状态联动（会话结束→未解决自动转工单）、双通道消息同步（工单内回复同步到 IM 会话——客户无感知渠道差异）。
- 数据统一：客户 360（订单/历史工单/历史会话/会员状态聚合——SCN-296 搜索复用）、指标统一（响应时长跨渠道统计）。

```javascript
function AgentWorkspace({ me }) {
  return <ThreePane
    left={<QueueList mode={me.mode} />}       // 会话+工单队列
    center={<ConversationOrTicket active />}  // 当前上下文
    right={<Customer360 customer={active.customer}
      kb={<KbSuggest />} />} />;
}
// 会话→工单：toTicket(session, { carry: digestOf(session) })
// 状态联动：session.close → unresolved && autoTicket()
// 工单回复 → 同步 IM 会话（客户无感知）。
```
