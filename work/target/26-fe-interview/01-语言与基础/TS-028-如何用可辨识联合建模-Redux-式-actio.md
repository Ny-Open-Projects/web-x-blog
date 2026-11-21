---
title: [TS-028] 如何用可辨识联合建模 Redux 式 action？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-028：如何用可辨识联合建模 Redux 式 action？
**答**：
- 每种 action 一个类型，type 字段做辨识标签，payload 结构各不相同。
- reducer 里 switch type 即可拿到精确的 payload 类型，不需要断言。
- 新增 action 时配合 never 穷尽检查，漏处理直接编译报错。
- 比单一 action 接口 + 可选 payload 的写法安全得多。

```typescript
type Action =
  | { type: "increment"; step: number }
  | { type: "decrement"; step: number }
  | { type: "reset" };

interface State {
  count: number;
}

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case "increment":
      return { count: state.count + action.step }; // action 收窄，step 类型精确
    case "decrement":
      return { count: state.count - action.step };
    case "reset":
      return { count: 0 };
    default: {
      const _check: never = action; // 穷尽检查
      return state;
    }
  }
}
```
