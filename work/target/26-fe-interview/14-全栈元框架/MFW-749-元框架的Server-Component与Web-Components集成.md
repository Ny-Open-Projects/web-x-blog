---
title: [MFW-749] RSC 与 Web Components 集成
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-749：RSC 与 Web Components 集成

**答**:
- RSC 中使用 Web Components：1) **server 渲染 WC**（WC 的 HTML 直接在 server 渲染（<my-button> 标签——WC 的 shadow DOM 在 server 渲染（Declarative Shadow DOM RBL-WCN 目录）；2) client 引用 WC（client 组件 import WC 的 JS（自定义元素注册——client 侧注册 RBL-WCN 目录）；3) **WC 的框架无关优势**（RSC 中 WC 不需要 'use client'（WC 是自定义元素——React 的 JSX 支持（React 19 原生支持 WC RBL-WCN 目录）；「WC 在 RSC 中 = server 可渲染 + client 可增强」。
- 集成的模式：1) **server 渲染 WC 标签**（RSC 输出 <my-card> 标签——DSD 的 shadow template 内联 RBL-WCN 目录的 declarative shadow DOM）；2) client 增量增强（WC 的 JS chunk 加载 → 交互增强——WC 的自定义元素注册在 client；3) props 传递（WC 的 attribute/property——React 19 的 WC 支持（attribute 传 string/property 传 object）。
- 追问钩子：为什么「WC 在 RSC 中不需要 'use client'」是独特优势？——'use client' = React 组件的 client 标注（需要 React runtime）；WC = 原生自定义元素（浏览器原生——无需框架 runtime）；WC 在 server 渲染 HTML（DSD——shadow 在 server 内联）+ client 按需注册（无需 React 水合）——「WC 的框架无关性」让它在 RSC 中天然跨边界（server 渲染 HTML + client 增强交互——不需要框架的边界标注）。

```tsx
// RSC 中渲染 WC（server 侧）
export default async function Page() {
  const product = await getProduct(id);
  return (
    <my-card name={product.name} price={product.price}>  {/* WC：server 渲染标签 */}
      <span slot="description">{product.description}</span>
      <my-button slot="actions" variant="primary">Buy</my-button>
    </my-card>
  );
}
// WC 的 DSD（Declarative Shadow DOM——server 渲染 shadow）
// <my-card name="x"><template shadowrootmode="open">
//   <style>:host { ... }</style><slot name="description"></slot>
// </template></my-card>
// client 增量注册（WC 的 JS——client 侧）
// if (!customElements.get('my-card')) {
//   await import('./my-card.js');                        // 按需注册
//   customElements.define('my-card', MyCard);
// }
// React 19 的 WC 原生支持：props → attribute/property 自动映射
// <my-card name="x" />  → attr name="x"；对象 → property 赋值
```
