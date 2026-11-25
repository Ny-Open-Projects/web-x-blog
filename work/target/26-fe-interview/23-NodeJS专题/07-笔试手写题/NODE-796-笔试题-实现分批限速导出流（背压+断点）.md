---
title: [NODE-796] 笔试题——实现分批限速导出流（游标 + 背压 + 断点）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-796：手写限速导出

**需求与边界**：
- 需求：大导出流（SCN-NODE-681/796）——① DB 游标流（SCN-NODE-725 pipeline）；② 分批限速（每批 sleep——DB 保护，SCN-联想-770 限速）；③ 断点（游标记录——中断续导）；④ 完成通知（SCN-FIN-512）。
- 边界：① 断点与幂等（续导从游标继续——upsert 幂等）；② 游标稳定性（排序键唯一——ts+id，SCN-FIN-739）；③ 失败的中断处理（客户端断开——游标销毁，SCN-NODE-725）。

**答**：
```javascript
async function exportStream(res, query, taskId) {
  const start = await getCursor(taskId) ?? { ts: 0, id: 0 };   // 断点（SCN-联想-770）
  let cursor = start, rows = 0;
  res.setHeader('Content-Type', 'text/csv');
  res.write('id,name,ts\r\n');
  while (true) {
    if (res.destroyed) { saveCursor(taskId, cursor); return; }   // 客户端断开存游标
    const batch = await db.query(`SELECT * FROM t WHERE (ts,id) > ($1,$2)
      ORDER BY ts,id LIMIT 500`, [cursor.ts, cursor.id]);   // 双键游标（SCN-FIN-739）
    if (!batch.length) break;
    for (const r of batch) { res.write(toCsv(r)); rows++; }
    cursor = { ts: batch.at(-1).ts, id: batch.at(-1).id };
    saveCursor(taskId, cursor);                        // 游标断点
    await sleep(100);                                  // 分批限速（DB 保护）
    progress(taskId, rows);                            // 进度（SCN-FIN-512）
  }
  notifyDone(taskId);                                  // 完成（SCN-FIN-512）
}
```

**评分点**:
- 双键游标断点（中断续导——SCN-联想-770）。
- 分批限速（DB 保护——sleep 节流）。
- 客户端断开存游标（资源回收 + 断点——SCN-NODE-725 联动）。
- 完成通知（任务化——SCN-FIN-512）。
