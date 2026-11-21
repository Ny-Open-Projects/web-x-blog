---
title: "第 4 章 Spring 与框架生态"
date: 2026-11-18
categories: [Java面试, 速记卡]
tags: [Java面试, 速记卡, 33]
type: 速记卡
disableNunjucks: true
---

## 第 4 章 Spring 与框架生态

1. Bean 生命周期口诀：实例化→注入→Aware→前置→初始化→后置→使用→销毁；AOP 代理在后置生成。
2. 三级缓存：成品/半成品/工厂；第三级为 AOP 延迟决定；构造器循环依赖无解。
3. AOP 失效根因一句话：绕过代理。同类自调用是头号坑。
4. 事务失效：非 public、自调用、catch 吞、默认只回滚 RuntimeException、受检异常要 rollbackFor。
5. REQUIRES_NEW 挂起新开（双连接）；NESTED 保存点（同连接）。
6. 自动装配：imports 文件 + 条件注解；@ConditionalOnMissingBean = 用户优先。
7. Mapper 无实现类 = JDK 动态代理 + FactoryBean + ImportBeanDefinitionRegistrar。
8. 先提交后通知：afterCommit 里发 MQ；事件监听默认同步、@TransactionalEventListener(AFTER_COMMIT)。
9. @Async 四坑：默认池不池化、自调用失效、异常静默、上下文丢失（TaskDecorator/TTL）。
10. prototype 注入 singleton：ObjectProvider / @Lookup / scoped proxy 三正解。
11. Boot 启动优化：先测量 → 懒加载 → 扫描收敛 → CDS → AOT。
12. 迁移即治理：老 SpringMVC 迁 Boot 四步渐进，禁业务变更混入迁移分支。
