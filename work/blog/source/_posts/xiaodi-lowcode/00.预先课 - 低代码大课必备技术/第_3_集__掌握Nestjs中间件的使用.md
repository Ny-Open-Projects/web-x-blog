---
title: "掌握 NestJS 中间件的使用"
date: 2026-11-17 02:59
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# 掌握 NestJS 中间件的使用

> **导语**：中间件决定了"请求到达 handler 之前和之后能做什么"。本文用一条珍珠奶茶管道讲清中间件的本质，再落地到 NestJS 的三类用法：类中间件 + MiddlewareConsumer 注册、函数式全局中间件、以及第三方 cors 中间件。读完你能独立完成鉴权白名单、按方法/路径精细限制，以及跨域配置，并避开 next() 漏调、send 写成 render 这类高频坑。

## 前置知识

中间件要挂在模块上，建议先读《如何理解Nestjs的模块Module》熟悉 @Module 与 NestModule 的 configure；Controller 与路由装饰器可参看《Nestjs提供Get和Post请求》。若此前学过 Express，其 (req, res, next) 心智模型可以直接迁移过来。

## 正文

### 中间件是什么：一条珍珠奶茶管道

定义很朴素：在请求到达处理程序之前或之后，对请求和响应做一些处理，和 Express 的中间件是同一个意思。典型用途包括身份验证（很多接口要求携带合法 token 才能访问，可在 JWT 校验层统一处理）、日志记录、数据转换等。

讲师用了一个很生动的比喻：把一次接口请求想象成一根管道，里面流动的是牛奶（原始请求）；中途加"珍珠"的环节是一个中间件，加"茶叶"的是另一个中间件，还有像仪表一样记录流速、压力的中间件（对应日志与监控）；走到末端封装出来的珍珠奶茶，就是最终响应。这个管道既可以在入口处加料（请求前处理），也可以在出口处封装（响应后处理）。

### 自定义类中间件：implements NestMiddleware

新建 src/middleware/test.ts，导出一个实现 NestMiddleware 接口的类。注意这里是 implements（实现接口），不是 extends（继承类）：接口只约束"必须有哪些成员"，类里要自己把 use 方法补齐，这和继承一个现成类拿到其属性方法完全不同。

use 方法接收三个参数，类型都从 express 引入：req: Request、res: Response、next: NextFunction。逻辑写完后必须调用 next()，否则请求会停在这一层不再向下走——演示里把 next() 注释掉后，浏览器请求一直卡顿无响应；改成 res.send('被拦截了') 则直接返回拦截提示。

```ts
import { NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

export class Test implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    console.log('测试中间件执行了');
    next(); // 不调用 next 则请求被拦截，不会继续向下走
  }
}
```

### 在模块里注册：MiddlewareConsumer 的三种粒度

中间件要生效，需在目标模块实现 NestModule 接口并写 configure(consumer: MiddlewareConsumer)，这是固定写法：

```ts
@Module({ /* ... */ })
export class UserModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(Test).forRoutes('user');
  }
}
```

consumer.apply(...).forRoutes(...) 支持三种限制粒度：

1. 传字符串路径：forRoutes('user')，命中整个用户路径下的接口。演示中访问 course 路径仍能正常返回，说明只有 user 模块挂了中间件。
2. 传对象限定路径 + 方法：forRoutes({ path: 'user/find', method: RequestMethod.GET })，只让某个接口的某种方法走中间件。演示里 GET 被拦截，而用 Apifox 发的 POST 正常放行。
3. 直接传 Controller：forRoutes(UserController)，把该控制器下所有接口一次性纳入。

演示时还遇到一个干扰项：控制器里另有一条动态路由，导致直接传 Controller 的写法看似没生效，注释掉动态路由后就按预期拦截了。排查这类问题，先把路由表理清往往比反复改中间件更快。

### 函数式全局中间件：白名单与 token 校验

类中间件适合模块级复用；若要对全站生效，可在 main.ts 里写一个函数式中间件，用 app.use(...) 挂载，和 Express 完全一致。函数同样接收 (req, res, next)，通过 req.originalUrl 拿到请求路径，再与白名单数组比对：命中则 next() 放行，否则 res.send('user 接口才能请求')。

```ts
const passPaths = ['user'];
app.use((req: Request, res: Response, next: NextFunction) => {
  console.log('全局中间件执行了', req.originalUrl);
  if (passPaths.some((p) => req.originalUrl.includes(p))) {
    next();
  } else {
    res.send('user 接口才能请求');
  }
});
```

有两个值得记下的坑：一是误把 res.send 写成 res.render，导致报 500、找不到 render 方法——报错时要回头逐字核对逻辑；二是演示用了浏览器缓存，注释掉配置后请求仍"成功"，换无痕窗口才复现真实结果。真实项目中这个判断条件通常不是路径白名单，而是校验请求是否携带 token、token 是否合法，合法才放行需要权限的接口。

### 第三方中间件与框架自带跨域

跨域（CORS）可以用第三方中间件解决：`pnpm add cors` 安装后，在 main.ts 里引入并执行 app.use(cors())。复现跨域的方式是在另一个站点页面的控制台里用 fetch 请求本地 http://localhost:3000 接口——协议、域名、端口任一不同即触发跨域报错，返回数据还要经 .json() 转换后再读取。

NestJS 也自带等价能力，无需装包，直接调用 app.enableCors() 即可。演示中两种方式都验证通过（记得用无痕窗口排除缓存干扰）。选型上，需要细粒度配置时第三方 cors 更灵活，简单放行用框架自带的一行调用就够。

### 配套工程

本篇示例工程同样是 pnpm workspace 多包仓库，根目录 scripts 用 `pnpm --filter` 驱动各子包（见 `代码（已8期）/代码（已8期）/8-4/lowcode/package.json`），client 子包基于 Vite + React + TypeScript（见同目录 `packages/client/package.json`、`tsconfig.json`）。中间件代码位于 server 子包的 src 下，与模块、控制器放在一起便于管理。

## 小结

- 中间件在请求前/后对 req、res 做处理，用途涵盖鉴权（JWT/token）、日志、数据转换；珍珠奶茶管道是理解链式处理的好类比。
- 类中间件用 implements NestMiddleware + use(req, res, next)，类型来自 express，implements 与 extends 语义不同。
- next() 必须调用，否则请求被拦截卡住；可用 res.send 主动返回拦截提示。
- 模块级注册靠 NestModule.configure + MiddlewareConsumer.apply().forRoutes()，支持路径字符串、{ path, method } 对象、Controller 三种粒度。
- 全站用 main.ts 里的函数式中间件 app.use(...)，可基于 req.originalUrl 做白名单，实际项目多改为 token 校验；注意 send 而非 render、无痕窗口排除缓存。
- 跨域可选第三方 cors（app.use(cors())）或框架自带 app.enableCors()。

## 下一步

中间件之后，NestJS 还有几层"请求处理链"值得补齐。建议接着看《Nest的响应拦截器》，学习统一包装响应结构；再看《Nest的异常拦截器》处理错误返回，以及《Nest的管道Pipe转换》与《Nest的管道验证DTO》做参数转换与校验。它们与中间件共同构成从请求进入到响应返回的完整管线。
