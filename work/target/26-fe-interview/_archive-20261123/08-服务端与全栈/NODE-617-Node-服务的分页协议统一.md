---
title: [NODE-617] Node 服务的分页协议统一（cursor 规范全站落地）如何推进？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-617：分页协议统一
**答**:
- 协议统一：cursor 结构标准（base64(JSON [sortKey, tiebreakId])——排序字段+唯一 tiebreaker）、请求/响应规范（cursor/limit/nextCursor/hasMore——NODE-400 全站协议）、兼容期（offset 参数保留过渡——deprecation 流程 NODE-440）。
- 落地路径：新接口强制 cursor（脚手架模板默认——出生即正确）、存量接口迁移（每迭代顺带改——ARC-589 顺手偿还）、中间件封装（分页通用库——repo 层统一实现，业务零成本）、前端配合（无限滚动/分页组件统一——ARC-442/594）。
- 特殊场景：多字段排序 cursor（复合排序键编码——排序稳定性）、跳页需求（offset 兼容保留（低频管理页）——语义声明：跳页有性能代价）、实时插入的翻页一致性（cursor 天然免疫——对比 offset 的重复/漏数据）。
- 治理：接口分页方式清单（offset 存量清单——收敛进度追踪）、性能验收（深分页压测——OFFSET 10w 的耗时对比证据）。
- 度量：cursor 覆盖率（新接口 100%/存量收敛趋势）、深分页事故（归零目标）。
```javascript
// 统一分页中间件
function paginate(repo, { sort = 'id' }) {
  return async (q) => {
    const cur = decodeCursor(q.cursor);                          // [sortVal, id]
    const rows = await repo.page(cur, q.limit + 1);
    return { items: rows.slice(0, q.limit),
      nextCursor: rows.length > q.limit ? encodeCursor(rows[q.limit - 1]) : null };
  };
}
```
