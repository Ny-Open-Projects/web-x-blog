---
title: "NestCli常用命令提高开发效率"
date: 2026-11-17 09:37
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# NestCli常用命令提高开发效率

> **导语**：手写 Module、Controller、Service 的装饰器与 import 既枯燥又容易漏，NestJS 自带的脚手架 Nest CLI 就是来解决这件事的。本文从 `nest --help` 出发，梳理 `nest g` 系列常用指令与别名，重点讲清 `nest g resource` 一次性生成的 RESTful 资源结构，并顺带记录接口调试时动态路由抢占路径的坑。掌握这些命令，后面每开一个新业务模块都能省下大把重复劳动。

## 前置知识

需要先能跑起一个 NestJS 工程，建议先看过《Nestjs环境搭建和项目创建》与《Nestjs初始化目录结构介绍》，理解 `src` 下 `app.module.ts`、`app.controller.ts`、`app.service.ts` 各自的作用；再配合《如何理解Nestjs的模块Module》和《什么是装饰器和Nestjs中的应用》，才能看懂 CLI 自动生成的装饰器代码在做什么。有 Angular 经验的同学会发现这套 generate 指令非常眼熟。

## 正文

### 先看有哪些指令：`nest --help`

在项目终端执行 `nest --help`，会打印出脚手架支持的全部命令及对应别名。表格里左侧是名字、右侧是快捷指令，比如 `generate` 简写为 `g`，`module` 简写为 `mo`，`controller` 简写为 `co`，`service` 简写为 `s`。记别名比记全名快得多，日常开发基本只用简写。

注意这里说的是 **NestJS 框架的 Nest CLI**，不是前端 Next.js 的脚手架；按 NestJS 基础知识这一章的上下文应统一理解为 Nest CLI。

### 为什么要分模块

默认工程只有一个 `AppController`，但真实项目里接口动辄几十上百个，不可能全塞进同一个控制器。合理做法是按业务域拆分：用户相关归 `user` 模块，课程相关归 `course` 模块，每个模块自带自己的 Module、Controller、Service、DTO 与 entities。CLI 的 generate 指令正是为这种目录结构服务的——它不只建文件，还会顺手把新模块注册到根模块的 `imports` 数组里。

### 逐个生成：module / controller / service

三条基础指令可以分开用：

- `nest g module user`：在 `src` 下生成 `user/user.module.ts`，并自动把 `UserModule` 加进 `app.module.ts` 的 `imports`，省去手写 `@Module` 装饰器与 import。
- `nest g controller user`（或 `nest g co user`）：生成 `user.controller.ts`，同时在该模块里注册好 Controller。
- `nest g service user`（或 `nest g s user`）：生成 `user.service.ts`，类上带好 `@Injectable()` 装饰器。

这样生成出来的文件是干净的骨架，接着往里写接口就行。缺点是三件套要敲三次，而且不带任何示例接口，仍要自己从零写方法。

### 一步到位：`nest g resource`

想一次拿到完整 CRUD 骨架，用 `nest g resource user`。执行后会先让你选风格，一般选 **REST API**（RESTful API），确认后生成 `users` 目录，里面是一整套可直接运行的结构：

- `users.module.ts`：模块定义，与根模块写法一致，负责引入 Controller 与 providers。
- `users.controller.ts`：控制层，已经写好一组示例接口——`GET` 列表、带 `:id` 的 `GET` 详情、`POST` 新增、`PATCH` 更新、`DELETE` 删除，装饰器齐全，这就是一套标准的 RESTful API。
- `users.service.ts`：服务层，与控制层一一对应，提供 `create`、`findAll`、`findOne`、`update`、`remove` 等示例方法。
- `dto/create-user.dto.ts`、`dto/update-user.dto.ts`：入参校验用的 DTO，`CreateUserDto`、`UpdateUserDto` 会被 Service 引用。
- `entities/user.entity.ts`：实体，用来声明用户表有哪些字段、字段是什么属性，数据库操作都围绕它展开。
- 以及 `*.spec.ts` 测试文件（端到端测试在脚手架 `test/` 目录，此处不涉及），暂不涉及可先放着。

再执行 `nest g resource course`，同样选 REST API 风格，就会得到课程模块的 Module、Controller、Service、DTO 与 entity，`CourseModule` 也会自动注册进 `app.module.ts`。后续写业务时不必再手工 import，直接在这些骨架里填逻辑即可。这里出现的 DTO 与 entities，正是后面《Nest的管道验证DTO》和 TypeORM 实体章节要展开的内容。

### 联调踩坑：动态路由抢了 `/user`

生成完想验证接口，先 `pnpm start:dev` 启动项目，再用接口调试工具发请求。这里有个很典型的坑：如果原来的 `app.controller.ts` 里留着一个 `@Get(':id')` 动态路由，直接请求 `/user` 会先被它命中，把 `user` 当成 `:id` 参数，返回的自然是旧逻辑而不是 `UsersController.findAll()` 的结果。

给主控制器加一个固定前缀（例如 `app`）把两条路径区分开，重启服务后再请求 `/user`：GET 返回 `This action returns all users`，改成 POST 则返回 `This action adds a new user`，说明请求已经正确落到新生成的控制器上。热更新偶尔不及时，必要时重启一次服务再测。其他方法按同样方式切请求方法即可逐一验证。

### 关联工程配置

本阶段的工程同样是 pnpm workspace 多包结构，根目录 `代码（已8期）/代码（已8期）/8-3/lowcode/package.json` 用 `pnpm --filter ...` 统一调度各子包：

```json
{
  "name": "lowcode",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "run:client": "pnpm --filter client run dev",
    "run:server": "pnpm --filter server run start:dev",
    "run:share": "pnpm --filter share run dev",
    "run:release": "pnpm --filter release run dev",
    "build:client": "pnpm --filter client run build",
    "build:server": "pnpm --filter server run build",
    "build:release": "pnpm --filter release run build",
    "build:share": "pnpm --filter share run build",
    "start:server": "pnpm --filter server run start:prod",
    "start:release": "pnpm --filter release run start"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "@types/lodash": "^4.14.201",
    "@types/node": "18",
    "@types/react": "^18.2.37",
    "@types/react-dom": "^18.2.15",
    "typescript": "^5.2.2"
  },
  "dependencies": {
    "@ant-design/icons": "^5.2.6",
    "antd": "^5.11.2",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

配套的 `packages/server/nest-cli.json`（见 `8-4/lowcode/packages/server/` 目录）是 Nest CLI 的工程配置，`packages/client/tsconfig.json` 则约束前端的编译选项。generate 指令要在 `server` 子包的工程根目录执行，生成的文件才会落进正确位置。

## 小结

- `nest --help` 查看全部命令与别名：`g`=generate、`mo`=module、`co`=controller、`s`=service。
- 按业务域拆分模块，避免把所有接口堆在 `AppController` 里；CLI 会自动把新模块注册进根模块。
- `nest g module/controller/service` 逐个生成骨架，但不带示例接口。
- `nest g resource` 选 REST API 风格可一次生成 module、controller、service、dto、entities 与测试文件，含完整 CRUD 示例。
- 联调时留意旧控制器里的 `:id` 动态路由会抢占 `/user`，加固定前缀或重启服务后再验证。

## 下一步

生成出来的那一组 GET/POST/PATCH/DELETE 示例接口正是下一节的主角，建议接着看《NestjsRESful风格API开发》，把这些接口逐个调一遍、弄清 RESTful 的方法语义。之后可以顺着《Nest的管道验证DTO》把 DTO 校验补齐，再用《TypeORM配置实体和操作数据库》把 entities 与真实表结构接起来。
