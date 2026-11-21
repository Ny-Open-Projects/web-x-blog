---
title: [NODE-574] Node 服务的敏感操作二次确认（二次认证编排）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-574：敏感操作二次确认
**答**:
- 敏感操作清单：改密码/改手机/改支付设置/提现/注销——操作分级（各操作的认证强度：密码 → OTP → 人脸——策略配置）。
- 编排协议：操作发起 → 返回 challenge（认证方式清单——用户选择或默认）→ 完成认证 → 认证凭证（短时一次性）→ 重放原操作（带凭证）——ARC-613 挑战协议同构。
- 实现细节：认证凭证绑定（凭证绑定操作类型 + 上下文——防拿 A 操作凭证做 B）、时效（5 分钟）、失败次数限制（防暴力——锁定退避）、认证方式降级（主方式不可用（手机丢了）→ 备用通道——找回流程安全 ARC-455）。
- 体验：认证记忆（同会话内同类操作短窗免二次——平衡安全与体验，策略化）、风险自适应（低风险环境跳过二次——风控分驱动 NODE-456）。
- 审计：二次认证事件全记录（认证方式/结果——合规）。
```javascript
// 二次认证编排
app.post('/sensitive/withdraw', async (ctx) => {
  if (!(await sfa.satisfied(ctx.user, 'withdraw', ctx.session)))
    return { challenge: sfa.challenges(ctx.user, 'withdraw') };  // 返回挑战清单
  return doWithdraw(ctx.body, ctx.state.sfaCred);                // 凭证通过执行
});
// sfa.satisfied：会话内最近 5min 已认证同类操作 → 复用（策略记忆）
```
