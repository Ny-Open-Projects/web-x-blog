---
title: [MFW-317] 大型分步表单的 Server 侧草稿与恢复
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-317：分步表单 Server 草稿

**答**:
- 架构：每步完成即 PATCH 草稿资源（/api/form/:draftId/step/2——部分保存非整体事务）→ 服务端聚合校验只在最终提交；刷新/换设备凭 draftId 恢复（ZSM-376 的 server 强化版）
- 草稿生命周期：TTL 7 天（清理 job）+ schema 版本号（变更后旧草稿迁移或提示重填——防语义错位恢复）
- 安全：draftId 不透明随机串（不可枚举）+ 归属校验（只能读写自己的草稿——IDOR 防线）；敏感字段草稿期加密存储
- 体验闭环：步骤进度由服务端状态驱动（刷新不丢）+ 最终全量校验错误定位到步（跳回出错步并高亮字段）

```javascript
await prisma.formDraft.updateMany({
  where: { id, ownerId: user.id },                     // 归属校验（IDOR）
  data: { step2: encryp(tFields), version, updatedAt: now },
})
// 恢复：GET → schema 版本比对 → 迁移或提示；提交全量校验 → fieldErrors 定位步
```
