---
title: [SOFT-774] 手写 techRadar：四环清单管理、环迁移记录、引入纪律检查（champion/退出标准）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-774：手写 techRadar：四环清单管理、环迁移记录、引入纪律检查（champion/退出标准）

**需求与边界**：
- 实现 TechRadar：place(tech, ring)/move(tech, toRing, reason)/checkIntroduce(tech)。
- 边界要求：① 四环 adopt/trial/assess/hold；② 引入检查：trial 环新增必须配 champion 与退出标准（缺则拒绝）；③ move 记录迁移历史（何时为何迁移——雷达的演进可追溯）；④ hold 环的重新评估（hold 超 1 年的项提示复查——环境可能变了）；⑤ 输出雷达快照。

**答**：
```javascript
class TechRadar {
  constructor() {
    this.rings = { adopt: new Map(), trial: new Map(),
      assess: new Map(), hold: new Map() };
    this.history = [];
  }
  place(tech, ring) {
    if (!this.rings[ring]) throw new Error(`未知环：${ring}`);
    this.rings[ring].set(tech, { at: Date.now() });
    this.history.push({ tech, to: ring, at: Date.now() });
  }
  move(tech, toRing, reason) {
    const from = Object.keys(this.rings)
      .find(r => this.rings[r].has(tech));
    if (!from) throw new Error(`未收录：${tech}`);
    if (toRing === 'trial') this.checkIntroduce(tech);
    this.rings[from].delete(tech);
    this.rings[toRing].set(tech, { at: Date.now(), reason });
    this.history.push({ tech, from, to: toRing, reason, at: Date.now() });
  }
  checkIntroduce(tech, { champion, exitCriteria }) {
    if (!champion || !exitCriteria)
      throw new Error(`引入${tech}必须配champion与退出标准`);
  }
  review(now = Date.now()) {
    const stale = [];
    for (const [tech, meta] of this.rings.hold)
      if (now - meta.at > 365 * 864e5)
        stale.push({ tech, note: 'hold超1年——复查环境是否变化' });
    return { snapshot: Object.fromEntries(Object.entries(this.rings)
      .map(([r, m]) => [r, [...m.keys()]])), staleReview: stale,
      history: this.history.slice(-10) };
  }
}
```

**评分点**:
- trial 环引入强制 champion+退出标准（引入纪律制度化）。
- 迁移历史可追溯（雷达演进留痕）。
- hold 超 1 年复查（环境变化的重新评估）。

