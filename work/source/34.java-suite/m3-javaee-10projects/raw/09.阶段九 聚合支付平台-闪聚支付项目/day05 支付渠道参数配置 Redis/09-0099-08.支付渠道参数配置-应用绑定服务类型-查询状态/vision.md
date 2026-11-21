# 画面线理解：08.支付渠道参数配置-应用绑定服务类型-查询状态

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\08.支付渠道参数配置-应用绑定服务类型-查询状态【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:08, 01:25, 02:18, 02:38, 03:07, 03:42, 04:09, 04:31, 04:41, 05:10, 05:40, 06:08, 06:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:21:54

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现应用与平台服务类型的绑定功能，包括数据库操作、服务层代码、控制器接口及 API 测试。

2) 按时间顺序列出每张画面的要点：
画面1：展示数据库表 `app_platform_channel` 的数据，ID 为 1211159463723554260，APP_ID 为 1234567890123456789，PLATFORM_CHANNEL 为 “huanqiu_22b”。
画面2：在 IDE 中展示 `PayChannelServiceImpl.java` 文件，代码逻辑为：若 `appPlatformChannel` 为空，则创建新实体并插入数据库。
画面3：在 IDE 中展示 `PayChannelService.java` 接口，定义了 `queryAppBindPlatformChannel` 方法，用于查询应用绑定的服务类型。
画面4：在 IDE 中展示项目结构，鼠标指向 `src/main/java/com/shan/jupy/transaction/service/PayChannelService.java` 文件。
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
