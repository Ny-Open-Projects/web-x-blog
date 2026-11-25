---
title: [DP-142] 布局组件如何体现组合模式？children 与 slot 各适合什么？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-142：布局组件如何体现组合模式？children 与 slot 各适合什么？（高频）
**答**：
- 布局组件 = 组合模式的结构节点：Layout 不管"装什么"，只管"怎么摆"（栅格、间距、层级），内容通过 children/slot 注入，结构与内容解耦（DP-037）。
- children 适合单一内容流；多插槽（Card 的 header/body/footer）用子组件约定或具名 props（element 传 VNode/JSX），React 亦可用 context 注入。
- 收益：页面不再写裸 div 拼样式，布局规则集中可换肤、可响应式；嵌套布局天然递归（组合模式自相似）。

```jsx
// React：多插槽布局 = 组合组件（结构组件 + 约定子组件）
function PageLayout({ sidebar, children }) {
  return (
    <div className="page">
      <aside className="page-sidebar">{sidebar}</aside>
      <main className="page-main">
        <header className="page-header">{extractSlot(children, Header)}</header>
        <section className="page-body">{stripSlot(children, Header)}</section>
      </main>
    </div>
  );
}
PageLayout.Header = ({ children }) => children;               // 声明用子组件，由 Layout 决定摆位
// 使用：内容自己声明"是什么"，布局决定"放哪里"
<PageLayout sidebar={<Nav />}>
  <PageLayout.Header><h1>订单中心</h1></PageLayout.Header>
  <OrderTable />
</PageLayout>
// Vue：具名插槽同构
// <PageLayout><template #sidebar><Nav /></template><template #header><h1>订单中心</h1></template>...</PageLayout>
```
