# 21-车辆轨迹服务（pd-netty开发_HTTP接口方 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是整体来看了一下这个车辆轨迹服务啊,它的结构图,那接下来呢,我们就来开发第一个服务,就是PD-90这个服务,那么这个服务它的作用刚才也说了,它就是接收我们司机端上报的车辆定位信息,对吧,并且呢,把这个信息呢,把它发送到卡普卡队列当中,那这个时候呢,我们就需要来考虑一个问题,就是什么呢,这个司机端APP如何跟我们的PD-90来进行交互,对吧,我们说它上报信息其实就是什么呢,

就是它发送请求,请求到我们这个PD-90,并且呢,把它这个信息呢,作为参数的给我们传递过来,对吧,这就是上报信息,那么它跟我们PD-90来进行交互的话呢,我们这个地方呢,准备提供两种方式,分别是什么呢,这种TCP方式,还有一种就是HTTP接口的方式,那么也就是说司机端呢,它可以任意选择其中的一种,然后呢,都可以连接到我们的PD-90服务来上报信息,

好,但是呢,从这个效率上来说呢,肯定是TCP这种方式啊,它的效率会更高,好,那么我们这个地方呢,就为了能让这个,它的适用性更强,对吧,所以说呢,我们是提供两种这个接收方式,两种接收方式,

那么我们先来看第一种呢,就是这种HTTP接口方式,这种方式呢,是相对来说比较简单,对吧,那么我们就可以开发我们的Controller,对吧,然后呢,提供HTTP接口,然后呢,我们这个,

司机端呢,直接发送通过这个HTTP协议的方式,然后呢,来上报它的这个位置信息,然后一会儿呢,我们再来提供第二种,就是TCP这种方式,而这种方式的话呢,那么它走的就是很显然就是TCP协议,对吧,那么底层呢,我们就需要使用Netty来进行编程,基于Netty来实现的TCP方式,好,那首先呢,我们先来看第一种啊,就是比较简单的这种HTTP接口的方式,好,咱们呢,打开我们的这个,

打开我们的ID啊,然后呢,到这儿来,这是我们PDNetty,对吧,但是这里边呢,相关的明文坐标呢,我们都已经提供好了,这个我们就不再多说了,然后呢,我们直接使用就可以,然后接下来呢,我们需要来编写一个配置,对吧,这也就是我们这个bootstrap.yml,好,但是这个配置文件呢,我们前面已经建过很多了,所以在我这里边呢,其实已经提前提供好了,好,这些呢,配置,我们就不用再说了,然后呢,主要看一下这儿,对吧,

那么它当前激活的这个开发模式啊,这个模式呢,是这种DEV,对吧,那么也就是说我们当前这个环境是一个开发环境,开发环境的话呢,它就会读取这个文件,对吧,bootstrap-dev,这是根据规则啊,能够读取到这个文件,然后这个文件里边呢,前面这些配置我们是不是都看过了啊,包括我们这个discovery,对吧,服务的这个注册中心呢,还有什么配置中心呢,这些,好,然后呢,包括这一块,然后呢,可能不太一样的,

就是我们前面没有接触到的,就是下面这段配置,这个呢,其实就是关于卡夫卡的,啊,因为什么呢,因为我们刚才也看到了,咱们这个地方pdneti呢,它接收到这个位置信息之后啊,是不是需要把消息发送到卡夫卡对列当中,对吧,那这个时候呢,我们就需要在我们这个pdneti这个Main文工程当中来操作卡夫卡,对吧,来发送消息,那么具体怎么操作呢,我们就需要通过这段配置,通过这段配置,

那么配置上什么呢,我们这个卡夫卡,它的服务器的地址,对吧,服务器地址,当然这个地方呢,我们没有写死,而是什么呢,通过这种方式啊,这种语法的方式,从我们的配置中心是不是动态的去获取数据,对吧,那么具体这个卡夫卡,它的服务在什么位置呢,我们需要来看一下我们的配置中心,我这提前已经打开了,咱们现在用的就是这个配置中心,好,

然后呢,我们可以来看一下,

它应该读的是哪个文件呢,是不是应该是我们pdneti,然后什么dv.yml,对吧,pdneti,dv,应该是这个,好,然后呢,我们可以来看一下详情,对吧,大家可以看到,这是不是配置了我们卡夫卡,然后呢,这是不是bootstrap server,那么它就会读取到这个值,68797.219,对吧,端口号呢,还是默认的,就是9092,这个我们前面安装卡夫卡的时候,大家也都知道了,包括下边还有什么监听器,对吧,

然后什么线程数啊,等等,这些,好,重施的次数啊,等等,啊,这些,

所以说呢,我们回到这边来,你看,这边呢,它其实都是啊,我们全都是用这种类似于ER表达式这种写法,这样的话呢,它其实就是从我们这个配置中心的这个文件,动态的把这些值是不是给它读取到,好,

所以以后呢,我们改的话呢,咱们当前这个文件,项目内部的这个文件根本就不用改,哎,那么如果改的话呢,直接改配置中心,好,

我们改改配置中心那边这个文件,对吧,好,这是关于我们卡夫卡这块的配置,那么配置完之后呢,一会儿在我们的项目当中呢,就可以直接通过AutoVar的注解来注入卡夫卡提供的一个对象,然后我们就可以直接来操作卡夫卡对列了,对吧,比如说我可以向对列当中来发送消息,好,这是这个配置,好,你看,这第一步我们相当于就已经搞定了啊,还有这个,对吧,什么PlusFab-D1V,啊,这个就已经搞定了,好,

然后接下来呢,我们需要来编写一个实体类啊,这个实体类呢,就是来封装什么呢,封装我们这个位置信息的,哎,因为呢,它这边,哎,我们来看这个图,它是不是需要把这个消息啊,发送到卡夫卡当中,对吧,哎,那么这个时候呢,我们就可以通过这么一个实体类,哎,把这些信息呢,全都封装到这个实体类里面去,咱们可以先来看一下,这个实体类里面都有什么呢,有这个ID,对吧,当然我们只要提供这个实体类,

这个getID方法就可以了,好,然后呢,这个ID的话呢,它不是一个简单的属性,它是由这么三部分构成的,一个是businessID,businessID呢,其实就是业务ID,对吧,就是业务ID,好,然后呢,加上一个type,这个type呢,从哪来的呢,就是这个,哎,就是类型,好,这个类型的话,你看啊,有这个什么呢,有tranc啊,有courier,tranc代表的是车辆,对吧,哎,其实指的就是我们司机的坐标信息,如果是courier呢,代表的就是快递员的,

坐标信息,哎,因为我们这一块啊,不光是针对这个司机来收集他的坐标信息,那么快递员他在派送过程当中,对吧,那么我们也希望能够知道快递员他每时每刻他在什么位置,对吧,他的坐标信息也需要存进来,所以说呢,快递员那个APP呢,也会实时的上报他的信息,当然是在他派送过程当中才会上报信息,啊,如果他是在下班的时候,他,我们收集这个信息其实是没有任何意义的,对吧,所以说呢,应该是快递员呢,

快递员在派送过程当中,或者是司机在运输过程当中,这个时候呢,他才会上报信息,啊,所以说呢,我们这个地方呢,是通过这么一个type是不是来进行区分,对吧,我们收集的这个坐标信息到底是这个司机的车辆的呀,还是快递员的呀,那么有通过type来进行这个描述,啊,然后还有一个是current time,对吧,就是当前的时间,啊,这是业务ID,对吧,然后呢,还有什么呢,name,这就是司机的名称,啊,

啊,司机的电话,对吧,但是如果是对应的是,也可能是快递员的名字,对吧,也可能是快递员的电话,啊,这个呢,只是这样描述了一下,啊,然后呢,这是车牌号,然后还有什么呢,进度,纬度,对吧,这两个是最关键的信息,进纬度,啊,还有一个时间,还有所属的车队,对吧,还有运输任务的ID,等等,这个都是跟我们的业务相关的,啊,所以说呢,我们就需要把整个位置信息包括这么多,对吧,全都封装到这个地方,

这个实体类里面去,好,那接下来呢,我们把这个实体类呢,来创建一下,啊,咱们创建一个entity包,在我们这个地方来创建一个entity包,存放我们的实体,对吧,这个实体类叫什么名字呢,我就不敲了,咱们直接从讲义上来抄一下,叫做location entity,好,location entity,所有的代码呢,我就直接全考过来,好,整理一下,那这样的话,我们这个

实体类呢

就已经搞定了

还是比较简单的

从这描述

你看API model

描述这个实体

它是一个什么呢

位置信息的

封装的位置信息

然后呢

我们接下来

看下一个

下一个是不是就是

编写一个启动类的吧

这个启动类呢

我也就不写了

直接从这来抄一下

放在上一层目录

品达这层目录里面来

整个这个代码

我就来复制一下

那么一个是

Spring Boot Application

这是必须的

一个Spring Boot应用

还有一个呢

开启我们这个什么呢

服务发现的客户端

对吧

那么因为它是需要

有可能是需要

去查找一些服务的

好

这个就不用说了

这是关于我们这个

启动类的吧

好

那么前面这四步呢

都是比较简单的

那么我们直接从这个

讲义当中考过来

一会儿呢

我们来看第五步的话呢

这就是比较关键了

就是什么呢

我们需要来编写

这么一个类

叫做Kavka Center

其实从这个名字上

大家也能够看到

这个呢

类呢

主要就是用来操作

我们的Kavka的

用于操作Kavka

好

那么我们先说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是“品达物流TMS项目”第7章《车辆轨迹服务开发》的第1部分，主要讲解如何使用 `pd-netty` 服务来接收司机App上报的车辆定位信息，并将这些信息发送到 Kafka 队列。课程内容聚焦于 `pd-netty` 服务的 HTTP 接口方式开发，包括配置文件（`bootstrap.yml` 和 `bootstrap-dev.yml`）的编写、实体类 `LocationEntity` 的定义以及服务启动类的编写。整个开发流程旨在构建一个能够接收并处理车辆轨迹数据的后端服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，展示项目结构和本章目标。
*   **00:15 - 00:30**: 讲解 `pd-netty` 服务的核心功能和两种接入方式（TCP 和 HTTP）。
*   **00:30 - 01:00**: 详细介绍 `pd-netty` 服务的 HTTP 接口开发步骤。
*   **01:00 - 01:30**: 展示并讲解 `bootstrap.yml` 配置文件，包括 Spring Cloud Nacos、Kafka 等配置。
*   **01:30 - 02:00**: 展示并讲解 `bootstrap-dev.yml` 配置文件，用于开发环境。
*   **02:00 - 02:30**: 编写 `LocationEntity` 实体类，定义车辆定位信息的结构。
*   **02:30 - 03:00**: 编写服务启动类 `NettyApplication`，配置服务发现。
*   **03:00 - 03:30**: 讲解后续步骤，包括编写 `KafkaSender` 用于操作 Kafka。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **PPT / 图表**

*   **系统架构图** (00:00): 展示了 `司机App` -> `pd-netty` -> `kafka` -> `druid` -> `浏览器` 的数据流向。
*   **章节大纲** (00:00): 显示了课程的目录结构，当前位于“5. 车辆轨迹服务”下的“5.1 pd-netty开发”。

#### **代码**

*   **`pom.xml` 配置** (00:30):
    ```xml
    <groupId>com.itehima</groupId>
    <artifactId>pd-netty</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <name>pd-netty服务</name>
    <description>netty服务</description>
    ```
    定义了项目的基本信息和依赖。

*   **`bootstrap.yml` 配置** (01:00):
    ```yaml
    spring:
      cloud:
        nacos:
          username: tms
          password: itehima123
          discovery:
            server-addr: 68.79.63.42:8848
            group: pinda-tms
            namespace: 6107553214-48d8-89c3-945f8446e3d9
        config:
          server-addr: 68.79.63.42:8848
          group: pinda-tms
          namespace: 6107553214-48d8-89c3-945f8446e3d9
    jackson:
      time-zone: ${spring.jackson.time-zone}
      date-format: ${spring.jackson.date-format}
    servlet:
      multipart:
        max-file-size: ${spring.servlet.multipart.max-file-size}
        max-request-size: ${spring.servlet.multipart.max-request-size}
        enabled: ${spring.servlet.multipart.enabled}
    # kafka
    kafka:
      bootstrap-servers: ${spring.kafka.bootstrap-servers}
      listener:
        concurrency: ${spring.kafka.listener.concurrency}
      producer:
        retries: ${spring.kafka.producer.retries}
        batch-size: ${spring.kafka.producer.batch-size}
        buffer-memory: ${spring.kafka.producer.buffer-memory}
        key-serializer: ${spring.kafka.producer.key-serializer}
        value-serializer: ${spring.kafka.producer.value-serializer}
      consumer:
        group-id: ${spring.kafka.consumer.group-id}
    ```

*   **`bootstrap-dev.yml` 配置** (01:30):
    ```yaml
    server:
      port: 8192
      connection-timeout: 5000ms
    spring:
      application:
        name: pd-netty
        profiles:
          active: dev
        main:
          allow-bean-definition-overriding: true
    ```

*   **`LocationEntity` 实体类** (02:00):
    ```java
    @Data
    @ApiModel("位置信息")
    public class LocationEntity {
        public String getId() {
            return businessId + "#" + type + "#" + currentTime;
        }
        @ApiModelProperty("业务id，快递员id 或者 车辆id")
        private String businessId;
        @ApiModelProperty("司机名称")
        private String name;
        @ApiModelProperty("司机电话")
        private String phone;
        @ApiModelProperty("维度")
        private String lat;
        @ApiModelProperty("经度")
        private String lng;
        @ApiModelProperty("当前时间，格式：yyyy-MM-dd HH:mm:ss")
        private String currentTime;
        @ApiModelProperty("所属车队")
        private String team;
        @ApiModelProperty("运输任务id")
        private String transportTaskId;
    }
    ```

*   **`NettyApplication` 启动类** (02:30):
    ```java
    @SpringBootApplication
    @EnableDiscoveryClient
    public class NettyApplication {
        public static void main(String[] args) {
            SpringApplication.run(NettyApplication.class, args);
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：系统架构概览** (00:00)
    *   **描述**: 讲师首先展示了一个系统架构图，图中清晰地描绘了司机App如何通过 `pd-netty` 服务上报位置信息，`pd-netty` 服务再将消息发送到 Kafka，最终由 Druid 服务进行数据查询。这为后续的开发工作提供了宏观的背景。

*   **场景二：开发环境与配置** (00:30)
    *   **描述**: 讲师在 IntelliJ IDEA 中打开项目，展示了 `pom.xml` 文件，确认了项目依赖。随后，讲师切换到 `bootstrap.yml` 文件，详细讲解了其中的 Spring Cloud Nacos 服务发现和 Kafka 生产者/消费者配置，强调了配置文件中使用环境变量（如 `${spring.kafka.bootstrap-servers}`）的灵活性。

*   **场景三：开发环境配置** (01:00)
    *   **描述**: 讲师展示了 `bootstrap-dev.yml` 文件，这是为开发环境准备的配置文件。他重点讲解了 `server.port` 和 `spring.application.name` 的设置，以及 `spring.profiles.active` 用于激活开发环境配置。

*   **场景四：实体类开发** (02:00)
    *   **描述**: 讲师开始编写 `LocationEntity` 实体类，用于封装车辆定位信息。他使用了 Lombok 的 `@Data` 注解简化代码，并使用 `@ApiModel` 和 `@ApiModelProperty` 注解为 Swagger 提供 API 文档。他详细讲解了每个字段的含义，如 `businessId`（业务ID）、`lat`（纬度）、`lng`（经度）和 `currentTime`（当前时间）。

*   **场景五：服务启动** (02:30)
    *   **描述**: 讲师编写了 `NettyApplication` 启动类，使用 `@SpringBootApplication` 注解标记这是一个 Spring Boot 应用，并使用 `@EnableDiscoveryClient` 注解启用服务发现功能，以便服务能够注册到 Nacos 中。

*   **场景六：后续步骤预告** (03:00)
    *   **描述**: 讲师在屏幕右下角显示了“第五步：编写 KafkaSender，用于操作 Kafka”的提示，预告了接下来将要讲解的内容，即如何将接收到的数据发送到 Kafka 队列。
