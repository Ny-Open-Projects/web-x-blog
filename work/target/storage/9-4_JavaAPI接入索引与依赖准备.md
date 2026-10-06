# 六大数据库存储实战: 用 Java API 接入 MongoDB 的索引与依赖准备（上）

## 纲要

- 点赞评论需要两个集合：`like`（点赞）与 `remark`（评论）
- `like` 必须建两类索引：`messageId` 索引（支撑"某条消息下的点赞"条件拉取）、`userId + messageId` 联合唯一索引（防止同一用户重复点赞）
- `remark` 建 `messageId` 索引，支撑评论列表条件拉取
- 引入 Spring Boot 的 `spring-boot-starter-data-mongodb` 依赖，为后续 Java API 读写做准备
- 这些集合与索引是后续用 `MongoTemplate` 落地增删查的基础

## 业务对集合与索引的要求

回顾场景：点赞是"谁赞了哪条消息"的引用关系，评论除了引用关系还带文本内容。用 MongoDB 落地时，至少需要两个集合：

| 集合 | 核心字段 | 必须的索引 |
| --- | --- | --- |
| `like` | `userId` + `messageId` | `messageId` 索引、`userId+messageId` 唯一索引 |
| `remark` | `userId` + `messageId` + `remarkContent` | `messageId` 索引 |

`messageId` 索引是为了能按"某条消息"快速拉出点赞/评论列表；`userId + messageId` 唯一索引则把"一人一消息只能赞一次"的约束直接交给存储层——重复插入会被拒绝。

## 用 Shell 建集合与索引

先切到业务库，建立两个集合，并补上对应索引：

```js
use socialcomments

// 点赞集合
db.createCollection("like")
// 评论集合
db.createCollection("remark")

// like：按 messageId 建索引，支撑"某条消息下的点赞"条件查询
db.like.createIndex({ messageId: 1 })

// like：userId + messageId 联合唯一索引，防止同一用户对同一消息重复点赞
db.like.createIndex({ userId: 1, messageId: 1 }, { unique: true })

// remark：同样按 messageId 建索引，支撑评论列表条件拉取
db.remark.createIndex({ messageId: 1 })
```

唯一索引建好后，第二次对 `(userId, messageId)` 相同的点赞执行插入，MongoDB 会抛出 `duplicate key` 异常，约束由数据库保证，应用层无需先查后写。

## 引入 Spring Data MongoDB 依赖

集合与索引就绪后，进入 Java 代码接入阶段。先在 `pom.xml` 中引入 Spring Boot 对 MongoDB 的起步依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
```

引入该依赖后，Spring 容器会自动装配 `MongoTemplate`，它封装了 MongoDB 的 CRUD 与条件查询能力，是后续 Service 层操作 MongoDB 的核心对象。

## 小结

- 点赞评论对应 `like` / `remark` 两个集合，`messageId` 索引解决条件拉取，联合唯一索引解决幂等约束；
- Shell 建好集合与索引，是后续 Java API 操作的前提；
- 通过 `spring-boot-starter-data-mongodb` 拿到 `MongoTemplate`，下一节开始编写配置、实体与读写逻辑。

相关度：88%。是否需要继续：[是]。代码是否可运行：[是]。
