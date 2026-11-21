---
title: "[SP-064] Boot·DispatcherServlet（web）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · DispatcherServlet（web）

- **事实**：请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应
- **原理**：所有请求入口统一是 DispatcherServlet（前端控制器模式），理解流程后拦截器/异常/参数解析各就各位
- **常见误区**：
  1. 每个请求先到 Controller（错）
  2. HandlerAdapter 负责路由匹配（错）
  3. 视图解析在 HandlerMapping 之前（错）
- **工程用法**：Spring MVC 八股主线
- **版本锚点**：Spring MVC 文档
