# 画面线理解：16.Sentinel入门案例

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-3 Sentinel的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-3 Sentinel的理解和使用\16.Sentinel入门案例_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 02:51, 03:51, 04:44, 05:15, 05:50, 08:19, 10:01, 10:43, 12:45, 13:46, 15:26, 16:12, 17:36, 18:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:14:17

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Sentinel 实现流量控制，包括创建项目、引入依赖、编写代码定义资源和配置限流规则。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 第 2 页“快速入门”，说明使用 Sentinel 实现流控的三个步骤：定义资源、定义规则、检验规则是否生效。列出 Sentinel 支持的主流框架：Web Servlet、Dubbo、Spring Boot / Spring Cloud、Spring WebFlux、gRPC。
画面 2: 在 IntelliJ IDEA 中展示 TestController.java 代码，包含 @RestController、@GetMapping、@Autowired 注解，以及一个返回 "hello" 的方法。
画面 3: 展示 PPT 第 3 页“2.1 入门案例”，内容为创建 Maven 工程和引入依赖的说明。同时展示 TestService.java 代码，其中包含 @SentinelResource 注解和 exceptionHandler 方法。
画面 4: 在 IntelliJ IDEA 中展示 TestService.java 代码，其中方法返回 "Hello Sentinel"。
画面 5: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于方法名 "hello" 上。
画面 6: 展示 PPT 第 3 页“2.1 入门案例”的内容，同时在 IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 7: 展示 PPT 第 3 页“2.1 入门案例”，内容为创建 Maven 工程和引入依赖的说明。同时展示 TestService.java 代码，光标位于 @SentinelResource 注解的 value 属性。
画面 8: 展示 PPT 第 3 页“2.1 入门案例”，内容为创建 Maven 工程和引入依赖的说明。同时展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 9: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 10: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 11: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 12: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 13: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 14: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
控制台（Dashboard）基于 Spring Boot 开发，打包后可以直接运行，不需要额外的 Tomcat 等
应用容器。
2 快速入门
使用 Sentinel 来实现流控，主要分为几个步骤：
1. 定义资源，这里的资源可以是任何东西，例如某个服务，某个服务里的方法，甚至是一段代码。
2. 定义规则，指的是流量控制规则
3. 检验规则是否生效
先把可能需要保护的资源定义好，之后再配置规则。也可以理解为，只要有了资源，我们就可以在任何
时候灵活地定义各种流量控制规则。在编码的时候，只需要考虑这个代码是否需要保护，如果需要保护，
就将之定义为一个资源。
对于主流框架，Sentinel 都提供了适配，只需要按照适配中的说明配置，Sentinel 就会默认支持提供的
服务，方法等为资源。Sentinel 支持的主流框架适配列表如下：
• Web Servlet
• Dubbo
• Spring Boot / Spring Cloud
• Spring WebFlux
• gRPC
```

画面 2:
```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {
    @Autowired
    private TestService testService

    @GetMapping("hello")
    public String hello() { return testService.hello(); }
}
```

画面 3:
```
@SentinelResource(value = "hello",blockHandler = "exceptionHandler")
public String hello() {
    return "hello sentinel";
}

public String exceptionHandler(BlockException ex){
    ex.printStackTrace();
    return "系统繁忙，请稍候";
}

@PostConstruct
public void initFlowRules(){
    List<FlowRule> rules=new ArrayList<>();
    //创建FlowRule对象封装限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
    rules.add(rule);
}
```

画面 4:
```
public String hello() {
    return "Hello Sentinel";
}
```

画面 5:
```
public String hello() {
    return "Hello Sentinel";
}
```

画面 6:
```
@SentinelResource(value = "hello",blockHandler = "exceptionHandler")
public String hello() {
    return "hello sentinel";
}

public String exceptionHandler(BlockException ex){
    ex.printStackTrace();
    return "系统繁忙，请稍候";
}

@PostConstruct
public void initFlowRules(){
    List<FlowRule> rules=new ArrayList<>();
    //创建FlowRule对象封装限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
    rules.add(rule);
}
```

画面 7:
```
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
</parent>

<groupId>com.itheima.msa.sentinel</groupId>
<artifactId>sentinel-demo</artifactId>
<version>0.0.1-SNAPSHOT</version>
<name>sentinel-demo</name>

<properties>
    <java.version>1.8</java.version>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
</properties>
```

画面 8:
```
@SentinelResource(value = "hello",blockHandler = "exceptionHandler")
public String hello() {
    return "hello sentinel";
}

public String exceptionHandler(BlockException ex){
    ex.printStackTrace();
    return "系统繁忙，请稍候";
}

@PostConstruct
public void initFlowRules(){
    List<FlowRule> rules=new ArrayList<>();
    //创建FlowRule对象封装限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
    rules.add(rule);
}
```

画面 9:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
}
```

画面 10:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
}
```

画面 11:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
}
```

画面 12:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
}
```

画面 13:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
}
```

画面 14:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
    rules.add(rule);
    //加载限流规则，作用于
    FlowRuleManager.loadRules(rules);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2 快速入门”，内容包括三个步骤：定义资源、定义规则、检验规则是否生效。列出 Sentinel 支持的主流框架。
画面 7: PPT 标题为“2.1 入门案例”，内容为创建 Maven 工程和引入依赖的说明。
画面
