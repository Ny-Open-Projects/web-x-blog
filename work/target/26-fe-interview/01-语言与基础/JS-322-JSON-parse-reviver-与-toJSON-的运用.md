---
title: [JS-322] JSON.parse 的 reviver 与 toJSON 的运用
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 序列化]
type: 面试题
---

## JS-322：JSON.parse 的 reviver 与 toJSON

**答**：
- reviver：parse 的第二个参数——按「由内到外」顺序对每个值做后处理（还原 Date、BigInt 字符串化还原）
- toJSON：对象自定义序列化输出——JSON.stringify 时优先调用；Date 内建 toJSON 返回 ISO 字符串
- 组合场景：服务端下发的 Long ID 字符串还原为 BigInt（防精度丢失）；日期字段自动转 Date 实例
- 注意：reviver 返回 undefined 会**删除该键**——用于字段白名单过滤
- toJSON 的返回值再走一遍 stringify（对象继续序列化）

```javascript
// reviver：还原类型
const data = JSON.parse(raw, (key, value) => {
  if (key === 'createdAt') return new Date(value);
  if (key === 'id') return BigInt(value);   // Long 精度
  if (key.startsWith('_')) return undefined; // 内部字段过滤
  return value;
});
// toJSON：自定义输出
class Money {
  constructor(cents) { this.cents = cents; }
  toJSON() { return this.cents / 100; }     // 序列化为元
}
JSON.stringify({ price: new Money(9950) }); // {"price":99.5}
```
