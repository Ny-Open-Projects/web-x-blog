# 104. 六大数据库存储实战: 动手用 MongoDB Shell 完成 CRUD

## 纲要

- 用 Docker 拉起开启了鉴权（`--auth`）的 MongoDB（默认端口 27017）
- 先建管理员账户并授权，才能看到库、做操作
- MongoDB 的"库"是懒加载的：只有创建了集合，库才真正存在
- 文档（document）即行，集合（collection）即表，插入时自动生成 `_id`（ObjectId）
- 主键查询走索引；非主键字段查询会全集合扫描，需 `createIndex` 建索引
- 排序、分页用 `sort` / `limit` / `skip` 链式调用

## 📎 代码说明

本讲代码以**内联片段**形式呈现在正文中。课程课件仅发布第 2/3/4 章（MySQL 核心能力）的完整工程源码，本讲所属章节未随课件发布独立源码文件，故不做外部文件关联，请以正文片段为准。

## 起一个带鉴权的 MongoDB

用 Docker 拉最新版并启动，注意加上 `--auth`，表示连接需要用户名密码：

```bash
docker pull mongo:latest
docker run -d -p 27017:27017 mongo --auth
```

容器起来后用 `mongosh` 连本地 27017 端口。新版本 MongoDB 已经到 6.x，shell 命令与老版本基本一致。

## 建管理员并登录

MongoDB 默认就要鉴权。直接 `show dbs` 什么都看不到，因为当前用户没被授权。先切到 `admin` 库建一个管理员：

```js
use admin

db.createUser({
  user: "admin",
  pwd: "123456",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "readWriteAnyDatabase", db: "admin" }
  ]
})

db.auth("admin", "123456")
```

授权完成后，`show dbs` 就能看到 `admin`、`config`、`local` 三个系统库了。这个 `admin` 账户拥有任意库的读写权限，后续操作都用它。

## 库的懒加载特性

切到一个还不存在的库，再 `show dbs` 却看不到它——这是 MongoDB 的一个关键特性：

```js
use socialcomments      // 切换到（还不存在的）库
show dbs                // 列表里没有 socialcomments
db.createCollection("student")  // 建一个集合
show dbs                // 现在 socialcomments 出现了
```

也就是说，**库只有在创建集合之后才会被懒加载出来**。只有 `use` 而不建集合，库是不会落地的。

## 插入与查询

插入一条文档，字段用 JSON / BSON 表达即可，MongoDB 会自动补一个 `_id` 字段（ObjectId）：

```js
db.student.insertOne({ name: "david", age: 30, gender: 1 })
db.student.find()       // 不带条件，查出全部
```

更新必须带查询条件，并且用 `$set` 表达"要改哪些字段"，主键要用 `ObjectId` 包一层：

```js
db.student.update(
  { _id: ObjectId("64a1...省略...") },
  { $set: { name: "marry" } }
)
```

删除一条用 `deleteOne`（老版本叫 `remove`）：

```js
db.student.deleteOne({ _id: ObjectId("64a1...省略...") })
```

## 主键查询 vs 非主键查询

按 `_id` 查，命中主键索引，很快：

```js
db.student.find({ _id: ObjectId("64a1...省略...") })
```

但按 `name` 这种非主键字段查，会**全集合扫描**——可以把它理解为把整个 collection 里的文档挨个过一遍：

```js
db.student.find({ name: "david" })
```

解决办法是建索引。对 `name` 建一个升序索引（1 升序、-1 降序）：

```js
db.student.createIndex({ name: 1 })
```

建完再查 `name`，就会走这个升序索引，不必扫全表。

## 排序与分页

`limit`、`skip`、`sort` 可以链式组合，对应"取几条 / 跳过几条 / 按某字段排序"：

```js
db.student.find().limit(1)              // 只看一条
db.student.find().skip(2)               // 跳过两条
db.student.find().sort({ age: 1 })      // 按 age 升序
```

## 小结

| 操作 | Shell 写法 | 备注 |
| --- | --- | --- |
| 建库 | `use dbName` + `createCollection` | 库懒加载 |
| 插 | `insertOne({...})` | 自动 `_id` |
| 查 | `find({条件})` | 非主键会全扫 |
| 改 | `update({条件},{$set:{...}})` | 主键用 `ObjectId` |
| 删 | `deleteOne({条件})` | 老版 `remove` |
| 索引 | `createIndex({字段:1})` | 解决非主键慢查 |
| 分页排序 | `limit` / `skip` / `sort` | 链式调用 |

这套 shell 操作是后续用 Java API 操作 MongoDB 的手感基础：集合、文档、索引、条件查询的语义完全一致，只是换成了驱动提供的对象方法。

