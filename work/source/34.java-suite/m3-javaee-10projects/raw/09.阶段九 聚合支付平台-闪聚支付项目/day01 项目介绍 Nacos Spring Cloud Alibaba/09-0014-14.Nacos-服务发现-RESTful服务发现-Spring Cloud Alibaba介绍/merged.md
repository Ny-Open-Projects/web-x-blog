# 14.Nacos-服务发现-RESTful服务发现-Spring Cloud Alibaba介绍

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\14.Nacos-服务发现-RESTful服务发现-Spring Cloud Alibaba介绍【海量资源尽在 666java.com】.mp4
- 时长 6分36秒（音频 396s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,接下来我们来学习RESTful服务发现那么Necros作为服务发现中心我们可以把RESTful服务注册到Necros中那其实在前边我们所写的测试程序我们当初实现了Service A和Service B那它对外暴露的其实就是一个RESTful服务那RESTful服务在互联网开发当中是比较常见的一种微服务的形式
[00:28] 那首先我们先来看一下RESTful服务发现首先我们先准备一下测试环境那么我们说这套测试环境呢需要具备什么样的功能当初我们在学习服务发现流程的时候大家应该还记得首先呢我们说每个微服务它是不是有一个服务发现的客户端需要请求服务发现中心拿到服务注册表那其实各位每个微服务都需要这个客户端那么这个客户端应该是一个
[00:57] 通用的东西需要我们去在我们的测试环境当中呢去实现它另外还有一点就是服务的消费方需要通过负载均衡的机制呢去获取到一个地址进行远程调用所以负载均衡这个也需要我们的测试环境也来实现这样的话我们整个服务发现的流程这两点是不是就满足了所以接下来我们来看这套测试环境我们是准备采用什么Spring Cloud Alibaba新发布的一个
[01:27] 微服务框架来完成那其实从这个字面上来看一下其实它是阿里开源的基于Spring Cloud的一套微服务框架所以这里边有两个东西一个是Spring Cloud一个是Spring Cloud的阿里巴巴来我给大家解释一下Spring Cloud呢大家应该有人听说过它是当前比较流行的一套微服务开发的一套框架集合它是Spring的一个项目
[01:55] 其实大家可以进到Spring Cloud的这个项目的主页那这个页面呢也是Spring官方的一个地址它是Spring Cloud的一个项目页面那么这个Spring Cloud呢其实它集成了很多这个什么很多的这个微服务开发的一些什么框架来实现整个微服务开发的一个技术生态那其实Spring Cloud各位你要把它理解成一套什么
[02:24] 微服务开发的什么标准注意你把它理解成一套标准为啥我说它是一套标准是因为Spring的思想它是要拿来主义是吧要集成一些比较优秀的项目来整合进来来供企业使用所以Spring Cloud也是基于这种思想它只是制定一套微服务开发的标准那么它把很多的这种什么
[02:52] 微服务开发的项目呢都集成进来在里面最有名的啊应该有同学自学过一些Spring Cloud的知识应该知道有一个叫Netflix公司一个做这个唱片的一个公司他呢其实这家公司开发了很多优秀的开源框架都被Spring Cloud给集成进来了比如说他的服务注册中心有一个叫Eureka还有他的网关注还有等等啊很多
[03:19] 所以后期我们学习Spring Cloud的知识的时候呢你就会接触这个公司的很多开源项目所以Spring Cloud呢它是一套什么它是一套微服务开发的标准然后呢集成众多公司的这个微服务开发的项目组成这么一个微服务开发框架的集合好了那么那Spring Cloud阿里巴巴又是什么呢因为我们说Spring Cloud是一套标准所以阿里巴巴呢就基于Spring Cloud这一套标准呢它呢
[03:48] 开发了一套微服务的开发框架所以这个名字就叫做Spring Cloud Alibaba大家能理解吧那么其实Spring Cloud Alibaba它和Netflix它的地位也是一样的都是基于Spring Cloud这个标准所开发的一套微服务框架集合好那这个呢就是Spring Cloud Alibaba这个项目的地址那我们可以到它的这个GitHub这个它的一个项目的主页我们来看一下
[04:18] 当然它的源码也是开源的这里面有很多的这些说明那么当前版本大家可以看到它已经发展到2.1.1了那么我们项目会采用比较主流一个版本也是2019年发布的就是2.1.0这个版本那么Spring Cloud我们来看当前版本是应该是这个叫Houston对吧那我们用它比较主流的一个版本叫Greewich这个版本
[04:48] 当然你会发现它是不是还有一个版本对其实这里边你会发现Greywich它的版本已经发展到SRC这个版本所以我们用Greywich然后Hodlton当前版本我们暂时先不用为什么选择这个版本是因为我们最终会用Spring Cloud的阿里巴巴对吧那么它其实是支持Greywich这个版本大家看到了吗对主要是因为我们要选择Spring Cloud的阿里巴巴然后我们要选择Spring Cloud的
[05:17] 和这个Spring Cloud的阿里巴巴这套框架集合进行匹配所以我们的项目呢就采用Spring Cloud Greenwich这个版本以及Spring Cloud的阿里巴巴2.1.0这个版本好那以上呢其实就是我们说的Spring Cloud和Spring Cloud的阿里巴巴它的一个意义Spring Cloud相当于一套微服务开发的标准然后呢Spring Cloud的阿里巴巴基于这套标准进行实现了一系列的微服务开发框架那么我们学习的Necros
[05:44] 其实就属于Spring Cloud的阿里巴巴这个技术生态当中的一个产品好我们刚才说这套测试环境我们需要具备什么需要具备两点第一点这个服务发现的客户端需要从服务发现中心获取服务列表因为我们说每个微服务都需要这么一个客户端那么到这个Spring Cloud的阿里巴巴这套框架它应该有这个客户端对吧就不用我们去开发了另外还有一套就是
[06:13] 服务消费方通过负载均衡来获取服务地址这是刚当初我们学习服务发现流程的时候这两点这两点应该是我们采用Spring Cloud Alibaba这套框架这套环境它所具备的功能好了那以上呢是我们介绍了Spring Cloud以及Spring Cloud Alibaba的一些情况好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud Alibaba 生态中，通过 Nacos 实现服务发现与消费，包括配置文件、代码实现和相关技术文档查阅。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE 中展示项目结构，选中 `Nacos-RESTful-consumer` 模块。
- `application.yml` 文件内容：
  server:
    port: 58020
  #配置为提供方的地址（小端口）
  provider:
    address: 127.0.0.1:58010

画面2：
- IDE 中展示 `RestConsumerController` 类代码。
- 代码中使用 `RestTemplate` 调用服务：
  String result = restTemplate.getForObject("http://" + provider + "/Service", String.class);
  return "consumer invoke!" + result;

画面3：
- PPT 页面标题为“2.3 RESTful服务发现”，子标题“2.3.1 测试环境”。
- 文本内容：
  Spring Cloud 是一套微服务开发框架集合，包括微服务开发的方方面面，Spring Cloud 是一套微服务开发的标准，集成了很多优秀的开源框架，比如有名的Netflix公司的众多项目。
  本测试环境采用阿里开源的Spring Cloud Alibaba微服务开发框架，Spring Cloud Alibaba是阿里巴巴公司基于Spring Cloud标准实现一套微服务开发框架集合，它和Netflix一样都是Spring Cloud微服务开发实现方案。
  Spring Cloud 项目地址：https://spring.io/projects/spring-cloud
  Spring Cloud Alibaba项目地址：https://github.com/alibaba/spring-cloud-alibaba
  通过Spring Cloud Alibaba实现解决：
  1. 服务发现客户端从服务发现中心获取服务列表
  2. 服务消费方通过负载均衡获取服务地址

画面4：
- PPT 页面展示服务发现流程图。
- 图中包含：
  - 服务发现中心（橙色方框）
  - Service A（蓝色六边形）
  - Service B（蓝色六边形）
  - 服务发现客户端（蓝色六边形）
- 流程：
  (1) Service A 上报地址 192.168.25.3:8080 到服务发现中心。
  (2) 服务发现客户端从服务发现中心获取服务注册表。
  (3) 服务发现客户端调用 Service B。
  (4) Service B 上报地址 192.168.25.4:8080 到服务发现中心。

画面5：
- 浏览器打开 Spring Cloud 官网的“Documentation”页面。
- 页面显示多个版本的文档链接，如 Hoxton CURRENT GA、Hoxton SNAPSHOT、Greenwich SR4 GA、Finchley SR4 GA。

画面6：
- 浏览器在 Spring Cloud 官网中点击“Spring Cloud Alibaba”链接。
- 页面显示 Spring Cloud Alibaba 的文档列表。

画面7：
- PPT 页面标题为“2.3.1 测试环境”。
- 文本内容与画面3相同。

画面8：
- 浏览器打开 GitHub 的 Spring Cloud Alibaba 仓库页面。
- 页面显示仓库的文件列表，包括 `spring-cloud-alibaba-Nacos-config`、`spring-cloud-alibaba-Nacos-discovery` 等。

画面9：
- 浏览器在 GitHub 页面中点击“spring-cloud-alibaba-Nacos-config”文件夹。
- 页面显示该文件夹下的文件列表，包括 `pass checkstyle plugin`、`format code with maven plugins` 等。

画面10：
- 浏览器打开 Spring Cloud Alibaba 的 GitHub Releases 页面。
- 页面显示 v2.1.1.RELEASE 版本的发布说明，包括：
  Features / Enhancements
  - Adding module Spring Cloud Alibaba Sidecar(#941)
  - ROM has dependency management for non direct dependencies(#911)
  - OssStorageResource support WritableResource(#930)
  - Nacos Discovery support GROUP(#608)
  - Nacos Config support json and xml format(#608)
  - NacosRestTemplate support UrlClean(#762)
  - Nacos Config support more configuration items(#409)
  - Enhance RocketMQ Binder header value coded(#737)
  - Use partition to implement RocketMQ queue selection(#733)
  - Adding recurrence times in header(#415)
  - Disable Sentinel web filters when using Sentinel gateway starters(#811)

画面11：
- 浏览器在 Spring Cloud 官网中点击“Guides”标签。
- 页面显示“Client-Side Load-Balancing with Spring Cloud LoadBalancer”指南。

画面12：
- 浏览器在 Spring Cloud 官网中点击“Projects”标签。
- 页面显示“Spring Cloud”下的子项目列表，包括 Spring Cloud Alibaba、Spring Cloud for Amazon Web Services、Spring Cloud Bus、Spring Cloud CLI、Spring Cloud Cluster、Spring Cloud Commons、Spring Cloud Config、Spring Cloud Consul、Spring Cloud Contract、Spring Cloud Function 等。

画面13：
- PPT 页面标题为“2.3.1 测试环境”。
- 文本内容与画面3相同。

画面14：
- PPT 页面标题为“2.3.1 测试环境”。
- 文本内容与画面3相同。

