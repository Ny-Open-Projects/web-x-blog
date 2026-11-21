# 画面线理解：22.万信金融P2P项目实现网关限流

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-4 万信金融P2P项目实现网关限流
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-4 万信金融P2P项目实现网关限流\22.万信金融P2P项目实现网关限流_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:44, 02:18, 04:22, 05:06, 06:26, 09:33, 10:46, 12:01, 14:16, 15:01, 16:01, 18:08, 19:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:17:59

1) 这一组画面整体在讲如何在 Spring Cloud Zuul 网关中集成 Sentinel 流量控制，并通过 Apollo 配置中心动态管理限流规则。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 Zuul 和 Spring Cloud Gateway 的架构对比图，中间是 Sentinel 网关限流公共模块（API Gateway Adapter Common），包含请求属性解析、网关规则管理、网关规则检查、调用参数组装、自定义 API 分组管理、API 路径匹配等模块。
画面 2: 展示了在父工程 pom.xml 中添加 Sentinel-Zuul 适配器依赖的代码片段。
画面 3: 展示了文档中关于功能实现的说明，提到项目采用 Spring Cloud Zuul 作为网关，Apollo 作为配置中心，Sentinel 作为限流组件。
画面 4: 展示了 ZuulConfig.java 中的代码，用于配置 CORS 和注册 Filter。
画面 5: 展示了 Apollo 配置中心的界面，显示了多个配置项，如 micro_service.spring-boot-http、micro_service.spring-eureka 等。
画面 6: 展示了在 ZuulConfig 中增加限流规则配置的 JSON 格式，包含 resource、resourceMode、grade、count、intervalSec、controlBehavior、burst、maxQueueingTimeouts 等字段。
画面 7: 与画面 6 内容相同，展示限流规则配置的 JSON 格式。
画面 8: 展示了功能测试部分的代码，包含 @PostConstruct 注解的 initGatewayRules 方法，用于从 Apollo 获取限流规则并注册。
画面 9: 与画面 6 内容相同，展示限流规则配置的 JSON 格式。
画面 10: 展示了 initGatewayRules 方法中创建 ApolloDataSource 的代码。
画面 11: 展示了 initGatewayRules 方法中创建 ApolloDataSource 的代码，光标位于参数部分。
画面 12: 展示了功能测试部分的说明，提到通过 Postman 发送登录请求进行测试。
画面 13: 展示了 initGatewayRules 方法中创建 ApolloDataSource 的代码，光标位于参数部分。
画面 14: 与画面 2 内容相同，展示在父工程 pom.xml 中添加 Sentinel-Zuul 适配器依赖的代码片段。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 2:
```xml
<dependency>
    <artifactId>sentinel-zuul-adapter</artifactId>
    <version>1.6.2</version>
</dependency>

<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-datasource-apollo</artifactId>
    <version>1.6.2</version>
</dependency>
```

画面 3:
```xml
<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-zuul-adapter</artifactId>
    <version>1.6.2</version>
</dependency>

<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-datasource-apollo</artifactId>
    <version>1.6.2</version>
</dependency>
```

画面 6:
```json
{
  "resource": "uaa-service", // 对应zuul的routes，这里的资源指的是统一认证服务
  "resourceMode": 0, // 网关模式
  "grade": 1, // QPS限流模式
  "count": 2, // 上限值
  "intervalSec": 1, // 统计时间窗口，单位是秒，默认是 1 秒
  "controlBehavior": 0, // 流量控制效果（直接拒绝、Warm Up、匀速排队等待）
  "burst": 0, // 应对突发请求时额外允许的请求数目
  "maxQueueingTimeoutMs": 500, // 匀速排队模式下的最长排队时间，单位是毫秒。仅在匀速排队模式下生效
  "paramItem": { // 动态参数，目前不需要
  }
}
```

画面 8:
```java
/**
 * 从Apollo获取限流规则并进行配置
 */
@PostConstruct
private void initGatewayRules() {
    String namespaceName = "application"; // 对应Apollo的命名空间名称
    String ruleKey = "sentinel.rule.gateway-flow-rule"; // 限流规则的key
    String defaultRules = "";
    ReadableDataSource<String, Set<GatewayFlowRule>> gatewayRuleDataSource = new ApolloDataSource<>(namespaceName, ruleKey, defaultRules, source ->
            JSON.parseObject(source, new TypeReference<Set<GatewayFlowRule>>() {}));
    GatewayRuleManager.register2Property(gatewayRuleDataSource.getProperty());
}
```

画面 10:
```java
/**
 * 从Apollo上获取限流规则并进行配置
 */
@PostConstruct
private void initGatewayRules() {
    String namespaceName = "application"; // 对应Apollo的命名空间名称
    String ruleKey = "sentinel.rule.gateway-flow-rule"; // 根据规则的key
    String defaultRules = "";
    new ApolloDataSource<>(namespaceName, ruleKey, defaultRules, source ->
            JSON.parseObject(source, new TypeReference<Set<GatewayFlowRule>>() {}));
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 1: 架构图，左侧是 Zuul 的过滤器链（ZuulPreFilter, ZuulErrorFilter, ZuulPostFilter），右侧是 Spring Cloud Gateway 的组件（SentinelGatewayFilter, BlockRequestHandler），中间是 Sentinel 网关限流公共模块（API Gateway Adapter Common），包含六个功能模块：请求属性解析、网关规则管理、网关规则检查、调用参数组装、自定义 API 分组管理、API 路径匹配。
画面 3: PPT 标题为“3.2 功能实现”，内容说明项目采用 Spring Cloud Zuul 作为网关，Apollo 作为配置中心，Sentinel 作为限流组件。
画面 8: PPT 标题为“3.3 功能测试”，内容说明通过 Postman 发送登录请求进行测试。
画面 12: PPT 标题为“3.3 功能测试”，内容说明通过 Postman 发送登录请求进行测试。

5) 无。
