---
title: [MP-007] 小程序与浏览器 SPA 的本质差异有哪些？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-007：小程序与浏览器 SPA 的本质差异有哪些？
**答**：
- **线程模型**：SPA 单线程 JS 直接操作 DOM；小程序双线程，数据驱动，DOM 不可见。
- **路由**：SPA 靠 History API + 前端路由表；小程序由 native 管理页面栈（上限 10），跳转即入栈/退栈，页面是独立 WebView。
- **资源与管控**：SPA 无包体限制、无审核；小程序有 2M 主包/30M 总包限制、域名白名单、审核发布流程。
- **登录态**：SPA 有 Cookie；小程序无 Cookie，用 storage + header 自行携带 token。
- **生命周期**：SPA 是应用级；小程序是 App/Page/Component 三层生命周期。

```javascript
// 同为"跳详情页"的差异对比
// SPA:  router.push('/detail?id=1')，历史记录由浏览器管理
wx.navigateTo({ url: '/pages/detail/detail?id=1' })  // native 页面栈 +1
const stack = getCurrentPages()                       // 页面栈实例数组
console.log(stack.length, stack[stack.length - 1].route) // 深度 与 当前页面路径
```
