# 4.服务调用链路追踪-快速上手

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-1 服务调用链路追踪的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-1 服务调用链路追踪的理解和使用\4.服务调用链路追踪-快速上手_【海量资源尽在 666java.com】.mp4
- 时长 2分6秒（音频 127s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们一起学习了一下服务调用链路追踪的这个什么解决方案那这里边其实主要就涉及到两块技术吧一块就是Spring Cloud当中的什么Flux一个就是Wiki南极亚一个一个来先学习这个是什么做Flux那么Flux呢它属于Spring Cloud当中的一个什么呀一个组件吧那它的主要作用就是在什么呀在这儿啊相当于调用
[00:30] 链监控工具的客户端他直接放在什么各个微服务当中那他的作用就是负责产生什么对一些监控数据这个数据怎么产生我们刚才给大家分析过是不是就是记录日志对不对你把这个src给它集成到我们各个微服务里边然后他就要干活干什么活就是记录日志其实这个时候就产生这个什么这个数据上这些数据之后他不做分析他不做分析他会上传给谁
[00:59] 就传给这个VKINGVKING呢就会存储和分析这些什么呀对日志然后最终呢用图形化的方式给它干什么整理出来那咱具体在项目当中啊怎么去使用这个Sluice呢使用起来非常简单啊我们来个快速上手非常简单只需要两步只需要两步啊第一步呢就是引入Sluice的这个依赖大家看一下就是这个地方这儿
[01:27] 对你就在你现有的这个项目的基础上再加入这么一个依赖就行了这是第一步非常简单那第二步就是在配置当中增加这么一个配置spin.sluice.enable对不对给点指示就是开启sluice这个链路追踪这个功能就想搞定了就这么简单所以说要想在你的项目或微服务当中去
[01:53] 加入这个什么链路追踪的功能就是通过sluice对不对只需要两步第一步就是引入sluice的依赖第二步呢就是开启这个什么呀sluice就ok了就这么简单咱一会呢会给大家来一个入门案例

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 Spring Cloud Sleuth 以实现分布式链路追踪，并结合 Zipkin Server 进行数据存储与展示。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程 PPT 的目录结构，当前章节为“2.1 快速上手”，并显示了“Spring Cloud Sleuth”与“Zipkin Server”的架构图，说明 Sleuth 作为客户端将链路数据发送至 Zipkin Server。
画面2: 展示“2.1 快速上手”章节内容，介绍使用 Sleuth 的两步操作，第一部分是引入 Maven 依赖。
画面3: 展示“2.1 快速上手”章节内容，继续介绍引入 Maven 依赖。
画面4: 展示“2.1 快速上手”章节内容，继续介绍引入 Maven 依赖。
画面5: 展示“2.1 快速上手”章节内容，继续介绍引入 Maven 依赖。
画面6: 展示“2.1 快速上手”章节内容，继续介绍引入 Maven 依赖。
画面7: 展示“2.1 快速上手”章节内容，展示 Maven 依赖的 <parent> 配置块。
画面8: 展示“2.1 快速上手”章节内容，展示 Maven 依赖的 <dependencies> 配置块，包含 spring-boot-starter-web 和 spring-cloud-starter-sleuth。
画面9: 展示“2.1 快速上手”章节内容，展示 Maven 依赖的 <dependencyManagement> 配置块，包含 spring-cloud-dependencies。
画面10: 展示“2.1 快速上手”章节内容，展示 Maven 依赖的 <dependencyManagement> 配置块，包含 spring-cloud-dependencies 的 <version> 和 <scope>。
画面11: 展示“2.1 快速上手”章节内容，展示 Spring Boot 配置文件中的 sleuth 配置项。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面7:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
    <relativePath/>
</parent>
```

画面8:
```xml
<properties>
    <java.version>1.8</java.version>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <spring-cloud.version>Greenwich.RELEASE</spring-cloud.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
</dependencies>
```

画面9:
```xml
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
```

画面11:
```properties
# 是否开启 sleuth
spring.sleuth.enabled=true
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: PPT 标题为“2. Spring Cloud Sleuth”，子标题“2.1 快速上手”。架构图中，“Zipkin Server”通过双向箭头指向“追踪数据存储”，“Zipkin Server”通过双向箭头指向“图形化展示”。
画面7-11: PPT 标题为“2.1 快速上手”，内容为文字说明和代码配置。

5) 无。

