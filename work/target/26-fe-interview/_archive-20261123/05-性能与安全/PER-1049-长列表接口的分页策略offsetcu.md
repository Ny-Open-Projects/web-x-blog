---
title: [PER-1049] 长列表接口的分页策略：offset/cursor 与稳定性
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1049：长列表接口的分页策略：offset/cursor 与稳定性

**答**：
- offset 分页实现简单但数据变更时页内容漂移（删除导致重复/跳过）；cursor（基于位置/时间戳）稳定但要求数据有序且游标不可篡改。
- 深水：cursor 伪造风险（遍历他人数据）——游标要签名或使用不可枚举的内部 ID；offset 有深分页性能问题（DB 前扫描）。
- 前端体验：无限滚动 + cursor；列表刷新用"新 cursor + 增量 diff"，避免整页替换导致滚动位置丢失。
- 混合方案：首屏 offset 快速出数据，继续滚动切 cursor。

```javascript
function cursorPaginate(fetcher, { pageSize = 20 } = {}) {
  let cursor = null, done = false;
  return {
    async next() {
      if (done) return { items: [], done };
      const r = await fetcher({ cursor, limit: pageSize });
      cursor = r.nextCursor;
      done = !cursor;
      return { items: r.items, done };
    },
    reset() { cursor = null; done = false; },   // 数据源变更时重置
  };
}
// 服务端校验 cursor 签名：HMAC(cursor+uid)，伪造返回 400
```
