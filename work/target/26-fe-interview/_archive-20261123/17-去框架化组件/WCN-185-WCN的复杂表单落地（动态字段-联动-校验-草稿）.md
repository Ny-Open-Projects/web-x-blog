---
title: [WCN-185] WCN 的复杂表单落地：动态字段、联动、校验与草稿恢复的完整方案？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-185：WCN 的复杂表单落地：动态字段、联动、校验与草稿恢复

**答**：
- 状态层：表单数据 store（Signals）+ 字段 schema（JSON 驱动，WCN-119 生成器）；字段级 signal/computed 保证细粒度校验与联动。
- 动态字段：schema 由服务端下发（规则引擎），渲染器按 schema 增删字段块（keyed）；字段值按路径存 store（`store.set('a.b.c')`）。
- 联动：跨字段规则（A>0 时 B 必填）在 computed 层声明（WCN-080），规则本身也是 schema 的一部分——运营可配。
- 校验：即时（input 时字段级）+ 提交时全量；异步校验（查重）走防抖 resource；错误信息本地化。
- 草稿恢复：store → persist 中间件（WCN-083，节流写 localStorage）；恢复时 schema 版本比对，字段缺失/类型变更的迁移策略（忽略或转换）。
- 提交：原子事务——全量校验通过 → 构造 payload 快照 → 提交；失败保留草稿并标记错误块滚动定位。

```javascript
// 联动规则 schema 化
const rules = [
  { when: { field: 'refund.amount', op: '>', value: 0 },
    require: 'refund.reason', message: '退款金额大于 0 必须填写原因' },
];
// 编译为 computed：canSubmit = computed(() => rules.every((r) => satisfied(r)));
```
