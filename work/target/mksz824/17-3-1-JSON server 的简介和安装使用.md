# 17-3-1-JSON server 的简介和安装使用

之前描述了前后端分离开发以及对应的接口。录课阶段后端功能已经开发完毕，所以后面编码我都直接使用测试服务器。但大家都知道，真实开发中前后端是并行进行的：前端写代码的时候，后端功能肯定还不完善，API 还不能最终提供使用。这时候就需要一个简单的 mock server 来完成前后端的快速连接。作为加餐，这里介绍一个可以快速搭建 mock server 的工具，供大家在以后的工作中酌情选用。

## Mock server 选型

上一阶段介绍过一系列流行的 Node.js 框架：Express、Koa、Egg.js 等。它们成熟，但实施起来要写大量逻辑代码，我认为不符合需求。一个好的 mock server 应该有这些特点：

1. **快速搭建**：这不是主要业务代码，希望不需要任何逻辑或配置就能迅速搭起来，时间越短越好；
2. **支持标准的 RESTful 操作**：前后端交互都用 RESTful 请求，mock server 要支持标准方法；
3. **支持 RESTful 标准的路由规则**：拿一组数据（collection）用 `/templates`，拿一条数据用 `/templates/:id`，以此类推；
4. 进阶扩展：自定义路由、中间件支持等等。

隆重推出我的选择：JSON Server，GitHub 上有 53k star。对照文档看它是否符合需求：第一句话就是 with zero coding，一个代码都不用写，less than 30 seconds，三十秒内就能搭好，符合快速搭建的标准。往下看特性：支持各种单数和复数路由、filter、paginate、slice、operate 等，还有 full-text search；extra 里还能当文件服务器（file server）、支持 HTTPS、添加自定义路由和 middleware，扩展性很强。

最简单的用法：只需新建一个 JSON 文件（如 `db.json`）写入数据，启动后它就会提供与文件字段相对应的一系列路由。

## 安装与启动

安装：

```bash
npm install --save-dev json-server
```

在项目根目录创建 `db.json`，写入数据：

```json
{
  "posts": [
    { "id": 1, "title": "json-server", "author": "typicode" }
  ],
  "comments": [
    { "id": 1, "body": "some comment", "postId": 1 }
  ],
  "profile": { "name": "typicode" }
}
```

启动：

```bash
json-server --watch db.json
```

`--watch` 后面跟希望生成对应路径的文件。回车后它会打印生成的路由，和配置文件完全一致。访问 `localhost:3000/posts` 就能看到两条与文件一样的数据；访问 `/posts/1` 可以单独拿到 id 为 1 的那条。

## 验证 RESTful 操作

用 Postman 测试。向 `localhost:3000/posts` 发 POST 请求，body 选 application/json，添加 `id: 3`、`author: typicode`，点 Send 成功。刷新 `/posts` 路径，新的一条已经自动添加，访问 id 3 也没问题。

它的底层用的是 lowdb 这个库，用文件来 serve 数据。PUT、PATCH 和 DELETE 这些标准方法也都支持：向 `/posts/3` 发 DELETE 请求，返回成功；再刷新，只剩 id 1 和 2，第 3 条已被删除。

不到三分钟，我们就搭好了一个非常健壮的 mock server，支持一系列路由和标准的 RESTful 操作。JSON Server 的基础用法讲到这里，下节课了解怎样自定义 routes，让它适应我们的接口规范。
