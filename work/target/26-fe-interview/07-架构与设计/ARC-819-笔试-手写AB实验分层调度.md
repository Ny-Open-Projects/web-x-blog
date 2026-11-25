---
title: [ARC-819] 笔试：手写 AB 实验分层调度
date: 2026-11-21
categories: [前端架构]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## ARC-819：手写 AB 分层调度

**答**：实现多团队 AB 实验的分层调度器 `ExperimentManager`：① 实验注册：{ id, layer(域: 搜索/推荐/交易), traffic(流量百分比), teams }——同层实验互斥（总流量 ≤100%）、跨层正交（各层独立分流）；② 分流：`assign(userId)`——每层独立哈希（同层内按实验注册顺序切分流量预算）；③ 流量预算管理：注册时校验同层总流量 ≤100%（超卖拒绝）；④ 实验生命周期：running → paused → concluded（concluded 后流量归还预算池）；⑤ 冲突告警：同层两个实验都改同一 UI 区域（declared areas 重叠）→ 注册时告警。写出实现。

```javascript
class ExperimentManager {
  #exps = new Map();   // id -> { layer, traffic, areas, status }
  register(exp) {
    // 同层流量预算校验
    const layerTotal = [...this.#exps.values()]
      .filter((e) => e.layer === exp.layer && e.status === 'running')
      .reduce((s, e) => s + e.traffic, 0);
    if (layerTotal + exp.traffic > 1) throw new Error(`layer ${exp.layer} 流量超卖: ${layerTotal + exp.traffic}`);
    // 同层 UI 区域冲突告警
    const conflicts = [...this.#exps.values()].filter((e) =>
      e.layer === exp.layer && e.status === 'running' &&
      e.areas?.some((a) => exp.areas?.includes(a)));
    if (conflicts.length)
      console.warn(`[exp] ${exp.id} 与 ${conflicts.map((c) => c.id).join(',')} 的 UI 区域重叠`);
    this.#exps.set(exp.id, { ...exp, status: 'running' });
  }
  assign(userId) {
    const result = {};
    const layers = new Set([...this.#exps.values()].map((e) => e.layer));
    for (const layer of layers) {                       // 跨层独立哈希(正交)
      const exps = [...this.#exps.values()].filter((e) => e.layer === layer && e.status === 'running');
      const h = stableHash(`${layer}:${userId}`);       // 层内统一哈希→切分段
      let acc = 0;
      for (const e of exps) {
        acc += e.traffic;
        if (h < acc) { result[layer] = e.id; break; }
      }
      result[layer] ??= 'control';                      // 未命中任何实验
    }
    return result;                                      // { search: 'exp1', trade: 'control' }
  }
  conclude(id) { const e = this.#exps.get(id); e.status = 'concluded'; }   // 流量归还
}
function stableHash(s) { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) >>> 0; return (h % 10000) / 10000; }
```

**评分点**：
- 分层正交（各层独立哈希——实验互不污染）
- 同层互斥（流量预算 ≤100% 超卖拒绝）
- UI 区域冲突告警（注册时发现——比运行时发现早）
- concluded 流量归还（生命周期闭环）
