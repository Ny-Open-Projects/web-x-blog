# NestJS 响应拦截器：用 Interceptor 统一接口返回格式

> **导语**：后端接口一多，返回给前端的数据格式就容易变成"各写各的"——有的接口返回一串字符串，有的返回一个结构完全不同的对象，前端每接一个接口都要单独写一套适配逻辑。本文带你用 NestJS 的响应拦截器（Interceptor）做一次全局收口，把成功响应统一成 `code / message / data` 结构。读完后你能独立写出 `ResponseInterceptor`，并在 `main.ts` 里全局注册让它真正生效。

## 前置知识

- 会创建 NestJS 项目、定义简单的 Controller 与 Service，并能请求一个返回字符串或对象的接口。
- 理解 RxJS 的 `Observable` 与 `pipe / map` 操作符，建议先阅读《掌握Rxjs和在Nest中的应用》。
- 了解 TypeScript 的 `implements` 接口实现与 `@Injectable()` 装饰器，建议先阅读《什么是装饰器和Nestjs中的应用》。

## 正文

### 为什么需要统一响应格式

在预先课的示例里，请求 `users` 接口拿到的是一串字符串，访问 `cos`（课程）相关接口时又是另一种结构。接口数量少的时候还能忍，一旦注册、登录、课程查询、课程创建等接口逐个铺开，前端就要针对每一种返回结构写一遍判断，联调成本陡增，也不利于接口文档的规范化。

更合理的做法是由后端做一次统一处理：所有接口对外只暴露同一种数据结构。这样前端只需要认一种格式，无论成功还是失败都能用同一套逻辑解析。

### 统一后的数据结构长什么样

一个常见的成功响应包含三部分：`code` 表示业务状态码（成功用 `0` 或 `200`，失败用 `400` 等），`message` 是给前端的提示文案，`data` 放真正的业务数据。比如登录或注册成功后要返回 `token`，就把它放进 `data`：

```json
{
  "code": 0,
  "message": "请求成功",
  "data": {
    "token": "eyJhbGciOi..."
  }
}
```

这只是其中一种约定，也可以精简成只有 `code` 加内容，关键是**所有接口保持一致**。除了包装格式，响应拦截器这个位置还适合顺带做响应数据格式化、加密、日志记录等横切逻辑——它们都属于"每个接口都要做、又不该写进业务代码"的事情。

### 实现 ResponseInterceptor

先在 `src` 下建一个 `common` 目录，把响应拦截器和后面要讲的异常过滤器都放在这里，便于统一管理全局切面。新建 `response.interceptor.ts`，导出一个类并实现 NestJS 提供的 `NestInterceptor` 接口：

```ts
import {
  CallHandler,
  ExecutionContext,
  Injectable,
  NestInterceptor,
} from '@nestjs/common';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable()
export class ResponseInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    return next.handle().pipe(
      map((data) => ({
        code: 0,
        data,
      })),
    );
  }
}
```

几个关键点：

- `NestInterceptor` 接口规定必须实现 `intercept(context, next)`，第一个参数是执行上下文，第二个参数 `next` 上有个 `handle()` 方法。
- `next.handle()` 返回的是一个 `Observable`，也就是前面 RxJS 里讲过的可观察对象，因此返回值要标注为 `Observable<any>`，否则会有类型警告。
- 用 `pipe` 配合 `map` 拿到控制器原本返回的 `data`，再包一层 `{ code, data }`。这里用了 ES6 的属性简写，`data` 既是属性名也是值。
- 类要用 `@Injectable()` 装饰，才能作为依赖注入的类被框架管理。

需要注意：如果 `intercept` 里拿到结果后忘了 `return`，运行时会报警告，因为拦截器没有把处理完的数据交回请求链路。

### 全局注册才会生效

拦截器定义好之后**必须使用才会生效**，这是很容易漏掉的一步。在 `main.ts` 里通过 `useGlobalInterceptors` 注册：

```ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ResponseInterceptor } from './common/response.interceptor';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalInterceptors(new ResponseInterceptor());
  await app.listen(3000);
}
bootstrap();
```

保存后重启项目，再刷新浏览器请求 `users` 接口，返回内容就从原来的字符串变成了带 `code` 和 `data` 的对象。若还想加 `message`，直接在 `map` 返回的对象里补一个字段即可，完全由项目自己定义。

### 放到低代码平台的工程语境里

预先课是在一个 NestJS 小项目里练手，而正式的《全栈多端低代码平台项目大课》工程采用 pnpm workspace 多包结构，服务端 NestJS 代码位于 `packages/server`。根工程 `代码（已8期）/代码（已8期）/8-5/lowcode/package.json` 里已经把各子项目的启动脚本收口好了：

```json
{
  "scripts": {
    "run:server": "pnpm --filter server run start:dev",
    "run:client": "pnpm --filter client run dev",
    "run:share": "pnpm --filter share run dev"
  }
}
```

也就是说，服务端通过 `pnpm --filter server run start:dev` 启动，全局拦截器最终会落在 `packages/server` 的公共目录里，对所有后端接口统一生效。配套资料中还包含 `packages/server/nest-cli.json`、`tsconfig.json` 等配置，可对照源码查看工程结构。低代码平台里图形验证码、短信验证码、问卷提交等大量接口，都依赖这一层统一格式来简化前端联调。

## 小结

- 响应拦截器本质是处理 HTTP 响应的切面，用统一方式收口后端返回给前端的数据。
- 统一格式能避免前端针对每个接口单独适配，常见结构为 `code / message / data`。
- `ResponseInterceptor` 实现 `NestInterceptor` 的 `intercept`，借助 RxJS 的 `map` 包装 `next.handle()` 的结果。
- 类需要 `@Injectable()` 装饰，并且必须在 `main.ts` 用 `useGlobalInterceptors` 注册，否则不生效。
- 除包装格式外，格式化、加密、日志记录等横切逻辑也适合放在这里。

## 下一步

建议接着看《Nest的异常拦截器》——响应拦截器只负责成功路径，异常过滤器负责把错误也收敛成同一种格式，两者配合才算把接口返回彻底统一。之后建议接着看《项目初始化—接口响应和异常拦截器》，看这两个全局切面如何真正接入低代码平台工程。
