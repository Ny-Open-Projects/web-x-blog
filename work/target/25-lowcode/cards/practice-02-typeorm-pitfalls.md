---
title: TypeORM 实战要点与高频坑
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, TypeORM, MySQL]
---

## TypeORM 实战要点与高频坑

**连接**：三件套 typeorm + @nestjs/typeorm + **mysql2（最常漏装）**；`database` 填数据库名不是 Docker 容器名（高频坑）；`synchronize:true` 开发开、生产关（改手动迁移）；`autoLoadEntities:true` 自动加载 forFeature 注册的实体。

**CRUD**：`find({where})` 单对象=AND、数组=OR；条件属性名须与实体字段一致否则查不到；`update(条件,新值)/delete(条件)` 返回 `affected` 用于确认影响条数；TypeORM 没有 findAll，查全部用 `find()`。批量查用 `In` 操作符（统计模块一次查出四种问卷组件）。

**关系**：`@OneToOne` + `@JoinColumn({name})`；`@OneToMany/@ManyToOne` 成对定义，回调指定回指属性；`relations` 写**属性名**不是列名，拼错直接报错；自动同步只建结构，关联数据需手动补。

**事务**：新版走 `DataSource.createQueryRunner()`（弃用 getConnection，中文官网旧写法要避开）；事务内操作必须走 `queryRunner.manager`。

选型理由一句话：TypeORM 装饰器写法与 Nest+TS 高度集成，比 Prisma 多库联合查询支持好、比 Sequelize 配置省心。

出处「课程25 · 10-1~10-8、21-3」
