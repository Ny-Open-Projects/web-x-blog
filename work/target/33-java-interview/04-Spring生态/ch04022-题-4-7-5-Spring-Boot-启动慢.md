---
title: "题 4.7.5：Spring Boot 启动慢，怎么优化？（从分钟级到秒级）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 4.7.5：Spring Boot 启动慢，怎么优化？（从分钟级到秒级）

**【参考回答（可背）】** 按代价从低到高：① **测量先行**：--debug 看 ConditionEvaluationReport + 启动端点（ApplicationStartup/StartupStep）定位耗时 Bean；② **懒加载**：spring.main.lazy-initialization=true（注意首次请求 RT 变长，需配预热）；③ **组件瘦身**：排查无用的自动配置与组件扫描范围（@ComponentScan 收敛包路径）；④ **类加载优化**：CDS/AppCDS 共享类存档；⑤ **AOT**：Boot 3 的 spring.aot.enabled 编译期固化 Bean 定义，免运行时反射（GraalVM Native 启动毫秒级）；⑥ **部署侧**：大单体拆微服务/分层镜像预热。
**【追问链】** ① 懒加载有什么坑？（配置错误/装配失败延迟到运行时才暴露，监控与预热必须跟上）② 为什么扫描包越小启动越快？（ClassPath 扫描读字节码+条件评估，BeanDefinition 数量线性影响）。
**【P10 加分项】** 给量化叙事："我们的 800+ Bean 单体通过'懒加载+CDS+扫描收敛'从 42s 降到 15s，AOT 试验后 8s——但结论是'启动优化是为扩容和发布提速服务'，非核心服务不值得投入，先按发布频率和弹性需求排序。"
