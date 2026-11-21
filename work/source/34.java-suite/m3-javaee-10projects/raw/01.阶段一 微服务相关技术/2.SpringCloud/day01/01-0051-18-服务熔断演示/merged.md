# 18-服务熔断演示

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\18-服务熔断演示_【海量资源尽在 ubkz.com】.mp4
- 时长 12分4秒（音频 724s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 服务熔断演示在这一小节中我们的主要目标是了解熔断器工作原理那接下来我们打开讲义来了解服务熔断在服务熔断中使用的熔断器也叫断路器它的英文单词为Circuit Breaker熔断机制与家里使用的电路熔断原理类似当如果电路发生短路的时候能立刻熔断电路避免发生灾难那么在分布式系统中应用服务熔断后服务调用方可以自行
[00:30] 判断哪些服务反应慢或存在大量超时可以针对这些服务进行主动熔断防止整个系统被拖垮也就是说当如果真的是出现了这种反应慢或是大量的超时请求的时候我们可以对这些请求进行一个服务降级也就是及时返回一个失败的结果让它不用继续等待那么在我们的High Stress的服务熔断机制中可以实现弹性的容错
[00:58] 当服务请求情况好转之后可以自动重连具体我们来看High Stress的熔断状态机模型在这一个图中你有三个状态三个状态分别是这图里面的这一个Closed 关闭Open 打开Half Open 是半开那这个状态是怎么变化的我们来了解在我们的
[01:36] 断路器是关闭的状态情况下这些状态都描述的是断路器circuit breaker它的状态这个关闭状态时候呢所有请求都是正常访问不会被服务降级那在访问的过程中如果是有一些失败但是这个失败呢又还没有达到一个具体的法制的时候请求还是正常的服务也不会被降级那如果这些失败的请求达到了法制那么就会
[02:03] 把我们的段路器给打开那具体法值是什么法值就是服务失败达到一定的值时会将段路器打开那这个值呢具体的值是默认情况下请求次数最少不低于
[02:40] 20次失败的请求占比达到了50%也就是一半的话呢这个段路器就会被打开也就是20次请求10次以上失败就会把这个段路器给打开这一个情况这条线就是已经达到乏值失败请求达到乏值了达到乏值以后呢我们的段路器就会打开
[03:15] 打开后所有的请求全部都会进行服务降级服务降级也就是调用我们服务降级的方法提前返回这个服务失败的一个结果就当时我们在服务降级方法中指定这个返回结果内容不会一直等待那在经过一定的休眠时间就是服务既然降级了那它会有一个休眠时间我们休眠会五秒也可以修改休眠五秒
[03:47] 之后会进入一个半开状态半开状态他不是完全不能去访问服务他是允许半开状态是允许部分请求进行访问好那访问的时候呢如果是成功的话他就会将这个段落器能给关闭如果是访问的时候还是失败那么他还会保持这个段落器能是打开的状态
[04:20] 这就是我们在用这个熔断服务的时候它的一个断路器状态的变化我们把这一个记录到笔记中回到我们的讲义刚才我们在图里面说到的这几个状态其实也就是这几个关闭状态所有请求都正常访问打开状态所有请求都会被降级处理罚值刚才跟大家介绍过50%的
[04:51] 这个比例如果是失败的达到50%那么就会去打开这个段路器半开状态那它可以允许部分请求通过然后请求是健康的会关闭段路器不然的话还会持续的打开段路器让这些服务能进行降级处理那我们现在项目中也想去测试一下这个服务垄断那么以我们的服务消费工程中去配置这么一些逻辑
[05:21] 我们的逻辑就是在我们的请求方法中指定一个ID如果是1的话永远让它是失败一旦是失败的那么就会被我们的High Stress进行服务降级好那如果是其他ID又是正常的我们的测试的点就是去频繁的访问这个失败的地址导致它达到法子也就是至少来个超过10次20次让它失败进入一个熔断
[05:49] 打开的状态也就是我们的容段录器能是打开状态所有都会进行一个服务降级即使你是成功的地址就是这一条二是没有拦截的应该要正常处理但是因为你已经到达了阀值也就是段录器已经打开状态所以即使你地址是没有问题但是也会进行服务降级返回的也是这种提示信息好所以我们来去配置我们现在的项目打开idea打开处理器
[06:20] 处理器里边我们去修改它的代码如果ID是等于1的话那我们就让它报错如果报错了就会进入我们的服务降级的方法太忙了一旦报错达到了一定的法值那么它就会后面正常的请求也会进入我们的服务降级的方法也就是现在我们的代码是全局的就这个类里面只要有错或者是服务有问题那么都会到这个
[07:00] 服务降级的方法中显示的是这句话默认提示对不起网络太拥挤了好我们已经改好了改好后呢去启动我们的这个服务消费工程consumer7号以后呢我们去测试它去访问这两个至少有两个地址多个也行只要ID是等于1和不等于1之间进行一个切换测试都行好7号以后我们打开浏览器
[07:29] 去访问这个呢不是1那也就是说正常可以获取到服务的没问题那接下来呢我们用一个1的来复制一下1呢是失败的我们故意的把它返回失败好所以这个就是当如果出现失败了就到了我们的服务降级方法显示这个内容是我们预期的那现在呢因为你只有一次还不会导致我们的段落器打开所以你现在再访问呢这个是完全不受影响的那我们现在来故意的让它至少来个
[07:59] 10次20次的失败好直到呢这一个是出现了这句话也就是出现了一个服务降级好所以我们去访问他点点点点疯狂的点点点点点点点这个多少次了1234567891011121314151678910好再来刷哎还不是还不行我们再来点击一下要快速的点好点了以后呢接着我们再回到
[08:28] 刚才的这个正常的地址中再去刷新他服务现在还没有这么巧的吗再去点点点点点点点到他这个提示默认的提示信息对不起网络太拥挤为止也就是要进行一个服务降级还没有啊是不是没有直接发到我们的后台我们打开F12来让他每一次都让我们的服务器去请求刷123456789是
[09:01] 再点我们点个20次点好以后我们再来刷好出现了就是现在已经是处于我们的段落器打开状态即使刚才这个地址好的现在也已经到了我们的服务降级的方法但是如果你过一段时间也就我们现在应该是已经过了的过了5秒他现在进入半开状态他再次访问的时候因为这个服务是根本没有问题的所以在刷新他又依然是可以提供正常服务的好这就是我们的一个服务熔断的一个测试
[09:34] 那测完以后呢我们也可以去修改刚才说到那些法指我们打开讲义可以去修改它的一些配置参数那我们也去修改一下我们复制这一段这个是跟我们原来配置的这一个值是平级的excuse跟circuitbreaker这边复制一下打开配置文件excuse跟它平级好打开后呢接着大家一定要注意你看这个线
[10:13] 是没有像这个有层次感的所以这肯定有问题好所以我们把它删掉121212好这就是正常的一个配置了配好以后呢我们接着再去重启一下我们的系统如果没有错当然各自呢大家在配好以后可以自行的去测试一下这些参数那我们去试着重启一下看一下会不会有问题会不会有报错如果有同学看到说这个没有提示那很遗憾的前面跟大家说过不是在我们的
[10:48] yaml文件中的所有配置项都有提示的不一定ok所以我们不用管它你重启这一个我们配置的是一个比例值那比例值它默认就是50我们现在没有改还有一个是熔断后休眠时长默认是5秒我们现在改成是10秒它因为用的是毫秒作为单位现在启动的是没有报错的ok也就是我们的参数不影响我们刚才服务的启动还就是一个
[11:19] 最小的请求次数默认是20我们现在改成10这就是按照你要需要你自己呢自行私下的去根据这些参数测试就可以了这就是我们的一个服务熔断的测试演示我们回到我们的笔记中进行小结刚才我们配置的其实也就是这些参数我怕大家不好复制所以把它拿过来可以通过配置服务熔断参数修改默认
[11:52] 默认的配置项有这一些可以去修改好这就是我们的一个服务熔断的演示所有内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Hystrix 服务熔断机制的原理和如何在 Spring Cloud 项目中通过配置文件进行实战操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程目录结构，当前位于“8.4. 服务熔断”章节，具体为“8.4.1. 熔断原理”。
画面 2: 展示 Hystrix 熔断器的“Closed”、“Open”状态转换图，图中包含“call / raise circuit open”、“fail [threshold reached]”、“reset timeout”等转换条件。
画面 3: 展示 Hystrix 熔断器的“Half Open”状态，图中显示从“Open”状态通过“reset timeout”后进入“Half Open”，并有“success”和“fail”流向。
画面 4: 展示 Hystrix 熔断器的三种状态（Closed、Open、Half Open）的文字说明，并进入“8.4.2. 动手实践”部分。
画面 5: 展示“8.4.2. 动手实践”部分，说明需要修改的文件路径：`consumer-demo/src/main/java/com/heima/consumer/Controller/ConsumerController.java`。
画面 6: 展示在浏览器中访问 `localhost:8080/consumer/1` 和 `localhost:8080/consumer/2` 的结果，其中 `consumer/1` 返回“默认提示：对不起，网络太拥挤了！”，说明熔断器已触发。
画面 7: 展示在 IntelliJ IDEA 中打开 `ConsumerController.java` 文件，代码中包含 `@HystrixCommand` 注解和 `defaultFallback` 方法。
画面 8: 展示在 IntelliJ IDEA 中修改 `ConsumerController.java` 文件，添加 `@HystrixCommand` 注解，并在 `queryById` 方法中抛出异常。
画面 9: 展示在 IntelliJ IDEA 中修改 `ConsumerController.java` 文件，添加 `@HystrixCommand` 注解，并在 `queryById` 方法中添加 `@DefaultProperties` 注解和 `defaultFallback` 方法。
画面 10: 展示在浏览器中访问 `localhost:8080/consumer/8` 的结果，返回用户信息 JSON 数据。
画面 11: 展示在 IntelliJ IDEA 中打开 `application.yml` 文件，准备修改 Hystrix 配置。
画面 12: 展示在 IntelliJ IDEA 中修改 `application.yml` 文件，添加 Hystrix 配置项，并在控制台中查看应用启动日志。
画面 13: 展示 Typora 中的“18. 服务熔断演示”页面，包含 Hystrix 熔断器状态转换图，图中包含“关闭”、“打开”、“半开”状态及转换条件。
画面 14: 展示 Typora 中的“18. 服务熔断演示”页面，展示 Hystrix 熔断器的“Half Open”状态及配置参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 代码：
```java
public String queryById(@PathVariable Long id) {
    if (id == 1) {
        throw new RuntimeException("太忙了");
    }
    String url = "http://user-Service/user/" + id;
    String user = restTemplate.getForObject(url, String.class);
    return user;
}
```
画面 7 代码：
```java
@HystrixCommand
public String queryById(@PathVariable Long id) {
    if (id == 1) {
        throw new RuntimeException("太忙了");
    }
    String url = "http://user-Service/user/" + id;
    String user = restTemplate.getForObject(url, String.class);
    return user;
}
```
画面 8 代码：
```java
@HystrixCommand
public String queryById(@PathVariable Long id) {
    if (id == 1) {
        throw new RuntimeException("太忙了");
    }
    String url = "http://user-Service/user/" + id;
    String user = restTemplate.getForObject(url, String.class);
    return user;
}
```
画面 9 代码：
```java
@HystrixCommand
public String queryById(@PathVariable Long id) {
    if (id == 1) {
        throw new RuntimeException("太忙了");
    }
    String url = "http://user-Service/user/" + id;
    String user = restTemplate.getForObject(url, String.class);
    return user;
}
```
画面 11 配置：
```yaml
spring:
  application:
    name: consumer-demo
  cloud:
    Eureka:
      client:
        Service-url:
          defaultZone: http://127.0.0.1:10000/Eureka
      registry-fetch-interval-seconds: 10
hystrix:
  command:
    default:
      execution:
        isolation:
          Thread:
            timeoutInMilliseconds: 2000
```
画面 12 配置：
```yaml
hystrix:
  command:
    default:
      execution:
        isolation:
          Thread:
            timeoutInMilliseconds: 2000
  circuitBreaker:
    errorThresholdPercentage: 50 # 制定熔断阈值比例的配置， 默认值50%
    sleepWindowInMilliseconds: 10000 # 熔断后休眠时长， 默认值5秒
    requestVolumeThreshold: 10 # 熔断触发最小请求数， 默认值20
```
画面 13 配置：
```yaml
hystrix:
  command:
    default:
      execution:
        isolation:
          Thread:
            timeoutInMilliseconds: 2000
  circuitBreaker:
    errorThresholdPercentage: 50 # 制定熔断阈值比例的配置， 默认值50%
    sleepWindowInMilliseconds: 10000 # 熔断后休眠时长， 默认值5秒
    requestVolumeThreshold: 10 # 熔断触发最小请求数， 默认值20
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 架构图标题为“Circuit Breaker”，包含三个状态：“Closed”、“Open”、“Half Open”。从“Closed”状态出发，若“fail [threshold reached]”则指向“Open”状态；从“Open”状态出发，若“reset timeout”则指向“Closed”状态；从“Open”状态出发，若“fail”则指向“Half Open”状态；从“Half Open”状态出发，若“success”则指向“Closed”状态；从“Half Open”状态出发，若“fail”则指向“Open”状态。
画面 3: 架构图标题为“Circuit Breaker”，包含三个状态：“Closed”、“Open”、“Half Open”。从“Closed”状态出发，若“fail [under threshold]”则指向“Closed”状态；从“Closed”状态出发，若“fail [threshold reached]”则指向“Open”状态；从“Open”状态出发，若“reset timeout”则指向“Closed”状态；从“Open”状态出发，若“fail”则指向“Half Open”状态；从“Half Open”状态出发，若“success”则指向“Closed”状态；从“Half Open”状态出发，若“fail”则指向“Open”状态。
画面 13: 架构图标题为“Circuit Breaker”，包含三个状态：“关闭”、“打开”、“半开”。从“关闭”状态出发，若“fail [threshold reached]”则指向“打开”状态；从“打开”状态出发，若“reset timeout”则指向“关闭”状态；从“打开”状态出发，若“fail”则指向“半开”状态；从“半开”状态出发，若“success”则指向“关闭”状态；从“半开”状态出发，若“fail”则指向“打开”状态。
画面 14: 架构图标题为“Circuit Breaker”，包含三个状态：“关闭”、“打开”、“半开”。从“关闭”状态出发，若“fail [threshold reached]”则指向“打开”状态；从“打开”状态出发，若“reset timeout”则指向“关闭”状态；从“打开”状态出发，若“fail”则指向“半开”状态；从“半开”状态出发，若“success”则指向“关闭”状态；从“半开”状态出发，若“fail”则指向“打开”状态。

5) 不要评价画面美观，不要输出与课程无关的内容。
（以上内容已按要求输出）

