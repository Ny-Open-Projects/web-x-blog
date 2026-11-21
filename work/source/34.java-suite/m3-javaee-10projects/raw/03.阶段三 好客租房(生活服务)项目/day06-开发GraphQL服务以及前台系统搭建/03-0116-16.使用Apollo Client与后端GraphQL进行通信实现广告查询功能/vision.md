# 画面线理解：16.使用Apollo Client与后端GraphQL进行通信实现广告查询功能

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\16.使用Apollo Client与后端GraphQL进行通信实现广告查询功能【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:38, 02:58, 04:39, 06:09, 07:10, 08:19, 09:35, 10:44, 11:54, 13:34, 14:38, 15:56, 17:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:16:41

1) 这一组画面整体在讲如何在 React 应用中使用 Apollo Client 作为 GraphQL 客户端，包括安装、创建客户端、发起查询以及后端 Java 服务端的实现。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PDF 中关于 GraphQL 客户端的介绍，重点是 Apollo Client。
画面 2: Apollo Client 官网的 Introduction 页面，介绍其特性。
画面 3: Apollo Client 官网的 Get started 页面，引导创建客户端。
画面 4: 在 IntelliJ IDEA 中，代码文件 `home.js` 中导入 ApolloClient 并创建实例，配置 GraphQL 服务端点。
画面 5: 在 IntelliJ IDEA 中，`home.js` 文件中定义组件状态和生命周期方法，准备发起请求。
画面 6: 浏览器开发者工具 Network 面板，显示对 GraphQL 服务端点的 OPTIONS 请求。
画面 7: 浏览器开发者工具 Network 面板，显示对 GraphQL 服务端点的 POST 请求。
画面 8: 使用 Altair GraphQL Client 工具，向 GraphQL 服务端点发送请求并查看返回数据。
画面 9: 在 IntelliJ IDEA 中，Java 服务端代码 `GraphQLController.java` 中导入 GraphQL 依赖并定义私有字段。
画面 10: 在 IntelliJ IDEA 中，`GraphQLController.java` 中实现 `@GetMapping` 和 `@PostMapping` 方法，用于处理 GraphQL 查询。
画面 11: 浏览器中显示 React 应用的首页，包含多个功能按钮。
画面 12: 课程 PDF 中关于安装依赖、创建客户端和创建查询的代码示例。
画面 13: 在 IntelliJ IDEA 中，`home.js` 文件中使用 Apollo Client 发起查询，处理数据。
画面 14: 课程 PDF 中关于查询的其他用法的介绍，展示一个广告页面。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 4:
```javascript
import gql from 'graphql-tag'
const client = new ApolloClient({
  uri: "http://127.0.0.1:18080/graphql"
});
```

画面 12:
```bash
npm install apollo-boost react apollo graphql --save
```

画面 12:
```javascript
import ApolloClient from "apollo-boost";
const client = new ApolloClient({
  uri: "http://127.0.0.1:18080/graphql"
});
```

画面 12:
```javascript
import gql from "graphql-tag";
```

画面 13:
```javascript
let swipe = new Promise((resolve, reject) => {
  client.query({query: GET_INDEX_ADS}).then(result => {
    resolve(result.data.IndexADList.list);
  });
});
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PPT 标题为“4.6. GraphQL客户端”，内容包括 Relay 和 Apollo Client 的介绍。
画面 12: PPT 标题为“4.6.1. 安装依赖”、“4.6.2. 创建客户端”、“4.6.3. 创建查询”。
画面 14: PPT 标题为“4.6.5. 查询的其他用法”，并附有参考链接。

5) 无。
