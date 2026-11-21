---
disableNunjucks: true
title: 14-23 Docker 初始化 MongoDB 数据库操作
date: 2026-11-17 12:34:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课介绍了 Mongo 的权限管理，现在希望把这套流程添加到 Docker 中。这一系列操作属于启动容器前的准备工作，无论启动什么数据库都可能遇到类似任务，所以统称为数据库准备工作，包括配置和初始化。比如在 opsflow 数据库中插入一个 admin 类型的用户供以后后台登录，或者插入几条初始化的模板数据。另外，上节课说过，为了提高安全性要避免在代码中直接用 root 操作，所以在启动服务前需要以 root 身份完成必要的准备工作：创建数据库管理员，之后在代码中切换到这个管理员去连接数据库。

## 特殊文件夹 /docker-entrypoint-initdb.d

Docker 的数据库镜像都提供了一个特殊的文件位置：`/docker-entrypoint-initdb.d`。这是一个文件夹，可以在里面放置要运行的脚本，比如 MySQL 放 `.sql` 文件，Mongo 可以放 `.js` 或 `.sh` 文件。这些脚本会在数据库启动之前被自动执行。

看两个文档验证：MongoDB 的文档说，放在这个文件夹下的 .js 文件会在数据库启动之前自动执行，并特别标注了 "create on first use"；PostgreSQL（关系型数据库）同样支持，放置任何 .sql、.sql.gz 或 .sh 脚本，在初始化 db 的过程中都会自动执行。

这里要特别注意 "create on first use"：只有数据库文件夹为空、数据库第一次被创建时，这些脚本才会执行。假如文件夹里已经有数据文件，脚本不会执行。在我们的项目里，之前启动过 Docker，会有 `.docker-volumes` 文件夹，对应 `/data/db`，也就是 Mongo 保存数据的地方。它发现里面有数据就不是第一次创建，脚本就不会跑。所以测试前要把这个文件夹删掉，这一点很多同学都会踩坑，记得先把 db 清空。

## 用内置环境变量创建 root

脚本里本应先创建 admin 级别的 root 用户，但其实不需要：Mongo 提供了两个环境变量，`MONGO_INITDB_ROOT_USERNAME` 和 `MONGO_INITDB_ROOT_PASSWORD`。只要提供这两个值，它就会自动创建对应的 root user，并以 `--auth` 这种需要验证的形式启动 Mongo 实例。

在 docker-compose.yaml 中设置环境变量用 `environment` 字段，多个用横杠加 name=value 的形式。为了这节课专注数据库启动，先把 opsflow-backend 服务注释掉：

```yaml
environment:
  - MONGO_INITDB_ROOT_USERNAME=admin
  - MONGO_INITDB_ROOT_PASSWORD=pass
```

有了这两个，运行之前就会自动创建 root user。当然 username 和 password 目前是明文，这是之后要改进的点，暂时先这样写。

## 挂载初始化脚本

接下来把脚本映射到容器里。新建一个文件夹 mongo-entrypoint，在服务的 volumes 里添加一条映射，把本地这个文件夹映射到 `/docker-entrypoint-initdb.d`。注意一个坑：如果只写一个没有路径结构的值，它会被判定成一个 named volume，启动会失败。所以前面要加一个路径前缀，用 `$PWD`（指代当前目录的全局环境变量，`echo $PWD` 可以验证）：

```yaml
volumes:
  - $PWD/mongo-entrypoint:/docker-entrypoint-initdb.d
```

两层结构之后就不会被误判，可以按路径启动。启动脚本 setup.js 写在 mongo-entrypoint 里：

```js
let db = connect('admin:pass@localhost:27017/admin');
db = db.getSiblingDB('opsflow');

db.createUser({
  user: 'user',
  pwd: 'pass',
  roles: [{ role: 'readWrite', db: 'opsflow' }]
});

db.createCollection('works');
db.works.insertOne({ /* 一条模板初始化数据 */ });
```

梳理一遍：connect 之前在学习 mongo 脚本时用过，这类函数是容器启动时自动提供给我们的；连接 admin（用刚才环境变量创建的 root 授权），然后用 `getSiblingDB` 选择同级要操作的数据库 opsflow；再用和上节课一样的 `createUser` 创建业务用户 user/pass，roles 是 readWrite、作用于 opsflow。这个用户是之后代码里真正要用的。这里的 user/pass 同样是明文，不符合规矩，之后要解决，和 Docker Compose 里的 environment 是同一个问题。最后 `createCollection` 创建 works 并插入一条模板数据，任何数据初始化都可以放在这里。

## 运行验证

清空 .docker-volumes 后 `docker compose up -d`。启动成功后，Dashboard 里只有 mongo 在 running。进去验证：`docker ps` 拿到 ID，`docker exec -it <id> bash`，用脚本中创建的用户连接：

```bash
mongo -u user -p pass --authenticationDatabase opsflow
```

`--authenticationDatabase`（authentication database）填 opsflow，因为这个用户管理的只是 opsflow 这个库。回车后进入成功，`show dbs` 显示能管理的数据库只有 opsflow 一个，说明权限正确。再 `use opsflow`，`db.works.find()` 能看到之前插入的 work 数据，说明整个脚本完全成功：root user 有了，数据库和基于它的用户建好了，测试数据也在。

现在 Docker 已能成功运行初始化脚本。下一步是把这些敏感信息隐藏起来，我们不希望 user、password 这些字段提交到代码里泄露秘密。本篇记住两点：初始化脚本都可以写到 `/docker-entrypoint-initdb.d`，会自动执行；Mongo 有两个内置环境变量可以用来初始化 root user。
