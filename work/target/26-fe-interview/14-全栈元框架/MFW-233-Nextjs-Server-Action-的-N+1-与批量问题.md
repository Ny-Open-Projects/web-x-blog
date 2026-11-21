---
title: [MFW-233] Server Action 的隐藏 N+1 与批量治理
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-233：Server Action 的隐藏 N+1

**答**:
- 场景一：表单逐字段调 Action（10 个字段 10 次 RPC）——合并为单 Action 批量载荷（validator 用 object schema 一次收全）
- 场景二：Action 内循环 await DB（for + await 单条更新）→ 事务批量（prisma.$transaction/updateMany）——Action 是黑盒 RPC，内部 N+1 用户无感但延迟线性涨
- 场景三：列表页每行一个删除按钮各自 Action——改为批量选中一次提交（UI 语义同步改）
- 监控：Action 层打点（次数/耗时/内部 DB 查询计数）——N+1 在黑盒里最隐蔽，必须可观测

```javascript
// ❌ 逐字段
for (const f of fields) await updateField(id, f)          // N 次 RPC + N 次查询
// ✅ 单 Action 批量 + 事务
const save = createServerFn().validator(z.array(fieldSchema))
  .handler(({ data) => prnisma.$transaction(
    data.map((f) => prisma.field.update({ where: { id: f.id }, data: f }))))
```
