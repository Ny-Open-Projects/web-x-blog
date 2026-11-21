# 画面线理解：22.GraphQL入门之通过SDL构建Schema

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\22.GraphQL入门之通过SDL构建Schema【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:16, 02:20, 03:25, 04:14, 05:02, 06:23, 07:03, 08:05, 09:07, 09:51, 10:46, 11:54, 12:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:03:38

1) 这一组画面整体在讲如何在 Java 项目中通过 GraphQL 的 Schema 定义和 RuntimeWiring 配置来构建并执行 GraphQL 查询。

2) 按时间顺序列出每张画面的要点：
画面 1：
- 在 IntelliJ IDEA 中，展示 `GraphQlDemo.java` 文件，其中定义了 GraphQL 对象类型 `User`，包含字段 `id`（GraphQlLong）、`name`（GraphQlString）和 `age`（GraphQlInt）。
- 同时定义了查询字段 `user`，并设置了参数 `id` 的数据获取器（dataFetcher）。

画面 2：
- 在 IntelliJ IDEA 中，右键点击项目目录 `src/main/java/itcast/graphq`，弹出菜单，选择“Create New Class”。
- 用于创建新的 Java 类。

画面 3：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件的创建过程。
- 项目结构显示 `src/main/resources/user.graphqls` 文件。

画面 4：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件的初始代码，其中定义了 GraphQL 查询 `user(id:100) {id,name}` 并执行。

画面 5：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中开始使用 `SchemaGenerator` 来生成 Schema。
- 代码中包含 `SchemaGenerator` 的构造函数和 `makeExecutableSchema` 方法。

画面 6：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中使用 `SchemaGenerator` 生成可执行的 Schema。
- 代码中包含 `new SchemaGenerator().makeExecutableSchema()`。

画面 7：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中使用 `SchemaParser` 解析 GraphQL 文件。
- 代码中包含 `new SchemaParser().parse(fileContent)`。

画面 8：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中使用 `IOUtils.toString` 方法读取 `user.graphqls` 文件内容。
- 代码中包含 `IOUtils.toString(GraphQLSDLDemo.class.getClassLoader().getResource(fileName))`。

画面 9：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中使用 `SchemaParser` 解析文件内容并创建 `TypeDefinitionRegistry`。
- 代码中包含 `new SchemaParser().parse(fileContent)`。

画面 10：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中创建 `RuntimeWiring` 对象并设置查询类型。
- 代码中包含 `RuntimeWiring.newRuntimeWiring().type(typeName: "UserQuery", builder -> ...).build()`。

画面 11：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中定义了 `UserQuery` 类型的数据获取器。
- 代码中包含 `builder.dataFetcher(fieldName: "user", environment -> { Long id = environment.getArgument(name: "id"); return new User(id, name: "张三:" + id, age: 20 + id.intValue()); })`。

画面 12：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中执行 GraphQL 查询并打印结果。
- 代码中包含 `System.out.println("query:" + query); System.out.println(result.toSpecification());`。

画面 13：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中修改了 GraphQL 查询，增加了 `age` 字段。
- 代码中包含 `String query = "{user(id:100) {id,name,age}}";`。

画面 14：
- 在 Adobe Reader 中，展示 PDF 文档的第 7.2.2 节“构建schema”，其中包含 Java 代码示例。
- 代码中包含 `import cn.itcast.graphql.vo.User;` 和 `import orgaql.schema.idl.TypeDefinitionRegistry;`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
public class GraphQLDemo {
    public static void main(String[] args) {
        /* type User {#定义对象}
        GraphQLObjectType userObjectType = newObject()
            .name("User")
            .field(newFieldDefinition().name("id").type(GraphQLLong))
            .field(newFieldDefinition().name("name").type(GraphQLString))
            .field(newFieldDefinition().name("age").type(GraphQLInt))
            .build();
        /* user : User #指定对象以及参数类型
        GraphQLFieldDefinition userFieldDefinition = newFieldDefinition()
            .name("user")
            .type(userObjectType)
            .argument(newArgument().name("id").type(GraphQLLong).build())
            .dataFetcher(environment -> {
                Long id = environment.getArgument(name: "id");
            });
    }
}
```

画面 3：
```java
package cn.itcast.graphql.demo;
public class GraphQLSDLDemo {
}
```

画面 4：
```java
import graphql.ExecutionResult;
import graphql.GraphQL;
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema: null).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 5：
```java
import graphql.schema.GraphQLSchema;
import graphql.schema.idl.SchemaGenerator;
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema();
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 6：
```java
import graphql.schema.idl.SchemaGenerator;
import graphql.schema.idl.TypeDefinitionRegistry;
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        TypeDefinitionRegistry typeRegistry = null;
        RuntimeWiring wiring = null;
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema();
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 7：
```java
import graphql.schema.idl.SchemaParser;
import graphql.schema.idl.TypeDefinitionRegistry;
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        String fileContent = null;
        TypeDefinitionRegistry typeRegistry = new SchemaParser().parse(fileContent);
        RuntimeWiring wiring = null;
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema(typeRegistry, wiring);
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 8：
```java
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        String fileName = "user.graphqls";
        String fileContent = IOUtils.toString(Reader input);
        TypeDefinitionRegistry typeRegistry = null;
        RuntimeWiring wiring = null;
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema(typeRegistry, wiring);
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 9：
```java
public class GraphQLSDLDemo {
    public static void main(String[] args) throws IOException {
        String fileName = "user.graphqls";
        String fileContent = IOUtils.toString(GraphQLSDLDemo.class.getClassLoader().getResource(fileName));
        TypeDefinitionRegistry typeRegistry = new SchemaParser().parse(fileContent);
        RuntimeWiring wiring = null;
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema(typeRegistry, wiring);
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 10：
```java
public class GraphQLSDLDemo {
    public static void main(String[] args) throws IOException {
        String fileName = "user.graphqls";
        String fileContent = IOUtils.toString(GraphQLSDLDemo.class.getClassLoader().getResource(fileName));
        TypeDefinitionRegistry typeRegistry = new SchemaParser().parse(fileContent);
        RuntimeWiring wiring = RuntimeWiring.newRuntimeWiring()
            .type(typeName: "UserQuery", builder -> {
