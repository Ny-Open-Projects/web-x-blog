---
title: "NestJS 初始化目录结构介绍"
date: 2026-11-17 19:12
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# NestJS 初始化目录结构介绍

> **导语**：用 Nest CLI 初始化项目后，根目录里一下子多出十几个文件和文件夹，很多人第一反应是「先别动，别改坏了」。本文逐一拆解这些目录的职责，再顺着 `main.ts` → `AppModule` → `Controller` → `Service` 的调用链，把 NestJS 处理一次请求的完整流程走一遍。读完后你不仅能看懂脚手架，还清楚业务代码该往哪里加。

## 前置知识

建议先读《Nestjs环境搭建和项目创建》，完成 Node.js、pnpm 与 Nest CLI 的安装，并初始化出第一个项目。另外需要了解 TypeScript 中 `class` 与装饰器（`@` 语法）的基本写法，以及 REST 接口里 GET / POST 的概念。

## 正文

### 顶层目录：区分「产物」与「源码」

项目根目录下最显眼的是四个文件夹：

- `dist/`：TypeScript 编译后的产物目录，部署时跑的就是这里，不需要手动维护。
- `node_modules/`：项目依赖，当前用到哪些依赖、插件、模块都会下载到这里。
- `src/`：日常开发的代码都放在这里，是唯一需要长期维护的源码目录。
- `test/`：端到端测试目录。相比 Express 脚手架，这是 NestJS 多出来的部分，用来模拟前端请求后端接口，验证接口是否生效、返回数据是否正确。

源码目录里还会自动生成 `app.controller.spec.ts`，它是 `app.controller.ts` 的单元测试文件；`package.json` 中的 `test`、`test:watch`、`test:e2e` 命令都可以直接跑。如果你只想用 Apifox 之类的工具请求接口，把这类测试文件删掉也完全没问题。

### 根目录配置文件各司其职

根目录散落的配置文件，各自承担一件小事：

- `.gitignore`：忽略哪些文件夹不纳入 Git 管理。
- `.prettierrc`：Prettier 格式化插件的配置。
- `nest-cli.json`：NestJS 框架自身的配置，`sourceRoot` 指向 `src`，编译时会先清空输出目录。
- `package.json`：项目依赖与版本声明，以及 `start:dev`、`build`、`test` 等脚本命令。
- `pnpm-lock.yaml`：pnpm 下载依赖后锁定的版本快照。
- `README.md`：项目说明。
- `tsconfig.json` 与 `tsconfig.build.json`：分别用于开发环境与生产构建的 TypeScript 配置。

其中 `pnpm-lock.yaml` 值得单独说。别人接手你的项目执行 `pnpm install` 时，会按这个文件还原出与你完全一致的版本。如果某个插件迭代很快、甚至大改版废弃了一批 API，没锁版本就装到新版，项目很可能直接跑不起来，排查起来也很费劲。

本大课后续演进为 pnpm workspace 多包工程，工作空间声明见 `代码（已8期）/代码（已8期）/8-2/lowcode/pnpm-workspace.yaml`：

```yaml
packages:
  - "packages/*"
```

### src 里的四个根文件与请求调用链

`src/` 下由脚手架生成的是「根」级别的四个文件，也就是应用主入口相关的那一套：

```ts
// src/main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
```

`main.ts` 是应用程序入口，定义异步函数 `bootstrap`，通过 `NestFactory.create(AppModule)` 创建应用，再 `listen(3000)` 监听端口。

`app.module.ts` 是根模块，也是 NestJS 应用的主要入口。它用 `@Module()` 声明这个模块挂了哪些控制器、哪些提供者：

```ts
@Module({
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

`app.controller.ts` 是根控制器，负责接收前端请求、接收参数，再调用 Service 执行业务逻辑；`app.service.ts` 用 `@Injectable()` 声明，是真正写注册、登录等业务逻辑的地方。控制器里一个典型的处理器长这样：

```ts
@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}
```

注意这里没有 `new AppService()`——实例由框架创建并通过构造函数注入，这正是依赖注入。至于 `@Controller()`、`@Get()`、`@Module()` 这些装饰器底层如何实现，有兴趣可以读 NestJS 源码，本课程不展开。

### 用 Nest CLI 一键生成业务模块

用户、课程这类业务如果每个模块都手写 controller / module / service 太繁琐，NestJS 提供了快捷命令：

```bash
nest g resource user
```

执行后选择 RESTful 风格，脚手架会自动生成 `user` 文件夹，里面 controller、module、service 一应俱全，还附带 DTO（接口入参校验）与 entities（数据库字段定义）。如果新模块里想复用 `AppService`，同样通过构造函数注入即可，前提是该服务已在对应模块中注册并导出。

## 小结

- `dist/` 是构建产物，`node_modules/` 是依赖，`src/` 是源码，`test/` 是 NestJS 相比 Express 多出的端到端测试目录。
- `pnpm-lock.yaml` 锁定依赖版本，是多人协作时「我这边能跑」的关键。
- 调用链是 `main.ts` 的 `bootstrap()` → `AppModule` → `AppController` 的 `@Get()` → `AppService` 的业务方法。
- 控制器只负责接请求与返结果，业务逻辑全部下沉到 Service。
- 用 `nest g resource <name>` 可一键生成完整的 RESTful 业务模块。

## 下一步

建议接着看《什么是装饰器和Nestjs中的应用》，把本篇反复出现的 `@Module()`、`@Controller()`、`@Get()` 彻底弄明白。想进一步提升脚手架使用效率，建议接着看《NestCli常用命令提高开发效率》，系统梳理 `nest g` 系列命令。
