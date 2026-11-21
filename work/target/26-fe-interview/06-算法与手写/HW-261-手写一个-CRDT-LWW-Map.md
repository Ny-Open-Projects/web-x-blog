---
title: [HW-261] 手写一个 CRDT LWW-Map：对象字段的并发写合并
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-261：手写一个 CRDT LWW-Map：对象字段的并发写合并

**答**：
- 需求：实现 LWWMap：set(key, value, ts)（LWW：ts 大胜，平局 siteId 大胜）；delete 是 value=null 的写；merge(remote) 合并远端状态；dump 输出含删除墓碑的完整状态（供增量同步）；read 忽略 null。
- 边界：写后删 vs 删后写按 ts 定（同 ts 平局规则）；时钟回拨防护（本地 ts 单调递增）；增量同步（对端上次版本之后的变化）。
- 评分点：LWW 平局规则；本地时钟单调；增量 diff。

```javascript
class LWWMap {
  constructor(siteId) { this.site = siteId; this.state = new Map(); this.lastTs = 0; }
  set(key, value) {
    const ts = Math.max(Date.now(), this.lastTs + 1);       // 本地时钟单调
    this.lastTs = ts;
    this.state.set(key, { value, ts, site: this.site, del: value === null });
  }
  merge(entries) {                                          // 远端状态合并
    for (const [key, e] of entries) {
      const cur = this.state.get(key);
      if (!cur || e.ts > cur.ts || (e.ts === cur.ts && e.site > cur.site))
        this.state.set(key, e);
    }
  }
  read(key) { const e = this.state.get(key); return e && !e.del ? e.value : undefined; }
  delta(sinceTs) {                                          // 增量：某时刻后变化
    return [...this.state].filter(([, e]) => e.ts > sinceTs);
  }
  dump() { return [...this.state]; }                        // 含墓碑全量
}
```
