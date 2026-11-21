# 项目初始化：安装配置 TypeORM 与 MySQL 并自动同步实体

> **导语**：项目进入初始化阶段，第一件要打通的事就是持久层——让 NestJS 能连上 MySQL，并用代码里的实体自动建表。本文按"装依赖 → 写配置 → 主模块注册 → 定义实体 → 验证自动同步"的顺序讲清楚 TypeORM 的接入过程，并重点强调一个高频误区：`database` 填的是数据库名，不是 Docker 容器名。读完你能独立跑通一次实体到数据表的同步。

## 前置知识

- 本地或 Docker 中已安装好 MySQL，了解 `host / port / username / password / database` 各自的含义，建议先阅读《安装Mysql数据库和可视化工具安装使用》。
- 熟悉 NestJS 的模块与 `imports` 写法，建议先阅读《Nestjs初始化目录结构介绍》与《Nest通过TypeORM链接Mysql数据库》。
- 会用可视化工具（如 Navicat）查看数据库与表，会用 Docker 的基本查看命令。

## 正文

### 安装依赖：typeorm、mysql2 与 @nestjs/typeorm

先另起一个终端窗口安装依赖，不用停掉正在运行的项目：

```bash
pnpm add @nestjs/typeorm typeorm mysql2
```

这里三个包各有分工：`typeorm` 是 ORM 本体，`mysql2` 是 MySQL 驱动，`@nestjs/typeorm` 则是把 TypeORM 接进 NestJS 依赖注入体系的桥接模块。课上先装了前两个，写到主模块时发现还差桥接模块，于是补装——按这个一次性装齐即可。

### 用 Docker 与可视化工具确认 MySQL

配置之前先确认数据库实例确实在。除了可视化工具，也可以用 Docker 命令查看当前运行的容器、所有容器以及本地已拉取的镜像：

```bash
docker ps
docker ps -a
docker images
```

Docker Desktop 的好处是这些状态可以直接在界面里看到，不必逐个敲命令。本章默认是连接本地自行安装的 MySQL，也可以用容器化方式安装，两种方式对后面的配置没有区别。

### 编写 TypeORM 配置

在 `src` 下新建 `config.ts`（或 `config/index.ts`），把连接配置集中放一处：

```ts
import { TypeOrmModuleOptions } from '@nestjs/typeorm';

export const TypeOrmConfig: TypeOrmModuleOptions = {
  type: 'mysql',
  host: 'localhost',
  port: 3306,
  username: 'root',
  password: 'your password',
  database: 'nest',
  entities: [__dirname + '/**/*.entity{.ts,.js}'],
  synchronize: true,
};
```

逐项说明：

- `type` 指定为 `mysql`，`host` 为本地地址，端口、用户名（`root`）、密码按本机实际情况填写。
- **`database` 是数据库名，不是容器名**。比如用 Docker 装 MySQL 时容器可能叫 `class_nest`，但这里要填的是创建数据库时起的那个库名，两者不能混。这是最容易配错的一项。
- `entities` 告诉 TypeORM 去哪里找项目里的实体文件，找到后才知道要同步哪些表。
- `synchronize` 开启后，实体结构会自动同步到数据库，开发阶段非常省事。

### 在主模块注册 forRoot

打开 `app.module.ts`，把配置通过 `TypeOrmModule.forRoot` 注入：

```ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { TypeOrmConfig } from './config';

@Module({
  imports: [TypeOrmModule.forRoot(TypeOrmConfig)],
})
export class AppModule {}
```

`forRoot` 是 `@nestjs/typeorm` 提供的静态方法，进入源码还能看到另外几种配置方式，初学阶段先用这一种即可。顺便把脚手架自带、这里用不上的 `app.controller.ts` 与 `app.service.ts` 删掉，模块更干净。

### 定义实体并验证自动建表

此时重启项目、刷新数据库，是不会凭空多出表的——因为实体还没定义，TypeORM 不知道该建什么表、什么字段。接下来定义 `user` 与 `course` 两个实体：

```ts
import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  username: string;

  @Column()
  password: string;

  @Column()
  headImage: string;
}
```

要点：`@Entity()` 是类装饰器，把类标记成一张表；`id` 用 `@PrimaryGeneratedColumn()` 保证每条数据的唯一性；其余字段用 `@Column()` 逐个声明。`course` 实体同理，字段包括 `id`、`title`、`courseImage`、`price`、分数、分类以及是否删除的标记位。

启动命令走的是 `start:dev`，会监听代码改动并热更新重启。在根工程 `代码（已8期）/代码（已8期）/9-1/lowcode/package.json` 里，服务端脚本已经收口成：

```json
{
  "scripts": {
    "run:server": "pnpm --filter server run start:dev"
  }
}
```

验证方法：先在可视化工具里把旧表删掉，保存任意一个实体文件触发热重启，再刷新数据库——`user` 和 `course` 两张表会自动出现，字段与装饰器里声明的一一对应。想再确认一次，就删表、重启、再看，结果一致说明 `synchronize` 确实生效了。

### 对比 Sequelize

讲师在结尾提到，相比之前用过的 Sequelize，这套写法更简单。原因主要在于 TypeORM 用装饰器描述实体，表结构直接长在 TypeScript 类上，再配合 NestJS 的依赖注入，和框架风格天然贴合，不必在模型定义与框架接入之间来回切换。

## 小结

- 依赖三件套：`typeorm`（ORM）、`mysql2`（驱动）、`@nestjs/typeorm`（NestJS 桥接）。
- 配置的 `database` 填数据库名，绝不是 Docker 容器名，这是最常见的配置错误。
- `entities` 指向实体文件，`synchronize: true` 负责把实体结构自动同步到数据库。
- 主模块用 `TypeOrmModule.forRoot(TypeOrmConfig)` 注册，并清理无用的脚手架文件。
- 实体靠 `@Entity()`、`@PrimaryGeneratedColumn()`、`@Column()` 描述，保存后经 `start:dev` 热重启即可自动建表。

## 下一步

持久层打通后，建议接着看《项目初始化—接口响应和异常拦截器》，把前面学过的响应拦截器与异常过滤器一并接入这个初始化好的项目。若想更深入地掌握实体与表结构的映射，建议接着看《TypeORM配置实体和操作数据库》。
