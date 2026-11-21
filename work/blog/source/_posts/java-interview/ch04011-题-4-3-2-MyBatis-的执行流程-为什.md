---
title: "题 4.3.2：MyBatis 的执行流程？为什么 Mapper 接口不需要实现类？"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 面试题, 进阶题, 33]
type: 面试题
disableNunjucks: true
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
