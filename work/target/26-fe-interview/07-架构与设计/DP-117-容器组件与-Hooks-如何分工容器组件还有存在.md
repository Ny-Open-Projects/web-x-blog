---
title: [DP-117] 容器组件与 Hooks 如何分工？容器组件还有存在必要吗？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-117：容器组件与 Hooks 如何分工？容器组件还有存在必要吗？（高频）
**答**：
- Hooks 时代容器/展示的划分没有消失，只是从"组件分层"变成"逻辑分层"：容器层 = 自定义 Hook 集合（取数、状态、订阅），展示层 = 纯函数组件（props in、JSX out）。
- 判断标准：一个组件同时干"取数 + 布局 + 交互样式"就该拆——把数据逻辑提为 `useXxxContainer` Hook，JSX 留给纯展示组件。
- 收益：展示组件可 storybook 单测/截图测试；数据逻辑可跨页面复用；迁 Zustand/Context 时只动 Hook 层。

```jsx
// 逻辑层：容器 Hook（原容器组件的全部职责）
function useOrderListContainer(query) {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    let alive = true;                                    // 防竞态：卸载后不写入
    setLoading(true);
    fetchOrders(query).then((d) => alive && setOrders(d)).finally(() => alive && setLoading(false));
    return () => { alive = false; };
  }, [query.page, query.status]);
  const actions = useMemo(() => ({ refresh: () => setOrders((o) => [...o]) }), []);
  return { orders, loading, actions };                   // 只吐数据与动作
}
// 展示层：纯函数组件，无副作用，props 决定一切
function OrderList({ orders, loading, onRefresh }) {
  if (loading) return <Spin />;
  return (
    <table>
      <tbody>{orders.map((o) => <tr key={o.id}><td>{o.no}</td><td>{o.amount}</td></tr>)}</tbody>
    </table>
  );
}
// 页面 = 组装点：Hook 接数据，展示组件接视图
export default function OrderPage() {
  const [query, setQuery] = useState({ page: 1, status: 'all' });
  const { orders, loading, actions } = useOrderListContainer(query);
  return <OrderList orders={orders} loading={loading} onRefresh={actions.refresh} />;
}
```
