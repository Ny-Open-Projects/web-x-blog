---
title: [NODE-912] 笔试题——实现接口级灰度数据回填（灰度期数据规范化）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-912：手写数据回填

**需求与边界**：
- 需求：灰度数据回填（SCN-OPS-832/331）——① 灰度期数据识别（灰度标记关联——SCN-NODE-670）；② 规范化回填（新格式 → 统一格式——SCN-OPS-331 expand）；③ 回填幂等（idemKey——SCN-NODE-655）；④ 回填的完成度对账（SCN-OPS-331）。
- 边界：① 回填的批量限速（SCN-OPS-331 小事务）；② 回填失败的重试（SCN-NODE-733）；③ 回填的审计（SCN-OPS-220）。

**答**：
```javascript
async function backfillGrayData(grayTag) {
  const rows = await db.query(`SELECT * FROM t WHERE gray_tag = $1 AND normalized = false`, [grayTag]);   // 灰度标记（SCN-NODE-670）
  for (const batch of chunk(rows, 500)) {
    await db.transaction(async (tx) => {
      for (const r of batch)
        await tx.query(`UPDATE t SET normalized_data = $1, normalized = true
          WHERE id = $2 AND normalized = false`, [normalize(r), r.id]);   // 幂等条件更新（SCN-NODE-655）
    });
    await sleep(100);                                  // 限速（SCN-OPS-331）
  }
  const remaining = await countUnnormalized(grayTag);  // 对账（SCN-OPS-331）
  audit({ tag: grayTag, total: rows.length, remaining });
  return { remaining };
}
```

**评分点**:
- 灰度标记识别（SCN-NODE-670）。
- 幂等条件更新（normalized=false 守卫——SCN-NODE-655）。
- 分批限速（SCN-OPS-331）。
- 完成度对账 + 审计（SCN-OPS-331/220）。
