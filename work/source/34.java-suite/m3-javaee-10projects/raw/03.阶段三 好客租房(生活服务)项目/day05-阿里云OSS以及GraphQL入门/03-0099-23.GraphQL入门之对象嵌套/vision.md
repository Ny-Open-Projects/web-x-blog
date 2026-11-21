# 画面线理解：23.GraphQL入门之对象嵌套

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\23.GraphQL入门之对象嵌套【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:29, 01:26, 01:53, 02:14, 02:39, 03:34, 04:18, 04:44, 05:05, 05:40, 06:23, 06:43, 07:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:04:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中使用 GraphQL，包括创建工程、定义 Schema、构建对象模型（User 和 Card）以及实现数据查询和返回。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示创建新工程的界面，Group Id 为 cn.itcast.graphql，Artifact Id 为 itcast-graphql-java，Version 为 1.0-SNAPSHOT。
画面 2: 展示构建 Schema 的代码片段，package 为 cn.itcast.graphql.demo，import 了 cn.itcast.graphql.vo.User。
画面 3: 展示对象嵌套的概念，说明要创建 Card 对象，与 User 对象建立一对一关系。
画面 4: 展示 Card 类的 Java 代码，包含私有字段 cardNumber 和 userId，以及对应的 getter 和 setter 方法。
画面 5: 展示 User 类的 Java 代码，包含私有字段 id、name、age 和 Card card，以及对应的构造函数和 getter/setter 方法。
画面 6: 展示 user.graphqls 文件的内容，定义了 UserQuery 类型和 User 类型，其中 User 类型包含 id、name 和 age 字段。
画面 7: 展示 GraphQLSchema 对象的生成代码，以及根据 Schema 生成 GraphQL 对象的代码。
画面 8: 展示 DataFetcher 的实现代码，用于根据 id 查询 User 对象。
画面 9: 展示运行结果，显示查询成功返回了 User 对象的信息。
画面 10: 展示修改后的 DataFetcher 代码，用于返回包含 Card 对象的 User 对象。
画面 11: 展示修改后的 DataFetcher 代码，用于返回包含 Card 对象的 User 对象。
画面 12: 展示运行结果，显示查询成功返回了包含 Card 对象的 User 对象的信息。
画面 13: 展示 User 类的 Java 代码，包含私有字段 id、name、age 和 Card card，以及对应的构造函数和 getter/setter 方法。
画面 14: 展示测试用例，包括查询 user(id:1) 的 id 和 name，以及查询 user(id:1) 的 id、name、card 和 userId。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
New Project
Group Id: cn.itcast.graphql
Artifact Id: itcast-graphql-java
Version: 1.0-SNAPSHOT

画面 2:
package cn.itcast.graphql.demo;
import cn.itcast.graphql.vo.User;

画面 3:
下面，我们创建一个 Card 对象，User 和 Card 对象为一对一的关系。

画面 4:
package cn.itcast.graphql.vo;
public class Card {
    private String cardNumber;
    private Long userId;
    public Card() {
    }
    public Card(String cardNumber, Long userId) {
        this.cardNumber = cardNumber;
        this.userId = userId;
    }
    public String getCardNumber() { return cardNumber; }
    public void setCardNumber(String cardNumber) { this.cardNumber = cardNumber; }
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
}

画面 5:
public User() {
    this.id = id;
    this.name = name;
    this.age = age;
}

画面 6:
schema {
    query: UserQuery
    type UserQuery {
        user(id:Long) : User
    }
    type User {
        id:Long!
        name:String
        age:Int
    }
}

画面 7:
// 生成Schema
GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema(typeRegistry, wiring);
// 根据Schema对象生成GraphQL对象
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
String query = "{user(id:1)}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.toSpecification());

画面 8:
builder.dataFetcher(fieldName: "user", environment -> {
    Long id = environment.getArgument(name: "id");
    return new User(id, name: "张二" + id, age: 20 + id.intValue(), card: null);
})

画面 9:
String query = "{user(id:100){id,name,age,card(cardNumber,userId)}}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.toSpecification());

画面 10:
RuntimeWiring wiring = RuntimeWiring.newRuntimeWiring()
    .type(typeName: "UserQuery", builder -> {
        builder.dataFetcher("user", environment -> {
            Long id = environment.getArgument(name: "id");
            return new User(id, name: "张三" + id, age: 20 + id.intValue(), card: null);
        });
    })
    .build();

画面 11:
RuntimeWiring wiring = RuntimeWiring.newRuntimeWiring()
    .type(typeName: "UserQuery", builder -> {
        builder.dataFetcher("user", environment -> {
            Long id = environment.getArgument(name: "id");
            Card card = new Card(Number: "123456789", id);
            return new User(id, name: "张三" + id, age: 20 + id.intValue(), card);
        });
    })
    .build();

画面 12:
String query = "{user(id:100){id,name,age,card(cardNumber,userId)}}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.toSpecification());

画面 13:
public class User {
    private Long id;
    private String name;
    private Integer age;
    private Card card;
    public User() {
    }
    public User(Long id, String name, Integer age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
}

画面 14:
return RuntimeWiring.newRuntimeWiring()
    .type(typeName: "UserQuery", builder -> {
        builder.dataFetcher("user", environment -> {
            Long id = environment.getArgument(name: "id");
            Card card = new Card(Number: "123456789", id);
            return new User(id, name: "张三" + id, age: 20 + id.intValue(), card);
        });
    })
    .build();

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: 标题为“7.2.3、对象嵌套”，内容说明要创建 Card 对象，与 User 对象建立一对一关系。
画面 6: 标题为“7.2.2、构建schema”，内容为 GraphQL Schema 的定义，包括 query 和 type。
画面 14: 标题为“测试”，内容为 GraphQL 查询语句的测试用例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
