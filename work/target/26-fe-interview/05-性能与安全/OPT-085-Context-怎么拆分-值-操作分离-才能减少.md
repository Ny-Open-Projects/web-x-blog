---
title: [OPT-085] Context 怎么拆分（值/操作分离）才能减少重渲染？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-085：Context 怎么拆分（值/操作分离）才能减少重渲染？

**答**：
- Context 的重渲染规则：Provider 的 value 引用变化 → **所有消费组件全量重渲**，与是否用到变化的字段无关。
- 拆分两个维度：**按值拆**（theme/user/lang 各自独立 Provider，互不牵连）、**按读写拆**（state 与 dispatch 分开——操作函数引用稳定，值高频变化时只通知读的一方）。
- value 必须记忆化：`useMemo` 包住 value 对象，否则 Provider 每次渲染都产生新引用，consumers 全跟涨。
- 大状态不要全塞一个 context：拆得越细，重渲染面越小；跨页低频状态再考虑 store。

```jsx
// 一一对应：Context 值/操作分离 + 记忆化 value
// 反例：一个 Provider 装所有，任何变化全体消费者重渲
// <AppContext.Provider value={{ user, cart, theme, setTheme, addToCart }}>

// 正解 1：操作与值分家——操作引用永久稳定
const CartStateContext = createContext(null);
const CartDispatchContext = createContext(null);

function CartProvider({ children }) {
  const [cart, setCart] = useState({ items: [], total: 0 });
  // 操作对象只创建一次，引用永不变：消费它的组件永不因 cart 变化而重渲
  const actions = useMemo(
    () => ({
      add: (item) => setCart((c) => ({ ...c, items: [...c.items, item] })),
      clear: () => setCart({ items: [], total: 0 }),
    }),
    []
  );
  return (
    <CartDispatchContext.Provider value={actions}>
      <CartStateContext.Provider value={cart}>
        {children}
      </CartStateContext.Provider>
    </CartDispatchContext.Provider>
  );
}

// 只消费操作的组件（如"清空按钮"），加购时不重渲
function ClearCartButton() {
  const { clear } = useContext(CartDispatchContext);
  return <button onClick={clear}>清空购物车</button>;
}

// 正解 2：按值再拆——theme 高频换肤也不牵连 cart 消费者
// <ThemeProvider>、<CartProvider> 并列，各自独立失效范围
```
