# 15.Nacos-服务发现-RESTful服务发现-服务注册

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\15.Nacos-服务发现-RESTful服务发现-服务注册【海量资源尽在 666java.com】.mp4
- 时长 7分15秒（音频 435s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们就来实现RESTful服务发现整个过程那么在当初我们学习服务发现流程的时候我们知道它有三点第一点呢是微服务向服务发现中心进行注册上报自己的地址第二点就是微服务去注册就是服务发现中心去发现提供方的地址所以其实它应该说分成两部分第一部分是注册第二部分是发现
[00:30] 所以大家来看那接下来我们要学习REST服务发现整个过程呢我们会分服务注册啊以及服务发现啊这两个比较核心的东西呢来讲解好服务注册呢就是每个微服务呢把自己的地址注册到服务发现中心那服务发现呢就是微服务呢从服务发现中心获取对方的地址进行调用好那么服务注册我们来看一下
[00:56] 那现在我们是基于REST服务的这种服务发现其实在当初啊我们去写的这个当时为了去给大家讲服务发现流程的时候我们是不是写了两个微服务一个是provider一个是consumer并且provider它是对外提供的是不是就是REST服务的这个服务接口啊所以其实我们可以对原来的我们这个程序呢进行一个什么进行一个改造对吧好那么各位我们在进行改造之前呢
[01:25] 我把这段代码呢给大家保留一下啊这段代码给大家保留一下保留之后呢回头你可以针对我们这个入门程序呢可以去回头练习一下其实这段代码呢来我给大家保存一下这段代码将来我放到咱们这个资料文件夹啊它其实就是我们说的服务发现的一个流程的一个测试对吧好那么接下来我要做的就是在基于刚才我们这套环境当中啊准备呢
[01:55] 去采用Spring Cloud的阿里巴巴来完成REST复的服务发现原来我们其实这个是通过配置文件的方式来配置对方的地址当初大家应该还有印象对吧那现在我们要做的是不是就是智能的方式来进行复发现对那怎么做呢看好首先因为我们说Spring Cloud的阿里巴巴是基于Spring Cloud对吧并且还要引入Spring Cloud的阿里巴巴的依赖所以我们需要在复工程当中
[02:25] 把我们说的SpinCloud以及SpinCloud Alibaba这个依赖把它加进去好那么我们把这个依赖加进去之后呢那接下来我们要做什么事啊仍然我们先做提供方再做消费方那么这个提供方要做的事是不是就是将自己的网络地址注册到服务发现中心对吧那注册服务发现中心怎么注册
[02:52] 通过前面的流程学习我们知道它是不是要通过一个服务发现的客户端所以这个客户端是一个通用的东西每个微服务都需要所以这里边我们只需要引入这条框架给我们提供的什么提供的依赖就可以了所以我们在哪里在我们的服务提供方这里我们在POM文件当中我们把这个依赖
[03:18] 这个依赖挺长的叫Spring Cloud的Data Alibaba Necros Discovery这个其实就是我们说的什么服务发现的客户端这个服务发现的客户端它的功能是什么呢第一将自己将自己就是他自己所处的一个微服务把它注册到就将自己的地址注册到哪里服务发现中心对第二个它的功能是从
[03:51] 服务发现中心来获取服务列表其实它是两个功能那么好那你要把这个依赖引进去之后其实它现在这个客户端你就可以去用了那有时候老师那咋用因为你只要引进去它就可以自己把自己注册到服务发现中心了但是你要让它注册你是不是得告诉它你向哪个服务发现中心去注册所以你是不是需要配置一下
[04:20] 你的这个服务发现中心的地址啊对所以呢怎么配呢那所以其实在我们说的这个Spring的这个标签下边呢我们去配置一下注意整个的这个配置文件的过程我给大家强调一下大家不用去根据我的讲义里面去手动的去敲啊比如说这里边呢我们去Spring你看这里边是不是很多配置你看见吗对那我建议你不要去敲为什么因为你可能敲错所以我建议你复制
[04:49] OK那么你复制我讲义上的配置呢把它粘进去但是你要能排错啊比如说我讲义里边或者说你复制的时候出错了比如说这里弄错了那你得知道你怎么排你看见吗空一格那么哎它是这种yml的这种文件格式好那现在呢我们来看我们呢就把这个配置拿过来了这个名称是不是就是我们的工程名啊其实这个名称啊你注意这个名称
[05:16] 将来我们注册到服务发现中心这就是我们的服务名对那这个不用说了你向哪注册吗对你是不是要向服务发现中心注册所以那就是服务发现中心的地址通过这个配置其实很简单大家应该知道把哪一个服务注册到哪一个服务发现中心对吧好了那现在你把这个配上去呢其实就已经OK了有时候老是这么简单吧
[05:44] OK那来我们来看一下你只需要把Provider重启重启了之后呢它就会把自己呢注册到服务发现中心当初我们是不是已经把Nexus安装好了对不对所以这个时候我们打开Nexus然后呢我们找到服务列表大家可以看到其实在这个服务列表这这是不是就是一个服务名
[06:07] 对这个服务名你告诉我是不是和我们刚才配置的这个nexos rest4-provider是不是一致另外通过这个服务列表呢你会看见它是不是有一个实例数看见吗当前我是不是只起了一个进程就是provider所以它的实例数是几是1点开详情我们可以看到上面的服务名就是和我们的这个配置的这个sbring application内幕的这个服务名一致
[06:37] 就说明把自己的这个服务名注册到服务注册中心了这个分组呢回头我再说我在详细讲的时候再说先不要管它下边我们这个端口是不是56010啊56010是不是就是我们指定的一个服务的端口可以吗对所以通过这个详细信息很清楚知道这个服务的具体情况它的健康状态是处表示还健康还活着是吧好那各位到这儿我们是不是就完成了服务的注册这是我们整个服务发现的第一部分服务注册
[07:08] 那服务注册成功了之后是不是才可以服务发现好那服务注册我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Nacos 服务注册中心中，配置并启动一个基于 Spring Cloud Alibaba 的 RESTful 服务提供者和消费者，实现服务注册与发现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档目录，当前章节为“2.3 RESTful服务发现”，并聚焦于“2.3.1 测试环境”，介绍 Spring Cloud Alibaba 作为测试环境。
画面 2: 文档目录中高亮“2.3.2 服务注册”，并展示服务消费者配置文件中 Nacos 服务发现的配置。
画面 3: 在 IntelliJ IDEA 中打开 `RestConsumerController.java`，展示消费者服务中使用 `RestTemplate` 调用服务的代码。
画面 4: 展示 Windows 资源管理器，路径为 `course-pa.../Nacos`，显示 `Nacos` 文件夹。
画面 5: 文档目录中高亮“2.3.1 测试环境”，并展示在 `Nacos-discovery` 工程中添加依赖的 Maven 配置片段。
画面 6: 展示 `pom.xml` 文件中添加 Spring Cloud Alibaba 依赖的配置，版本为 `2.1.0.RELEASE`。
画面 7: 展示 `pom.xml` 文件中 Spring Cloud Alibaba 依赖的配置，版本为 `2.1.0.RELEASE`。
画面 8: 展示 Nacos 控制台，服务名称为 `Nacos-RESTful-provider`，服务实例数为 1，并解释服务名称和实例的概念。
画面 9: 在 IntelliJ IDEA 中打开 `application.yml` 文件，展示 `Nacos-RESTful-provider` 服务的依赖配置，包含 `spring-cloud-starter-alibaba-Nacos-discovery`。
画面 10: 在 IntelliJ IDEA 中打开 `application.yml` 文件，展示 `server.port` 配置为 `56010`。
画面 11: 在 IntelliJ IDEA 中打开 `application.yml` 文件，展示 `spring.cloud.Nacos.discovery.server-addr` 配置为 `127.0.0.1:8848`。
画面 12: 在 IntelliJ IDEA 中，`application.yml` 文件配置完成，点击运行后，控制台显示服务启动日志，服务名为 `Nacos-RESTful-provider`。
画面 13: 屏幕空白，无内容。
画面 14: 文档目录中高亮“2.3.2 服务注册”，并展示服务提供者配置文件中 Nacos 服务发现的配置，以及 Nacos 控制台显示服务已注册成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
服务消费：
spring:
  application:
    name: Nacos-RESTful-consumer
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8848
```

画面 5:
```
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-dependencies</artifactId>
      <version>2.1.3.RELEASE</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-dependencies</artifactId>
      <version>Greenwich.RELEASE</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
    <dependency>
      <groupId>com.alibaba.cloud</groupId>
      <artifactId>spring-cloud-alibaba-dependencies</artifactId>
      <version>2.1.0.RELEASE</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

画面 6:
```
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-dependencies</artifactId>
  <version>Greenwich.RELEASE</version>
  <type>pom</type>
  <scope>import</scope>
</dependency>
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-alibaba-dependencies</artifactId>
  <version>2.1.0.RELEASE</version>
  <type>pom</type>
  <scope>import</scope>
</dependency>
```

画面 9:
```
modelVersion>4.0.0</modelVersion>
<artifactId>Nacos-RESTful-provider</artifactId>
<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  <dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-Nacos-discovery</artifactId>
  </dependency>
</dependencies>
```

画面 10:
```
server:
  port: 56010
```

画面 11:
```
server:
  port: 56010
spring:
  application:
    name: Nacos-RESTful-provider #服务名
  cloud:
    Nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8: PPT 标题为“2.3.3 服务发现”，下方有文字说明“服务名称：每个服务在服务注册中心的标识，相当于java中的类名。服务实例：网络中提供服务的实例，具有IP和端口，相当于java中的对象，一个实例即为运行在服务器上的一个进程。”
画面 14: PPT 标题为“2.3.2 服务注册”，下方有文字说明“在服务提供工程中配置Nacos服务发现相关的配置：服务提供：”，并展示配置内容，以及 Nacos 控制台显示服务已注册成功。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

