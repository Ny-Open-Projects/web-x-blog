# 6.服务调用链路追踪-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-1 服务调用链路追踪的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-1 服务调用链路追踪的理解和使用\6.服务调用链路追踪-功能测试_【海量资源尽在 666java.com】.mp4
- 时长 10分52秒（音频 652s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好 截止到目前呢我们已经把slues入门案例呢全部编写完毕了接下来咱们就要进行功能测试那咱首先是不是应该把这两个微服都给它启动起来好 咱现在分别把这两个微服呢启动一下好 大家看一下现在呢这两个微服都正在启动等它们启动完了之后我们怎么进行功能测试给大家看一下讲义看一下这个地方
[00:41] 根据这个图的话我们很简单就是通过浏览器先往微服A的这个地方是不是先发一个请求然后呢就出发它去干什么呀远程访问微服B然后又出发微服B去远程访问微服A然后结束对吧很简单啊那咱看他们现在都启动完毕了没有这个已经启动完毕了58022这个呢也启动完毕了58011对吧那咱现在呢先把
[01:10] 有控制台的日志呢先给他清一下清空清空完之后呢咱进行功能测试功能测试的话咱就是要往这发请求往这个地方啊点击一下允许好大家看一下页面咱是不是看到返回来有信息对吧咱先分析分析这个信息是怎么得到的啊咱先看看58011大家知道这是什么呀demo1就是微服A它的这个基本访问路径大家看一下是吧然后呢
[01:42] 后边的路径是service1这个应该是看control了吧control了里面你看咱这里边是不是有两个方法其中第一个方法就是service1那这块呢其实对应的是不是就是这个庆头对应的就是前端发了这个庆头对不对那我们在这个什么呀哎浏览器当输入这个地址敲回车那么其实呢就相当于是不是往这发庆头了啊对应的位置呢我们刚才说了其实就是呃这个什么呀demo1里边的这个什么呀service1没错吧
[02:13] 你看这个代码然后呢在这里边呢他又发请求到哪对Demo2就是微服B里边的这个谁啊Service谁啊E对就到这儿没错吧然后呢这边呢又发一请求回到这个什么呀微服A就是Sluice1什么呀Service2就是又回到这儿又回到这儿然后呢每次掉它是不是都返回一个字幕上我们在这儿是不是就都进行这个什么呀拼接了
[02:43] 然后我们在页面上看到的这个输出就是我们字幕上拼接的一个最终的一个效果啊其实对于我们来说页面上输出啥不重要啊不重要那我们重点要看的是日志就是控制台日志的一个输出啊来咱看看这个跟之前有啥区别看看这两块啊这两块和这一块这是咱以前日志输出的时候没有的东西啊你看咱平时这个日志输出是不是都长这样你看这个info后边这个中国号里边
[03:14] 是不是就一个这个应用程序的名字吗对不对后边没信息了但是这次不一样我们把Sluice加入到我们的微服务当中之后我们每次发请求每次进行微服务之间的这个调用的话它都会在这个中管号里边呢记录一些信息这些信息呢就是我们说的啊Sluice通过日志记录的这个什么呀对服务链路追踪信息
[03:40] 有同学说老师这看不懂啊这是啥意思那咱今天一起分析分析啊一起给大家说一说来咱看一下讲义吧讲义里边呢有具体的这个说明啊大家看一看呃讲义在这儿啊这跟咱刚才看到的是一样的对不对那么这个中国号里边这一个中国号里边你看1234有四块内容是不是第一块内容呢就是application内部这个大家都猜到就应用程序的名字了对吧那么第一
[04:11] 二块内容非常关键叫trace IDtrace ID第三块内容就这一块啊这一块就这个什么272FD这个什么呀A38B4对不对还有什么92CC8E对不对这几个呢我们称之为是什么呀span ID那么还有最后一块内容叫什么呀export对不对我们这的值都是什么呀fuzz所以首先你得知道啊
[04:40] 这块日志信息呢一共有四部分组成我们重点关注的是后三部分那咱一个一个来首先我们说说这个Trees ID是啥就这块272FD272FD272FD哎你会发现啊这个每个微服务制度当中这个值是不是都是一样的你看这个值是不是蓝框里面这个值一样吗一样的啊但是后边这个你看272FD但是这是38B4对不对这是CC81这个值就要干什么
[05:11] 就不一样那也就是说呢trace id是一样的spy id都是不一样那咋回事呢接下来你注意了啊你看他说了sloos可以在发起每个请求的时候他帮我们自动生成trace id还有什么呀spy id啥意思啊咱看看这个图你看这是不是开始发请求然后先走到这然后再调用这个地方然后又回到这进行调用对吧你每次发请求或每次发起这个远程调用的时候呢sloos都会帮我们生成trace id和什么呀spy id
[05:43] 这两个值是由slose帮我们生成的这个你首先要知道然后还没完你要注意的是这样同一个请求链路当中的trace id是一样的但是什么id是不一样的span id的值是不一样的啥意思呢来看看啊来我放到这儿跟你说一说举个例子啊我这个值给你的这个模拟的一个值比较简单一些比如说举个例子前端发了一次请求这是一次请求
[06:14] 但是这一次请求里边包含了这个是不是有多次的微幅之间的一个调用对不对那么这一次请求它会生成一个trace id比如说叫1举个例子叫1这是trace id那么它第一次调用是不是出现在这个地方对不对那比如说这个spy id它就是多少2然后又发起一次请求是不是1到2对吧这个spy id就是多少就是3然后呢2到3之间又发起一次请求假设这个spy id是多少是4
[06:43] 你明白什么意思吧就是每发几次请求就会生成一个什么呀spy id但是你不管发生多少次请求这些spy id对应的trace id的值都是什么呀一样的那就是由于这多个spy id他们的trace id的值是一样的才证明这多次调用属于什么呀对属于一个请求当中属于一个请求也就是他们组成了一个什么呀调用链就是服务调用链
[07:12] 这是他们之间的一个什么呀一个关系咱们具体再回到这再说一说你看TRACE ID一个请求分配的ID号用来标识一条什么呀请求线路然后SPID是一个基本的工作单元就是一个请求可以包含多个步骤其实你可以认为就是多次的一个什么微幅的调用每次调都拥有自己的一个什么呀对SPID对于我们来说最最重要的就是这两个ID我们结合这个图再给大家说一说
[07:46] 你看这是不是发起了一次性求对吧一次性求我们这里边包含了几次调用三次调用这个箭头到1这这是一次调用1到2这是一次调用2到3这是一次调用三次调用因此整个调用链当中有一个trace id然后有三个什么span id你看这是一次调用有一个span id这是一次调用有一个span id这是一次调用有一个span id这三个span id只是不一样但是整个span id
[08:15] 它都只有一个什么呀Trace ID这个Trace ID的值是什么呀一样的这是它们之间的关系那有时候这一次请求包含了三次的这个什么呀对微服务调用整个调用链有一个Trace ID一共有三个什么呀对Span ID你再回到我们的控制台你看看啊你看这是Demo 1这边你看它这个Trace ID是9AED
[08:40] 这是9 ad 你再看demo2这边是不是也是什么呀9 ad因为他们是属于一次请求嘛所以这个tree id是一样的但你再看这个spot id这是第一次调你看这是第二次调然后这是什么呀第三次调你会发现每次调这个spot id的值都是什么不一样哎这是这两id非常非常重要一定要搞明白了啊然后还有最后一个值是不是就是这个什么trufrance对吧他是干啥的呢这个呢大家目前先不用管我们一会会演示啊
[09:10] 这个呢是一个不二类型的一个取之对吧它是用来决定是否要将这个日志信息输出到像Z King对吧这样的追踪服务端来进行这个什么呀信息收集和展示的咱目前是不是还没有讲到这个什么呀Z King说咱这个值目前是默认就是什么呀False那False的意思就是这个Sluth收集到的这个信息它就直接以日志的行用传闻版吧我就输出来你分析这个日志就行了
[09:39] 那将来的话我们一结合这个什么ZKING你会发现这个值就不是FORCE而是什么呀初有表示这些日志信息就是你看到的控制台的这些日志信息它会上传给谁或者输出给谁对输出给ZKINGZKING收集到这些信息之后就会用图形化的方式给我们进行一个展示这块咱一会儿再讲那咱目前这一块在讲SLOOSE的时候你一定要注意我们在分析控制台日志的时候就是看这两个ID一个是TRACE ID一个是什么呀
[10:07] 对spy id我们通过分析这些id基本上就能得到一些什么呀一些信息当然这些信息呢都是这个呃什么呀服务调用链路啊链路追踪吧相关的一些信息当然我们前面提到我这种日志是纯文本我们分析起来或观察起来是不都不方便所以说啊这个日志呢你大概知道这里边哎他都是什么含义就行了最终啊我们一会儿是一定要结合谁啊zking啊把这些
[10:37] 纯文本的日日信息给他用什么呀图形化的方式给他展示出来这目前吧咱们把Sluice这个入门案例啊给他测试通过然后把日日里边包含的这些信息都是什么意思啊给他做了一个解释

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Cloud Sleuth 实现微服务间的链路追踪，并通过浏览器访问接口查看调用链路。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `package com.theima.msa.sleuthdemo1;` 和 `import ...`。
画面2：PPT页面，标题为“5. Controller类”，展示 `TestController` 类代码，其中包含 `@Autowired private RestTemplate restTemplate;`，`@GetMapping("service1")`，`log.info("sleuth1_service");`，`String sleuth1_service2 = restTemplate.getForObject("http://localhost:58011/sleuth1/service2", String.class);`，`return "sleuth1_service2";`。
画面3：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service2")`，`public String node2(){ log.info("sleuth1_service2"); return "sleuth1_service2"; }`。
画面4：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service2")`，`public String node2(){ log.info("sleuth1_service2"); return "sleuth1_service2"; }`，下方终端显示启动日志。
画面5：PPT页面，标题为“2.2.3 功能测试”，展示通过浏览器访问 `http://localhost:58011/sleuth1/service1` 得到的输出 `sleuth1_service1--->sleuth2_service1--->sleuth1_service2`，并说明日志格式。
画面6：浏览器页面，显示访问 `http://localhost:58011/sleuth1/service1` 后的输出 `sleuth1_service1--->sleuth2_service1--->sleuth1_service2`。
画面7：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service1")`，`public String node1(){ log.info("Sleuth1_Service1"); String sleuth1_service2 = restTemplate.getForObject("http://localhost:58012/sleuth2/service2", String.class); return "sleuth1_service2--->" + sleuth1_service2; }`。
画面8：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service2")`，`public String node2(){ log.info("sleuth1_service2"); return "sleuth1_service2"; }`。
画面9：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service2")`，`public String node2(){ log.info("sleuth1_service2"); return "sleuth1_service2"; }`，下方终端显示启动日志。
画面10：PPT页面，标题为“2.2.3 功能测试”，展示通过浏览器访问 `http://localhost:58021/Service-a/service1` 得到的输出 `Service-a-service1--->Service-b-service1--->Service-a-service2`，并说明日志格式。
画面11：PPT页面，标题为“2.2.1 案例简介”，展示创建两个微服务并通过 RestTemplate 实现调用的架构图，图中“前端请求”指向“微服务A”，“微服务A”指向“微服务B”，“微服务B”指向“微服务A”。
画面12：PPT页面，标题为“2.2.2 功能实现”，展示“2.2.1 微服务A”部分，内容为“1. 新建一个名为 SleuthDemo1 的 Maven 工程”和“2. 引入依赖”，并显示 `<parent>` 和 `<dependency>` 配置。
画面13：PPT页面，标题为“3. Zipkin”，展示日志格式说明，内容为“applicationName, traceId, spanId, export”。
画面14：PPT页面，标题为“3. Zipkin”，展示日志格式说明，内容为“applicationName, traceId, spanId, export”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public class TestController {
    @Autowired
    private RestTemplate restTemplate;
    @GetMapping("service1")
    public String node1(){
        log.info("sleuth1_service");
        String sleuth1_service2 = restTemplate.getForObject("http://localhost:58011/sleuth1/service2", String.class);
        return "sleuth1_service2";
    }
}
```
画面3：
```java
@GetMapping("service2")
public String node2(){
    log.info("sleuth1_service2");
    return "sleuth1_service2";
}
```
画面7：
```java
@GetMapping("service1")
public String node1(){
    log.info("Sleuth1_Service1");
    String sleuth1_service2 = restTemplate.getForObject("http://localhost:58012/sleuth2/service2", String.class);
    return "sleuth1_service2--->" + sleuth1_service2;
}
```
画面12：
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.0.RELEASE</version>
</parent>
```
画面12：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面11：
标题：2.2.1 案例简介
架构图：
- “前端请求” → “微服务A”
- “微服务A” → “微服务B”
- “微服务B” → “微服务A”

画面12：
标题：2.2.2 功能实现
内容：
- 2.2.1 微服务A
  - 1. 新建一个名为 SleuthDemo1 的 Maven 工程
  - 2. 引入依赖

画面13：
标题：3. Zipkin
内容：
- 上图中的红框内容是在引入 Sleuth 之后多出来的日志，日志的格式为：`applicationName, traceId, spanId, export`
- applicationName：应用的名称，也就是 application.properties 中的 spring.application.name 属性的值。
- traceId：一个请求的 ID，用来标识一条请求链路。
- spanId：表示一个基本的工作单元，一个请求可以包含多个步骤，每个步骤都有自己的 spanId。
- export：布尔类型，表示是否要将该信息输出到类似 Zipkin 这样的运维服务进行收集和展示。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

