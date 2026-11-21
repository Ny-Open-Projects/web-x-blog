---
title: NestJS 全家桶要点：装饰器、Provider、Module、拦截器
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, NestJS]
---

## NestJS 全家桶要点：装饰器、Provider、Module、拦截器

**架构思想**：IoC（思想）+ DI（实现），框架负责实例化注入；控制器只接请求，业务下沉 Service。

参数装饰器分工速记：GET query 用 `@Query()`、POST body 用 `@Body()`、动态路由 `@Get(':id')` 配 `@Param()`、请求头 `@Headers()`。

Providers 注入四种姿势：类直注（需 `@Injectable()`）、`{provide:'Token', useClass}` + `@Inject('Token')` 改名注入、`useValue` 常量、`useFactory`+`inject` 工厂。共享模块 = 提供方 `exports`、使用方 imports；跨模块全局用 `@Global()`；动态模块 `static forRoot(options)` 返回 DynamicModule——课程里 Redis 模块、AliOss 模块都是这个模式。

统一响应三板斧（本项目标配）：响应拦截器统一 `{code:0,data}`（`NestInterceptor` + `next.handle().pipe(map(...))`）、异常过滤器统一 `{code:-1}`（`@Catch()` + `switchToHttp()`）、DTO 校验（class-validator + `useGlobalPipes(new ValidationPipe())`，`@Body()` 必须标注 DTO 类型才生效）。

坑：异常过滤器的正式名称是 Exception Filter，别混用拦截器 API 注册。

出处「课程25 · 00-4~5、9-3」
