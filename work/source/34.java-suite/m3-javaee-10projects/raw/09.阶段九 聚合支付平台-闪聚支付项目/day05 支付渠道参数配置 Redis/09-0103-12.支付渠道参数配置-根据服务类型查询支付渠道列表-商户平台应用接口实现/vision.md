# 画面线理解：12.支付渠道参数配置-根据服务类型查询支付渠道列表-商户平台应用接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\12.支付渠道参数配置-根据服务类型查询支付渠道列表-商户平台应用接口实现【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:20, 00:34, 00:55, 01:08, 01:31, 01:53, 02:16, 02:24, 02:43, 02:56, 03:22, 03:43, 03:52, 04:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:24:52

1) 这一组画面整体在讲什么（一句话）：
演示如何在商户平台应用中定义并测试一个根据服务类型查询支付渠道列表的 RESTful 接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程 PPT 的“5.4.3 商户平台应用支付渠道查询接口(接口⑥)”章节，重点是“5.4.3.1 接口定义”，并展示了在 PlatformParamController 类中定义的 queryPayChannelByPlatformChannel 接口代码，包含 @ApiOperation 和 @GetMapping 注解。
画面 2: 展示了 IntelliJ IDEA 中的项目结构，选中了 shanjupay-transaction-service 模块，右侧编辑器中显示了 TestPayChannelService 类的测试代码，其中包含 @Autowired 注解注入 PayChannelService。
画面 3: 展示了 PPT 中“5.4.3.2 接口测试”部分，提供了使用 Postman 测试接口的 URL：http://localhost:57010/merchant/my/pay_channels/platform-channel/shanju_c2b。
画面 4: 展示了 PlatformPayChannelController 类的代码，其中包含 @ApiOperation 注解和 @GetMapping 注解定义的 queryAppBindPlatformChannel 方法。
画面 5: 展示了 PlatformPayChannelController 类的代码，其中包含 @ApiOperation 注解和 @GetMapping 注解定义的 queryPayChannelByPlatformChannel 方法。
画面 6: 展示了 PlatformPayChannelController 类的代码，其中包含 @ApiOperation 注解和 @GetMapping 注解定义的 queryPayChannelByPlatformChannel 方法。
画面 7: 展示了 PlatformPayChannelController 类的代码，其中包含 @ApiOperation 注解和 @GetMapping 注解定义的 queryPayChannelByPlatformChannel 方法。
画面 8: 展示了 PlatformPayChannelController 类的代码，其中包含 @ApiOperation 注解和 @GetMapping 注解定义的 queryPayChannelByPlatformChannel 方法。
画面 9: 展示了 PlatformPayChannelController 类的代码，其中包含 @ApiOperation 注解和 @GetMapping 注解定义的 queryPayChannelByPlatformChannel 方法。
画面 10: 展示了 IntelliJ IDEA 中的控制台输出，显示了由于连接被拒绝导致的异常信息，包括 Caused by: java.net.ConnectException: Connection refused: no further information。
画面 11: 展示了 Postman 中的请求配置，请求 URL 为 http://localhost:57010/merchant/my/pay_channels/platform-channel/shanju_c2b，请求方法为 GET。
画面 12: 展示了 Postman 中的响应结果，显示了 JSON 格式的返回数据，包含 id、channelName、channelCode 字段。
画面 13: 展示了 Postman 中的响应结果，显示了 JSON 格式的返回数据，包含 id、channelName、channelCode 字段。
画面 14: 展示了课程 PPT 的“5.4.3 商户平台应用支付渠道查询接口(接口⑥)”章节，重点是“5.4.3.1 接口定义”，并展示了在 PlatformParamController 类中定义的 queryPayChannelByPlatformChannel 接口代码，包含 @ApiOperation 和 @GetMapping 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@ApiOperation("根据服务类型查询支付渠道列表")
@ApiImplicitParams({
@ApiImplicitParam(name = "platformChannelCode", value = "服务类型编码", required = true, dataType = "String", paramType = "path")
})
@GetMapping(value="/my/pay-channels/platform-channel/{platformChannelCode}")
public List<PayChannelDTO> queryPayChannelByPlatformChannel(@PathVariable String platformChannelCode){
return payChannelService.queryPayChannelByPlatformChannel(platformChannelCode);
}
```

画面 2:
```java
import org.springframework.test.context.junit4.SpringRunner;
import java.util.List;

@SpringBootTest
public class TestPayChannelService {

@Autowired
PayChannelService payChannelService;

//测试根据服务类型查询支付渠道
```

画面 3:
```text
使用Postman：http://localhost:57010/merchant/my/pay_channels/platform-channel/shanju_c2b
```

画面 4:
```java
@ApiOperation("查询应用是否绑定（某个服务类型）")
@ApiImplicitParams({
@ApiImplicitParam(name = "appId", value = "应用AppId", required = true, dataType = "String", paramType = "query"),
@ApiImplicitParam(name = "platformChannel", value = "服务类型", required = true, dataType = "String", paramType = "query")
})
@GetMapping("/my/merchants/apps/platformchannels")
public int queryAppBindPlatformChannel(@RequestParam String appId, @RequestParam String platformChannel) {
return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```

画面 5:
```java
@GetMapping("/my/merchants/apps/platformchannels")
public int queryAppBindPlatformChannel(@RequestParam String appId, @RequestParam String platformChannel) {
return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```

画面 6:
```java
@GetMapping("/my/merchants/apps/platformchannels")
public int queryAppBindPlatformChannel(@RequestParam String appId, @RequestParam String platformChannel) {
return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```

画面 7:
```java
@GetMapping("/my/merchants/apps/platformchannels")
public int queryAppBindPlatformChannel(@RequestParam String appId, @RequestParam String platformChannel) {
return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```

画面 8:
```java
@GetMapping("/my/merchants/apps/platformchannels")
public int queryAppBindPlatformChannel(@RequestParam String appId, @RequestParam String platformChannel) {
return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```

画面 9:
```java
@GetMapping("/my/merchants/apps/platformchannels")
public int queryAppBindPlatformChannel(@RequestParam String appId, @RequestParam String platformChannel) {
return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```

画面 10:
```text
Caused by: java.net.ConnectException: Connection refused: no further information
Disconnected from the target VM, address: '127.0.0.1:57010', transport: 'socket'
Process finished with exit code -1
```

画面 11:
```text
http://localhost:57010/merchant/my/pay_channels/platform-channel/shanju_c2b
```

画面 12:
```json
{
"id": 1,
"channelName": "微信",
"channelCode": "WX_JSAPI"
}
```

画面 13:
```json
{
"id": 2,
"channelName": "支付宝手机网站支付",
"channelCode": "ALIPAY_WAP"
}
```

画面 14:
```java
@ApiOperation("根据服务类型查询支付渠道列表")
@ApiImplicitParams({
@ApiImplicitParam(name = "platformChannelCode", value = "服务类型编码", required = true, dataType = "String", paramType = "path")
})
@GetMapping(value="/my/pay-channels/platform-channel/{platformChannelCode}")
public List<PayChannelDTO> queryPayChannelByPlatformChannel(@PathVariable String platformChannelCode){
return payChannelService.queryPayChannelByPlatformChannel(platformChannelCode);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“5.4.3 商户平台应用支付渠道查询接口(接口⑥)”，子标题为“5.4.3.1 接口定义”，内容包括“1. 接口描述：根据服务类型查询支付渠道列表”和“2. 接口定义如下：在PlatformParamController类中定义queryPayChannelByPlatformChannel：”。
画面 3: PPT 标题为“5.4.3.2 接口测试”，内容为“使用Postman：http://localhost:57010/merchant/my/pay_channels/platform-channel/shanju_c2b”。
画面 14: PPT 标题为“5.4.3 商户平台应用支付渠道查询接口(接口⑥)”，子标题为“5.4.3.1 接口定义”，内容包括“1. 接口描述：根据服务类型查询支付渠道列表”和“2. 接口定义如下：在PlatformParamController类中定义queryPayChannelByPlatformChannel：”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
