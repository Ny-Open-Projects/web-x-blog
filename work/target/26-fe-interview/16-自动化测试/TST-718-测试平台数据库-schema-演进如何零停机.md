---
title: [TST-718] 测试平台的数据库 schema 演进如何做到零停机测试
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-718：测试平台的数据库 schema 演进如何做到零停机测试

**答**：
- 结论：用「扩展-迁移-收缩」三步法（expand-migrate-contract），先加新字段兼容旧代码，再双写双读，最后才删旧字段。
- 任何时刻新旧版本代码都能跑：新增列必须可空或有默认值，禁止直接改列含义。
- 用影子表/在线 DDL 工具避免锁表，迁移过程用测试平台自己的用例验证数据一致性。
- 追问钩子：迁移中途发现新代码写错数据，如何回滚而不丢数据？

```javascript
// 双写一致性校验：新旧字段值应一致
function verifyDualWrite(rows) {
  const bad = [];
  for (const r of rows) {
    // 迁移期 oldStatus 与 status 应保持一致
    if (r.oldStatus !== undefined && r.oldStatus !== r.status) {
      bad.push({ id: r.id, old: r.oldStatus, now: r.status });
    }
  }
  return { consistent: bad.length === 0, bad };
}
console.log(verifyDualWrite([
  { id: 1, oldStatus: 'pass', status: 'pass' },
  { id: 2, oldStatus: 'pass', status: 'fail' },
]));
```
