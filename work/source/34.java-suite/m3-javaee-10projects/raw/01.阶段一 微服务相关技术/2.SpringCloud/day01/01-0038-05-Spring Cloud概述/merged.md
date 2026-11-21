# 05-Spring Cloud概述

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\05-Spring Cloud概述_【海量资源尽在 ubkz.com】.mp4
- 时长 6分25秒（音频 385s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] Spring Cloud 概述在这一小节中我们的主要目标是了解 Spring Cloud 整合的组件和版本特征现在我们打开讲义来了解 Spring Cloud微服是一种架构方式需要技术架构去实施微服实现的方式有很多但是当下最火的那就是 Spring Cloud 了为什么因为它后台硬作为 Spring 家族的一员有整个 Spring 全家统靠山技术强有强力的
[00:31] Spring技术团队支撑群众基础好很多企业都在使用Spring而Spring Cloud与Spring的各个框架无缝整合那大家在开发的时候用起来就会有比较有熟悉感使用方便前面我们用Spring Boot的时候可以通过添加具体的启动器依赖到我们的工程中就可以方便的快捷的去整合各种组件而Spring Cloud完全支持
[00:57] Springboard的开发使用很少的配置就能够完成微幅框架的搭建其实呢我们的Springcloud是要基于Springboard来去搭建微幅框架里面的那些微幅的微幅系统的OK所以我们后面如果要去用Springcloud中提供的各种组件的话一样的只要在我们的Po文件中去添加对应的启动器依赖那么这个组件也就被用起来了OK那接下来具体来了解
[01:28] Spring CloudSpring Cloud是Spring旗下的项目之一它的官网地址那我们来访问一下它的地址呢是这一个访问以后你见到了它的一个概述它的特征说明它的版本信息它的一个案例说明OK有这一些那么回到我们的讲义中来去继续了解Spring最擅长的就是集成然后把很多其他框架都集成到自己的项目中Spring Cloud也是一样
[01:56] 它将现在非常流行的一些技术整合到一起实现了诸如配置管理服务发现智能路由负载均衡熔断器控制总线集群状态等功能协调分布室环境中各个系统为各类服务提供模板性配置那主要我们设计的组件呢有Urica注册中心ZOO或者是Gateway服务网关Ribbon负载均衡FAN服务调用High Street
[02:25] 或者是resilient4j熔断器那如果用了这些组件的话它的综合架构可以如下我们大概来说一下当一个请求过来的时候首先经过一个网关那这个网关可以用zoo或者是spring gateway那现在因为zoo不再维护所以我们现在学的都是spring gateway来代替这个网关然后接着再进行一个负载均衡ribbon负载均衡就是从
[02:52] 要用到的这个服务的地址中选择一个地址去调用那这个地址是怎么来的从我们的服务注册中心获取对应服务的地址列表从地址列表中选择一个地址去访问那这个选择呢是基于负载均衡算法去选择之后当如果是服务之间要相互调用的话可以通过我们的FAN去调用如果是服务的配置有改变那么我们可以通过配置中心服务器
[03:21] 统一实时的去改变所有微服务的那些配置项ok接下来我们再去了解spin cloud的一个版本信息spin cloud不是一个组件而是有许多组件的集合前面大家已经见到了这些都是spin cloud里面集成的一些组件好所以它不是只有一个组件然后它的版本的话呢命名比较特殊是以英文单词来命名的就不再是数字那它其实这个单词
[03:52] 命名方式呢是以伦敦的地铁站的名字来命名那我们打开它官网也了解得到我们打开来它版本信息在这一边现在最新版本的是Huston但是它不是稳定版那最新稳定版本是Greenwich或是叫Greenwich格林威治SRE这是稳定版本OK那正确读法呢是Greenwich那我们的读法读中文也行
[04:20] 读成格林威治也都是可以的OK那这个版本信息大概大家了解一下就可以了我们再回到我们的笔记中来去记录一下刚才spin cloud概述中的一些内容那它的组件整合的有哪一些整合的组件包括呢有可以有很多组件常见的组件有
[04:59] Urica注册中心Gateway网关Ribbon负载均衡还有是我们的Fan服务调用之后呢还有High Street是我们的熔断器OK这些组件是我们用Spring Cloud的话常见到的一些组件那怎么使用呢在有需要的时候项目中添加
[05:48] 对应的启动器依赖即可好那它的版本有什么特征版本特征就是以英文单词命名比较特别然后呢这个英文单词一般是来自我们的伦敦地铁站名OK这就是它的一个版本的命名这个特征这也是我们Spring Cloud概述部分的内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
介绍 Spring Cloud 的基本概念、核心组件、版本体系及其在微服务架构中的作用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 内容：PPT 页面标题为“4. 初识Spring Cloud”，内容介绍微服务架构需要技术架构支持，Spring Cloud 是主流选择。
- 画面序号：1

画面 2:
- 内容：PPT 页面继续展示“4.1. 简介”，列出 Spring Cloud 的优势：后台强大、技术强、基础好、使用方便，并展示其官网地址。
- 画面序号：2

画面 3:
- 内容：浏览器页面显示 Spring Cloud 官网的“Overview”部分，介绍其提供分布式系统常见模式的工具。
- 画面序号：3

画面 4:
- 内容：浏览器页面切换到“Samples”部分，列出可尝试的示例，如 Config Server、Service Registry、Circuit Breaker Dashboard 等。
- 画面序号：4

画面 5:
- 内容：浏览器页面回到“Overview”部分，展示 Spring Cloud 的功能描述。
- 画面序号：5

画面 6:
- 内容：PPT 页面展示“4.1. 简介”，列出 Spring Cloud 的主要组件：Eureka、Zuul、Ribbon、Feign、Hystrix。
- 画面序号：6

画面 7:
- 内容：PPT 页面展示“4.1. 简介”，列出 Spring Cloud 的主要组件：Eureka、Zuul、Ribbon、Feign、Hystrix。
- 画面序号：7

画面 8:
- 内容：PPT 页面展示 Spring Cloud 架构图，包含 Request → Zuul → Ribbon → Service A/B/C → Eureka Server → Config Server。
- 画面序号：8

画面 9:
- 内容：PPT 页面展示“4.2. 版本”，介绍 Spring Cloud 是组件集合，版本命名规则。
- 画面序号：9

画面 10:
- 内容：PPT 页面展示 Spring Cloud 架构图，包含 Request → Zuul → Ribbon → Service A/B/C → Eureka Server → Config Server。
- 画面序号：10

画面 11:
- 内容：PPT 页面展示“4.2. 版本”，列出 Spring Cloud 的版本：Hoxton SNAPSHOT、Greenwich SR1 GA、Greenwich SNAPSHOT、Finchley SR3 GA。
- 画面序号：11

画面 12:
- 内容：浏览器页面显示 Spring Cloud 官网的“Learn”部分，列出各版本的文档链接。
- 画面序号：12

画面 13:
- 内容：IDE（Typora）页面展示代码片段，使用 restTemplate 进行 HTTP 请求。
- 画面序号：13

画面 14:
- 内容：IDE（Typora）页面展示代码片段，使用 restTemplate 进行 HTTP 请求。
- 画面序号：14

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 13 和 14:
```java
public void test(){
    String url = "http://localhost/user/8";
    //restTemplate可以对json格式字符串进行反序列化
    User user = restTemplate.getObject(url, User.class);
    System.out.println(user);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8:
- 架构图结构：
  - Request → Zuul
  - Zuul → Ribbon (多个)
  - Ribbon → Service A (多个)
  - Ribbon → Service B (多个)
  - Ribbon → Service C (多个)
  - Service A/B/C → Eureka Server (双向箭头)
  - Service A/B/C → Config Server (双向箭头)
  - Git → Config Server (双向箭头)

画面 11:
- 表格数据：
  - Hoxton SNAPSHOT
  - Greenwich SR1 GA
  - Greenwich SNAPSHOT
  - Finchley SR3 GA

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

