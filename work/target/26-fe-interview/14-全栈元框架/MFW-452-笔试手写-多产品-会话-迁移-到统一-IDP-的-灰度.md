---
title: [MFM-452→MFM→MFW-452] 笔试：手写会话迁移灰度控制器（双凭证期）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFM→MFW-452：会话迁移灰度
**需求**：实现 `sessionCutover(users, { stages = [0.01, 0.1, 0.5, 1] } = {})`：1) 用户分桶进新 IdP（sticky hash——同用户不摇摆）；2) 双凭证期：旧 session 未到期仍有效 + 新登录走 IdP——验证期互不干扰；3) 迁移动作：用户首触新域→静默 exchange（旧凭证换新——无感）；失败→保留旧会话重试（不锁死用户）；4) 指标门禁：每阶段登录成功率/静默换发失败率 <0.1% 才放下一档；5) 紧急停（比例回退 0——已迁移用户会话兼容读旧——双向兼容写入）。

```javascript
export function cutoverMid (req, { pct, oldAccept = true) } = {}) {
  const inNew = bucketOf (uid, 'idp-cut') < pct * 100
  const cred = req.cookie('sid_new') ?? req.cookie('session_old')
  const sess = inNew && hasNew ? verifyNew (v) : verifyOld (o) (dual read)
  if (inNew && !hasNew && hasOld && autoExchangeOk) silentExchange()      // 无感换发
  if (exchangeFail) fallBackOldSession()                    // 不锁死：失败留旧
  metrics.push({ stage: pctOf(uid), ok: !!sess, kind })
}
// gate: stage[i+1] 需 stage[i] failRate < 0.1% 且 48h 稳定
```
**评分点**：
- sticky 分桶 + 阶梯 gate（数据驱动放档——不拍脑袋全量）
- 无感 exchange + 失败留旧（迁移永不锁死用户——可用性第一）
- 双向兼容读（回退比例=已迁用户也能回旧验证——真可回滚）
- 静默失败率指标（迁移健康度量化）
