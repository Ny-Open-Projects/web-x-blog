# 08-Activiti与SpringBoot开发-引入坐标

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\08-Activiti与SpringBoot开发-引入坐标_【海量资源尽在 ubkz.com】.mp4
- 时长 5分17秒（音频 317s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 那下面我们就开始啊来实现activity与sprintboot整合啊那要做这个工作呢我们的activity7啊在发布正式版之后啊它是可以跟我们的这个sprintboot2.几的版本实现啊完全的整合那我们可以呢在我们的这个工程中将activity与sprintboot整合的这个坐标给它加入进来啊那现在我们开始啊来操作一把
[00:33] 那我可以这样在我们的这个里头我去新建一个新的project好,然后让它下一步比如说这个时候我就再去创建一个比如说叫做activitysati, vitiactivity这一次我起名比如说叫做activity06这个是我们的这个artifact的ID我把它放在这里那我们的这个group ID我可以叫做comit黑马
[01:06] 叫这名字然后接着往后走下一步啊然后这个时候就涉及到我们把当前的这个项目啊放在一个什么样的位置啊那我可以这样做啊那在咱们今天的这个第六天的这个圆码中啊比如说我这里边啊就是之前已经有了一个是吧已经有了一个啊那我没关系了我可以在这个地方呢我再去啊搞一个啊叫做新的啊
[01:35] 比如说来一个叫做demo叫做demo2在这个demo2里面我们将来再去把我们的这个activity放入进去好那这个部分我把这个名字也给各位再次修改一下把这个名字比如说我再回到上一步我们把这个名字改成叫做activity和我们的这个sprintboot整合的第六个势力往后走对吧那这一次我们再往后放
[02:04] 我给它放到我们的这个activity对应的第六天第六个部分然后呢放在我们的这个源码的demo放在我们源码的这个demo2里面可以吗放在这里面然后点OK对吧那这样我们就相当于放在我们源码demo2里面再有一个叫做它对不对这样就完整了好我们再往后走finish
[02:32] 这样我们就可以去创建出这样的一个目录,没问题的然后打开一个新的窗口我们的项目就已经创建好了但是我们的这个POM.XML中并没有去添加我们的这个activity7与我们的Spring Boot整合相关的这个坐标所以我们现在要做的工作就是activity7与
[03:03] 我们的Spring Boot整合整合的相关依赖需要加入进来我们整合的时候有哪样的一些依赖需要添加进来呢对吧我们肯定是需要加入很多相关的Starter对不对好我们也一样再次回到我们的第六天有一个叫资料在我们的基本素材中有一个Activity与Spring Boot整合的一个基本的资料
[03:32] 那这个部分其实就是我们啊提前给各位准备好的一个整合的这个坐标那来分析一下有哪样的一些坐标呢比如说整个这个过程我们要去实现啊activity背后将来真正连接的是我们的这个myseq数据库啊那我们将来要连接数据库需要JDBC啊Spring Boot start干JDBC
[03:59] 当然我们连接的过程中需要用到MySQL的驱动当然你可以这个部分你可以去掉因为它这里导的是一个高版本的依赖我们这边应该是在底下部分我给各位又添加了一个我们所用的5点5点几的MySQL的版本然后我们再往后走还有一个就是我们的Spring Boot Start Web
[04:28] 这是我们与web整合所需要用到的一个坐标但是我们实现与与我们的这个jUnit的单元测试整合在一起所需要用到的这个坐标那这一个就很关键了是activity和我们的sprintboot整合的一个坐标下面部分呢这个mybidness和我们的mycircle这个各位都非常容易理解那现在我可以做一个工作就是来把
[04:57] 对应的我们的这一段的内容都可以添加到我们的这个坐标里头来啊可以control v啊lendl再来这样呢我们基本上啊就完成了我们的工程创建以及我们的这个依赖所对应的这个依赖坐标啊添加就完成了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何将 Activiti7 与 SpringBoot2.x 整合开发，重点是添加必要的依赖坐标和配置。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程PPT，内容为“Activiti7 发有正式版之后，它与 SpringBoot2.x 已经完全支持整合开发。我们可以将 Activiti7 与 Spring Boot 整合开发的坐标引入到工程中，从而达到 Spring Boot 支持 Activiti7 整合。”
画面2: 在IDEA中打开项目，展示一个简单的BPMN流程图，包含StartEvent、Service Task和EndEvent。
画面3: 在IDEA中新建项目，项目名为“activiti06”，项目路径为“G:\Activiti7\开发计划\Activiti7-day06\activiti06”。
画面4: 在新建项目对话框中，选择项目存储目录为“G:\Activiti7\开发计划\Activiti7-day06\activiti06”。
画面5: 在新建项目对话框中，选择项目存储目录为“G:\Activiti7\开发计划\Activiti7-day06\activiti06”。
画面6: 在IDEA中编辑BPMN流程图，将Service Task的Id属性设置为“seniorTask”。
画面7: 在文件资源管理器中，显示“activiti06”项目文件夹。
画面8: 在文件资源管理器中，显示“pom.xml”文件。
画面9: 在EditPlus中打开“pom.xml”文件，显示Spring Boot相关依赖。
画面10: 在EditPlus中显示“pom.xml”文件中Spring Boot的插件配置。
画面11: 在EditPlus中高亮显示Spring Boot的测试依赖。
画面12: 在EditPlus中高亮显示Activiti Spring Boot Starter依赖。
画面13: 在EditPlus中高亮显示所有依赖和插件配置。
画面14: 展示课程PPT，内容为“Spring Boot 整合 Activiti7 的具体步骤如下：1. 添加 Spring Boot 整合 Activiti7 的坐标 2. 添加 SpringSecurity 安全框架的整合配置信息 3. 使用 Activiti7 新支持的类来实现工作流开发 ProcessRuntime 接口 TaskRuntime 接口 4. 使用新的 API 实现工作流开发。”

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面9:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.activiti</groupId>
    <artifactId>activiti06</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>activiti06</name>
    <description>Demo project for Spring Boot</description>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.0.Beta2</version>
        <relativePath/>
    </parent>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
    </properties>

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
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-amqp</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-redis</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-cassandra</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-Elasticsearch</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jdbc</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-cassandra</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-Elasticsearch</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jdbc</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-cassandra</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-Elasticsearch</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jdbc</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-cassandra</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-Elasticsearch</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jdbc</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-cassandra</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-Elasticsearch</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jdbc</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-cassandra</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-Elasticsearch</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jdbc</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring

