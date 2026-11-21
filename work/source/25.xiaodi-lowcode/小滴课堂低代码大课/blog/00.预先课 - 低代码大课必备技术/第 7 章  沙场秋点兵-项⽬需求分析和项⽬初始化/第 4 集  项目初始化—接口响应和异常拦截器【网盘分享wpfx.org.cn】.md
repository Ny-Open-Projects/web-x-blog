# 项目初始化：把响应拦截器与异常过滤器接入工程

> **导语**：预先课里我们已经分别写过响应拦截器和异常过滤器，这一节要做的是把它们搬进正式初始化的项目，并在 `main.ts` 里全局注册、逐一验证效果。内容不难，但藏着几个真实会踩的坑：RxJS 依赖的警告怎么处理、两个注册 API 别用错、以及"类必须实例化才能传进去"。读完后你能让所有接口的成功与失败响应都收敛到同一套格式。

## 前置知识

- 已经理解《Nest的响应拦截器》与《Nest的异常拦截器》的实现原理。
- 已完成《项目初始化—安装配置TypeORM和Mysql》，项目能正常启动并有可请求的接口。
- 了解 RxJS 的 `Observable`、`pipe`、`map`，建议先阅读《掌握Rxjs和在Nest中的应用》。

## 正文

### 建公共目录，把两个文件搬进来

拦截器属于全局公共逻辑，所以在 `src` 下新建 `common` 目录，把预先课写好的两个文件放进去：`response.interceptor.ts`（响应拦截器）和 `abnormal.filter.ts`（异常过滤器）。代码与预先课一致，直接复用即可，不必重写。

搬进来后先补齐依赖。这里 `@nestjs/common`、`rxjs` 都是框架自带或随依赖安装的，若编辑器仍提示 RxJS 找不到，多半是类型服务没刷新：用 VS Code 的 `Developer: Reload Window` 重新加载窗口（Mac 上 `Command + Shift + P` 后搜索即可），不用退出再打开，警告就会消失。

### 响应拦截器的代码复盘

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
      map((data) => ({ code: 0, data })),
    );
  }
}
```

按执行顺序读一遍：`@Injectable()` 把类纳入依赖注入；类实现 `NestInterceptor` 接口，因此必须提供 `intercept(context, next)`，其中 `context` 是执行上下文，`next` 代表下一个处理器。调用 `next.handle()` 拿到 `Observable`，再用 `pipe` 操作符做管道处理——这一步有点像 Express 里把数据转成 stream 流来处理——管道里用 `map` 操作符（同样从 `rxjs` 引入）把每条数据映射成一个新对象 `{ code, data }`。返回值类型是 `Observable<any>`，别漏写，否则会有类型警告。

### 异常过滤器的代码复盘

```ts
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

它实现 `ExceptionFilter` 接口并调用 `catch(exception, host)`：先由 `host.switchToHttp()` 拿到请求上下文，再 `getResponse()` 取得 response 对象，才能对返回数据做处理。状态码取 `exception.getStatus()`，异常信息取 `exception.message`；如果业务 service 返回的数据里没有带 `message`，就统一回退到 `Service error`，有则原样返回给前端。

### 在 main.ts 注册：两个 API，别用错

两个切面都要在 `main.ts` 注册，而且**用的是不同的 API**：

```ts
import { ResponseInterceptor } from './common/response.interceptor';
import { AbnormalFilter } from './common/abnormal.filter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalInterceptors(new ResponseInterceptor());
  app.useGlobalFilters(new AbnormalFilter());
  await app.listen(3000);
}
bootstrap();
```

- `useGlobalInterceptors` 注册响应拦截器，统一正常返回数据的格式；
- `useGlobalFilters` 注册异常过滤器，统一错误返回数据的格式。

这里有个高频报错：直接把类名 `ResponseInterceptor` / `AbnormalFilter` 传进去会提示"不存在"，因为它们是类，需要 `new` 实例化后再传入。写成 `new ResponseInterceptor()`、`new AbnormalFilter()` 即可。

### 验证效果

重启项目后依次请求三个场景：

1. 请求 `cos`（课程）接口，返回对象里带上了 `code` 与 `data`，不再是裸数据；
2. 请求 `user` 接口，格式一致；
3. 访问一个不存在的路径（如 `/aa`），返回的是异常过滤器里约定的 `code: -1`、`data: null`、`msg` 错误提示。

成功与失败都走同一套约定，前端解析逻辑就能只写一份。这一步做完，项目初始化的"接口规范层"就补齐了。

### 工程落点

在《全栈多端低代码平台项目大课》的 pnpm workspace 工程里，这两个文件最终位于 `packages/server` 的公共目录，对所有后端接口生效。根工程 `代码（已8期）/代码（已8期）/9-1/lowcode/package.json` 的脚本把服务端启动与构建都收口好了：

```json
{
  "scripts": {
    "run:server": "pnpm --filter server run start:dev",
    "build:share": "pnpm --filter share run build"
  }
}
```

`run:server` 对应热更新启动，`build:share` 用于构建公共类型子项目——低代码平台里前后端共用的类型都放在 `share` 包中。配套资料可参考 `packages/server/tsconfig.json`、`nest-cli.json` 等配置。

## 小结

- 把预先课的两个切面文件放进 `src/common`，依赖以框架自带为主，RxJS 类型警告可用 Reload Window 解决。
- 响应拦截器实现 `NestInterceptor`，靠 `next.handle().pipe(map(...))` 包装成功数据。
- 异常过滤器实现 `ExceptionFilter`，靠 `host.switchToHttp().getResponse()` 写回错误结构。
- 注册用 `useGlobalInterceptors` 与 `useGlobalFilters` 两个不同 API，且必须传入 `new` 出来的实例。
- 验证要覆盖正常接口与不存在的路径，确认成功、失败都符合统一格式。

## 下一步

讲师在结尾已经点明：接下来继续做项目初始化中的 DTO 验证。建议接着看《项目初始化—接口参数DTO验证》，把请求参数的校验也收敛到框架层；若想先补理论，建议接着看《Nest的管道验证DTO》。
