# 15.解决读取haoke.graphqls文件失败的问题

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\15.解决读取haoke.graphqls文件失败的问题【海量资源尽在 ubkz.com】.mp4
- 时长 5分42秒（音频 342s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们解决一下刚刚我们在启动我们的API Server这个API Server的这个服务的时候我们报的一个错误其实错误原因是我们在这个位置去读起我们ClassPass下面的hawk.webql文件读不到原因是我们使用的Spring中的这个工具类去读那么我们把我们的这个文件打包到我们的一个加包里面的话它是读不到的那么这个问题怎么解决呢我们需要去换一种写法去做实现
[00:30] 那么就不能采用这种方式了那么怎么做呢我们可以这样来做那我们就通过这个我们的内加载器去读取就可以了比如说它的class.loader.getResource那么iStream就可以拿到一个什么的inputStream那么有了inputStream那么是不是就可以去得到一个我们的一个
[00:55] 这个拿到我们的字幕串了对吧那么我们所以说应该这么来玩叫get as stream那么这个里面呢传递谁呢就传递的是这个浩克浩克.webqls那么就他然后下面这个我们就注册掉了然后这个拿到之后拿到什么内容呢其实拿到的是一个input stream那么input stream怎么去转成字幕串呢我们可以这样来拿叫做contact吧
[01:25] contact等于叫做通过IOIO util然后呢我们使用apache的util.m然后呢有一个叫做toString然后呢传递一个inputString然后再指定一个编码叫UTF-8去做一个这样的一个指定那么它有异常的是去抛出异常的我们就直接抛出exception吧然后呢就拿到一个contact那么把这个contact呢传递到我们这个里面来
[01:53] 那么在我们这个build的这个方法中啊它接收的是一个fail那么其实我们没有必要去拿到一个去接收fail了拿到内容就可以了因为它这种解析呢是解析你这个文件中的内容的啊那么这样的话呢我们就换了一种思路就去通过我们内加载器去拿到我们这个文件中内容那么因为我们最终的目的最终的目标呢还是要去读取到我们文件中的内容啊关键是拿到它OK好那么这样的话呢我们就
[02:21] 可以这么来玩一下就是我们把这个文件我们拷贝到我们的比如说拷贝到桌面桌面已经存在这个文件我就替换一下然后我就进入到进入到我们这个17这个下面然后我去得这么玩一下那么cd点点回去然后进入src下面我们找到这个找到这个java的一个代码然后cn下面有一个itcast然后进入这个浩克
[02:50] 然后呢我们再去进入double然后呢再进入API然后再进入grabql就这个目录啊就在这那我们把这个grabql这个加网文件给它删除掉删除掉之后呢我们再去做一个上传这一块我们刷新一下啊那么就没了然后呢我们做一个上传把它呢上传到我们这个里面来那么相当于我们增量的去修改了一个文件那么等待它的上传上传之后啊
[03:19] 那么这个文件是不是就有了然后呢我们再回到浩克下面一个publish下面呢我们再回到这个里面来我们把刚刚那个执行的命令呢我们再来执行一下然后到这执行那么等待他的一个这个安装成功呢我们就会重新得到一个新的包然后我们再去做一个测试就OK了好那我们稍微等待一下好那么现在呢我们也重新的打包完成了那我们就来找一下我们打好的一个包那么进入到这个API这个server
[03:50] 这个里面然后呢我们再去进入这个target下面呢我们去找到我们这个加包然后呢我们cp一下这个加包到hawk下面呢有个publish下面有个hawk那么把它复制过来那么复制过来之后呢我们就会得到一个新的一个这个加包那么重新来启动一下就可以了那么就这个API server这个加包走那么我们等待它的一个启动然后呢我们就可以做一个测试了
[04:19] 那我们来看一下它的启动有没有报错呢如果没有报错那就说明我们这个服务呢它是一个OK的服务啊我们可以来测试一下那么可以看到它添加了我们三个这个ES的这个节点OK好那么到目前为止呢就已经跑起来了没有任何错误啊那么我们就可以来尝试的访问一下那么通过这个192.168.1.7.180.80那么house resource去做一个访问走
[04:48] 那么OK你可以看到那么现在我们是不是已经拿到数据了对吧那么当然你还可以去做一些这个配置做一些这个分页比如说去配置3那么是不是也可以拿到数据OK好那么我们现在就已经是拿到数据了那就说明什么说明我们这个服务已经是OK了那么他说
[05:09] 连接到的我们double的服务是不是也是OK的那么其实到目前为止我们是已经把我们的后台系统的服务是不是就已经就搞定了但是目前为止我们还并没有去通过域名去访问这个我们放到后面统一去做一个处理就是我们可以通过NGX去做一个访问OK好那么关于刚刚我们在部署我们这个API server的时候
[05:33] 报的这个错误就是我们读取不到GrabQL这个错误呢我们就解决到这里那么这个问题呢我们就解决了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 GraphQL，包括编写 GraphQLProvider 初始化代码、构建 GraphQL Schema、打包并部署服务，以及通过浏览器访问 GraphQL API。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 IDE 中查看 GraphQLProvider.java 文件，展示 @PostConstruct 初始化方法，其中使用 ResourceUtils.getFile 获取 haoke.graphqls 文件并构建 GraphQLSchema。
画面 2: 在 IDE 中，光标位于 init 方法内，展示通过 getClassLoader().getResourceAsStream 获取 haoke.graphqls 文件流。
画面 3: 在 IDE 中，光标位于 init 方法内，展示将 InputStream 转换为 String content。
画面 4: 在 IDE 中，展示 GraphQLProvider.java 文件，光标位于 buildGraphQlSchema 方法内，显示将 content 传入 SchemaParser 解析。
画面 5: 在终端中，进入项目 target 目录，列出打包后的 jar 文件。
画面 6: 在终端中，进入项目根目录，然后进入 haoke/dubbo 目录。
画面 7: 在终端中，进入 GraphQL 目录，列出 Java 文件，并删除 GraphQlProvider.java。
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
cd GraphQL/
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
[INFO] Installing /haoke/publish/itcast-haoke-manage-dubbo-server/itcast-haoke-manage-dubbo-server-ad-Service/1.0-SNAPSHOT.pom to /haoke/repo/cn/itcast/itcast-haoke-manage-dubbo-server-ad-Service/1.0-SNAPSHOT.pom
[INFO] Reactor Summary for itcast-haoke-manage 1.0-SNAPSHOT:
[INFO] itcast-haoke-manage ................................ SUCCESS [ 1.410 s ]
[INFO] itcast-haoke-manage-dubbo-server .................. SUCCESS [ 0.015 s ]
[INFO] itcast-haoke-manage-dubbo-server-common ........... SUCCESS [ 4.431 s ]
[INFO] itcast-haoke-manage-dubbo-server-house-resources ... SUCCESS [ 0.297 s ]
[INFO] itcast-haoke-manage-dubbo-server-ad-interface ...... SUCCESS [ 0.031 s ]
[INFO] itcast-haoke-manage-dubbo-server-ad-Service ........ SUCCESS [ 0.195 s ]
[INFO] itcast-haoke-manage-dubbo-server-house-resources-dubbo-Service SUCCESS [ 3.305 s ]
[INFO] itcast-haoke-manage-dubbo-server-ad-Service ........ SUCCESS [ 2.826 s ]
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

