# 画面线理解：20.Sentinel动态规则

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-3 Sentinel的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-3 Sentinel的理解和使用\20.Sentinel动态规则_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:20, 00:37, 00:51, 01:14, 01:51, 02:44, 03:29, 03:37, 04:03, 04:37, 05:07, 05:47, 06:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:16:43

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过 Sentinel 控制台和 Apollo 配置中心动态管理限流规则。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，展示 TestService.java 文件中 initFlowRules() 方法的代码，用于定义一个 QPS 为 2 的限流规则，资源名为 "hello"。代码中注释说明“测试限流规则”和“加载限流规则，使其生效”。
画面 2: 同画面 1，但光标位置在 rule.setCount(2); 行，强调设置 QPS 为 2。
画面 3: 同画面 1，光标在 rule.setResource("hello"); 行，强调资源名。
画面 4: 同画面 1，光标在 rule.setResource("hello"); 行，强调资源名。
画面 5: 同画面 1，光标在 rule.setResource("hello"); 行，强调资源名。
画面 6: 展示 PPT 页面，标题为“2.3.3 动态规则”，内容说明通过 Dashboard 手动设置规则不够灵活，官方推荐通过 DataSource 接口实现动态规则管理。
画面 7: 展示 Sentinel 控制台界面，显示“SentinelDemo”应用的限流规则，资源名为 "hello"，QPS 为 2，效果为“单机”，并有“编辑”和“删除”按钮。
画面 8: 展示多窗口界面，包括 IntelliJ IDEA、Sentinel 控制台、Apollo 配置中心和 PowerShell，说明动态规则的实现涉及多个组件。
画面 9: 同画面 1，光标在 rule.setCount(2); 行，强调设置 QPS 为 2。
画面 10: 展示 Sentinel 控制台的“新增流控规则”弹窗，包含“资源名”、“针对来源”、“阈值类型”、“阈值”等字段。
画面 11: 展示 PPT 页面，标题为“达生演示如何使用 Apollo 配置中心”，内容说明 Sentinel 可以通过 Apollo 作为规则配置数据源，并展示相关依赖和代码示例。
画面 12: 展示 Apollo 配置中心的“application”配置页面，其中配置了多个路由规则，如 zull.routes.account-service.path = /account/**。
画面 13: 同画面 11，展示 PPT 页面，内容说明 Sentinel 与 Apollo 的集成方式。
画面 14: 同画面 13，展示 PPT 页面，内容说明 Sentinel 与 Apollo 的集成方式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
List<FlowRule> rules=new ArrayList<>();
//测试限流规则
FlowRule rule=new FlowRule();
rule.setResource("hello");
rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
rule.setCount(2);
rules.add(rule);
//加载限流规则，使其生效
FlowRuleManager.loadRules(rules);
```

画面 6:
```text
2.3.3 动态规则

前面不管是通过java代码还是通过Dashboard的方式去设置限流规则，都属于手动方式，不够灵活。这种方式一般仅用于测试和演示，生产环境上一般通过动态规则的方式来动态管理限流规则。也就是说，很多时候限流规则会被存储在文件、数据库或者配置中心当中。Sentinel的DataSource接口提供了对接任意配置源的能力。

官方推荐通过控制台设置规则后将规则推送到统一的规则中心，客户端实现 ReadableDataSource 接口监听规则中心实时获取变更，流程如下：
```

画面 11:
```xml
<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-datasource-apollo</artifactId>
    <version>1.6.2</version>
</dependency>
```

```java
// namespaceName 对应Apollo的命名空间名称
// ruleKey 对应规则存储的key
// defaultRules 对应连接不上Apollo时的默认规则
ReadableDataSource<String, List<FlowRule>> flowRuledataSource = new ApolloDataSource<>(namespaceName, ruleKey, defaultRules, source -> {
    return JSON.parseObject(source, new TypeReference<List<FlowRule>>() {});
});
FlowRuleManager.registerProperty(flowRuledataSource.getProperty());
```

画面 12:
```properties
zull.routes.account-service.stripPrefix = false
zull.routes.account-service.path = /account/**
zull.routes.consumer-service.stripPrefix = false
zull.routes.consumer-service.path = /consumer/**
zull.routes.transaction-service.stripPrefix = false
zull.routes.transaction-service.path = /transaction/**
zull.routes.repayment-service.stripPrefix = false
zull.routes.repayment-service.path = /repayment/**
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6:
标题：2.3.3 动态规则
内容：说明动态规则的必要性，推荐通过 DataSource 接口实现动态规则管理。

画面 11:
标题：达生演示如何使用 Apollo 配置中心
内容：说明 Sentinel 与 Apollo 的集成方式，展示依赖和代码示例。

画面 12:
标题：Apollo 配置中心
内容：展示路由规则配置，如 zull.routes.account-service.path = /account/**。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
