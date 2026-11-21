---
title: [NODE-030] Express、Koa、NestJS 如何选型？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-030：Express、Koa、NestJS 如何选型？
**答**：
- **Express**：生态最大、中间件最多、心智简单；回调风格老、无原生 async 错误捕获（v5 改善）、大项目结构靠自觉。适合：中小 API、快速原型、老项目维护。
- **Koa**：洋葱模型 + async/await 原生支持，代码优雅、内核极小（按需装配）；但生态小于 Express、无内置路由/校验。适合：BFF、SSR 服务、对控制流要求高的服务。
- **NestJS**：基于装饰器 + DI 的企业级框架（底层可切 Express/Fastify），模块化、依赖注入、管道/守卫/拦截器、天然契合 TS 与微服务。适合：多人协作的中大型服务端、微服务、全栈同构 TS。
- 一句话：小服务 Express/Koa 起步快，规模上来或重 TS 选 NestJS；BFF 场景 Koa/Nest 均为主流。

```typescript
// NestJS 风格示意：Controller + 依赖注入（对比 Express 的函数拼装）
import { Controller, Get, Query, Injectable, Module, BadRequestException } from '@nestjs/common';

@Injectable()
class UserService {
  private users = [{ id: 1, name: 'Alice' }];
  findById(id: number) {
    const user = this.users.find((u) => u.id === id);
    if (!user) throw new BadRequestException('用户不存在'); // 统一异常过滤器转 HTTP 响应
    return user;
  }
}

@Controller('users')
class UserController {
  constructor(private readonly userService: UserService) {} // DI 自动注入

  @Get()
  getUser(@Query('id') id: string) {
    return this.userService.findById(Number(id));
  }
}

@Module({ controllers: [UserController], providers: [UserService] })
export class UserModule {}
// 对比：Express 中 service 靠 require 手动传递；Nest 通过模块图自动组装并支持单例/请求作用域
```
