# 画面线理解：23.万信金融P2P项目网关限流测试

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-4 万信金融P2P项目实现网关限流
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-4 万信金融P2P项目实现网关限流\23.万信金融P2P项目网关限流测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:09, 00:16, 00:59, 01:53, 02:05, 02:12, 02:31, 02:38, 03:26, 03:40, 03:52, 03:59, 04:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:18:35

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Apollo 配置中心动态配置 Sentinel 流量控制规则，并通过 Postman 测试登录接口以验证规则生效。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中关于 Sentinel 动态规则配置的代码，包括 `@PostConstruct` 方法中初始化 `ApolloDataSource` 并注册规则的逻辑。
画面2：展示 PDF 文档中配置项的 JSON 格式，包含 `resource`、`resourceMode`、`grade`、`count`、`intervalSec`、`controlBehavior`、`burst`、`maxQueueingTimeouts` 等参数。
画面3：与画面2内容相同，为 PDF 文档中配置项的 JSON 格式。
画面4：与画面1内容相同，为 PDF 文档中关于 Sentinel 动态规则配置的代码。
画面5：展示 IDE 中 `ZuulConfig.java` 文件的代码，其中包含 `@PostConstruct` 方法初始化 `ApolloDataSource` 并注册规则的逻辑。
画面6：展示 IDE 中 `ZuulConfig.java` 文件的代码，其中包含 `@PostConstruct` 方法初始化 `ApolloDataSource` 并注册规则的逻辑。
画面7：展示 IDE 中 `ZuulConfig.java` 文件的代码，其中包含 `@PostConstruct` 方法初始化 `ApolloDataSource` 并注册规则的逻辑。
画面8：展示 IDE 中 `ZuulConfig.java` 文件的代码，其中包含 `@PostConstruct` 方法初始化 `ApolloDataSource` 并注册规则的逻辑。
画面9：展示 IDE 中 `ZuulConfig.java` 文件的代码，其中包含 `@PostConstruct` 方法初始化 `ApolloDataSource` 并注册规则的逻辑。
画面10：展示 Postman 中用于获取登录令牌的 POST 请求，请求地址为 `http://localhost:3301/uaa/oauth/token`，包含 `client_id`、`client_secret`、`username`、`password`、`domain`、`authenticationType` 等参数。
画面11：展示 Apollo 配置中心的界面，显示 `application` 空间下的配置项，其中包含 `sentinel.rule.gateway-flow-rule` 的 JSON 配置。
画面12：展示 Postman 中用于获取登录令牌的 POST 请求，请求地址为 `http://localhost:3301/uaa/oauth/token`，包含 `client_id`、`client_secret`、`username`、`password`、`domain`、`authenticationType` 等参数。
画面13：展示 Postman 中用于获取登录令牌的 POST 请求，请求地址为 `http://localhost:3301/uaa/oauth/token`，包含 `client_id`、`client_secret`、`username`、`password`、`domain`、`authenticationType` 等参数。
画面14：展示 Postman 中用于获取登录令牌的 POST 请求，请求地址为 `http://localhost:3301/uaa/oauth/token`，包含 `client_id`、`client_secret`、`username`、`password`、`domain`、`authenticationType` 等参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 从Apollo上获取限流规则并进行配置
 */
@PostConstruct
private void initGatewayRules() {
    String namespaceName = "application"; // 对应Apollo的命名空间名称
    String ruleKey = "sentinel.rule.gateway-flow-rule"; // 限流规则的key
    String defaultRules = "";
    ReadableDataSource<String, Set<GatewayFlowRule>> gatewayRuleDataSource = new ApolloDataSource<>(namespaceName, ruleKey, defaultRules, source -> JSON.parseObject(source, new TypeReference<Set<GatewayFlowRule>>() {}));
    GatewayRuleManager.registerProperty(gatewayRuleDataSource.getProperty());
}
```

画面2：
```json
{
  "resource": "uaa-service", // 对应zuul的routes，这里的资源指的是统一认证服务
  "resourceMode": 0, // 网关模式
  "grade": 1, // QPS限流模式
  "count": 2, // 上限值
  "intervalSec": 1, // 统计时间窗口，单位是秒，默认是 1 秒
  "controlBehavior": 0, // 流量控制效果（直接拒绝、Warm Up、匀速排队等待）
  "burst": 0, // 应对突发请求时额外允许的请求数目
  "maxQueueingTimeoutMs": 500, // 匀速排队模式下的最长排队时间，单位是毫秒，仅在匀速排队模式下生效
  "paramItem": { // 动态参数，目前不需要
  }
}
```

画面5：
```java
/**
 * 从Apollo上获取限流规则并进行配置
 */
@PostConstruct
private void initGatewayRules() {
    String namespaceName = "application"; // 对应Apollo的命名空间名称
    String ruleKey = "sentinel.rule.gateway-flow-rule"; // 限流规则的key
    String defaultRules = "";
    ApolloDataSource<Set<GatewayFlowRule>> gatewayRuleDataSource = new ApolloDataSource<>(namespaceName, ruleKey, defaultRules, source -> JSON.parseObject(source, new TypeReference<Set<GatewayFlowRule>>() {}));
    GatewayRuleManager.registerProperty(gatewayRuleDataSource.getProperty());
}
```

画面11：
```properties
sentinel.rule.gateway-flow-rule = [{"resource":"uaa-service","resourceMode":0,"grade":1,"count":2,"intervalSec":1,"controlBehavior":0,"burst":0,"maxQueueingTimeoutMs":500,"paramItem":{}}]
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
