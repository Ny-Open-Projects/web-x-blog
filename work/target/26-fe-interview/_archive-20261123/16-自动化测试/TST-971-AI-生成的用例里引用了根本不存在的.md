---
title: [TST-971] AI 生成的用例里引用了根本不存在的 API 字段（幻觉），怎么自动识别？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-971：AI 生成的用例里引用了根本不存在的 API 字段（幻觉），怎么自动识别？
**答**：
- 结论：用「静态符号解析」对账——把用例里访问的对象属性/方法与实际代码或 OpenAPI schema 求交集，未命中的即幻觉引用。
- 做法：TS 项目用类型检查器直接报错；JS 项目用 AST 提取 member expression 与真实模块导出比对；接口字段与 OpenAPI 对账。
- 兜底：无法静态判定的（动态拼字符串访问）标记可疑并转人工。
- 追问钩子：AI 用例引用了 res.data.couponAmount，但真实接口只有 couponPrice，静态检查没开，运行时才报 undefined，你怎么提前拦？

```javascript
// 用类型系统拦截幻觉字段（TS）
interface OrderResponse { price: number; couponPrice: number; }
function assertCoupon(res: OrderResponse) {
  // res.data.couponAmount // TS 编译期即报错：属性不存在
  return res.couponPrice;
}
// 运行时对账：用例访问的字段必须存在于 schema
const schemaFields = new Set(['price', 'couponPrice', 'status']);
function checkHallucinatedFields(paths, schema = schemaFields) {
  return paths.filter(p => !schema.has(p.split('.').pop()));
}
console.log(checkHallucinatedFields(['res.price', 'res.couponAmount']));
// ['res.couponAmount'] → 幻觉，打回重生成
```
