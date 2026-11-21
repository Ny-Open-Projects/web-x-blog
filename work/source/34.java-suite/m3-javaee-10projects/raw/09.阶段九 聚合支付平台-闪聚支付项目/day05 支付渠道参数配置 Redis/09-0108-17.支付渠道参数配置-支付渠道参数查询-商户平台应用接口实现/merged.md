# 17.支付渠道参数配置-支付渠道参数查询-商户平台应用接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\17.支付渠道参数配置-支付渠道参数查询-商户平台应用接口实现【海量资源尽在 666java.com】.mp4
- 时长 7分58秒（音频 478s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来实现商户平台应用查询支付渠道参数的接口那么刚才我们完成了交易服务支付渠道参数查询接口下面呢我们就是来写一个http的接口来调用交易服务查询的接口那给前段的返回查询的结果好那么仍然是两个接口一个是根据应用服务类型查支付渠道参数列表一个是根据应用服务类型以及支付渠道来查单个的支付渠道它的参数信息好
[00:29] 那么我们来看吧首先呢我们需要在找到这个商户应用的这个平台来看一下啊application对吧然后找到control了来看一下它这个里头呢我们需要传什么参数呢传什么参数啊反正两个接口嘛一个是根据应用服务类型查列表一个是根据应用服务类型和支付渠道查单个支付渠道参数对不对一个是俩参数一个是三个参数那现在呢我们来看吧
[01:02] 那我们怎么说我先把这个URL给你写到这对我写URL呢你得根据我的URL来写代码好然后呢现在来看啊最终啊它是不是要返回一个列表对吧那我先把这个列表返回来叫支付渠道参数的这个列表你看吧来根据URL来写这个参数怎么写填空题pass variable对不对然后呢
[01:35] 你这个第一个通过pass来传递的你看appid这里边就是appid对吧然后还有后边这个服务类型它是不是也是通过pass来传递的搞定看懂了吗好然后上边我们写Square的这些注解这个不用说简单吧然后再看
[02:08] 那现在要写这个参数了这个参数好像我写过无数次了注意看我再给你写一次挺好俩参数吧两个参数我们就来写valuevalue是啥第一个是应用的ID对吧namename是和它保持一致然后datatype啥string那关键的就是这个parametype我之前说过这是pass
[02:41] 对不对好然后继续下面这个是不是就是我们说的叫做服务类型代码对吧服务类型代码是不是就后边这个行三呀你把它写到这他是不是也是pass搞定了然后最后呢他要调用我们说的pay channel Service然后return直接现在要查询看好哇好多
[03:11] 好多接口了现在要查谁啊查这个嗯点开它查哪个查列表吗查它对不对所以这里边呢我们要查这个方法然后这个方法呢一个是app id一个是什么哎一个是服务类型代码这是不是就搞定了对吧然后其他的另外一个复制
[03:37] 对吧行不行然后我们改了啊开始改了这个呢是他查单个支付渠道的参数那这个例子又变成单个了对吧然后呢方法名和讲义保持一致方法名和讲义保持一致看好没问题吧然后URL和讲义保持一致看好然后呢我就给你这两个空然后呢你给我填咋填呀看现在呢
[04:06] 它是需要三个参数一个是APP ID一个是服务类型代码还有一个叫做Pay Channel这是啥是不是就是我们说的支付渠道呀对吧支付渠道也是通过pass所以这里边呢我们就把这个支付渠道这个pass variable加上去可以吧那么这是三个参数很显然上面也得加这是不是就是一个支付渠道呀
[04:37] 支付渠道代码对吧那都是通过pass嘛对不对好还有啥那剩下的是不是就是这个往下翻我们是不是要查调用这个方法没错吧然后后边的参数给他一个pay channelpay channelOK了吧好现在呢我们把交易服务给他重启一下然后呢再把商户平台应用
[05:10] 也重启一下我们现在呢就来测这两个接口行不行查询接口呢都是get还是比较方便测的啊我们用Swagger就可以非常方便的把它测出来好了来看一下啊让它起完那起完了之后呢我们就可以来打开Swagger刷新好那现在呢我们看一下这两个接口
[05:36] 哇好藏啊是这个吧这是获取呃应用指定服务类型下所包含的原始支付渠道参数列表这是所有对吧这是所有然后下边这个呢是获取单个的啊根据应用服务类型下所包含的原始支付渠道参数列表啊然后呢看一下啊这个应该是没有改的把这个改一下因为我拷贝的嘛这个是获取啊
[06:08] 根据应用和服务类型然后呢获取支付渠道参数列表简化一下行不行然后呢这个是根据应用和服务类型和支付渠道获取单个的单个的支付渠道参数不是列表了懂吧好好那这个呢我们来开始测试了啊
[06:39] 先测一个列表吧先测一个列表的话这里边我们应用和服务类型应用服务类型主要的是你看我们现在是不是查这张表啊应用服务类型这里边最终要拿到一个绑定ID吧那么应用和服务类型绑定这个应用的ID我们拿到然后服务类型拿到这是不是就OK执行各位这是不是就查到了你看
[07:08] 你看这个是不是一个输组结构呀所以它这里头是一个列表对吧好然后呢接下来再测另外一个是测试啥呀单个的支付渠道参数的查询同样你也要把应用的ID输进去把支付渠道把服务类型输进去支付渠道呢支付渠道呢你得看你要哪个支付渠道我们要查微信那把微信拿到这然后我们执行这个呢你看
[07:38] 看它是不是一个对象就没有这个素组对不对这就是单个的支付渠道参数好了那么以上呢我们就完成了支付渠道参数查询的两个接口啊一个是查支付渠道参数列表一个是查单个支付渠道参数我们呢就测试通过了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解商户平台应用渠道参数查询接口的定义与实现，包括控制器层和业务服务层的代码编写及Swagger文档测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示接口定义文档，说明接口功能为“根据应用和服务类型获取原始参数列表”，并给出在PlatformParamController中定义的queryPayChannelParam方法的Java代码。
画面2：在文档中点击“接口定义2”，准备查看下一个接口定义。
画面3：在IDE中展示PlatformParamController的代码，光标位于queryPayChannelParam方法的返回值类型上，右侧显示了相关注解的自动补全列表。
画面4：在IDE中展示PlatformParamController的代码，光标位于@ApiImplicitParams注解的dataType参数上，右侧显示了相关注解的自动补全列表。
画面5：在IDE中展示PlatformParamController的代码，光标位于payChannelService.savePayChannelParam(payChannelDTO)方法调用处，右侧显示了相关方法的自动补全列表。
画面6：在IDE中展示PlatformParamController的代码，光标位于@ApiImplicitParams注解的value参数上，右侧显示了相关注解的自动补全列表。
画面7：在IDE中展示PlatformParamController的代码，光标位于@GetMapping注解的value参数上，右侧显示了相关注解的自动补全列表。
画面8：在IDE中展示PayChannelServiceImpl的代码，光标位于queryPayChannelParamByAppPlatformAndPayChannel方法的返回值类型上，右侧显示了相关注解的自动补全列表。
画面9：在IDE中展示PlatformParamController的代码，光标位于@GetMapping注解的value参数上，右侧显示了相关注解的自动补全列表。
画面10：在浏览器中打开Swagger UI，显示“闪聚支付-商户应用API文档”，并展示“商户平台-渠道和支付参数”下的接口列表。
画面11：在IDE中展示PlatformParamController的代码，光标位于@ApiImplicitParams注解的value参数上，右侧显示了相关注解的自动补全列表。
画面12：在Swagger UI中，显示GET请求的参数配置页面，其中“appId”字段值为“ebcceed-3032-49a6-9691-4770e66577a”，“platformChannel”字段值为“shaniu.czb”。
画面13：在Swagger UI中，显示GET请求的参数配置页面，其中“payChannel”字段值为“payChannel - 支付渠道代码”，“platformChannel”字段值为“platformChannel - 服务类型代码”。
画面14：展示接口定义文档，说明接口功能为“根据应用和服务类型及支付渠道获取单个原始支付参数”，并给出在PayChannelService接口中定义的queryPayChannelParamByAppAndPlatform方法的Java代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@ApiOperation("获取指定应用指定服务类型下所包含的原始支付渠道参数列表")
@ApiImplicitParams({
@ApiImplicitParam(name = "appId", value = "应用Id", required = true, dataType = "String", paramType = "path"),
@ApiImplicitParam(name = "platformChannel", value = "服务类型", required = true, dataType = "String", paramType = "path")
})
@GetMapping(value = "/my/pay-channel-params/apps/{appId}/platform-channels/{platformChannel}")
public List<PayChannelParamDTO> queryPayChannelParam(@PathVariable String appId,
@PathVariable String platformChannel) {
return payChannelService.queryPayChannelParamByAppAndPlatform(appId, platformChannel);
}
```

画面3：
```java
@GetMapping(value = "/ay/pay-channel-params/apps/{appId}/platform-channels/{platformChannel}")
public List<PayChannelParamDTO> queryPayChannelParam(@PathVariable String appId,
@PathVariable String platformChannel) {
```

画面4：
```java
@ApiImplicitParams({
@ApiImplicitParam(value = "应用Id", name = "appId", dataType = "String", paramType = "path"),
@ApiImplicitParam(value = "服务类型代码", name = "platformChannel", dataType = "String", paramType = "path")
})
@GetMapping(value = "/ay/pay-channel-params/apps/{appId}/platform-channels/{platformChannel}")
public List<PayChannelParamDTO> queryPayChannelParam(@PathVariable String appId,
@PathVariable String platformChannel) {
```

画面5：
```java
public List<PayChannelParamDTO> queryPayChannelParamByAppPlatformAndPayChannel(String appId, String platformChannel, String payChannel) throws BusinessException;
```

画面6：
```java
@GetMapping(value = "/ay/pay-channel-params/apps/{appId}/platform-channels/{platformChannel}/pay-channels/{payChannel}")
public PayChannelParamDTO queryPayChannelParam(@PathVariable("appId") String appId,
@PathVariable("platformChannel") String platformChannel,
@PathVariable("payChannel") String payChannel) {
```

画面7：
```java
@GetMapping(value = "/ay/pay-channel-params/apps/{appId}/platform-channels/{platformChannel}/pay-channels/{payChannel}")
public PayChannelParamDTO queryPayChannelParam(@PathVariable("appId") String appId,
@PathVariable("platformChannel") String platformChannel,
@PathVariable("payChannel") String payChannel) {
```

画面8：
```java
@Override
public PayChannelParamDTO queryPayChannelParamByAppPlatformAndPayChannel(String appId, String platformChannel, String payChannel) {
List<PayChannelParamDTO> payChannelParamDTOs = queryPayChannelParamByAppAndPlatform(appId, platformChannel);
return payChannelParamDTOs.getPayChannelParamDTO(payChannel);
}
```

画面9：
```java
@GetMapping(value = "/ay/pay-channel-params/apps/{appId}/platform-channels/{platformChannel}/pay-channels/{payChannel}")
public PayChannelParamDTO queryPayChannelParam(@PathVariable("appId") String appId,
@PathVariable("platformChannel") String platformChannel,
@PathVariable("payChannel") String payChannel) {
```

画面11：
```java
@GetMapping(value = "/ay/pay-channel-params/apps/{appId}/platform-channels/{platformChannel}/pay-channels/{payChannel}")
public PayChannelParamDTO queryPayChannelParam(@PathVariable("appId") String appId,
@PathVariable("platformChannel") String platformChannel,
@PathVariable("payChannel") String payChannel) {
```

画面14：
```java
/**
 * 获取指定应用指定服务类型下所包含的某个原始支付参数
 * @param appId
 * @param platformChannel
 * @param payChannel
 * @return
 * @throws BusinessException
 */
PayChannelParamDTO queryPayChannelParamByAppPlatformAndPayChannel(String appId, String platformChannel,
String payChannel) throws BusinessException;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“5.5.2 商户平台应用渠道参数查询接口”，子标题为“5.5.2.1 接口定义1”，内容包括“接口描述”和“接口定义如下”。
画面2：PPT标题为“5.5.2.1 接口定义2”，内容包括“接口描述”和“接口定义如下”。
画面10：Swagger UI页面标题为“闪聚支付-商户应用API文档 1.0.0”，显示“商户平台-渠道和支付参数”下的接口列表，包括POST、GET、POST、PUT四个接口。
画面12：Swagger UI页面显示GET请求的参数配置，包括“appId”、“platformChannel”两个参数。
画面13：Swagger UI页面显示GET请求的参数配置，包括“appId”、“payChannel”、“platformChannel”三个参数。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

