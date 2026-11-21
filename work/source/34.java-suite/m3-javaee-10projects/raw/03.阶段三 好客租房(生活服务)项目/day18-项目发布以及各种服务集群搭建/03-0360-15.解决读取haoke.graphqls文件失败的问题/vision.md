# 画面线理解：15.解决读取haoke.graphqls文件失败的问题

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\15.解决读取haoke.graphqls文件失败的问题【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:18, 01:36, 02:24, 02:41, 02:54, 03:09, 03:32, 03:45, 04:16, 04:25, 04:48, 05:01, 05:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:56:25

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 GraphQL，包括编写 GraphQLProvider 初始化代码、构建 GraphQL Schema、打包并部署服务，以及通过浏览器访问 GraphQL API。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 IDE 中查看 GraphQLProvider.java 文件，展示 @PostConstruct 初始化方法，其中使用 ResourceUtils.getFile 获取 haoke.graphqls 文件并构建 GraphQLSchema。
画面 2: 在 IDE 中，光标位于 init 方法内，展示通过 getClassLoader().getResourceAsStream 获取 haoke.graphqls 文件流。
画面 3: 在 IDE 中，光标位于 init 方法内，展示将 InputStream 转换为 String content。
画面 4: 在 IDE 中，展示 GraphQLProvider.java 文件，光标位于 buildGraphQlSchema 方法内，显示将 content 传入 SchemaParser 解析。
画面 5: 在终端中，进入项目 target 目录，列出打包后的 jar 文件。
画面 6: 在终端中，进入项目根目录，然后进入 haoke/dubbo 目录。
画面 7: 在终端中，进入 graphql 目录，列出 Java 文件，并删除 GraphQlProvider.java。
画面 8: 在终端中，进入 publish 目录，列出项目文件，并执行 mvn install 命令。
画面 9: 在终端中，显示 Maven 构建成功，列出各个模块的构建时间。
画面 10: 在终端中，显示 Maven 构建后生成的 jar 文件列表。
画面 11: 在终端中，显示 Dubbo 服务启动日志，包括 ZooKeeper 连接成功和服务注册信息。
画面 12: 在浏览器中，访问 http://192.168.1.7:8080/house/resource，显示资源列表。
画面 13: 在浏览器中，访问 http://192.168.1.7:8080/house/resource/page，显示分页后的资源列表。
画面 14: 在 IDE 中，展示 GraphQLProvider.java 文件，光标位于 buildWiring 方法内，显示为每个 DataFetcher 构建 RuntimeWiring。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
@Component
public class GraphQLProvider {
    @Autowired
    private List<MyDataFetcher> myDataFetchers;

    //实现对GraphQL对象的初始化
    @PostConstruct
    public void init() throws FileNotFoundException {
        File file = ResourceUtils.getFile(resourceLocation);
        this.graphQL = GraphQL.newGraphQL(buildGraphQlSchema(file)).build();
    }

    private GraphQLSchema buildGraphQlSchema(File file) {
        TypeDefinitionRegistry typeRegistry = new SchemaParser().parse(file);
        return new SchemaGenerator().makeExecutableSchema(typeRegistry, buildWiring());
    }

    private RuntimeWiring buildWiring() {
        return RuntimeWiring.newRuntimeWiring()
                .type(typeName: "HaokeQuery", builder -> {
                    for (MyDataFetcher myDataFetcher : myDataFetchers) {
                        builder.environment -> myDataFetcher;
                    }
                    return builder;
                });
    }
}
```

画面 2:
```java
InputStream inputStream = GraphQLProvider.class.getClassLoader().getResourceAsStream("haoke.graphqls");
```

画面 3:
```java
String content = IOUtils.toString(inputStream, "UTF-8");
```

画面 4:
```java
private GraphQLSchema buildGraphQlSchema(String content) {
    TypeDefinitionRegistry typeRegistry = new SchemaParser().parse(content);
    return new SchemaGenerator().makeExecutableSchema(typeRegistry, buildWiring());
}
```

画面 5:
```bash
cd target/
ls
```

画面 6:
```bash
cd src/
cd itcast/
cd haoke/
cd dubbo/
```

画面 7:
```bash
cd graphql/
ls
rm GraphQLProvider.java
```

画面 8:
```bash
cd publish/
ls
mvn install -Dmaven.test.skip=true
```

画面 9:
```bash
[INFO] Installing /haoke/publish/itcast-haoke-manage-dubbo-server/itcast-haoke-manage-dubbo-server-ad-service/1.0-SNAPSHOT.pom to /haoke/repo/cn/itcast/itcast-haoke-manage-dubbo-server-ad-service/1.0-SNAPSHOT.pom
[INFO] Reactor Summary for itcast-haoke-manage 1.0-SNAPSHOT:
[INFO] itcast-haoke-manage ................................ SUCCESS [ 1.410 s ]
[INFO] itcast-haoke-manage-dubbo-server .................. SUCCESS [ 0.015 s ]
[INFO] itcast-haoke-manage-dubbo-server-common ........... SUCCESS [ 4.431 s ]
[INFO] itcast-haoke-manage-dubbo-server-house-resources ... SUCCESS [ 0.297 s ]
[INFO] itcast-haoke-manage-dubbo-server-ad-interface ...... SUCCESS [ 0.031 s ]
[INFO] itcast-haoke-manage-dubbo-server-ad-service ........ SUCCESS [ 0.195 s ]
[INFO] itcast-haoke-manage-dubbo-server-house-resources-dubbo-service SUCCESS [ 3.305 s ]
[INFO] itcast-haoke-manage-dubbo-server-ad-service ........ SUCCESS [ 2.826 s ]
[INFO] BUILD SUCCESS
[INFO] Total time: 55.775 s
[INFO] Finished at: 2019-02-28T22:50:09+08:00
```

画面 10:
```bash
ls
```

画面 11:
```bash
INFO 12093 --- [main] c.a.d.c.b.s.f.a.ReferenceBeanBuilder : <dubbo:reference singleton="true" object="com.alibaba.dubbo.server.api.ApiAdService" interface="cn.itcast.haoke.dubbo.server.api.ApiAdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiAdService" />
INFO 12093 --- [main] c.a.d.c.b.s.f.a.ReferenceBeanBuilder : <dubbo:reference singleton="true" object="com.alibaba.dubbo.server.api.ApiHouseResourcesService" interface="cn.itcast.haoke.dubbo.server.api.ApiHouseResourcesService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiHouseResourcesService" />
```

画面 12:
```json
{
  "created": 1548029400000,
  "writer": "1548029400000",
  "id": 0,
  "type": "0000",
  "build": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.0",
  "buildTime": "1.
