---
title: "题 4.7.6：老 SpringMVC 单体迁到 Spring Boot，路径怎么走？"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 4.7.6：老 SpringMVC 单体迁到 Spring Boot，路径怎么走？

**【参考回答（可背）】** 四步渐进：① **容器先行**：war 包直接部署进 Boot 的可运行容器（Boot 兼容传统 war：SpringBootServletInitializer），行为零变化；② **配置收编**：XML 配置逐步翻译为 Java Config/@ConfigurationProperties，一次一类（数据源/事务/MVC），每步回归；③ **依赖治理**：parent 换 spring-boot-starter-parent，冲突靠 BOM + dependency:tree 清理（jakarta 命名空间是 Boot3 迁移最大断点，老 javax 依赖需 Boot2 过渡）；④ **特性启用**：加 Actuator/统一异常/优雅停机等 Boot 红利。验收口径：接口回归全绿 + 监控指标无差 + 回滚预案随时可用。
**【追问链】** ① 最大的坑？（配置迁移的"隐式行为差异"：如 Jackson 版本、日期序列化、异常默认页——都要回归用例兜底）② 什么该迁什么不该迁？（按变更频率与部署耦合度排序，边缘低频服务最后迁）。
**【P10 加分项】** 迁移即治理："迁移窗口是'免费重构期'——顺手统一异常体系、日志格式、配置中心接入；但严禁业务逻辑变更混入迁移分支，否则回归爆炸。CI 双跑对比（新旧接口 diff）是迁移安全的护城河。"

---
*下一章：第 5 章 MySQL 与存储 —— InnoDB 体系、索引与 MVCC、日志与主从、分库分表。*
