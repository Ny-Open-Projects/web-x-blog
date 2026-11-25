---
title: [NODE-905] 笔试题——实现多实例请求分流的会话一致性（sticky + 回退）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-905：手写会话一致

**需求与边界**：
- 需求：sticky 分流（SCN-OPS-244）——① 会话版本戳（cookie——SCN-OPS-244）；② sticky 失效回退（实例下线——重新分流，SCN-NODE-703 服务发现联动）；③ 灰度横跳防御（SCN-OPS-244 核心语义）；④ sticky 与弹性伸缩的冲突（缩容实例的会话迁移——SCN-NODE-834）。
- 边界：① sticky 的 TTL（24h——SCN-OPS-244）；② 回退后的数据一致性（新实例拿不到旧实例内存状态——状态外置，SCN-NODE-637）；③ sticky 的覆盖（紧急回滚——SCN-OPS-244）。

**答**：
```javascript
function resolveInstance(session, user, instances) {
  if (session.instanceId && instances.some(i => i.id === session.instanceId && i.healthy))
    return session.instanceId;                         // sticky 命中（SCN-OPS-244）
  if (emergencyRollback) return stableInstance();      // 覆盖 sticky（SCN-OPS-244）
  const inst = lb.pick(user);
  session.instanceId = inst.id;                        // 首次分配固化
  return inst.id;
}
// 实例下线：sticky 失效 → 重新分流（SCN-NODE-703 discovery watch）
discovery.on('removed', (id) => sessionsOn(id).forEach(s => delete s.instanceId));
```

**评分点**:
- sticky 命中/失效/覆盖三语义（SCN-OPS-244）。
- 实例下线的 sticky 失效（SCN-NODE-703 联动）。
- 状态外置声明（SCN-NODE-637 集群原则）。
- 紧急回滚覆盖（SCN-OPS-244）。
