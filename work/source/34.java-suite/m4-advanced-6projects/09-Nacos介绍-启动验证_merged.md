# 09-Nacos介绍-启动验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对Nacos做个启动和验证

首先咱们要确保Nacos已经安装

并且启动好

那么这个是Nacos的下载地址

已经提供出来

我们可以打开它的官方下载地址

在下面的话有很多的一些版本

目前的话已经是到1.2.1的一个版本

也算是更新的话比较快

之前的话在讲义编写的过程当中

版本还是0.8 0.9的一个版本

那么我们在测试过程当中

做了一个改进

采用了1.0.1的一个版本

因为之前的一些版本

会存在一些稳定性

兼容性的方面的一些问题

好那么在这里

就建议大家采用1.0.1的一个版本进行安装

那么的话下载完成之后

打开Nacos的安装目录

里面我们可以不用做任何的修改

那么如果是你想免密码登录

之前在第一天的课程当中

给大家做了一个具体讲解

这里就不做赘述

那修改了它的配置文件

实现免密码登录之后

我们就可以启动Nacos服务

那么怎么启动呢

通过Starlab CMD做一个启动

在这里要观测它的一个启动日志

因为如果说你这个服务运行时间比较长

然后在这里面的话

存入了很多的服务注册信息

或者配置信息的话

它可能会出现一些假死的情况

也可能就是说启动在这里

它就不再运行

所以最终我们要看

它在这里能否出现这个提示

如果是出现这个提示

说明它是启动成功的

那么Nacos服务启动完成之后

我们可以去访问一下

127.0.0.1

然后在这里是8848的专口

因为我们这边已经实现了免密码的配置

这个是Nacos的配置管理列表

接下来我们就会在上面去修改它对应的一个配置

怎么去实现它的配置管理

我们在这里首先新增点击加号

注意是在配置列表

然后点击一个加号

点击加号之后

这里会出现一个Data ID

还有Group

在我们之前讲Nacos的原理的时候

讲了三个维度

一个是Namespace

Namespace是什么意思

就在这里面的一个D

这里它有很多的命运空间

我们可以看到

默认的话是Public

它是一个保留的空间

如果说我们会有多个空间

那么建议大家可以根据不同的环境

创建不同的命运空间

记录命运空间之后

我们可以给它创建具体的配置文件

那么创建配置文件会有一个Group

这个Group的话

如果说我们的业务节点特别多

那么可以把相同业务性质的服务归为一个主编

比如说交易服

然后用户服等等

那么我们就来实现了它的一个配置

大家还记不记得

在我们的工程室配置文件之后

我们在这个配置中

我们指向一个Data ID

这个Data ID的话是一个Nexus Configure Demo

一个完整的文件名称

那么我们将它直接引入进来

Group在这里不需要做任何调整

然后这个配置内容

我们需要编写一个配置项

这个配置项要根据我们Demo里面的所定义的属性来命名

我们是定义了一个Stock Name

对不对

好

那么我们给它的名称呢

就是Stock Name

注意我们是Properties作为后缀

那么在这里也改成Properties

这个名称的话

我们就随便给它一个股票名称

比如说叫工商银行

然后呢

然后我们再点击发布

点击确定

好

这样就发布完成

我们再点击配置列表

这个时候是不是可以看到

多出来一个Data ID的配置项

这个就是我们刚才所配置的

那Cross的Configure Demo

我们就可以了启动

来做一个验证

好

那我们找它的启动内

Narcos Configure Demo

启动内的话呢

我们还没有实现它的启动路口

我们增加一下

PSVM

然后呢

Split Application

点乱

Narcos Configure Demo Application

Cross

然后将这张参数也传递进来

接着的话呢

我们就来启动做个验证

那Narcos服务呢

是已经启动成功

我们就来启动

我们的Configure配置应用服务

配置的时候呢

我们会去做一个修改

就是将这个名称呢

做一个调整

修改它的股票名称

然后呢

我们再去看一下它的一个变化

就在不重启服务的前提下面

看一下它的配置是否能够动态刷新

在这里呢

它整个服务已经启动完成了

对不对

端口呢是8080

那么我们就来访问一下

这个接口名称呢

接口名称的话呢

我们还没给他定义了

我们要注意了

在这里要加上一个注解

否则的话呢

也是不能访问的

然后呢

是get stock name

这跟分款名保持一致

这的话呢

我们重启下服务

然后呢

我们可以通过浏览器进行访问

80.80没有后缀

直接去访问get stock name

我们要不要传递一个股票名称呢

股票名称可以不用传递

他默认了就会打印配置里面所获取的属性值

好

那么我们访问一下

这个时候大家可以看到股票名称是不是能够读取到了

他的股票名称呢

就叫工商银行

我默认指的是中国平安

对不对

那么在配置中心里面呢

我们给他定义了一个属性

然后这个属性的话呢

给了他一个属性值是叫工商银行

所以呢

他会从中去读取并且呢

然后输出返回给客户端

那这个的话呢

配置的读取是没有问题

接下来我们就去验证一下动态配置的修改是否能够成功的呢

好

那么进入Nakos配置中心

将他呢改成招商银行

然后点击发布

这个时候大家可以看到

比较人性化

他能够提示你所修改的地方

防止出现错误

因为在一些线上的配置当中

有些配置项是比较重要的

如果是你修改错误了

可能会造成一些不可预知的损失

所以呢

我们一定要核对清楚

是不是我们预期修改错误

这是我们修改的一个结果

好

那这个的话呢

是从工商银行改成了招商银行

我们点击确认发布

他提示呢

已经是修改成功

我们返回一下

可以再查看详情

可以看到他已经改成招商银行

对不对

那我们接下来先别着急去验证

我们看一下后台日志有没有些什么变化

那我们的话呢

通过后台日志

我们可以看到他的一个日志信息

看到没有

loading nakos data

加载nakos中心

的数据

因为他检测到了nakos config demo

这个数据标识呢

他产生了内容产生了变化

所以呢

他将他的数据呢

重新做了更新

并且能够读取到对不对

最新的配置属性配置值呢

是招商银行好

那么我们再访问一下

刷新

这个时候大家可以看到是不是内容呢

已经发生变化

从之前的工商银行已经变成了招商银行

这个呢

就

验证了整个配置中心

他的一个读取

而且呢

他的一个动态配置的修改都是没有问题

那这个的话呢

是验证OK

接着话呢

咱们再来验证一下nakos的注册和发现功能

那同样我们把服务呢

启动一下

我们启动discovery下面的client还有售后端

右键run运行

好启动完成了

他应该在配置中心上面可以找到对应的服务节点

再去启动服务端

右键run运行

client已经启动完成

那我们去配置中心查看一下

点击服务列表

大家是不是可以看到nakos discovery client呢

他已经成功注册到我们nakos服务中心上面

那这个client呢是没有问题

接着话呢

我们再看一下

servo端这一块他也是启动OK的

我们再刷新下整个服务

服务端呢

也已经成功注册到nakos当中

那我们呢

就可以做一个访问进行了验证

那我们通过client的接口呢

进行访问调用来验证了整个服务的调用是否正常的

代码当中呢

我们提供的接口是叫client get stock price

对不对

那么我们呢

又来进行访问

将端口呢

改成8092

我们的client服务

然后呢

后面是接口名称get stock price

那在这里呢

我们可以给他一个股票名称

name呢

就比如说叫中国平安

好

然后我们看一下这个接口能不能访问成功

好

大家可以看到这个结果的话呢

能够正常返回

我们再刷新几遍

并且呢

价格也产生了一个变化

对不对

因为这一块的话呢

按照我们的随机数

在不断去生成和变化了

从中的话呢

我们可以知道client

nakos get stock price client

调用nakos get stock price server是OK的

他们的话呢

也正是依赖于nakos的服务注册发现

实现了服务节点之间的相互交换

和相互访问

好

这个呢

就是对nakos的配置功能

以及动态配置

还有服务注册发现

做了一个测试和验证

那整个验证结果的话呢

也是符合我们的预期

好

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 **Nacos 服务注册与配置中心** 的实战演示。讲师通过一个“股票价格服务”的示例，完整地展示了如何：
- **启动 Nacos 服务**：通过配置文件 `application.yml` 设置端口和服务器地址。
- **创建并管理配置**：在 Nacos 控制台中新建配置项，设置 `Data ID`、`Group` 和 `配置内容`。
- **服务注册与发现**：通过 Spring Cloud Nacos Discovery，将服务注册到 Nacos 服务列表。
- **动态配置**：通过 Nacos 的配置中心，动态修改服务的配置（如股票名称），并验证服务能实时感知并响应变化。
- **客户端调用**：通过客户端应用调用服务，验证服务发现和配置的正确性。

整个过程旨在说明 Nacos 在微服务架构中作为服务注册中心和配置中心的核心作用。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中的时间点，以下章节基于画面内容和逻辑顺序进行划分：

- **0:00 - 0:30**: **课程导航与目标介绍**。讲师在 Markdown 文档中展示课程大纲，当前章节为“3.8 启动验证”，目标是验证 Nacos 配置功能。
- **0:30 - 1:00**: **启动 Nacos 服务**。讲师展示 `application.yml` 配置文件，设置 `server.port=8091` 和 `spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848`，并说明访问地址 `http://127.0.0.1:8080/getStock`。
- **1:00 - 2:00**: **Nacos 配置中心操作**。讲师在浏览器中访问 Nacos 控制台，进入“新建配置”页面，设置 `Data ID` 为 `nacos-config-demo.properties`，`Group` 为 `DEFAULT_GROUP`，配置内容为 `stockName=建设银行`，并点击“发布”。
- **2:00 - 3:00**: **服务端代码与启动**。讲师在 IDEA 中展示服务端 `NacosConfigDemoApplication` 的代码，包含 `@Value` 注解注入配置，并启动服务。控制台显示服务成功注册到 Nacos。
- **3:00 - 4:00**: **修改配置并验证**。讲师在 Nacos 控制台修改配置内容为 `stockName=招商银行`，并再次发布。服务端控制台日志显示配置已更新。
- **4:00 - 5:00**: **客户端服务与调用**。讲师展示客户端 `NacosDiscoveryClientApplication` 的代码，使用 `RestTemplate` 调用服务。启动客户端后，通过浏览器访问 `http://127.0.0.1:8092/client?name=中国银行`，成功获取到股票价格。
- **5:00 - 5:30**: **总结与演示**。讲师在 Markdown 文档中总结，说明客户端成功通过 Nacos 找到服务并获取了正确的股票价格，验证了服务发现和配置中心的功能。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **Markdown 文档**：显示了课程大纲，包括“3.5 Nacos 架构设计”、“3.6 服务设计”、“3.7 工程结构”、“3.8 启动验证”等章节。
- **目标与分析**：明确指出本节目标是“验证 Nacos 配置功能”，并进行“分析”和“讲解”。
- **关键地址**：
  - Nacos 服务地址：`http://127.0.0.1:8080/getStock`
  - Nacos 配置管理地址：`http://127.0.0.1:8848/nacos/#/configurationManagement?serverId=center&namespace=&searchDataId=&searchGroup=`
  - 客户端调用地址：`http://127.0.0.1:8092/client?name=中国银行`

#### 代码关键内容

- **Nacos 服务端配置文件 (`application.yml`)**
  ```yaml
  server:
    port: 8091
  spring:
    application:
      name: nacos-discovery-server
    cloud:
      nacos:
        discovery:
          server-addr: 127.0.0.1:8848
  ```

- **Nacos 服务端 Java 代码 (`NacosConfigDemoApplication.java`)**
  ```java
  @SpringBootApplication
  @RestController
  public class NacosConfigDemoApplication {
      @Value(value = "${stockName:中国平安}")
      private String stockName;

      public static void main(String[] args) {
          SpringApplication.run(NacosConfigDemoApplication.class, args);
      }

      @RequestMapping("/getStockName")
      public String getStockName() {
          return "股票名称：" + stockName;
      }
  }
  ```

- **Nacos 客户端 Java 代码 (`NacosDiscoveryClientApplication.java`)**
  ```java
  @SpringBootApplication
  @RestController
  public class NacosDiscoveryClientApplication {
      @Bean
      public RestTemplate restTemplate() {
          return new RestTemplate();
      }

      @RequestMapping("/clientGetStockPrice")
      public String clientGetStockPrice() {
          // 调用服务端接口
          String result = restTemplate.getForObject("http://nacos-discovery-server/getStockName", String.class);
          return result;
      }
  }
  ```

#### 图表 / 界面截图

- **Nacos 控制台界面**：
  - **新建配置页面**：显示 `Data ID`、`Group`、`配置格式` 和 `配置内容` 字段。
  - **配置列表页面**：显示已创建的配置项，如 `nacos-config-demo.properties`。
  - **配置编辑页面**：显示配置内容编辑框，如 `stockName=招商银行`。

---

### 4) 关键场景与演示描述

#### 场景一：启动 Nacos 服务

- **描述**：讲师在 IDEA 中打开 `application.yml` 配置文件，设置 `server.port` 为 `8091`，并设置 `spring.cloud.nacos.discovery.server-addr` 为 `127.0.0.1:8848`。然后在浏览器中访问 `http://127.0.0.1:8080/getStock`，页面显示“股票名称：建设银行”，证明服务已启动并能响应请求。

#### 场景二：创建与修改配置

- **描述**：讲师在 Nacos 控制台中进入“新建配置”页面，设置 `Data ID` 为 `nacos-config-demo.properties`，`Group` 为 `DEFAULT_GROUP`，配置内容为 `stockName=建设银行`，并点击“发布”。随后，讲师修改配置内容为 `stockName=招商银行`，再次发布。服务端控制台日志显示配置已更新。

#### 场景三：客户端调用服务

- **描述**：讲师在 IDEA 中启动客户端应用 `NacosDiscoveryClientApplication`。在浏览器中访问 `http://127.0.0.1:8092/client?name=中国银行`，页面成功返回“股票名称：中国银行，股票价格：70”，证明客户端能通过 Nacos 服务发现并调用服务。

#### 场景四：验证服务发现与配置

- **描述**：讲师在 Nacos 控制台的“服务管理”页面中，可以看到服务 `nacos-config-demo` 和 `nacos-discovery-client` 已成功注册。通过客户端调用，验证了服务发现和配置中心的功能。

---

以上是根据视频画面进行的结构化技术分析，希望能帮助您更好地理解 Nacos 的服务注册与配置中心功能。
