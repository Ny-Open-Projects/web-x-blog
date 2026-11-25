---
title: [919] 业务动作导致的缓存失效怎么事务化封装
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 失效]
type: 面试题
---

## 919：业务动作导致的缓存失效怎么事务化封装

**答**：
- 问题：一个业务动作（改订单）需失效 N 个 Key（列表/详情/统计/积分）——散落在 mutation 回调里漏一个就是「页面数据不一致」事故。
- 事务化封装：invalidators 注册表——按业务事件注册失效集，mutation 成功只发事件，失效逻辑集中一处；新增依赖方只改注册表不改 mutation。
- 顺序与依赖：失效 A 依赖 B 的结果时——失效链异步序（await A 再 B）；无依赖并行 Promise.all。
- 追问钩子：为什么不用「失效全部」图省事？——失效全部 = 全站请求风暴，大型应用必须精确失效；事务化封装是精确失效的工程化保障。

```ts
// 集中注册失效事务
const invalidators = {
  'order.updated': (qc, evt) => Promise.all([
    qc.invalidateQueries({ queryKey: orderKeys.detail(evt.id) }),
    qc.invalidateQueries({ queryKey: orderKeys.lists() }),
  ]),
  'order.paid': async (qc, evt) => {
    await qc.invalidateQueries({ queryKey: orderKeys.detail(evt.id) }); // 先订单
    await qc.invalidateQueries({ queryKey: ['stats'] });                // 后统计
  },
};
useMutation({ mutationFn: updateOrder,
  onSuccess: (d, v) => invalidators['order.updated'](qc, d) });
```

