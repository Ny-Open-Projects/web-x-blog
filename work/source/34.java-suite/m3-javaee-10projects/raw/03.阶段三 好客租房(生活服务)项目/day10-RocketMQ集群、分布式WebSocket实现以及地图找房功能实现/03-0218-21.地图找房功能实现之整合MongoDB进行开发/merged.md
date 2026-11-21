# 21.地图找房功能实现之整合MongoDB进行开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\21.地图找房功能实现之整合MongoDB进行开发【海量资源尽在 ubkz.com】.mp4
- 时长 11分41秒（音频 702s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们基于mongoDB呢来做一个具体的一个查询那么我们需要在我们的这个manager这个API这个系统中啊我们来导入来导入在这啊来导入我们的mongoDB相关的这个依赖把它呢拷过来然后呢我们就在下面这个位置吧把它添加到这哎OK好那么这样的话呢添加完成没问题吧别添加错了那么这个下面
[00:30] OK添加是对的没有问题那么添加完成之后我们需要给它添加一个mongodb的一个配置好拷贝然后进入到我们的API这个server下面找到最下面有一个application properties文件然后我们给它拷贝到最下面去OK好那么现在我们是不是这个就已经拷贝这个是有点问题我看一下这个是2185冒号是不是多了一个1
[01:00] 27017它是db这样就没有问题了刚刚多了一个1这个没有问题好那么这个配置搞定之后呢我们就需要去给它去编写一些这个具体的一个代码那么首先呢我们需要编写的是我们的一个实体因为我们要去通过我们这个mongo db是不是查询到我们的数据刚刚我们看到查询这个数据要有一个对象与之做一个映射所以呢我们需要去创建一个这个pojo这个包来保存我们这个对象
[01:30] 那么进入到这个里面来就是在这然后呢我们创建一个这个package这个包那就叫pojo这个包那么pojo下面呢我们需要给它创建一个这个类呢就叫mongo一个host好把它拷贝一下然后呢我们把它贴过来那么它自然的会导入一些相关的一些这个包object id把它呢也导入进来好嘞
[01:56] 那么这个是不是就对应到我们的mongodb里面的一个几个字段我们来看一下id那就不用说了就是我们下滑线 id对吧然后还有就是hid就是房源的id然后标题还有就是我们的一个地理位置那么地理位置我们在mongodb中所保存的结构是这样的一个结构就是一个竖组中间保存了两个我们的一个经纬度的数据所以在这个位置我们通过一个flot的一个竖组做一个接收
[02:25] 好嘞,那么有了这个之后我们下面就可以去编写我们的一个逻辑了那么下面我们来看我们的一个查询那么编写一个叫做mongo,mongo host Service在这个Service包下面创建这样的一个类那么在这个里面我们先把它添加为这是一个Service那么这个里面我们想要去操作mongo db那么需要住谁是不是住一个mongo
[02:54] Mongo这个叫template模板把这个模板是不是注入进来那么有了这个模板之后呢我们就可以去做一些数据MongoDB数据的一个查询那么怎么查呢我们就这样咱们就把这个逻辑我们就直接拷贝过来吧我们定义这样的一个方法定义这样的方法通过什么呢通过我们的这个中心点的一个精纬度一个精度和纬度
[03:22] 然后再去通过他的一个这个说放笔做一个这个查询那么我们来看一下那么最终我们查询的逻辑应该是这样去来对吧那么我们就这么来把它一点一点拷贝过来那么最后return其实return的是我们的一个maphouse.datereadult就我们定义的这样的一个对象然后他需要一个list那么这个list其实我们是定义一个他
[03:52] 第一个这样的一个list就是xy的这个list好嘞那么这个xy怎么填充呢是需要我们通过mongodb是不是去做一个查询啊怎么查询呢是不是通过类似点这个mongodbtemplate点是不是做一个这个fed做一个查询对吧那么第一个参数是一个query第二个参数呢就是我们刚刚锁定的那个mongo那个mongohost.class那么我们来看这个query应该怎么构造那么query呢我们是应该这样来构造
[04:22] 把这个query拷贝过来那么我们来看一下这个query在这OK那么我们来看一下那么这个query我们要根据一个条件什么条件呢就local这个条件local条件通过这个Nil附近附近把我们这个查询目标点的这个经纬度传递给他然后我们去查找他附近附近的多少公里之内的一个数据所以这个需要我们去
[04:54] 给他去做一个计算怎么计算呢就需要参考我们前面所说的他的一个说放比所对应的一个公里数那么我们前面说过是按照他的一个说放比的对应的公里数的1.5倍对吧那么这个怎么玩呢应该是这样来玩那么我们先在我们的上面需要去定义我们这样的一个数据就是他的一个说放比所对应的一个我们的一个公里数可以看到啊比如说他的12所对应的是5公里对吧
[05:24] 然后呢这个19对应的是20这个19对应的是这个20D除以100020D呢代表什么意思就是20公里除以1000其实就是那个20米这样的意思啊因为我们单位统一成都是这个千米啊就是公里啊好嘞那么有了这个之后呢我们就可以做一个计算了怎么计算呢来看一下那么我们去计算它的一个这个就是
[05:53] 就相当于换一个圆了半径是我们缩放比的1.5倍对吧来看一下那么通过我们缩放比拿到我们里面的具体的一个它的一个比例尺就多少公里然后我们再乘以1.5乘以1.5是不是就1.5倍然后再去除以111.12这个前面我们是不是也说过对吧要除以它就会得到我们查询的一个范围
[06:19] 然后传递给他就会得到我们这样的一个数据那我们来看他的数据就是一个这个host对吧然后呢在这个里面呢我们需要给他做一个便利就好了便利谁呢便利的是他是不是拿到他然后呢我们只需要去给他去按的添加就好了点点按的去添加一个new一个这个XY那么他需要一个XY那么怎么拿到这个XY呢
[06:50] 那么我们就通过这个mongo host点get什么get local然后呢中括号0对吧然后呢再来一个点get localget local然后呢中括号1因为它是一个数组01拿到它的一个经纬度那么就是它的一个xy这样的话是不是就可以返回数据了来看一下对不对啊那么在这个位置拿到它没有问题好那么下面呢我们就需要去修改我们的这个
[07:21] datafetcher这个里面去做一个数据的一个查询那么在这那么在这个里面我们就就不需要这样去构造数据了对不对那么不需要构造这个数据那么这个就不需要了那么我们需要怎么玩是不是在上面这个位置把我们刚刚所写的这个mongo的一个houseresourceservice注入进来然后我们把它注入进来之后我们就可以去调用它了那么就可以直接return了对吧
[07:51] retrace.Service.query它那么传递三个参数lng,lat然后还有一个zom是不是做这样的一个查询那么下面这个retrace也就不需要了是不是真正我们去查询mongodb了OK
[08:08] 好嘞那么我们这个就暂时先给它保留这个打印吧到后面我们如果测试这个效果没有问题的话就可以把它删掉了然后呢我们现在接下来是不是就可以把我们这个服务做一个重启然后呢整合到我们的前端去做一个测试看它结合到MangoDB是不是OK的呢当然了这个里面还有个小的一个细节点需要我们去调一下就是我们需要把我们的那个我们默认的那个地址改成上海因为
[08:37] 默认地址他是在北京我们的数据都是在上海所以把默认的一个城市给他去调一下把这两个我们拷过来在我们的前台的系统中这个位置把它改一下改成上海默认的是在人民工厂默认点是在人民工厂12然后下面北京我们要改成上海好嘞好那么接下来我们等待它的一个启动之后
[09:05] 那么就可以来做一个我们具体的一个测试了好等待它的一个启动好那么现在呢我们就已经启动好了我们来测试一下啊点击我们这个房源地图找房然后来看一下它呢默认已经进入这个上海市并且呢已经查询出来有有这么几套这个数据啊然后我点击这个加号把这个地图放大那么在拖动是不是也是OK的对吧也是OK的其实我们可以看到它那个刚刚我们所看到拖动
[09:35] 会有半透明的效果是不是还是存在的对吧ok然后放大看一下然后是不是可以看到在中山公园附近是不是有这么几套房然后在人民广场附近看一下人民广场人民广场是在这个位置是在这个位置有这么几套房应该是数据是对的你看这边人民广场
[10:03] 人民广场在这个位置有腹地有这么几套房然后呢看看房源的显示有两套只有两套三套啊三套哎OK那么大概呢是这样的一个呃总共我们的十个数据看对不对啊这个是三个三个六八九再有一个十条数据哎没问题啊是对的啊
[10:24] 所以说呢我们可以看到通过我们前后端一个整合是不是就看到这样的一个效果了对吧就看到这样的效果了那么OK好那么到目前为止呢我们是不是就已经去对接到我们的后端查询了芒果DB然后呢去把这个数据最终是不是就显示出来了OK当然了我们现在其实还有一个没有做就是我们的数据现在有点不太够有点不太够因为毕竟我们在造数据嘛
[10:53] 如果大家比较感兴趣的话可以去抓一些数据或者是说其实我们也不应该去抓因为我们是做这样的平台应该是自己去上传一些数据的对不对所以但是我们现在已经把逻辑都已经搞好了那么我们只要把数据装到我们的芒果地位里面那么我们是不是就可以实现这样的效果表示随便可以去如果你数据多的话随便可以这样拖转都可以显示出对应的数据出来对不对OK好那么
[11:20] 关于我们这个地图找房的功能我们就基本我们就实现这么多了那么还有一些没做的功能包括我点击这个可以再继续去查看这个下面的方圆把地图放大等等一些这种效果他没有去做那么OK那么这个我们就to do了好那么关于地图找房的一个功能的实现我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现基于 MongoDB 的房屋数据查询功能，包括定义实体类、编写服务层代码、配置数据源以及前端页面展示。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 PDF 文档“5.6.1 导入依赖”，内容为“5.6.6.3 编写pojo”，并列出目录结构，当前页码为 34。
画面2: 显示 IntelliJ IDEA 中的 `application.properties` 文件，内容为 Dubbo 注册中心和 Redis 集群配置。
画面3: 显示 PDF 文档“5.6.3 编写pojo”，内容为 `MongoHouse` 实体类的 Java 代码，包含 `@Data`、`@AllArgsConstructor`、`@NoArgsConstructor`、`@JsonSerialize` 等注解。
画面4: 显示 IntelliJ IDEA 中创建 `MongoHouseService` 类的弹窗。
画面5: 显示 PDF 文档“5.6.3 编写pojo”，内容为 `MongoHouseService` 类的 Java 代码，包含 `@Service` 注解和 `@Autowired` 注解。
画面6: 显示 PDF 文档“5.6.3 编写pojo”，内容为 `MongoHouseService` 类的 Java 代码，包含 `@Autowired` 注解和 `queryHouseData` 方法的定义。
画面7: 显示 IntelliJ IDEA 中 `MongoHouseService` 类的 Java 代码，内容为 `queryHouseData` 方法的实现，包含 `Query` 查询条件和 `List<MapHouseXY>` 的构造。
画面8: 显示 IntelliJ IDEA 中 `MongoHouseService` 类的 Java 代码，内容为 `queryHouseData` 方法的实现，包含 `List<MapHouseXY>` 的构造。
画面9: 显示 IntelliJ IDEA 中 `MapHouseDataFetcher` 类的 Java 代码，内容为 `dataFetcher` 方法的实现，包含 `System.out.println` 输出调试信息。
画面10: 显示 PDF 文档“5.6.3 编写pojo”，内容为前端 JavaScript 代码，包含 `render` 函数和 `div` 标签。
画面11: 显示浏览器中前端页面，内容为“地图找房”页面，包含“2层”、“3层”等按钮和一个红色标记点。
画面12: 显示浏览器中前端页面，内容为“地图找房”页面，显示了地图和多个房屋标记点。
画面13: 显示 PDF 文档“5.6.1 导入依赖”，内容为 MongoDB 查询示例，包含 `db.house.find` 的查询语句和返回结果。
画面14: 显示浏览器中前端页面，内容为“地图找房”页面，显示了地图和多个房屋标记点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```
dubbo.registry.address = ZooKeeper://172.16.55.185:2181
dubbo.registry.client = zkclient
# redis集群配置
spring.redis.jedis.pool.max-wait = 5000
spring.redis.jedis.pool.maxIdle = 100
spring.redis.jedis.pool.minIdle = 10
spring.redis.timeout = 10
spring.redis.cluster.nodes = 172.16.55.185:6379,172.16.55.185:6380
spring.redis.cluster.max-redirects=5
```

画面3:
```
package cn.itcast.haoke.dubbo.api.pojo;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "house") // 指定表的名称
public class MongoHouse {
    @Id
    @JsonSerialize(using = ToStringSerializer.class)
    private ObjectId id;
    private String title;
    private String desc;
    private String price;
    private String area;
    private String houseType;
    private String houseDirection;
    private String houseStatus;
    private String houseImg;
    private String houseUrl;
    private String houseLocation;
    private String houseAddress;
    private String housePhone;
    private String houseEmail;
    private String houseWebsite;
    private String houseDescription;
    private String houseTags;
    private String houseKeywords;
    private String houseNote;
    private String houseRemark;
    private String houseRemark2;
    private String houseRemark3;
    private String houseRemark4;
    private String houseRemark5;
    private String houseRemark6;
    private String houseRemark7;
    private String houseRemark8;
    private String houseRemark9;
    private String houseRemark10;
    private String houseRemark11;
    private String houseRemark12;
    private String houseRemark13;
    private String houseRemark14;
    private String houseRemark15;
    private String houseRemark16;
    private String houseRemark17;
    private String houseRemark18;
    private String houseRemark19;
    private String houseRemark20;
    private String houseRemark21;
    private String houseRemark22;
    private String houseRemark23;
    private String houseRemark24;
    private String houseRemark25;
    private String houseRemark26;
    private String houseRemark27;
    private String houseRemark28;
    private String houseRemark29;
    private String houseRemark30;
    private String houseRemark31;
    private String houseRemark32;
    private String houseRemark33;
    private String houseRemark34;
    private String houseRemark35;
    private String houseRemark36;
    private String houseRemark37;
    private String houseRemark38;
    private String houseRemark39;
    private String houseRemark40;
    private String houseRemark41;
    private String houseRemark42;
    private String houseRemark43;
    private String houseRemark44;
    private String houseRemark45;
    private String houseRemark46;
    private String houseRemark47;
    private String houseRemark48;
    private String houseRemark49;
    private String houseRemark50;
    private String houseRemark51;
    private String houseRemark52;
    private String houseRemark53;
    private String houseRemark54;
    private String houseRemark55;
    private String houseRemark56;
    private String houseRemark57;
    private String houseRemark58;
    private String houseRemark59;
    private String houseRemark60;
    private String houseRemark61;
    private String houseRemark62;
    private String houseRemark63;
    private String houseRemark64;
    private String houseRemark65;
    private String houseRemark66;
    private String houseRemark67;
    private String houseRemark68;
    private String houseRemark69;
    private String houseRemark70;
    private String houseRemark71;
    private String houseRemark72;
    private String houseRemark73;
    private String houseRemark74;
    private String houseRemark75;
    private String houseRemark76;
    private String houseRemark77;
    private String houseRemark78;
    private String houseRemark79;
    private String houseRemark80;
    private String houseRemark81;
    private String houseRemark82;
    private String houseRemark83;
    private String houseRemark84;
    private String houseRemark85;
    private String houseRemark86;
    private String houseRemark87;
    private String houseRemark88;
    private String houseRemark89;
    private String houseRemark90;
    private String houseRemark91;
    private String houseRemark92;
    private String houseRemark93;
    private String houseRemark94;
    private String houseRemark95;
    private String houseRemark96;
    private String houseRemark97;
    private String houseRemark98;
    private String houseRemark99;
    private String houseRemark100;
```

画面6:
```
static {
    BAI_DU_ZOOM.put(19, 20d / 1000);
    BAI_DU_ZOOM.put(18, 50d / 1000);
    BAI_DU_ZOOM.put(17, 100d / 1000);
    BAI_DU_ZOOM.put(16, 200d / 1000);
    BAI_DU_ZOOM.put(15, 400d / 1000);
    BAI_DU_ZOOM.put(14, 800d / 1000);
    BAI_DU_ZOOM.put(13, 1600d / 1000);
    BAI_DU_ZOOM.put(12, 3200d / 1000);
    BAI_DU_ZOOM.put(11, 6400d / 1000);
    BAI_DU_ZOOM.put(10, 128

