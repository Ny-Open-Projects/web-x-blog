---
title: "题 4.3.1：Spring Boot 自动装配原理？怎么写一个 Starter？"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 面试题, 进阶题, 33]
type: 面试题
disableNunjucks: true
---

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
