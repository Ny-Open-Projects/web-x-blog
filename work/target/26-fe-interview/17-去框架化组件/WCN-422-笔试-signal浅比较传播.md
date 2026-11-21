---
title: [WCN-422] 笔试：computed 的「依赖版本验证」惰性重算实现。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-422：笔试：computed 的「依赖版本验证」惰性重算实现。
**题目**：computed 存上次计算时的依赖版本号集合；读取时比对：全相同 → 返回缓存；任一变化 → 重算。版本号 = 全局 epoch（每次写 ++）。

```javascript
let epoch = 0;
function computedLazy(fn) {
  const node = { deps: new Map(), cached: undefined, hasValue: false,
    get() {
      track(this);
      if (this.hasValue) {
        for (const [d, ep] of this.deps)
          if (d.epoch !== ep) { this.recompute(); break; }   // 版本验证
      } else this.recompute();
      return this.cached;
    },
    recompute() {
      stack.push(this);
      this.cached = fn();
      stack.pop();
      this.deps = new Map([...collectDeps(this)].map(d => [d, d.epoch]));
      this.hasValue = true;
    } };
  return node;
}

```

**评分点**：
- 版本快照：计算时记录 {depNode: epoch}。
- 验证 O(依赖数)（无传播开销）。
- 重算后更新快照。
- 与脏标记方案对比说明（写窄 vs 读验证）。
