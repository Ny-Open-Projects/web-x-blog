---
title: [DP-118] 如何沉淀自定义 Hook 模式库？useReducer 复杂状态与 useMemo 派生的标准写法？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-118：如何沉淀自定义 Hook 模式库？useReducer 复杂状态与 useMemo 派生的标准写法？（高频）
**答**：
- Hook 模式库三条设计准则：输入是参数/ref、输出是"状态 + 稳定的动作函数"（用 useCallback/useMemo 包住）、内部封装订阅清理（DP-073）。
- 复杂状态选 useReducer：把状态转移收敛成 reducer 纯函数（状态模式思想的 Hook 化，DP-052），action 命名即领域语言。
- 派生数据选 useMemo：把"过滤/排序/统计"做成派生 selector，避免冗余 state（同一份数据存两遍必然漂移）。

```jsx
// 模式1：useReducer 承载复杂业务状态（转移规则集中、可测试）
const cartReducer = (state, action) => {
  switch (action.type) {
    case 'add': {
      const item = state.items.find((i) => i.id === action.sku);
      return item
        ? { ...state, items: state.items.map((i) => i.id === action.sku ? { ...i, qty: i.qty + 1 } : i) }
        : { ...state, items: [...state.items, { id: action.sku, qty: 1 }] };
    }
    case 'clear': return { ...state, items: [] };
    default: return state;
  }
};
function useCart() {
  const [state, dispatch] = useReducer(cartReducer, { items: [] });
  const actions = useMemo(() => ({                       // 动作引用稳定，下游 memo 不失效
    add: (sku) => dispatch({ type: 'add', sku }),
    clear: () => dispatch({ type: 'clear' }),
  }), []);
  return { items: state.items, ...actions };
}
// 模式2：useMemo 派生数据，绝不复制 state
function useCartSummary(items, { keyword, sortKey }) {
  const filtered = useMemo(() => items.filter((i) => i.name.includes(keyword)), [items, keyword]);
  const sorted = useMemo(() => [...filtered].sort((a, b) => a[sortKey] - b[sortKey]), [filtered, sortKey]);
  const total = useMemo(() => sorted.reduce((s, i) => s + i.price * i.qty, 0), [sorted]);
  return { list: sorted, total };                        // total 由 items 推导，永不与明细不一致
}
```
