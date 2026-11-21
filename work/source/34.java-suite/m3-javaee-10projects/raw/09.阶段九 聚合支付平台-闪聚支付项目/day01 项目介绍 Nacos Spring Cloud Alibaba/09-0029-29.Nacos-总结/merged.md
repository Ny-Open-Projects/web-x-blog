# 29.Nacos-总结

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\29.Nacos-总结【海量资源尽在 666java.com】.mp4
- 时长 4分23秒（音频 263s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们来总结一下Nexos服务发现和配置管理Nexos是用来干什么的呢这里边列了一些问题来看一下Nexos是阿里巴巴公司开源的一个项目它主要用来实现配置中心和服务注册中心什么是服务发现因为我们说Nexos主要实现两部分的功能一个是服务发现一个是配置管理什么是服务发现呢
[00:25] 我们知道在微服务架构当中一个业务流程需要多个微服务通过网络接口进行远程调用来完成那么服务的消费方要通过服务注册中心来获取服务提供方的地址从而进行远程调用这个过程就是服务发现具体服务发现的流程又是什么呢首先服务发现它有一个客户端从服务注册中心来获取服务列表
[00:50] 这个客户端是不是就是我们在这个我们的POM文件里面所配置的这个依赖了你看一个是叫做Nexus Discovery这是不是就是服务发现的客户端呢那么这个客户端呢就是从服务注册中心来拿到服务列表然后呢根据客户端负载均衡的这个算法然后呢获取服务实力的地址来进行远程调用其实服务发现就干这两件事啊另外还有配置中心配置中心是什么呢
[01:17] 在微服务架构当中很多微服务的配置文件我们都通过配置中心进行统一管理它的流程是什么首先发布配置将配置信息发布到配置中心Nexus就是我们的配置中心你在配置列表当中会看到有很多的配置文件对吧这就是我们将配置发布到配置中心那么具体微服务它就会从Nexus来获取配置
[01:44] 当配置文件更改它就得到通知然后自动从配置文件获取配置其实这里边也有一个客户端就是配置中心的客户端就是NetClose Configure这是它的配置中心的客户端它来获取配置Spring Cloud是什么呢因为我们项目是采用Spring Cloud阿里巴巴这个框架来进行开发的这里边我们要知道Spring Cloud和Spring Cloud阿里巴巴是什么Spring Cloud是一套微服务的开发框架集合
[02:15] 它是一套什么微服务开发的标准它集成了很多优秀的开源框架比如非常有名的Netflix公司对吧这个后期大家学习Spring Cloud的时候会去了解这个公司的很多开源项目那么Spring Cloud的阿里巴巴它和Netflix是差不多的它也是基于Spring Cloud的标准实现了一套微服务开发框架的集合那么我们用Spring Cloud的阿里巴巴这个框架具体怎么用呢我们是采用Double服务
[02:45] 这种架构来进行开发那double服务的架构当初我们讲过整个的架构图大家看是不是这样的在应用层对外暴露RESTful接口供客户端调用那么微服务层暴露double协议的接口供应用层调用这就是double服务架构它的一个简略图吧然后呢继续往后看那么double服务开发的流程呢
[03:15] 就是现在我们要开发一个微服务暴露double服务接口首先我们定义两个子工程一个API一个API实现工程对吧那这个API工程里面是不是就存放的接口为了方便其他服务调用其他服务是不是可以引用这个API工程的jar 包然后调用它的接口API实现功能就是接口的实现类注意接口实现类上边我们要用这个注解去标记这个注解会被double框架扫描到最终
[03:44] 将Service接口实现的方法呢就暴露成网络接口那供远程调用那么如果我们要消费这个double服务的接口怎么办呢就在首先引入API工程就是引入接口其次我们要使用这个reference这个注解然后这个注解呢就可以将接口生成代理对象实现double服务的远程调用以上呢就是我们NetClose服务发现配置管理的
[04:14] 重要内容我们希望你通过问题的方式能够自己理解自己表达出来好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud 项目中集成 Nacos 作为服务发现与配置中心，并展示其在 Dubbo 服务架构中的应用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 IDEA 中的项目结构，重点是 `bootstrap.yml` 配置文件，其中配置了 Nacos 的服务发现和配置中心地址。
画面2：展示 `pom.xml` 文件，添加了 Spring Cloud Alibaba 的 Nacos Discovery 和 Nacos Config 依赖。
画面3：展示 PPT 内容，介绍 Nacos 作为配置中心和注册中心的作用。
画面4：展示浏览器访问 Nacos 配置中心的 URL，页面显示“application1 config|zhengzhou”。
画面5：展示 Nacos 控制台界面，列出已配置的配置文件，如 `Nacos-RESTful-consumer.yaml` 和 `ext-config` 系列文件。
画面6：展示 PPT 内容，解释服务发现的流程。
画面7：展示 PPT 内容，介绍配置中心的作用和应用流程。
画面8：展示 PPT 内容，介绍 Spring Cloud 和 Spring Cloud Alibaba。
画面9：展示 PPT 内容，介绍 Dubbo 服务开发流程。
画面10：展示 Nacos 配置中心的发布配置界面，配置格式为 YAML，内容包含 HTTP 相关的编码设置。
画面11：展示 PPT 内容，介绍服务发现的流程。
画面12：展示 PPT 内容，介绍配置中心的作用和应用流程。
画面13：展示 PPT 内容，介绍 Dubbo 服务开发流程，包括定义 API 工程、实现工程和消费方开发。
画面14：展示 PPT 内容，介绍 Nacos 作为配置中心和注册中心的作用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```yaml
name: Nacos-RESTful-consumer #服务名
cloud:
  discovery:
    server-addr: 127.0.0.1:8848 #服务发现中心地址
    namespace: fbee3c14905-0c0d-9654-8c8d4f34jabb #指定命名空间的id
    config:
      server-addr: 127.0.0.1:8848 #配置中心地址
      file-extension: yaml #配置文件的后缀名，配置文件名根据application.name+后缀名
      ext-config[0]:
        data-id: ext-config:common0.yaml
        group: COMMON_GROUP
        refresh: true
      ext-config[1]:
        data-id: ext-config:common2.yaml
        group: COMMON_GROUP
        refresh: true
      ext-config[2]:
        data-id: ext-config:common3.yaml
        group: COMMON_GROUP
        refresh: true
```

画面2：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-Nacos-discovery</artifactId>
</dependency>
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-Nacos-config</artifactId>
</dependency>
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-dubbo</artifactId>
</dependency>
```

画面10：
```yaml
#HTTP请求配置
spring:
  http:
    encoding:
      charset: UTF-8
      force: true
      enabled: true
    messages:
      encoding: UTF-8
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：Nacos 控制台界面，左侧菜单栏包含“配置管理”、“服务列表”、“服务管理”等选项。右侧显示配置文件列表，包括 `Nacos-RESTful-consumer.yaml`、`ext-config:common0.yaml`、`ext-config:common2.yaml`、`ext-config:http.yaml`，它们的 Group 分别为 `DEFAULT_GROUP` 和 `COMMON_GROUP`。

画面10：展示 Dubbo 服务架构图，结构如下：
- 客户端（HTTP） → API 网关（Zuul） → 服务注册发现（Nacos Server） → Service-1（Dubbo） → Service-2（Dubbo）
- 组件说明：客户端（前端或外部系统） → API 网关（Zuul） → 服务注册发现（Nacos Server） → Service-1（Dubbo） → Service-2（Dubbo）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

