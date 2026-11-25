---
title: [MFW-050] Next.js 这类元框架和 Vite SPA 在架构上的本质差异是什么？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-050：Next.js 这类元框架和 Vite SPA 在架构上的本质差异是什么？
**答**：
- 本质差异一句话：**元框架把「渲染发生的位置」变成可编程决策**（每页/每组件可选静态、SSR、边缘、客户端），SPA 只有一种模式——浏览器渲染一切。
- 数据层差异：SPA 绕不开「先出壳再 fetch 再渲染」两段式；元框架服务端取数直达（RSC/SSR），省一次网络往返、SEO 开箱即用。
- 路由与代码组织：元框架的文件约定路由天然支持嵌套布局/错误边界/流式；SPA 手工组装。
- 后端能力：元框架自带服务端运行时（Route Handler/Server Action/Middleware），全栈闭环；SPA 需要另起 BFF。
- 何时仍选 Vite SPA：纯后台管理（登录后使用、无 SEO 需求、交互极重）、强依赖本地能力（桌面端壳）、部署只能静态托管。

```jsx
// 同一个商品列表的两种实现对比

// ===== Next.js（元框架）：服务端取数直达 =====
// app/products/page.tsx
export default async function Page() {
  const items = await db.product.findMany(); // 1 次往返：服务端 -> DB
  return <List items={items} />;             // 首屏 HTML 已含数据，SEO 完整
}

// ===== Vite SPA：两段式 =====
// src/pages/Products.jsx
function Products() {
  const [items, setItems] = useState(null);
  useEffect(() => {
    fetch('/api/products')                    // 第 2 段：浏览器 -> API -> DB
      .then((r) => r.json())
      .then(setItems);                        // 白屏/loading 后才有内容
  }, []);
  if (!items) return <Spinner />;             // SEO 爬虫只看到 Spinner
  return <List items={items} />;
}
```
