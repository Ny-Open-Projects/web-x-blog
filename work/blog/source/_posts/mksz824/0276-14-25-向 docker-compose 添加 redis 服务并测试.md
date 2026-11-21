---
disableNunjucks: true
title: 14-25 向 docker-compose 添加 redis 服务并测试
date: 2026-11-17 14:36:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

Docker Compose 的各种用法都学完了，这节课把整个应用整合一下，把 Redis 也添加进去，让整个系统一起运作。先自己去下载 Redis 镜像，版本很多，这里选了 6，可以按需选择。

## 添加 redis 服务

写法已经很熟悉了，和 mongo 并列添加一个服务：

```yaml
  opsflow-redis:
    image: redis:6
    container_name: opsflow-redis
    command: redis-server --requirepass $REDIS_PASSWORD
    ports:
      - 6379:6379
    env_file:
      - .env
```

image 来自 redis:6；container_name 命名为 opsflow-redis，因为之后要在代码中访问它；ports 是 6379 对 6379；再加上 env_file 引入 .env。

## 密码访问：command 字段

我们希望像 MongoDB 那样给 Redis 加上密码保证安全。但 Redis 的 Docker 镜像没有提供类似 Mongo 的内置环境变量。有一篇 2016 年的帖子，很多人回复希望镜像提供密码访问的环境变量，但开发者经过讨论最终没有添加，引来不少程序员的不满。所以要另辟蹊径。

回忆一下，本地启动 Redis 用的是 redis-server 命令，Docker 启动容器时执行的也是它。想在启动时加密码访问，可以给它一个特殊参数 `requirepass`，后面写密码值。于是目的变成：自定义 Redis 镜像的启动命令。Docker Compose 有个专门的字段 command，文档里写明 override default command，可以覆盖容器启动后默认执行的命令，既能写成字符串也能写成数组。

上面的配置里我用了一个特殊写法：command 的值以尖括号开头（YAML 里的折叠写法），代表沿用默认命令 redis-server，只需把要加的参数追加到后面。参数就是 requirepass，值引用 .env 中添加的 REDIS_PASSWORD（记得自己去 .env 里加上）。这样 Redis 就会以需要密码访问的形式启动。

## 修改生产配置

config 的 production 中对 redis client 做修改：port 是 6379；添加 host，就是主机名称，对应 container name opsflow-redis；depends_on 除了 opsflow-mongo，还要加上 opsflow-redis；password 直接取 `process.env.REDIS_PASSWORD`，环境变量已经被注入。这样连接的是容器中运行在 6379 的 Redis 服务，并且带着密码。

## ping 接口：一键自检

最后在 API 里做一个 ping 接口，每次上线后访问它，就能获得当前版本、数据库连接和环境变量是否生效。修改 home.ts，替换掉原来的 index 方法，返回一系列信息：

- Redis 状态：从 `ctx.app.redis` 拿到 status，即 Redis 当前的 ready 状态。
- Mongo 版本：看数据库是否连接，有版本号方便很多。注意不能拿 `ctx.app.mongoose` 上的 version，那是 mongoose 库自己的版本；要拿 MongoDB 整体的版本需要执行一条命令：`await ctx.app.mongoose.connection.db.command({ buildInfo: 1 })`，返回结果里有 version。
- 应用版本：从 package.json 取，代表当前代码的版本。`import pkg from '../package.json'` 时 TS 报了 cannot find module，因为 TS 默认不支持导入 JSON 文件，需要在 tsconfig.json 中添加 `resolveJsonModule: true`，保存后错误消失。导入时用 as 起个别名叫 appVersion，避免重名。
- 环境变量测试：返回 `process.env.PING_ENV`，在 .env 里加了一条不敏感的变量，有这个变量就说明环境变量注入成功。

用 ctx.helper.success 返回 `{ dbVersion: version, readyStatus: status, appVersion, env: process.env.PING_ENV }`。修改完别忘了在 config.default.ts 中把开发环境的 Redis 注释也去掉，开发环境也需要连接 Redis。

## 构建验证

每次 build 之前再强调一次：都要把之前构建的 opsflow-backend 镜像删掉，否则不会触发重新 build。然后 `docker compose up -d`。等待之后所有服务启动成功、都是绿色。

访问 API 检查：dbVersion 显示 MongoDB 已连接；readyStatus 是 ready；appVersion 是 1.0.0；env 有值，说明环境变量已注入。整个应用全部启动成功。再去看看 templates，预置的数据还在。

现在使用 Docker Compose 改造程序告一段落：可以轻松把多个服务整合成几个 container，用一个文件一键启动所有服务，比原来的运行方式简便非常多。
