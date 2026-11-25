---
title: [NODE-832] 笔试题——实现灰度回滚的数据验证（回滚后数据可读）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-832：手写回滚验证

**需求与边界**：
- 需求：灰度回滚数据验证（SCN-OPS-277/227）——① canary 期间写入数据识别（灰度标记关联——SCN-NODE-670 标记）；② stable 版本读新数据实测（SCN-OPS-277 三层——读/渲染/逻辑）；③ 不兼容数据修复任务（SCN-OPS-227 善后）；④ 验证通过才完成回滚（SCN-OPS-227 阻塞善后清单）。
- 边界：① 抽样策略（canary 数据量小——全量验证，SCN-NODE-682）；② 验证失败的用户补偿（数据丢失评估——SCN-OPS-227）；③ 验证结果回填兼容声明（SCN-OPS-793）。

**答**：
```javascript
async function verifyRollbackData(canaryWrites, stable) {
  const results = [];
  for (const d of canaryWrites) {                      // canary 写入全量（量小——SCN-NODE-682）
    const read = await stable.read(d);                 // stable 读实测（SCN-OPS-277）
    if (!read.ok) { results.push({ id: d.id, failure: 'READ' }); continue; }
    const render = await stable.render(read);          // 渲染层
    if (!render.ok) { results.push({ id: d.id, failure: 'RENDER' }); continue; }
    const logic = await stable.businessLogic(read);    // 业务逻辑
    if (!logic.ok) results.push({ id: d.id, failure: 'LOGIC', detail: logic.err });
  }
  if (results.length) {
    await scheduleRepair(results);                     // 修复任务（SCN-OPS-227 善后）
    assessCompensation(results);                       // 用户补偿评估（SCN-OPS-227）
    blockReleaseCompletion();                          // 阻塞善后清单完成（SCN-OPS-227）
  }
  return { verified: results.length === 0, failures: results };
}
```

**评分点**:
- 三层实测（读/渲染/逻辑——SCN-OPS-277）。
- canary 数据全量验证（量小——SCN-NODE-682 抽样策略翻转）。
- 失败修复 + 用户补偿 + 善后阻塞（SCN-OPS-227 五步）。
- 验证结果回填兼容声明（SCN-OPS-793）。
