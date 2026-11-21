# 12.支付渠道参数配置-根据服务类型查询支付渠道列表-商户平台应用接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\12.支付渠道参数配置-根据服务类型查询支付渠道列表-商户平台应用接口实现【海量资源尽在 666java.com】.mp4
- 时长 4分10秒（音频 250s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来实现商户平台应用来根据服务类型来查询支付渠道其实刚才我们做的是在交易服务当中我们把double接口完成了下面呢我们要写一个http的接口给前端调用好那么我们来看啊那么整个的这个根据服务类型查询支付渠道很显然它的参数呢就是服务类型的代码对吧好那下面呢我们就来写啊那么首先我们需要在
[00:28] 商户平台应用的工程我们在Controller当中来定义这个接口那么在这儿对吧好那么这个接口呢我们说它传的餐是不是就是我们说的platform对吧然后呢这个有点长啊原则是channel什么code对吧好那么注意那么你最终啊
[01:00] 你要返回的是什么呢最终返回啥最终返回的肯定是个list嘛对吧还记得那个list里面啥吗就是paychannel.to对不对好然后呢这个呢其实就是根据什么根据服务类型来查询支付渠道支付渠道好那这个应该说它是一个查询一般来说我们都是
[01:33] get对吧所以这是这个get那另外的话这里面我们看它传参它是不是通过pass来传呢所以这里面呢就是pass variable然后呢和这个名称保持一致对吧好然后还有这个这个Swagger的这个什么它的参数它的定义方法这里面是一个参数对不对所以这一个参数的话我们其实你把它拷过来
[02:02] 我们改吧改吧就可以了那这个呢应该是我们说的这个名称跟他一样这个呢就是叫支付服务类型代码参数嘛参数不是服务类型代码吗对不对然后呢他呢是啥pass因为你是不是通过pass传然后呢我们再通过Service来调用就是return直接哎哪个
[02:31] 是不是根据好多好多是不是根据它然后把它放到这我们方法名好长的慢慢来这个接口是不是就写好了写好了之后我们是不是就可以第一我们要做的是不是把这个交易服务给起起来第二我们要把三户平台应用给起起来第三我们是不是要在Postman当中来测对吧
[03:02] 这个应该我们说来再来一个这是啥呀改一下啊这叫做根据服务类型来查询支付渠道对不对好然后呢它的这个参数的信息包括URL这里边我们一个一个复制啊可以吧那这个呢这是服务类型的代码服务类型的代码是不是就是散具C早币啊这是不是就可以了
[03:40] 那好那现在呢我们就让他请求嗯就出来了看是不是两条记录微信和支付宝也就是散具C扫币它是需要配置两个支付渠道的参数咱们先把这两个支付渠道呢在页面展示出来后面呢有一个配置参数一点我们再去配置参数那是后面的内容了到这呢我们是不是就完成了商户平台啊查询支付渠道的接口啊就是根据服务类型来查询它所对应的支付渠道好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在商户平台应用中定义并测试一个根据服务类型查询支付渠道列表的 RESTful 接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程 PPT 的“5.4.3 商户平台应用支付渠道查询接口(接口⑥)”章节，重点是“5.4.3.1 接口定义”，并展示了在 PlatformParamController 类中定义的 queryPayChannelByPlatformChannel 接口代码，包含 @ApiOperation 和 @GetMapping 注解。
画面 2: 展示了 IntelliJ IDEA 中的项目结构，选中了 shanjupay-transaction-Service 模块，右侧编辑器中显示了 TestPayChannelService 类的测试代码，其中包含 @Autowired 注解注入 PayChannelService。
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

