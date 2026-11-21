# 14-HATEOAS介绍-HATEOAS订单服务工程搭建 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来咱们呢继续去实现了

那种OS对应的服务

我们之前呢实现了股票服务

对不对

接下来呢我们就来实现了订单服务

在实现订单服务之前呢

我们回顾一下股票服务这一块的

实现他所需要注意的一些地方

这里呢我们要注意加上

Anti-Scan以及呢EnableJPA

RebossedTools的注解

这个呢要指定路径

否则的话呢它是不生效的

就在那个Startup启动内容当中

这一块呢必须要去指定

不然的话呢启动的时候它扫不了

扫描不到JPA相关的数据层实现

就会呢出现对应的错误

那我们还需要注意的地方呢就是

我们要在JPA上面加上一个注解

这个注解的话呢就是HitOS

所提供的Rest接口

如果说我们不加这个注解的话呢

那我们之前的传统写法

还要再写一个Service层

然后再写一个Control层

再做对应的实现对不对

就会比较麻烦

那么我们可以看到呢HitOS

直接通过这个注解呢

它就可以甚至什么

可以供外部

访问的接口

通过这个路径呢

它就能够呢直接去查询

我们的对应接口数据

比如说我根据股票名称

去查询了股票信息

对不对

好

这个呢就是之前呢

股票服务实现了

所需要注意的关键地方

那接下来呢

我们就来创建

对应的订单服务

我们在这里创建一个新的模块

点击Next

然后呢给模块一个名称

叫HitOS-Ord

点击Next

Dream呢它是放在Demo这个层级下面

点击Finish

好

接着的话呢

帮我们创建了订单服务工程

导入生销

那我们呢要创建对应的包结构

New Package

然后呢

Com.ID Cust

HitOS.Zim.Ord

这个呢是整体的包结构

我们在下面的话呢

要创建对应的纸包

好

Open in terminal

然后呢

Make dir

第一个纸包呢是N体

放入我们的实体

第二个纸包呢是数据层接口的实验

LibreCtl

第三个纸包呢就是SATA启动内的放置

好

接着的话呢

我们刷新一下

可以看到三个包已经创建完成

那么同样的话呢

我们先创建它的BaseN体

对不对

BaseN体这边的话呢

可以直接扣取过来

好

然后呢

我们还创建什么

订单实体

已经呢

股票实体

股票实体呢

也可以把它扣取过来

还有什么实体呢

还有一个订单实体

我们创建一个Nu

class

然后呢是OrderN体

为什么要封装BaseN体呢

这个好处就可以显现出来

对不对

我们就不需要再去重新定义一下

什么功用的属性

ID创建时间等等

好

这样呢

计算完成之后

我们就要添加Order所需要的属性

Order这一块呢

我们给它定义一下

DirectString

是什么

用户名

然后呢

还给它一个股票名称

订单里面的话呢

要包括股票名称

对不对

然后是

加上它对应的注释

我们还要再创建呢

它的一个数量

FiredString

这个呢

就是成交数量

组成订单的关键信息

然后呢

我们还要去添加什么

它的成交价格

对吧

再加上

这个成交价格呢

我们就给它那个双进度类型就行了

Pi

Price

加上对应的注释

是成交价格

好

那接下来呢

我们还去这个实例上面呢

给它加上对应的注解

对不对

注解的话呢

第一个是

Nt

然后是Date

Long Book的插件

这个导入一下

加我X下面的包

然后是那个Table

你要映射到哪个表

这个呢

要给它一个

分配

来

Word表

然后呢

我们再给它创建那个构造方法

RX

然后呢

ORX

这样呢

实际上这块创建完成

然后呢

我们再创建什么

数据上这块呢

其实也比较简单

我们来创建一下

是一个接口

通过JPA进行实现

对不对

Word

微波C图里

G是什么

JPA接口

微波C图里

然后这个是

OrderNt

给它的一个ID类型

然后我们要提供接口

这个接口是什么

根据用户来查找所有的订单信息

OrderNt

FindByUser

这个呢

它都会给出提示啊

我们按提示就可以

敲回头就行了

Header

然后就是User

StreamUser

给它加上对应的注射

根据用户查找

获取所有订单信息

好

这样呢

我们这个接口就已经提供完成

提供完成之后呢

不要忘了加上我们的对应的Rest注解

否则的话呢

它生成的接口并不能什么

对外包入访问

给它一个访问路径

干Order就可以

好

那数据层创建完成之后呢

我们还要去创建什么

它的启动类

New

Dial Class

然后呢

启动类

Generate

叫Header

OS

Odd Application

这里面的话呢

我们同样给它一个启动入口

Screen

Application

Run

然后我们加这个Class

加入进来

传递参数

我们在这一块呢

可以做个copy

节省一些时间

这个呢是必要的一些注解

然后呢

我们还有什么

节省的这个序列化知识

对不对

然后要把这块呢

要加入进来

我们把它放在这里

在这里面不要忘记

它需要加什么

加上一个

并要纳入到什么

Supply容器当中

这个呢

是Talker当中

好像没有加上

对不对

我们也把它补充上去

就是确保这块呢

纳入Supply容器当中

然后的话呢

我们再给它呢

进相关的接口

这里呢

还有一些配置需要加上

那我们打开讲义

找到对应的那个

订单符工程的这个说明

那因为我们这才是什么ATD呢

HTTP的一个调用

所以连接词这块呢

我们也必须把它加入进去

还有LessTemplate的配置

对应呢

这个导入的类

那导入类这块我们可以看到

在这里面呢

连接词的策略

它在这里设置了它的一个调用的总数

对不对

Default的一个配置

然后呢

把这个

我们需要呢

加上它对应的依赖

Home文件当中

这个依赖的话呢

是HTTP Client的调用依赖

Defensive

Group ID呢

打字顶一下

要传输下面的

HTTP Compense

然后呢

Artifact ID是什么

HTTP Client

再给它一个版主号

Wash

然后呢

4.5.7的一个版主就可以

这个是什么组件呢

这个呢

是HTTP

就是我们所用到的HTTP连接词的组件

HTTP Client

连接的

我们再回到刚才的配置当中

这样呢

它就把我们自动导入了

对不对

在这里还有一个什么

KeepLive的策略设定

这个呢

是Less Template的一个配置

这是HTTP的一个调用

设置它的一些连接操作时间等信息

好

那我们的话呢

再增加它的一个KeepLive的策略

KeepLive策略的话

我们来看一下

在上面会有对应的一个实现

那么呢

这个实现内的加入进来

new class

然后呢

将名字合比过来

这个呢

是它具体实现

很简单的合比进来

在这里呢

就已经导入进来了

对不对

这个呢

是它的一个连接设置策略

我们来看一下

主要呢

是设置KeepLive的

是连接的一个有效存活的设置

在这里面的话呢

设置它的一些头部处理

然后呢

它的一个默认的一些超时的

实现的配定

那这里的话呢

第4s时呢

我们是设置30秒的有效连接时间

好

如果说你要更改或者调整的话呢

修改这个参数就可以了

好

这个呢是黑狗OS

最后的话呢

我们要去编写一个接口

做一个调用和验证

对不对

创建一个接口

remote

忘了

那这LibreLine怎么去测试呢

我们等服务启动完成之后呢

然后就去做一个调用测试

那么怎么知道服务启动完成之后呢

那么怎么知道服务启动完成之后呢

我们就要去实现对应的接口

implements application

忘了

去实现它的方法

忘方法

这个就是服务启动后执行

这个就是服务启动后执行

你不能说等服务还没启动完成

你就去调用

那么很多主页都没出出发

你是无法进行调用的

然后在上面呢

去增加它对应的属性

那我要进行一个远程调用

对不对

我是不要配置远程D字啊

对吧

URI

点create

这里面的话是attp

loghost

8080

只想8080端口就可以了

这个呢是URI路径地址

指定呢

票服务这口地址

然后在下面的话呢

我们还定义它什么

yes template

这个呢将它注入进来

go to wild

它是负责attp远程的调用

它是负责attp远程的调用

好

这个呢是less template的一个作用

那么的话呢

是不是还要去增加对应的

数据层接口呢

对吧

order

这个是一个c2ray

将它呢也注入进来

这个呢是什么

order的

数据层操作接口

最后的话呢

我们就可以进行一个测试和调用

那测试实现逻辑是怎样的

首先的话呢

我们要给它一个link

对吧

stops link

这个呢给它一个get link

对吧

link

root

ui

然后呢是一个

要具体的是获取什么样的数据

stops

我要获取的股票信息对不对

这个是link

将它呢加了进来

我们将link包呢

给它进来

import class

hit os

对吧

然后在这里面的话呢

还实现了get link的一个方法

为了快速实现

体现呢

节省大家的一些时间

我们在这里呢

就直接扩展过来

从这里开始

扩展过来呢

我们再做一个详细讲解

然后呢

还有它对应的方法

点的link

这里呢

就全部扩展过来

好

那扩展过来之后呢

我们再讲一下它整体的一个逻辑

这个呢

还要再加上呢

nombook的注解

那个佛街图

我们看一下

order entity

再加上一个

builder的注解

看一下

还有没有缺少什么

这些的话呢

这里还有一个报酬

对不对

我们再来看看

我们再来看看

我们再来看看

我们再来看看

我们再来看看

在这里呢

我们加入它的builder的注解

好

那还有没有其他数

这个是成交数量

成交数量的话呢

我们不应该给string

对不对

这里改成init

那整理逻辑我们看一下

首先呢

我们是查询股票信息

对不对

然后呢

就要去更新股票的价格

最后呢

我们就要重新打印

所查询的股票信息

做一个比对

这个呢

就知道有没有修改成功

然后呢

原生的调用是否OK

最后呢

我们再生成订单信息

调用了本地的order的接口

做一个存储

好

接着的话呢

我们还去实现了它的一个工程配置

工程配置这一块呢

也比较简单

我们呢

可以直接将它拷贴过来

在这里呢

放到我们的

BitcoinSource支援目的下面

端口呢

我们修改一下

改成了8082

跟之前的股票服务呢

做一个区分

然后呢

在这里我们也定义它的一个表结构

先拷贴过来

表结构呢

我们也做一个拷贴

好

这个呢

是订单表的一个创建

整个的话呢

订单服务的创建

以及它对应的部分

它的配置呢

我们就已经实现完成

那这一讲呢

我们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程是关于 Spring Boot 中 HATEOAS（Hypermedia as the Engine of Application State）框架的实战教学。讲师通过一个“股票订单”微服务的完整示例，详细讲解了如何使用 HATEOAS 来构建具有自描述能力的 RESTful API。课程内容涵盖了 HATEOAS 的核心概念、如何在 Spring Data JPA 中使用 `@RepositoryRestResource` 注解、如何定义资源对象（`Resource`）和链接对象（`Link`），以及如何通过 `RestTemplate` 进行远程调用并处理 HATEOAS 返回的超媒体数据。同时，课程也涉及了如何配置 `RestTemplate` 的超时参数和自定义的连接保持活跃策略（`RemoteConnectionKeepAliveStrategy`），以优化远程调用性能。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从截图中精确获取视频的时间戳，以下章节结构是根据画面内容和课程逻辑推断的：

*   **00:00 - 00:30**：课程开场，介绍本节将讲解 HATEOAS 的核心概念和在 Spring Boot 中的应用。
*   **00:30 - 01:00**：展示项目结构，包括 `hateoas-order` 和 `hateoas-stocks` 两个模块，并介绍 `StocksEntity` 和 `OrderEntity` 的数据模型。
*   **01:00 - 01:30**：讲解 `StockRepository` 的定义，重点是 `@RepositoryRestResource` 注解的使用，以及如何通过方法名自动映射查询。
*   **01:30 - 02:00**：演示 `OrderRepository` 的定义，继承 `JpaRepository`，并展示其方法。
*   **02:00 - 02:30**：讲解 `HateoasOrderApplication` 的主类，展示如何启动 Spring Boot 应用。
*   **02:30 - 03:00**：配置 `RestTemplate`，设置连接超时和读取超时。
*   **03:00 - 03:30**：讲解 `RemoteConnectionKeepAliveStrategy` 类，用于自定义远程连接的保持活跃策略。
*   **03:30 - 04:00**：演示 `RemoteRunner` 类，展示如何使用 `RestTemplate` 调用远程服务并处理 HATEOAS 返回的 `Resource` 和 `Link` 对象。
*   **04:00 - 04:30**：讲解 `queryStocksLink` 方法，展示如何通过 `@Autowired` 注入 `RestTemplate`，并使用 `@Param` 注解来处理 HATEOAS 返回的链接。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **大纲**：视频中显示的文档大纲包括：
    *   3.1 HATEOAS 简述
    *   3.2 HATEOAS 示例
    *   3.3 HATEOAS 常用链接类型
    *   3.4 HATEOAS CRUD 示例
    *   3.5 服务设计
    *   3.6 工程说明
    *   3.7 启动股票服务验证
    *   3.8 启动订单服务验证
    *   第3章 GRPC介绍与使用

#### 代码关键内容

*   **`StockRepository` 接口**：
    ```java
    @RepositoryRestResource(path = "/stocks")
    public interface StockRepository extends JpaRepository<StocksEntity, Long> {
        public StocksEntity findByName(@Param("name") String name);
    }
    ```
    *   **注解说明**：`@RepositoryRestResource` 用于指定资源路径，`@Param` 用于指定方法参数名。

*   **`OrderRepository` 接口**：
    ```java
    public interface OrderRepository extends JpaRepository<OrderEntity, Long> {
        // 方法定义
    }
    ```

*   **`HateoasOrderApplication` 主类**：
    ```java
    public class HateoasOrderApplication {
        public static void main(String[] args) {
            SpringApplication.run(HateoasOrderApplication.class, args);
        }
    }
    ```

*   **`RestTemplate` 配置**：
    ```java
    @Bean
    public RestTemplate restTemplate(RestTemplateBuilder builder) {
        return builder
            .setConnectTimeout(Duration.ofMillis(2000))
            .setReadTimeout(Duration.ofMillis(1800))
            .requestFactory(this::requestFactory)
            .build();
    }
    ```

*   **`RemoteConnectionKeepAliveStrategy` 类**：
    ```java
    public class RemoteConnectionKeepAliveStrategy implements org.apache.http.conn.HttpClientConnectionManager {
        private final long DEFAULT_SECONDS = 30;

        @Override
        public long getKeepAliveDuration(HttpResponse response, HttpContext context) {
            return Arrays.asList(response.getHeaders(HTTP.CONN_KEEP_ALIVE))
                .stream()
                .filter(h -> StringUtils.endsWithIgnoreCase(h.getName(), "keep-alive")
                    && StringUtils.isNumeric(h.getValue()))
                .mapToLong(h -> Long.parseLong(h.getValue()))
                .findFirst()
                .orElse(DEFAULT_SECONDS);
        }
    }
    ```

*   **`RemoteRunner` 类**：
    ```java
    @Service
    public class RemoteRunner {
        @Autowired
        private RestTemplate restTemplate;

        private Resource<StocksEntity> updateStocks(Link link) {
            StocksEntity americano = StocksEntity.builder()
                .name("中国平安")
                .price(68.9)
                .build();
            RequestEntity<StocksEntity> req = RequestEntity.put(link.getTemplate().expand())
                .body(americano);
            ResponseEntity<Resource<StocksEntity>> resp = restTemplate.exchange(req, new ParameterizedTypeReference<Resource<StocksEntity>>() {});
            log.info("add Stocks -> {}", resp);
            return resp.getBody();
        }

        private void queryStocksLink(StocksLink stocksLink) {
            ResponseEntity<PagedResources<Resource<StocksEntity>>> stocksResp = restTemplate.exchange(
                uri, HttpMethod.GET, requestEntity, new ParameterizedTypeReference<PagedResources<Resource<StocksEntity>>>() {});
            log.info("查询到的 stocks.link: {}", stocksResp.getBody().getContent());
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示** (截图 2, 3, 4, 5)
    *   讲师在 IntelliJ IDEA 中展示了 `hateoas-order` 和 `hateoas-stocks` 两个模块的项目结构。
    *   重点展示了 `entity` 包下的 `OrderEntity` 和 `StocksEntity` 类，以及 `repository` 包下的 `OrderRepository` 和 `StockRepository` 接口。
    *   通过鼠标悬停和滚动，展示了类的成员变量和继承关系。

*   **场景二：`StockRepository` 定义演示** (截图 1, 6)
    *   讲师在 Typora 文档中展示了 `StockRepository` 接口的代码。
    *   重点讲解了 `@RepositoryRestResource` 注解的作用，以及 `findByName` 方法如何通过方法名自动映射查询。
    *   强调了 `@Param` 注解用于指定方法参数名。

*   **场景三：`RestTemplate` 配置演示** (截图 6, 7)
    *   讲师在代码中展示了如何通过 `RestTemplateBuilder` 配置 `RestTemplate`。
    *   重点讲解了 `setConnectTimeout` 和 `setReadTimeout` 方法，用于设置连接和读取超时时间。
    *   展示了 `requestFactory` 方法的实现。

*   **场景四：`RemoteConnectionKeepAliveStrategy` 实现演示** (截图 8)
    *   讲师展示了 `RemoteConnectionKeepAliveStrategy` 类的实现。
    *   重点讲解了 `getKeepAliveDuration` 方法，用于根据 HTTP 响应头中的 `Connection` 字段来设置连接保持活跃的时间。
    *   展示了 `Stream` 的 `filter` 和 `mapToLong` 方法的使用。

*   **场景五：`RemoteRunner` 类演示** (截图 9, 10, 11)
    *   讲师展示了 `RemoteRunner` 类，用于演示如何使用 `RestTemplate` 进行远程调用。
    *   在 `updateStocks` 方法中，演示了如何创建 `StocksEntity` 对象，使用 `RequestEntity` 发送 PUT 请求，并处理 `ResponseEntity` 返回的 `Resource<StocksEntity>`。
    *   在 `queryStocksLink` 方法中，演示了如何发送 GET 请求，并处理返回的 `PagedResources<Resource<StocksEntity>>`。
    *   通过日志输出，展示了调用结果。

---

以上是根据您提供的视频画面截图，对这段技术课程进行
