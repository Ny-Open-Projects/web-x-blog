---
title: "Java 后端面试全景大纲 — 对标阿里 P10（专家/资深技术总监）"
date: 2026-11-18
categories: [Java面试, 课程导览]
tags: [Java面试, 导览, 33]
type: 导览
disableNunjucks: true
---

## Java 后端面试全景大纲 — 对标阿里 P10（专家/资深技术总监）

> 定位：P10 = 阿里技术序列专家级（M5/资深技术专家~技术总监），要求：
> 1) 基础功底扎实到"知其所以然"（能讲清 JDK 源码、JVM 内部实现）；
> 2) 主导过亿级用户/十万级 QPS 以上系统的架构设计与落地；
> 3) 对技术趋势（云原生、AI/Agent）有判断力，能做技术选型与团队技术布道。
>
> 使用方法：每章按"入门考察 → 进阶深挖 → P10 级压轴题"三层递进，
> 每题给出【面试官意图】【参考回答】【追问链】【P10 加分项】。

### 篇章结构（10 章 + 附录）

#### 第 1 章 Java 语言基础与集合
- 语言核心：final/不可变、String 与字符串常量池、==/equals/hashCode 契约
- 泛型：类型擦除、通配符 PECS、super/extends 边界
- 集合源码级剖析：ArrayList/LinkedList、HashMap（1.7→1.8 演进、扩容、树化）、
  ConcurrentHashMap（1.8 CAS+synchronized、size 统计）、LinkedHashMap/LRU
- 枚举、内部类、Object 方法体系、Comparable/Comparator

#### 第 2 章 并发编程与 JUC
- Java 内存模型：happens-before、volatile/MESI、内存屏障
- synchronized 锁升级、AQS 源码（CLH 队列、独占/共享模式）
- 线程池：核心参数、执行流程、拒绝策略、参数动态化实践
- 并发容器、ThreadLocal（内存泄漏）、CompletableFuture
- 无锁化：CAS/Atomic、LongAdder 原理、伪共享 @Contended

#### 第 3 章 JVM 与性能调优
- 运行时内存区域、对象创建/布局/OOP-Klass、逃逸分析
- 类加载机制与双亲委派（打破场景：SPI/Tomcat/热部署）
- GC 算法与收集器：CMS/G1/ZGC 对比、三色标记与读写屏障
- 调优实战：GC 日志分析、常见 OOM 排查、Arthas/jprofiler 实战
- GraalVM/AOT、JIT（C1/C2、分层编译、方法内联）

#### 第 4 章 Spring 与主流框架生态
- IoC 容器启动流程、Bean 生命周期、三级缓存与循环依赖
- AOP：动态代理（JDK/CGLIB）、切面失效场景
- 事务：传播机制、失效场景、分布式事务衔接
- Spring Boot 自动装配原理、Spring Boot 3/AOT、Spring Cloud 组件
- MyBatis 执行流程、插件机制

#### 第 5 章 MySQL 与存储
- InnoDB 体系结构：BufferPool、ChangeBuffer、双 LRU
- 索引：B+ 树、聚簇/回表/覆盖索引、索引下推、最左前缀
- 事务与 MVCC：ReadView、快照读/当前读、间隙锁与幻读
- 日志体系：redo/undo/binlog、两阶段提交、组提交
- 高可用：主从复制、半同步、MGR；分库分表与 ShardingSphere

#### 第 6 章 Redis 与缓存体系
- 数据结构底层：SDS、跳表、quicklist/listpack、字典渐进式 rehash
- 持久化：RDB/AOF/混合持久化、主从复制原理（repl_backlog）
- 高性能原理：单线程→多线程 IO、IO 多路复用
- 缓存三大问题：穿透/击穿/雪崩，缓存一致性方案矩阵
- 分布式锁（Redisson/RedLock 争议）、集群与数据分片

#### 第 7 章 消息队列与异步化
- Kafka：架构、ISR 机制、 Exactly-Once、顺序性、性能 zero-copy
- RocketMQ：事务消息、延迟消息、消息轨迹
- 消息不丢不重：发送/存储/消费三端保障、幂等设计
- 削峰填谷、异步解耦的架构实践与反模式

#### 第 8 章 分布式理论与微服务架构
- CAP/BASE/Paxos/Raft/ZAB 一致性协议
- 分布式事务：2PC/3PC/TCC/SAGA/本地消息表/最大努力通知
- 注册中心/配置中心：Nacos(AP/CP 切换)、服务网格 Istio
- 网关、限流（令牌桶/漏桶/滑动窗口/Sentinel 源码）、熔断降级
- 分布式 ID、时钟问题、全链路压测、可观测性（Metrics/Tracing/Logging）

#### 第 9 章 亿级高并发系统设计与真实场景题
- 性能方法论：RT/QPS/吞吐估算、压测模型、容量规划
- 高并发三板斧：缓存/限流/降级 + 异步化/池化/批量化
- 秒杀系统：库存超卖、队列削峰、热点 key、链接防刷
- 读写分离/分库分表/冷热分离/多级缓存（本地+分布式）
- 场景设计题：短链系统、Feed 流、抢红包、排行榜、IM 系统

#### 第 10 章 AI 时代：LLM、Agent 与 AI 应用架构
- LLM 基础：Transformer/Attention、Token/上下文窗口、推理优化（KV Cache、量化、vLLM）
- RAG：Embedding、向量数据库、Chunking 策略、重排与评估
- Agent 架构：ReAct/Function Calling/Planning/Memory/MCP 协议
- 多 Agent 协作、LangChain/Spring AI/Dify 技术选型
- AI 应用工程化：幻觉治理、成本控制、Prompt 管理、评测体系
- Java 工程师的 AI 转型路径：AI 网关、Agent 编排平台、传统系统 AI 化改造

### 附录
- A. P10 级"软实力"题：技术战略、团队管理、跨部门协作、技术决策复盘
- B. 简历与项目包装方法论（STAR 法则、量化指标）
- C. 高频"反问面试官"问题清单
- D. 30/60/90 天备考计划

### 每章统一结构模板
1. 考察范围雷达（面试官视角）
2. 入门题（P4-P6 必答对）
3. 进阶题（P7-P8 深挖链）
4. 压轴题（P9-P10：架构权衡、源码细节、踩坑复盘）
5. 本章高频追问链图谱
6. 参考资料与延伸阅读
