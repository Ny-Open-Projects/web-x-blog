---
title: [WEB-173] Sources 面板支持哪些断点类型？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-173：Sources 面板支持哪些断点类型？
**答**：
- 行断点之外五类：条件断点（表达式为真才停）、日志点 Logpoint（不暂停只打印）、DOM 断点（子树/属性修改时停）、事件监听断点（click/mouseover 一律暂停）、XHR/fetch 断点（URL 含关键字时停）。
- 黑盒脚本（Blackbox）：调试时跳过第三方库内部堆栈，聚焦业务代码。
- 暂停后用 Call Stack 回溯来源、Scope 面板看闭包值；debugger 语句等价行断点。
- 条件断点在热路径里慎用——每次命中都要求值，会明显拖慢执行。

```javascript
// 条件断点：行断点上右键 Add conditional breakpoint，输入表达式
//    cart.items.length > 100        // 只在购物车超 100 件时暂停
// 日志点：Add logpoint，输入
//    'add-to-cart', cart.items.at(-1).id   // 不暂停，仅打印每次加入的商品 id
// XHR/fetch 断点：面板输入关键字 checkout，任何匹配 URL 的请求发出前暂停
async function addToCart(item) {
  const cart = await api.get('/cart');
  cart.items.push(item);
  return api.post('/cart', cart);   // 在这一行设条件断点或日志点观察 cart 内容
}
```
