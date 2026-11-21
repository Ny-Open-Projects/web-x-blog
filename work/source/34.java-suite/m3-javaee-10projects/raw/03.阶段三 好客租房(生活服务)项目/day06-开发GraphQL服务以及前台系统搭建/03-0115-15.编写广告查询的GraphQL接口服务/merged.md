# 15.编写广告查询的GraphQL接口服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\15.编写广告查询的GraphQL接口服务【海量资源尽在 ubkz.com】.mp4
- 时长 9分40秒（音频 580s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来实现广告服务的GrabQL的一个接口的服务的一个编写那么首先第一个呢我们对这个数据结构的做一个优化就是说之前我们呢可以看到前端所要求的数据结构呢是这个样子的其实通过前面我们的一个编写和分装这个结构会发现这个结构它不是一个很优的一个这样的一个结构所以呢我们需要对它做一些这个优化
[00:29] 然后呢我们去结合我们那个轮播组件的一个需求啊就是说我们这个在我们的前端呢其实它使用的是一个轮播广告的这样的一个组件啊这个组件其实只需要的是你返回的是一个这个集合啊就是一个这样的一个集合就可以了其实呢所以我们结合这样的需求啊我们只需要返回这个集合就OK所以我们把它优化后之后的一个数据呢就改成这个样子啊
[00:57] 改成这个样子就是返回一个对象对象中的包含一个listlist中的又是一个这个宿主宿主中的又是他的一些相关的一些这个图片的信息那么这样的话呢就比较是简单的一种结构啊前面这种结构呢不是特别的理想啊好嘞那么我们改成这种结构之后呢就以这个结构为准我们去呃给新编或者说实践我们那个grabql的一个接口那么首先呢我们需要去
[01:26] 对这个GrabQL文件的一个编写那么这个编写呢我就不一点一点去写了我就来做一个拷贝吧那么去首先呢先进入到我们这个API这个server的工程然后在它下面呢有一个有一个什么呢有一个resource我们找到这个resource下面的有一个好客GrabQL然后呢我们给他添加一个什么呢
[01:55] 添加一个indexAdList这样的一个查询查询的名字呢就叫它然后呢它的没有参数啊没有参数直接返回的类型呢就是indexAdResult所以呢我们需要在下面呢给它定义一个这个indexAdResult那么indexAdResult呢它的一个结构
[02:24] 是不是就参考我们刚刚的所说的结构你看它返回的结构是不是就是一个中间包含了listlist是一个竖组竖组中的一个内容就是一个对象它又是一个对象是吧所以我们设置为是一个indexedit, 一个data好那么下面我们来看一下这个对象这个对象我们给它定义一下那么它里面就包含了一个字段叫original
[02:53] 然后它是什么类型呢是String类型对吧你看它是这个的一个类型好那么我们这个结构是不是就搞定了那么接下来我们其实就要去编写一个我们的一个查询那么在这个下面还记得我们分装的这个接口吗我们来实现一个这个接口那么这个写一个类吧这叫什么呢AD是吧AD然后DataFetcher
[03:25] F E T C H E ROK那么我们写一个写一个他然后呢去实现我们的一个接口就是叫mydata好那么我们来实现这个方法那么可以看到这个里面有两个方法然后呢我们给他去写一个叫component是一个我们的一个组件的一个注解是不应组件的一个注解
[03:55] 然后呢field name其实前面我们说过啊他的field name就对应的就是上面的这个名称对吧就他然后呢把它贴过来然后呢可以看一下在下面这个位置那么这个里面怎么去玩呢所返回的一个object其实就是对应的我们这里的一个这样的一个对象对吧但是这个对象我们现在是不是还没有啊所以我们需要创建一个这个对象
[04:21] 那么这样吧我把你来靠下这个对象那么这个对象首先第一个就是我们index ad without对象然后我们还有一个是without date对象就是我们集合中的对象当然了这个对象我们这么玩我们把这个对象先删掉我们在下面我们再来创建一个包这个包的名字就叫ad
[04:51] AD然后index因为我们广告可能会有很多那么所以我们来一个AD下面index然后我们再去创建这两个类创建到这个下面要不然我们全部都丢到VU里面的话后面我们这个里面的类会越来越多了好然后我们再把下面这个Data这个类我们也拷过来把它拷贝放到这个里面来那么这样的话就OK了就按照我们刚刚的一个结构去做一个这样的一个分桌
[05:23] 好嘞那么这样的话就搞定然后我们就可以在我们刚刚写的ad data fetch中去做一个处理对吧最终其实我们需要返回的是一个index ad result这样的一个对象因为这个对象要和我们所定义的一个对象是不是做一个匹配做一个匹配我们来看一下这个应该怎么去分装我们去到这个里面去写一下逻辑
[05:49] 那么显然呢这个里面需要注的是谁呢是不是我们前面写的ad这个Service这个服务把它注进来把它注进来然后呢在这个里面呢我们就可以去调用了去调用它race.adservice.queryid list然后呢1然后呢page是1site是3是不是我们去拿这个三条数据拿到是一个叫做page info对吧一个对象
[06:18] 然后我们通过这个PageInfo这个对象就可以拿到一个recode对吧对他的一个数据那么拿到一个recode那么拿到这个ADS就是我们的数据拿到数据之后我们需要去对他做一个分装分装什么最终我们需要返回的是一个叫做ADIndexADResult对不对那么返回他那么是不是需要一个这个list
[06:46] 那么我们就先定义这样的一个listok那么我们在这个里面定义这样的一个list那么这个就叫list等于new一个arrival list那么它里面是不是需要这些对象那么它对象怎么来就去做一个便利做一个便利谁便利 ad然后我们就循环我们结果集对吧然后我们去这个里面给它去按的
[07:17] 按的去添加一个这个对象那就new一个这个index ad result date对象那么它里面呢是有一个构造函数那么我们就给它去设置一个ad点get什么get url好这样是不是就完成了它的一个构造对吧好那么得到这个对象是不是最终得到一个list然后呢最后返回是不是就直接new一个叫做index ad resultad result
[07:45] 然后呢我们给他去添加一个设置一个参数勾到函数设置一个参数那就list这样的话是不是就可以得到一个返回了ok好那么接下来呢我们是不是就可以进行做一个测试了对吧好那么我把我们这个服务呢重启一下那么我先把这个视频呢先暂停一下好那么现在呢我们这个服务呢重启好了下面我们来测试一下啊怎么测呢还要进入到我们这个GrabQL的client工具
[08:14] 那么我们添加一个这个添加一个查询啊然后呢设置一个get查询那么查询的一个这个呃结构呢是这样的那么首先呢我们来找到我们的一个呃这个这个名字啊那么就叫他啊index ad list那么有没有查询呃条件呢没有那么但是呢他里面的返回的是一个list对不对哎ok那么就邀请他返回一个list
[08:43] 那么list里面又会返回的是一个这个URL地址那么查询走查询来看一下是不是就正常的返回这个数据了那么可以看到我们返回的数据是不是就已经按照我们刚刚所定义的一个结构就是我们所期望的这样的一个结构是不是去做一个返回那么就是这样的一个结构这样的一个结构这样的一个结构你看
[09:14] 是一模一样的一个结构好这个位置来看一下这样的一个结构好那么其实到目前为止我们是不是已经写好一个GrabQL这样的一个接口对不对那么关键的问题就是我们的前端如何该如何去调用我们的这个接口那么下面我们是不是要解决这个问题OK好那么关于这个GrabQL的一个服务的一个编写我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在广告管理系统中使用 GraphQL 接口，优化数据结构并实现广告轮播图的查询功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 讲义第 4 章“广告服务的 GraphQL 接口”，子章节 4.1“数据结构优化”，并展示原始数据结构示例。
画面2：继续展示 4.1 节内容，说明优化后只需返回 list 数组和每个对象的 original 字段。
画面3：进入 4.2 节“编写 haoke.graphqls”，展示 GraphQL Schema 的初始定义。
画面4：展示 GraphQL Schema 中定义的 HouseResources 和 IndexAdResult 类型。
画面5：在 IntelliJ IDEA 中编辑 haoke.graphqls 文件，定义 IndexAdResult 类型。
画面6：在 IntelliJ IDEA 中编辑 AdDataFetcher.java 文件，定义 GraphQL 数据获取器。
画面7：在 IntelliJ IDEA 中右键点击 IndexAdResult.java 文件，选择“Delete”。
画面8：在 IntelliJ IDEA 中创建 IndexAdResultData 类，定义 original 字段。
画面9：在 IntelliJ IDEA 中修改 AdDataFetcher.java，注入 AdService 并返回 "IndexAdList"。
画面10：在 IntelliJ IDEA 中查看 AdDataFetcher.java 的完整代码，包含必要的导入和注解。
画面11：在 IntelliJ IDEA 中展示 AdDataFetcher.java 的完整代码，包含所有必要的导入和注解。
画面12：在 Altair GraphQL Client 中配置 GraphQL 接口地址。
画面13：在 Altair GraphQL Client 中发送请求，展示返回的广告图片 URL 列表。
画面14：展示 PDF 讲义中优化后的数据结构示例，与画面13的返回结果一致。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
{
  "data": {
    "list": [
      {
        "original": "http://127.0.0.1:8086/public/1.png"
      },
      {
        "original": "http://127.0.0.1:8086/public/2.png"
      },
      {
        "original": "http://127.0.0.1:8086/public/3.png"
      }
    ],
    "meta": {
      "status": 200,
      "msg": "测试数据"
    }
  }
}

画面2：
{
  "list": [
    {
      "original": "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/11/26/15432029946/21854.jpg"
    }
  ]
}

画面3：
schema {
  query: HaokeQuery
}

画面4：
type HaokeQuery {
  HouseResources(id:Long):HouseResources
  HouseResourcesList(page:Int, pageSize:Int):TableResult
  IndexAdList:IndexAdResult
}

type HouseResources {
  id:Long!
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
  useArea:String
  floor:String
  orientation:String
  decoration:Int
  facilities:String
}

画面5：
type IndexAdResult {
  list:[IndexAdResultData]
}

画面6：
package cn.itcast.haoke.dubbo.api.GraphQL;
import GraphQL.schema.DataFetchingEnvironment;

public class AdDataFetcher implements MyDataFetcher {
  @Override
  public String fieldName() {
    return null;
  }

  @Override
  public Object dataFetcher(DataFetchingEnvironment environment) {
    return null;
  }
}

画面8：
@Data
@AllArgsConstructor
@NoArgsConstructor
public class IndexAdResultData {
  private String original;
}

画面9：
@Component
public class AdDataFetcher implements MyDataFetcher {
  @Autowired
  private AdService adService;

  @Override
  public String fieldName() {
    return "IndexAdList";
  }

  @Override
  public Object dataFetcher(DataFetchingEnvironment environment) {
    return null;
  }
}

画面10：
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicLong;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.util.stream.DoubleStream;
import java.util.stream.FloatStream;
import java.util.stream.BaseStream;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;
import java.util

