---
title: [MFW-292] Session 轮换与并发登录策略
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-292：Session 轮换与并发登录

**答**:
- Access/Refresh 分离：access 短命（5-15min，无状态验）+ refresh 长命（有状态可吊销）——refresh 使用即轮换（rotating refresh token：旧 token 立即失效，重放检测 = 被盗信号）
- 并发登录策略三选：允许多设备（每设备独立 refresh 链）、单设备挤下线（新登录踢旧——版本号+1）、可配（金融类单设备/社交类多设备）——产品决策写进策略表
- 重放窗口处理：refresh 被重复使用（网络重试 vs 真被盗）→ 宽限 3s 内同 token 放行同结果（幂等），超窗吊销全家（tokenVersion+1 强制全端重登）
- 前端配合：401 单飞刷新（并发请求共享一次 refresh——ZSM-219 同款）——刷新风暴防护

```javascript
async function rotateRefresh(oldToken, ua) {
  const rec = await store.get(`rt:${hash(oldToken)}`)
  if (!rec) return forceReloginAll()                     // 未知 token
  if (rec.consumedAt && Date.now() - rec.consumedAt > 3000)
    return revokeFamily(rec.userId)                      // 重放超窗 → 全家吊销
  markConsumised(record)
  return issueNewPair(rec.userId, ua)                    // 轮换新对
}
```
