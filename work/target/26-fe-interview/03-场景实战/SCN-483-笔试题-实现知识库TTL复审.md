---
title: [SCN-483] 笔试题——实现知识复审调度（TTL/到期提醒/复审流转）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-483：手写知识库 TTL 复审：到期调度、owner 提醒、复审流转与降权

**需求与边界**：
- 输入：文档（reviewDueAt）、调度器；输出：复审流程。
- 边界要求：① 到期前 7 天提醒 owner；② 到期未复审→检索降权+"已过期"标注（SCN-312 复用）；③ 复审通过→TTL 刷新；④ 复审可委托/批量。

**答**：
```javascript
class ReviewScheduler {
  constructor({ docs, notify }) {
    docs.on('change', () => this.sync(docs));
    setInterval(() => this.check(), 3600e3);   // 1h 巡检
  }
  check() {
    for (const d of docs.dueIn(7 * 864e5))     // 7 天内到期
      if (!d.reminded) {
        notify(d.owner, `知识《${d.title}》将于 ${fmt(d.reviewDueAt)} 到期复审`);
        d.reminded = true;
      }
    for (const d of docs.expired()) {          // 已过期
      search.downweight(d.id);                 // 检索降权
      markStale(d.id);                         // "已过期"标注
    }
  }
  async review(docId, { approve, delegatedTo }) {
    if (delegatedTo) reassign(docId, delegatedTo);  // 委托
    if (approve) {
      docs.refreshTTL(docId, 180 * 864e5);     // 通过：TTL 刷新
      search.restore(docId);                   // 恢复权重
    } else docs.markDeprecated(docId);         // 不通过：废弃归档
    audit.log({ docId, action: 'review', approve });
  }
}
// 批量复审：owner 多文档一键确认（逐条审计）。
```

**评分点**:
- 到期前提醒（7 天）+过期降权标注双阶段。
- 复审流转：通过刷新 TTL 恢复权重/不通过废弃归档。
- 委托与批量复审支持。
- 审计留痕。
