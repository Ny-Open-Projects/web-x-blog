# 画面线理解：04.通过Altair GraphQL Client插件进行测试GraphQL接口

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\04.通过Altair GraphQL Client插件进行测试GraphQL接口【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:20, 00:48, 01:19, 01:37, 02:12, 02:42, 03:21, 03:30, 04:25, 04:38, 05:07, 06:00, 06:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:07:44

1) 这一组画面整体在讲如何在 Chrome 浏览器中安装 Altair GraphQL Client 插件，并通过该插件测试后端 GraphQL 接口。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 PDF 文档中关于“1.6、chrome安装GraphQL client插件”的说明，包含插件安装地址：https://chrome.google.com/webstore/detail/altair-graphql-client/inheeeplciglpasdhkmapeljopja...（地址被截断）。
画面 2: 展示 IntelliJ IDEA 中的 GraphQlProvider.java 代码，其中包含 @Autowired 注解和 @PostConstruct 初始化方法。
画面 3: 展示 Chrome 浏览器的 Google 主页。
画面 4: 展示 Chrome 网上应用店的“扩展程序”页面。
画面 5: 展示 Chrome 网上应用店中 Altair GraphQL Client 插件的详情页。
画面 6: 展示 Altair GraphQL Client 插件的界面，已输入 GraphQL 服务地址 http://127.0.0.1:18080/graphql，右侧显示了返回的 JSON 数据。
画面 7: 展示 IntelliJ IDEA 中的 GraphQlController.java 代码，包含 @GetMapping 注解和执行 GraphQL 查询的逻辑。
画面 8: 展示 IntelliJ IDEA 中的 GraphQLDemo.java 代码，包含生成 Schema 和执行查询的逻辑。
画面 9: 展示 IntelliJ IDEA 中的 hooke.graphqls 文件，其中定义了 GraphQL Schema，包含 type HookeQuery 和 type HouseResources。
画面 10: 展示 Altair GraphQL Client 插件界面，已输入查询语句：{ HouseResources(id:1) }。
画面 11: 展示 Altair GraphQL Client 插件界面，已执行查询并返回了包含 HouseResources 对象的 JSON 数据。
画面 12: 展示 Altair GraphQL Client 插件界面的 Network 标签页，显示了请求的详细信息，包括 Request URL、Request Method 和 Status Code。
画面 13: 展示 PDF 文档中关于“1.6、chrome安装GraphQL client插件”的说明，包含插件安装地址：https://chrome.google.com/webstore/detail/altair-graphql-client/inheeeplciglpasdhkmapeljopja...（地址被截断）。
画面 14: 展示 PDF 文档中关于“1.6、chrome安装GraphQL client插件”的说明，包含插件安装地址：https://chrome.google.com/webstore/detail/altair-graphql-client/inheeeplciglpasdhkmapeljopja...（地址被截断）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2 代码：
```java
import javax.annotation.PostConstruct;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

// 实现的功能：将GraphQL对象放到Spring容器，并完成GraphQL对象的初始化
@PostConstruct
public void init() throws FileNotFoundException {
    File file = ResourceUtils.getFile(resourceLocation);
    this.graphQL = GraphQL.newGraphQL(buildGraphQLSchema(file)).build();
}
```

画面 7 代码：
```java
@GetMapping
@ResponseBody
public Map<String, Object> query(@RequestParam("query") String query) {
    return this.graphQL.execute(query).toSpecification();
}
```

画面 8 代码：
```java
.build();

// 生成Schema
GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema(typeRegistry, wiring);

// 根据Schema对象生成GraphQL对象
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();

String query = "{user(id:100) {id,name,age,card(cardNumber)}}";
ExecutionResult result = graphQL.execute(query);

System.out.println("query:" + query);
System.out.println(result.toSpecification());
```

画面 9 代码：
```graphql
schema {
  query: HookeQuery
}

type HookeQuery {
  HouseResources(id:Long) : HouseResources
}

type HouseResources {
  id:Long
  title:String
  estateId:Long
  buildingNum:String
  buildingUnit:String
  buildingFloorNum:String
  rent:Int
  rentMethod:Int
  paymentMethod:Int
  houseType:String
  coveredArea:String
  useFloor:String
  floor:String
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
