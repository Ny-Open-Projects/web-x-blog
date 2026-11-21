# TypeORM 配置实体和操作数据库

> **导语**：连接建立之后，真正让数据「活起来」的是实体与 CRUD。本文用一张 User 表贯穿全程：用 `@Entity` / `@Column` 把类映射成表，用 `TypeOrmModule.forFeature` 注册实体、`@InjectRepository` 注入 `Repository`，再用 `save` / `delete` / `update` / `find` 跑通增删改查，并说明 `synchronize` 自动建表背后的机制与启动顺序的坑。

## 前置知识

- 建议先了解《Nest通过TypeORM链接Mysql数据库》与《如何理解Nestjs的提供者Providers》，前者保证连接已打通，后者是依赖注入的基础。
- 需要 NestJS 控制器、依赖注入的基本概念，以及 TypeORM 中实体（Entity）的概念。

## 正文

### 用装饰器定义实体

`@Entity()` 类装饰器把 `User` 类声明成数据库里的一张表；类里的字段用 `@Column()` 声明成列。本节演示的字段有：`id`（每条数据的唯一 ID，作主键）、`name`、`form`、`password`，后三者都是字符串。按演示整理成骨架如下（主键装饰器以工程内 entity 文件为准）：

```ts
import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column()
  form: string;

  @Column()
  password: string;
}
```

在可视化工具里对照，就能看到 `user` 表以及 `id`、`name`、`form`、`password` 四个字段。定义实体，本质上就是在代码里声明表结构。

### 在模块里注册实体

打开 `user.module.ts`，在 `@Module` 的 `imports` 里加一项 `TypeOrmModule.forFeature([User])`。它接收的是**数组**，因为一个数据库里不止一张表，后续可以往里放多个实体：

```ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from './entities/user.entity';

@Module({
  imports: [TypeOrmModule.forFeature([User])],
})
export class UserModule {}
```

记得同时引入 `TypeOrmModule` 与 `User` 实体。这一步注册完，实体才被纳入 ORM 的管理范围。

### 在控制器里注入 Repository

来到 `UserController`，沿用之前声明服务依赖的写法，只是把依赖换成数据仓库：用 `@InjectRepository(User)` 注入，类型为从 `typeorm` 引入的 `Repository<User>`。

```ts
import { Controller } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from './entities/user.entity';

@Controller('user')
export class UserController {
  constructor(
    @InjectRepository(User)
    private readonly userRepository: Repository<User>,
  ) {}
}
```

之后在控制器方法里通过 `this.userRepository` 就能操作这张表了。

### 增：save

调用 `save` 并传入字段对象即可插入一条数据，示例数据沿用讲师演示的「大招 / 111 / 111」：

```ts
await this.userRepository.save({
  name: '大招',
  form: '111',
  password: '111',
});
```

请求对应接口后，刷新可视化工具就能看到数据入库。这里还有个前提：上一节开启了 `synchronize: true`，所以即使手动把 `user` 表删掉，重启项目时 ORM 也会依据实体定义自动把表建回来。

### 删：delete

`delete` 接收一个条件对象，按条件删除。比如按名字删，或按 ID 删都可以：

```ts
await this.userRepository.delete({ name: '大招' });
// 或 await this.userRepository.delete({ id: 1 });
```

请求接口后再刷新，那条数据就没有了。

### 改：update

`update` 与 `delete` 不同，它接收**两个参数**：第一个是查询条件（要更新哪条），第二个是要改成的新字段。例如把「大招」改成「老王」，同时改掉电话和密码：

```ts
await this.userRepository.update(
  { name: '大招' },
  { name: '老王', form: '888', password: '222' },
);
```

演示里有个小插曲：前面已经把「大招」这条删掉了，直接 `update` 会找不到记录，所以先用 `save` 把数据插回来，再打开更新逻辑请求，数据库里就会出现 `老王 / 888 / 222`。

### 查：find 与 find()

- `find({ where: { name: '冰冰' } })`：带 `where` 条件查匹配的数据。
- `find()`：不带条件查全部，结果以数组形式返回。

```ts
const one = await this.userRepository.find({ where: { name: '冰冰' } });
const all = await this.userRepository.find();
```

这里要特别纠正一个口误：**TypeORM 里没有 `findAll`**，那是 Sequelize 的 API。讲师当场把笔记里的 `findAll` 改回了 `find`，别记混。演示中 `find()` 一次性返回了老王、冰冰、大招三条数据，正是以数组形式给出的。

### 自动建表与启动顺序

`synchronize: true` 时，实体定义会在项目启动时同步成表结构；手动删表后重启，即可看到表被重建。另一个容易踩的坑是**启动顺序**：项目还没启动完成就发请求会报错，等启动日志就绪再调接口。演示里连续快速插入时，就有一条因为项目未就绪而没写进去。

### 在工程里的位置

配套代码 `代码（已8期）/代码（已8期）/8-6/lowcode/package.json` 的脚本显示后端子项目通过 `--filter` 启停，删表后执行 `run:server` 重启即触发自动建表：

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

配套资料：`代码（已8期）/代码（已8期）/8-6/lowcode/packages/server/package.json`、`代码（已8期）/代码（已8期）/8-6/lowcode/packages/server/tsconfig.json`、`代码（已8期）/代码（已8期）/8-6/lowcode/pnpm-workspace.yaml`。

## 小结

- `@Entity()` + `@Column()` 把类映射成表与列，主键用 `@PrimaryGeneratedColumn()` 声明。
- `TypeOrmModule.forFeature([User])` 注册实体，`@InjectRepository(User)` 注入 `Repository<User>`。
- `save` / `delete` / `update` / `find` 对应增删改查；`update` 是「查询条件 + 新字段」两个参数。
- `find()` 不带条件查全部并返回数组，TypeORM 没有 `findAll`。
- `synchronize` 会在启动时自动同步表结构，注意等项目启动完成再请求接口。

## 下一步

本节的 API 是分散演示的，建议接着看《TypeORM 框架—实现数据库增+查操作》与《TypeORM 框架—实现数据库改+删操作》，把它们收拢成工程化的实现；也可以看《后端接口开发—用户的查询接口开发》，了解如何把这些操作封装进正式接口。
