---
title: "题 4.3.3：Spring MVC 一个请求的处理流程？@Controller 是线程安全的吗？"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 面试题, 进阶题, 33]
type: 面试题
disableNunjucks: true
---

### 题 4.3.3：Spring MVC 一个请求的处理流程？@Controller 是线程安全的吗？

**【参考回答（可背）】**
DispatcherServlet 前端控制器统一入口：
1. HandlerMapping 找 Handler（HandlerExecutionChain：Handler + 拦截器链）；
2. HandlerAdapter 适配执行（RequestMappingHandlerAdapter）；
3. 参数解析（HandlerMethodArgumentResolver）→ 调 Controller 方法 → 返回值处理（ReturnValueHandler：@ResponseBody 走 HttpMessageConverter 序列化）；
4. 拦截器 postHandle → 视图渲染（前后端分离时代多为直接写响应）→ afterCompletion（清理，异常也保证执行）。

线程安全：Controller 是 **singleton**，多线程共享——**无状态才安全**。可变成员变量会导致串数据（经典事故：把请求统计计数器写成 Controller 字段）。需要状态用 ThreadLocal（请求级）或外部存储。

**【追问链】**
1. 全局异常处理？→ @RestControllerAdvice + @ExceptionHandler 统一兜底；错误响应契约（code/message/traceId）团队统一。
2. 拦截器和 Filter 区别？→ Filter 是 Servlet 规范（容器级，执行更早，如编码/CORS）；拦截器是 Spring（能拿 Handler 元数据、依赖注入）；鉴权在 Filter，业务前置校验在拦截器。

**【P10 加分项】**
讲 Web 层演进判断：Servlet 同步模型（Tomcat 线程池 200）→ 异步 Servlet/WebFlux（少量 EventLoop 线程）→ 虚拟线程（同步写法获得异步吞吐）。选型结论：普通业务保持同步+虚拟线程；高 IO 聚合型（网关/BFF）考虑响应式——给出判断依据而不是炫技。

---
