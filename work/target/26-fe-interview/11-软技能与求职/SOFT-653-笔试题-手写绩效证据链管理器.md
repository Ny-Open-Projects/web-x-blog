---
title: [SOFT-653] 手写 EvidenceLog：周记记录、证据分类检索、述职素材组装、缺口提醒？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-653：手写 EvidenceLog：周记记录、证据分类检索、述职素材组装、缺口提醒

**需求与边界**：
- 实现 EvidenceLog：add(entry)/assemble(period, n)/gapCheck()。
- 边界要求：① entry 含 { week, kind: 'result'|'process'|'testimony'|'growth', text, metric?, link? }，result 类必须有 metric（无则拒绝）；② assemble 从指定周期挑 n 条（result 优先，按重要性）组装成"挑战→行动→结果"半成品段；③ gapCheck 检测连续缺失（连续 2 周无记录则提醒）；④ 重复条目（同周同 text）幂等；⑤ 输出 markdown。

**答**：
```javascript
class EvidenceLog {
  constructor() { this.entries = []; this.seen = new Set(); }
  add(e) {
    if (e.kind === 'result' && !e.metric)
      throw new Error('result条目必须带metric');   // 结果必有数据
    const key = `${e.week}|${e.text}`;
    if (this.seen.has(key)) return false;          // 幂等
    this.seen.add(key);
    this.entries.push({ ...e, at: Date.now() });
    return true;
  }
  assemble(period, n = 5) {
    const pool = this.entries.filter(e =>
      e.week >= period.from && e.week <= period.to);
    const rank = { result: 0, testimony: 1, growth: 2, process: 3 };
    const picked = pool.sort((a, b) =>
      rank[a.kind] - rank[b.kind]).slice(0, n);
    return picked.map(e => e.kind === 'result'
      ? `### ${e.text}
- 挑战→行动→结果：${e.text}；数据：${e.metric}${e.link ? `（${e.link}）` : ''}`
      : `- 【${e.kind}】${e.text}`).join('\n');
  }
  gapCheck(lastWeek) {
    const weeks = new Set(this.entries.map(e => e.week));
    const missed = [];
    for (let w = lastWeek - 1; w >= lastWeek - 2; w--)
      if (!weeks.has(w)) missed.push(w);
    return missed.length >= 2
      ? { alert: `连续${missed.length}周无记录`, weeks: missed }
      : null;
  }
}
```

**评分点**:
- result 条目强制 metric（证据链的灵魂——无数据的结果不入库）。
- assemble 按 kind 权重排序（result 优先）组装述职半成品。
- gapCheck 连续缺失提醒（证据链断档预警）。

