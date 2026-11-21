# 04.通过Altair GraphQL Client插件进行测试GraphQL接口

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\04.通过Altair GraphQL Client插件进行测试GraphQL接口【海量资源尽在 ubkz.com】.mp4
- 时长 6分25秒（音频 385s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们进行测试那么前面呢我们把这个代码逻辑都已经写好了对吧那么可以看一下provider那这个呢就是将我们的GraphQL这个对象注册到我们的Spring的容器啊然后呢下面呢我们进行做一个测试那么首先呢我们需要把这两个服务呢跑起来第一个呢就是我们这个double的这个服务把它跑起来第二个呢就是我们把API这个server跑起来那么跑起来之后呢
[00:28] 他呢就对外提供了webql这样的一个接口服务那么下面呢我们就要针对于这个webql做一个测试那么要想去测试webql那么我们就需要去安装一个谷歌的一个插件那么基于这个谷歌浏览器安装这样的一个插件进行做一个测试那我们可以来找一下那么我们去他的应用里面去去做一个搜索到他的网上的应用商店的去做一个搜索在这呢需要给大家强调的一点是
[00:57] 谷歌的网上应用商店是需要去翻墙去才能够访问到的这个需要大家自行去解决一下这个问题我其实也尝试着给大家去看这个插件是否能够离线的安装但是好像发现不行所以就只能去大家去找一下了找一下这个
[01:19] 找一下这个如何去翻墙对吧这个问题要自己把它解决掉那么我们在这个应用商店那去做一个搜索我搜一个GrabQL对吧那么我们就可以看到这样的这样的一个插件那么搜索一下那么其实就是第二个这个插件我们点击进去来看一下那么由于我现在已经安装好了对吧它所以显示的是从Chrome中删除那么如果你没有安装它显示的是这个添加到Chrome中
[01:48] 然后呢这是一个还是比较好用的工具啊OK那么其实安装比较简单你点击一下这个位置的一个添加到添加到QRM中那么就可以完成一个安装了非常简单那么安装好之后呢在这个位置呢会有这样的一个会有这样的一个小的图标那么点击这个图标呢它就会打开我们的这个插件那么打开这个插件之后呢我们就需要去写一下这里面一些内容啊那么把这个清一点清清楚一下然后呢我们再去
[02:18] 这样吧我添加一个把这个就这个保留吧好那么我们来看一下这个工具怎么用怎么用那么首先我们看这个位置那么我们去给他设置一个get请求然后请求谁请求是我们这个地址要注意的是我们这个地址是不是前面我们在写Controller的时候我们是不是指定了这样的一个请求的一个路径grabql对吧然后我们要求
[02:44] 你做一个get请求那么必须要传递一个query这样的一个参数所以我们这个位置去设置是一个get请求这个是我们的地址那么下面就需要去设置我们的一个查询的一个支付串那么查询支付串前面我们在做学习GrabQL的时候已经知道那么它其实是一个json这样的一个结构对不对所以我们就按照这样的一个结构去给它去做一个设置一个查询的参数就可以了
[03:13] 那么我们这个位置要查询什么呢是不是查询我们的host那么要注意的是这个他呢没有提示啊那么现在他呢还没有提示那么我们就需要去找一下他的一个这个结构那么回到我们这个项目中在结构里面我们要查询是不是他呀host啊resource那么你要对应到这个位置来写一下hostresource那么查询参数呢是不是就idid呢我们给他设置是1然后呢我们要查询哪些字段那么比如说我要查询这个
[03:41] 这么多这个字段吧我随便写一些啊随便写一些那么我把后面的这个给他拿掉这个不需要后面的这个是我们不需要的把它拿掉那么我我只需要查询这么几个字段就可以了好哎把这个拿掉然后呢我点击这个发送走那么就可以看到是不是已经查询到数据了那么当我继续继续给他去添加我们这个字段的时候那么他是不是就会继续请求到我们新的这个字段哎OK
[04:10] 当你去减少的时候我不需要这个制度那么是不是也可以去查询到那个你不想要那个制度对不对那个制度你不查询了吗好那么这样的话呢其实我们就完成了一个测试啊来完成个测试那么我们可以打开我们这个开发者这个工具啊然后呢我们在我们的network里面去做一个查看当我们点击这个发送这个请求的时候呢他会发送什么样的请求呢我们来看一下他那个请求的一个内容
[04:39] 那么我们可以看到他请求的是一个做一个get请求对吧然后他后面会传递一个query等于什么什么这个是不是就是我们刚刚所写的这个查询的一个json的字符创那么我们只需要通过这个query拿到一个查询这个字符创那么传递到我们这个API里面是不是就可以完成一个查询那个动作最后呢是不是把我们的结果是不是做一个返回那就OK了好
[05:07] 那么这个工具这个插件呢用起来是非常简单的啊非常简单的那么呢也可以做一些其他的操作包括呢它可以做一些这个美化就是说我们有些时候你写的这个格式比如说有点不太对比如说我多加一个table键啊这格式呢是有点不太对的对吧你可以点一下它帮你做一个这个格式化那么我们点击发送哎OK那么这样的话看起来更加美观一点啊那么也可以去做一些这个压缩
[05:33] 我们可以把我们请求资格不算压成这一行是不是就和我们在我们做这种demo测试的时候这个应该还有印象那么是不是做这样的一个测试对吧还像这样的一个写法ok那么当然其他的就我们暂时可能就用不着了对吧那么我基本的用法就是这些用法ok
[05:53] 好那么点击这个发送就可以了好这个就是我们使用了一个这个小的一个插件然后呢对我们的GrabQL的一个接口的一个测试啊一个测试哎OK好那么这个呢大家要自己想想办法去做一下安装了那个离线版的是安装不了哎OK然后呢这个安装后进行做一个测试是这样做一个测试哎OK好那么关于我们编写的这GrabQL的一个
[06:21] 这个服务的一个测试呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Chrome 浏览器中安装 Altair GraphQL Client 插件，并通过该插件测试后端 GraphQL 接口。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 PDF 文档中关于“1.6、chrome安装GraphQL client插件”的说明，包含插件安装地址：https://chrome.google.com/webstore/detail/altair-GraphQL-client/inheeeplciglpasdhkmapeljopja...（地址被截断）。
画面 2: 展示 IntelliJ IDEA 中的 GraphQlProvider.java 代码，其中包含 @Autowired 注解和 @PostConstruct 初始化方法。
画面 3: 展示 Chrome 浏览器的 Google 主页。
画面 4: 展示 Chrome 网上应用店的“扩展程序”页面。
画面 5: 展示 Chrome 网上应用店中 Altair GraphQL Client 插件的详情页。
画面 6: 展示 Altair GraphQL Client 插件的界面，已输入 GraphQL 服务地址 http://127.0.0.1:18080/GraphQL，右侧显示了返回的 JSON 数据。
画面 7: 展示 IntelliJ IDEA 中的 GraphQlController.java 代码，包含 @GetMapping 注解和执行 GraphQL 查询的逻辑。
画面 8: 展示 IntelliJ IDEA 中的 GraphQLDemo.java 代码，包含生成 Schema 和执行查询的逻辑。
画面 9: 展示 IntelliJ IDEA 中的 hooke.graphqls 文件，其中定义了 GraphQL Schema，包含 type HookeQuery 和 type HouseResources。
画面 10: 展示 Altair GraphQL Client 插件界面，已输入查询语句：{ HouseResources(id:1) }。
画面 11: 展示 Altair GraphQL Client 插件界面，已执行查询并返回了包含 HouseResources 对象的 JSON 数据。
画面 12: 展示 Altair GraphQL Client 插件界面的 Network 标签页，显示了请求的详细信息，包括 Request URL、Request Method 和 Status Code。
画面 13: 展示 PDF 文档中关于“1.6、chrome安装GraphQL client插件”的说明，包含插件安装地址：https://chrome.google.com/webstore/detail/altair-GraphQL-client/inheeeplciglpasdhkmapeljopja...（地址被截断）。
画面 14: 展示 PDF 文档中关于“1.6、chrome安装GraphQL client插件”的说明，包含插件安装地址：https://chrome.google.com/webstore/detail/altair-GraphQL-client/inheeeplciglpasdhkmapeljopja...（地址被截断）。

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
```GraphQL
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

