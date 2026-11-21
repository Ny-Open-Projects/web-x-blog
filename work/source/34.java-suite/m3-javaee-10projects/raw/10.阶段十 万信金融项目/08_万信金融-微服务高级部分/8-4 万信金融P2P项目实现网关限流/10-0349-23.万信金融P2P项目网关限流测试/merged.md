# 23.万信金融P2P项目网关限流测试

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-4 万信金融P2P项目实现网关限流
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-4 万信金融P2P项目实现网关限流\23.万信金融P2P项目网关限流测试_【海量资源尽在 666java.com】.mp4
- 时长 4分32秒（音频 272s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们在万信金融P2P项目当中呢把这个网关限流呢给集成进来了集成进来之后呢咱接下来就要进行功能测试怎么测试呢因为咱当时在定义限流规则的时候是不是针对这个谁呀这个资源是谁呀是不是UA这个服务对吧那所以说你要测试的话你必须是往这个什么呀往UA这个服务上发什么呀发请求然后才能进行测试
[00:29] 那我们还是以什么为例啊登录吧因为在登录业务当中呢它就涉及到要访问谁啊UAF那为了测试方便了我这次呢就通过前端去发这个登录请求因为前端这个做这个限流测试不太方便啊我们用这个什么铺层麦然后频繁的你去发这个登录请求你要想看到效果的话就是你一秒内要超过几次请求要超过几次超过两次嘛因为你看咱们当时设置的这个上限值是多少二嘛对不对
[00:59] 超两次能怎么着呢超两次呢你其实你能收到这么一个返回的一个信息这个信息就是由这个网关限流啊返回的这是他内部定义好的一个什么提示信息这个编号是329这是提示内容就Sentinel什么呀相当于就是出现什么出现限流了啊那是哪出现限流呢我们的资源名字就是就是这个什么ua这个这个这个赛华放的就是失败了
[01:28] 你只要看到这个信息就证明了就证明这个限流起作用了因为正常情况下的话你应该是看不到这个信息应该是登录成功嘛是不是那你看到这个信息就证明了限流起作用那咱既然是不是应该把相关的微服给启动一下吧登录的话我看我刚才是不是主要是改的网关这一块的代码吧其他地方代码咱应该没改那我就需要把网关的给它重新一下其他的
[02:00] 咱应该没动其他咱应该都没动因为这是网关线聊嘛所以说咱刚才的这些代码啥的都是加到这个什么网关里边咱就把网关这个微服务给它启动一下然后咱在postman当中呢就开始进行测试53020对吧这应该是启动完了啊然后其他相关的这些跟登录有关的吧这些微服务呢我全都已经启动过大家看一下阿布罗也启动过是不是
[02:40] 那应该就可以了我们就可以去这个什么呀对postman当中我们找一找咱之前的那个什么登录那个测试是吧呃应该是在统一账号这里是这个吧这就是这个登录你看这是不是就往ua发个请求吧没错吧ua啊然后传的参数对有这么一堆吧但我有印象啊有这么一堆然后你就找一找你的postman吧你之前应该在postman里边应该也做过登录测试你找一找啊
[03:11] 看这里边的数据现在还对不对不对的话你给他改改给他改成正确的啊这是我的账号密码了干完之后你是不是在这点击什么呀send就开始做这个登录测试了我先点一下试试这应该就是什么呀这应该就是成功了是不是啊你这不是拿到令牌了吗对拿令牌就是成功了啊那我要想看到那个线流到像我们说了我得点的快一点对不对那一秒之内呢要要超过几次超两次那我就使劲点呗在这个什么呀pulseman里边使劲点对不对
[03:45] 你注意看这一块啊看这一块有没有什么变化这手速有这么慢吗哎哎哎刚才闪亮眼你刚才看到没有这还不好整呢哎出来了哎呀这次运气比较好是不是你看你是不是就看到这么一个什么呀返回的一个信息啊我刚才让大家看到了吗就39这是它内部的一个一个什么呀一个编号吧这就是提示信息就是出现限流了啊然后呢这个是哪出现的限流啊就唯一这一块大家就看到这么一个什么提示信息这就证明什么呀
[04:27] 限流已经起作用了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面11：展示 Apollo 配置中心的界面，显示 `application` 空间下的配置项，其中包含 `Sentinel.rule.gateway-flow-rule` 的 JSON 配置。
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
    String ruleKey = "Sentinel.rule.gateway-flow-rule"; // 限流规则的key
    String defaultRules = "";
    ReadableDataSource<String, Set<GatewayFlowRule>> gatewayRuleDataSource = new ApolloDataSource<>(namespaceName, ruleKey, defaultRules, source -> JSON.parseObject(source, new TypeReference<Set<GatewayFlowRule>>() {}));
    GatewayRuleManager.registerProperty(gatewayRuleDataSource.getProperty());
}
```

画面2：
```json
{
  "resource": "uaa-Service", // 对应zuul的routes，这里的资源指的是统一认证服务
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
    String ruleKey = "Sentinel.rule.gateway-flow-rule"; // 限流规则的key
    String defaultRules = "";
    ApolloDataSource<Set<GatewayFlowRule>> gatewayRuleDataSource = new ApolloDataSource<>(namespaceName, ruleKey, defaultRules, source -> JSON.parseObject(source, new TypeReference<Set<GatewayFlowRule>>() {}));
    GatewayRuleManager.registerProperty(gatewayRuleDataSource.getProperty());
}
```

画面11：
```properties
Sentinel.rule.gateway-flow-rule = [{"resource":"uaa-Service","resourceMode":0,"grade":1,"count":2,"intervalSec":1,"controlBehavior":0,"burst":0,"maxQueueingTimeoutMs":500,"paramItem":{}}]
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

