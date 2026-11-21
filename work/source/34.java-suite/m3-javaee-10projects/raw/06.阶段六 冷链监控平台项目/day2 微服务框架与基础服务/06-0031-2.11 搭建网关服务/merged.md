# 2.11 搭建网关服务

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.11 搭建网关服务_【海量资源尽在 666java.com】.mp4
- 时长 7分48秒（音频 469s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好,前面呢我们给大家介绍了网关服务网关服务到底有什么意义我们为什么要使用网关服务那么下面呢我们就使用Spring Boot来搭建一个Spring Cloud的一个网关那么我们首先呢我们可以使用我们的这个Spring的官网上提供的这个Starter那么我们选择的是工程是Maven工程然后它的语言呢是用Java开发的然后Spring Boot的版本是2.2.2然后我们再输入我们的
[00:29] 整个项目它的一个一个原数据或者是要group ID啊artifact ID等等这样的一些信息我们group ID输入是com.it黑码然后artifact ID呢我们输入could-getaway然后在我们的option里边我们需要更改一点点比如我们的description描述描述信息我们输入网关服务
[00:59] 然后这个packager的名字packager我们把横杠改成了getaway选择我们的packaging是假类型的然后java的JDK是8那么在下面的它的依赖的话我们输入getaway然后把getaway给它添加进去因为本身我们的网关也是Ureca服务者中心里边的一个服务我们需要注册到服务中心去所以我们需要输入Ureca
[01:27] 那么这个Urica的话我们有两个一个叫做Urica的server一个叫client我们选择的是clientok下一步的话我们就点击这个generator然后生成我们的这个生成我们的这个jar 包然后保存到我们的目录里面去我们的工程目录然后这个jar 包ok他已经下载完了我们看一看已经有了这个getaway的一个zip包然后我们把它解压解压完了之后把原来这个zip包给删除掉那么
[01:58] 我们在我们的工程里边就可以把我们的这个工程给他添加进去我们选择project structure然后点击选择这个model然后点击加号这个加号里边我们import model然后选择这个getaway点击ok然后一步一步的啊但是这里边的话大家需要注意他是import modelfrom external model然后选择mavon工程点击next然后一步一步的添加进来ok我们这里边已经有了
[02:31] 我们这个工程的一些基础的一些信息比如我们的这个工程的名字啊这工程名字的主主程序主程序是一个Mavin的一个呃工程然后呢是一个Springboard的工程此时他会先下载一些依赖的包然后我们把这个名字给他更改一点那更改成什么呢更改成我们一个啊更简单的一个名字比如说就叫做Gateway的一个Gateway的一个application然后点击OKOK那么
[03:09] 还有一个文件叫做application的propertyapplication property文件的话我们需要给它给改成叫yaml文件yaml文件的结构比较好一点我们点击refact的rename然后yaml文件啊yaml文件你可以写成yaml或者是yaml都是可以的然后此时我们需要给我们的服务添加一些配置比如第一个我们要配置我们的yuruker
[03:39] 服务处的中心因为我们当前的这个服务呢是我们想要把它注册到我们的Uric服务里边那么此时我们需要先添加啊先添加我们可以先在我们的组程序里边添加一个EnableEnableDiscoveryClient这个呢是把我们当前添加成一个Uric的Client那么我们在样本文件里边可以添加Uric服务注册中心的地址Uric的一个Service URL然后它
[04:09] 有一个叫什么呢default然后这个地址就是我们的Urica服务处的中心的地址是http的一个urica.it黑马.com然后端口是8001然后斜杠uricaOK大家需要注意的是它的一个层次的一个结构层次结构不对的话
[04:36] 整个也是呃也是没办法正常运行的那么下面的话我们要定义我们的springspringcloud的spring的application的名字name我们把这个name起成叫做code gateway然后还有的话是我们可以添加我们整个服务的一个名字这个服务的就是这个工程的名字这工程的名字我们可以用server点比如说pot
[05:09] 8080然后server的Tomcat里边可以输入一些参数这个参数的话比如说url encoding就是utf8然后再输入我们的另外的参数叫max Thread就是最大的一个线程数比如说我们设置200还有就是我们的最小的一个mini的一个spare的线程数比如说我们设置30个那么
[05:45] 另外还需要添加一个什么呢比较重要的其实就是有一个connection的timeout连接超时的时间连接超时时间我们可以把它设置成50秒50秒的话就是5万毫秒然后还有一个就是我们的server letter的context pathserver letter server letter我看看哈
[06:21] 他应该在前面的一个server letter.context path这个context path我们也可以直接输入成叫codeok此时我们就添加完了我们的一些配置属性那么下一步的话我们就直接来启动我们这个服务getaway的然后点击run把我们的网关服务给启动起来那么此时我们只是做了什么操作呢第一我把我的网关的这个
[06:53] 服务给它启动起来这个网关服务呢它是注册到我们的服务注册中心去它的端口是8080然后它的路径contact pass是code那么我们看一看我们网关服务里边这个服务有没有注册上OK它已经在网关服务里边注册上了那么我们看一眼我们的这个POM文件这个POM文件呢它会把我们的什么呢把我们的Spring Cloud的getaway的这个
[07:22] 依赖给添加上另外一个他会添加一个Uric的一个client的一个依赖这是我们创建的我们的一个网关服务这个网关服务目前为止只是一个普通的spinbook的工程还没有添加我们的API建权啊还没有添加我们的跨域访问的一些处理等等我们下一边给大家介绍我们如何来进行操作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
使用 Spring Initializr 创建 Spring Cloud Gateway 项目，并配置其 Eureka 服务发现和核心服务端口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 Spring Initializr 网站选择 Maven 项目，语言为 Java，Spring Boot 版本为 2.2.2，Group 为 com.example，Artifact 为 demo，选中 Gateway 和 Eureka Discovery Client 依赖。
画面2：在 Spring Initializr 页面，Package Name 设置为 com.ithema.cold.gateway，Packaging 为 Jar，Java 版本为 11，选中了 2 个依赖。
画面3：在 IntelliJ IDEA 中，通过“Import Project”对话框导入项目，路径为 D:\projects\cold-gateway。
画面4：在 IntelliJ IDEA 中，确认导入项目，选择“OK”完成导入。
画面5：在 IntelliJ IDEA 中，显示 GatewayApplication.java 文件，其中包含 SpringBootApplication 注解和 main 方法。
画面6：在 IntelliJ IDEA 中，右键点击 application.properties 文件，选择“Add to Ignore List”。
画面7：在 IntelliJ IDEA 中，显示 GatewayApplication.java 文件，其中包含 SpringBootApplication 注解和 main 方法。
画面8：在 IntelliJ IDEA 中，打开 application.yml 文件，准备进行配置。
画面9：在 IntelliJ IDEA 中，编辑 application.yml 文件，添加 Eureka.client 配置。
画面10：在 IntelliJ IDEA 中，编辑 application.yml 文件，添加 spring.application.name 和 server.port 配置。
画面11：在 IntelliJ IDEA 中，编辑 application.yml 文件，添加 server.Tomcat.accept-count 配置。
画面12：在 IntelliJ IDEA 中，编辑 application.yml 文件，添加 server.Tomcat.max-threads 和 server.Tomcat.min-spare-threads 配置。
画面13：在 IntelliJ IDEA 中，显示 GatewayApplication.java 文件，其中包含 SpringBootApplication 注解和 main 方法。
画面14：在 IntelliJ IDEA 中，显示 pom.xml 文件，其中包含 Spring Cloud Gateway 的依赖配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
无

画面2：
无

画面3：
无

画面4：
无

画面5：
package com.ithema.cold.gateway;
import org.springframework.boot.SpringApplication;
public class ColdGatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(ColdGatewayApplication.class, args);
    }
}

画面6：
无

画面7：
无

画面8：
无

画面9：
Eureka:
  client:
    Service-url:
      defaultZone: http://Eureka.ithema.com:8001/Eureka

画面10：
Eureka:
  client:
    Service-url:
      defaultZone: http://Eureka.ithema.com:8001/Eureka
spring:
  application:
    name: cold-gateway
  server:
    port: 8080
    Tomcat:

画面11：
Eureka:
  client:
    Service-url:
      defaultZone: http://Eureka.ithema.com:8001/Eureka
spring:
  application:
    name: cold-gateway
  server:
    port: 8080
    Tomcat:
      accept-count: 100

画面12：
Eureka:
  client:
    Service-url:
      defaultZone: http://Eureka.ithema.com:8001/Eureka
spring:
  application:
    name: cold-gateway
  server:
    port: 8080
    Tomcat:
      accept-count: 100
      max-threads: 200
      min-spare-threads: 20

画面13：
无

画面14：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.2.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <groupId>com.ithema</groupId>
    <artifactId>cold-gateway</artifactId>
    <version>2.0.1-SNAPSHOT</version>
    <name>cold-gateway</name>

</project>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

