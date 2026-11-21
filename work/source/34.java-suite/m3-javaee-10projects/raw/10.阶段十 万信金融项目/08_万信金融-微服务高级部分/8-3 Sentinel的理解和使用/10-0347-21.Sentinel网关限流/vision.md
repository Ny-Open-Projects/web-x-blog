# 画面线理解：21.Sentinel网关限流

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-3 Sentinel的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-3 Sentinel的理解和使用\21.Sentinel网关限流_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:48, 00:55, 01:06, 01:09, 01:16, 01:22, 01:37, 02:07, 02:16, 02:19, 02:24, 04:02, 04:57, 05:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:17:11

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 Sentinel 实现接口限流，并展示其在万信金融 P2P 网关场景中的架构应用。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 TestService.java 中的 @SentinelResource 注解配置，用于定义限流规则和异常处理方法。
画面 2: 展示 exceptionHandler 方法，用于处理限流触发时的异常，并打印堆栈信息。
画面 3: 与画面 2 相同，光标位置略有变化。
画面 4: 展示 initFlowRules 方法，用于动态加载限流规则。
画面 5: 展示 initFlowRules 方法，光标位于规则定义处。
画面 6: 展示 hello 方法，光标位于方法名上。
画面 7: 展示 hello 方法，光标位于方法体内部。
画面 8: 展示 hello 方法，光标位于方法体内部，准备执行。
画面 9: 展示万信金融技术架构图，包含多个业务模块和数据层。
画面 10: 展示架构图中 HTTP API 接入层的 80% 流量接入比例。
画面 11: 展示架构图中 HTTP API 接入层的 90% 流量接入比例。
画面 12: 展示 PPT 标题“3 实现万信金融P2P网关限流”，并介绍 Sentinel 在网关限流中的作用。
画面 13: 展示 Sentinel 网关限流公共模块（API Gateway Adapter Common）的架构图，包含 Zuul 和 Spring Cloud Gateway 的组件。
画面 14: 展示 Sentinel 网关限流公共模块的架构图，光标位于“API 路径匹配”按钮上。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 1:
```java
@SentinelResource(value = "hello", blockHandler = "exceptionHandler")
public String hello(){
    return "Hello Sentinel";
}
```

画面 2:
```java
public String exceptionHandler(BlockException ex) {
    ex.printStackTrace();
    return "系统繁忙，请稍候";
}
```

画面 4:
```java
List<FlowRule> rules = new ArrayList<>();
//1.定义限流规则
FlowRule rule = new FlowRule();
rule.setResource("hello");
rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
rule.setCount(2);
rules.add(rule);
//2.加载限流规则，使其生效
FlowRuleManager.loadRules(rules);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 12:
标题: 3 实现万信金融P2P网关限流
正文: 万信金融P2P平台在发展过程中，吞吐量也会与日俱增，为了保证系统稳定性，需要考虑使用Sentinel进行限流。由于该平台使用HTTP网关作为系统的唯一入口，因此我们使用Sentinel 的网关限流模式。
子标题: 3.1 网关限流概述
正文: Sentinel 支持整合 Spring Cloud Gateway, Zuul 等主流的网关进行限流。Sentinel 1.6.0 引入了 Sentinel API Gateway Adapter Common 模块，此模块中包含网关限流的规则和自定义 API。整体架构如下图所示:

画面 13:
架构图:
左侧: Zuul 部分，包含 ZuulPreFilter (API 匹配)、ZuulErrorFilter (业务异常记录)、ZuulPostFilter (调用完成)，并指向“Fallback 处理”。
右侧: Spring Cloud Gateway 部分，包含 SentinelGatewayFilter (Route ID 识别、API 路径匹配)、BlockRequestHandler (限流请求处理)。
下方: Sentinel 网关限流公共模块 (API Gateway Adapter Common)，包含“请求属性解析”、“网关规则管理”、“网关规则检查”、“调用参数组装”、“自定义 API 分组管理”、“API 路径匹配”六个模块。

5) 无。
