---
title: [TST-932] 微前端跨应用事件的 schema 版本如何演进而不互相踩踏？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-932：微前端跨应用事件的 schema 版本如何演进而不互相踩踏？
**答**：
- 结论：事件是「跨应用接口」——事件名带版本后缀或 payload 带 schemaVersion，消费者按版本路由，旧版本并存直到下线。
- 做法：发布方新增字段用可选，删除字段需先标 deprecated 并观察消费方监控为零再删；消费方对未知字段忽略。
- 验证：契约测试覆盖「新旧 payload 各喂一遍」，确保双方都能处理。
- 追问钩子：订单应用发了个 cart.updated 事件，payload 把 itemId 改名 skuId，购物车子应用没改，怎么在灰度前发现？

```javascript
// 事件 schema 版本化
const evtV1 = { type: 'cart.updated', schemaVersion: 1, payload: { itemId: 'i1', qty: 2 } };
const evtV2 = { type: 'cart.updated', schemaVersion: 2, payload: { skuId: 'i1', qty: 2 } };

function handleCartUpdated(evt) {
  const id = evt.schemaVersion >= 2 ? evt.payload.skuId : evt.payload.itemId;
  if (!id) throw new Error('事件契约违约：缺少商品标识');
  return id;
}
// 契约测试：新旧事件都要能处理
test.each([evtV1, evtV2])('兼容 schemaVersion=$schemaVersion', e => {
  expect(handleCartUpdated(e)).toBe('i1');
});
// 发布方：新增字段可选，弃用字段先标记
const evtV3 = { ...evtV2, deprecated_itemId: 'i1', schemaVersion: 3 };
```
