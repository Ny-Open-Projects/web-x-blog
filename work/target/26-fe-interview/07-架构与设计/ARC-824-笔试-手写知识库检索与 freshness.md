---
title: [ARC-824] 笔试：手写知识库保鲜机制
date: 2026-11-21
categories: [前端架构]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## ARC-824：手写知识库保鲜

**答**：实现架构知识库的保鲜机制 `KnowledgeFreshness`：① 文档登记：{ id, title, lastReviewed, owner, relatedVersion(关联架构版本), tags }；② 保鲜评分：距上次 review 的时间衰减（<3 月 100 分 / 3~6 月 70 / 6~12 月 40 / >12 月 20）——过期文档评分低；③ 关联校验：文档 relatedVersion 与当前架构版本不匹配 → 标注「可能过时」（旧架构的文档防误导）；④ 刷新提醒：评分 <40 的文档 → owner 刷新任务（到人到时）；⑤ 无人认领处理：owner 离职（成员清单比对）→ 文档转公共待认领池。写出实现。

```javascript
class KnowledgeFreshness {
  #docs = new Map(); #members = new Set();
  constructor(docs, members) {
    docs.forEach((d) => this.#docs.set(d.id, d));
    members.forEach((m) => this.#members.add(m));
  }
  freshnessScore(doc, now = Date.now()) {
    const months = (now - new Date(doc.lastReviewed).getTime()) / (30 * 86400e3);
    const score = months < 3 ? 100 : months < 6 ? 70 : months < 12 ? 40 : 20;
    const versionMatch = doc.relatedVersion === CURRENT_ARCH_VERSION;
    return { score, versionMatch,
      stale: score < 40 || !versionMatch,
      reason: !versionMatch ? `关联架构版本 ${doc.relatedVersion} ≠ 当前 ${CURRENT_ARCH_VERSION}` : null };
  }
  refreshTasks() {
    const tasks = [];
    for (const [id, doc] of this.#docs) {
      const f = this.freshnessScore(doc);
      if (!f.stale) continue;
      const ownerAlive = this.#members.has(doc.owner);
      tasks.push({
        docId: id, title: doc.title, score: f.score, reason: f.reason,
        assignee: ownerAlive ? doc.owner : 'UNCLAIMED',
        note: ownerAlive ? null : `owner ${doc.owner} 已离职 → 转待认领池`,
      });
    }
    return tasks.sort((a, b) => a.score - b.score);    // 最腐烂的优先
  }
  search(query, { includeStale = false } = {}) {
    // 搜索结果标注新鲜度 (用户看到 staleness 标记自行判断)
    const hits = this.#match(query);
    return hits.map((d) => ({ ...d, freshness: this.freshnessScore(d) }))
      .filter((d) => includeStale || d.freshness.score >= 40);
  }
}
```

**评分点**：
- 时间衰减评分（3/6/12 月阶梯）
- 架构版本关联校验（旧版本文档标注「可能过时」）
- owner 离职检测 → 待认领池（文档不死人手散）
- 搜索结果的新鲜度标注（用户自行判断）
