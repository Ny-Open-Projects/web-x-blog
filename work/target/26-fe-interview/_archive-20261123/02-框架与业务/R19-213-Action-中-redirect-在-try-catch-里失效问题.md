---
title: [R19-213] 为什么 redirect 写在 try/catch 里会失效？怎么正确处理？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-213：为什么 redirect 写在 try/catch 里会失效？怎么正确处理？
**答**：
- Next 的 redirect 通过 throw 特殊错误对象实现控制流；try/catch 会把它当成普通异常捕获吞掉，跳转丢失。
- 正确写法一：redirect 放在 try/catch 之外（成功分支最后一步）。
- 正确写法二：catch 里检查 `isRedirectError(error)` 重新 throw（框架内部判定，需用官方工具函数）。
- 同类陷阱：notFound() 也是 throw 实现，同样会被误捕。
- 根因总结：「用异常做控制流」的 API 必须了解其实现方式，catch 范围要精确——只 catch 业务操作，不 catch 框架控制流。
```javascript
async function action(fd) {
  let order
  try { order = await createOrder(fd) } catch (e) { return { ok: false, msg: '创建失败' } }
  redirect(`/orders/${order.id}`) // try 外
}
```
