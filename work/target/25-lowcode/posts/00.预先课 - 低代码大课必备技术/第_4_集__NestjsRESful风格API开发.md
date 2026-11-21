---
title: "NestJS RESTful 风格 API 开发"
date: 2026-11-17 10:04
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# NestJS RESTful 风格 API 开发

> **导语**：RESTful 到底是什么？为什么说它是「风格」而不是标准？本文从日常用 GET / POST 写接口的方式讲起，对比 RESTful「同一路径 + 不同 HTTP 方法」的做法，用 Nest CLI 生成的控制器把 `@Get` / `@Post` / `@Patch` / `@Delete` 与动态路由串起来，最后补上接口版本控制（URI 版本）的两种写法。即便实战项目不采用 RESTful，这套认知也能帮你读懂大部分公开 API。

## 前置知识

- 建议先了解《详解Nestjs控制器《上》》与《Nestjs提供Get和Post请求》，熟悉 NestJS 控制器与方法装饰器。
- 建议先了解《NestCli常用命令提高开发效率》，本文的控制器骨架正是由 CLI 快捷命令生成。

## 正文

### RESTful 是一种风格，不是标准

RESTful API 首先是一种**设计风格**，既不是标准也不是协议。日常开发后端接口，前端请求时主要用 GET 和 POST 两种方法就够了；但如果后端采用了 RESTful 风格，前端就得按对应的 HTTP 方法去请求。实际项目里并不强制遵循，理解它的意义更多在于能读懂别人设计的接口。

### 常规写法：一个功能一个路径

平时我们习惯给每个功能单独起路径：

- 注册：`POST /api/user/register`，把账号、密码、图形验证码、短信验证码等敏感信息放进请求体，不暴露在 URL 上。
- 删除：路径里带 `delete`，用 POST 或 GET 把用户 ID 传给后端。
- 修改：路径里带 `update`，传用户 ID 以及要改的昵称、简介等字段，常用 POST。
- 查询：路径里带 `find`，用 GET 请求。

以小滴课堂官网为例，网络面板里能看到 `GET /api/account/v1/detail` 用于查用户信息，修改资料后则发起 `POST /api/account/v1/update`，随后重新请求详情接口刷新页面数据。这是「四个功能、四个路径」的典型写法。

### RESTful 写法：同一路径，换 HTTP 方法

RESTful 把增删改查收敛到**同一个接口路径**，靠 HTTP 方法区分动作：

| 动作 | 方法 |
| --- | --- |
| 查询 | GET |
| 新增 | POST |
| 更新 | PUT 或 PATCH |
| 删除 | DELETE |

也就是说，前端不再换路径，只换 `get` / `post` / `patch`（或 `put`）/ `delete` 就能对同一资源完成不同操作。

### 控制器里的五个方法

上一节用 Nest CLI 快捷命令生成了 `user` 与 `course` 模块，打开 `user.controller.ts` 能看到 RESTful 骨架：

```ts
import {
  Controller, Get, Post, Patch, Delete, Param,
} from '@nestjs/common';

@Controller('user')
export class UserController {
  @Post()
  create() { /* 创建新用户 */ }

  @Get()
  findAll() { /* 查询全部用户 */ }

  @Get(':id')
  findOne(@Param('id') id: string) { /* 按 ID 查单个 */ }

  @Patch(':id')
  update(@Param('id') id: string) { /* 更新指定用户 */ }

  @Delete(':id')
  remove(@Param('id') id: string) { /* 删除指定用户 */ }
}
```

几个要点：

- 五个方法都挂在同一个 `@Controller('user')` 下，路径相同、方法不同。
- `@Get(':id')`、`@Patch(':id')`、`@Delete(':id')` 用的是**动态路由**：把 ID 拼在路径上（如 `/user/1`），而不是 `?id=1` 这种查询参数，两者不要混用。
- `@Patch` 更新完成后给前端返回修改成功的结果；删除时同样靠路径里的 ID 定位。

### 实战里的取舍

讲师明确表态：实战开发**不采用 RESTful**，直接用 GET 和 POST 就够了——每个动作都要重新设计同一资源的多种方法，确实累。这一节的价值是建立概念，知道「什么叫 RESTful」，以及别人给你一份 RESTful 接口文档时怎么读。

### 接口版本控制：URI 版本

官网接口里的 `v1` 就是版本控制。第一版是 v1，迭代后改成 v2，和 App 版本更新的道理一样。NestJS 里开启方式很简单，在 `main.ts` 调用：

```ts
import { VersioningType } from '@nestjs/common';

app.enableVersioning({ type: VersioningType.URI });
```

`VersioningType.URI` 表示把版本号放在 URI 里。接着在控制器上声明：

```ts
@Controller({ path: 'user', version: '1' })
export class UserController {}
```

此时要请求 `GET /v1/user` 才能命中，返回 CLI 生成的默认字符串 `This action returns all users`。用 ApiFox 测试时会提示「返回数据结构校验失败、不是 JSON」，因为返回的是字符串，这属于测试工具的格式要求，不影响接口本身。

如果只想给**某个方法**加版本，用方法级装饰器 `@Version('1')`（注意首字母大写 `V`，从 `@nestjs/common` 引入）即可：

```ts
@Get()
@Version('1')
findAll() { /* 仅此方法需要 /v1/user */ }
```

去掉路径里的 `v1` 就请求不到这个方法；而未加版本的其他方法（比如 POST）不受影响，仍按原路径正常返回 `This action adds a new user`。控制器级与方法级两种粒度，按需要选用。

### 工程配置一览

本节的 monorepo 根配置里，各子项目通过 `--filter` 启停，公共的 TypeScript 与类型声明统一放在根 `devDependencies`：

```json
{
  "name": "lowcode",
  "scripts": {
    "run:client": "pnpm --filter client run dev",
    "run:server": "pnpm --filter server run start:dev",
    "build:server": "pnpm --filter server run build",
    "start:server": "pnpm --filter server run start:prod"
  },
  "devDependencies": {
    "@types/lodash": "^4.14.201",
    "@types/node": "18",
    "@types/react": "^18.2.37",
    "@types/react-dom": "^18.2.15",
    "typescript": "^5.2.2"
  }
}
```

配套资料：`代码（已8期）/代码（已8期）/8-3/lowcode/packages/client/tsconfig.json`、`代码（已8期）/代码（已8期）/8-4/lowcode/packages/server/package.json`、`代码（已8期）/代码（已8期）/8-4/lowcode/packages/server/nest-cli.json`。

## 小结

- RESTful 是风格而非标准/协议；常规项目用 GET + POST 即可，实战中不强制采用。
- 常规写法是「一个功能一个路径」，RESTful 是「同一路径 + 不同 HTTP 方法」：GET 查、POST 增、PUT/PATCH 改、DELETE 删。
- NestJS 用 `@Get` / `@Post` / `@Patch` / `@Delete` 声明方法，`@Get(':id')` 是路径拼接的动态路由，区别于查询参数。
- 版本控制在 `main.ts` 用 `app.enableVersioning({ type: VersioningType.URI })` 开启，可用 `@Controller({ version: '1' })` 或方法级 `@Version('1')`。
- 加了版本后必须请求 `/v1/user`，未加版本的方法不受影响。

## 下一步

理解接口形态后，接下来要处理「请求进来之后怎么校验和转换」，建议接着看《Nest的管道Pipe转换》与《Nest的管道验证DTO》，把控制器里的参数处理链路补齐。
