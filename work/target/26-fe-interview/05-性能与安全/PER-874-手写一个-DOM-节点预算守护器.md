---
title: [PER-874] 手写一个 DOM 节点预算守护器：实时统计节点数、超预算告警与来源建议
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-874：手写一个 DOM 节点预算守护器：实时统计节点数、超预算告警与来源建议

**答**：
- 需求：实现 NodeBudgetGuard：start({budget, interval}) 周期采样 document 节点总数；连续 2 次超预算触发告警（带节点数/超出比例/最大子树 Top3 的 owner 标记）；stop 清理定时器；支持 unregister（第三方容器注册后可单独豁免其子树）。
- 边界：interval 采样用 requestIdleCallback（不抢占主线程）；豁免子树不计入统计；页面隐藏（document.hidden）暂停采样。
- 评分点：连续超限才告警（防毛刺）；idle 采样；豁免子树剔除。

```javascript
class NodeBudgetGuard {
  constructor() { this.exempt = new Set(); this.timers = []; }
  exemptSubtree(el) { this.exempt.add(el); }
  count() {
    let n = 0;
    const walk = el => {
      if (this.exempt.has(el)) return;                         // 豁免子树剔除
      n++;
      for (const c of el.children) walk(c);
    };
    walk(document.documentElement);
    return n;
  }
  start({ budget = 3000, interval = 5000, onAlert } = {}) {
    let overStreak = 0;
    const tick = () => {
      if (document.hidden) { this.timers.push(setTimeout(tick, interval)); return; }   // 隐藏暂停
      const n = this.count();
      if (n > budget) {
        if (++overStreak >= 2) onAlert({ n, ratio: +(n / budget).toFixed(2),   // 连续超限
          biggest: topSubtrees(3) });
      } else overStreak = 0;
      this.timers.push(setTimeout(tick, interval));
    };
    this.timers.push(setTimeout(tick, interval));
  }
  stop() { this.timers.forEach(clearTimeout); this.timers = []; }
}
function topSubtrees(k) {                                      // 最大子树 TopK（owner 标记）
  return [...document.querySelectorAll('body > *')]
    .map(el => ({ owner: el.dataset?.owner || el.tagName.toLowerCase(),
      nodes: el.querySelectorAll('*').length + 1 }))
    .sort((a, b) => b.nodes - a.nodes).slice(0, k);
}
```
