---
title: [AIC-133] Agent 长任务的超时与心跳怎么设计？「僵尸任务」怎么发现与处理？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-133：Agent 长任务的超时与心跳怎么设计？「僵尸任务」怎么发现与处理？
**答**：
- 超时分层：单步超时（一次工具调用 60s~10min，按工具类型）+ 任务总时长上限（按任务类型预算，如普通任务 30min）+ 预算超限（token/费用超预算即停，AIC-087）。
- 心跳设计：agent 每完成一步上报心跳（step 完成事件）；监控按「最后心跳 > 阈值（如 5 分钟）」判定僵尸——僵尸任务的典型特征是进程活着但没有新步骤。
- 僵尸处理：自动终止 + 保留现场（trace 与已做改动）+ 回滚到绿色快照（AIC-083）+ 记入失败样本；连续僵尸告警排查（常见根因：工具调用死循环、模型限流卡死）。
- 恢复而非重来：僵尸任务若已完成大半，产出交接文件（AIC-100）让新会话续作——损失最小化。
- 追问钩子：超时设计的哲学是「宁可误杀也不能僵尸占资源」——误杀成本低（可续作），僵尸的成本是资源占用与人的注意力。

```javascript
// 心跳监控器
class HeartbeatMonitor {
  #last = new Map(); // taskId -> ts
  beat(taskId) { this.#last.set(taskId, Date.now()); }
  sweep({ zombieMs = 5 * 60_000 } = {}) {
    const now = Date.now();
    return [...this.#last.entries()]
      .filter(([id, ts]) => now - ts > zombieMs)
      .map(([id]) => { terminate(id); rollbackToGreen(id); return id; });
  }
}
```
