# 06-创建微服务工程

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\06-创建微服务工程_【海量资源尽在 ubkz.com】.mp4
- 时长 6分58秒（音频 418s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 创建微服务工程在这一小节中我们的主要目标是创建微服务副工程黑码-Spring Cloud用户服务工程user-Service服务消费工程consumer-demo这三个工程那为什么我们要去创建这三个工程我们有这样一个需求就是查询数据库中的用户数据并输出到浏览器
[00:29] OK那如果要去实现这么一个查询的话我们要有工程那用用的是Spring Cloud所以我们分服务的提供方跟服务的消费方这一类这一些工程所以我们去创建这三个这三个工程分别是这三个那每个具体的工程主要功能是做一些什么的我们也稍微的分析一下第一个复工程复工程我们主要做的事情呢是添加SpringBot复
[00:59] 坐标和管理其他组件的依赖的那接着用户服务工程用户服务工程的话我们去做的事情是整合mybattis查询数据库中用户数据也就是提供查询用户服务的好接下来是消费工程消费工程我们
[01:30] 主要的目的是利用查询用户服务获取用户数据并输出到浏览器好这就是这三个工程主要的作用现在我们打开idea去创建这三个工程创建第一个复工程不是project我们创建一个module模块工程下一步com.it黑码
[02:05] 然后是hema-Spring Cloud版本默认下一步路径名称没问题finish我们在里面去创建它的聚合子模块工程在实际应用中我们的服务提供跟消费的两个工程可以不在一个副工程下面我们现在为了展示方便跟上课所以我们把它放置到一个副工程里面做一个聚合子模块工程而存在好
[02:38] 当然实际开发中也是可以在一个工程中的好那如果是业务类似而且呢是同一个项目团队开发那当然是可以放在我们的一个副工程中好接下来我们名称是叫user-Service下一步路径没问题好名称finish你就造好了另外一个呢是消费工程叫做consumer-demo下一步
[03:15] 好创建完成完成后呢接着我们去添加复工程的这个碰文件依赖那他的依赖呢主要去添加我们一些其他组件的依赖坐标还就是我们springbook的一个副坐标ok我们打开今天的资料中去添加过来资料里边有一个这个文件黑马-Spring Cloud.sml配准键我们打开里面呢就有一些依赖我们把复工程跟其他的依赖给拿过来我们再来说明到idea中好加过来以后接下来
[03:48] 一定要注意好大家不要把这个modules给去掉这个意思是它的聚合子模块工程有哪一些你如果删掉的话它就检测不到它里面有这些子模块了ok那我们家的这个springboard的副坐标是2.1.5这个版本然后除此以外呢它的一些其他组件配置的有draw版本Spring Cloud版本用的是格林威治sre然后是tomymapper的还有mycycle的驱动内包好这版本
[04:17] 然后尤其是我们的spin cloud版本用了一个叫做scout import也就是说我们接下来那些项目中包括这个项目中应用的版本是来自于spin-cloud-dependencies这里边的可以去继承这些版本ok所以后续我们在应用spin cloud的组件时就不用写版本号也一样可以去应用那些组件好这就是我们的一个关于复混程中的依赖添加你就已经加好了
[04:45] 那后面的因为都是常规的连接还是一个配置的后续我们会讲到还是一个Lumbo我们以前用过接下来是一个打包的Maven插件Spinboard的一个打包插件我们当时也去打包部署过我们的一个Spinboard工程也见过没有什么特别至于其他两个工程我们暂时先不加他们具体的依赖因为我们一会再去独个的去配置这两个
[05:12] 一个是服务的提供一个是服务的消费工程好那我们的创建就已经创建完成回到笔记中那我们在刚才创建的过程中需要注意的地方就是在这个地方复工程中添加了依赖我们用了一个这个方式SprinterMaven中的一个score它的值是import把它拿过来到笔记中意思就是呢我们的这一个黑马杠Spring Cloud工程不仅是继承来自
[05:53] SpringBow的一个2.1.5的依赖坐标还要去继承来自这一个工程的依赖坐标好通过scout的import可以继承我们自己家的spring-cloud-dependencies工程中的依赖OK就不再是只继承来自SpringBow工程的一个依赖
[06:33] OK也就是在我们创建的时候你看复工程只是指定的是spring-book-starter-parent如果我们不这么写的话只能去继承这个工程的那我们现在还有要用到spring cloud的很多其他组件那么我们就可以这么加OK这就是我们的一个关于工程的一个搭建微服工程搭建完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建并配置 Spring Cloud 微服务工程的父工程和子模块，包括 pom.xml 文件的结构和依赖管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 页面，标题为“5. Spring Cloud概述”，内容包括 Spring Cloud 的组件和版本特征。
画面2：在 IntelliJ IDEA 中，鼠标悬停在“Build”菜单上，显示下拉菜单选项。
画面3：在 IntelliJ IDEA 中，项目结构显示为“http-demo”，但未展开具体模块。
画面4：在 IntelliJ IDEA 中，右键点击项目“helma-Spring Cloud”，弹出菜单，选择“New” -> “Module...”。
画面5：在 IntelliJ IDEA 中，打开并显示“pom.xml”文件，内容为父工程的 Maven 配置。
画面6：在 IntelliJ IDEA 中，项目结构中显示了“helma-Spring Cloud”父工程和“user-Service”、“consumer-demo”子模块。
画面7：在 IntelliJ IDEA 中，项目结构中显示了“helma-Spring Cloud”父工程和“user-Service”、“consumer-demo”子模块，但“pom.xml”文件未完全展开。
画面8：在 IntelliJ IDEA 中，显示“pom.xml”文件内容，包含父工程的 <properties> 和 <dependencyManagement> 部分。
画面9：在 IntelliJ IDEA 中，显示“pom.xml”文件内容，包含 <build> 部分，其中定义了 <plugins>。
画面10：展示课程 PPT 页面，标题为“6. 创建微服务工程”，内容包括工程需求和分析。
画面11：在 IntelliJ IDEA 中，显示“pom.xml”文件内容，包含 <dependencyManagement> 部分，其中定义了 <dependency>。
画面12：展示课程 PPT 页面，标题为“6. 创建微服务工程”，内容包括工程需求和分析，下方显示了 <dependency> 的代码片段。
画面13：在 IntelliJ IDEA 中，显示“pom.xml”文件内容，包含 <dependencyManagement> 部分，其中定义了 <dependency>。
画面14：展示课程 PPT 页面，标题为“7. 搭建配置user-Service工程”，内容包括工程目标和分析，下方显示了 <dependency> 的代码片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.itheima</groupId>
    <artifactId>helma-Spring Cloud</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>user-Service</module>
        <module>consumer-demo</module>
    </modules>
</project>
```

画面8：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.itheima</groupId>
    <artifactId>helma-Spring Cloud</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>user-Service</module>
        <module>consumer-demo</module>
    </modules>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.5.RELEASE</version>
        <relativePath/>
    </parent>
    <properties>
        <java.version>1.8</java.version>
        <spring-cloud.version>Greenwich.SR1</spring-cloud.version>
        <Mapper-starter.version>2.1.5</Mapper-starter.version>
        <mysql.version>5.1.46</mysql.version>
    </properties>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.mybatis.spring.boot</groupId>
                <artifactId>mybatis-spring-boot-starter</artifactId>
                <version>${Mapper-starter.version}</version>
            </dependency>
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>${mysql.version}</version>
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

画面11：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.itheima</groupId>
    <artifactId>helma-Spring Cloud</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>user-Service</module>
        <module>consumer-demo</module>
    </modules>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.5.RELEASE</version>
        <relativePath/>
    </parent>
    <properties>
        <java.version>1.8</java.version>
        <spring-cloud.version>Greenwich.SR1</spring-cloud.version>
        <Mapper-starter.version>2.1.5</Mapper-starter.version>
        <mysql.version>5.1.46</mysql.version>
    </properties>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.mybatis.spring.boot</groupId>
                <artifactId>mybatis-spring-boot-starter</artifactId>
                <version>${Mapper-starter.version}</version>
            </dependency>
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>${mysql.version}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
```

画面12：
```xml
<!-- springCloud -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-dependencies</artifactId>
    <version>${spring-cloud.version}</version>
    <type>pom</type>
    <scope>import</scope>
</dependency>
```

画面13：
```xml
<!-- springCloud -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-dependencies</artifactId>
    <version>${spring-cloud.version}</version>
    <type>pom</type>
    <scope>import</scope>
</dependency>
```

画面14：
```xml
<!-- springCloud -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-dependencies</artifactId>
    <version>${spring-cloud.version}</version>
    <type>pom</type>
    <scope>import</scope>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“5. Spring Cloud概述”，内容包括：
- 目标：Spring Cloud整合的组件和版本特征。
- 小结：
  - 整合的组件可以有很多组件：常见的组件有：Eureka注册中心，Gateway网关，Ribbon负载均衡，Feign服务调用，Hystrix熔断器。在有需要的时候项目添加对应的启动器依赖即可。
  - 版本特征：以英文单词命名（伦敦地铁站名）。

画面10：标题为“6

