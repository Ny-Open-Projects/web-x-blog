# 画面线理解：17.Sentinel入门案例-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-3 Sentinel的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-3 Sentinel的理解和使用\17.Sentinel入门案例-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:29, 00:55, 01:13, 01:58, 02:25, 02:35, 02:42, 03:16, 03:42, 03:48, 04:13, 05:34, 05:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:15:07

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
  server.servlet.context-path=/sentinel
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
- PPT 内容：通过浏览器访问 `http://localhost:90000/sentinel/hello`，慢速刷新则持续显示 “Hello Sentinel”，快速刷新则交替出现 “Hello Sentinel” 与 “系统繁忙，请稍候”，说明对 hello 资源限流成功。还可以通过查看日志获取限流详情，日志文件的位置可以在控制台找到（图中红框处）。

画面 11:
- 控制台日志：显示应用启动成功，端口 90000 已启动。
- 控制台日志：显示 Spring Boot 版本为 2.1.3.RELEASE。

画面 12:
- 文件夹：`csp` 文件夹下的日志文件列表，包括 `SentinelDemo-metrics.log`、`sentinel-dashboard-metrics.log`、`sentinel-record.log` 等。

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
server.servlet.context-path=/sentinel
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
- PPT 内容：通过浏览器访问 `http://localhost:90000/sentinel/h
