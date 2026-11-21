# 8.Sleuth&Zipkin集成案例

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-2 Zipkin的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-2 Zipkin的理解和使用\8.Sleuth&Zipkin集成案例_【海量资源尽在 666java.com】.mp4
- 时长 17分21秒（音频 1041s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们一起了解了一下Z King接下来的话咱就要整一个入门案例开始给大家演示Sluth和Z King如何进行这个什么呀集成特别是大家要关注这个Z King呢是如何把这个Sluth追踪到的这些日志信息呢给它用图形化的方式在里面展示出来那咱这个案例呢其实还是这个是呀Sluth的这个入门案例还是这个案例
[00:28] 但是这次呢我们要给它整的更加规范更加完整一些我们准备这么干啊大家看看我们要加入这个什么呀对有瑞卡注册中心然后呢还是这两个微服但是呢他们之间的调用呢我不再通过rest template我要换成什么呀对换成非
[00:50] 这是不跟sluice那个入门案例不太一样的对不对那sluice入门案例呢它没有注册中心啊然后呢远程请求也是通过res的template我们现在加入了注册中心啊然后加入了这个什么呀非这更贴近于这个真实项目开发嘛啊这个案例然后呢在每个微服里边呢都集成这个谁啊sluice当我们发起请求发起这个什么呀微服之间调用的时候sluice是不是就会生成追踪日志对吧
[01:17] 那么这个追踪日日生成之后呢还会最终上报给谁啊对上报给我们刚才介绍的这个谁啊Z King Server我这是不是都已经启动过了嘛对不对这是他的这个UI界面上报给这个Z King Server然后Z King Server呢最终呢就会把这些日志给用图形化的形式给他干什么呀展示出来所以例子啊还是Sluice那个入门案例但是呢我们增加了注册中心啊请求呢换成了Fain然后呢又跟谁集成到一起了呀
[01:46] 对Z King集成到一起了这是我们这个Sluice跟Z King集成的一个案例吧大概给大家介绍一下那咱接下来呢就开始编码实现这个功能那咱这里边是这样子的啊我们呢是咱是不是刚才说了涉及到一个注册中心微服A微服B三个工厂对不对所以我们这样准备再来一个什么呀副工厂啊统一这个做一个依赖的管理
[02:12] 这三个微服务包括这个复工程的呢这个基本的代码我都已经给大家提供好因为这些东西或者整个这一套这个东西大家都非常非常熟了啊有些东西我都提前准备好咱一起看一看咱看这个复工程对吧我们重点看他的泡沫文件吧咱整体过一遍就行你看他是不是继承了这个Spring Boot对不对213这个版本然后呢这里边是不是有三个某块吗一个是注册中心一个是a微服一个是谁啊b微服
[02:43] 然后呢这我们这个依赖管理呢其实只是规定了一下spin cloud的这个版本对吧这是复工程吧然后我们看这个注册中心啊注册中心其实跟你平时用的有瑞卡注册中心没啥区别没啥区别啊你这个你用之前的注册中心拿过来也可以用啊或者说你自己搭一个快速的一搭一搭完事那不就是铺文件里边对不对放一些这个依赖然后呢就是这个谁啊配容件里边配置一下这个名字啊特别是这个什么呀
[03:13] 端口号对吧还有有瑞卡客户端啊等等相关的一些这个地址啊相关的一些信息这个我不再说了然后最后呢就是启动类上是不是要加这个inable什么呀有瑞卡server这个注解就完事就这么简单是不是一个注册中心就干什么呀搭建起来啊这不再过多说了啊然后我们看看这个Service a和Service b这两个微服务呃这个大家还有印象吗我们其实就是还是这个例子啊哪个例子呢这个例子这是一个a一个b吗
[03:44] A首先发请求到BB再发一个请求到什么到A就是123还是这个例子只不过换成什么通过非去发起这个什么调用这个请求咱看看Service A和Service B这两个微服务基本代码先看碰文件看一个就行了对不对我们需要引入的依赖你看有web你看这儿是不是就是zking对吧这个你一定要注意这个你要注意你看我们这儿是不是引入一个依赖zking的依赖
[04:12] 这个呢其实就是Z King的客户端刚才我们下载了一个jar 包然后把它运行起来我们刚才说这是Z King的什么呀对服务器端啊这儿对应的是扣端扣端是不是应该集成到我们的微服务里边那你应该能猜到这个扣端的作用是啥对将来Sloth产生的这个追踪日志是不是由这个扣端给上传到什么地方对上传到上传到什么呀Z King Server
[04:44] 上场的Zking Server也就是说呢微服里边除了有sluth其实我们放进去的还有什么呀Zking的客户端sluth是产生追踪之志的而Zking的客户端是负责把这个追踪之志上报给谁呀Zking Server的啊说这个细节呢大家一定要注意我们在泡沫文件里边是不是有所提对不对然后有维卡的客户端呀飞印呀对不对还有这个熔断熔断咱后边马上就会讲到那Source B里边这个依赖跟Source A是一样的我就不再过头说了
[05:15] 然后呢我们看看这个谁呀配置配置里面就是一些基本的配置吧应用程序的名字啊端口号呀基本仿路径呢还有这个诸董中心的地址对不对那saurus b里面的这个配置跟这也是一样当然他的这个名字啥的仿路径端口号肯定都是不一样的啊然后我们看加代码这块要啥加代码我们先看启动类吧启动类这个跟平时是不是没啥区别然后呢我们看看还有哪些代码给大家准备好
[05:44] 大家看这个非印代理我们已经给大家提供好了因为这个大家比较熟我们就不再花时间去编写这个东西非印代理大家也知道我们这个例子当中它是它是这个样子的微幅A是要通过非印调用微幅B微幅B是也要通过非印去调用微幅A是吧那也就是说这两个微幅都要有什么非印代理非印接口那这个代码咱已经写好咱一起看一看我们现在看到的这个是
[06:15] 微服a这边的飞行代理你看他是不是往微服b那边发请求发起调用了对不对然后你再看看serviceb这边他肯定也有一个非应代理我们找一找二进的对吧你看然后他是往微服a这边是不是发请求呢这个代码大家都比较熟就不再过多说了然后呢剩下就是什么呀Controller呗我们将来是不是先发请求到微服a这边的Controller微服a这边的Controller再通过非应发起请求到
[06:45] 微幅B这边的什么呀控制了微幅B这边的控制在通过飞应发现请求到什么呀微幅A这边的控制了是不是完成了这两三次的一个什么呀一个微幅之间的一个什么呀表用啊还是这个入门案例只不过是换成有瑞卡和谁呀飞应了而已啊更贴近于这个企业实际开发的一个情况啊这咱目前呢吧把这个案例当中我们提供好的这些代码整个呢我们是过了一遍
[07:14] 那接下来是不是该咱们去编写代码实现功劳首先是应该要把这个什么呀微服之间的这个调用这块代码先搞定对不对就是我们刚才说的呃还是这个地方微服a先发请求到bb再发请求到什么到a先把他们之间的这个调用啊微服之间这个调用这个代码咱先搞定吧这个代码比较简单是不是主要通过飞行就行了咱先去这个谁呀呃微服a这边的这个control在这里边呢我们通过飞行
[07:45] 往哪发请求对威福B这边发请求就OK了那咱首先的话就把这个FIN代理先给他注入进来然后我们这个叫Service A应该是Service B而进的对不对Service B发请求的把它注进来注进来之后我们是不是该写方法定义一个方法反而指stream类型起个名字叫SERVICE目前是不需要参数的
[08:23] 然后回车那在这里边的话我们呃在这个sluice那个入门里边是通过resttemplate发的这个请求那现在呢我们就换上这个什么呀对非音代理通过他的一个什么方法我们的名字就叫Service哎他就往serviceb那边干什么呀发请求发行之后那边是不是给我们有返回值吗我们起个名字叫serviceb来接受一下就行接完之后呢我们就返回呗
[08:53] 这个返回的东西呢我们跟讲义要保持一致啊我们找一找在这个地方大家看一下是吧还是一个自动刷拼接啊跟前面那个sluice入门案例阴谋一样这是这边这个远程调用这个代码咱就搞定搞定完之后呢咱接下来去哪啊按照流程是不是该去这个Service b这个control了你是不是往这发请求了吗对不对那所以说呢这边我们
[09:25] 需要定义一个方法他应该叫Service没有参数那在这里边我们需要写什么代码呢那这呢我们是不是要通过飞行代理往Service a那边去发起一个什么远程调用互相调用嘛那所以说我们也需要把这个什么呀飞行代理呢给他注入进来他应该是叫Service a而进的好接下来的话我们就通过他的这个什么呀
[10:01] 对Service 2这个方法哇Service a那边干什么呀发请求然后呢反而值呢我们接收一下stream我们就叫Service s1 vse 2吧然后返回一个字符串这个我们也要跟讲义保持一致就这块对吧那接下来呢他这是不是往微服a a那边啊往微服a那边发一请求那接下来咱是不是应该回到微服a的Controller里边
[10:43] 来再编写一个方法是不是接收这个请求就行了A这边我们再加一个方法public string s e r v i c e r 是吧到这是不是就该结束了吧反正这个调用对吧那这里边的话我们就直接返回一个字幕串就行了咱跟讲义保持一致啊他就直接返回一个字幕串完事了整个调用就到此结束了
[11:14] 没错啊这是咱们把这个什么呀微服之间的这个相互调用这块代码通过主要是通过飞应对不对把这块代码给补充一下当然还没补充完啊加代码咱基本上写的差不多接下来是不是要加这个什么呀get mapping这个访问路径啊咱正好呢通过加这个get mapping呢把咱这个什么呀调用的这个什么呀链路对吧这个路径呢跟他补充完整首先呢大家知道我们的前端就是浏览器是不是应该先往这发尽就就是微服A的service1
[11:43] 是不要发请求那我这呢就要加一个什么呀对给他埋屁给一个路径我们就叫s e r v i c e1就叫service1没错吧往这发请求然后呢他呢这通过非是不是往Service b那边发请求是不是往Service b那边发请求请求的路径是不是叫Service哎他叫Service那接下来这个流程是不是该走到Service b这边是不是该往这发请求啊
[12:13] 那他这呢我也得配一个什么呀给他卖品刚才大家看到了他这的路径是不是就叫什么呀对就叫Service咱给他补上然后呢到这之后呢他又通过飞是不是往Service a那边又发了一个什么呀对发起了一次调用你看这里他调的这个路径是不是叫Service 2对不对那所以说咱应该回到sales a这Controller应该是往这发起的这个调对不对那这呢我就需要也加上一个什么呀
[12:43] 给他买品那他的这个路径一定是叫什么呀对service2哎大家看一看这样子的话我们是不是就把这个微服之间相互请求相互调用的这个代码是不是就给他补充完整了将来前端发请求先到这儿然后这儿发请求再到什么呀B的这边这边再发请求又回到什么呀A的这边然后调用结束没错吧那这块代码搞定之后接下来干嘛接下来是不是该死路次上场了
[13:14] 我们说了我们将来一往这发请求是不是这个WIFI之间就开始调用那这个时候呢Sluice是不是就该产生这个追踪制制了那怎么让Sluice去工作呢哎大家应该还有印象是不是我们只需要在这个什么呀配置文件里边是把那个开关打开就行你还有印象吗在Sluice入门案里边咱讲过吗开启什么呀对开启SLEUTH对吧怎么开启啊那个配置是哎
[13:51] 第一个就是对吧Spring.slose.enable给一个值什么呀true就搞定了这样子slose就开始干什么呀工作了啊然后呢微幅B这边的配置文件我们是不是也应该加上没错吧那两边的这个开关都打开了将来发生这个请求或者发生调用的时候slose就会去工作去产生这个什么呀对追踪日志然后我们在控制台是能看到吗前面我们已经给大家演示过这个信息了
[14:18] 但是呢我们这次呢我们说了我们不想看那个空闪对不对因为那个重文本呢我们观察起来不方便分析起来也太麻烦我们准备干什么呀我们准备把这些日志让他上传给谁呀对传给Z King传给Z King的服务器端谁去传给Z King的服务器端刚才我们也提到我在碰碰键里边我们是不是引入了Z King的这个谁呀扣孔短是不是那他就该工作他就会负责呀把Sluth生成的这个追踪日志给上传给谁呀
[14:47] 上传给Z King Server再找一找那个图对上传给他那Z King Server在哪Z King Server我们是不是下载了一个加包现在已经把它跑起来了对不对那现在我只需要把Sluth产生的日志信息是不是传给这个Z King Server就行那这话咋传给他我问他扣端是不是就有这个功能但是扣端并不知道Z King Server的这个什么呀服务器地址并不知道他的端口号是不是那因此呢我们要想把追踪日志
[15:15] 上传给Zkingthrower只需要加一个配置就搞定了就是配置一下Zkingthrower的这个什么呀对它的服务地址和端口号就OK非常非常简单啊咱看一看讲义哎你看就是这儿就这个地方是不是指定Zkingthrower的这个地址吗你只要把地址告诉他你就不用管啊那个扣端他会负责把sloss生成的追踪之志往这儿进行什么呀对往这儿进行上传你就不用管了
[15:46] 那咱接下来是不是就可以把这个配置也给他干什么呀加上对就是指甲配置就够了啊其他咱就不用过然后呢怎么写啊对还是spring.spring.然后后边就是zkingzking base url对就是他然后呢就是http冒号杠杠look host端口号我们刚才给大家展示过了是不是九四11吗
[16:18] 默认值9411那两边是不是都得配啊对不对这微服A微服B那边是不是也得配这个东西因为它每个微服都会产生这个什么呀追踪日志嘛好这块配置加上之后呢咱们这个sluth啊跟这个zking它集成的这么一个案例这个代码咱就全部编写完了啊你注意一下我们主要编写代码一块呢就是微服之间的这个通过分译相互的一个什么呀请求一个调用啊
[16:46] 然后呢就是我们又把sluth这个功能给它开启了将来它就会产生这个什么呀追踪日志呃然后最后呢我们把zking server的这个地址给它配置了一下那将来呢呃sluth产生的这个追踪日志是不是就会往这进行上传那上传给zking server之后呢zking server就会帮我们去干什么呀分析这些日志然后以图形化的形式给展示出来那但是这个案例呢这个代码咱就已经全部干什么呀
[17:14] 编写完了就这么多咱一会就可以进行什么功能测试了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spring Cloud Sleuth 和 Zipkin 实现分布式服务链路追踪，并通过 Feign 实现服务间调用。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程PPT，内容为“2.2 入门案例”下的“2.2.1 案例简介”，图示两个微服务（1、3）调用微服务B（2）。
画面2：在IDEA中打开项目结构，展示 `pom.xml` 文件，其中包含父依赖 `<parent>` 和 `<modules>` 配置。
画面3：在IDEA中打开 `discovery-server` 项目的 `application.properties` 文件，配置 Eureka 服务注册与发现。
画面4：在IDEA中打开 `Service-a` 项目的 `pom.xml` 文件，配置 Spring Boot Web 和 Spring Cloud Sleuth 依赖。
画面5：展示课程PPT，内容为“3.2 Sleuth & Zipkin集成”下的“3.2.1 案例简介”，说明将使用 Eureka 作为注册中心、Feign 实现调用，并将日志上报至 Zipkin。
画面6：展示课程PPT，内容为“2.1 快速上手”，说明引入 Sleuth 依赖的步骤。
画面7：在IDEA中打开 `Service-a` 项目的 `ServiceController.java` 文件，展示 `@RestController` 和 `@RequestMapping` 注解。
画面8：展示课程PPT，内容为“4. Feign代理”和“5. Controller类”，展示 Feign 客户端接口 `ServiceAgent` 和 Controller 类 `ServiceAController`。
画面9：在IDEA中打开 `Service-b` 项目的 `ServiceController.java` 文件，展示 `@Autowired` 注解和 `serviceAgent.Service()` 方法调用。
画面10：展示课程PPT，内容为“3.2 Sleuth & Zipkin集成”下的“3.2.2.2 启动类”和“4. Feign代理”，展示 `@SpringCloudApplication` 和 `@EnableFeignClients` 注解。
画面11：在IDEA中打开 `Service-a` 项目的 `ServiceController.java` 文件，展示 `service1` 和 `service2` 两个方法。
画面12：在IDEA中打开 `Service-b` 项目的 `application.properties` 文件，配置服务端口和 Eureka 服务地址。
画面13：在IDEA中打开 `Service-a` 项目的 `application.properties` 文件，配置 `spring.sleuth.enabled=true`。
画面14：在IDEA中打开 `Service-a` 项目的 `application.properties` 文件，配置 `spring.zipkin.base-url=http://localhost:9411`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2：
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
    <relativePath/>
</parent>

<modules>
    <module>discovery-server</module>
    <module>Service-a</module>
    <module>Service-b</module>
</modules>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter</artifactId>
            <version>Greenwich.RELEASE</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

画面3：
```properties
spring.application.name=sleuth-discovery
server.port=58020
Eureka.instance.hostname=localhost
Eureka.client.register-with-Eureka=false
Eureka.client.fetch-registry=false
Eureka.client.serviceUrl.defaultZone = http://${Eureka.instance.hostname}:${server.port}/Eureka/
```

画面4：
```xml
<parent>
    <artifactId>SleuthWithZipkinDemo</artifactId>
    <groupId>com.thema.sleuth</groupId>
    <version>1.0-SNAPSHOT</version>
</parent>

<artifactId>Service-a</artifactId>

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

画面6：
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
    <relativePath/>
</parent>

<properties>
    <java.version>1.8</java.version>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <spring-cloud.version>Greenwich.RELEASE</spring-cloud.version>
</properties>
```

画面7：
```java
package com.thema.sleuth.servicea.Controller;

import ...
@RestController
public class ServiceController {
    @RequestMapping("/hello")
    public String hello() {
        return "hello world";
    }
}
```

画面8：
```java
@RestController
public class ServiceAController {
    @Autowired
    private ServiceAgent serviceAgent;

    @GetMapping("/service1")
    public String service1(HttpServletResponse request) {
        String Service = serviceAgent.Service();
        return "Service-a-service1" + "-->" + Service;
    }
}
```

画面9：
```java
package com.thema.sleuth.serviceb.Controller;

import ...
@RestController
public class ServiceController {
    @Autowired
    private ServiceAgent serviceAgent;

    public String Service() {
        return serviceAgent.Service();
    }
}
```

画面10：
```java
@SpringCloudApplication
@EnableFeignClients
public class ServiceBootstrap {
    public static void main(String[] args) {
        SpringApplication.run(ServiceBootstrap.class, args);
    }
}
```

画面11：
```java
package com.thema.sleuth.servicea.Controller;

import ...
@RestController
public class ServiceController {
    @Autowired
    private ServiceAgent serviceAgent;

    @GetMapping("/service1")
    public String service1() {
        String Service = serviceAgent.Service();
        return "Service-a-service1" + "-->" + Service;
    }

    @GetMapping("/service2")
    public String service2() {
        return "Service-a-service2";
    }
}
```

画面12：
```properties
spring.application.name=sleuth-with-zipkin-Service-b
server.port=58022
server.servlet.context-path=/Service-b
Eureka.client.serviceUrl.defaultZone = http://localhost:58020/Eureka/
```

画面13：
```properties
spring.application.name=sleuth-with-zipkin-Service-a
server.port=58021
server.servlet.context-path=/Service-a
Eureka.client.serviceUrl.defaultZone = http://localhost:58020/Eureka/
# 开启Sleuth
spring.sleuth.enabled=true
```

画面14：
```properties
spring.application.name=sleuth-with-zipkin-Service-a
server.port=58021
server.servlet.context-path=/Service-a
Eureka.client.serviceUrl.defaultZone = http://localhost:58020/Eureka/
# 开启Sleuth
spring.sleuth.enabled=true
# 指定zipkin server的地址上报链路日志
spring.zipkin.base-url=http://localhost:9411
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT标题“2.2 入门案例”，子标题“2.2.1 案例简介”，图示：微服务A（包含服务1和3）通过调用链指向微服务B（服务2）。
画面5：PPT标题“3.2 Sleuth & Zipkin集成”，子标题“3.2.1 案例简介”，文字说明：采用Eureka作为服务注册与发现中心，采用Feign实现服务间调用，并将日志上报至Zipkin服务端，最终使用Zipkin图形化展示服务调用链路追踪情况。
画面6：PPT标题“2.1 快速上手”，文字说明：引入 Sleuth 依赖的步骤。
画面8：PPT标题“4. Feign代理”和“5. Controller类”，文字说明：展示 Feign 客户端接口 `ServiceAgent` 和 Controller 类 `ServiceAController`。
画面10：PPT标题“3.2 Sleuth & Zipkin集成”，子标题“3.2.2.2 启动类”和“4. Feign代理”，文字说明：展示 `@SpringCloudApplication` 和 `@EnableFeignClients` 注解。

5) 无。

