# 第 4 章 Spring 与主流框架生态 —— IoC/AOP 源码、事务、自动装配

> Spring 题的陷阱在于"人人都会用，一半人答不对源码，极少数人答得出设计动机"。
> P10 面试官会问：**Spring 为什么这么设计？如果没有 Spring 你怎么办？** —— 考察的是
> "框架之上的抽象能力"，而不是注解背诵。

---

## 4.0 本章考察范围雷达

| 维度 | P4-P5 | P6-P7 | P8-P10 |
|------|-------|-------|--------|
| IoC | 注解会用 | Bean 生命周期全流程 | 扩展点清单、框架级二次开发 |
| AOP | 切面会写 | 动态代理原理、失效场景 | AOP 在架构治理中的应用（幂等/日志/熔断统一封装） |
| 事务 | @Transactional | 传播行为+失效场景 | 分布式事务选型与一致性权衡 |
| Boot | 会搭建 | 自动装配原理 | Starter 体系建设、Spring Boot 3 AOT/GraalVM |

---

## 4.1 零基础起步

### 卡片 1：IoC 是什么？为什么需要？
- **控制反转**：对象的创建和依赖装配交给容器（IoC 容器），代码只声明"我需要什么"（依赖注入 DI）。
- 没有容器时：`OrderService` 自己 `new OrderDao()`，耦合在编译期；有了容器：构造器注入，运行期装配，**可替换、可测试（mock 注入）、可管理（生命周期/AOP 织入）**。
- 记住本质一句话：**IoC 解决的是"对象图的组装"问题，收益是解耦与可测试性。**

### 卡片 2：AOP 是什么？
把"横切关注点"（日志、事务、权限、监控）从业务代码中剥离，通过动态代理在运行期织入。
Spring AOP = **JDK 动态代理**（目标实现了接口）或 **CGLIB**（子类继承，字节码生成）。

### 卡片 3：Bean 的作用域
singleton（默认，容器内唯一）/ prototype（每次新建）/ request / session / websocket。
**坑**：singleton 注入 prototype 时 prototype 也会变单例——要用 @Lookup、ObjectFactory 或 scoped proxy。

### 卡片 4：Spring Boot 解决了什么？
不是新框架，是 Spring 的**约定优于配置层**：自动装配（按 classpath 条件装配 Bean）+ Starter 依赖聚合 + Actuator 生产特性。"Spring Boot 的本质是：**把'如何配置'的决策权收编到框架，团队配置漂移归零**。"

---

## 4.2 入门题（P4-P6）

### 题 4.2.1：说说 Bean 的生命周期？

**【参考回答（可背，按顺序）】**
1. **实例化**：构造器/工厂方法创建对象（此时还是"生 Bean"，属性未注入）；
2. **属性注入**：@Autowired/@Value 填充依赖；
3. **Aware 回调**：BeanNameAware → BeanFactoryAware → ApplicationContextAware（给 Bean 塞容器引用）；
4. **BeanPostProcessor.postProcessBeforeInitialization**（@PostConstruct 由 InitDestroyAnnotationBeanPostProcessor 在此触发）；
5. **初始化**：@PostConstruct → InitializingBean.afterPropertiesSet → init-method；
6. **BeanPostProcessor.postProcessAfterInitialization**（★AOP 代理在此生成：AbstractAutoProxyCreator#wrapIfNecessary）；
7. **使用**；
8. **销毁**：@PreDestroy → DisposableBean.destroy → destroy-method。
一句话版（面试口播）：**实例化 → 属性注入 → Aware → 前置处理 → 初始化 → 后置处理 → 使用 → 销毁**，记住"两个后置处理器夹住初始化"。

**【追问链】**
1. AOP 代理什么时候生成？→ AbstractAutoProxyCreator 是 BeanPostProcessor，在 postProcessAfterInitialization 阶段生成代理对象——所以**代理对象替换了原对象放进容器**，这是 AOP 失效问题的根源（见题 4.2.3）。
2. BeanPostProcessor 和 BeanFactoryPostProcessor 区别？→ BFPP 在**所有 Bean 实例化前**改 Bean 定义（如 PropertySourcesPlaceholderConfigurer 处理占位符）；BPP 逐 Bean 干预实例过程。

**【P10 加分项】**
列出工程常用扩展点清单并说明各自用途：InstantiationAwareBeanPostProcessor（自定义创建）、FactoryBean（复杂对象创建，MyBatis Mapper 的实现方式）、EnvironmentPostProcessor（启动早期改配置）、ApplicationListener/Event 体系（解耦内部通知）、SmartLifecycle（优雅启停）。**"扩展点清单"是区分"用过 Spring"与"改过 Spring"的试金石。**

---

### 题 4.2.2：@Autowired 的注入过程？循环依赖怎么解决？为什么三级缓存能解决、二级不行？

**【参考回答（可背）】**
注入方式：AutowiredAnnotationBeanPostProcessor 在属性注入阶段按类型（byType）→ 多个候选再按名称（byName/@Qualifier）→ 优先级 @Primary。
**循环依赖**（A 依赖 B，B 依赖 A，仅限 singleton 且 setter/字段注入）：
- **一级缓存** singletonObjects：成品 Bean；
- **二级缓存** earlySingletonObjects：半成品（已实例化未填充属性）；
- **三级缓存** singletonFactories：ObjectFactory（能产出早期引用的工厂）。
流程：A 实例化后把"产出自己的工厂"放入三级缓存 → 填充属性需要 B → B 实例化后要注入 A，从三级缓存拿到 A 的早期引用放入二级 → B 完成初始化进一级 → A 继续，拿到 B 完成自己。

**为什么需要第三级（高频追问）**：
因为要兼容 **AOP**。若 A 需要代理，三级缓存的工厂在"被别人提前引用"的时刻才决定返回原对象还是提前生成代理（保证代理只生成一次，且正常流程仍走 BeanPostProcessor）；如果只有二级缓存，要么所有 Bean 无条件提前代理（违背设计原则：代理应在初始化后生成），要么 AOP 场景循环依赖直接失败。**三级缓存是用"延迟决定"换取"代理语义正确"**。

构造器注入的循环依赖无解（还没实例化就要对方的引用），Spring 直接报错——这是合理的失败快速原则。

**【追问链】**
1. Spring Boot 2.6+ 为什么默认禁止循环依赖？→ 循环依赖往往是设计坏味道（职责纠缠），框架选择"默认禁止、需要时显式开启"，推动重构。
2. @Lazy 能解吗？→ 能：注入的是延迟代理，首次真正调用时才解析目标，绕开创建期循环。

**【P10 加分项】**
架构判断："循环依赖报警应接入代码门禁——我们团队策略是：禁止新增 setter/字段注入（强制构造器注入），构造器注入天然暴露循环依赖，编译期就失败；@Lazy 只允许出现在过渡性重构中并有 TODO 期限。"

---

### 题 4.2.3：AOP 失效的场景有哪些？为什么失效？

**【参考回答（可背，考频极高）】**
根源一句话：**AOP 是代理对象在干活，绕过代理直接调"原始对象"的方法，增强就失效**。
必背 6 场景：
1. **同类内部调用**：this.methodB()（A 方法内调 B 方法，B 上的 @Transactional/@Cacheable 失效）——最常见；
2. **final/private/static 方法**：CGLIB 无法重写；
3. **new 出来的对象**：不在容器里，根本没代理；
4. 异常被 catch 吞掉（针对事务场景）；
5. 多线程调用事务方法（事务绑定 ThreadLocal 连接）；
6. 传播行为配置不符合预期（如 NOT_SUPPORTED 挂起事务）。

解法：注入自身（self 注入代理）、AopContext.currentProxy()（需 exposeProxy=true）、拆类（最推荐）、AspectJ 编译期织入。

**【追问链】**
1. JDK 动态代理和 CGLIB 区别与选择？→ JDK 代理基于接口（Proxy+InvocationHandler，反射调用）；CGLIB 基于继承生成子类（FastClass 机制索引方法避免反射）。Spring Boot 2.x 起默认 CGLIB（proxyTargetClass=true），避免"注入具体类型失败"。
2. 事务失效完整清单？→ 上述 1-3 + 方法非 public（JDK 代理接口限制；CGLIB 也要求 public 可见性）、rollbackFor 默认只回滚 RuntimeException/Error（受检异常不回滚，必背）、catch 后不重新抛、传播行为嵌套错配、数据源/事务管理器配置错。

**【P10 加分项】**
给"团队治理"方案：用 ArchUnit 在 CI 里静态检查"同类调用被 @Transactional 方法"的规则，把运行期失效变成构建期失败——**把框架坑转化为自动化门禁**是 P10 的典型动作。

---

### 题 4.2.4：Spring 事务的传播行为？REQUIRES_NEW 和 NESTED 的区别？

**【参考回答（可背）】**
7 种传播行为，重点背 3+1：
- REQUIRED（默认）：有事务加入，没有新建；
- REQUIRES_NEW：**挂起当前事务**，新建独立事务（内层回滚不影响外层已提交；外层回滚不影响内层已提交）；
- NESTED：在当前事务内设置**保存点（savepoint）**，内层回滚回滚到保存点，外层可继续；外层回滚内层必回滚（同一物理事务）；
- SUPPORTS/NOT_SUPPORTED/MANDATORY/NEVER：边界语义。
选择经验：**发短信/写日志等"必须独立成败"用 REQUIRES_NEW；主流程内的可补偿子步骤用 NESTED**。
底层：事务状态由 PlatformTransactionManager 管理，挂起 = 把当前 ThreadLocal 连接保存、清空、新建连接（注意 REQUIRES_NEW 占用**两个数据库连接**，嵌套过深会耗尽连接池——真实事故点）。

**【追问链】**
1. Spring 事务和数据库事务的关系？→ Spring 事务是**编程模型抽象**，真事务由 JDBC 连接的 autocommit/commit/rollback 完成；Spring 做的是把"连接绑定 ThreadLocal、传播、回滚规则"这套胶水管好。
2. 长事务危害？→ 连接占用（池耗尽）、undo 增长、间隙锁范围扩大（死锁概率↑）、主从延迟放大。治理：事务内不 RPC/不发 MQ（先落库后异步）、@Transactional 只包必要代码、大事务拆分。

**【P10 加分项】**
讲"大事务治理"专项：APM 按 RT 维度找 Top 事务 → 规则扫描（事务内 RPC/IO）→ 拆分为"本地事务 + 事务外副作用 + 补偿" → 落地 TransactionSynchronization 的 afterCommit 发消息（保证**先提交再通知**，避免消费方读不到数据）。

---

## 4.3 进阶题（P7-P8）

### 题 4.3.1：Spring Boot 自动装配原理？怎么写一个 Starter？

**【参考回答（可背）】**
1. @SpringBootApplication = @Configuration + @ComponentScan + **@EnableAutoConfiguration**。
2. @EnableAutoConfiguration 通过 @Import(AutoConfigurationImportSelector.class) 加载：
   `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`（Boot 2.7+ 新文件，旧的 spring.factories 已废弃）里的自动配置类清单。
3. 每个自动配置类用条件注解决定是否生效：@ConditionalOnClass（类路径有）、@ConditionalOnMissingBean（用户没自定义，**用户优先**的关键）、@ConditionalOnProperty（开关）。
4. 配置绑定：@ConfigurationProperties + 松散绑定 + 元数据提示（spring-configuration-metadata）。

**写 Starter 步骤（可背）**：
xxx-spring-boot-starter（空聚合模块）+ xxx-autoconfigure（自动配置类 + @Bean + 条件注解 + 配置属性类）+ imports 注册文件；发布到私服，业务方引依赖即用。
公司价值：统一中间件接入（如公司内部 Redis 客户端封装、审计日志、幂等组件），**"开箱即用 + 默认安全"**。

**【追问链】**
1. 同名 Bean 用户自己定义了会怎样？→ @ConditionalOnMissingBean 判断用户 Bean 先注册（用户扫描在自动装配之前），自动配置让位——这是"约定可覆盖"原则的机制保证。
2. 自动装配的加载顺序控制？→ @AutoConfigureBefore/After + Ordered；排查装配问题用 --debug 启动看 ConditionEvaluationReport。

**【P10 加分项】**
讲"公司 Starter 体系治理"：版本对齐 BOM、Starter 分层（基础/可选）、废弃 Starter 的兼容下线策略、启动性能治理（自动装配类数量 → 启动耗时 → lazy init / CDS / AOT）。

---

### 题 4.3.2：MyBatis 的执行流程？为什么 Mapper 接口不需要实现类？

**【参考回答（可背）】**
1. **Mapper 是 JDK 动态代理**：MapperProxy implements InvocationHandler，接口方法调用被拦截 → 定位 MapperMethod → 按方法签名解析成 SQL 命令类型（insert/update/select）→ 走 SqlSession 执行。
2. **接入 Spring 靠 FactoryBean + 扫描**：@MapperScan → MapperScannerRegistrar（ImportBeanDefinitionRegistrar）→ 每个接口注册 MapperFactoryBean（getObject 返回代理）——回答了"接口怎么变成 Bean"。
3. 执行链路：Executor（Simple/Reuse/Batch；CachingExecutor 二级缓存装饰）→ StatementHandler → ParameterHandler（参数设置，TypeHandler）→ 执行 SQL → ResultSetHandler（结果映射，自动映射/嵌套 resultMap）。
4. 缓存：一级缓存 SqlSession 级（默认开；**Spring 集成下非事务时每条语句一个 SqlSession、跨语句失效，同一事务内共享 Session 故事务内有效**）、二级缓存 namespace 级（默认关，多表关联更新会脏读，**生产建议关掉改用 Redis**）。

**【追问链】**
1. #{} 与 ${} 区别？→ #{} 预编译参数占位（防 SQL 注入）；${} 字符串拼接（order by 列名动态化不得不用时，白名单校验）。
2. 大数据量查询？→ 游标（Cursor）/流式（fetchSize=Integer.MIN_VALUE for MySQL）+ 逐条处理，避免全量加载（衔接第 3 章 OOM 案例）。
3. 插件机制？→ Interceptor 拦截四大对象（Executor/StatementHandler/ParameterHandler/ResultSetHandler），责任链+动态代理，分页插件、慢 SQL 监控、SQL 审计都基于此。

**【P10 加分项】**
对比 JPA/MyBatis-Plus 选型：强领域模型与 CRUD 密集选 JPA/MP，复杂 SQL 与 DBA 审查文化选 MyBatis；再讲公司级 SQL 治理（全量 SQL 采集、慢查询门禁、强制走索引检查）——落点在"数据访问的团队工程能力"。

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

## 4.4 压轴题（P9-P10）

### 题 4.4.1：如果没有 Spring，你会如何设计一个依赖注入容器？（考察"脱离框架的设计力"）

**【参考回答（框架可背：需求 → 最小设计 → 逐步加约束）】**
1. **明确最小需求**：按类型/名称注册与获取（容器本质是 `Map<Class, ObjectFactory>`）+ 生命周期管理 + 单例缓存 + 依赖解析。
2. **核心流程**：扫描（classpath 扫描 @Component → BeanDefinition 元数据）→ 排序（先无依赖后有依赖，拓扑排序）→ 实例化 → 注入（反射 setField/constructor）→ 生命周期回调。
3. **加约束一：AOP** → 创建后用代理工厂包装；需要"提前暴露引用"解决循环依赖 → 引入三级缓存结构。
4. **加约束二：配置** → @Value 占位符解析（PropertySource 抽象）；外部化配置热更新 → 配置中心监听 + Bean 动态刷新（@RefreshScope 的原理：代理 + 缓存失效重建）。
5. **加约束三：生态** → 事件总线（解耦组件通信）、条件装配（面向多环境）、扩展点体系（让别人不改源码扩展你的容器——**框架的竞争本质是扩展点生态的竞争**）。
6. **收尾判断**：最后你会发现设计收敛到 Spring 的架构——这不是巧合，Spring 是这个问题域三十年工程实践的局部最优解。**复述 Spring 设计恰好证明你理解了它每一步的"为什么"**。

**【追问链】**
1. Spring 容器启动为什么慢？→ 类路径扫描（ASM 读字节码）、BeanDefinition 解析、Bean 逐个实例化（反射+初始化回调+代理生成）。优化：懒加载、CDS/AppCDS、AOT（Boot 3 编译期生成 Bean 定义，运行时免反射）、拆分部署单元。
2. Spring 6/Boot 3 关键变化？→ JDK17 基线、Jakarta EE 9+（javax→jakarta）、AOT/Native、RFC 7807 问题详情、可观测性内置（Micrometer Tracing 替代 Sleuth）。

**【P10 加分项】**
给出"框架依赖战略"：中间件与框架选型的决策框架——社区活跃度、公司人才储备、迁移退出成本、与云厂商绑定度；并以"我们自研 XX 框架 vs 深度定制开源"的真实权衡为例（自研条件：核心路径不可控风险 > 自研维护成本；否则拥抱开源 + 少量扩展点）。

---

### 题 4.4.2：Spring 生态里如何实现"一个接口多个实现按条件路由"？背后的设计模式是什么？在架构里怎么用？

**【参考回答（可背）】**
1. **机制**：接口多个 @Component 实现 → 注入 Map<String, X> 或 List<X>（Spring 自动按名/序收集）→ 路由器按业务 key 取实现；或 @ConditionalOnProperty 多配置变体。
2. **设计模式**：策略模式（实现族）+ 工厂/注册器（Map 路由）+ 模板方法（公共骨架）——Spring 把"找实现"这个工厂职责容器化了。
3. **架构应用（必背 3 例）**：
   - 支付渠道路由（微信/支付宝/银联实现同一 PaymentChannel 接口，按订单属性路由）；
   - 数据源路由（AbstractRoutingDataSource，读写分离/多租户）；
   - 审批流/风控规则引擎（策略+责任链组合）。
4. **治理**：新渠道接入成本 = 一个类 + 一行注册，开闭原则落地；配合 Starter 把通用路由骨架下沉为公共组件。

**【追问链】**
1. 策略多了怎么管理？→ 注册中心化（枚举 key + Spring 容器自检启动时校验"每个业务 key 都有实现"，缺实现启动失败 fail-fast）。
2. 和规则引擎（Drools/QLExpress）的关系？→ 简单分支用策略；规则高频变更、业务同学自助配置时上规则引擎，代价是可读性与调试成本——**别为了技术而技术**。

**【P10 加分项】**
讲"扩展点设计"作为架构能力：定义 SPI 时同时定义契约测试（每个实现必须通过的公共测试套件），保证 N 个实现行为一致；渠道实现放在独立 maven 模块按需打包——体现"架构 = 让变更低成本"的价值观。

---

## 4.5 本章高频追问链图谱

```
IoC ──→ Bean 生命周期 ──→ BeanPostProcessor ──→ 扩展点体系 ──→ 自研容器设计
AOP ──→ JDK/CGLIB ──→ 代理失效 ──→ ArchUnit 门禁 ──→ AspectJ
循环依赖 ──→ 三级缓存 ──→ AOP 提前代理 ──→ 2.6 默认禁止 ──→ 构造器注入规范
事务 ──→ 传播行为 ──→ REQUIRES_NEW 双连接 ──→ 大事务治理 ──→ afterCommit 发消息
自动装配 ──→ 条件注解 ──→ Starter 体系 ──→ 启动优化 ──→ Boot3 AOT/Native
Mapper 接口 ──→ 动态代理 ──→ FactoryBean ──→ 插件机制 ──→ SQL 治理
```

## 4.6 一页速记卡

1. Bean 生命周期口诀：实例化→注入→Aware→前置→初始化→后置→使用→销毁；AOP 代理在 postProcessAfterInitialization 生成。
2. 三级缓存：成品/半成品/工厂；第三级为 AOP 延迟决定；构造器循环依赖无解。
3. AOP 失效根因一句话：绕过代理。同类自调用是头号坑。
4. 事务失效：非 public、自调用、catch 吞、默认只回滚 RuntimeException、受检异常要 rollbackFor。
5. REQUIRES_NEW 挂起新开（双连接）；NESTED 保存点（同连接）。
6. 自动装配：imports 文件 + 条件注解；@ConditionalOnMissingBean = 用户优先。
7. Mapper 无实现类 = JDK 动态代理 + FactoryBean + ImportBeanDefinitionRegistrar。
8. Controller 单例必须无状态；全局异常 @RestControllerAdvice。
9. 先提交后通知：TransactionSynchronization#afterCommit 里发 MQ。
10. Boot3：JDK17、jakarta、AOT/Native、Micrometer Tracing。

## 4.7 参考资料
- 《Spring 源码深度解析》/ 小傅哥《手写 Spring》系列（理解容器最小实现）
- Spring 官方文档：Core（IoC 容器、AOP）、Boot（Auto-configuration、AOT）
- 阿里《Java 开发手册》：并发与事务相关强制条款
- 源码入口：AbstractApplicationContext#refresh（背下 13 个方法名顺序是进阶信号）

## 4.7 增补题（v1.1 深度扩充）

### 题 4.7.1：Spring 事件机制怎么用？事务边界与事件监听的关系？

**【面试官意图】** 检验事件解耦的真实工程理解，尤其是"事件发出去但事务没提交"这个经典坑。
**【参考回答（可背）】** 机制：发布方 ApplicationEventPublisher.publishEvent，监听器实现 ApplicationListener 或 @EventListener（支持泛型/条件/有序 @Order）；默认**同步**在同一线程执行，@Async 才异步。经典坑：事务方法内发布事件，监听器拿到的是**未提交事务**里写入的数据（读不到或读到中间态）。正确姿势：用 @TransactionalEventListener(phase = AFTER_COMMIT)（默认只处理提交后；BEFORE_COMMIT 可用于校验；AFTER_ROLLBACK 用于补偿）。
**【追问链】** ① @Async 监听器里事务怎么算？（新事务，无传播上下文）② 事件会丢吗？（AFTER_COMMIT 阶段抛异常不影响事务但事件丢失——监听器内部要自行兜底重试）③ 和 MQ 的选择？（进程内同步联动用事件，跨服务用 MQ；事件是"方法级解耦"不是"服务级解耦"）。
**【P10 加分项】** 给治理经验："我们规定 AFTER_COMMIT 监听器只做'低风险动作'（日志/缓存刷新/通知），高风险动作一律转 MQ——把事件失败从'同步异常'降级为'可重试消息'。"再提 Spring 自身就是重度用户（ContextClosedEvent、ServletRequestHandledEvent 等），能举 2 个内置事件即加分。

### 题 4.7.2：BeanPostProcessor 有哪些典型应用？写一个会踩什么坑？

**【参考回答（可背）】** 典型应用四类：① AOP 代理生成（AbstractAutoProxyCreator）；② @Autowired/@Value 解析（AutowiredAnnotationBeanPostProcessor）；③ 参数校验与审计埋点（自定义 BPP 包装 Bean 为代理）；④ 延迟初始化/占位符处理。写自定义 BPP 的坑：① BPP 本身也是 Bean，**启动极早**——构造器里别依赖其他业务 Bean（会拉长依赖链甚至循环）；② returnBean 为 null 会直接"吞掉" Bean（框架内 BPP 的高级用法，业务慎用）；③ 判断别过度：每个 Bean 都会被 BPP 处理，逻辑必须便宜（缓存元数据、精确 instanceof）。
**【追问链】** ① BPP 与 BeanFactoryPostProcessor 的执行顺序？（BFPP 在所有 Bean 实例化前改 BeanDefinition；BPP 逐 Bean 干预实例过程；PropertySourcesPlaceholderConfigurer 是 BFPP）② 为什么 @PostConstruct 不会被代理拦住？（InitDestroyAnnotationBeanPostProcessor 在初始化阶段反射调用，绕过代理链）。
**【P10 加分项】** "BPP 是 Spring 的'字节码级扩展点'——公司基础库用它统一给所有 Service 织入 traceId 日志与慢调用采样，业务方零侵入接入。这就是框架团队和业务团队的能力分水岭。"

### 题 4.7.3：@Async 的四大坑？

**【参考回答（可背）】** ① **默认线程池要分清**：纯 Spring（无 Boot）时 @Async 回退 SimpleAsyncTaskExecutor（每任务一线程，不池化）；而 **Spring Boot 2.1+ 自动配置 applicationTaskExecutor**（ThreadPoolTaskExecutor：core 8、**队列无界**——风险是任务积压 OOM 而非不池化）；Boot 3.2+ 开启 spring.threads.virtual.enabled 后它又变为 SimpleAsyncTaskExecutor（虚拟线程不限量）。生产无论哪种都应显式定义 ThreadPoolTaskExecutor 并与第 2 章线程池规范对齐；② **自调用失效**：同类调 @Async 方法走原对象，异步不生效（与 AOP 失效同根）；③ **异常静默**：void 方法异常被吞，要配 AsyncConfigurer 的 getAsyncUncaughtExceptionHandler；返回 Future 则异常在 get 时抛出；④ **上下文丢失**：异步线程拿不到 ThreadLocal（MDC traceId、SecurityContext）——用 TaskDecorator 复制上下文或 TTL。
**【追问链】** ① @Async 与事务怎么交互？（被调用方法在新线程，调用方事务不覆盖它；方法内有 @Transactional 则是新事务）② 线程池打满怎么办？（排队+拒绝策略，CallerRunsPolicy 退化为同步——能接受则天然反压）。
**【P10 加分项】** 组合拳："@Async + @TransactionalEventListener 是事务后异步通知的标准姿势；但两者叠加时必须意识到'异步监听器没有事务上下文'，我们用'提交后发 MQ'替代了它，彻底摆脱 ThreadLocal 治理负担。"

### 题 4.7.4：prototype Bean 注入 singleton 有什么问题？如何正确获取？

**【参考回答（可背）】** 问题：singleton A 注入 prototype B，B 在 A 创建时注入一次，之后 A 的每次使用拿到的是**同一个** B——prototype 语义失效（只"新"了一次）。正确获取三种：① 注入 `ObjectFactory<B>` / `ObjectProvider<B>`，用时 getObject() 每次新建；② @Lookup 抽象方法（CGLIB 覆写返回容器实例）；③ scoped proxy（proxyMode = TARGET_CLASS，代理每次委托容器取新实例）。
**【追问链】** ① request/session 作用域 Bean 注入 singleton 为什么能工作？（就是 scoped proxy 在起作用）② prototype Bean 的销毁回调谁负责？（容器只负责到创建，销毁由客户端自己管理——面试冷知识，答出即证明读过文档）。
**【P10 加分项】** 设计判断："多实例对象优先考虑'工厂模式 + 显式 create'，而不是滥用 prototype 作用域——作用域是容器特性不是对象生命周期管理的万能锤。"

### 题 4.7.5：Spring Boot 启动慢，怎么优化？（从分钟级到秒级）

**【参考回答（可背）】** 按代价从低到高：① **测量先行**：--debug 看 ConditionEvaluationReport + 启动端点（ApplicationStartup/StartupStep）定位耗时 Bean；② **懒加载**：spring.main.lazy-initialization=true（注意首次请求 RT 变长，需配预热）；③ **组件瘦身**：排查无用的自动配置与组件扫描范围（@ComponentScan 收敛包路径）；④ **类加载优化**：CDS/AppCDS 共享类存档；⑤ **AOT**：Boot 3 的 spring.aot.enabled 编译期固化 Bean 定义，免运行时反射（GraalVM Native 启动毫秒级）；⑥ **部署侧**：大单体拆微服务/分层镜像预热。
**【追问链】** ① 懒加载有什么坑？（配置错误/装配失败延迟到运行时才暴露，监控与预热必须跟上）② 为什么扫描包越小启动越快？（ClassPath 扫描读字节码+条件评估，BeanDefinition 数量线性影响）。
**【P10 加分项】** 给量化叙事："我们的 800+ Bean 单体通过'懒加载+CDS+扫描收敛'从 42s 降到 15s，AOT 试验后 8s——但结论是'启动优化是为扩容和发布提速服务'，非核心服务不值得投入，先按发布频率和弹性需求排序。"

### 题 4.7.6：老 SpringMVC 单体迁到 Spring Boot，路径怎么走？

**【参考回答（可背）】** 四步渐进：① **容器先行**：war 包直接部署进 Boot 的可运行容器（Boot 兼容传统 war：SpringBootServletInitializer），行为零变化；② **配置收编**：XML 配置逐步翻译为 Java Config/@ConfigurationProperties，一次一类（数据源/事务/MVC），每步回归；③ **依赖治理**：parent 换 spring-boot-starter-parent，冲突靠 BOM + dependency:tree 清理（jakarta 命名空间是 Boot3 迁移最大断点，老 javax 依赖需 Boot2 过渡）；④ **特性启用**：加 Actuator/统一异常/优雅停机等 Boot 红利。验收口径：接口回归全绿 + 监控指标无差 + 回滚预案随时可用。
**【追问链】** ① 最大的坑？（配置迁移的"隐式行为差异"：如 Jackson 版本、日期序列化、异常默认页——都要回归用例兜底）② 什么该迁什么不该迁？（按变更频率与部署耦合度排序，边缘低频服务最后迁）。
**【P10 加分项】** 迁移即治理："迁移窗口是'免费重构期'——顺手统一异常体系、日志格式、配置中心接入；但严禁业务逻辑变更混入迁移分支，否则回归爆炸。CI 双跑对比（新旧接口 diff）是迁移安全的护城河。"

---
*下一章：第 5 章 MySQL 与存储 —— InnoDB 体系、索引与 MVCC、日志与主从、分库分表。*
