---
title: [TS-183] exactOptionalPropertyTypes 解决什么"三态"问题？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-183：exactOptionalPropertyTypes 解决什么"三态"问题？
**答**：
- 开启后可选属性区分三态：缺席、有值、显式 undefined；`{ title: undefined }` 不再能赋给 `title?: string`。
- 之前 `title?: string` 实际是 `string | undefined`，"没填"与"填了 undefined"在类型上不可区分。
- 真要允许显式 undefined 的接口显式写 `title?: string | undefined`，意图进入类型签名。

```typescript
// exactOptionalPropertyTypes: true
interface Card { title?: string }

const a: Card = {};                  // ✅ 缺席
const b: Card = { title: "hi" };     // ✅ 有值
// const c: Card = { title: undefined }; // ❌ 报错：undefined 不能赋给 string

// 有意区分三态的接口这样写：
type ApiCard = { title?: string | undefined };
const d: ApiCard = { title: undefined }; // ✅ 显式允许

function render(card: Card) {
  if ("title" in card) {
    // 开启该选项后，"in 判断缺席/传值"才真实可靠（传进来的一定不是显式 undefined）
    console.log(card.title);
  }
}
```
