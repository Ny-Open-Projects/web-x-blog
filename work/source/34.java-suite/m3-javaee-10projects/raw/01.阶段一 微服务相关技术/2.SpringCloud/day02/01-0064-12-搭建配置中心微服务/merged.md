# 12-搭建配置中心微服务

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\12-搭建配置中心微服务_【海量资源尽在 ubkz.com】.mp4
- 时长 11分10秒（音频 670s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 搭建配置中心vfoo在这一小节中我们的主要目标是创建马云的远程公开git仓库搭建配置中心vfoo config-server前面说到了在有了配置中心之后所有的vfoo配置文件都可以从git仓库中进行集中管理要做到这一点的话需要有git仓库和配置中心所以我们在这一小节的具体需求就是要去创建git仓库搭建配置
[00:36] 中心我们给它起一个名字config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config.config
[01:12] 我们现在呢逐一去完成第一个创建Git仓库你要先去注册马云一个账号注册以后呢接着我们再打开它的界面去创建具体的仓库这是注册了的那大家也可以在这边去免费注册一个账号注册以后呢接着我们去创建具体的仓库新建仓库起一个名称简介非币田配置中心创建一个公开的我们没有具体的私密代码
[01:50] 所以这个可以创建公开的继续语言我们是抓网模板的话我们用的是idea好这一个的随便选好那开源的那也是随便选一个许可证Remi文件创建没问题好点击创建创建以后呢接下来我们在这上面的去添加一个配置文件主要就是我们希望可以通过这个Git仓库呢去
[02:24] 集中修改配置文件所以我们去创建一个配置文件出来好文件新建后面呢这个配置文件可以更新到所有其他微服中也就是给那些微服去应用我们在这GitHub或是马云上去修改配置文件的时候呢就可以去同步修改我们的那些微服对应的配置文件配置项这边起一个名字这个名字起呢比较特别就是要有规格格式
[02:52] 那这具体格式呢我们可以打开来了解一下讲义这个配置文件命名方式第一个呢是应用名第二个呢是环境就是你用的是开发还是测试环境还是生产环境那你自己命名这个现在命名的倒是还随意但是格式呢是要一个杠的之后呢我们在后面用的时候要指定清楚名称是什么环境是什么在我们的项目中到时候要指定这一个配置就可以了好
[03:21] 对应上就行那现在你你这边名字这些可以随便写我们回到浏览器中继续完成这个文件这个里面的内容的话呢我们可以使用我们提供服务的工程user-Service里面的那些配置我们把它复制过来打开找到配置文件粘贴过来创建user-dev.yml这个可以不写那就不用写了提交
[04:00] 这个文件就已经创建好了按照分析我们现在要去搭建配置中心回到我们的开发工具创建一个聚合子模块工程config-server这名称也是任意定名称finish添加具体的依赖那我们的依赖呢要加Eureka client的依赖加了以后我们再加一个配置
[04:56] 就是这是一个配置中心的所以我们要加一个依赖是关于配置中心的依赖config-server好依赖加完加完以后呢接下来我们去修改它的启动引导类那我们去生成配置文件也要好然后我们再去修改这个启动引导类中让它开启配置服务config-server
[05:49] 再到我们的配置文件去修改端口号我们来起一个12000名称最重要的就是告诉它我们的Git地址我们是在马云上创建的所以这个地址从那边复制过来打开这个地址点击复制好复制了回到开发工具中值是它接下来继续配置Ureka
[06:51] 我们要把这个当做一个服务也要注册到Urica上Urica.好这个也就配置完了配置完以后呢接下来我们要去启动测试看一下能否现在访问配置中心这个服务呢能够读取到马云上面的一个配置文件我们当时写了一个叫user-dev.yaml的文件看一下能否访问到也就是我们访问是
[07:38] 这一台服务器但是呢因为它是会从我们的马云上去拉取这些配置文件所以看一下能否去拉取到并且能够正确访问到这个配置文件大家在做的时候一定要注意这个要改成你自己的这个马云地址或者是GitHub的地址启动看一下报错没好是没有的没有的话我们现在去访问打开浏览器我们访问的地址呢是127.0.0.1然后是1万
[08:30] 2000user-dev.yml因为它是从我们的马云中去拉取这个文件那直接访问就可以了我回车成功的标准就可以看到这个配置文件的内容见到了没有问题好这就是我们一个配置中心的一个搭建搭建完成回到我们的笔记中进行削减那么刚才呢搭建配置中心的时候这个依赖依赖有
[09:02] 配置中心依赖还有就是我们的配置中心的配置文件给他拿过来依赖的话我们加了这两个依赖配置文件这个内容那一定要注意就是我们现在呢是从马云上去拉取配置的那如果现在配置改了的话会不会跟着改呢我们可以去测试一下就是
[09:52] 我们指定了这个地址了现在上去故意的去改动一下现在的情况是如此那现在我们去到这个文件中去修改编辑我们改一个东西假设你这个添加一个像的话添加一个当然你这边加这个外面有格式也要加对才行好加个test然后呢来一个黑码回这个要空一个黑码好加了以后接着我们再去
[10:25] 保存更新了它提交再去刷新这个地址也见到了这个文件的更新说明我们是实时能够及时的去获取到的直接这样访问的话是可以获取到最新的配置软件你也注意一下就是在GIG11中也就是马云中修改了配置文件会在配置中心服务
[11:00] 即时更新好这就是我们的一个搭建配置中心微服的所有内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
搭建并配置 Spring Cloud 配置中心服务（config-server），使其从码云（Gitee）远程仓库获取配置文件，并集成 Eureka 服务注册与发现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT，标题为“12. 搭建配置中心微服务”，目标是创建远程 git 仓库并搭建 config-server，分析部分提到使用 Spring Boot 方式搭建。
画面 2: 浏览器访问码云（Gitee）网站，准备创建新仓库。
画面 3: 在码云网站上创建名为 “heima-config” 的新仓库，选择 Java 语言和 Apache 2.0 协议。
画面 4: 在 IntelliJ IDEA 中新建模块，选择 Maven 项目，准备创建 config-server 项目。
画面 5: 显示 config-server 项目的 pom.xml 文件内容，包含 Spring Cloud Config Server 和 Eureka Client 的依赖。
画面 6: 显示 config-server 项目的 application.yml 文件，准备配置。
画面 7: 在 application.yml 文件中配置 server.port 和 spring.application.name。
画面 8: 在 application.yml 文件中配置 git 仓库地址和 Eureka 服务地址。
画面 9: 启动 config-server 服务，控制台显示服务启动成功并注册到 Eureka。
画面 10: 重复画面 1 的 PPT 内容，强调搭建配置中心的目标。
画面 11: 显示 config-server 启动后控制台的详细日志，确认服务已注册到 Eureka。
画面 12: 展示配置中心的配置文件内容，包括 server、spring.application.name、git 仓库地址和 Eureka 服务地址。
画面 13: 在码云仓库中编辑 user-dev.yml 文件，配置数据库连接信息和 Eureka 服务地址。
画面 14: 重复画面 12 的配置文件内容，强调配置文件的结构和关键参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5 的 pom.xml:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.2.RELEASE</version>
        <relativePath/>
    </parent>

    <groupId>com.ithema.config</groupId>
    <artifactId>config-server</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>config-server</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-config-server</artifactId>
        </dependency>
    </dependencies>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Finchley.SR1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

画面 6 的 application.yml:
```yaml
server:
  port: 12000
spring:
  application:
    name: config-server
  cloud:
    config:
      server:
        git:
          uri: https://gitee.com/guheima/heima-config.git
Eureka:
  client:
    Service-url:
      defaultZone: http://127.0.0.1:10086/Eureka
```

画面 12 的配置文件内容：
```yaml
server:
  port: 12000
spring:
  application:
    name: config-server
  cloud:
    config:
      server:
        git:
          uri: https://gitee.com/guheima/heima-config.git
Eureka:
  client:
    Service-url:
      defaultZone: http://127.0.0.1:10086/Eureka
```

画面 13 的 user-dev.yml:
```yaml
uri: jdbc:mysql://localhost:3306/Spring Cloud
username: root
password: root
application:
  name: user-Service
  type: Elasticsearch
  package: com.ithema.user
Eureka:
  Service-url:
    defaultZone: http://127.0.0.1:10086/Eureka
  prefer-ip-address: true
  instance:
    ip-address: 127.0.0.1
  lease-renewal-interval-in-seconds: 5
  lease-expiration-duration-in-seconds: 10
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 和 10 的 PPT：
标题：12. 搭建配置中心微服务
目标：
- 创建 git 仓库：在码云上创建仓库
- 搭建配置中心 config-server：使用 Spring Boot 方式搭建和配置
标题：13. 获取配置中心配置
目标：改造用户微服务 user-Service，配置文件信息不再由微服务项目提供，而是从配置中心获取

画面 1 的架构图：
- 用户（蓝色人形图标）指向“git 仓库（红色方框）”
- “git 仓库”指向“配置中心（紫色方框）”
- “配置中心”指向“服务 A（蓝色方框）”
- “配置中心”指向“服务 B（蓝色方框）”
- “配置中心”指向“服务 X（蓝色方框）”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

