---
title: [SCN-219] IM 客服会话——人工客服与机器人衔接的体验设计？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-219：客服 IM 中机器人转人工的衔接体验怎么设计？

**答**:
- 模式标识：机器人/人工状态在会话头部明确标识（切换时系统消息提示"客服 XX 已接入"）——用户知道在跟谁说话，避免"对机器人发火"的体验事故。
- 转人工流程：入口显性（机器人回答底部常驻"转人工"）、排队态（当前第 N 位/预计等待，排队中机器人可继续服务简单问题）、接入交接（机器人把上下文摘要传给人工——用户不用重复描述；人工端看到机器人的对话摘要与用户意图标签）。
- 上下文携带：转人工时携带（用户问题摘要/已尝试的自助方案/订单上下文），人工侧一个面板看到全部——衔接质量的关键是上下文无损传递。
- 中断与超时：人工长时间未回复（>2 分钟）→ 提示可留言（异步工单）+ 保留会话；用户离开后人工回复→推送通知；会话结束评价（满意度收集放在明确的结束点）。

```javascript
async function transferToHuman(convId) {
  const q = await csApi.enqueue(convId, {
    digest: summarize(bot.history),          // 上下文摘要
    intent: bot.detectedIntent,              // 意图标签
    tried: bot.solutionsTried,               // 已尝试方案
  });
  setMode('queueing', { position: q.position,
    eta: q.eta });
  // 排队中机器人继续兜底简单问题
  pollQueue(q.token);
}
ws.on('cs_joined', (e) => {
  setMode('human', { agent: e.agent });
  system(`客服 ${e.agent.name} 已接入`);
});
ws.on('cs_message', (m) => {
  append(m);
  if (idle(m.agent) > 120e3) suggestLeaveMessage(); // 超时留言
});
```
