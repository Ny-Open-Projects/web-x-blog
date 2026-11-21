# 画面线理解：21.GraphQL入门之查询参数的设置

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\21.GraphQL入门之查询参数的设置【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:37, 00:52, 01:13, 01:45, 02:47, 02:58, 03:31, 04:01, 04:17, 05:01, 05:21, 05:34, 05:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:02:44

1) 这一组画面整体在讲如何在 Java 中使用 GraphQL 框架定义对象类型、查询类型、字段和参数，并通过代码执行查询。

2) 按时间顺序列出每张画面的要点：
画面1:
- 代码：在 GraphQlFieldDefinition 中定义了三个字段：id（GraphQlLong）、name（GraphQlString）、age（GraphQlInt），并为 user 字段设置了 StaticDataFetcher，返回一个预设的 User 对象。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面2:
- 代码：在定义 user 字段时，使用 .argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build()) 添加了 id 参数。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面3:
- 代码：在定义 user 字段时，使用 .argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build()) 添加了 id 参数。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面4:
- 代码：在定义 user 字段时，使用 .dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20))) 设置了数据获取器。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面5:
- 代码：在定义 user 字段时，使用 .dataFetcher(environment -> { ... }) 设置了数据获取器。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面6:
- 画面显示了 IntelliJ IDEA 的 Project Structure 设置界面。
- 语言级别设置为 8 - Lambda, type annotations etc.
- 项目结构中包含 src 和 target 文件夹。

画面7:
- 代码：定义了 GraphQLSchema，创建了 GraphQL 对象，并执行了查询。
- 代码：查询字符串为 "user{id,name,age}"。
- 代码：打印了查询结果和错误信息。

画面8:
- 代码：查询字符串为 "user(id:1){id,name}"。
- 代码：执行查询并打印结果和错误信息。
- 代码：打印了查询结果和错误信息。

画面9:
- 代码：查询字符串为 "user(id:100){id,name}"。
- 代码：执行查询并打印结果和错误信息。
- 代码：打印了查询结果和错误信息。

画面10:
- PDF 页面显示了 GraphQL 的 Schema 和类型规范。
- 代码：展示了如何定义字段和参数。
- 代码：展示了如何执行查询。

画面11:
- 代码：导入了 GraphQL 相关的包。
- 代码：定义了 GraphQLDemo 类。
- 代码：定义了 User 类型。

画面12:
- 代码：定义了 GraphQLSchema，创建了 GraphQL 对象，并执行了查询。
- 代码：查询字符串为 "user(id:100){id,name}"。
- 代码：打印了查询结果和错误信息。

画面13:
- 代码：定义了 GraphQLDemo 类。
- 代码：定义了 User 类型。
- 代码：定义了 UserQuery 类型。

画面14:
- PDF 页面显示了 GraphQL 的 Schema 和类型规范。
- 代码：展示了如何定义字段和参数。
- 代码：展示了如何执行查询。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1:
```java
.field(GraphQLFieldDefinition.newFieldDefinition().name("id").type(Scalars.GraphQLLong)
.field(GraphQLFieldDefinition.newFieldDefinition().name("name").type(Scalars.GraphQLString)
.field(GraphQLFieldDefinition.newFieldDefinition().name("age").type(Scalars.GraphQLInt)
.build();

/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20)))
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面2:
```java
/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build())
.dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20)))
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面3:
```java
/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build())
.dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20)))
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面4:
```java
/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build())
.dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20)))
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面5:
```java
/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.dataFetcher(environment -> {
    return new User(id:1L, name: "张三", age: 20);
})
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面6:
```java
Language level: 8 - Lambda, type annotations etc.
```

画面7:
```java
/**
 * schema { #定义查询 }
 */
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().query(userQueryObjectType).build();
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();

String query = "{user{id,name,age}}";
ExecutionResult result = graphQL.execute(query);

System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
System.out.println(result.toSpecification());
```

画面8:
```java
/**
 * schema { #定义查询 }
 */
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().query(userQueryObjectType).build();
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();

String query = "{user(id:1){id,name}}";
ExecutionResult result = graphQL.execute(query);

System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
System.out.println(result.toSpecification());
```

画面9:
```java
/**
 * schema { #定义查询 }
 */
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().query(userQueryObjectType).build();
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();

String query = "{user(id:100){id,name}}";
ExecutionResult result = graphQL.execute(query);

System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
System.out.println(result.toSpecification());
```

画面10:
```java
// 代码：展示了如何定义字段和参数。
// 代码：展示了如何执行查询。
```

画面11:
```java
import cn.itcast.graphql.vo.User;
import graphql.ExecutionResult;
import graphql.GraphQL;
import graphql.Scalars;
import graphql.schema.GraphQLLong;
import graphql.schema.GraphQLString;
import graphql.schema.GraphQLInt;
import graphql.schema.GraphQLFieldDefinition;
import graphql.schema.GraphQLObjectType;
import graphql.schema.GraphQLObjectType.newObject;
```

画面12:
```java
/**
 * schema { #定义查询 }
 */
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().query(userQueryObjectType).build();
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();

String query = "{user(id:100){id,name}}";
ExecutionResult result = graphQL.execute(query);

System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
System.out.println(result.toSpecification());
```

画面13:
```java
import static graphql.schema.GraphQLObjectType.newObject;
import static graphql.schema.GraphQLFieldDefinition.newFieldDefinition;

public class GraphQLDemo {
