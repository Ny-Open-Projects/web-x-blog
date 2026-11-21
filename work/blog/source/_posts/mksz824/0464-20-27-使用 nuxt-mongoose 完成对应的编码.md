---
disableNunjucks: true
title: 20-27 使用 nuxt-mongoose 完成对应的编码
date: 2026-11-17 12:44:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

这节课继续完成 MongoDB 模块的应用。第一步当然是需要创建对应的 model。nuxt-mongoose 给我们提供了一个很方便的特性：它可以自动加载特定文件夹中的 model 文件，默认位置就是 server 下的 models 文件夹，放在那里的所有 model 都会被自动加载。它也提供配置项（modelsDir）可以自定义位置，想放在别的位置可以去修改，这里就不改了。

在 models 下创建 user.ts，使用之前创建好的用户模型来完成一次查询，把整个流程跑通。关于 Mongoose 的知识如果有遗忘，可以去看后端课程"用户系统设计与实现"中的第二章：用户数据模型、创建接口以及验证功能的开发，那里讲得非常详尽。我这里直接写代码了，大家遗忘的话一定要回去看。

nuxt-mongoose 提供了一个函数叫 defineMongooseModel，顾名思义用来定义模型，可以很方便地定义用户的 schema。首先导入要使用的函数和类型。特别注意：类型要整个系统运行起来才能生成，如果你没有运行应用，直接从这里导入是会报错的，因为很多类型都是运行起来自动生成的。所以要先运行，再写代码。

先定义 user 的 interface，直接从之前课程的代码拷贝过来，是一系列 user 的属性。有了它就可以完成定义：

```ts
export const UserSchema = defineMongooseModel({
  name: 'User',
  schema: {
    username: { type: String, unique: true, required: true },
    nickname: { type: String },
    email: { type: String },
  },
  options: {
    timestamps: true,
    toJSON: {},
  },
})
```

第一，这是具名导出。函数可以接受一个泛型，好处是定义每个属性的类型时有自动补全，比如定义 username 时能补全出 type 是 string、unique 表示唯一、required 表示必选，这些直接复制之前课的内容就行。这里还能体会到 TS 的好处：type 在这里只有三种可选值，随便写一个不存在的类型会直接报错，非常方便。

第二个参数是一系列字段，第三个参数是额外的 options，和之前写的一样：timestamps 自动添加时间；toJSON 表示把对象转 JSON 时自动做转换，删除其中比较敏感的信息。对这块遗忘的话务必去回看之前的内容。

model 定义完毕后就做一次查询。在 API users 下面已经建了一个 next 路由：

```ts
export default defineEventHandler(async () => {
  const users = await UserSchema.find()
    .select(['username', 'nickname'])
    .limit(10)
    .lean()
  return users
})
```

具名导出的 UserSchema 会注册到一个全局的地方，可以直接使用。find 查询后调用 select 选择两个字段：username 和 nickname，只显示这两个；limit(10) 只取十条；lean() 返回普通的 JSON 对象；最后直接把 users 返回出去。

刷新页面，用户信息完全显示出来了，并且只显示了需要的 username 和 nickname，很完美。这样就完成了 Mongoose 的配置，并带着大家简单回顾了之前的内容，也理解了 modules 的概念。建议大家课下再找一个模块安装熟悉一下，比如 ESLint 就是一个很好的工具，加深对模块使用的印象。

这节课我们成功完成了整个 MongoDB 的配置，并且完成了一次查询。
