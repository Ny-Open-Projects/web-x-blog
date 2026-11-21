# 05.优化改进GraphQLProvider实现逻辑

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\05.优化改进GraphQLProvider实现逻辑【海量资源尽在 ubkz.com】.mp4
- 时长 14分50秒（音频 890s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么刚刚呢在我们实现了我们的GrabQL之后啊那么我们是通过这个provider然后呢去将我们的这个GrabQL对象载入到Spring的中继中那么功能已经实现了前面我们测试过了没有问题但是回过头来我们来看一下在我们实现的这个过程中啊那么它有没有一些
[00:25] 问题或者说有没有些什么逻辑啊需要我们去优化的呢我们来看一下其实呢它是有优化的那么需要优化的点呢其实就是在这个方法中啊那我们来看一下在这个方法中呢我们去构造了我们这个查询的逻辑对不对你看是不是这样的查询逻辑那么我们现在是不是只是只有一个查询对吧只有一个查询
[00:48] 那我们就通过这个datefactor去做一个查询那么如果那么我后面会有很多的查询的比如说这个有一个什么叫list对吧然后呢还有什么1还有什么2哎ok那么假设啊我有这么多的一些查询那么有这么多查询那么也就意味着我是不是需要在这个位置对吧给他有设置什么的多个datefactor那么这个表示1
[01:15] 这个是二这个是三哎OK大概呢表达一下这个意思啊那么我是不是需要在这个位置设置很多的这个data factor那么大家可以想象一下那么后面我们这个查评可能会越来越多那么也就意味着我这个方法呢是不是需要不断的去做一个修改并且呢在这个位置我要不断添加这么多逻辑那么如果有一些逻辑变得非常复杂的话那这个里面写的内容是不是就非常多那么这样就会导致我们的这个方法
[01:43] 是不是越来越庞大越来越臃肿那么这显然不是一种好的编程的一些方式所以我们需要对这个方法做一些优化那么怎么样去做优化呢那么我们可以想一下那么我们是不是可以把这个具体的这个业务逻辑可以丢到外面的一个内中去完成对吧而在这个位置呢我们只需要拿到那个内
[02:07] 去做一个执行就可以了ok是不是可以采用这样的一种方式对这个逻辑做一个优化ok好那么咱们还是把刚刚这个先给它还原回去ok那我相信现在大家已经是能够理解这个意思了我们为什么要去做一个优化那么最底怎么玩这么来玩那么在这个在这个包下面我要包下面我们创建一个接口
[02:35] 这个接口的名字呢我们其实就叫它my data factor那么在这个接口中呢我们来给它定义一些方法那么定义哪些方法呢我们就需要来看一下在这个位置对吧那么首先它需要是一个叫做field name对吧你看是不是需要一个field name那么我们就给它定义一个这个field name的一个方法因为每一个查询啊
[03:00] 他的这个field name都是不一样的对吧所以每一个查询呢他都需要去返回一个field nameok这个能够理解吗field name就是我们查询的名称我们加一个注释吧这个就是我们的一个QL中的这个查询名称对吧查询的一个名称就是一个名字那么他是不是所对应的就是我们这个位置的他呀ok这是第一个这个方法
[03:30] 第二个方法呢我们是在处理这个environment这个参数啊就是说传递给我们这个environment这个参数之后我们去做一个处理然后呢我们返回一个obj的对象就可以了所以呢我们就在这个方法中啊我们就定义一个方法名就叫data factor吧那么返回值呢就叫obj然后方法名叫data factor然后呢传递的一个参数是谁呢我们来看一下那我们进入到这个
[03:59] data venture中那它是不是接收一个data venture然后呢我们点进去下面呢是不是有这样的一个方法那么参数其实就是这个参数那么我们把它拿过来那么我们放到这个位置参数就就它对吧OK那么这个方法其实处理的就是我们数据的一个查询对吧数据的查询哎OK好那么我们根据这个evaluate是不是就可以去拿到我们的一些这个参数啊哎OK好那么我们这个接口是不是就就定义OK了
[04:29] 那么接口定UK之后呢我们是不是就可以把这个逻辑把这个逻辑我们是不是可以改造一下对吧那么把这个逻辑呢我就先给它去做一个注释给它注掉然后呢我们在下面这个位置来看一下怎么玩呢那么在这个位置是使用了一个箭头函数那么我们就这个位置来一个这个括号对吧来一个这个大括号然后呢给它去return啊return什么的return这个build
[04:57] 好然后呢在这个里面我们去写一下这个逻辑啊写什么逻辑呢就是我们需要拿到我们的这个所有的这个接口啊所有的这个接口的一个实现类那么这个怎么玩呢这么来玩那么我们就进入到那个provider里面啊咱们在这那么我让他呢去spring帮我去注进来注什么呢注这个集合因为我们这个类的实现类啊可能会有很多
[05:25] 可能会有很多所以我们就注了一个实现类然后我们把它注进来注的是一个集合好嘞然后在下面这个位置我们只需要去对它做一个什么复循环对吧复循环谁呢就是mydatafetcher那么拿到它之后怎么玩呢把它是不是拿过来那就直接来写是不是就是一个build.datafetcher
[05:52] 第一个呢我们拿着它的一个failed name那就是叫点什么呢叫failed name那第二个呢就是我们通过这个my data factor然后呢点来一个data factor然后呢我们把这个environment是不是传递过去那么这environment怎么去拿到呢我们去还是使用这个箭头这个函数那么拿到这个environment那么把它传递过去这样的话我们是不是就实现这样的一个效果了
[06:22] 好那么下面这个逻辑是不是就不需要了对吧咱把这个逻辑把这个逻辑给它去掉把这个代码格式我们去整理一下好这样的话我们是不是就搞定了那么接下来我们只需要去编写它的实现类就可以了然后继续往下面看这个注入是不是也不需要了把它拿掉好嘞那么这个也不要了那么把这个代码去整理一下好那么我们现在逻辑是不是就变成这样的一个逻辑了OK好那么
[06:51] 接下来我们就在这个下面去继续编写它的实现类那么我们写一个类叫什么的hostresource然后我们写一个叫什么呢就叫data-fetcherdata-fetcher好然后我们让这个类我们去实现一个接口就是我们刚刚写的my-data-fetcher就它
[07:20] 然后我们去实现这个内中的两个方法把这两个方法我们拿过来我们两个方法都去做一个实现然后我要注意的是那么我们在这个位置需要去把它标记为是一个component就需要我们的sprint去扫描一下它对吧把它作为一个组件去注册然后是不是就可以去注入到我们这个provider中的集合里面来注到这对吧ok好那么接下来我们继续那么在下面的我们这个
[07:49] houseresource.factor中那我们来看一下这个实现类应该怎么去做那么它的返回的一个field name是不是就是我们刚刚可以看到的是不是就是它就这个查询的这个名字查询的名字那么我们把它放到这个里面来就是它然后下面的这个实现怎么做是不是跟我们刚刚写逻辑是一样的对吧那我们就再来写一下evaluament然后点getget一个什么呢
[08:17] argument参数是不是就是通过一个id去获取到它的一个参数那么我们拿到的其实就是什么呢是不是就是一个id然后呢它的类型呢是一个none类型的id然后呢我们把那个Service是不是注入进来叫househousehouseresourceservice把这个Service注入进来好那么到这我们去给它注入进来
[08:45] 那么注入进来之后呢我们就需要在这个位置去调用他类似点这个hostresourceservice点什么呢query这个byid这个方法把这个id传递给他那么我们是不是就拿到这样的一个对象了哎呀ok好那么接下来呢我们来做一个测试做一个测试那我们来看一下当我们的spirit启动之后他是否能够在这个provider中去注这样的一个做这样的一个集合呢我们来看一下这样咱们在
[09:15] 这个位置来打一个断点打一个断点我们debug来启动一下好那么我们来把它去停止然后呢我们去做一个debug的一个启动那么到这个位置来走那么启动之后呢我们第一呢来看一下它是否能够输入第二呢我们来看一下我们的功能呢是否是ok正常的
[09:35] OK那么如果他是正常的话那么以后呢我们要去实现一些其他的一些查询的方法的时候那我们是不是只需要去实现一些相关的这个实现类是不是就可以了哎OK这个里面的逻辑是不是就不需要做任何的一个改动了啊不需要做任何的改动了好嘞好那么现在我们可以看到他呢还没有完全启动起来那我们稍等一下好到他已经来了那么在这个里面呢我们断点已经进入OK那么来看一下
[10:04] 那么我们当前是不是有一个这个my data factors当前这次他做的是一个arrival list看到了吗是不是一个arrival list对吧是一个集合那么这个集合它里面的一些这个对象有哪些呢我们来看一下诶等一下这个里面的对象呢现在是不是有一个对象只有一个对象就是我们这个house result data factors就这个对象ok那么以后我们有多个的时候它是不是也可以去注入进来ok然后呢我们通过
[10:34] 把这个断点我们就通过了然后呢我们断点就可以打到什么呢再次打到我们这个实现内中那实现到这那么我们是不是就可以做一个查询了对吧来做一个查询来看一下效果那我点击这个查询走那么会发现断点是不是已经进入我这个方法那么可以看到在这个位置是不是它已经断点进入了然后呢我们继续往下面走一步走走一步呢我们看这个ID拿到没有看拿到ID的值是不是就是1
[11:02] 然后呢我们通过这个Service这个serviceSpring有没有帮我们注入呢那肯定有是不是也注入进来了那么做查询那肯定就没有任何问题了对不对走通过那段点我就拿掉了然后我们来看一下测试这个结果跟我们刚刚测试结果是不是一模一样没有任何的区别啊比如说我们再去哎没有没有其他的了吗没有没有提示啊没有提示那这样我们来去找一下
[11:30] 我们再去查询几个字段随便查几个字段比如说我们查询这个它的一个地址来看一下是不是查询到数据了没有任何问题包括我们查询图片来看一下有没有问题这个数据是没有的换一个数据比如说我们查询数据ID为8的这个数据来看一下是不是有这样的一些这个数据所以说我们这个实现的一个功能是没有任何问题的那么OK
[11:58] 那么我们是不是通过这样的一个优化改进那么我们就对我们这个逻辑是不是做了一些这个优化改进那么以后呢只要去实现不同的这个data virtual接口就可以了哎OK那么这种改进的这种优化的这种思想啊希望大家能够去学会这种思想好那么我们来看一下我们的讲义啊那么优化改进我们这个provider这个逻辑那么问题呢其实就是我们刚刚所分析的在这个这个方法中的一些问题所在那么
[12:27] 当我们以后去增加这个查询的时候都必须要修改这个方法而且我们查询的方法很多的话这个方法会变得非常的难以维护所以我们需要做改进这个是不是跟我们刚才分析的是一样的哎呀ok那么改进的思路是怎么来看一下第一个呢编写一个接口然后呢去第二呢是所有实现查询逻辑的都要实现这个接口那么这个接口是不是就刚刚我们所写的那个my data factory这样的一个接口那么所有具体查询的逻辑就实现这个接口就可以了
[12:56] 然后呢带我在我们的这个provider这个中呢使用该接口的进行这该接口的实现类进行做一个处理而不是把这个具体逻辑写到这个位置不是这样的而是通过我们具体实现类去做一个处理那么以后我们新增查询呢只需要去新增实现类就可以了哎OK好这个就是我们的一个这个优化改进的一个逻辑啊
[13:19] 那么具体的一个实现呢我们编写这样的一个接口跟我们应该写的是一样的啊然后呢我们去改进一个它改进这个是这个是我们具体的一个实现house resource具体的一个实现ok那么这个别忘记啊component的别忘记好那么去实现这个接口实现这两个方法ok然后呢下面呢我们继续往下面看在这个位置呢我们去修改我们的provider的这个逻辑
[13:44] 在这个里面的我们非常重要的一点是在这我们需要Spring帮我们去注入这个容器中的所有这个类型的对象那么然后把它去以一个集合的一个类型给我们注入进来OK这个Spring是不是也可以做到对吧然后我们在下面的这个位置中就可以对我们的这个集合中的一个对象去做一些这个便利
[14:07] 便利之后呢都去分别调用它的一个data factor这样的一个处理对吧拿到它的一个fail name再去调用它的data factor的一个处理逻辑那么ok就可以去做一个具体逻辑的一个处理了ok那么注意这个位置的一个编写我们使用的Lamb的表达式注意这个地方有个括号括号要把它括起来在这个位置括起来然后呢要别忘记有一个return build把这个传入这个build对象给它返回回去哎呀ok
[14:34] 好那么这样的话呢我们会做一个重启做一个测试测试结果跟前之前是不是一致啊哎OK好这个就关于我们的一个provided具体的一个逻辑的一个改进那么这个改造呢这个逻辑呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 GraphQL，通过定义数据获取器（MyDataFetcher）和配置 GraphQLProvider 来实现 GraphQL 查询功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 `GraphQlProvider.java` 文件中的 `@PostConstruct` 初始化方法，用于加载 GraphQL Schema 文件并构建 GraphQL 对象。
- 代码片段：
  ```java
  @PostConstruct
  public void init() throws FileNotFoundException {
      File file = ResourceUtils.getFile(resourceLocation: "classpath:haoke.graphqls");
      this.graphQL = GraphQL.newGraphQL(buildGraphQlSchema(file)).build();
  }
  ```

画面 2：
- 展示了 `buildGraphQlSchema` 方法，用于解析 GraphQL Schema 文件。
- 展示了 `buildWiring` 方法，用于构建 GraphQL 的数据获取逻辑。
- 代码片段：
  ```java
  private GraphQLSchema buildGraphQlSchema(File file) {
      TypeDefinitionRegistry typeRegistry = new SchemaParser().parse(file);
      return new SchemaGenerator().makeExecutableSchema(typeRegistry, buildWiring());
  }
  ```

画面 3：
- 展示了 `buildWiring` 方法中定义的 GraphQL 查询类型 `HaokeQuery`。
- 代码片段：
  ```java
  private RuntimeWiring buildWiring() {
      return RuntimeWiring.newRuntimeWiring()
          .type(typeName: "HaokeQuery", builder ->
              builder.dataFetcher(fieldName: "HouseResources", environment -> {
                  Long id = environment.getArgument(name: "id");
                  return this.houseResourcesService.queryHouseResourcesById(id);
              })
          ).build();
  }
  ```

画面 4：
- 展示了 `MyDataFetcher` 接口的定义，用于定义 GraphQL 查询的数据获取器。
- 代码片段：
  ```java
  package cn.itcast.haoke.dubbo.api.GraphQL;
  public interface MyDataFetcher {
  }
  ```

画面 5：
- 展示了 `MyDataFetcher` 接口的实现类 `HouseResourcesDataFetcher`。
- 代码片段：
  ```java
  @Component
  public class HouseResourcesDataFetcher implements MyDataFetcher {
      @Override
      public String fieldName() {
          return "HouseResources";
      }
      @Override
      public Object dataFetcher(DataFetchingEnvironment environment) {
          Long id = environment.getArgument(name: "id");
          return this.houseResourcesService.queryById(id);
      }
  }
  ```

画面 6：
- 展示了 `GraphQlProvider` 类中 `@Autowired` 注解的 `myDataFetchers` 字段，用于注入所有实现 `MyDataFetcher` 接口的类。
- 代码片段：
  ```java
  @Autowired
  private List<MyDataFetcher> myDataFetchers;
  ```

画面 7：
- 展示了 `GraphQlProvider` 类中 `@PostConstruct` 方法的注释，说明其功能是初始化 GraphQL 对象。
- 代码片段：
  ```java
  @PostConstruct
  public void init() throws FileNotFoundException {
      File file = ResourceUtils.getFile(resourceLocation: "classpath:haoke.graphqls");
      this.graphQL = GraphQL.newGraphQL(buildGraphQlSchema(file)).build();
  }
  ```

画面 8：
- 展示了 `HouseResourcesDataFetcher` 类的定义，用于实现 GraphQL 查询的数据获取器。
- 代码片段：
  ```java
  @Component
  public class HouseResourcesDataFetcher implements MyDataFetcher {
  }
  ```

画面 9：
- 展示了 `HouseResourcesDataFetcher` 类中 `fieldName` 方法的实现，用于返回查询字段名。
- 代码片段：
  ```java
  @Override
  public String fieldName() {
      return "HouseResources";
  }
  ```

画面 10：
- 展示了 `DubboApiApplication` 类的主方法，用于启动 Spring Boot 应用。
- 代码片段：
  ```java
  @SpringBootApplication
  public class DubboApiApplication {
      public static void main(String[] args) {
          SpringApplication.run(DubboApiApplication.class, args);
      }
  }
  ```

画面 11：
- 展示了 `GraphQlProvider` 类中 `buildWiring` 方法的调试信息，显示 `myDataFetchers` 数组中包含 `HouseResourcesDataFetcher` 对象。
- 调试信息：
  ```
  myDataFetchers = [HouseResourcesDataFetcher@6250]
  ```

画面 12：
- 展示了 `haoke.graphqls` 文件中的 GraphQL Schema 定义。
- 代码片段：
  ```GraphQL
  schema {
      query: HaokeQuery
  }
  type HaokeQuery {
      HouseResources(id: Long): HouseResources
  }
  type HouseResources {
      id: Long!
      title: String
      estateId: Long
      buildingNum: String
      buildingUnit: String
      buildingFloorNum: String
  }
  ```

画面 13：
- 展示了 PDF 文档中关于编写 `MyDataFetcher` 接口的说明。
- 代码片段：
  ```java
  package cn.itcast.haoke.dubbo.api.GraphQL;
  import GraphQL.schema.DataFetchingEnvironment;
  public interface MyDataFetcher {
  }
  ```

画面 14：
- 展示了 PDF 文档中关于修改 `GraphQlProvider` 逻辑的说明。
- 代码片段：
  ```java
  package cn.itcast.haoke.dubbo.api.GraphQL;
  import GraphQL.GraphQL;
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第 2 点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- PPT 标题：1.7.1、1.7.3
- 表格数据：无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

