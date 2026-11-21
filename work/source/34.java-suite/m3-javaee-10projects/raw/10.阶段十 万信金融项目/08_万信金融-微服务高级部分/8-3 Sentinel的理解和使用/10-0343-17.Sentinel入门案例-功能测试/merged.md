# 17.Sentinel入门案例-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-3 Sentinel的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-3 Sentinel的理解和使用\17.Sentinel入门案例-功能测试_【海量资源尽在 666java.com】.mp4
- 时长 5分50秒（音频 350s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们一起把Sentinel入门案例给编写完毕了接下来我们就可以进行对功能测试了那怎么测试呢我们是不是通过浏览器要往这个微服上发请求具体是不是应该是往Controller的这个什么呀哈喽这儿是发请求你往这儿发请求它就会触发去调用业务层的这个什么呀哈喽方法而咱这个哈喽方法是不是已经被定义成受保护的资源了
[00:29] 而且我们也为他定义了这个限流规则就是一秒钟最多调用什么呀两次是不是那咱接下来就进行测试我先把这个微幅给他启动起来启动一下我们观察控制台有没有报错啊没有报错的话接下来就通过浏览器是不是开始发请求了没有报错对吧端口号59000然后呢反而路径的话首先是不是要要要要填这个基本反而路径然后就是这个谁呀哈喽是不是
[01:02] 那咱剪辑里边有这个路径啊你看就这个路径我直接点一下就发警团了啊你看页面上是不是展示什么哈喽森体呢这个值是从哪来的这个值多简单啊我们现在是不是往这发警团了然后他去调右层的这个什么呀哈喽发右层的哈喽发返回的就是什么呀哈喽森体呢最终是不是就展示到页面上这个单位没问题吧对没问题那我怎么看出来他能不能进行限流呢哎这时候你要注意看了啊
[01:32] 因为咱这是一个demo我只能人工的在这刷新我们的规则是不是一秒钟最多干什么呀只允许调用两次这个哈喽方法对不对那你看我接下来先慢一点走刷新再刷新我这一秒钟也就一次了是不是很慢是吧哎这是不是一直展示的是什么呀哈喽森体那如果我快点就刷新的快点我这刷新的越快那理论来讲那调用这个什么呀
[02:01] 卡牢方法的次数是不是就越快或者越多对不对有可能是不是就会超过这个什么呀我们的这个规则那这个时候咱看看它有啥变化没有我就快速的进行刷新了有变化吗刚才你看到了吧有没有变化是不是把系统繁忙请稍后给展示出来为什么会展示出来这个东西呢这时候你要注意看看刚才写的这个代码由于呢我是人工的这个快速的进行刷新所以说它很快是不是就会这个什么呀
[02:36] 是不是超出这个规则的这个限制呢就是每秒钟两次那一旦超出的话它就会对这个方法进行什么呀限流进行保护那一旦限流的话我们刚才说了这就是用来设置限流后的这个什么呀对后续处理的不就是对上这个方法然后返回来一个系统繁忙请稍后你在这是不是就看到它了那你在页面看到这个东西就证明证明限流是不是已经出现了对不对就对这个海洋方法进行了这个什么呀
[03:06] 这个效果就已经出来了如果没有进行限流的话我们在页面上是不是应该正常看到这个部分对不对那我们现在看到这个东西就证明Centino对它进行什么呀对这个方案进行什么呀进行限流了然后才出现了这个什么呀后续的这个什么呀对这个处理或者这个动作所以我们通过这儿呢其实就已经观察出来这个限流的这个什么呀这个效果
[03:31] 另外呢这个Centino呢它还有一个什么日志文件它在日志文件里边呢也记录了一些这个限流的一些什么呀详情那这个日志文件在哪呢我们可以通过这个地方找到的就是控制台控制台呢我们在启动的时候在这你看它这是不是打印了一个路径啊这个路径呢其实就是Centino的日志文件的这个路径我们可以访问一下这里我们找一找它的日志文件
[04:06] 哪个日文件呢我们要看的就是这个日文件Centino Demo然后后边是不是有这个日期的对不对我们打开打开之后呢你看这里边是不是有什么时间戳啊有具体的年日时分秒对吧有这个什么呀有这个受保护的资源的这个什么呀名字然后后边这一堆数字这是干嘛我们就看不懂什么1010什么样15对吧000这都什么玩意儿大家注意了这一堆数字里边其实每个数字都是有意义的
[04:39] 有的数字表示这个通过的次数有的数字表示什么呀对有的数字表示被拒绝的次数总之吧他们都是有含义的但是有的学员会说老师这这个谁能记得住啊这一堆数字我也分不清是谁是谁是干嘛的对不对那这个日文念不需要大家去看啊我们说这纯文本的东西这个观察起来很不方便是吧很麻烦啊这个日文念呢我只是打开让大家看一眼就行了啊那至于这里边啊
[05:10] 这些数字都是干啥的对不对我们说了这叫限流的什么呀详情但是你不用管它我们一会儿呢会有一个图形化的控制台图形化的控制台这个控制台呢会把这些纯文本的数据给你转换成什么呀图形化的这个什么呀界面给你展示出来非常的这个什么呀这个直观我们前面不是也提到过吗这个Sentino它也是有这个什么呀
[05:36] 对dashboard就是有图形化的这个控制台的一会呢咱就给大家演示是目前吧我们就把这个谁啊对Centino的这个入门案例呢就给大家测试通过了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成并配置 Sentinel 流量控制，包括定义限流规则、配置应用属性以及查看限流日志。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 代码：在 `TestController.java` 中定义了 `@GetMapping("hello")` 的接口和 `@ExceptionHandler` 的异常处理方法。
- 代码：在 `TestService.java` 中定义了 `@Service` 和 `@SentinelResource` 注解的 `hello` 方法。
- 代码：在 `SentinelDemoApplication.java` 中定义了 `@PostConstruct` 初始化限流规则的方法 `initFlowRules()`，其中创建了 `FlowRule` 并设置资源名、限流策略和阈值。

画面 2:
- 代码：在 `TestController.java` 中，`@GetMapping("hello")` 方法被高亮选中。
- 代码：在 `TestService.java` 中，`@SentinelResource` 注解的 `hello` 方法被高亮选中。

画面 3:
- 配置：`application.properties` 文件内容：
  ```
  spring.application.name=SentinelDemo
  server.port=90000
  server.servlet.context-path=/Sentinel
  ```

画面 4:
- 代码：在 `TestController.java` 中，`@GetMapping("hello")` 方法被高亮选中。
- 控制台日志：显示应用启动成功，端口 90000 已启动。

画面 5:
- 代码：在 `TestService.java` 中，`@SentinelResource` 注解的 `hello` 方法被高亮选中。
- 控制台日志：显示应用启动成功，端口 90000 已启动。

画面 6:
- 代码：在 `TestController.java` 中，`@GetMapping("hello")` 方法被高亮选中。
- 代码：在 `TestService.java` 中，`@SentinelResource` 注解的 `hello` 方法被高亮选中。
- 代码：在 `SentinelDemoApplication.java` 中，`initFlowRules()` 方法中的 `rule.setCount(2)` 被高亮选中。

画面 7:
- 代码：在 `SentinelDemoApplication.java` 中，`initFlowRules()` 方法中的 `rule.setCount(2)` 被高亮选中。
- 代码：在 `TestService.java` 中，`@SentinelResource` 注解的 `hello` 方法被高亮选中。

画面 8:
- 代码：在 `TestService.java` 中，`@SentinelResource` 注解的 `hello` 方法被高亮选中。
- 代码：在 `SentinelDemoApplication.java` 中，`initFlowRules()` 方法中的 `rule.setCount(2)` 被高亮选中。

画面 9:
- 代码：在 `TestService.java` 中，`@SentinelResource` 注解的 `hello` 方法被高亮选中。
- 代码：在 `SentinelDemoApplication.java` 中，`initFlowRules()` 方法中的 `rule.setCount(2)` 被高亮选中。

画面 10:
- PPT 标题：6. 功能测试
- PPT 内容：通过浏览器访问 `http://localhost:90000/Sentinel/hello`，慢速刷新则持续显示 “Hello Sentinel”，快速刷新则交替出现 “Hello Sentinel” 与 “系统繁忙，请稍候”，说明对 hello 资源限流成功。还可以通过查看日志获取限流详情，日志文件的位置可以在控制台找到（图中红框处）。

画面 11:
- 控制台日志：显示应用启动成功，端口 90000 已启动。
- 控制台日志：显示 Spring Boot 版本为 2.1.3.RELEASE。

画面 12:
- 文件夹：`csp` 文件夹下的日志文件列表，包括 `SentinelDemo-metrics.log`、`Sentinel-dashboard-metrics.log`、`Sentinel-record.log` 等。

画面 13:
- PPT 标题：1.2 Sentinel简介
- PPT 内容：Sentinel 介绍，包括其发展历程（2012 年诞生，2017 年成为基础技术，2018 年开源）、应用场景（如秒杀、实时监控、广泛生态）。

画面 14:
- 代码：在 `TestService.java` 中，`@SentinelResource` 注解的 `hello` 方法被高亮选中。
- 代码：在 `SentinelDemoApplication.java` 中，`initFlowRules()` 方法中的 `rule.setCount(2)` 被高亮选中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 3:
```
spring.application.name=SentinelDemo
server.port=90000
server.servlet.context-path=/Sentinel
```

画面 6:
```
public class TestService {
    @SentinelResource(value = "hello", blockHandler = "exceptionHandler")
    public String hello() {
        return "Hello Sentinel";
    }

    public String exceptionHandler(BlcokException ex) {
        ex.printStackTrace();
        return "系统繁忙，请稍候";
    }

    @PostConstruct
    public void initFlowRules() {
        List<FlowRule> rules=new ArrayList<>();
        //设置限流规则
        FlowRule rule=new FlowRule();
        rule.setResource("hello");
        rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
        rule.setCount(2);
        rules.add(rule);
        //加载限流规则，使其启用
        FlowRuleManager.loadRules(rules);
    }
}
```

画面 7:
```
public class TestService {
    @SentinelResource(value = "hello", blockHandler = "exceptionHandler")
    public String hello() {
        return "Hello Sentinel";
    }

    public String exceptionHandler(BlcokException ex) {
        ex.printStackTrace();
        return "系统繁忙，请稍候";
    }

    @PostConstruct
    public void initFlowRules() {
        List<FlowRule> rules=new ArrayList<>();
        //设置限流规则
        FlowRule rule=new FlowRule();
        rule.setResource("hello");
        rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
        rule.setCount(2);
        rules.add(rule);
        //加载限流规则，使其启用
        FlowRuleManager.loadRules(rules);
    }
}
```

画面 8:
```
public class TestService {
    @SentinelResource(value = "hello", blockHandler = "exceptionHandler")
    public String hello() {
        return "Hello Sentinel";
    }

    public String exceptionHandler(BlcokException ex) {
        ex.printStackTrace();
        return "系统繁忙，请稍候";
    }

    @PostConstruct
    public void initFlowRules() {
        List<FlowRule> rules=new ArrayList<>();
        //设置限流规则
        FlowRule rule=new FlowRule();
        rule.setResource("hello");
        rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
        rule.setCount(2);
        rules.add(rule);
        //加载限流规则，使其启用
        FlowRuleManager.loadRules(rules);
    }
}
```

画面 9:
```
public class TestService {
    @SentinelResource(value = "hello", blockHandler = "exceptionHandler")
    public String hello() {
        return "Hello Sentinel";
    }

    public String exceptionHandler(BlcokException ex) {
        ex.printStackTrace();
        return "系统繁忙，请稍候";
    }

    @PostConstruct
    public void initFlowRules() {
        List<FlowRule> rules=new ArrayList<>();
        //设置限流规则
        FlowRule rule=new FlowRule();
        rule.setResource("hello");
        rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
        rule.setCount(2);
        rules.add(rule);
        //加载限流规则，使其启用
        FlowRuleManager.loadRules(rules);
    }
}
```

画面 14:
```
public class TestService {
    @SentinelResource(value = "hello", blockHandler = "exceptionHandler")
    public String hello() {
        return "Hello Sentinel";
    }

    public String exceptionHandler(BlcokException ex) {
        ex.printStackTrace();
        return "系统繁忙，请稍候";
    }

    @PostConstruct
    public void initFlowRules() {
        List<FlowRule> rules=new ArrayList<>();
        //设置限流规则
        FlowRule rule=new FlowRule();
        rule.setResource("hello");
        rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
        rule.setCount(2);
        rules.add(rule);
        //加载限流规则，使其启用
        FlowRuleManager.loadRules(rules);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 10:
- PPT 标题：6. 功能测试
- PPT 内容：通过浏览器访问 `http://localhost:90000/Sentinel/h

