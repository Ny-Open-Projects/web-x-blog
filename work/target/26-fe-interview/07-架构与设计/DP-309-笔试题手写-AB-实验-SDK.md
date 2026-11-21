---
title: [DP-309] 笔试题：手写 AB 实验 SDK（曝光/快照/锁定）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-309：笔试题：手写 AB 实验 SDK（曝光/快照/锁定）？
**题目**：实现 Experiments SDK：1) get(name) 返回分组（首次判定并触发曝光事件 assignment）；2) 会话锁定（同一会话同分组，sessionStorage）；3) 埋点自动附加分桶快照；4) 跨实验互斥（同层互斥）。
**评分点**：
- 分桶 hash 正确 + 层 salt 正交。
- 曝光事件直发不进批量队列（ARC-283）。
- 会话锁定读写正确（切换实验 key 粒度）。
- 埋点快照是当前全量分组 map。
```javascript
class Experiments {
  #ctx = {};
  constructor(private config, private track) {}
  init(uid) {
    const locked = JSON.parse(sessionStorage.getItem('__exp') ?? '{}');
    for (const exp of this.config) {                        // 4) 层互斥由层 salt 决定
      const v = locked[exp.name] ?? this.#assign(uid, exp);
      locked[exp.name] = v;
      if (!locked[`__assigned:${exp.name}`]) {
        this.track.sendNow('experiment:assignment', { exp: exp.name, value: v });  // 2) 曝光直发
        locked[`__assigned:${exp.name}`] = true;
      }
      this.#ctx[exp.name] = v;
    }
    sessionStorage.setItem('__exp', JSON.stringify(locked));
  }
  #assign(uid, exp) {
    return hash(`${exp.layer}:${exp.salt}:${uid}`) % 100 < exp.ratio ? exp.value : 'control';
  }
  get(name) { return this.#ctx[name] ?? 'control'; }
  snapshot() { return { ...this.#ctx }; }                  // 3) 埋点快照
}
// track.sendNow：曝光事件必须先于行为事件落库，用于归因窗口
```
