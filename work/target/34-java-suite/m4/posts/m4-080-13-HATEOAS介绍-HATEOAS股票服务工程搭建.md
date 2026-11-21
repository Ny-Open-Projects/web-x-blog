---
title: "HATEOAS 双服务工程落地验证与 gRPC 精讲：股票/订单服务搭建、线程模型、gRPC vs Rest 性能对比"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 智牛股]
tags: [Java, 项目实战, gRPC]
---

# HATEOAS 双服务工程落地验证与 gRPC 精讲：股票/订单服务搭建、线程模型、gRPC vs Rest 性能对比

智牛股第三章"技术基础二"的下半单元做两件事。前半段把上一篇的 HATEOAS 设计落成两个真实工程：股票服务（8080）与订单服务（8082），从实体、数据层、启动类一路写到启动验证，把四步调用流程完整跑通；后半段切入 gRPC，讲清它是什么、性能为什么好、线程模型如何演进、客户端调用分几步，最后用实测数据把" gRPC 比 REST 快多少"的预期校准到位。

## 先给结论

- 股票服务的数据层只要继承 JpaRepository 并加上 `@RepositoryRestResource(path = "/stocks")`，Spring Data REST 就会自动生成整套 CRUD 与分页接口——Service 层、Controller 层都不用写，没实现的分页查询和修改能力也会自动提供。
- 启动类上的 @ComponentScan、@EntityScan、@EnableJpaRepositories 必须指定 basePackages，否则扫不到 JPA 数据层实现直接报错；实体侧用 @MappedSuperclass 的 BaseEntity 收拢 id、createTime、updateTime 公共属性。
- 订单服务用 RestTemplate 按 HATEOAS 链接驱动的方式调用股票服务：先 getLink 拿到 stocks 链接，再按链接查询、PUT 更新价格、复查比对，最后生成订单。调用逻辑放在实现 ApplicationRunner 的 RemoteRunner 里，类上必须有 @Component 纳入容器管理，否则服务启动后不会自动触发——课程里实际踩过的坑。
- gRPC 是 Google 开源的高性能通用 RPC 框架，性能优势由三件事撑起：Proto Buffer 二进制序列化（对比 JSON/XML 有数倍提升）、HTTP/2 头部压缩与连接复用、底层 Netty NIO；天然跨语言，支持负载均衡、调用跟踪、健康检查与安全认证。
- gRPC 线程模型遵循 Netty 的线程分工原则：协议层消息接收与编解码交给 Netty 的 IO 线程（NioEventLoop），应用层逻辑交给应用线程，两层分离互不阻塞；Reactor 模式在大数据量场景下响应效率更高，请求量只有几十上百时体现不出优势。
- 性能对比要校准预期：小数据量下 gRPC 与 REST 差别不明显，大数据量、高并发下差距才拉开。课程实测口径是性能提升约 32%、CPU/内存等资源占用降低约 30%、综合吞吐提升约 20%——不是数倍数十倍的魔法。

## 股票服务：实体、数据层与自动暴露的接口

### 实体与数据层

hateoas-demo 父工程下新建 hateoas-stocks 模块，包结构里划出 entity、repository、startup 三个子包。先写实体父类 BaseEntity，收拢所有实体公用的属性：

```java
@Data
@MappedSuperclass
public class BaseEntity implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "create_time", updatable = false)
    @CreationTimestamp
    private Date createTime;

    @Column(name = "update_time")
    @UpdateTimestamp
    private Date updateTime;
}
```

三个细节：实现 Serializable 序列化接口；创建时间设 updatable = false，数据创建之后不允许再调整；@CreationTimestamp 与 @UpdateTimestamp 让 Hibernate 自动维护两个时间戳，@MappedSuperclass 声明它是父类、不单独映射表。

股票实体继承它，只关心业务字段：

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "t_stocks")
public class StocksEntity extends BaseEntity {
    private String name;   // 股票名称
    private Double price;  // 股票价格
}
```

name 与 price 不加 @Column，按默认方式进行映射匹配。数据层接口是 HATEOAS 能力的来源：

```java
@RepositoryRestResource(path = "/stocks")
public interface StocksRepository extends JpaRepository<StocksEntity, Long> {
    // 根据股票名称查询股票信息
    StocksEntity findByName(@Param("name") String name);
}
```

按 JPA 的方法命名规则写 findByName 即可，不用写实现类；关键在 @RepositoryRestResource 这个 HATEOAS 提供的注解——不加它，就得自己再写 Service 层和 Controller 层才能对外提供服务；加上它，Spring Data REST 直接把数据层接口暴露成可访问的 REST 资源。再补一个按名称集合查询、按 ID 排序的 findByNameInOrderById，供后面验证用。

### 启动类与配置

启动类除了 @SpringBootApplication，三个扫描注解都要指定 basePackages：

```java
@SpringBootApplication
@ComponentScan(basePackages = {"com.idcast"})
@EntityScan(basePackages = {"com.idcast"})
@EnableJpaRepositories(basePackages = {"com.idcast"})
public class HateoasStocksApplication {
    public static void main(String[] args) {
        SpringApplication.run(HateoasStocksApplication.class, args);
    }
}
```

不指定路径就扫描不到 JPA 相关的数据层实现，启动时会出错。容器里还要注册两个 Bean：Hibernate5Module 处理 JPA 实体相关的序列化，Jackson2ObjectMapperBuilder 定制 JSON 封装——HATEOAS 的传输载体是 JSON 数据。application.properties 里 server.port=8080；spring.jpa.hibernate.ddl-auto 设为 none，不要求每次启动都更新表结构；show-sql 与 format_sql 打开，打印格式化的 SQL 便于跟踪测试。

表结构与初始数据放在 schema.sql：

```sql
drop table t_stocks if exists;
create table t_stocks (
    id bigint auto_increment,
    name varchar(64),
    price double,
    create_time timestamp,
    update_time timestamp,
    primary key (id)
);
insert into t_stocks(name, price, create_time, update_time)
values ('中国平安', 86.6, now(), now());
insert into t_stocks(name, price, create_time, update_time)
values ('工商银行', 6.6, now(), now());
insert into t_stocks(name, price, create_time, update_time)
values ('招商银行', 26.6, now(), now());
```

### 启动验证

启动后浏览器直接访问 `http://127.0.0.1:8080/`，返回的就是 _links 资源信息。访问 /stocks：_embedded 里能看到三条初始股票数据，下面还带分页链接 `http://127.0.0.1:8080/stocks{?page,size,sort}`、profile 与 search——代码里没有写过任何分页查询或修改接口，CRUD 全部自动提供，这是 Spring Data REST 替实体做的事。

/stocks/search 会把自定义实现的查询方法全部呈现出来，不用查 API 文档就能直接访问。实测 findByName 传 name=工商银行，返回工商银行这条数据；换成 name=中国平安同样命中。findByNameInOrderById 传 list 参数，多个值用逗号分割，比如 list=中国平安,工商银行，返回符合条件的中国平安与工商银行两条数据。

## 订单服务：RestTemplate 链接调用与四步验证

### 工程与调用方配置

hateoas-order 模块同样拆 entity、repository、startup 三包。BaseEntity 与 StocksEntity 直接从股票服务拷贝过来——订单服务要解析股票响应，BaseEntity 收拢公共属性的好处在这里显现，id、创建时间都不用重复定义。订单实体只多四个业务字段：

```java
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "t_order")
public class OrderEntity extends BaseEntity {
    private String user;      // 用户名
    private String stockName; // 股票名称
    private Integer volume;   // 成交数量
    private Double price;     // 成交价格
}
```

成交数量不能用 String，要用 Integer。数据层 OrderRepository 继承 JpaRepository<OrderEntity, Long>，提供 findByUser（根据用户查找所有订单信息），同样加 @RepositoryRestResource(path = "/order")。订单服务端口改为 8082，与股票服务区分。

订单服务要主动发起 HTTP 调用，pom 里补上 org.apache.httpcomponents:httpclient:4.5.7 连接组件；RestTemplate 用 RestTemplateBuilder 配置连接与读取超时，并挂上自定义的 KeepAlive 策略类 RemoteConnectionKeepAliveStrategy——从响应头解析 keep-alive 信息，默认设置 30 秒的有效连接时间，需要调整改参数即可。

### RemoteRunner：四步流程落地

调用逻辑放在实现 ApplicationRunner 的 RemoteRunner 里，服务启动完成后自动触发执行。ROOT_URI 指向股票服务 `http://localhost:8080`，注入 RestTemplate（负责 HTTP 远程调用）与 OrderRepository（负责订单落库）：

```java
@Component
@Slf4j
public class RemoteRunner implements ApplicationRunner {
    // 指定股票服务接口地址
    private static final URI ROOT_URI = URI.create("http://localhost:8080");

    @Autowired
    private RestTemplate restTemplate;
    @Autowired
    private OrderRepository orderRepository;

    @Override
    public void run(ApplicationArguments args) {
        // 从 _links 中取出 stocks 资源链接
        Link stocksLink = getLink(ROOT_URI, "stocksEntities");
        // Step1 查询股票信息并打印
        queryStocks(stocksLink);
        // Step2 通过 HTTP PUT 更新股票价格（中国平安改为 68.9）
        // Step3 重新查询股票信息，打印名称与价格，与 Step1 比对
        // Step4 调用自身接口生成订单信息
        OrderEntity order = OrderEntity.builder()
                .user("mirson").stockName("建设银行")
                .volume(1000).price(99.9)
                .build();
        orderRepository.save(order);
    }
}
```

客户端解析响应用的是 HATEOAS 的 Link、Resource、PagedResources 这组类型，配合 ParameterizedTypeReference 声明泛型；PUT 更新通过 RequestEntity.put(link.getTemplate().expand()) 展开模板链接后提交新的 StocksEntity。整条链路没有任何硬编码的 URL，全靠响应里的 _links 驱动。

验证时先踩了一个坑：RemoteRunner 实现了 ApplicationRunner，启动后控制台却没有预期日志——实现接口不等于自动执行，类上漏了 @Component、没纳入 Spring 容器管理，Spring 就不会触发调用。补上注解重启，日志依次输出：远程调用查出三只股票及价格 → PUT 修改中国平安（按唯一 ID 定位），价格改为 68.9，其余数据不变 → 生成订单数据。

### 验证结果

访问 8082 的 order 服务，_embedded.orderEntities 里出现一条订单：user 为 mirson、stockName 为建设银行、volume 1000、price 99.9，与代码构建参数一致，四步流程闭环。再用 Postman 模拟一遍增删改查——这些都由 Spring Data REST 完成了封装，整个服务没有 Controller 层。

这正是 REST 设计风格与传统写法的分野：它没有"接口"的概念，一切以资源为对象，增删改查靠 HTTP method 的不同动作类型来区分。从 Spring MVC + Boot 的写法切过来，要先扭转思路，所有修改都以目标资源为出发点。

## gRPC：特性、线程模型与客户端调用流程

### gRPC 是什么，为什么快

gRPC 是 Google 开源的高性能通用 RPC 框架。RPC（Remote Procedure Call）即远程服务调用：客户端和服务端约定好接口，双方按约定通信，做过 Dubbo 这类 RPC 框架的话对这个模型不陌生。官方架构图里，C++ 的 gRPC Server 居中，Ruby、Android-Java 等客户端通过 gRPC Stub 发起 Proto Request、接收 Proto Response——跨语言是它的天然属性，适合构建分布式微服务应用。数据载体统一是 Proto Buffer（PB），后台应用、前端 JS 都支持调用。

性能优势来自三件事：

| 手段 | 作用 |
| :--- | :--- |
| Proto Buffer 序列化 | 二进制序列化，对比 JSON 与 XML 有数倍提升；JSON 的序列化/反序列化效率差很多 |
| HTTP/2 协议 | 头部信息压缩，连接复用，减少 TCP 连接次数，比传统基于 HTTP 的 RestTemplate、Feign 这类调用方式更优 |
| Netty 底层 | 优秀的 NIO 处理框架，通讯性能进一步提升 |

工程能力上，gRPC 支持多语言多客户端（C++、Go、Ruby 等主流语言，符合接口规范即可互调），面向大数据高并发场景支持负载均衡、调用跟踪、健康检查、安全认证，扩展性强；节点出现瓶颈就扩充节点，靠负载均衡把整体吞吐能力继续抬上去。

### 线程模型：从 BIO 到 Reactor

gRPC 的线程模型遵循 Netty 的线程分工原则：协议层消息的接收和编解码由 Netty 的 IO 线程（NioEventLoop）负责，应用层处理由应用线程负责，防止应用逻辑耗时阻塞 Netty 的 IO 线程——IO 与应用两部分线程分离设计。理解这套设计要看三种模型的演进：

| 模型 | 处理方式 | 问题 |
| :--- | :--- | :--- |
| 基础模型 | Acceptor 接收请求后分发给新线程，来多少请求创建多少线程（非线程池） | 请求一多线程失控 |
| BIO（线程池模式） | Acceptor 把任务放进线程池执行 | 应用处理仍是同步阻塞，阻塞时间取决于对方 IO 处理速度与网络 IO 传输速度；终端带宽参差不齐（1M、100K、10K 各有不同），数据即使很快处理完，也会被 IO 瓶颈拖出明显延迟 |
| NIO（Reactor 模式） | Reactor 线程统一接收所有客户端请求，Dispatcher 把读写事件分发给多个 Handler（分别处理 read、encode、write、decode 等事件），处理结果直接回给 Reactor | 业务应用处理不再产生阻塞，响应效率更高 |

Reactor 模式的优势是针对大数据量场景的——请求只有十个上百个时体现不出来，这一点要了解清楚。

### 客户端调用的六个步骤

客户端调用链路上有五个模块：ClientCalls → LoadBalance → Netty Transport Base HTTP/2 → Protobuf 序列化 → Network。拆成六步：

1. 客户端 Stub 发起 RPC 远程调用；
2. LoadBalance 按负载均衡策略选择一个服务端实例，角色类似 Nginx，默认策略轮询选择，多个服务节点都可以提供出来；
3. 客户端与服务端之间没有可用连接时，创建 Netty 的 transport 与 handler，建立一个新的 HTTP/2 连接；
4. 请求使用 Proto Buffer 序列化，基于 HTTP/2 Stream 流式方式将数据发送给 gRPC 服务端，进行网络读写；
5. 服务端收到请求后使用 PB 做反序列化操作，处理业务逻辑；
6. 回调 GrpcFuture 的 setResponse 方法，唤醒调用方被阻塞的线程，将响应传递给调用方。

前五步是请求出去的路径，第六步是响应回来的路径，异步 Future 机制让调用线程不必死等网络 IO。

## gRPC vs REST：把性能预期校准到实测

"性能优异"不能停留在口号，课程给了一组跨平台测试：Windows 与 Linux 两个平台、100 与 200 两档请求量，对比同一批方法的执行耗时（ms），方法覆盖 GrpcGetSmallPayloadAsync、RestGetSmallPayloadAsync、GrpcPostLargePayloadAsync、GrpcGetLargePayloadAsListAsync、RestGetLargePayloadAsync、GrpcStreamLargePayloadAsync、RestPostLargePayloadAsync。两个平台表现略有差异但不大，读数分三个层次：

- 传输数据量小（Small Payload）时，gRPC 与 REST 看不出明显差别；
- 数据量大、高并发的场景下差距拉开，REST 的耗时远大于 gRPC，但提升幅度并没有达到数倍数十倍的程度；
- 参考开源的 Go 基准测试（gRPC+ProtoBuf 对比 REST 的 Http+Json），两者几乎打平：BenchmarkGRPCProtobuf-8 为 117649 ns/op、7686 B/op、154 allocs/op，BenchmarkHTTPJSON-8 为 105837 ns/op、8932 B/op、116 allocs/op——纯序列化层面 HTTP+JSON 甚至略快、内存分配次数更少。CPU 使用率用 go test -bench=... -cpuprofile=xxx.cpu 生成剖析文件对比，项目源码开源，Go 项目跑起来也简单，可以自己复测。

课程结合项目实测给出的综合口径是：gRPC 通讯方案相比 REST 性能提升约 32%；CPU、内存等系统硬件资源占用降低约 30%。资源开销降下来，同样的机器就能跑更多线程，整体吞吐量实际提升约 20%。

落到场景上：gRPC 既节省系统资源，又有相对明显的性能提升，适合大数据量、高并发的服务间调用；小负载场景下不必为了几十个百分点的差距做迁移。性能到底能提升多少，必须结合具体实际情况评估，不能盲目拍一个数字。

## 小结

这个单元把 HATEOAS 从概念推到了可运行的服务。股票服务证明 @RepositoryRestResource 加 JpaRepository 就能自动暴露全套 CRUD 与分页，search 会自动收录自定义查询，验证只需浏览器按链接访问；订单服务证明客户端可以完全按 _links 里的链接驱动调用，四步流程（查询、PUT 更新、复查比对、生成订单）跑通后，8082 上能看到与代码参数一致的订单数据。两个服务都没有 Controller 层——以资源为对象、用 HTTP 动作区分增删改查，是 REST 与传统 MVC 写法的本质区别，写 HATEOAS 服务前要先扭转这个思路。gRPC 部分记三层：特性（PB 序列化、HTTP/2、Netty），线程模型（IO 线程与应用线程分离，Reactor 模式服务大数据量场景），客户端六步调用（Stub 发起 → 负载均衡 → HTTP/2 连接 → PB 序列化 → 反序列化 → GrpcFuture 唤醒）。性能上小负载打平、大负载拉开，实测口径约性能 +32%、资源 -30%、吞吐 +20%，具体收益要结合场景评估。gRPC 的服务设计、Proto 生成与工程集成，在后续章节展开。
