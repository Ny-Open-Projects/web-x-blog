---
title: [ZSM-230] 多中间件下 Zustand 的类型推导为什么会断
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-230：多中间件下 Zustand 的类型推导为什么会断

**答**：
- 断链根因：中间件的泛型签名 `Mutator` 要求「包装后 set 的类型」与「config 期望的 set 类型」对齐，多中间件嵌套时联合类型膨胀，TS 推导到某一层丢信息
- 官方方案：`create<State>()(middleware1(middleware2(fn)))` 的「立即调用双括号」显式注入 State，让推导从锚点重新开始
- persist 的 partialize 返回子集类型也要显式声明（`persist<Bare, [], [], Partial<State>>` 一类参数），否则 options 里全是 unknown
- 经验法则：类型报错时优先检查「是否用了双括号」与「中间件顺序是否与类型参数顺序一致」，而不是加 as

```javascript
type Store = { count: number; inc: () => void }

// ✅ 双括号锚定
export const useStore = create<Store>()(
  devtools(persist((set) => ({
    count: 0,
    inc: () => set((s) => ({ count: s.count + 1 }), undefined, 'inc'),
  }), { name: 'counter' }))
)
// ❌ create(devtools(...)) 不带 State → set 类型为 never/unknown 报错
```
