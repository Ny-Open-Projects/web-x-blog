---
title: [NODE-439] Node 服务的业务配额（非流量限流）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-439：业务配额设计
**答**:
- 限流 vs 配额：限流保护系统瞬时容量（秒级令牌桶 NODE-360）；配额约束周期用量（用户每天导出 3 次/团队每月 API 10 万次/免费版存储 5GB）——是商业规则不是容量保护。
- 配额实现：配额计数器（Redis hash/DB 表，原子扣减）、周期重置（自然月/滑动 30 天）、预扣与回滚（任务提交先预扣，失败回滚——防并发超额）、超额语义（拒绝并引导升级 vs 排队 vs 降级）。
- 一致性：配额扣减与业务操作同事务或最终一致（配额超扣比少扣安全——先扣后放）；重置任务幂等（NODE-437）。
- 展示与预警：用量进度（前端展示 80%/100% 预警，ARC-469 组合矩阵）、管理员可调（配额变更即时生效 NODE-388）。
- 防绕过：配额以服务端为准（前端计数只是展示）、多端共享配额（账号维度）、异常刷量检测（配额消耗模式异常告警）。
```javascript
// 配额预扣 + 回滚
async function withQuota(uid, kind, cost, fn) {
  const ok = await luaDecr(`quota:${uid}:${kind}:${period()}`, cost);   // 原子预扣
  if (!ok) throw new QuotaExceeded(kind);
  try { return await fn(); }
  catch (e) { await luaIncr(`quota:${uid}:${kind}:${period()}`, cost); throw e; } // 失败回滚
}
```
