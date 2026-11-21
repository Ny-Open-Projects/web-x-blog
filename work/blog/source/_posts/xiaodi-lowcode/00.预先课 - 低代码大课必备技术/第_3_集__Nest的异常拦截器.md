---
title: "NestJS 异常过滤器：用 Exception Filter 统一错误响应"
date: 2026-11-17 18:26
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# NestJS 异常过滤器：用 Exception Filter 统一错误响应

> **导语**：响应拦截器把成功路径统一了，可一旦接口报错，NestJS 默认的错误结构又和自定义格式对不上，前端仍然要写两套解析逻辑。本文讲清楚"异常拦截器"在 NestJS 里的准确叫法——异常过滤器（Exception Filter），并带你实现一个全局 `AbnormalFilter`，把所有错误收敛成 `code / data / msg` 结构。读完后你能解释它与响应拦截器的分工，也能避开注册时用错 API 的坑。

## 前置知识

- 已经掌握《Nest的响应拦截器》，理解 `useGlobalInterceptors` 的注册方式。
- 了解 NestJS 内置异常处理与 HTTP 状态码，建议先阅读《掌握Rxjs和在Nest中的应用》与《什么是装饰器和Nestjs中的应用》，熟悉装饰器与接口实现的写法。

## 正文

### 为什么错误也要统一格式

图形验证码、短信验证码、注册、登录……这些接口都有失败的可能。如果每个接口各自抛错，或者干脆沿用框架默认的错误结构，前端就要针对不同的错误形状分别处理。

异常过滤器的作用，就是提供一种统一的方式来处理和修改从后端返回给前端的错误信息：约定一个固定的 `code`（比如 `-1`，也可用其他业务状态码），`data` 在出错时通常为空，`msg` 用来告诉前端到底哪里出了问题。这样"成功长什么样、失败长什么样"都由后端一套约定说了算：

```json
{
  "code": -1,
  "data": null,
  "msg": "接口不存在 / Service error"
}
```

### 准确名称：异常过滤器，而非"异常拦截器"

口播里常把"全局处理 HTTP 异常的中间件"叫作异常拦截器，但在 NestJS 中它的正式身份是**异常过滤器（Exception Filter）**。这一点会直接决定后面注册时用哪个 API，先记牢：

- 响应拦截器对应 `NestInterceptor` + `useGlobalInterceptors`；
- 异常过滤器对应 `ExceptionFilter` + `useGlobalFilters`。

### 实现 AbnormalFilter

在和响应拦截器相同的 `common` 目录里新建 `abnormal.filter.ts`，导出一个类并实现 `ExceptionFilter` 接口：

```ts
import {
  ArgumentsHost,
  Catch,
  ExceptionFilter,
  HttpException,
} from '@nestjs/common';

@Catch()
export class AbnormalFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse();
    const status = exception.getStatus();
    const message = exception.message || 'Service error';

    response.status(status).json({
      code: -1,
      data: null,
      msg: message,
    });
  }
}
```

按调用顺序拆开看：

1. 类要用 `@Catch()` 装饰器标记，这是 NestJS 规定好的固定写法；实现了 `ExceptionFilter` 接口，就必须提供 `catch` 方法，否则编译期就会报错。
2. `catch` 接收两个参数：`exception` 是异常对象，`host` 是参数宿主。刚接触时对这两个参数感到困惑很正常，记住框架约定即可。
3. 通过 `host.switchToHttp()` 拿到请求上下文 `ctx`，再用 `ctx.getResponse()` 取得 `response` 对象——只有拿到它，才能决定返回给客户端什么。
4. 状态码用 `exception.getStatus()` 获取；异常消息取 `exception.message`，若业务层没有给出具体提示，就回退到默认值 `Service error`。
5. 最后用 `response.status(status).json(...)` 以 JSON 格式写回统一结构：业务 `code` 置为 `-1`，`data` 为 `null`，`msg` 为拿到的异常信息。

### 全局注册：用 useGlobalFilters

和响应拦截器一样，异常过滤器定义完必须注册才生效。这里有个很容易踩的坑：一开始若沿用 `useGlobalInterceptors` 会报错，因为过滤器有自己专属的 API：

```ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { AbnormalFilter } from './common/abnormal.filter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalFilters(new AbnormalFilter());
  await app.listen(3000);
}
bootstrap();
```

### 验证效果

打开浏览器请求一个不存在的接口，返回的就是我们自定义的结构：`code` 为 `-1`、`data` 为空、`msg` 是"没有找到对应接口"之类的提示。把注册那一行的 `useGlobalFilters` 注释掉再请求一次，响应立刻变回 NestJS 默认的 `statusCode / message / error` 结构。这个对比很直观：有没有全局异常过滤器，前端拿到的是两种完全不同的东西。

### 工程落点

在正式的《全栈多端低代码平台项目大课》工程里，响应拦截器与异常过滤器会一起放在 `packages/server` 的公共目录中，对所有后端接口生效。根工程 `代码（已8期）/代码（已8期）/8-5/lowcode/package.json` 通过 `run:server` 脚本（即 `pnpm --filter server run start:dev`）启动服务端；配套资料中的 `packages/server/nest-cli.json`、`tsconfig.json` 可对照查看工程配置。低代码平台里验证码、问卷提交等接口的错误返回，都依赖这一层统一约定。

## 小结

- 异常过滤器用于全局处理 HTTP 异常，统一修改后端返回给前端的错误信息。
- 它在 NestJS 里的正式名称是 Exception Filter，对应 `ExceptionFilter` 接口与 `@Catch()` 装饰器。
- `catch(exception, host)` 中通过 `host.switchToHttp().getResponse()` 拿到响应对象，再决定返回内容。
- 状态码取 `exception.getStatus()`，消息取 `exception.message`，缺省回退到 `Service error`。
- 注册必须用 `useGlobalFilters`，误用拦截器的 API 会报错。

## 下一步

建议接着看《项目初始化—接口响应和异常拦截器》，把响应拦截器与异常过滤器一起接入真实的项目初始化流程，看它们如何配合工作。之后建议接着看《Nest的管道Pipe转换》，继续补齐请求参数处理这一环。
