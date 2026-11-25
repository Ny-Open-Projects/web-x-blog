---
title: [NODE-541] Node 服务的账号注销（冷静期/级联清理）服务端如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-541：账号注销服务端
**答**:
- 流程状态机：申请（前置检查：余额/订阅/未完成订单——阻断项清单化）→ 冷静期（7 天可撤回——期间登录即撤回）→ 执行（级联清理编排 NODE-443）→ 完成（账号失效 + 通知）。
- 前置检查清单：资金类阻断（余额不为零 → 先提现/放弃余额确认）、权益类（订阅未到期 → 取消确认）、进行中事务（订单/提现中 → 等待完成）、关联账号（主账号注销 → 子账号处置策略）。
- 执行编排：数据清理计划（DB 匿名化/ES 删除/缓存清/数仓延迟清除——每步回执，失败重试 ARC-443 deletePlan）、会话全端踢出（ARC-415）、注销后登录尝试的处理（返回"账号已注销"而非"密码错误"——明确语义）、同手机号重新注册（新账号——不继承旧数据）。
- 合规：注销时效 SLA（合规要求内完成——编排超时告警）、删除完成度验证（NODE-443 抽检）、注销记录保留（注销行为本身留痕——合规审计）。
- 防滥用：注销刷号检测（注册-注销循环薅新人权益——风控标记 NODE-456）。
```javascript
// 注销编排
const plan = [
  { step: 'precheck', run: precheckAccount },                    // 阻断项清单
  { step: 'cooldown', until: '+7d' },                            // 冷静期
  { step: 'purge', run: () => orchestrate(deletePlan(uid)) },    // 级联清理
  { step: 'revoke', run: () => auth.revokeAllSessions(uid) },
  { step: 'verify', run: () => sampleVerifyPurged(uid) }         // 完成度抽检
];
login.onAccount(() => cooldownActive(uid) && cancelDeletion(uid)); // 登录撤回
```
