---
title: [TS-157] 如何实现元组分块 Chunk？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-157：如何实现元组分块 Chunk？
**答**：
- 双累加器：Cur 攒当前块，攒满 N 时"整体产出"并重新从当前剩余 T 开始，未满而输入耗尽则产出余块。
- 关键易错点：Cur 攒满时消费的是整个 T（含当前 F），而不是继续取 F，否则会漏元素。
- 基线双出口：输入耗尽且 Cur 为空返回 []，否则返回 [Cur]。

```typescript
type Chunk<T extends unknown[], N extends number, Cur extends unknown[] = []> =
  T extends [infer F, ...infer R]
    ? Cur["length"] extends N
      ? [Cur, ...Chunk<T, N>]          // Cur 攒满：整体产出，T 保持不动
      : Chunk<R, N, [...Cur, F]>       // 未满：F 进块，继续消耗
    : Cur extends [] ? [] : [Cur];     // 基线：余块或空

type C1 = Chunk<[1, 2, 3, 4, 5], 2>; // [[1, 2], [3, 4], [5]]
type C2 = Chunk<[1, 2, 3], 3>;       // [[1, 2, 3]]
type C3 = Chunk<[1], 2>;             // [[1]]（不满也产出）
type C4 = Chunk<[], 2>;              // []
```

## 第三十三章 递归类型与性能（TS-158 ~ TS-163）
