---
title: [ALG-413] 手写 BIT 持久化思想：历史快照前缀
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-413：手写 BIT 持久化思想：历史快照前缀

**答**：
- 题目：要查「昨天 14:00 时某渠道的累计消耗」——历史时点查询。BIT 每次修改存版本日志，查询指定时刻 = 重放日志到该时刻（离线）或可持久化 BIT（路径复制）。
- 思路：简化离线版——操作日志 [{t, idx, delta}]，查询(t, i) = 二分日志截断点 → 从头重放 BIT（O(操作数 log n)）。完整版：可持久化（BIT 本质是隐式树，可路径复制但工程上少见，通常用版本快照数组）。
- 评分点：离线重放的时间复杂度；可持久化 BIT 的可行性与工程取舍；快照节流方案。

```javascript
class VersionedBIT {
  constructor(n) { this.n = n; this.base = new Array(n + 1).fill(0);
    this.log = []; this.snapshotEvery = 100; this.snapshots = []; }
  add(t, i, v) {                                            // 带时间戳修改
    this.applyBIT(i, v);
    this.log.push({ t, i, v });
    if (this.log.length % this.snapshotEvery === 0)         // 快照节流
      this.snapshots.push({ t, state: [...this.base] });
  }
  applyBIT(i, v) { for (; i <= this.n; i += i & -i) this.base[i] += v; }
  queryAt(t, i) {                                           // 历史时点查询（离线重放）
    const snap = [...this.snapshots].reverse().find(s => s.t <= t);
    const bitArr = snap ? [...snap.state] : new Array(this.n + 1).fill(0);
    const idx = snap ? this.log.findIndex(e => e.t > snap.t) : 0;
    const from = idx < 0 ? this.log.length : idx;
    const bsum = j => { let s = 0; for (; j > 0; j -= j & -j) s += bitArr[j]; return s; };
    const badd = (j, v) => { for (; j <= this.n; j += j & -j) bitArr[j] += v; };
    for (const e of this.log.slice(from))                   // 重放至 t
      if (e.t <= t) badd(e.i, e.v); else break;
    return bsum(i);
  }
}
```

## 补充：评分点与变体

**评分点**：

- 离线重放要先用二分定位时间截断点再从头重放，线性扫描日志在操作量大时直接退化
- 重放复杂度是 O(k log n)，k 为截断点之前的操作数，不能笼统写成 O(log n)
- 可持久化 BIT 路径复制每次修改复制 O(log n) 个节点，节点总量与版本数同阶，这就是工程上少见的真实原因
- 快照节流按操作数或时间任一先到触发，只按时间在突发写入时会把内存顶穿

**变体与延伸**：

1. 查询时刻落在两次快照中间 → 取最近快照再重放其后的增量日志，这是「快照 + 重放」的标准组合
2. 日志无限增长怎么控 → 定期把旧日志合并进基线快照并截断，只保留可回溯窗口
3. 为什么生产很少真用可持久化 BIT → 指针复制的对象开销与 GC 压力超过收益，通常用版本化数组或直接换线段树
