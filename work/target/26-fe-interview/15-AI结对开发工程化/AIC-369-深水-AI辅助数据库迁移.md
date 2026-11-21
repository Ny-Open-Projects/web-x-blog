---
title: [AIC-369] 前端团队负责的 IndexedDB/本地存储 schema 迁移，AI 如何辅助？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-369：前端团队负责的 IndexedDB/本地存储 schema 迁移，AI 如何辅助？
**答**：
- 迁移设计：AI 生成版本化迁移链（v1→v2→v3），每步可独立执行与回退。
- 数据保全测试：迁移测试必须断言「旧数据完整迁移 + 异常数据（损坏/超预期版本）降级处理」。
- 多标签页并发：迁移期间的并发访问（另一标签页写数据）场景必须覆盖。
- 回滚策略：迁移失败的降级路径（清空重建 vs 中止升级），明确数据损失边界并告知用户。

```javascript
async function migrateIDB(db: IDB, from: number) {
  for (const step of migrations.slice(from)) {
    try { await step.up(db); }
    catch (e) { return fallback(step, e); // 损坏数据降级 + 明确损失边界
    }
  }
}
// 测试必含：旧数据保全 / 并发标签页 / 损坏记录跳过
r
```
