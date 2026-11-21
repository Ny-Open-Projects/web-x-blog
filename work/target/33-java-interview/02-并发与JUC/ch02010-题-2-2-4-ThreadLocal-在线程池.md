---
title: "题 2.2.4：ThreadLocal 在线程池里为什么会\"串数据\"？怎么系统性解决？"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 2.2.4：ThreadLocal 在线程池里为什么会"串数据"？怎么系统性解决？

**【参考回答（可背）】**
线程池线程复用，上一个请求 set 的 ThreadLocal 值没清理，下一个请求读到旧值（比如用户 A 的身份信息串到用户 B）。
解决三层：
1. 业务层：finally 里 remove()（治标，靠自觉）；
2. 框架层：拦截器/Filter 统一 set 与 remove（Spring 的 RequestContextHolder 就是 Tomcat 每请求处理完后清理）;
3. 线程池层：装饰任务——阿里 TransmittableThreadLocal（TTL），提交时捕获快照、执行前回放、执行后恢复，同时解决"上下文跨线程池传递"。

**【P10 加分项】**
引申到"并发上下文传递"这个工程主题：traceId 跨 N 个线程池的传递、日志 MDC 与 ThreadLocal 的关系、虚拟线程（JDK21）下 ThreadLocal 的成本变化（百万虚拟线程每个都带 map 不划算，官方推荐 ScopedValue）——这一条链答完基本封顶。

---
