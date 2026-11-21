---
title: "[话术SP-066] Boot·拦截器（web）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## Boot · 拦截器（web）—— 7 类问法与标准话术

**Qspring-456（概念考察·P1-P3）**
【面试官】请谈谈你对「Boot」中「拦截器」的理解。
【标准回答话术】HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。背后的原理是：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）。
【评分点】① 准确说出核心机制（拦截器）；② 能带出原理层而非背结论。 ③ 版本锚点：Spring MVC 文档

---

**Qspring-457（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「拦截器比 Filter 更早执行」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。原因是：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（Spring MVC 文档）。

---

**Qspring-458（原理深挖·P5-P7）**
【面试官】「拦截器」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）。落到结论：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。
【评分点】① 讲出web层面的机制；② 结论与机制对应不脱节。

---

**Qspring-459（工程落地·P7-P9）**
【面试官】在你带过的项目里，「拦截器」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：登录态/幂等/审计用拦截器，编码/全链路 header 用 Filter。事实依据：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理常见误区要规避：拦截器比 Filter 更早执行。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-460（结论依据·P8-P10）**
【面试官】关于「拦截器」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：Spring MVC 文档。事实与结论：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qspring-461（边界追问·P6-P9）**
【面试官】「拦截器」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「拦截器比 Filter 更早执行」是常见误区。正确的边界：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。使用要点：登录态/幂等/审计用拦截器，编码/全链路 header 用 Filter。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-462（追问链·P5-P8）**
【面试官】追问：如果有人按「Filter 能访问 HandlerMethod」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。原理：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
