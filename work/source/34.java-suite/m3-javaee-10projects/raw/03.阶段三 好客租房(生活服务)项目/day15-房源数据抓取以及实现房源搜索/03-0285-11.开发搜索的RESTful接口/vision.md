# 画面线理解：11.开发搜索的RESTful接口

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\11.开发搜索的RESTful接口【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:27, 01:25, 02:33, 03:21, 05:42, 07:07, 08:52, 09:31, 10:28, 11:22, 12:08, 13:20, 14:15, 14:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:07:07

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
    <groupId>com.graphql-java</groupId>
    <artifactId>graphql-java</artifactId>
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
try.address = zookeeper://172.16.55.185:2181
s.jedis.pool.max-wait = 5000
s.jedis.pool.maxIdle = 100
s.jedis.pool.minIdle = 10
s.timeout = 10
s.cluster.nodes = 172.16.55.185:6379,172.16.55.185:6380,172.16.55.185:6381,172.16.55.185:6382
s.cluster.max-redirects=5

.mongodb.uri-mongodb://172.16.55.185:27017/testdb

.elasticsearch.cluster-name=es-itcast-cluster
.elasticsearch.clusterNodes=192.168.1.7:9300,192.168.1.7:9301,192.168.1.7:9302
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
try.address = zookeeper://172.16.55.185:2181
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

spring.data.elasticsearch.cluster-name=es-itcast-cluster
spring.data.elasticsearch.clusterNodes=192.168.1.7:9300,192.168.1.7:9301,192.168.1.7:9302
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
