# 08-Nacos介绍-discovery工程搭建与配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们继续讲解和实现Nakos的注册服务

Nakos注册服务在这里面主要是分为两个模块

一个是它的client端

另外一个是它的收货端

好 那我们就来做一个具体实现

同样在Nakos的demo下面新建一个模块

点击next

给它一个模块名称

Nakos Discovery Demo

点击next

将名称做个调整

点击finish

好 创建完成之后呢

我们在下面创建两个子模块

这个呢就是具体的服务实现

那我们再创建model

点击next

下面呢我们创建一个服务叫Nakos Discovery

这个呢就作为client端

服务发现对不对

你必须要有一个client端

还得有一个什么服务端

那我们点击finish

先把client端创建好

client端创建完成之后呢

我们再创建它的finish

我们再创建它的服务端model

然后呢将它名称改为serve

好 点击next

那接下来的话点击finish

注意它的一个层次结构不要搞错了

引破的导入生效

导入生效完成之后呢

我们看一下这两个工程下面需不需要加依赖呢

并不需要加额外的其他依赖

因为呢在他们的复集工程下面

也就是Nakos Demo下面呢

已经加入了对应的服务注册发现的依赖了

好 接下来呢我们就可以做具体实现了

那在client下面呢

我们首先去创建它对应的包

package.com.idcast

然后呢nakos.discovery.client

好 OK

接下来的话我们再创建一个启动类

这个启动类名称呢

我们叫nakos.discovery.cove.application

点击OK

这个启动类的话呢

就是负责nakos.discovery的一个客户端的实现

那我们在这里呢

必须要给它对应的接口对不对

还有呢它的一些启动配置

那我们呢首先来实现一下supreme boot application

这个注册必须要加入进去

然后呢还有什么enable.discovery服务的注册发现

这个呢要把它加入进来

然后呢是我们的let'scontroller要实现了一个attp接口

咱们呢看一下怎么去调用呢

就可以通过let'stemplate做一个调用

let'stemplate

let'stemplate呢是除了

分内本之外的一个更底层的attp调用的组件

因为分内本他们呢

分是基于内本去做的调用

那么内本呢是基于let'stemplate去做的调用和实现

这一点关系呢大家要理解清楚

autowide

好

接下来的话呢我们要给它一个启动路口

supreme application

点乱

我们把这个class呢

填入进去

然后呢class将参数也填入进去

接着的话呢我们就必须要给它配置一个什么

let'stemplate对不对

好

那我们做个配置public let'stemplate

然后呢给它一个新增的注册发对象

在这里呢它要纳入到supreme容器当中去进行管理

然后呢它可以支持什么

负载均衡的方式进行调用

load balance

这个呢是let'stemplate的一个配置

就是template

完成调用配置

再往下面的话呢就是我们的提供接口

对不对

由客户端去调用和访问

那我们要提供一个什么接口呢

就是在我们讲义当中

在这里呢所规划的要获取股票名称的一个接口

这个呢是配置符

是下面要获取股票价格的一个接口

那么呢做一个具体实现

public

student

然后呢client

get stock price

下面的话呢要给它一个参数

你要传递一只股票

然后呢我配置这股票去返回对应的价格给你

对不对

这个的话呢是一个strain内型

那么加上它对应的注释

就是提供了客户端

获取股票价格接口

那这里呢怎么去调用和访问呢

就通过let'stemplate

进行一个远程的调用访问

get for object

object

get for object

好

然后呢要传递什么

url

这个url的话呢

我们写下attp

nucleus

这个我们就可以通过服务名称进行一个调用

就是这个nucleus discovery

好

因为它可以支持负载讯息嘛

对不对

所以不需要指定IP

然后呢get

get stock

price

然后呢是

name

等于

然后再拼接一下它传递过来的

name参数

下面的话呢

是它的一个内型

stream class

好

这样的话呢

就实现了一个远程调用

并且呢将结果返回给我们的接口

然后呢做进一步的一个返回

最后呢把结果输出给客户端

这个呢就是client的一个调用流程

接着的话呢

我们再实现client的一个配置

创建一个配置文件

叫application

点properties

创建完之后呢

我们给它一个基础的配置

收入点pod

8092端口

然后呢

服务名称application name

这个呢就取它的模块名称copy过来就行了

下面的话呢

就是naco传输的服务注册发现的地址

servo.js

127.0.0.1

8848

默认端口

这样呢就完成了客户端的一个基础性的配置

因为我们在这里呢

最主要是侧重什么

服务的注册和发现

那么通过这个client端

我们可以知道

我们并没有去指定服务的IP

对不对

那么如果是通过naco进行一个连接和调用

它能不能正常获取到远程服务的节点信息

能不能调用成功呢

好

这个呢就是我们接下来要做的启动和验证

那在启动验证之前呢

我们还必须把naco server服务端做一个实现

对不对

创建一个package

new

然后呢

给它一个报名

com.itcast

naco discovery

servo

同样的

我们要给它创建一个启动类

newcast

然后呢

naco

discovery

servo application

这个启动类的话呢

我们同样也实现它的一个基础性配置

supreme boot application

然后呢

enable

开启了服务的注册发现

然后呢

再给它一个less controller

就是一个远程访问的

提供一个远程接口

这个接口的话呢

就是返回股票的价格

psvm

supreme application

.run

然后呢

naco discovery class

然后呢

packs将参数也传递过去

好

那我们再看一下

这个股票价格接口的实现

public stream.getstock

视频拼错了

getstock price

在这里面呢

要给它一个参数

就是客户端所传递过来的股票价格

是

stream name

然后呢

我们还给它一个

默认值

如果说没有传递呢

我们不给它报错

我们给它的一个默认值就可以啊

efeo default

然后呢

是中国平安

这次话呢

咱们再实现它具体的逻辑

我们把它移过来一点

它的逻辑的话呢

也很简单

将股票价格呢

股票名称和股票价格呢

返回给客户端就可以了

股票名称

然后呢

就是它接收到的内容参数

然后再做一个拼接

返回了股票价格

股票价格在这一块呢

我们就给它一个随机数

确保每次访问呢

结果不一样

也变我们的一个直观验证

然后呢

next

in

在这里面呢

给它一个指定的随机范围

20

然后再加20到100的一个随机价格

这样呢

就完成了获取股票价格的一个接口

我们给它加上对应的注释

提供了查询股票价格的接口

好

再往下面的话呢

我们还要实现它的配置文件

对不对

new file

然后呢

application

点properties

那么servo.port

给它一个端口

8081

sprint.application

这个呢

是它的服务模块名称

我们将它copy下

然后呢

是sprint.cloud

它的服务注册地址

servo.js

127.0.0.1

然后呢

端口是8848

这样呢

就完成了

注册发现的

客户端的实现

那这一讲呢

我们就实现了注册发现的客户端

以及呢

服务端的编码和它的具体配置

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析：

---

### 1) 视频摘要

本视频课程是关于 **Nacos 服务发现与配置中心** 的实战演示。讲师通过 IntelliJ IDEA 开发环境，逐步构建一个包含 **配置中心（nacos-config-demo）** 和 **服务发现（nacos-discovery-demo）** 两个核心模块的 Spring Cloud 项目。演示重点在于如何使用 Nacos 注册中心实现服务的自动发现与负载均衡，以及如何通过 Nacos 配置中心管理应用配置。整个过程展示了从项目结构搭建、依赖配置、服务端代码编写到客户端调用的完整开发流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程引入，展示项目整体结构图，介绍 Nacos 在微服务架构中的角色。
*   **00:16 - 00:30**: 展示项目目录结构，重点介绍 `nacos-config-demo` 和 `nacos-discovery-demo` 两个模块。
*   **00:31 - 00:45**: 编辑 `nacos-discovery-demo` 模块的 `pom.xml` 文件，添加 Spring Cloud Alibaba Nacos Discovery 依赖。
*   **00:46 - 01:00**: 在 `nacos-discovery-client` 模块中编写 `NacosDiscoveryClientApplication` 启动类，并配置 `RestTemplate` 用于远程调用。
*   **01:01 - 01:15**: 在 `NacosDiscoveryClientApplication` 中编写 `clientGetStockPrice` 方法，使用 `@LoadBalanced` 注解和 `RestTemplate` 调用服务。
*   **01:16 - 01:30**: 编辑 `application.properties` 文件，配置 Nacos 服务注册中心地址。
*   **01:31 - 01:45**: 在 `nacos-discovery-server` 模块中编写 `NacosDiscoveryServerApplication` 启动类。
*   **01:46 - 02:00**: 在 `NacosDiscoveryServerApplication` 中编写 `getStockPrice` 接口，模拟返回股票价格。
*   **02:01 - 02:15**: 项目结构总结，强调 Nacos 在服务发现和配置管理中的作用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **系统架构图**: 展示了客户端（手机/用户）通过 HTTP 请求调用“获取股票价格”服务，该服务通过“Nacos 注册中心”发现并调用“股票价格服务”的流程。
    *   **项目结构图**: 以文件夹形式展示了 `nacos-config-demo` 和 `nacos-discovery-demo` 两个模块的目录结构，包括 `src`, `target`, `pom.xml` 等标准 Maven 项目文件。

*   **代码**:
    *   **`pom.xml` (nacos-discovery-demo)**:
        ```xml
        <parent>
            <artifactId>nacos</artifactId>
            <groupId>com.itcast.trade</groupId>
            <version>1.0-SNAPSHOT</version>
            <modelVersion>4.0.0</modelVersion>
        </parent>
        <artifactId>nacos-discovery-demo</artifactId>
        ```
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        ```
    *   **`NacosDiscoveryClientApplication.java`**:
        ```java
        @RestControllerAdvice
        public class NacosDiscoveryClientApplication {
            @Bean
            @LoadBalanced
            public RestTemplate restTemplate() {
                return new RestTemplate();
            }

            public String clientGetStockPrice(@RequestParam String name) {
                return restTemplate.getForObject(url: "http://nacos-discovery-server/getStockPrice", String.class);
            }
        }
        ```
    *   **`application.properties`**:
        ```properties
        spring.application.name=nacos-discovery-client
        server.port=8080
        spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848
        ```
    *   **`NacosDiscoveryServerApplication.java`**:
        ```java
        @SpringBootApplication
        @RestController
        public class NacosDiscoveryServerApplication {
            @Bean
            @LoadBalanced
            public RestTemplate restTemplate() {
                return new RestTemplate();
            }

            public String getStockPrice(@RequestParam(defaultValue = "中国平安") String name) {
                return "股票名称：" + name + "，股票价格：" + (new Random().nextInt(10000));
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与依赖配置** (00:31 - 00:45)
    *   讲师在 IntelliJ IDEA 中打开项目，展示 `nacos-discovery-demo` 模块的目录结构。
    *   通过右键菜单选择“Find in Path...”并搜索 `nacos-discovery-demo`，定位到 `pom.xml` 文件。
    *   在 `pom.xml` 中，讲师添加了 `spring-cloud-starter-alibaba-nacos-discovery` 依赖，用于实现服务注册与发现功能。

*   **场景二：客户端服务调用** (00:46 - 01:15)
    *   讲师在 `NacosDiscoveryClientApplication` 类中编写 `restTemplate` Bean，使用 `@LoadBalanced` 注解启用负载均衡。
    *   讲师编写 `clientGetStockPrice` 方法，使用 `RestTemplate` 的 `getForObject` 方法调用远程服务。
    *   讲师在 `application.properties` 中配置 Nacos 注册中心地址 `spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848`。

*   **场景三：服务端接口实现** (01:31 - 02:00)
    *   讲师在 `NacosDiscoveryServerApplication` 类中编写 `getStockPrice` 方法，该方法接收股票名称参数并返回一个随机生成的“股票价格”。
    *   讲师通过 `@RestController` 注解将该方法暴露为 HTTP 接口。

*   **场景四：系统集成与演示** (02:01 - 02:15)
    *   讲师总结了整个项目结构，强调 Nacos 作为服务注册中心和配置中心在微服务架构中的核心作用。
    *   通过客户端调用服务端接口，演示了服务发现和负载均衡的完整流程。

---
