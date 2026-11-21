---
title: [BAS-115] 元组和 readonly 数组怎么用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-115：元组和 readonly 数组怎么用？
**答**：
- 元组 `[string, number]` 固定长度、每个位置类型确定，适合返回多个不同类型的值；可命名：`[start: number, end: number]`。
- `readonly number[]` 禁止 push/pop 等修改；函数参数声明为 readonly 数组还能同时兼容元组。
- React 的 useState 返回类型就是元组：`[T, (v: T) => void]`。

```typescript
function useSize(): readonly [width: number, height: number] {
  return [window.innerWidth, window.innerHeight];
}
const [w, h] = useSize();            // 解构出 number
const list: readonly number[] = [1, 2, 3];
// list.push(4);                     // 报错：readonly
const point: [x: number, y: number] = [10, 20];
```
