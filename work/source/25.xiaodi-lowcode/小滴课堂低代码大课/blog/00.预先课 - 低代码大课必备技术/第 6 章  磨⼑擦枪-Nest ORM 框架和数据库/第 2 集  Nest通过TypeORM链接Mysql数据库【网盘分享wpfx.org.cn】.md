# NestJS 通过 TypeORM 连接 MySQL 数据库

> **导语**：低代码平台的服务端数据最终都要落到数据库里，连接配置是第一道门槛。本文把 NestJS 借助 TypeORM 打通 MySQL 的全过程拆开讲：安装哪些依赖、为什么把连接参数抽成独立的 `config.ts`、`TypeOrmModule.forRoot` 该怎么注册，以及「把 Docker 容器名当成数据库名」「漏装 mysql2 驱动」这两个几乎人人会踩的坑。读完后你可以独立写出一份可复用、能排错的连接配置。

## 前置知识

阅读本文前，建议先了解本课程已讲过的内容：

- 《安装Mysql数据库和可视化工具安装使用》：确保本机 MySQL 已启动，并能用可视化工具新建数据库。
- 《Nestjs环境搭建和项目创建》与《如何理解Nestjs的模块Module》：熟悉 NestJS 项目结构与根模块的 `imports` 写法。

此外需要基本的 TypeScript 与 pnpm 使用经验。

## 正文

### 连接配置为什么要单独成文件

TypeORM 的连接参数（数据库类型、地址、端口、账号、库名、实体扫描规则……）是一组相对独立、且多环境会复用的配置。把它集中放在一个 `config.ts` 里导出，再交给根模块读取，比散落在 `AppModule` 中更清晰。NestJS 封装 `@nestjs/typeorm` 提供了 `TypeOrmModuleOptions` 类型，正好用来给这份配置做类型约束，写错字段在编译期就能暴露出来。

### 安装依赖

要连上 MySQL，三样东西缺一不可：`typeorm` 本体、NestJS 的封装 `@nestjs/typeorm`，以及 MySQL 驱动 `mysql2`。前两者提供 ORM 能力与模块封装，后者才是真正与数据库建立连接的驱动——这一点在后面排查报错时会再强调。

本课程的工程是 pnpm workspace 多子项目结构，根 `package.json` 里通过 `--filter` 定位到 server 子项目启停：

```json
{
  "scripts": {
    "run:client": "pnpm --filter client run dev",
    "run:server": "pnpm --filter server run start:dev",
    "run:share": "pnpm --filter share run dev",
    "run:release": "pnpm --filter release run dev",
    "build:server": "pnpm --filter server run build",
    "start:server": "pnpm --filter server run start:prod"
  }
}
```

配套资料：`代码（已8期）/代码（已8期）/8-6/lowcode/packages/server/package.json`、`代码（已8期）/代码（已8期）/8-6/lowcode/pnpm-workspace.yaml`，可对照依赖与工作区声明。

### config.ts 里的关键字段

按本节演示整理，一份最小的连接配置包含这些字段（具体值以工程内 `config.ts` 为准）：

```ts
import { TypeOrmModuleOptions } from '@nestjs/typeorm';

export const typeOrmConfig: TypeOrmModuleOptions = {
  type: 'mysql',
  host: '127.0.0.1',
  port: 3306,
  username: 'root',
  password: '<安装 MySQL 时设置的密码>',
  database: '<可视化工具中新建的数据库名>',
  entities: ['**/*.entity{.ts,.js}'],
  autoLoadEntities: true,
  synchronize: true,
};
```

逐个说明：

- `type: 'mysql'`：声明数据库类型。
- `host` / `port`：本机地址 `127.0.0.1` 与默认端口 `3306`。
- `username` / `password`：本地默认 `root`，密码取安装 MySQL 时设置的值。
- `database`：要连接的库名，必须是真实存在的数据库。
- `entities`：扫描所有以 `.entity.ts` 或 `.entity.js` 结尾的实体文件，ORM 以这些类为蓝本建表。
- `autoLoadEntities: true`：自动加载各模块里通过 `forFeature` 注册的实体，不必在这里逐个手写。
- `synchronize: true`：把实体里定义的字段同步到数据库。开发阶段很方便——新增一个字段、重启项目，表结构就跟着更新；但它会直接改动表结构，生产环境通常不会开启。

### 在根模块里注册连接

配置写好后，在 `AppModule` 的 `imports` 中引入。导出的 `typeOrmConfig` 是一个普通对象而不是类，所以这里用的是 `TypeOrmModule.forRoot(...)` 这个静态方法调用，不要写成类名的形式：

```ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { typeOrmConfig } from './config';

@Module({
  imports: [TypeOrmModule.forRoot(typeOrmConfig)],
})
export class AppModule {}
```

保存后启动项目，控制台不再报连接错误，就说明链路已经打通。

### 两个高频报错与排查

**一、把容器名当成了数据库名。** 讲师本地用 Docker 桌面端跑 MySQL，界面里显示的名字其实是「容器名」，而不是真正的「数据库名」。第一次连接失败正是因为 `database` 填错了。正确做法：以可视化工具里新建数据库时填写的名字为准，容器名不作数。

**二、漏装 `mysql2`。** 改对库名后仍报「不能连接到数据库」，原因是只装了 ORM 相关依赖，没装 MySQL 驱动。补一条：

```bash
pnpm install mysql2
```

重新启动，连接成功。把这两点记进笔记，能省下大量来回试错的时间。

### 连接之后做什么

连接只是起点。有了 `synchronize`，实体类会被同步成真实的数据表；接下来定义实体字段，再通过控制器里的接口调用 TypeORM 去增删改查，比在接口里手写 SQL 更规整，也更容易维护。

## 小结

- 连接 MySQL 需要 `typeorm`、`@nestjs/typeorm`、`mysql2` 三者齐备，其中驱动最常被漏装。
- 连接参数抽成 `config.ts` 并用 `TypeOrmModuleOptions` 约束，根模块用 `TypeOrmModule.forRoot(...)` 注册。
- `entities` 扫描 `.entity.ts/.js` 文件，`autoLoadEntities` 自动加载，`synchronize` 把实体字段同步成表结构。
- `database` 填的是可视化工具里创建的库名，不是 Docker 容器名。
- `synchronize: true` 适合开发阶段，会直接改表结构，生产环境需谨慎。

## 下一步

连接打通后，下一集就会用实体去建表、并通过接口操作数据，建议接着看《TypeORM配置实体和操作数据库》。如果想系统补一遍 TypeORM 的配置思路，也可以看《TypeORM 框架-轻松掌握链接 Mysql 数据库配置》。
