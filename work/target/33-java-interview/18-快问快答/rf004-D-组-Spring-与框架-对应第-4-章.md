---
title: "D 组：Spring 与框架（对应第 4 章）"
date: 2026-11-18
categories: [Java面试, 快问快答]
tags: [Java面试, 快问快答, 33]
type: 快问快答
disableNunjucks: true
---

## D 组：Spring 与框架（对应第 4 章）

31. **Bean 生命周期一句话？** 实例化→注入→Aware→前置→初始化→后置→使用→销毁；AOP 代理在后置处理生成。
32. **三级缓存第三级为什么必须有？** ObjectFactory 延迟决定"返回原对象还是提前代理"，保证 AOP 语义正确。
33. **AOP 失效根因一句话？** 绕过代理对象直接调用（同类 this 调用、final/private 方法、new 出来的对象）。
34. **事务失效清单？** 非 public、自调用、catch 吞异常、默认只回滚 RuntimeException、传播错配。
35. **REQUIRES_NEW 与 NESTED？** 前者挂起旧事务新建独立事务（双连接），后者保存点同事务、外层回滚内层必回滚。
36. **自动装配机制？** imports 注册文件 + 条件注解（OnClass/OnMissingBean/OnProperty），用户 Bean 优先。
37. **Mapper 接口为什么能注入？** JDK 动态代理 + MapperFactoryBean + ImportBeanDefinitionRegistrar 扫描。
38. **先提交后通知怎么写？** TransactionSynchronization#afterCommit 里发 MQ，保证消费方能读到数据。
39. **构造器注入的好处？** 天然暴露循环依赖（启动即失败）+ 不可变 + 显式依赖，团队规范应强制。
40. **Boot3 关键变化？** JDK17 基线、javax→jakarta、AOT/Native、Micrometer Tracing。
