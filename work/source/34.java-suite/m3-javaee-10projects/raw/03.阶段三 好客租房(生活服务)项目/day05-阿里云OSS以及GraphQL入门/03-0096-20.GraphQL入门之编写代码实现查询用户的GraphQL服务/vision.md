# 画面线理解：20.GraphQL入门之编写代码实现查询用户的GraphQL服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\20.GraphQL入门之编写代码实现查询用户的GraphQL服务【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 02:14, 04:02, 05:23, 06:53, 08:18, 09:12, 10:03, 10:58, 12:24, 13:38, 14:52, 15:50, 16:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:01:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 GraphQL 框架定义查询对象类型、构建 Schema 并执行查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中 GraphQL Schema 的定义片段，包含 `type User { id:Long! name:String }`。
画面2：IDE 中显示 `GraphQlDemo.java` 的 `main` 方法，创建 `GraphQL` 实例。
画面3：在 `main` 方法中调用 `GraphQLSchema.newBuilder().query(...)` 构建 Schema。
画面4：PDF 文档中展示 `User` 类型的定义和 Java 实现的导入语句。
画面5：IDE 中 `GraphQlDemo.java` 的 `main` 方法，使用 `GraphQL` 类的静态方法。
画面6：IDE 中 `GraphQlDemo.java` 的 `main` 方法，定义 `GraphQLObjectType` 和 `GraphQLFieldDefinition`。
画面7：IDE 中 `GraphQlDemo.java` 的 `main` 方法，为 `userFieldDefinition` 设置 `type` 为 `userObjectTy`。
画面8：IDE 中 `GraphQlDemo.java` 的 `main` 方法，为 `userFieldDefinition` 设置 `name` 为 `"user"`。
画面9：IDE 中 `GraphQlDemo.java` 的 `main` 方法，定义 `userQueryObjectType` 并设置 `field`。
画面10：IDE 中 `GraphQlDemo.java` 的 `main` 方法，定义 `query` 字符串并执行。
画面11：IDE 中 `GraphQlDemo.java` 的 `main` 方法，为 `userFieldDefinition` 设置 `.dataFetcher(...)`。
画面12：PDF 文档中展示 `createGraphqlSchema` 方法的定义和 `createUserDefinition` 方法。
画面13：IDE 中 `GraphQlDemo.java` 的 `main` 方法，执行查询并打印结果。
画面14：IDE 中 `GraphQlDemo.java` 的 `main` 方法，打印 `result.toSpecification()`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```graphql
#对应的User定义如下
schema {
  query: UserQuery
}
type UserQuery {
  #定义查询的类型
  User: User #指定对象以及参数类型
}
type User {
  #定义对象
  id:Long! # !表示该属性是非空项
  name:String
}
```

画面2：
```java
package cn.itcast.graphql.demo;
import graphql.GraphQL;
public class GraphQlDemo {
    public static void main(String[] args) {
        GraphQL graphQL = GraphQL.newGraphQL(...
    }
}
```

画面3：
```java
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().q
    .query(Builder builder)
    .query(GraphQLObjectType queryType)
    .equals(Object obj)
    graphQL.execute(query);
```

画面4：
```java
package cn.itcast.graphql.demo;
import cn.itcast.graphql.vo.User;
import graphql.ExecutionResult;
import graphql.GraphQL;
```

画面5：
```java
GraphQL graphql = GraphQL.newGraphQL(graphqlSchema).build();
```

画面6：
```java
GraphQLObjectType userObjectType = GraphQLObjectType.newObject()
    .name("User")
    .field(userFieldDefinition)
    .build();

GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
    .name("UserQuery")
    .field(userFieldDefinition)
    .build();

GraphQLSchema graphQLSchema = GraphQLSchema.newSchema()
    .query(userQueryObjectType)
    .build();

GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema)
    .build();
```

画面7：
```java
.type(Builder builder)
.type(GraphQLObjectType type)
.toString()
.type(GraphQLObjectType type)
```

画面8：
```java
.type(Scalars.GraphQLLong)
.type(Scalars.GraphQLString)
.type(Scalars.GraphQLInt)
```

画面9：
```java
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema()
    .query(userQueryObjectType)
    .build();

GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema)
    .build();

String query = "{User{id,name}}";
graphQL.execute(query);
```

画面10：
```java
String query = "{User{id,name}}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
```

画面11：
```java
.dataFetcher(new StaticDataFetcher(new User()))
```

画面12：
```java
public static GraphQLSchema createGraphqlSchema(GraphQLFieldDefinition userDefinition) {
    GraphQLObjectType userQuery = newObject().name("UserQuery")
        .field(userDefinition).build();
    return GraphQLSchema.newSchema().query(userQuery).build();
}

// 定义查询的类型
public static GraphQLFieldDefinition createUserDefinition(GraphQLObjectType userObjectType) {
    return GraphQLFieldDefinition.newFieldDefinition()
        .name("user")
        .type(userObjectType)
        .build();
}
```

画面13：
```java
String query = "{user{id,name,age}}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
```

画面14：
```java
System.out.println(result.toSpecification());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PDF 文档标题为“7.1.3、编写查询User对象实现”，左侧目录显示“7.1.3、编写查询User对象实现”。
画面4：PDF 文档标题为“黑马程序员”，下方有“改变中国IT教育，我们正在行动”。
画面12：PDF 文档标题为“7.1.3、编写查询User对象实现”，左侧目录显示“7.1.3、编写查询User对象实现”。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
