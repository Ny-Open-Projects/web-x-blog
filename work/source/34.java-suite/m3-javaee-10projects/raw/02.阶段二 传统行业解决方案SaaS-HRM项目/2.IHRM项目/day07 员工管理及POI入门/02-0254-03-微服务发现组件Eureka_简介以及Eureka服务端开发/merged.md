# 03-微服务发现组件Eureka：简介以及Eureka服务端开发

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\03-微服务发现组件Eureka：简介以及Eureka服务端开发_【海量资源尽在 ubkz.com】.mp4
- 时长 8分28秒（音频 508s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 刚才和各位简单的介绍了一下就是这个员工管理的一些需求以及我们实现的一种方式那对于刚才那些全部都是一些基础的一些功能那些基础的功能呢我们就直接提供给各位那如果有兴趣的话你想写自己去写其实也可以好了那接下来呢就是说呢我们现在呢这个系统当中呢微服务各位发现越来越多了咱们现在已经写了三个微服务有企业的
[00:32] 有系统微服务还有一个我们的员工微服务那这些微服务呢是不是应该对它可以做一个统一的一个管理呢各位那怎么去做统一管理这边呢就用到我们之前学过的一种技术手段呢就是我们叫做ERICA好了ERICA那这边呢我们就可以借助ERICA统一的对我们所有的服务好了进行一个注册进行一个管理并且呢可以做一个监控的这么一个工作
[01:02] 那我们接下来呢就来看一下这个发现组件Ereka好了那对于Ereka呢其实是Spring Boot或者是Spring Cloud全家统之一因为Spring Cloud里面涵盖的东西比较多有比如说我们今天要用到的Ereka还有我们一会儿还要用到的我们的服务调用的组件等等那对于这个Ereka而言这边呢有它的一个简单的一个介绍
[01:27] Erica分成两个组件一个是server也就是我们的服务端一个就是我们的Erica client那不管是server还是client其实都是Erica的一部分那server是什么意思其实就是一个Erica的一个服务端一个Erica的一个服务那client呢其实就是所有的微服务因为我们现在有三个微服务那这些微服务是不是都要被统一的一个管理起来那借助谁就借助Erica serverErica服务端来作用那所以对于我们而言要想用Erica的话
[01:56] 其实很简单搞出一个Urica Server把所有的那些咱们自己写好的微服务是不是注册到Urica Server让它进行统一管理就可以了好了接下来这边对它的一个概述有兴趣的话各位去看一下就可以了其实就是说了一下它的一些特性我们之前都学过了在这边咱们简单的把这个Urica服务端给它构造出来接着把服务注册上去我们来看一下效果就可以了
[02:24] 当然了我们注册这个URI卡主要目的其实就是为了我们之后的代码打基础我们之后涉及到多个微服务之间的调用所以URI卡是我们不得不经过的一个环节好了我们刚才说到了首先呢要去搞一个URI卡服务端那对这个URI卡服务端呢这个比较简单我们可以这样去做那对于这个URI卡呢和我们的一些RPC组件不同的是URI卡呢这个服务端需要我们自己去搭建
[02:53] 这个注册中心需要我们自己去搭建所以我们自己着手去开发Eureka服务端怎么做很简单右键创建一个我们的model点击next好了这边可以给它起一个我们的名称ihrm好了我们的名称就叫我这边跟讲义上保持一致了就叫Eureka了OK好了接着点击nextfinish
[03:25] 那我们这个工程呢创建过来之后呢还需要导入相应的Eureka所依赖的一些坐标那这些坐标在今天的资料当中给各位准备好了Eureka的一些POM.txt那我们需要在复工程当中引入一个管理的坐标复工程在上边引入过来好了
[03:52] dependence management这里面就是声明我要用ERICA那ERICA里面设计的组件也比较多那我们在服务端呢也要引入自己的ERICA相应的一些我们叫做配置那这个ERICA server这边的Po文件呢咱们也引入过来抱歉这边只有一个client端的没关系咱们也可以拿过来dependence好了里面的依赖呢就把client改成server就可以了改成server就可以了
[04:21] 好了这个版本号呢我们就不填了统一让他自动帮我们管理OK那好了我们这个Ereka呢我们的PoE文件已经引入进来了那引入进来之后我们要做的事情呢比较简单我们可以一起参考一下我们的讲义是这样的在我们这边呢我们需要给他添加Ereka的一个配置文件那这个配置文件呢在今天资料当中也给各位准备好了
[04:49] 好了上面是Erica服务端的一个配置好了拿过来Resource下右键创建一个我们叫做Fill这个Fill自己创建那就自己创建吧右键自己创建一个Fill好了Application YMLOK把内容拷过来那拷过来之后呢我需要跟各位做一个简单的解释就是说呢这个配置究竟什么意思首先
[05:24] 这个代表的是我当前Ereka服务的请求端口6868好了里面才是我Ereka真正的一些配置那对于这个Ereka来说我们交货的地址这边也有就是我当前请求的一个地址和我们这个端口6868好了我们其他的地方比如说因为这个Ereka是一个所有微服务的一个管理端那所有的服务是不是都应该注册过来那其他的时候怎么注册过来其实借助的就是底下这个地址
[05:52] OK那这个和各位解释清楚了那接下来做的最后一件事就可以创建一个其实这个Eureka说的多么高端大气上档次其实说白了也是一个Springboard服务那对于我们而言只需要写一个启动类把它跑起来那这样一来Eureka服务端咱们就构建好了那所以接下来呢我们需要去配置一个Eureka的一个启动类配置一个Eureka的一个启动类好了在这边呢
[06:23] 创建一class把它放到com.ihrm.erica这个包下比如说呢我就叫做Eureka serverOK好了里面这个启动类呢比较简单咱们就写一个mint方法其实就可以了当然这个代码呢我就直接从讲义拷过来了好了对这个拷过来的时候有点问题啊好了我直接自己写吧psvmOK好了那接下来
[07:03] 我们刚才说过了其实对于这个呢是我们的Erica服务端的启动类那对于一个启动类来说是Sprint的一个启动类那既然是Sprint Boot的一个启动类我们需要配置注解那配置的这两个注解呢我们之前也玩过了第一个Sprint Boot Application好了那接下来第二个是我们比较关键的一个注解
[07:32] 因为我们这边是它的一个叫做Erica服务端所以我使用一个叫做Enable Erica Server代表它是一个服务端配置UIEOK那这样一来我这个Erica服务端咱们已经配置好配置好了之后执行启动类闷方法好了它就开始去启动了让它自己去启动吧我们这边打开浏览器那我们请求的是Localhost冒号叫做6868
[08:16] 好了点击回撤我们一起耐心等待一下好了那这样一来各位会发现我当前这个Eureka服务其实已经启动成功了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Spring Cloud 的微服务架构中，Eureka 服务注册与发现机制的配置与启动过程，以及 POI 报表的入门知识。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 第7章“POI报表的入门”，内容包括“员工管理”、“需求分析”和“数据库表概述”，其中数据库表包括 em_archive、em_positive、em_resignation、em_transferposition。
画面2：与画面1内容相同，为同一页面的重复展示。
画面3：在 IntelliJ IDEA 中，右键点击项目根目录“ihrm_parent”，弹出“New”菜单，准备创建新模块。
画面4：在文件资源管理器中，显示项目目录结构，当前选中“Sql”文件夹，其中包含“员工管理.sql”文件。
画面5：在 IntelliJ IDEA 中打开“ihrm_parent”的 pom.xml 文件，展示父工程的依赖管理，包括 Spring Boot Web、Logging、Test、Fastjson 等依赖。
画面6：在 Notepad++ 中打开“ihrm_parent”的 pom.xml 文件，展示子工程的依赖配置，包括 Spring Cloud Dependencies、Eureka Client、Feign。
画面7：在课程 PPT 中，展示“ihrm_eureka”模块的 pom.xml 文件内容，其中包含 Eureka Server 依赖，并提示“（3）添加 application.yml”。
画面8：在 IntelliJ IDEA 中，右键点击“ihrm_eureka”模块，弹出上下文菜单，准备进行操作。
画面9：在 IntelliJ IDEA 中，打开“ihrm_eureka”模块下的“application.yml”文件，准备进行配置。
画面10：在 IntelliJ IDEA 中，编辑“application.yml”文件，内容为 Eureka 服务的配置，包括 server.port、Eureka.client.registerWithEureka、fetchRegistry、serviceUrl、defaultZone。
画面11：在 IntelliJ IDEA 中，打开“EurekaServer.java”文件，准备编写主类。
画面12：在课程 PPT 中，展示“1.4.2 微服务注册”章节，内容为“（1）将其其他微服务模块添加依赖”。
画面13：在浏览器中打开新标签页，准备访问服务。
画面14：在浏览器中访问 Eureka 服务的管理页面，显示“Instances currently registered with Eureka”为空，以及“General Info”中的系统信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```xml
<parent>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
        <fastjson.version>1.2.47</fastjson.version>
    </properties>
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
</parent>
```
画面6：
```xml
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
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```
画面7：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-Eureka-server</artifactId>
    </dependency>
</dependencies>
```
画面10：
```yaml
server:
  port: 8888 #服务端口
Eureka:
  client:
    registerWithEureka: false #是否将自己注册到Eureka服务中，本身是所有无需注册
    fetchRegistry: false #是否从Eureka中获取注册信息，本身是所有无需注册
    serviceUrl:
      defaultZone: http://127.0.0.1:$(server.port)/Eureka/
```
画面11：
```java
package com.ihrm.Eureka;
import org.springframework.boot.SpringApplication;
public class EurekaServer {
    public static void main(String[] args) {
        SpringApplication.run(EurekaServer.class, args);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“第7章 POI报表的入门”，子标题包括“1 员工管理”、“1.1 需求分析”、“1.2 数据库表概述”。
画面7：PPT标题为“ihrm_eureka模块pom.xml引入Eureka-server”，下方提示“（3）添加application.yml”。
画面12：PPT标题为“1.4.2 微服务注册”，内容为“（1）将其其他微服务模块添加依赖”。
画面14：Eureka 管理页面表格数据包括“Instances currently registered with Eureka”（无实例）和“General Info”（包含 total-avail-memory、environment、num-of-cpus、current-memory-usage）。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

