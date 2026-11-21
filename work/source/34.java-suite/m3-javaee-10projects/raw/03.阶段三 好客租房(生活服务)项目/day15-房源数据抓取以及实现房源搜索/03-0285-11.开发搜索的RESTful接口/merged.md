# 11.开发搜索的RESTful接口

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\11.开发搜索的RESTful接口【海量资源尽在 ubkz.com】.mp4
- 时长 15分11秒（音频 912s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来开发我们的搜索的接口那么为我们前端的提供这样的接口服务那么我们依然呢是在Manager这个API Server工程中去做一个开发那么首先呢我们在这个工程中先导入Spring Boot的这个Spring Boot的一个Data Elixir那么把它呢先导入进来那么我们把它呢拷贝一下诶,拷贝然后呢我们找到我们的工程啊是在
[00:29] 这个下面啊别搞错然后呢这个里面呢就把它加到最下面吧这个位置无所谓啊那么就加到下面那么加入完成之后呢我们就需要在我们的配置文件中啊是不是添加elaxus集群的配置那么找到这个resource然后呢我们去把它丢到这个最下面要注意这个位置的一个换行那么我们来看一下这个呢是指定我们集群的一个名字啊然后呢下面是不是就是三个
[00:58] 集群的这个节点去给它指向就可以了那么在这个位置使用的端口呢是9300不是那个9200这个要别搞错了好那么接下来呢我们来编写一些相关的一些这个代码首先我们需要编写的第一个呢是VU就是我们需要将我们的从数据从我们的一来个设置中查询到之后呢有一个对象的一个映射要映射一个对象中啊所以呢我们把这个内容我们拷贝过来
[01:24] 然后呢我们把它丢到哪里呢丢到我们的一个这个VO这个里面来那么VO呢我们就直接丢到这个里面吧丢到这然后呢我们把这个代码格式呢做一下这个处理这个是没有导入进来吗那么它需要导入的呢就是这个document第一个这个OK好嘞那么我们可以看到在这个里面呢我们是不是已经指向了它的一些指定一些配置那么包括它的index的name
[01:52] 以及type以及后面的这个create index force因为不需要创建因为我们现在已经创建好了然后呢下面来看一下这个位置呢就是所对应的一些我们的一些数据的字段那么我们其实在这个位置只配置了一个是吧就是ID但其他的它默认也会去加入到这个映射的一个这个队列中的就会做一个一的映射那么你不加那个fail的注解也可以也是可以的但是呢我们在这个位置给它指向一个这个IDOK
[02:19] 好那么我们这个ID呢来看一下ID呢就是它去自动生成的这样的一个ID这样的一个ID所以呢我们使用这个Stream去做一个这个接收好那么这个就搞定了那么下面呢我们还需要一个这个VU就是用于我们数据的一个响应给我们前端是不是去响应的一个这样的一个对象我们把它称之为叫做Search Result其中有两个内容一个呢就是我们的Total Pages总页数一个呢就是我们的数据
[02:48] 这个数据呢就刚刚我们所写的这个对象好那么接下来呢我们把这个对象的拷贝过来然后呢去丢到哪里呢丢到这里面来丢到这儿然后呢把这个代码格式呢我们去整理一下那么上面这个就不解释了这个相信大家应该非常熟悉了OK好那么接下来我们继续往下面看那么下面呢边写一个Controller那么这个Controller的名字呢就叫search Controller那么我们来找一下找到我们的工程然后呢找到这个Controller
[03:19] 然后它的名字就要search Controller然后呢在这个里面呢我们需要给它添加一些注解那么这三个注解是必不可少的对吧拷贝一下那么到这个里面来这三个注解把它呢导入进来好那么这个呢是指向我们那个就是UR的对吧UR的一个路径然后呢这个呢是指向rest Controller那么我们下面再去写我们响应的时候呢就不需要写那个responsibility然后呢这个CROSS这个呢是去支持跨域的对吧
[03:50] OK这三个注解那么接下来呢我们去实现我们这个方法咱们把这个拷贝过来也是比较简单的一个实现那我们来看一下那么在这个里面呢把这个相关的一些这个包呢我们导入进来把它呢这个API对了API下面的view没问题然后呢这个设置一会儿呢我们再去写一个看一下这个一个不对啊它现在怎么已经导入进来了显然这个是不对的我们还没有创建这个需要我们自己创建一个设置Service
[04:19] 那么在这个Controller中呢我们去接收啊去接收两个参数一个就keyword就是我们的查询的关键字另外一个呢就是page就是我们的一个分页的一个页数然后在这个位置呢我们做一个判断如果我们这个传入这个page的一个大小大于100的话那么就设置为1那么其实我们可以看到那个链加网是不是也是这么去做的啊只要加一个这样的一个判断那么就可以去防止耳爬虫去抓取我们过多的一些数据啊其实我们这样做的目的啊
[04:47] 第一个呢是防止这个爬虫去抓取过多的数据那么另外一个呢其实就是来减少我们的electrode的一个它的一个这个性能吧或者它的一个压力那么前面我们在讲的时候其实说到我就是electrode它去做这个数据的一个分页的时候它是需要去取到前面的这个你的这个数量是吧from加sign这个数量的所以说你越往后面去分页的话它其实这个效率是越低的
[05:16] 所以我们为了去保证我们Elexus它的性能我们也会限制它是在100页以内当然了100也并不是说固定就100还是需要在去做项目的时候要和产品经理把这个数字要搞清楚我们是100还是50还是200这个一定要搞清楚好那么我们现在就有必要去创建一个search Service然后去实现我们的具体的搜索的逻辑那么我们来看一下
[05:44] 在Service这个包下面呢就写一个search Service然后呢我们去给他加一个注解叫做Service好那么来看一下这个里面的内容的编写哎好那么来看一下那么我们找到啊找到我们这个简易中的这个Service然后呢在这个里面我们来看一下啊呃先把他们两个先拿过来来看一下那么这两个呢就非常容易理解了首先去注入elect search的template模板呃然后呢第二个呢就是我们需要
[06:13] 去定义我们的一个这个行数就是我们每一页拿多少行那么要注意的一点是我们在做搜索引擎的时候呢是不允许用户在前端给我们去输入这个肉死去也就是说不允许用户来指定一页返回多少条数据那么这个必须由我们后端程序去做一个控制大家可以想一下为什么那么如果前端可以控制我们返回的这个数据行数的话那我们是不是这个数据很危险
[06:39] 对吧有可能比如说给你设置一千一万那么你的数据是不是一下全部都返回了那么第一你的数据数据容易被别人抓到第二呢就是我们会给我们的Alexis造成非常大的影响对吧或者这个压力OK所以说这个一定要注意不能开放出去然后接下来呢我们就需要去实现具体的业务逻辑了那我们实现一个这个设置这个方法我们先把它呢先拷贝过来
[07:06] 好那么我们来看一下在这个里面它需要返回一个search result我们把这个search result给它去导入进来导入进来之后这个里面的代码逻辑我们来看一下也是相对比较简单的一个代码逻辑
[07:19] 那么我们首先给他设置一个配置request然后呢呃这个位置要注意一下我们这个配置呢要去配置简易那么在前面我们在讲的时候呢这个点没有去讲到那么现在我们去说一下啊他呢是需要第一页是从零开始所以我们要来个配置简易啊这一点一定要注意那么这个很容易会踩到一个坑里面比如说啊你查询的数据刚好只有一页的话那么你会发现如果说你没有简易的话啊假设没有这个简易的话那你会发现你拿到数据拿不到
[07:48] 你可能会有疑惑我为什么没有拿到数据呢这样的一个疑惑其实是在这个问题这个位置的问题然后下面我们就需要去构造一个search query这个对象然后在这个里面我们去设置了一个叫什么呢match query就是做一个匹配通过一个title去做一个匹配
[08:07] 那么匹配谁呢匹配我们的关键字就是我们用户数的关键字然后呢如果有我们分词之后呢有多个词的话就要求它的一个操作是一个什么操作呢按的操作啊这样的一个query啊然后呢下面设置这个设置配置然后呢再去设置我们高亮的一个字段哎OK这样的话就可以去做一个查询了好那么我们把这个下面的这个逻辑啊这个拷贝过来然后呢丢到这那么这样的话呢我们就基本上就实现了一个查询了
[08:35] 好那么咱们把代码简单的去调整一下整理一下格式然后第一个第一个差然后我们做一个分割好那么这样的话这个是不是去构造我们的一个查询然后这个去做真正的一个查询最后是不是指定我们映射的对象是这个host data就我们刚刚所创建的对象然后最后可以反回一个host page这样的一个对象然后去返回一个new一个这个设置result
[09:04] 就可以了好嘞那么这样的话呢我们就可以在在我们的这个Controller中是不是去导入我们刚刚所写的这个Service对吧然后呢我们去做一个导入的还是不对导错了那我们再来看一下需要导入的是下面的这个下面第一个就是它导入进来好这回是不是就OK了好嘞那么到这里呢我们这个基本上呢就OK了对吧然后呢我们去做一个启动就把我们这个
[09:33] 这个项目能跑起来OK那么我们来试一下当然了这个现在可能会有点问题就是那么我们这个项目其实它要依赖于我们下面的一些这个服务对吧依赖于这种服务那么我还是把它都跑起来吧如果不跑的话是跑不起来的那么我需要找一下我上面执行的一个执行的一个历史然后找到这个double的provider然后把它启动一下
[10:03] 那我们来看一下他有没有启动有没有问题啊等待他的一个执行因为我们需要把其他跑起来他才能够跑起来那么我们等待一下他的一个执行那么我们把这个啊还有一个是ADAD也需要把AD也跑起来OK那么我们稍微等一下刚刚呢我们在启动的时候呢报错了原因是我的这个
[10:28] 就是我们之前那个服务地址已经发生变化但是现在呢我这个配置文件都没有去调整我需要去调一下192.168.1.7然后呢下面的其实也都一样啊那么我们把它都来改一下吧这个是我们看一下这个是redis然后呢把它呢也改一下然后呢我们把它呢也改一下这个redis有三个节点然后呢这个是mongodb的这个节点
[10:57] 下面这个elag search是ok的没有问题好那么这个是rowkeeper的一个这样的一个节点也没有问题好那么下面我们就去重新启动一下走这个是double的一个provider那么我们这个ad里面它稍等一下那么可能我们刚改的是在这个里面那么在我们这个resource下面还没改我们需要去进入这个resource下面我们去找到这个配置我们也需要去调一下把它
[11:26] 这个mycircle去改一下然后还有就是我们的这个double的这个配置好这两个改完改完之后我们就进入我们的adad下面也需要去调一下ad Service那么我们来找一下是在这个下面的src下面去resource下面去把和刚才是一样的把它调一下然后把这个也改一下
[11:53] 好那么这样的话呢就可以保证这两个服务呢可以正常启动了那么再来启动一下走把它启动一下那把AD呢也启动一下那我们等待它的一个执行好那么接下来我们来看一下啊那么我们已经把前面两个服务呢就跑起来了接下来我们把这个APS server把它跑起来来看一下会怎么样那么它是否能够正常去启动呢我们来看一下那么等待它的一个执行那么我们稍微等一下
[12:19] OK那么现在呢我们这个跑起来了但是呢会发现启动会报一个错啊这个错其实就需要跟大家去说一下他报的错呢是来看一下那是这样的一个意思他就说这个我们这个不可用啊就是可用的这个有三个啊那么就是当我们看到有这样的一个这个这个错误的时候啊他是什么意思啊这个呢其实就是我们在讲义中的所看到这样的一个错误就是
[12:46] 原因是什么根本的原因是这个neti发生了一个冲突因为我们在项目中其实我们去整合了redisredis它本身也用到了这个neti然后呢在eluxus中呢也引入了这个neti会导致neti的一个冲突啊那么我们要解决的就是我们需要在启动内里面加这样的一个配置那么就可以去做一个解决了那我们来尝试的去测试一下啊那么在我们这个启动内中那么去加这样的一个参数
[13:14] 那么就运行的一个参数啊那我们再次做一个启动等待看他的一个这个结果好那么现在呢我们看到这个服务呢他就已经啊跑起来了那么下面呢我们来测试一下啊那么怎么测呢我们就去这个位置吧那我们就直接去访问或者说我们使用Postman吧去做一个测试啊那么地址呢就是http冒号双斜杠然后呢127.0.a就是这个地址啊然后我们去搜索走
[13:42] 那么点击这个圣的发送轴那么就可以看到我们的一个返回的一个数据了比如说我们查询的关键字是上海那么它的一个总页数呢是有两页啊这样的一个数据那么比如说我们查询关键字是地铁然后呢看它会返回多少条数据呢总页数呢有42页那么也420条对吧然后大概420条吧然后呢因为我们每页是10条嘛然后呢比如说我们搜索一个搜索一个什么呢叫新村
[14:09] 有些这个小区叫新村什么什么新村可以看到是不是有什么中原新村有很多OK好那么这个我们是不是可以看到数据是不是就已经返回了那就说明那就说明我们的这个刚刚写逻辑是OK的当然我们还缺少一个配置对吧配置等于二轴可以查询到这个关键字是新村的第二页的这个数据好那么可以还可以继续去查一下第三轴是不是可以看到这个叫科院新村新的这个数据
[14:39] 总共有7亿好那么到这里我们是不是就发现我们刚刚的问题是不是也就解决了并且我们其实也就实现了对外是不是开放的这个接口去做一个查询就可以了大家如果说你要查询
[14:52] 比如说查询100页我们是不是也会有这样的逻辑的处理因为我们刚刚去在代码中做了一些判断对我们代码做了一些保护好那么现在我们这个接口就开发完成了对吧那么下面其实我们就可以去整合我们的前端是不是去做开发了OK好那么关于这个接口的开发我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个基于 Spring Boot、Dubbo、Elasticsearch 和 Redis 的房屋租赁管理 API 服务的开发与调试过程，包括配置、代码编写和接口测试。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构和 Maven 依赖，重点是 Dubbo、GraphQL、Spring Boot Data Redis、Redis Client、Commons IO 等依赖。
画面2：展示 application.properties 配置文件，包含服务名、Zookeeper 地址、Redis、MongoDB 和 Elasticsearch 的集群配置。
画面3：展示 Elasticsearch 的 Kibana 界面，显示 house 索引下的文档数据。
画面4：在 IntelliJ IDEA 中，创建 SearchController 类。
画面5：展示 SearchController.java 代码，包含 @CrossOrigin 注解、@Autowired 注解、@GetMapping 注解和分页逻辑。
画面6：展示 SearchService.java 代码，包含 @Service 注解和空的 search 方法。
画面7：展示 SearchService.java 代码，正在编写使用 ElasticsearchTemplate 的 NativeSearchQueryBuilder 构建查询并分页的逻辑。
画面8：展示 SearchController.java 代码，再次显示分页逻辑。
画面9：展示 application.properties 配置文件，包含服务名、端口、Zookeeper 地址、Redis 配置等。
画面10：展示 application.properties 配置文件，包含 Redis、MongoDB 和 Elasticsearch 的配置。
画面11：展示 DubboApiApplication.java 启动日志。
画面12：展示 DubboApiApplication.java 启动日志，设置系统属性并启动 Spring Boot。
画面13：展示 Postman 中对房屋搜索接口的测试，返回 JSON 数据。
画面14：展示 PDF 文档，内容为“3、整合前端开发”，并显示 JSON 数据结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependency>
    <groupId>cn.itcast.haoke.manage</groupId>
    <artifactId>itcast-haoke-manage-dubbo-server-ad-interface</artifactId>
    <version>1.0.0-SNAPSHOT</version>
</dependency>

<dependency>
    <groupId>com.GraphQL-java</groupId>
    <artifactId>GraphQL-java</artifactId>
    <version>11.0.0</version>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>

<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>2.3.0</version>
</dependency>

<dependency>
    <groupId>commons-io</groupId>
    <artifactId>commons-io</artifactId>
    <version>2.4</version>
</dependency>
```

画面2：
```properties
application.name = dubbo-consumer-haoke-manage
try.client = zkclient
try.address = ZooKeeper://172.16.55.185:2181
s.jedis.pool.max-wait = 5000
s.jedis.pool.maxIdle = 100
s.jedis.pool.minIdle = 10
s.timeout = 10
s.cluster.nodes = 172.16.55.185:6379,172.16.55.185:6380,172.16.55.185:6381,172.16.55.185:6382
s.cluster.max-redirects=5

.mongodb.uri-mongodb://172.16.55.185:27017/testdb

.Elasticsearch.cluster-name=es-itcast-cluster
.Elasticsearch.clusterNodes=192.168.1.7:9300,192.168.1.7:9301,192.168.1.7:9302
```

画面3：无代码或配置，为 Elasticsearch Kibana 界面。

画面4：无代码或配置，为创建类的弹窗。

画面5：
```java
@CrossOrigin
@Autowired
private SearchService searchService;

@GetMapping
public SearchResult search(@RequestParam("keyword") String keyword,
                           @RequestParam(value = "page", defaultValue = "1") Integer page) {
    if (page > 100) { //防止爬虫抓取过多的数据
        page = 1;
    }
    return this.searchService.search(keyword, page);
}
```

画面6：
```java
@Service
public class SearchService {

    @Autowired
    private ElasticsearchTemplate elasticsearchTemplate;

    public static final Integer ROWS = 10;

    public SearchResult search(String keyword, Integer page) {
    }
}
```

画面7：
```java
public SearchResult search(String keyword, Integer page) {
    PageRequest pageRequest = PageRequest.of(page - 1, ROWS);
    SearchQuery searchQuery = new NativeSearchQueryBuilder()
            .withQuery(QueryBuilders.matchQuery("title", keyword).operator(Operator.AND)) // match查询
            .withPageable(pageRequest)
            .withHighlightFields(new HighlightBuilder.Field(name: "title"))
            .build();

    AggregatedPage<HouseData> housePage = this.elasticsearchTemplate
            .search(searchQuery, HouseData.class);
    return new SearchResult(housePage.getTotalPages(), housePage.get());
}
```

画面8：与画面5内容相同。

画面9：
```properties
application.name = itcast-haoke-manage-api-server
port = 18080
version = 1.0.0-SNAPSHOT

application.name = dubbo-consumer-haoke-manage
try.client = zkclient
try.address = ZooKeeper://172.16.55.185:2181
s.jedis.pool.max-wait = 5000
```

画面10：
```properties
# redis集群配置
spring.redis.jedis.pool.max-wait = 5000
spring.redis.jedis.pool.maxIdle = 100
spring.redis.jedis.pool.minIdle = 10
spring.redis.timeout = 10
spring.redis.cluster.nodes = 192.168.1.7:6379,192.168.1.7:6380,192.168.1.7:6381,192.168.1.7:6382
spring.redis.cluster.max-redirects=5

spring.data.mongodb.uri-mongodb://192.168.1.7:27017/testdb

spring.data.Elasticsearch.cluster-name=es-itcast-cluster
spring.data.Elasticsearch.clusterNodes=192.168.1.7:9300,192.168.1.7:9301,192.168.1.7:9302
```

画面11：
```java
package cn.itcast.haoke.dubbo.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DubboApiApplication {
    public static void main(String[] args) {
        SpringApplication.run(DubboApiApplication.class, args);
    }
}
```

画面12：
```java
package cn.itcast.haoke.dubbo.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DubboApiApplication {
    public static void main(String[] args) {
        System.setProperty("es.set.netty.runtime.available.processors", "false");
        SpringApplication.run(DubboApiApplication.class, args);
    }
}
```

画面13：无代码或配置，为 Postman 测试结果。

画面14：无代码或配置，为 PDF 文档内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：PDF 文档标题为“3、整合前端开发”，内容包含 JSON 数据结构示例。

5) 不要评价画面美观，不要输出与课程无关的内容。

