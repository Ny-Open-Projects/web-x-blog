# 2.4 Springboot与Eureka集成

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.4 Springboot与Eureka集成_【海量资源尽在 666java.com】.mp4
- 时长 10分51秒（音频 651s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那么前面呢我们通过给大家介绍了手机通讯录的一个例子来给大家引出了我们的服务助手中心而服务助手中心包含的服务的助手中心消费者和停户者三个角色那么
[00:15] 在我们的服务的中心里面呢可能有多种多样的一些实现虽然Uric在2.0的以后的版本实现了闭源但是1.0的功能上也比较强大而且呢现在的很多企业里边用到的也比较多那么Spring Cloud也把它集成到一个子项目里边去了所以我们在冷链设备监控平台里边也给大家讲解一下我们如何使用Uric来封装成我们自己的一个服务的中心那么首先呢我们创建一个我们的工程
[00:44] 我们点击new然后new的是什么呢new了一个model我们新建一个model然后选择的工程类型是maven我们点击next然后我们输入group idcom.it然后呢我们的artifact id是什么呢是我们的code-urica然后我们点击nextnext里边我们可以选择我们当前urica的一个地址
[01:13] 比如说我们选择code-Eureka然后它的model的location我们可以输入选择我们的上一级location就是在project里边我们的这个工程它的路径也是第一盘的project的code-eurekaOK那么我们现在可以点击一下finishOK
[01:49] 我们当前的这个工程已经添加进来了但添加进来之后它只是一个空白的工程这空白工程里边它的POM文件也是没有的那么下一步我们就需要把我们URIK的一个包或者说URIK它的一个工程的一个POM文件给它添加进来而这个POM文件呢我们可以使用Starter比如说就是SpermStarter的这个来给它添加那我们
[02:16] 在这里边我们还是还可以重新啊输入一下比如说我们选择我们的这个groupgroup的名字呢就com.itc码那么我们的artifact id呢是code-urica啊当然这个可能给大家觉得是有重新输入了一遍那么我们服务注册中心然后他的包路径的名字
[02:46] 就是com.http://code.url我们使用JDK的8然后生成的jar 包我们在这儿主要是用它我们使用urlurl的话我们因为是服务我们所以说是我们使用的是url的一个server那么紧接着我们点击exploit再点击exploit的话它会把我们的泡沫文件或者说整个工程给它以预览的形式来给大家展示出来那么我们稍等一下已经显示好了
[03:15] 在显示好里边之后呢这个时候这个地方就是我们的POM文件了那么POM文件我们可以直接把POM文件给它拷贝过来我们点击这个copy然后呢在我们的这个POM文件里边就是我们刚才生成的code-uric的工程里边我们给它拷贝进来那么我们简单的看一下这个就是我们刚才生成的啊com.itk码code-uric然后呢我们在这里边的话使用的它是啊SminCloud是我们的
[03:46] Hotting Release也就是2.2的这个Release那么我们看一看和Uzure Server相关联的比如说这个是有一个Starter是Spring Cloud的Starter然后Netflix-Uzure Server这是Spring Cloud的封装的一个Uzure Server然后它此时它还依赖于Spring Boot然后这个时候我们整个工程的一个POM文件已经引入进来了不需要我们
[04:15] 一个一个的给它填兼进来啊这过程还是比较简单的那下一步的时候我们就可以创建我们的这个工程工程的一些代码代码结构了那因为刚才的时候我们没有使用这个download这个zip我们如果使用download的zip的时候我们其实可以发现我们整个的它的包名或者说它基础的一个工程已经填兼进来了那么我们直接在我们的代码里边可以给它
[04:43] 新添加一个新添加一个什么呢我们点击右键新建一个Java的类这个Java类呢我们可以直接输入我们的包的名字比如叫com.it黑马.code.Eureka.application那么前面呢com.it黑马是公司的一个坐标或者说叫group的一个坐标code呢是项目的一个坐标
[05:13] 指的是我们能电监控平台那么Urica是这个子系统的一个坐标那么后边呢Urica Application就是我们的一个主程序类那此时呢我们添加了这个类这个类的话我们首先需要把它安装或者说把它配置成我们的一个Spring Boot的应用所以我们在这儿需要Enable的需要添加我们的Spring Boot的一个Application这样的一个注解然后在这个注解里边呢我们可以创建一个命函数
[05:43] 那么这个命函数里边我们就直接添加spring application点run方法那么run方法里边就是我们的Urik当前的类的一个class再加上参数OK那此时我们已经添加好了我们的启动程序或者启动的函数那紧接着我们需要再添加一个我们的application的样本文件application.yml文件
[06:13] 而在这个YMR文件里边我们需要添加的是两部分内容一部分内容是属于我们当前的server的server port有server的端口我们当前的server端口是8001就是我们Urica服务柱子中心的端口那紧接着呢我们还需要添加一个我们当前服务的一个名字叫spring.application name那么这个name就是code-urica-
[06:42] 这个名字可以随便起但是我们要起的稍微有意义一点指的是我们当前冷链监控平台的Urica的一个服务端那此时它是作为一个application就是Spring Boot application其实是OK的是可以的那紧接着我们可以启动一下启动一下的时候大家会发现启动的时候会报错了为什么会报错呢因为我们在我们POM文件里边引入了我们的这种Urica的一些注册但是启动的时候呢你却没有
[07:11] 把URIKA这个注解使用上或者说是它里边有一些包的一些冲突我们没有发现它所以在这个地方我们需要我们的URIKA Application里边我们要添加我们的一个URIKA的一个注解比如说我们Enable它是Enable URIKA的一个Server那么这个时候我们当前的这个主函数就可以作为URIKA的一个辅助的中心了但是还需要添加我们的就是Application1Arm文件里边还要添加一些其他参数
[07:40] 这个其他三数就是辅助的中心的一个地址Eureka.clienteureka.instanceinstance.housename那么这个housename呢我们可以添加一个housename就是一个一个地址这个地址我们起一个名字叫Eureka.it可以吗.com
[08:10] 这个呢是我们当前Ureca实力所在的一个主机的一个名字那紧接着呢我们还可以再添加我们的client.serviceurl然后serviceurl的有一个叫defaultzone这个defaultzone就是我们具体的一个地址了http然后urica.it黑马黑马.com
[08:44] 然后呢加上我们的8001然后Urica这样的一个地址下面呢我们还需要加上Register with Eureka那么这个参数呢表示我们是否将自己注册到Eureka服务注册中心上我们可以把它设置成truetrue的意思就是我们自己的这个当前的一个Spring Boot的应用它也是一个Eureka的一个应用那紧接着我们可以再添加一个fetch
[09:17] FastRegisterRegistry那么这个呢表示我们是否从自己从URIK住的中心上获取信息当前因为当前的Spring Boot当前是一个URIK的也是一个Spring Boot的应用我们是否要从URIK上获取信息这是我们添加的这个URIK的一些配置信息OK我们保存一下
[09:45] 下一步的话我们就可以直接来使用了那当然这个地方好像有点是这样的一个地址应该是他和和我们的这个Service这样是是是是对齐的OK那我们启动一下我们的这个Ureca服务这个应用OK此时他已经注册到我们的当前的这个服务上了那这个地方
[10:20] 还有一点可能是需要注意的是啊我们可以先先打开我们的啊叫localhostlocalhostlocalhost或者是我们直接用我们的配置里面的一个一个地址8001我们来访问一下OK那此时我们就能够看到我们的Ureca的服务已经在我们当前的服务助的中心上已经启动起来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
使用 Spring Cloud 创建并运行一个 Eureka 服务注册中心。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Eureka 服务注册中心的架构图，说明服务消费者通过 Eureka 获取服务列表，服务提供者向 Eureka 注册，服务消费者调用服务。
画面 2: 在 IDEA 中新建项目，选择 Maven 项目，准备创建 Spring Boot 项目。
画面 3: 在 Spring Initializr 网站上配置项目，选择 Java 语言、Spring Boot 2.2.2 版本，Group 为 com.itheima，Artifact 为 cold-Eureka，点击 Generate。
画面 4: 在 IDEA 中打开项目，显示 pom.xml 文件内容，包含 Maven 配置和版本信息。
画面 5: 在 pom.xml 中添加 Spring Cloud Eureka Server 依赖。
画面 6: 显示 Spring Initializr 生成的项目结构和 EurekaApplication.java 文件内容。
画面 7: 在 IDEA 中打开 EurekaApplication.java 文件，准备编写代码。
画面 8: 在 EurekaApplication.java 中添加 Spring Boot 注解和主方法。
画面 9: 在 application.yml 文件中配置服务器端口和 Eureka 服务名称。
画面 10: 在 EurekaApplication.java 中添加 EurekaServer 注解。
画面 11: 在 application.yml 中配置 Eureka 服务名称为 cold-Eureka-server。
画面 12: 运行 EurekaApplication，控制台显示服务启动日志。
画面 13: 在浏览器中访问 http://localhost:8001，显示 Eureka 服务注册页面。
画面 14: 在浏览器中访问 Eureka 服务注册页面，显示服务实例信息和服务器状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.itheima</groupId>
    <artifactId>cold-Eureka</artifactId>
    <version>1.0-SNAPSHOT</version>

</project>
```

画面 5:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-server</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
    <exclusions>
        <exclusion>
            <groupId>org.junit.vintage</groupId>
            <artifactId>junit-vintage-engine</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

画面 6:
```java
package com.itheima.cold.Eureka;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ColdEurekaApplication {
    public static void main(String[] args) {
        SpringApplication.run(ColdEurekaApplication.class, args);
    }
}
```

画面 9:
```yaml
server:
  port: 8001
spring:
  application:
    name: cold-Eureka-server
```

画面 10:
```java
package com.itheima.cold.Eureka;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.Eureka.server.EnableEurekaServer;

@SpringBootApplication
@EnableEurekaServer
public class EurekaApplication {
    public static void main(String[] args) {
        SpringApplication.run(EurekaApplication.class, args);
    }
}
```

画面 11:
```yaml
server:
  port: 8001
spring:
  application:
    name: cold-Eureka-server
Eureka:
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 架构图，服务注册中心指向服务消费者和提供者，服务消费者指向服务注册中心，服务提供者指向服务注册中心。
画面 14: 表格数据，显示服务实例信息和服务器状态，包括 Application、AMIs、Availability Zones、Status、Name、Value 等列。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

