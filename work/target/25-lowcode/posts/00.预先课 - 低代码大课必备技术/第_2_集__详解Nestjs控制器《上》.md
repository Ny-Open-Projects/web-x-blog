---
title: "详解 NestJS 控制器（上）：把参数装饰器一次讲透"
date: 2026-11-17 18:10
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# 详解 NestJS 控制器（上）：把参数装饰器一次讲透

> **导语**：控制器是 NestJS 接收 HTTP 请求的第一站，但真正容易被绕晕的是那一堆参数装饰器——取 query 用哪个、取 body 用哪个、动态路由又用哪个？本文从一个最简单的 `@Get()` 接口出发，逐个演示 `@Request()`、`@Query()`、`@Body()`、`@Param()`、`@Headers()`、`@HttpCode()`，并说清 GET 与 POST 取参位置的差别。读完你会知道每个参数该用哪个装饰器取，以及怎么给接口设置响应状态码。

## 前置知识

建议先读《Nestjs初始化目录结构介绍》，了解 Controller / Service / Module 三者分工；再读《Nestjs提供Get和Post请求》，掌握 `@Get()`、`@Post()` 方法装饰器的写法。此外需要会用 Apifox 之类的接口调试工具发送 GET / POST 请求、设置请求头。

## 正文

### 先把控制器还原到最简

为了专注讲装饰器，先把 `main.ts` 里设置的全局路由前缀、以及 `@Controller('app')` 的路径前缀都去掉，`getHello()` 也改成直接返回一个简单对象：

```ts
@Controller()
export class AppController {
  @Get()
  getHello() {
    return { code: 0 };
  }
}
```

此时请求 `localhost:3000`，接口就返回 `{ code: 0 }`。后面每个装饰器都在这个最简骨架上加参数。

### @Request() 与 GET 请求的 query

先看最「全」的取法：`@Request()`（也可写作 `@Req()`）拿到的是整个请求对象。在 `getHello(@Req() req)` 里打印 `req`，会看到内容非常多；前端用 GET 方式传 `name=大招` 时，参数落在 `req.query` 上：

```ts
@Get()
getHello(@Req() req) {
  console.log(req.query); // { name: '大招' }
  return { code: 0 };
}
```

于是 `req.query.name` 就是「大招」。但每次都要从整个请求体里挖一层很麻烦，NestJS 提供了更直接的参数装饰器 `@Query()`：

```ts
@Get()
getHello(@Query() query: { name?: string }) {
  return { name: query.name };
}
```

`@Query()` 相当于直接把请求对象里的 `query` 取出来注入，代码干净得多。

### POST 请求取 body

换成 `@Post()` 时，方法名不能与 `getHello` 重复，另起一个 `postHello`。先用 `@Req()` 观察：POST 的参数不在 `query`，而在 `req.body`：

```ts
@Post()
postHello(@Req() req) {
  console.log(req.body); // { name: '大招' }
  return { code: 0 };
}
```

于是 `req.body.name` 就能取到值。同样地，更推荐直接用 `@Body()`：

```ts
@Post()
postHello(@Body() body: { name?: string }) {
  return { name: body.name };
}
```

一句话记住差别：**GET 看 `query`，POST 看 `body`**，`@Query()` 与 `@Body()` 分别对应这两个位置。

### 动态路由用 @Param()

动态路由用冒号声明参数段，写法和 Vue Router 里的动态路由类似：

```ts
@Get(':id')
getById(@Param() params: { id: string }) {
  return { id: params.id };
}
```

请求 `GET /11`、`/22`、`/33` 时，`params.id` 分别拿到 `11`、`22`、`33`。这里要特别注意装饰器名是 `@Param()`，**没有 s**，写成带 s 的形式是取不到值的。

### @Headers() 与 @HttpCode()

`@Headers()` 作为第二个参数注入，可以拿到请求头：

```ts
@Get(':id')
getById(
  @Param() params: { id: string },
  @Headers() headers: Record<string, string>,
) {
  console.log(headers);
  return { id: params.id };
}
```

前端在请求里加一个 `token` 头，服务端打印的 headers 里就会多出对应的值。

`@HttpCode()` 是方法装饰器，从 `@nestjs/common` 引入，用来设置返回给前端的 HTTP 状态码：

```ts
@Get()
@HttpCode(500)
getHello() {
  return { code: 0 };
}
```

改成 `200` 再请求，响应码就变回 200。至于 `@Res()`、`@Response()`、`@Next()` 这些，放到后面接口实战时再结合场景讲。

### 本阶段配套工程

本阶段的练习代码可参考 `代码（已8期）/代码（已8期）/8-3/lowcode/`，根目录 `package.json` 已经用 pnpm workspace 统一管理多个子包：

```json
{
  "scripts": {
    "run:client": "pnpm --filter client run dev",
    "run:server": "pnpm --filter server run start:dev",
    "run:share": "pnpm --filter share run dev",
    "run:release": "pnpm --filter release run dev",
    "build:client": "pnpm --filter client run build",
    "build:server": "pnpm --filter server run build"
  }
}
```

控制器与接口代码在 `packages/server` 下，前端联调页面在 `packages/client` 下。

## 小结

- `@Request()` / `@Req()` 注入整个请求对象，适合调试观察，但取参要自己挖一层。
- GET 参数在 `query`，用 `@Query()`；POST 参数在 `body`，用 `@Body()`。
- 动态路由写成 `@Get(':id')`，取值用 `@Param()`（无 s）。
- `@Headers()` 取请求头，前端自定义的 `token` 也会出现在其中。
- `@HttpCode()` 设置响应状态码，是方法装饰器，从 `@nestjs/common` 引入。

## 下一步

参数怎么取讲完了，下一步是「取到之后怎么校验」。建议接着看《Nest的管道Pipe转换》，了解管道如何在参数进入控制器前做转换；再建议接着看《Nest的管道验证DTO》，用 DTO 把入参校验规范化。
