---
title: [FRP-140] RSC 的渲染模型是什么？服务端组件为什么不进入客户端 bundle？（高频）
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-140：RSC 的渲染模型是什么？服务端组件为什么不进入客户端 bundle？（高频）

**答**：
- 服务端组件是**只在服务器执行的函数**，返回值不是组件实例而是"渲染描述"（RSC payload：序列化的元素树）——客户端拿到的是**结果**，不是可执行代码。
- 打包器据此切分：server 文件里的 import 只参与服务端模块图；客户端构建遇到 server 模块直接跳过——这就是"零 bundle 体积"的原理。
- 因此 server component 可以直接 import db/fs/密钥等"只能在服务端用的东西"，同时不能用 useState/useEffect/浏览器 API（这些代码根本没有机会在客户端跑）。
- 客户端组件以"模块引用"（`$L1` 这类 id 占位）出现在 payload 里，真正的 JS 由客户端 bundle 提供，两者在客户端拼装成完整树。

```javascript
// 简化实现，帮助理解 RSC 渲染与 payload 生成
// —— 服务端模块图 ——
async function renderServerComponent(Component, props) {
  // server component 就是普通 async 函数：渲染期直接取数
  if (Component.__client) {
    // client 组件引用：不执行！只输出引用占位
    return { $$typeof: Symbol.for('react.client.reference'), $$id: Component.__id, props };
  }
  const element = await Component(props);   // server 组件可以 await —— 数据在渲染时获取
  if (element && typeof element.type === 'function') {
    // 递归渲染子 server 组件
    return renderServerComponent(element.type, element.props);
  }
  return element; // 宿主元素（div/h1...）原样序列化
}

// —— RSC payload 片段示意 ——
// [
//   "$",            // 根元素
//   "div",
//   { children: [
//     ["$", "h1", { children: "商品列表" }],          // server 渲染的静态结果
//     ["$L1", { items: 3 }],                        // $L1 = client 组件引用占位
//   ]}
// ]
// ["$L1", ...] 的 JS 本体在客户端 bundle：由打包器单独构建

// —— 打包侧的切分规则 ——
function isClientModule(mod) {
  return mod.source.includes('"use client"') || mod.importedBy.some(isClientModule);
}
// server graph：从页面入口展开，遇到 isClientModule 就停（换成 client reference）
// client graph：从每个 client 模块重新展开，独立打包

// server 组件里的"越界"会直接报错：
// 'useState' cannot be used in a Server Component —— 因为它压根不在客户端执行
```
