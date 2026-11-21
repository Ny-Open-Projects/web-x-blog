---
title: [R19-209] Action 成功后怎么做导航？router.push 与 redirect 的取舍？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-209：Action 成功后怎么做导航？
**答**：
- 服务端 `redirect('/success')`：无 JS 也能导航（渐进增强闭环），action 返回前抛出跳转，客户端自动完成路由切换。
- 客户端 router.push：适合需要根据返回值动态决定目标的场景（如跳到新建订单的详情页），或 action 只返回数据不导航。
- 取舍：导航逻辑「服务端可决定」就 redirect（逻辑内聚在 action），需要客户端上下文（如表单临时状态）才 push。
- 注意 redirect 后 action 的返回值不会到达调用方（跳转优先）；不要在 redirect 后再写代码。
- 细节：redirect 在 try/catch 里会被 catch 误捕（它是 throw 实现），Next 中要放 try 外或重新 throw。
