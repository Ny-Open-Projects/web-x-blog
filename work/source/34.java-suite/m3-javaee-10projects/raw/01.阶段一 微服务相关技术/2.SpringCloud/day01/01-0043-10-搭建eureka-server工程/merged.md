# 10-搭建eureka-server工程

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\10-搭建eureka-server工程_【海量资源尽在 ubkz.com】.mp4
- 时长 9分33秒（音频 573s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 搭建Eureka-Server工程在这一小节中我们的主要目标是添加Eureka对应依赖和编写引导类搭建Eureka服务并可访问Eureka服务界面那Eureka呢我们知道它是服务注册中心只做服务注册自身并不提供服务也不消费服务好我们可以
[00:33] 搭建web工程使用Urica也就是说Urica是一个web服务器可以使用Springboard方式搭建那我们来分析具体的搭建步骤一创建工程创建后接下来添加启动器依赖这个启动器依赖加的是Urica服务相关的启动器依赖
[01:04] 加完后呢接下来我们去编写启动引导类和配置文件那这一步呢我们可以通过插件去生成只是要注意在生成以后这个启动引导类上面呢我们要去添加Urica的服务注解标注它是一个Urica服务接着我们再去修改配置文件可以修改web服务器的端口应用名称
[01:38] 还有其他的好之后我们再去启动测试如果是搭建成功的话我们可以通过访问Ureka服务的一个地址查看到服务界面OK这就是我们的分析接下来我们打开IDA按照分析去搭建Ureka-server工程创建New Module下一步工程名Ureka-serverFinish
[02:14] 添加Elai那这个Elai呢名称比较长我们可以从讲义中复制过来打开讲义回到我们的开发工具中我们加了Elai呢是这么个Elai好它的坐标点Spring里面的一个Cloud包里边然后呢我们的Elai名称叫做Spring-Cloud-Starter-Netflix-Eureka Server它是由Netflix这家公司开发的一个注册中心
[02:48] 然后这个Netflix是美国的一个视频网站好那我们的版本号其实是可以不用加的因为我们在复工程中已经引入了也就是这一个spring-cloud-dependencies这边已经对spring-cloud中那些组件的版本进行了一个锁定好那我们这边就可以不用加启动器加入以后接下来我们去生成具体的启动引导类和
[03:22] 配置文件右击名称com.it黑马点Urica ServerApplication配置文件要生成点击OK好然后不要忘了在生成的启动引导类上面我们说过要去添加一个Urica Server的注解叫做EnableUrica ServerOK这个注解这个注解的意思是声明当前
[03:55] 应用是Urica好服务启动引导内容改造完以后接着我们打开配置文件去添加一些配置项配置项我们可以加比如说服务的端口我们可以设置为10086然后接着我们再去设置这一个应用的名称spring.application.name这个的名称我们可以设置Urica-server
[04:31] 好那这个应用名称以后如果是其他服务注册到Urica的时候呢它会显示这个服务的名称即使是Urica自己如果以后有集群那么也可以显示这个应用的名称所以我们起一个这样的名称然后呢接着我们去设置Urica的一些其他参数Urica.clan再去设置它的一个Service-url
[05:02] 里面我们设置它的一个服务地址default zoom它的地址是当前这一台机器127.0.0.110086urica好这个是什么意思这个意思就是urica服务地址服务地址如果是集群的话需要指定其他
[05:40] 集群Urica地址好那现在呢因为是Urica只有一台没有做集群所以指定的是本身的Urica服务地址OK那这个地址呢后续要给其他的服务去注册的地址还有是从这一边去获取到具体服务名的一个地址好所以这是我们的一个地址的指定完了后呢接下来我们再去设置它的一些另外参数比如说
[06:15] 要不要去把自己注册到Ureca中Registry with Ureca默认是true我们改成false意思就是因为前面分析的时候跟大家说过Ureca自身不提供服务所以呢它不注册不注册自己到Ureca中那如果以后是集群当然要注册因为其他的服务器也要发现这一台Ureca还有一个是要不要去获取
[06:48] 具体的服务也是不需要的默认它是出那我们这边是不拉取服务OK这就是我们的参数配置配置完成完成以后呢接着我们去启动验证看一下我们的Urica能不能去正常的被访问到好启动启动以后呢成功的标准就是我们访问一个地址可以查看到Urica服务界面我们看它正在启动中好启动以后呢看到它这边
[07:26] 10086没有问题这个端口然后接着我们在这边是看到它的一个项目的路径是空的也就是说直接访问10086就可以了现在我们打开浏览器去访问127.0.0.110086回车我们就见到了这个Urica的服务界面上面说了一些概述一个环境是测试环境然后接着它的一个时间
[07:58] 还有呢就是我们的一个地址还有就是上面注册的服务现在是没有的这个是服务的名称后续我们如果在这个地方其他提供服务的应用中设置了一个application.name如果设置了这个名称就会显示在这一边OK然后接下来下面是JVN的一些参数好这就是我们的一个Eureka注册中心
[08:27] 它的一个搭建我们就已经搭建完成回到讲义中来进行回到我们的笔记中我们小结一下那刚才我们搭建的时候呢去做的事情一般的项目搭建都有做也没有什么太特殊的就是我们的启动器依赖给大家列出来还有就是我们的配置文件这样的话大家自己做的时候会更加好复制一些好参考一些OK我们把它从开发工具中给拿过来
[09:03] E-Lite的话呢我们加了一个是Netflix也就是网飞耐飞也有叫网飞也有叫耐飞的然后接着呢把这个E-Lite加入到我们的笔记中还有是配置文件配置文件的话呢是我们刚才的这一段配置把它拿过来OK这就是我们Eureka钢伺服工程的搭建全部完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
搭建并运行一个基于 Spring Cloud 的 Eureka 服务注册中心（Eureka-server），并演示其服务注册与发现功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：PPT 页面，标题为“10. 搭建Eureka-server工程”，下方有“目标”、“分析”、“小结”等部分。
- 重点文字：
  目标：添加Eureka对应依赖和编写引导类搭建Eureka服务并可访问Eureka服务界面
  分析：
  Eureka是服务注册中心，只做服务注册；自身并不提供服务也不消费服务。可以搭建web工程使用Eureka，可以使用Spring Boot方式搭建。
  小结：
  11. 服务注册与发现
  目标：将user-Service的服务注册到Eureka并在consumer-demo中可以根据服务名称调用

画面 2：
- 内容：IDEA 中的 Maven 依赖管理界面，正在添加 Spring Cloud 依赖。
- 重点文字：
  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-dependencies</artifactId>
        <version>${spring-cloud.version}</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>

画面 3：
- 内容：IDEA 中的 pom.xml 文件，展示 Eureka Server 的依赖配置。
- 重点文字：
  <groupId>com.ithema</groupId>
  <version>1.0-SNAPSHOT</version>
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.0.RELEASE</version>
  </parent>
  <artifactId>Eureka-server</artifactId>
  <dependencies>
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-starter-netflix-Eureka-server</artifactId>
    </dependency>
  </dependencies>

画面 4：
- 内容：IDEA 中的 pom.xml 文件，展示 Spring Cloud 的版本管理配置。
- 重点文字：
  <properties>
    <java.version>1.8</java.version>
    <spring-cloud.version>Finchley.SR1</spring-cloud.version>
    <mybatis.version>1.3.2</mybatis.version>
    <mysql.version>8.0.11</mysql.version>
  </properties>

画面 5：
- 内容：IDEA 中的 EurekaServerApplication.java 启动类文件。
- 重点文字：
  package com.ithema;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.cloud.netflix.Eureka.EnableEurekaServer;
  @EnableEurekaServer
  @SpringBootApplication
  public class EurekaServerApplication {
      public static void main(String[] args) {
          SpringApplication.run(EurekaServerApplication.class, args);
      }
  }

画面 6：
- 内容：IDEA 中的 application.yml 配置文件，设置 Eureka 服务端口和名称。
- 重点文字：
  server:
    port: 10086
  spring:
    application:
      name: Eureka-server
  Eureka:
    instance:
      environment: test
    client:
      register-with-Eureka: false
      fetch-registry: false

画面 7：
- 内容：IDEA 项目结构视图，显示了多个模块，如 consumer-demo、user-Service、Eureka-server。
- 重点文字：
  项目结构中包含：
  - heima-Spring Cloud
  - consumer-demo
  - Eureka-server
  - user-Service
  - http-demo

画面 8：
- 内容：IDEA 中的 EurekaServerApplication.java 文件，右键菜单弹出，选择“Run 'EurekaServerApplication'”。
- 重点文字：
  无代码或配置，仅是右键菜单操作。

画面 9：
- 内容：IDEA 控制台输出，显示 Eureka Server 成功启动。
- 重点文字：
  Application Context: initialization completed in 1078 ms
  ...
  Eureka Server started.
  ...
  http://127.0.0.1:10086/Eureka/

画面 10：
- 内容：浏览器访问 Eureka Server 的管理页面，显示“System Status”和“DS Replicas”。
- 重点文字：
  System Status:
  Environment: test
  Data center: default
  Current time: 2019-06-14T13:47:34.747+08:00
  Uptime: 00:00
  Lease expiration enabled: false
  Renew threshold: 1
  Renew (last min): 0
  DS Replicas:
  127.0.0.1

画面 11：
- 内容：浏览器访问 Eureka Server 的管理页面，显示“Instance Info”。
- 重点文字：
  Instance Info:
  Name: 192.168.174.1
  Status: UP

画面 12：
- 内容：PPT 页面，标题为“10. 搭建Eureka-server工程”，下方有“搭建步骤”。
- 重点文字：
  搭建步骤：
  1. 创建工程；
  2. 添加启动依赖；
  3. 编写启动引导类（添加Eureka的服务注解）和配置文件；
  4. 修改配置文件（端口、应用名称...）；
  5. 启动测试
  小结：
  - 启动器依赖
  - 配置文件

画面 13：
- 内容：IDEA 中的 application.yml 配置文件，展示 Eureka Server 的配置。
- 重点文字：
  <Xml version="1.0" encoding="UTF-8">
  <project xmlns="http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.1.0.RELEASE</version>
    </parent>
    <artifactId>Eureka-server</artifactId>
    <dependencies>
      <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-Eureka-server</artifactId>
      </dependency>
    </dependencies>
  </project>

画面 14：
- 内容：PPT 页面，标题为“11. 服务注册与发现”，下方有“目标”。
- 重点文字：
  目标：将user-Service的服务注册到Eureka并在consumer-demo中可以根据服务名称调用

