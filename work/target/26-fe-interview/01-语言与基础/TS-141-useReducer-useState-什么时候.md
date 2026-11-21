---
title: [TS-141] useReducer/useState 什么时候必须显式标注类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-141：useReducer/useState 什么时候必须显式标注类型？
**答**：
- useState：初值无法表达目标类型时必须显式——空数组推断 never[]、需要字面量联合时初值会被放宽成 string/boolean。
- useReducer：action 定义为可辨识联合，state/action 类型直接从 reducer 函数签名反推，dispatch 全联动。
- 收益：漏字段、错误 type、穷尽性检查全部编译期完成。

```tsx
// useState 显式标注的两个典型时机
const [items, setItems] = useState<Item[]>([]); // 不标注会推断 never[]
const [status, setStatus] = useState<"idle" | "loading">("idle"); // 锁定字面量联合

// useReducer：类型从 reducer 反推
type State = { list: Item[]; loading: boolean };
type Action =
  | { type: "add"; item: Item }
  | { type: "clear" }
  | { type: "loading"; on: boolean };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case "add": return { ...state, list: [...state.list, action.item] };
    case "clear": return { ...state, list: [] };
    case "loading": return { ...state, loading: action.on };
  }
}
const [state, dispatch] = useReducer(reducer, { list: [], loading: false });

// dispatch({ type: "nope" }); // 报错：type 不在联合中
// dispatch({ type: "add" });  // 报错：缺 item 字段
```
