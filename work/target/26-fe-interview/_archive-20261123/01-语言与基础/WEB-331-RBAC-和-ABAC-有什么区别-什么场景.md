---
title: [WEB-331] RBAC 和 ABAC 有什么区别？什么场景必须上 ABAC？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-331：RBAC 和 ABAC 有什么区别？什么场景必须上 ABAC？
**答**：
- RBAC 看角色（你是经理就能批单）；ABAC 看属性（你只能批金额<5000 且属于你部门的单）。
- ABAC 属性来源：主体属性（职级/部门）、资源属性（金额/密级）、环境属性（时间/IP/设备）。
- 前端表现：ABAC 决策在服务端，前端只能根据返回的"可用操作列表"渲染按钮，自己算权限必然错。

```javascript
// ABAC 决策在服务端
function can(user, order, ctx) {
  return user.dept === order.dept
      && order.amount <= user.approveLimit
      && ctx.hour >= 9 && ctx.hour <= 18;
}
// 前端: 渲染后端返回的 actions: ['view', 'comment'] —— 不含 approve
console.log('ABAC 前端只做展示映射，不做决策');
```
