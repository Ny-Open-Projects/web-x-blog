# 28.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\28.课程总结_【海量资源尽在 666java.com】.mp4
- 时长 3分3秒（音频 183s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程呢做一个总结那么今天呢是我们项目的第一天那么我们今天的主要呢是给大家去讲一下这个项目的介绍那么以及他的一些什么项目背景呢市场分析呢啊等等这个呢大家做一些了解就可以了那么大家呢其实是需要通过这个1.6开始啊去看详细看我们里面所提供的一些内容那么
[00:26] 这个呢就是去介绍了一些我们项目的一些本身的一些东西啊包括我们的技术的方案然后呢技术的架构那么以及技术解决方案还有技术亮点啊等等然后呢我们后面又详细的给大家去介绍了一下那么我们这个功能啊就是我们这个项目的一些功能那么大家也可以在我们所给大家提供的这个资料中啊找到呢有一个这个圆形图
[00:52] 那么大家可以去看一下比如说我们来看一下我们的这个index那么这个呢其实就是我们的原型图大家可以去看一下这个产品经理去所设置的这个原型图那么每一个功能其实都有大家可以去看一下OK好那么接下来呢我们讲完这个功能介绍之后那么我们就实现了今天的主要的一个功能的实现那就是这个注册以及登录那么注册登录呢其实
[01:20] 那么更多的我们在前期呢需要去把这工程搭建出来所以说我们先去把这工程呢做了一下这个搭建那么搭建完成之后呢我们就会搭建了两个工程对吧一个是副工程就是这个IDcast的碳花当然我叫那个麦碳花是一样的
[01:39] 那么还有就是这个SSO这个工程啊然后呢我们下面是不是就开始编写我们的一些这个业务逻辑的代码啊那我们大致有实现了什么呢就是短信验证码的这样的一个发送那么还有什么呢就是我们去做了用户的一个登录那么登录呢我们所使用的有一叫做什么JWT作为这样的一个规范
[02:00] 然后我们又去实现了完善的个人信息在这个里面会涉及到两个基础点那么一个就是图片的上传那么另外一个就是人脸识别那么这个我们都已经讲过了
[02:14] 最后我们去把前面的内容去综合起来去实现了一下个人信息的一个完善这样的功能那么最后我们也做了一下完整的从我们的这个输入手机号去发送验证码到完善信息整个流程的一个测试那发现也是OK的可以通走通的这样的一个流程那么最后我们实现了一个根据这个token来查询
[02:38] 用户信息的这样的一个接口那么这个呢就是以上的就是我们今天的一些主要的一些这个内容了那么今天呢是第一天啊所以说大家呢也跟着我们这个节奏去了解一下这个项目的一些内容以及跟着我们的这个代码的编写呢自己动手呢去写一下这个项目啊OK好那么这个关于这个课程的总结就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个名为“探花交友”的在线社交平台项目，涵盖项目背景、市场分析、技术架构、功能模块及用户登录与个人信息完善等核心内容。

2) 按时间顺序列出每张画面的要点：
画面1：课程介绍《探花交友》，目录结构显示项目包含项目介绍、市场分析、竞争分析、技术方案等章节。
画面2：项目简介，展示“探花”APP界面，包含“探花”、“搜附近”、“桃花传音”等功能模块，以及“今日佳人”和“推荐”用户卡片。
画面3：项目简介，展示用户发布动态的界面，包含用户头像、昵称、年龄、状态等信息，以及多张图片和“发布”按钮。
画面4：技术亮点，列出项目采用的技术栈，包括Elasticsearch、Spark+Millib、MongoDB、Redis、CDN、Apache Dubbo、Spring Boot+MyBatis等。
画面5：项目文件夹结构，显示“day01”目录下的多个AVI视频文件，以及“新建文件夹”和“WIN_A1A9NCDT4V4”等文件夹。
画面6：登录页面设计，展示手机登录注册界面，包含“获取验证码”按钮和“已验证至1351111111”的提示。
画面7：首页设计，展示“探花交友”APP首页，包含“附近人”、“推荐”、“消息”、“视频”、“我的”等导航选项，以及“今日佳人”和“推荐”用户卡片。
画面8：项目文件夹结构，显示“探花交友移动端原型V1.2”目录下的“data”、“files”、“images”、“resources”等文件夹，以及“index.html”、“start_c_1.html”等HTML文件。
画面9：搭建工程，展示“itcast-tanhua”项目的pom.xml文件，定义了依赖的版本和所需的信息。
画面10：搭建工程，展示“itcast-tanhua-ss0”模块的pom.xml文件，包含Spring Boot、MyBatis、Baomidou等依赖。
画面11：用户登录流程图，展示用户通过手机验证码登录，SSO校验，最终获得token的流程。
画面12：AliyunConfig配置类，定义了阿里云OSS客户端的配置属性，包括endpoint、accessKeyId、accessKeySecret等。
画面13：实现完善个人信息，展示Mock接口文档，包含用户登录和上传头像的接口地址。
画面14：检查登录状态，展示UserService和UserController的代码，用于根据token查询用户信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面9：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
        <relativePath/>
    </parent>
    <groupId>cn.itcast.tanhua</groupId>
    <artifactId>itcast-tanhua</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>
    <name>itcast-tanhua</name>
    <description>Demo project for Spring Boot</description>
    <properties>
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
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-mongodb</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-Elasticsearch</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
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
            <artifactId>spring-boot-starter-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-WebSocket</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-aop</artifactId>
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
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-WebSocket</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-aop</artifactId>
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
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-WebSocket</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-aop</artifactId>
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
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-WebSocket</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-st

