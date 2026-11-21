---
title: [DP-140] 容器-组件-服务三层模式如何落地？和 MVC 什么关系？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-140：容器-组件-服务三层模式如何落地？和 MVC 什么关系？（高频）
**答**：
- 三层：Service 层（数据与业务，DP-133 的 Service/Repository）、Container 层（连接 Service 与视图：取数、状态编排，多为自定义 Hook）、Component 层（纯视图：props in、事件 out）。
- 与 MVC 对应：Service ≈ Model、Container ≈ Controller/Presenter、Component ≈ View；本质都是"关注点分层"，前端以组件树为骨架重新表述。
- 依赖方向：Component 不许 import Service（靠 props）；Container 不写样式；Service 不碰 DOM——违规即分层破坏。

```jsx
// Service 层：纯业务与数据，不碰 React
const orderService = {
  async list(query) { return orderRepo.query(query); },       // 委托仓库（DP-132）
  async cancel(id) { return orderRepo.update(id, { status: 'canceled' }); },
};
// Container 层：自定义 Hook 编排（原 Controller 职责）
function useOrderPage() {
  const [orders, setOrders] = useState([]);
  const load = useCallback(async (q) => setOrders(await orderService.list(q)), []);
  const cancel = useCallback(async (id) => { await orderService.cancel(id); load(lastQuery.current); }, [load]);
  useEffect(() => { load({ page: 1 }); }, [load]);
  return { orders, cancel, load };                            // 数据 + 动作
}
// Component 层：纯视图，无 import service
function OrderPageView({ orders, onCancel, onLoadMore }) {
  return (
    <ul>
      {orders.map((o) => (
        <li key={o.id}>
          {o.no}
          <button onClick={() => onCancel(o.id)}>取消</button>
        </li>
      ))}
      <button onClick={onLoadMore}>加载更多</button>
    </ul>
  );
}
// 组装：依赖方向 Component ← Container ← Service，单向清晰
export default function OrderPage() {
  const { orders, cancel, load } = useOrderPage();
  return <OrderPageView orders={orders} onCancel={cancel} onLoadMore={() => load(nextPage)} />;
}
```
