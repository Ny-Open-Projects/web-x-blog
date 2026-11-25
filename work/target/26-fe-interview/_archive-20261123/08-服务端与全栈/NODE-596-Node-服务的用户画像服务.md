---
title: [NODE-596] Node 服务的用户画像（标签体系/实时特征）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-596：用户画像服务
**答**:
- 标签体系：标签分类（基础/行为/偏好/风险——标签字典：定义/口径/更新频率/owner——ARC-614 口径治理思想）、离线标签（T+1 批算——数仓）、实时标签（会话内行为——特征服务）。
- 画像服务：标签查询（批量接口——推荐/风控/营销消费）、画像写入（事件驱动标签更新——幂等）、标签生命周期（衰减：行为标签时效——过期自动失效；冲突合并规则）。
- 应用边界：画像消费方权限（标签敏感性分级——健康/金融类标签强权限）、画像与推荐/营销联动（人群圈选——ARC-554 名单）、隐私合规（标签可解释（用户可查自己的标签）、删除权联动 NODE-443）。
- 一致性：标签口径变更治理（版本化——下游感知）、画像与登录身份关联（匿名→实名合并 ARC-572 merge）。
- 观测：标签覆盖率/新鲜度（实时标签延迟）、消费方调用画像画像（谁在用——治理）。
```javascript
// 画像标签查询（消费方鉴权）
app.post('/profile/batch', requirePerm('profile:read'), async (ctx) => {
  const tags = await profileService.batch(ctx.body.uids, {
    groups: ctx.body.groups, sensitivity: permOf(ctx.caller) }); // 按调用方权限裁剪敏感标签
  ctx.body = tags;
});
```
