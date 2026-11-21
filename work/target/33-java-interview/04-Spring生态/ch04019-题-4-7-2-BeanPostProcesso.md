---
title: "题 4.7.2：BeanPostProcessor 有哪些典型应用？写一个会踩什么坑？"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 4.7.2：BeanPostProcessor 有哪些典型应用？写一个会踩什么坑？

**【参考回答（可背）】** 典型应用四类：① AOP 代理生成（AbstractAutoProxyCreator）；② @Autowired/@Value 解析（AutowiredAnnotationBeanPostProcessor）；③ 参数校验与审计埋点（自定义 BPP 包装 Bean 为代理）；④ 延迟初始化/占位符处理。写自定义 BPP 的坑：① BPP 本身也是 Bean，**启动极早**——构造器里别依赖其他业务 Bean（会拉长依赖链甚至循环）；② returnBean 为 null 会直接"吞掉" Bean（框架内 BPP 的高级用法，业务慎用）；③ 判断别过度：每个 Bean 都会被 BPP 处理，逻辑必须便宜（缓存元数据、精确 instanceof）。
**【追问链】** ① BPP 与 BeanFactoryPostProcessor 的执行顺序？（BFPP 在所有 Bean 实例化前改 BeanDefinition；BPP 逐 Bean 干预实例过程；PropertySourcesPlaceholderConfigurer 是 BFPP）② 为什么 @PostConstruct 不会被代理拦住？（InitDestroyAnnotationBeanPostProcessor 在初始化阶段反射调用，绕过代理链）。
**【P10 加分项】** "BPP 是 Spring 的'字节码级扩展点'——公司基础库用它统一给所有 Service 织入 traceId 日志与慢调用采样，业务方零侵入接入。这就是框架团队和业务团队的能力分水岭。"
