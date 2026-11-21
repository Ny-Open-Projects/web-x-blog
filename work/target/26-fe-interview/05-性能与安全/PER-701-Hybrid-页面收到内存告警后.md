---
title: [PER-701] Hybrid 页面收到内存告警后怎么响应？内存告警的分级行动清单与自动执行器
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-701：Hybrid 页面收到内存告警后怎么响应？内存告警的分级行动清单与自动执行器

**答**：
- 内存告警分级（容器 SDK 回调）：**一级（轻度）**——清理图片缓存/非当前路由组件状态；**二级（中度）**——降级重资源（关动画、图降清、虚拟列表窗口减半）；**三级（严重）**——释放大对象、提示用户刷新或自动保存状态后重载页面。
- 行动清单要提前注册（各模块声明自己的可释放资源与降级动作"），告警时按级遍历执行——事故现场没有时间想。
- 前置预防：大对象用完置 null、长列表窗口收窄、图片内存控制器（677）预算随档位调整——告警是最后防线，预算控制才是主战场。
- 度量：告警频次/页面分布、降级动作执行成功率、告警后崩溃率变化。

```javascript

const memoryAlarmLevels = {
  l1: ['clearImageCache', 'clearRouteState(非当前)'],
  l2: ['disableHeavyAnimation', 'downgradeImageTier', 'shrinkListWindow(减半)'],
  l3: ['releaseBigObjects', 'saveStateAndReload(自动保存+重载提示)'],
  registry: '各模块预注册可释放资源与降级动作，告警按级遍历执行',
  prevention: '告警是最后防线：大对象置 null/列表窗口收窄/图片预算控制才是主战场',
};
class MemoryAlarmExecutor {
  constructor(actions) { this.actions = actions; this.executed = new Set(); }
  onAlarm(level, bridge) {                                       // 容器 SDK 内存告警回调
    for (const act of memoryAlarmLevels[`l${level}`] ?? []) {
      if (this.executed.has(act)) continue;                      // 同一次告警不重复执行
      try { this.actions[act]?.(bridge); this.executed.add(act);
        track('mem-alarm-action', { level, act, ok: true }); }
      catch (e) { track('mem-alarm-action', { level, act, ok: false }); }
    }
    if (level === 3) this.executed.clear();                      // 严重级后重置（重载前）
  }
}
```
