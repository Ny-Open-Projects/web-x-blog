---
title: [ZSM-583] 多设备实时同步：last-write-wins 的适用与失效场景
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-583：多设备实时同步：last-write-wins 的适用与失效场景

**答**：
- LWW（last-write-wins）：每次写带时间戳/版本，冲突时取最新。适合**单值字段**语义清晰、且「新值覆盖旧值」天然合理的场景：昵称、头像、设置项开关、阅读位置。
- LWW 失效三类：1) **计数器**（未读数、点赞数）——两台设备各自 +1，LWW 只留一个，丢更新；要用增量操作同步（op-based）而不是值覆盖；2) **集合编辑**（清单项增删）——设备 A 删了项、设备 B 改了同名项，LWW 按整个集合覆盖，要么丢删除要么丢修改；3) **时钟不可信**——设备时间漂移（用户手动改时间）会让「最新」判断出错，要用服务端单调时钟或逻辑时钟（版本向量）。
- 改进路径：字段级 LWW（把状态拆细到叶子字段，只对冲突字段做覆盖）→ op-based（同步操作而非值，天然可交换）→ CRDT（完全去中心化收敛）。
- 工程落地：大多数业务「字段级 LWW + 计数器走 op」就够了，不必上完整 CRDT；判断标准是「冲突发生后用户能不能接受任意一方胜出」。
- 追问钩子：阅读位置这类「游标同步」要用 max（取最靠前的进度）而不是 LWW——语义化合并比机械策略更对。

```javascript
// 字段级 LWW + op 计数器的混合同步
function mergeDevices(local, remote) {
  const merged = { ...local }

  for (const [key, remoteField] of Object.entries(remote.fields)) {
    const localField = local.fields[key]
    // 每个字段带 { value, ts, device } —— 服务端时间戳
    if (!localField || remoteField.ts > localField.ts) merged.fields[key] = remoteField
    // 相同时间戳：用设备 id 决胜（确定性，两端算出同一结果）
    else if (remoteField.ts === localField.ts && remoteField.device > localField.device) {
      merged.fields[key] = remoteField
    }
  }

  // 计数器：op 合并（增量，不丢更新）
  merged.counters = {
    likes: (local.counters?.likes ?? 0) + (remote.opDelta?.likes ?? 0),
    unread: Math.max(local.counters?.unread ?? 0, remote.counters?.unread ?? 0),  // 游标取 max
  }
  return merged
}

// 场景对照
// nickname: LWW 合理（用户最后改的赢）
// likes:    op 合并（各设备 +1 都要计入）
// progress: max 合并（阅读进度取最远）
// cart:     服务端权威（交易态不走端上合并）
```
