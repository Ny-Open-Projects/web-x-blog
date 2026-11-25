---
title: [AGT-283] Agent 权限体系——最小权限原则怎么落地到工具与数据？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-283：Agent 的最小权限怎么设计——不是把用户权限整个给它？

**答**:
- 权限三层解耦：用户权限（用户在系统中的真实权限）、任务权限（当前任务需要的最小权限集合）、Agent 能力（被授权的工具与数据范围）——Agent 拿到的应是"任务权限"而非完整用户权限：查订单任务不应能删数据库。
- 落地手段：工具级 scope（每个工具声明所需权限，运行时校验）、数据级行级过滤（Agent 查询自动带用户 ACL，AGT-217）、会话级能力列表（任务开始时授最小集合，任务结束即回收）、操作分级（读/写/删的授权门槛递增，AGT-246）。
- 动态权限：按任务阶段渐进授权（先读分析→用户确认后授写权限）——"先看后写"模式让用户在知情下放权，也是产品体验的一部分。
- 审计与回收：每次能力使用有日志（谁/何时/用了什么能力/影响范围）；权限配置版本化可回滚；离职/降权用户自动同步 Agent 权限。

```javascript
async function scopedSession(user, task) {
  const caps = minimalCapsFor(task);      // 任务最小集合
  const session = {
    user, caps,
    can(tool) { return this.caps.includes(tool)
      && aclAllows(user, tool); },        // 双重校验
  };
  // 读阶段后动态升级：
  // writeConfirm() → caps.push('write') 需用户确认
  return session;
}
// 结束：session.destroy() 回收全部能力
```
