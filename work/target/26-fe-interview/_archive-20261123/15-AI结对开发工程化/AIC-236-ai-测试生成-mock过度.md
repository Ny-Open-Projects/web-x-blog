---
title: [AIC-236] AI 生成的测试经常过度 mock，导致测的全是 mock 逻辑，如何识别与纠正？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-236：AI 生成的测试经常过度 mock，导致测的全是 mock 逻辑，如何识别与纠正？
**答**：
- 识别信号：被测函数的每个依赖都被 mock、断言对象是 mock 调用参数而非业务结果。
- 危害：重构实现后测试全红但真实行为没坏（脆弱），或实现错了测试照过（假阳性）。
- 纠正：优先真实依赖（内存实现/MSW 拦截网络而非 mock fetch 函数），只 mock 边界（网络、时钟、随机）。
- 规则化：mock 数量上限 + 「断言不得引用 mock 自身」检查。

```javascript
// 反例：断言 mock 被调用 = 测试 mock 本身
expect(mockSave).toHaveBeenCalledWith({...}); // 若内部逻辑错但参数对，测试仍绿
// 正例：断言真实结果
const saved = await repo.find(id);
expect(saved.status).toBe('paid');            // 行为正确性
// 原则：mock 只允许在系统边界（http/db/clock），业务内核必须真实执行
r
```
