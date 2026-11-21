# 13-获取配置中心配置

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\13-获取配置中心配置_【海量资源尽在 ubkz.com】.mp4
- 时长 9分26秒（音频 567s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 获取配置中心配置在这一小节中我们的主要目标是改造用户微服务user-Service配置文件信息不再有微服务项目提供而是从配置中心获取那具体的需求呢就是在我们搭建好了配置中心之后希望可以将服务的提供工程user-Service的application.yml配置文件删除
[00:30] 修改为从配置中心也就是我们刚才搭建的config-server中获取那如何做到这么一个需求我们的实现步骤我们来分析一你要应用从配置中心获取这个配置文件的内容的话那么我们要去添加对应的配置启动其依赖加了以后我们要去修改配置文件也就是
[01:00] 要将这个文件删除并且我们还要加一个文件那之后我们再来说明之后呢再去启动测试验证我们这个服务提供工程原来提供的服务呢可以用到现在改了这种配置读取的方式以后依然是可以使用的那么说明我们的配置就是成功没有问题的接下来我们按照分析去实现打开IDA添加依赖我们要加一个依赖是spin-cloud-starter
[01:32] -config就它好版本号这个也得加一下加了以后呢接下来因为我们前面呢是没有呃这边配置这个config的启动器依赖的好所以这个可以加加了以后呢接下来我们在复工程里面我们看下有没有指定这边没有指定版本号好所以我们指定这个2011的哈好之后呢接着我们再去删除这个配置点把原来的这个配置点给删除删了以后呢我们再去
[02:02] 造一个配准件这个文件的也是spinbook工程中默认的配准件叫做bootstrap.yml这个配准件里面的我们加的内容是可以配置配置中心工程的一些参数我们的配置文件是哪一个一定要注意我们配置文件不是读取配置中心这个工程的这一个配准件不是他读取的是你自己指定的还就是
[02:31] 可以在这边去配置Urica的一些信息那这个文件一般情况下能配置的是我们这一个工程里面比较固定化的信息如果是比较变动的那么我们还是到application中去配置但是application因为我们说过了是集中去配置的如果你真的要配那应该是在我的仓库中去配置那些配置项现在已经不在工程里面配置了好所以我们这边可以去配置的东西有config.name这个名称我们可以指定一下
[03:01] 我们叫user还有配置一个profile这个叫dev这两个信息是当时我们在仓库中创建的那个user-dev的内容这个是要与仓库中的配置文件的application保持一致那这一个呢要跟profile保持一致具体这两个当时我们在
[03:39] 说的时候说这个配置文件的时候呢已经给他提过就是我们的配置文件呢他是有个格式的格式就是前面的是application后面是profile所以你现在指定的要跟曾经我们创建的配置文件要保持一致好回来回到我们的开发工具中继续配置他那这个文件呢有很多版本到底用的是哪一个版本的哪一个分支的好我们只有一个分支叫master分支要与仓库中的配置
[04:13] 文件所属的版本或是分支一样保持一致那我们打开马云来看当时我们创建这个文件的时候呢所属的分支是master好所以我们写的就是这个masterok你再回到开发工具中继续来去配置那允许使用配置中心你才能够去应用它所以我们这边要去配置一个叫做发现配置中心this
[04:46] GavelryUnable它默认是False我们改成True之后呢再来去指定我们的配置中心我们当时起了个名称叫ConfigurantServer这个的意思是使用配置中心那下面这个就是我们注册在Eureka中的配置中心的服务名那既然你用到了Eureka所以你要指定Eureka的信息我们的Eureka在这一个地方
[05:41] 好就已经全部配置完成完成以后呢接下来大家已经看到我们这边是没有当初的application.yml配置文件的那如果这时候还可以去访问到我们曾经的服务的话说明我们的配置是能够读取到而且是没有问题的我们来去启动9091它在启动过程中其实我们也可以去看这个启动情况除此以外它已经发现到我们的配置中心服务器是
[06:19] 一万两千了好读取到后接着我们去访问一下我们原来的服务我们的服务呢原来是90919091user8回车一样没有问题说明我们的配置从配置中心中获取到是完全没有问题的现在它依然可以去加载到我们比如说数据库的配置信息还有是一些其他的比如说Urica的还有是一些项目的名称还有端口号
[06:54] 那我们现在访问的依然还是9091完全不受到任何影响也就是说读取到了OK这就是我们关于从配置中心获取配置的一个内容我们回到笔记中来进行小结要去获取配置中心的配置的话呢要将原来的将原来的application.yml删除然后添加一个配置文件叫做
[07:27] bootstrap.yml配置文件该文件也是SpringBowl的配置默认配置文件其内容经常配置一些项目中固定的配置参数配置项如果是项目经常
[08:09] 变动的应该配置到application.yml中现在使用了配置中心则应该配置到git仓库中对应的配置文件好那我们刚才做了这个以后呢把配置文件也拿过来还有依赖具体的
[09:03] 依赖的话我们当时加了一个依赖当然在我们讲义中也有只是怕大家复制的时候格式又有问题配置文件是它我们粘过来这就是我们获取配置中心配置的所有内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何将 Spring Cloud 服务的配置文件从本地修改为从配置中心（如 Git 仓库）动态获取，并展示相关配置文件的修改和启动过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示课程 PPT 页面，标题为“13. 获取配置中心配置”，内容包括目标、分析、需求和实现步骤。其中提到“将服务提供工程 user-Service 的 application.yml 配置文件删除，修改为从配置中心 config server 中获取”。
画面 2: 在 IntelliJ IDEA 中，展示 user-Service 项目的 pom.xml 文件，其中已添加 spring-cloud-starter-config 依赖。
画面 3: 在 IntelliJ IDEA 中，展示 config-server 项目的 pom.xml 文件，其中包含 spring-cloud-starter-config 依赖。
画面 4: 在 IntelliJ IDEA 中，右键点击项目目录，弹出“New”菜单，准备创建新文件。
画面 5: 在 IntelliJ IDEA 中，打开并编辑 bootstrap.yml 文件，其中包含 spring.cloud.config.label、spring.cloud.config.profile 等配置项。
画面 6: 在浏览器中访问 http://127.0.0.1:10000/user-dev.yml，显示了从配置中心获取的配置内容。
画面 7: 在 IntelliJ IDEA 中，运行 user-Service 项目，控制台输出显示服务启动成功，并包含 Eureka 和 Config Server 的初始化信息。
画面 8: 在 IntelliJ IDEA 中，控制台输出显示服务正在从配置中心（http://localhost:12000）获取配置。
画面 9: 在浏览器中，地址栏输入 http://127.0.0.1:10000/api/user/8，准备访问服务。
画面 10: 显示课程 PPT 页面，标题为“13. 获取配置中心配置”，内容包括目标、分析、需求和实现步骤。
画面 11: 显示课程 PPT 页面，标题为“13. 获取配置中心配置”，内容包括目标、分析、需求和实现步骤。其中“小结”部分提到“将原来的 application.yml 删除；然后添加 bootstrap.yml 配置文件，该文件也是 Spring Boot 的默认配置文件，其内会经常配置一些项目中固定的配置项。如果是项目经常变动的应该配置到 application.yml 中，现在使用了配置中心就应该配置到 Git 仓库中对应的配置文件。”
画面 12: 在 IntelliJ IDEA 中，运行 user-Service 项目，控制台输出显示服务启动成功，并包含 Eureka 和 Config Server 的初始化信息。
画面 13: 在 IntelliJ IDEA 中，编辑 bootstrap.yml 文件，其中包含 spring.cloud.config.label、spring.cloud.config.profile 等配置项。
画面 14: 显示课程 PPT 页面，标题为“13. 获取配置中心配置”，内容包括目标、分析、需求和实现步骤。其中“小结”部分提到“将原来的 application.yml 删除；然后添加 bootstrap.yml 配置文件，该文件也是 Spring Boot 的默认配置文件，其内会经常配置一些项目中固定的配置项。如果是项目经常变动的应该配置到 application.yml 中，现在使用了配置中心就应该配置到 Git 仓库中对应的配置文件。”，并显示一个 <dependency> 代码块。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
cloud:
  config:
    server:
      git:
        uri: https://gitee.com/goheima/heima-config.git
  Eureka:
    client:
      Service-url:
        defaultZone: http://127.0.0.1:10086/Eureka
```

画面 2:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.4.0</version>
    <relativePath/>
</parent>

<groupId>com.heima.user</groupId>
<artifactId>user-Service</artifactId>
<version>0.0.1-SNAPSHOT</version>
<packaging>jar</packaging>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>

    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
        <version>2.1.3</version>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-config</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-openfeign</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-ZooKeeper-discovery</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-ZooKeeper-config</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-consul-discovery</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-consul-config</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-redis</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-RocketMQ</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-activemq</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-amqp</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-gateway</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-OAuth2</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-security</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-actuator</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-amqp</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-Kafka</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-RabbitMQ</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-redis</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-ZooKeeper</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-consul</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-vertx</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webflux</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webmvc</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-WebSocket</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webflux</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webmvc</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-WebSocket</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webflux</artifactId>
    </dependency

