---
title: [TST-602] 笔试：实现测试架构决策记录（ADR）的索引与检索工具
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-602：笔试：实现测试架构决策记录（ADR）的索引与检索工具

**题目**：输入 ADR 数组 {id,title,status,supersededBy,tags,body}。实现 search(keyword,{status,tag}) 返回按相关度排序且标记 superseded 的列表；chain(id) 返回替代链，需防环。

**答**：
- ADR 用 id + status（proposed/accepted/superseded）+ supersededBy 表达演进，检索时必须标出已被取代的记录。
- 相关性按标题/标签/正文加权求和，标签命中权重最高。
- chain(id) 沿 supersededBy 正向追踪替代链，需防环。

```javascript
class ADRIndex {
  constructor(list) { this.map = new Map(list.map(a => [a.id, a])); }
  search(kw, { status, tag } = {}) {
    const q = String(kw || '').toLowerCase();
    return [...this.map.values()]
      .filter(a => !status || a.status === status)
      .filter(a => !tag || (a.tags || []).includes(tag))
      .map(a => ({ a, score: ((a.title.match(q) || []).length * 3)
        + ((a.tags || []).filter(t => t.includes(q)).length * 2)
        + ((a.body.match(q) || []).length) }))
      .filter(x => x.score > 0 || !kw)
      .sort((x, y) => y.score - x.score)
      .map(x => ({ ...x.a, score: x.score,
        superseded: !!x.a.supersededBy }));
  }
  chain(id) {
    const out = [], seen = new Set();
    let cur = this.map.get(id);
    while (cur && !seen.has(cur.id)) {
      seen.add(cur.id); out.push(cur.id);
      cur = cur.supersededBy && this.map.get(cur.supersededBy);
    }
    return out;
  }
}
```

**评分点**：
- 状态语义正确，superseded 标记无遗漏
- 相关度加权合理（标题 > 标签 > 正文）
- 替代链追踪且不死循环
- 每个方法职责单一、可单测
