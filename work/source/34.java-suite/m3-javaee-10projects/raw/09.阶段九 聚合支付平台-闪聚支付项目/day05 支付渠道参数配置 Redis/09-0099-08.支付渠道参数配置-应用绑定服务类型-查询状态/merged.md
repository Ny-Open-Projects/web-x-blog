# 08.支付渠道参数配置-应用绑定服务类型-查询状态

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\08.支付渠道参数配置-应用绑定服务类型-查询状态【海量资源尽在 666java.com】.mp4
- 时长 6分37秒（音频 397s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢,我们继续来实现应用绑定服务类型。
[00:04] 刚才我们完成了应用绑定服务类型接口的开发。
[00:07] 那么当应用绑定服务类型成功之后呢,前端呢,需要来查询我们系统的接口,来看一下这个应用和服务类型到底是否绑定成功。
[00:17] 那么当然这个接口呢,不光是在绑定的时候要查询,那么在其他地方呢,前端也需要。
[00:24] 所以这里边呢,我们需要来单独写一个接口,就是服务类型绑定状态的查询。
[00:29] 其实也就是根据某一个应用和服务类型的代码来查一下它到底是否绑定成功那这里边它的返回值我说一下它返回一个int也就是当绑定成功的时候呢也就是当这个应用和服务类型绑定关系表有记录的时候那么我们选择返回一个1否则呢返回0那么这样的话这个接口呢就是一个什么绑定服务类型状态的一个查询
[00:56] 好那下面呢我们仍然是先写交易服务再写商户平台应用的两个地方都要写好那在交易服务这里面呢我们仍然来写一下啊交易服务找到对于前后端分离开发呢大家一定要去把这个接口开发的技能呢提升上去当然我们到写当中做的更多的工作还是接口开发根据刚才借口分析我们说返回值是一个int对吧然后呢它会有一个叫
[01:27] APP ID的参数请求进来对吧还有一个就是我们说的这个服务类型的代码好那么我们来看一下这个参数呢尽量和讲义当中保持一致啊好这个写完了之后呢各位它最终我们要知道它就是返回一个什么状态码而这个状态码呢其实就是应用绑定服务类型的一个什么一个状态
[02:01] 那么当我们说以绑定那这个时候它是不是为1啊否则为什么0对吧好那么现在呢如果我们要去查询这个状态各位思考一下我们怎么做怎么做因为当初我们在绑定应用和服务类型的时候我们其实已经做过查询了这是不是就是做的查询对不对那其实各位
[02:33] 很简单我们查出来之后啊我们可以判断一下如果说它已经绑定就是不为空的情况下我们让它返回1就行了否则返回0这是不是就是查询的应用与服务类型的绑定状态对好这样的话交易服务的接口呢咱们就完成了交易服务接口完成了之后呢那么我们呢就需要怎么弄啊需要来写一个
[03:04] 三户平台查询的接口注意看讲义这里边讲义和我写的不是很一样讲义你看他写的是slag.com也是跟应用和服务类型来查询但是各位讲义这么写也行但是我刚才给大家演示的这个写法是不是也OK也就是查询一下APP和服务类型的绑定关系这张表当中你要注意一个应用和一个服务类型的指定
[03:32] 只能绑定一次也就是他俩是在这个表当中是唯一的这两个字段所以我这个写法select one是不是也没有问题对好那么接下来继续那我们是不是要在商户平台应用当中来继续写一个绑定状态的查询那么我们来看一下这个接口应该怎么写这个接口的话其实跟刚才我们应用绑定服务类型类似了也是传入app id对吧然后这里边也是返回一个什么返回一个int
[04:03] 刚才Service我们写的是不是就返回印的这个整个的这个代码呢我就不再写了嗯那大家呢不要去考啊因为我说了这个应用绑定服务类型的这个接口你看和这个接口类似的啊所以我就不再写了啊也调用我们刚才写的这个Service这个就完工了吧好那么完成了之后呢我们来看啊我们把它给重启一下测试一下其实在我们实际开发当中啊
[04:35] 很多情况下你比如说刚才我会发现这两个参数一样那么你在开发的时候可能就把这两个参数直接拷过来甚至呢你可能把整个方法都拷过来改吧改吧是不是就可以了对所以大家呢一定要习惯于这种很多重复代码的这种拷贝啊好那么我们把这个应用交易服务起来把商户平台应用起来我们就可以测试了好那这个测试的话还是用这个Postman来测
[05:05] 来看一下啊这个是应用绑定服务类型啊这个呢是应用绑定服务类型的一个什么状态查询对不对好那这个是get对吧然后呢接下来我们看啊这个url是他改一下呃那么这个查询好像和原来我们应用绑定服务类型提交的时候不太一样你看这两个它有区别它都是query大家看见了吗这两个参数
[05:38] 所以呢在post的们写的时候呢也要注意好问号对吧问号然后呢参数呢我们从我们的control的接口当中来复制这不就是APP ID然后还有一个参数这不就是我们说的应用服务类型的什么代码就是我们平台服务类型的代码好那现在呢我们就找到我们应用的ID把它拿过来
[06:09] OK吧然后呢接下来服务类型的代码是不是就它说白了就是查这条记录如果查到我们就让它返回什么返回一个1对吧如果没有查到就返回0那这里边当然你也可以随便写一个字符它没有查到肯定是0看懂啥意思吧好到这儿呢我们说应用绑定服务类型的整个的接口呢咱们就做完了也就是5.3的这个小节好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现应用与平台服务类型的绑定功能，包括数据库操作、服务层代码、控制器接口及 API 测试。

2) 按时间顺序列出每张画面的要点：
画面1：展示数据库表 `app_platform_channel` 的数据，ID 为 1211159463723554260，APP_ID 为 1234567890123456789，PLATFORM_CHANNEL 为 “huanqiu_22b”。
画面2：在 IDE 中展示 `PayChannelServiceImpl.java` 文件，代码逻辑为：若 `appPlatformChannel` 为空，则创建新实体并插入数据库。
画面3：在 IDE 中展示 `PayChannelService.java` 接口，定义了 `queryAppBindPlatformChannel` 方法，用于查询应用绑定的服务类型。
画面4：在 IDE 中展示项目结构，鼠标指向 `src/main/java/com/shan/jupy/transaction/Service/PayChannelService.java` 文件。
画面5：在 IDE 中展示 `PayChannelServiceImpl.java` 文件，代码逻辑为：若 `appPlatformChannel` 为空，则创建新实体并插入数据库。
画面6：展示 PPT 内容，标题为“5.5.5.2 接口实现”，代码为：
```java
@Override
public int queryAppBindPlatformChannel(String appId, String platformChannel) {
    int count = appPlatformChannelMapper.selectCount(
        new QueryWrapper<AppPlatformChannel>().lambda()
            .eq(AppPlatformChannel::getAppId, appId)
            .eq(AppPlatformChannel::getPlatformChannel, platformChannel));
    //已存在绑定关系返回1
    if (count > 0) {
        return 1;
    } else {
        return 0;
    }
}
```
画面7：在 IDE 中展示 `PayChannelServiceImpl.java` 文件，代码逻辑为：若 `appPlatformChannel` 为空，则创建新实体并插入数据库。
画面8：在 IDE 中展示 `PlatformParamController.java` 文件，代码为：
```java
@PostMapping("/pay/apps/{appid}/platform-channels")
void bindPlatformChannel(@PathVariable("appid") String appId, @RequestParam("platformChannelCode") String platformChannelCode) {
    payChannelService.bindPlatformChannelForApp(appId, platformChannelCode);
}
@GetMapping("/pay/apps/{appid}/platform-channels")
public int queryAppBindPlatformChannel(@PathVariable("appid") String appId, @RequestParam("platformChannel") String platformChannel) {
    return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```
画面9：在 IDE 中展示 `PlatformParamController.java` 文件，代码为：
```java
@GetMapping("/pay/apps/{appid}/platform-channels")
public int queryAppBindPlatformChannel(@PathVariable("appid") String appId, @RequestParam("platformChannel") String platformChannel) {
    return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```
画面10：在 IDE 中展示 `PlatformParamController.java` 文件，代码为：
```java
@GetMapping("/pay/apps/{appid}/platform-channels")
public int queryAppBindPlatformChannel(@PathVariable("appid") String appId, @RequestParam("platformChannel") String platformChannel) {
    return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```
画面11：在 Postman 中展示“应用绑定服务类型”接口的 POST 请求，URL 为 `http://localhost:57010/merchant/my/apps/...`。
画面12：在 Postman 中展示“应用绑定服务类型”接口的 GET 请求，URL 为 `http://localhost:57010/merchant/my/apps/...`。
画面13：展示数据库表 `app_platform_channel` 的数据，ID 为 1211159463723554260，APP_ID 为 1234567890123456789，PLATFORM_CHANNEL 为 “huanqiu_22b”。
画面14：展示 PPT 内容，标题为“第三方支付渠道提供多种支付方式”，列出了微信支付的多种方式，包括：付码支付、JSAPI支付、Native支付、APP支付、H5支付、小程序支付、人脸支付。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面6：
```java
@Override
public int queryAppBindPlatformChannel(String appId, String platformChannel) {
    int count = appPlatformChannelMapper.selectCount(
        new QueryWrapper<AppPlatformChannel>().lambda()
            .eq(AppPlatformChannel::getAppId, appId)
            .eq(AppPlatformChannel::getPlatformChannel, platformChannel));
    //已存在绑定关系返回1
    if (count > 0) {
        return 1;
    } else {
        return 0;
    }
}
```
画面8：
```java
@PostMapping("/pay/apps/{appid}/platform-channels")
void bindPlatformChannel(@PathVariable("appid") String appId, @RequestParam("platformChannelCode") String platformChannelCode) {
    payChannelService.bindPlatformChannelForApp(appId, platformChannelCode);
}
@GetMapping("/pay/apps/{appid}/platform-channels")
public int queryAppBindPlatformChannel(@PathVariable("appid") String appId, @RequestParam("platformChannel") String platformChannel) {
    return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```
画面10：
```java
@GetMapping("/pay/apps/{appid}/platform-channels")
public int queryAppBindPlatformChannel(@PathVariable("appid") String appId, @RequestParam("platformChannel") String platformChannel) {
    return payChannelService.queryAppBindPlatformChannel(appId, platformChannel);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构、表格数据：
画面6：标题“5.5.5.2 接口实现”，内容为“在PayChannelServiceImpl中实现queryAppBindPlatformChannel方法”。
画面14：标题“第三方支付渠道提供多种支付方式”，内容为：
- 付码支付：用户打开微信钱包-付款码的界面，商户后台扫码完成支付。
- JSAPI支付：用户通过微信浏览器，关注公众号等方式进入商家H5页面，并在微信内调用JSSDK完成支付。
- Native支付：用户打开微信“扫一扫”，扫描商户的二维码完成支付。
- APP支付：商户APP中集成微信SDK，用户点击后跳转到微信内完成支付。
- H5支付：用户在微信中打开H5页面，商户后台扫码完成支付。
- 小程序支付：用户在微信小程序中使用微信支付的场景。
- 人脸支付：无需掏出手机，刷脸完成支付，透传给下层场景。

5) 无。

