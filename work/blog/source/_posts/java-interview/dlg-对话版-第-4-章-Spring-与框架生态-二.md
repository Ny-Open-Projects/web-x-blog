---
title: "对话版 · 第 4 章 Spring 与框架生态（二面，约 25 分钟）"
date: 2026-11-18
categories: [Java面试, 面试对话]
tags: [Java面试, 对话剧, 33]
type: 对话剧
disableNunjucks: true
---

## 对话版 · 第 4 章 Spring 与框架生态（二面，约 25 分钟）

**【面试官】** Spring 的 IoC 解决了什么问题？

**【面试者】** 对象图的组装：没有容器时 OrderService 自己 new OrderDao，耦合在编译期；IoC 把创建与装配交给容器，收益是解耦、可测试（mock 注入）、可管理（生命周期/AOP 织入）。本质一句话：IoC 解决"对象图的组装"问题。

**【面试官】** Bean 的生命周期完整走一遍？

**【面试者】** 实例化 → 属性注入 → Aware 回调 → BeanPostProcessor#postProcessBeforeInitialization（@PostConstruct 由 InitDestroyAnnotationBeanPostProcessor 在此触发）→ 初始化（afterPropertiesSet → init-method）→ **postProcessAfterInitialization（★AOP 代理在此生成：AbstractAutoProxyCreator#wrapIfNecessary）** → 使用 → 销毁。口诀：两个后置处理器夹住初始化。

**【面试官】** 等等，AOP 代理是在前置处理创建的？

**【面试者】** 是在 **AfterInitialization** 阶段——AbstractAutoProxyCreator 是 BeanPostProcessor，它的 wrapIfNecessary 在初始化完成后决定是否包装。代理对象替换原对象放进容器，这也是 AOP 失效问题的根源（绕过代理调原对象，增强就没了）。

**【评注】** ✅ 面试官故意用错误前提试探——候选人纠正了前提。这是真实面试的高频套路。

**【面试官】** 循环依赖怎么解决？为什么需要三级缓存？

**【面试者】** 一级成品、二级半成品、三级 ObjectFactory。流程：A 实例化后把工厂放三级缓存 → 填充属性要 B → B 要注入 A，从三级缓存拿 A 的早期引用进二级 → B 完成 → A 完成。**第三级是为了 AOP**：工厂在被提前引用时才决定返回原对象还是提前生成代理，保证代理只生成一次且正常流程走 BeanPostProcessor。构造器注入的循环依赖无解，Spring 直接报错——这是合理的失败快速原则。另外 Boot 2.6+ 默认禁止循环依赖，我的团队规范是构造器注入+ArchUnit 门禁，让坏味道编译期暴露。

**【面试官】** 事务传播行为？REQUIRES_NEW 和 NESTED 区别？

**【面试者】** 默认 REQUIRED 加入当前事务；REQUIRES_NEW 挂起旧事务新建独立事务（**占用两个连接**，嵌套过深耗尽连接池——真实事故点）；NESTED 是保存点，同一物理事务、内层回滚不拖垮外层。选择：独立成败的日志/短信用 REQUIRES_NEW，主流程可补偿子步骤用 NESTED。

**【面试官】** @Transactional 什么情况会失效？

**【面试者】** 六条：自调用（绕过代理）、方法非 public、异常被 catch 吞掉、默认只回滚 RuntimeException（受检异常要 rollbackFor）、传播行为错配、类没被 Spring 管理。治理：这类问题靠 ArchUnit 门禁而不是 review 自觉。

**【面试官】** MyBatis 的 Mapper 为什么不需要实现类？一级缓存呢？

**【面试者】** 三件套：JDK 动态代理（MapperProxy）+ MapperFactoryBean + @MapperScan 的 ImportBeanDefinitionRegistrar——接口注册为 FactoryBean，getObject 返回代理。一级缓存是 SqlSession 级：Spring 集成下非事务时每条语句一个 SqlSession，跨语句失效；**同一事务内共享 Session，事务内有效**。二级缓存 namespace 级默认关，多表更新脏读，生产用 Redis。

**【评注】** ✅ 一级缓存的"事务内有效"是精确版答案，比"基本失效"高一档。

**【面试官】** @Async 的默认线程池是什么？要注意什么？

**【面试者】** 分三种情况：纯 Spring 无配置回退 SimpleAsyncTaskExecutor（每任务一线程，不池化）；**Spring Boot 2.1+ 自动配置 applicationTaskExecutor**（ThreadPoolTaskExecutor：core 8、队列无界——风险是积压 OOM 而非不池化）；Boot 3.2+ 开 spring.threads.virtual.enabled 后它变为 SimpleAsyncTaskExecutor（虚拟线程不限量）。四坑全说：默认池看清、自调用失效、异常静默（void 被吞要配 UncaughtExceptionHandler）、上下文丢失（TaskDecorator/TTL）。

**【评注】** ⭐ 分 Boot 版本的精确回答——原来"Boot 默认 SimpleAsyncTaskExecutor"是流传甚广的错误说法。

**【面试官】** Spring 的事件机制用过吗？事务里发事件有什么坑？

**【面试者】** publishEvent + @EventListener，默认同步。坑：事务方法内发布事件，监听器读的是未提交数据。正解 @TransactionalEventListener(phase=AFTER_COMMIT)。治理：AFTER_COMMIT 监听器只做低风险动作（日志/缓存刷新），高风险转 MQ——事件失败从同步异常降级为可重试消息。

**【面试官】** 自动装配的原理？

**【面试者】** @EnableAutoConfiguration → AutoConfigurationImportSelector 加载 imports 注册文件 → 条件注解过滤（OnClass/OnMissingBean/OnProperty）→ 用户 Bean 优先（@ConditionalOnMissingBean）。MyBatis 的 Mapper 是"动态代理 + FactoryBean + ImportBeanDefinitionRegistrar"三件套。

**【面试官】** 如果让你重新设计一个 IoC 容器，你会怎么做？

**【面试者】** 从最小需求推：Map<Class, ObjectFactory> 注册表 → BeanDefinition 元数据 → 拓扑排序实例化 → 注入 → 生命周期回调。然后逐步加约束：加 AOP 就需要提前暴露引用（三级缓存）、加配置热更新就需要 RefreshScope 代理、加生态就需要扩展点体系——最后设计会收敛到 Spring 的架构。Spring 是这个问题域三十年工程实践的局部最优解。

**【评注·终局】** 定级 **P7**。亮点：纠正面试官错误前提、@Async 分版本精确回答、自研容器推演。Spring 域过。

---

### 对话要点速记（本章）

1. 追问顺序：IoC → 生命周期 → 代理时机（纠错试探）→ 循环依赖 → 事务三连 → MyBatis → @Async → 事件 → 自动装配 → 自研设计。
2. 三个超预期点：纠错"代理在前置创建"、@Async 分 Boot 版本、一级缓存"事务内有效"。
3. 要点：面试官的错误前提（如"AOP 在前置处理"）往往是故意的——礼貌纠正就是得分动作。
