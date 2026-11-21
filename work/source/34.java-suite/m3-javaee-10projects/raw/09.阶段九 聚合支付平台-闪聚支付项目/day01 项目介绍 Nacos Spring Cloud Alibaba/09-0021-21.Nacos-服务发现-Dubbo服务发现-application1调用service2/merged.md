# 21.Nacos-服务发现-Dubbo服务发现-application1调用service2

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\21.Nacos-服务发现-Dubbo服务发现-application1调用service2【海量资源尽在 666java.com】.mp4
- 时长 5分32秒（音频 332s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们实现application调用service2根据我们double服务的架构我们看到application它是不是需要去调用我们的service2这个微服务的对吧所以这里边呢我们来看我们是需要怎么做呀我们需要实现application来调用我们的service2微服务那怎么做呢那么我们刚才说到我们准备把我们原来做服务发现测试的这个
[00:29] 有一个工程叫做什么呀Necros RESTful Consumer作为Oplication那我们如果想要调用我们的Service2怎么做呢我们首先呀你是不是需要引入Service2的依赖呀对不对因为我们是不是已经把这个Service2把它拆分成两个工程一个API一个Server对吧好那这时候它的接口是不是就被这个Consumer工程引进来了对吧那引进来之后呢
[00:59] 他要调用他怎么调呢他要调用的时候他是不是基于double协议去调用对不对所以这里边你不光要引这个他的接口你还要引什么对你还要引这个double的依赖包注意啊就是你要以double协议方式去调用所以你要引double的这个依赖包OK那引进来之后各位你要进行远程调用怎么做
[01:27] 其实我们说double是基于RPC的远程方法调用那么其实就像调用本地方法一样去调用远程方法它的实现起来特别简单但是工作原理一会我给大家讲一下注意看首先这里边我们要实现远程调用的话你是不是需要把什么把刚才你引进来的service2它这个接口给注进来对不对注有哪个注进来autowire吗
[01:57] 不是啊注意这里边我们用用一个注解就是double框架给我们提供的叫reference对这个注解这个reference这个注解它的作用是干嘛呢对它的作用就是把这个接口把这个你因为你注进来是基于什么基于service2看好啊基于service2这个接口是不是就注进来了那它这个注解的作用呢其实就是把这个接口
[02:27] 住进来然后呢生成客户端的这个什么代理对象就是生成这个接口的代理对象而这个代理对象它实现的过程就是实现远程调用一会我们可以跟踪一下代码所以这时候呢我们只要把它住进来之后其实注意看这里边我们就可以实现什么我们就可以实现整个的这个什么远程调用了看好对边service2service2看好我要进行远程调用怎么调用我要调谁
[02:57] 我是不是要调用这个service2对不对所以这里边你要注意看我们要远程调用service2那远程调用service2我们说它是一个基于RPC的框架所以它相当于跟调用本地方法一样来调用就这么简单所以这里边拼装一下这就调用好了是不是这就调用到了一个什么这就调用到了一个
[03:25] service2的方法然后最终是不是就返回了一个结果对吧返回一个结果我们可以打印一些我们跟讲义保持一致叫consumer double invoke我们就可以打印出这么一个字符串最后这个字符串后边是不是拼接了方法说返回的结果这个方法返回的结果是不是返回一个double service2这个结果一会我们测试就注意好它的工作的原理是什么呢因为这个reference这个注解
[03:54] 它会把什么基于这个接口生成代理对象而这个代理对象内幕呢它就会干嘛进行远程的RPC调用好现在呢我们就把这个实现就写好了写好了之后呢我们是不是就可以干嘛哎我们就把这个consumer干嘛重启一下重启一下之后呢我们是不是就可以来测试service2的这个地址看看它是否进行什么远程调用嗯好那现在呢我们在这打一个断点
[04:23] 注意看啊我们打一个断点那么我们需要去刷新一下它的这个service2的这个URL回车注意断点进来进来之后注意看啊注意看现在呢在这个我们的这个客户端子对吧注意看它是不是就是一个什么代理对象对不对它是不是就是一个代理对象那么这个代理对象是double框架给我们生成的它呢就会实现远程调用对吧它会实现远程调用
[04:52] 那它实现的远程调用最后结果你看它是不是拿到了service2给我们返回的这步传这就是整个调用double服务的一个过程好我们总结一下整个的service1就是obligation1调用service2的过程首先引入要调用double的接口其次要通过double去调用那么我们要引入double的包然后我们需要采用double框架给我们提供的reference注解然后
[05:21] 对接口生成代理对象然后使用这个接口代理对象来完成远程调用以上就是我们实现了Oplication1调用Service2的整个过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Nacos 服务发现与配置管理环境下，通过 Dubbo 实现 application1 调用 service2 的远程服务调用。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程文档中“2.4.4 application1调用service2”章节，说明将 Nacos-RESTful-consumer 作为 application1，实现对 service2 的调用。
画面2: 在 IntelliJ IDEA 中打开 Nacos-RESTful-consumer 项目，展示 pom.xml 文件内容，其中包含 <dependency> 标签引用 service2-api。
画面3: 在 IDEA 中选中 Nacos-RESTful-consumer 项目，展示其目录结构。
画面4: 在 IDEA 中展示 pom.xml 文件，其中包含 <dependency> 标签引用 spring-cloud-starter-dubbo。
画面5: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service1") 和 RestTemplate restTemplate = new RestTemplate();。
画面6: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service1") 和 RestTemplate restTemplate = new RestTemplate();。
画面7: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service1") 和 RestTemplate restTemplate = new RestTemplate();。
画面8: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service2") 和 service2Api.dubboService();。
画面9: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service2") 和 service2Api.dubboService();。
画面10: 在 IDEA 中展示 application.yml 文件，位于 resources 目录下。
画面11: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service2") 和 service2Api.dubboService();。
画面12: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service2") 和 service2Api.dubboService();。
画面13: 展示课程文档中“2.4.4.2 实现远程调用”章节，通过架构图说明服务发现和负载均衡的问题。
画面14: 展示课程文档中“Nacos - 服务发现和配置管理”章节，列出教学目标。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
<dependency>
    <groupId>com.itheima.Nacos</groupId>
    <artifactId>service2-api</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>

画面4:
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-Nacos-discovery</artifactId>
</dependency>

画面5:
@GetMapping(value = "/service1")
public String service1() {
    //远程调用
    RestTemplate restTemplate = new RestTemplate();
    //发现一个地址
    ServiceInstance serviceInstance = loadBalancerClient.choose(serviceId);
    //获取一个http://开头的地址，包括ip和端口
    URI uri = serviceInstance.getUri();
    String result = restTemplate.getForObject(uri + "/Service", String.class);
    return "consumer invoke:" + result;
}

画面8:
@GetMapping(value = "/service2")
public String service2() {
    //远程调用service2
    service2Api.dubboService();
    return "consumer dubbo invoke " + providerResult;
}

画面10:
application.yml

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13:
架构图：
Service A → Service B 实例1
Service A → Service B 实例2
Service B 实例1 → 动态增加实例，增加 Service B 实例2
Service B 实例2 → 动态增加实例，增加 Service B 实例1

5) 不要评价画面美观，不要输出与课程无关的内容。

