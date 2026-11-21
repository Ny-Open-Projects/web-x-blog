---
title: "题 2.3.3：CompletableFuture 怎么用？怎么处理异常？怎么并行调用多个服务？"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 面试题, 进阶题, 33]
type: 面试题
disableNunjucks: true
---

### 题 2.3.3：CompletableFuture 怎么用？怎么处理异常？怎么并行调用多个服务？

**【参考回答（可背）】**
- 创建：supplyAsync（有返回）/ runAsync；默认用 ForkJoinPool.commonPool()——**生产必须传自定义线程池**（commonPool 是 JVM 全局共享，一个慢任务拖垮所有并行流和 CompletableFuture）。
- 编排：thenApply（转换）/ thenCompose（扁平化，避免 CF<CF<T>>）/ thenCombine（合并两个）/ allOf/anyOf（聚合）。
- 异步回调默认在哪个线程？→ 不指定 executor 时：前一步完成的线程执行（若已完成则当前线程）。
- 异常：exceptionally / handle（都处理）/ whenComplete（只看不动结果）；异常沿链传播，中断后续非异常回调。
- 典型场景（背模板）：详情页并行调 商品/价格/库存/营销 四个服务，allOf 聚合，超时用 orTimeout（JDK9）或 completeOnTimeout。

**【追问链】**
1. thenApply 和 thenApplyAsync 区别？→ Async 版本强制丢给 executor 新线程执行。
2. 上下文丢失问题？→ 异步化后 ThreadLocal（登录态/traceId）丢失：用 TTL 装饰 executor，或阿里开源的 transmittable-thread-local。
3. allOf 拿结果麻烦怎么办？→ 封装工具类收集 List<CompletableFuture> 再 join 转泛型列表（手写一段能力是加分项）。

**【P10 加分项】**
讲"全链路异步化"架构：Tomcat 请求线程（Servlet 异步/DeferredResult/WebFlux）→ 下游调用全异步 → 整个请求线程数从 200 降到个位数，吞吐提升数倍；代价是全链路 ThreadLocal 治理、堆栈可读性、调试难度。有此实践者直接对齐 P10。

---
