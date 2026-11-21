# 4.生成门店二维码-生成二维码-交易服务接口实现-生成URL

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\4.生成门店二维码-生成二维码-交易服务接口实现-生成URL【海量资源尽在 666java.com】.mp4
- 时长 6分23秒（音频 383s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下边呢我们接着来写这个生成二维码的URL刚才完成了校验那下边呢是不是要组装数据了组装数据这里边呢除了把我们说传入进去的这五个数据呢放到URL里边还需要一些数据啊有时候老师需要啥数据呢注意看我们看讲义啊
[00:19] 那么我们还需要的这个数据呢其实都不多了啊一个是我们做的这个三户ID应用ID门店ID还有就是订单的标题订单的内容还有一个参数这个参数是要写死的就是要硬编码的因为这个是我们系统的服务类型嘛就是C扫币对应该是需要几个参数啊六个参数对六个参数那么这六个参数我们用一个什么用一个类型
[00:49] 来去把它填充这个类型呢就叫做配解order DTO这个类型看好在这个类型当中你会看到是不是包括了很多的这个参数啊其中就有什么门店啊应用啊服务类型对吧还有标题内容然后还有啥你现在需要几个参数你先看清楚你不是要商户ID还需要一个商户商户
[01:22] 桑花ID有吗没有没有很简单我们往里边填往里边填就是这个类型就是用于让你干嘛对去拼装数据用的懂吧所以这样的话我们就可以在这儿去往里边干嘛拼装了拼装了怎么拼装这个过程就比较简单了吧从传进来的这里头拿是不是就这样一个一个的把它干嘛
[01:54] 拼进去拼进去另外还有最终我们说是不是有一个参数是额外我们加的就这服务类型这里边要干嘛对要写要写为什么叫C扫B的服务类型这个代码是不是就比较简单你大概知道啥意思就行了是吧好了那现在我们说这个拼好了之后呢拼好了之后我们是需要干嘛把它转成JIT
[02:25] 为啥转JSON因为按照我们的规则啊你把它先转成JSON再用base64编码然后呢你把它放到这个支付入口作为参数懂了吧所以这里面呢你要把它转JSON那转JSON怎么转怎么转那这里面它是不是有很多的方法呀那就toJSONstring是不是就行了那你把它放进去这个JSON串是不是就成了然后接下来是不是还要用base64进行编码呀
[02:56] Base64编码的话这里边我们在这个common的工具包当中有一个工具类我们把它编码编码我们用encoder解码我们用decoder是吧然后呢咱们把它放进去大家看懂了吗对这就是我们的一个URL的什么参数我们就生成OK了那么这个参数呢我们给它起个名叫take it
[03:24] 好下面我们拿到了这个参数我们你现在你是不是要返回一个支付入口啊这入口在哪呢入口因为入口将来就是这个扫二维码要这个请求到的一个地址是吧而这个只是一个参数嘛所以各位看讲义这个支付入口这一块呢我们是需要在我们的配置文件当中去把它配起来的对配起来将来因为可能这个就换成域名了嘛
[03:55] 因为让他扫嘛外网要扫这里边肯定是一个域名将来所以这里边要可以配置在我们当前进行内部测试的时候呢我们可以叫这个内网的域内网的地址将来上线肯定是一个公网域名所以这里边呢我们就进入什么呀进入Necros好那Necros这里边呢我们还是要进到配置列表吧然后呢找到当前你在哪个服务你先看清楚
[04:24] 当前你是不是要读取这个入口啊你是在交易服务对吧交易服务的话那很显然你是要找到交易服务transaction Service这个配置文件然后呢在最下边我们把它配上去是不是就OK了嗯然后我们把它配上去之后接下来要做的事就是要干嘛嗯把这个从配置文件把它读出来对现在要从配置文件
[04:54] 来读取支付入口它的地址这个地址呢我们用怎么样value注解这个我觉得大家应该都比较熟悉了吧然后呢是算号到了符号大括号那你就根据key value来读就行了对吧根据key value你看后边是不是有一个叫散去配配URL那我是不是就读到了读到了之后呢你拿着这个地址
[05:24] 放到这儿然后再加上刚才我们的这个参数各位这就是最终一个二维码的地址咱们就生成了这个逻辑大家理解了吗对最终这个二维码的这个地址会是啥样啊它是不是就是这是前边对吧这是前边然后呢注意看啊后边后边是不是你会生成一堆的这个被子64呀有啥啥都有对不对将来呢
[05:54] 请求到这个地址那么这个地址后边我们去开发它会把这个后边那个参数把它解开然后就知道是哪个商户哪个应用哪个门店甚至订单的标题和内容都知道了大家理解吗就这个思路好那这个就是我们生成二维码交易服务生成二维码URL的接口咱们是不是就写完了后边我们是不是要写商户平台应用然后生成二维码图片好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在交易服务中实现生成商户门店二维码的接口，包括数据传输对象定义、业务逻辑编码、以及在 Nacos 中配置支付入口 URL。

2) 按时间顺序列出每张画面的要点：
画面1：展示 QrCodeDto 类的定义，包含 merchantId、appId、storeId、subject、body 等字段。
画面2：展示 createStoreQrcode 方法的注释和部分代码，用于生成门店二维码。
画面3：展示 PayOrderDTO 类的定义，包含 storeId、appId、channel、outTradeNo、subject、body、totalAmount、currency、optional、extra、opend、authCode、payChannel、clientIp 等字段。
画面4：展示 PayOrderDTO 类的定义，光标位于 storeId 字段。
画面5：展示 createStoreQrcode 方法中设置 PayOrderDTO 对象的 appId 和 storeId。
画面6：展示 createStoreQrcode 方法中设置 PayOrderDTO 对象的 subject、channel、body，并生成 JSON 字符串。
画面7：展示 createStoreQrcode 方法中对 JSON 字符串进行 Base64 编码，生成 ticket。
画面8：展示 verifyAppAndStore 方法的注释和部分代码，用于验证商户和门店的合法性。
画面9：展示在 Nacos 中添加支付入口配置 transaction-Service.yaml，配置 payurl。
画面10：展示 Nacos 配置管理界面，列出多个配置文件。
画面11：展示 createStoreQrcode 方法中对 JSON 字符串进行 Base64 编码，生成 ticket。
画面12：展示 createStoreQrcode 方法的完整代码，包括注释和业务逻辑。
画面13：展示在 Nacos 中配置 transaction-Service.yaml，配置 payurl。
画面14：展示 createStoreQrcode 方法中设置 payEntryUrl，并返回。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * @Author administrator
 * @Version 1.0
 * @Data
 */
public class QrCodeDto implements Serializable {
    private Long merchantId;
    private String appId;
    private Long storeId;
    private String subject;//商品标题
    private String body;//订单描述
}
```

画面2：
```java
/**
 * @Reference
 * AppService appService;
 */
/**
 * 生成门店二维码
 * @param qrcodeDto 商户id、应用id、门店id、标题、内容
 * @return
 * @throws BusinessException
 */
@Override
public String createStoreQrcode(QrCodeDto qrcodeDto) throws BusinessException {
    //校验应用和门店
    verifyAppAndStore(qrcodeDto.getMerchantId(),qrcodeDto.getAppId(),qrcodeDto.getStoreId());
    //1.生成支付信息
    PayOrderDTO payOrderDTO = new PayOrderDTO();
    payOrderDTO.setMerchantId(qrcodeDto.getMerchantId());
    payOrderDTO.setAppId(qrcodeDto.getAppId());
    payOrderDTO.setStoreId(qrcodeDto.getStoreId());
    payOrderDTO.setSubject(qrcodeDto.getSubject());
    payOrderDTO.setChannel("shanju_czb");//服务类型
    payOrderDTO.setBody(qrcodeDto.getBody());
    String jsonString = JSON.toJSONString(payOrderDTO);
    log.info("transaction Service createStoreQrcode,JsonString is {}",jsonString);
    //将支付信息保存到缓存中
    String ticket = EncryptUtil.encodeUTF8StringBase64(jsonString);
    //支付入口
    String payEntryUrl = payurl + ticket;
    log.info("transaction Service createStoreQrcode,pay_entry is {}",payEntryUrl);
    return payEntryUrl;
}
```

画面3：
```java
/**
 * @Data
 */
public class PayOrderDTO implements Serializable {
    private Long storeId;//商户门店id，如果未绑定，默认绑定门店
    private String appId;//商户应用id，服务与服务之间用业务id区分
    private String channel;//聚合支付的通道，此处使用通道编码
    private String outTradeNo;//商户订单号
    private String subject;//商品标题
    private String body;//订单描述
    private Integer totalAmount;//订单金额，单位为分
    private String currency;//币种，CNY
    private String optional;//自定义数据
    private String extra;//用于统计分析的数据，用户自定义
    private String opend;//商户端和商户端参数
    private String authCode;//付款码，支付查看者微信“付款”产生的付款码
    private String payChannel;//原生渠道支付渠道编码
    private String clientIp;//请求IP
}
```

画面5：
```java
    //1.生成支付信息
    PayOrderDTO payOrderDTO = new PayOrderDTO();
    payOrderDTO.setMerchantId(qrcodeDto.getMerchantId());
    payOrderDTO.setAppId(qrcodeDto.getAppId());
    payOrderDTO.setStoreId(qrcodeDto.getStoreId());
    payOrderDTO.setSubject(qrcodeDto.getSubject());
    payOrderDTO.setChannel("shanju_czb");//服务类型
    payOrderDTO.setBody(qrcodeDto.getBody());
    String jsonString = JSON.toJSONString(payOrderDTO);
    log.info("transaction Service createStoreQrcode,JsonString is {}",jsonString);
    //将支付信息保存到缓存中
    String ticket = EncryptUtil.encodeUTF8StringBase64(jsonString);
    //支付入口
    String payEntryUrl = payurl + ticket;
    log.info("transaction Service createStoreQrcode,pay_entry is {}",payEntryUrl);
    return payEntryUrl;
```

画面6：
```java
    //将支付信息保存到缓存中
    String ticket = EncryptUtil.encodeUTF8StringBase64(jsonString);
    return url;
```

画面7：
```java
    //将支付信息保存到缓存中
    String ticket = EncryptUtil.encodeUTF8StringBase64(jsonString);
    return url;
```

画面8：
```java
/**
 * 检验应用和门店是否属于当前登录商户
 * @param merchantId
 * @param appId
 * @param storeId
 */
private void verifyAppAndStore(Long merchantId,String appId,Long storeId) {
    //根据应用和门店查询
    Boolean contains = appService.queryAppMerchant(appId, merchantId);
}
```

画面9：
```yaml
#支付入口url
shanjupy:
  payurl: "http://172.8.8.1:56810/transaction/pay-entry/"
```

画面10：无代码或配置。

画面11：
```java
    //将支付信息保存到缓存中
    String ticket = EncryptUtil.encodeUTF8StringBase64(jsonString);
    return url;
```

画面12：
```java
/**
 * @Reference
 * MerchantService merchantService;
 */
/**
 * 生成门店二维码
 * @param qrcodeDto 商户id、应用id、门店id、标题、内容
 * @return
 * @throws BusinessException
 */
@Override
public String createStoreQrcode(QrCodeDto qrcodeDto) throws BusinessException {
    //校验应用和门店
    verifyAppAndStore(qrcodeDto.getMerchantId(),qrcodeDto.getAppId(),qrcodeDto.getStoreId());
    //组装出所需要的参数
    PayOrderDTO payOrderDTO = new PayOrderDTO();
    payOrderDTO.setMerchantId(qrcodeDto.getMerchantId());
    payOrderDTO.setAppId(qrcodeDto.getAppId());
    payOrderDTO.setStoreId(qrcodeDto.getStoreId());
    payOrderDTO.setSubject(qrcodeDto.getSubject());
    payOrderDTO.setChannel("shanju_czb");//服务类型
    payOrderDTO.setBody(qrcodeDto.getBody());
    String jsonString = JSON.toJSONString(payOrderDTO);
    log.info("transaction Service createStoreQrcode,JsonString is {}",jsonString);
    //将支付信息保存到缓存中
    String ticket = EncryptUtil.encodeUTF8StringBase64(jsonString);
    //支付入口
    String payEntryUrl = payurl + ticket;
    log.info("transaction Service createStoreQrcode,pay_entry is {}",payEntryUrl);
    return payEntryUrl;
}
```

画面13：
```yaml
#支付入口url
shanjupy:
  payurl: "http://172.8.8.1:56810/transaction/pay-entry/"
```

画面14：
```java
    //支付入口
    String payEntryUrl = payurl + ticket;
    log.info("transaction Service createStoreQrcode,pay_entry is {}",payEntryUrl);
    return payEntryUrl;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT 标题为“3.4.2.4 接口实现”，内容包括“在 Nacos 中添加支付入口配置：transaction-Service.yaml”和“支付入口是扫码支付的统一入口。”
画面9：PPT 标题为“3.4.2.4 接口实现”，内容包括“在 Nacos 中添加支付入口配置：transaction-Service.yaml”和“支付入口是扫码支付的统一入口。”
画面13：PPT 标题为“3.4.2.4 接口实现”，内容包括“在 Nacos 中添加支付入口配置：transaction-Service.yaml”

