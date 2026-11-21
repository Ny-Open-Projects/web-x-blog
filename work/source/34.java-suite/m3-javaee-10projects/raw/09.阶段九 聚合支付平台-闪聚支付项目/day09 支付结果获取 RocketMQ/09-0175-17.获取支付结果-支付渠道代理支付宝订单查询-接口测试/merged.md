# 17.获取支付结果-支付渠道代理支付宝订单查询-接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\17.获取支付结果-支付渠道代理支付宝订单查询-接口测试【海量资源尽在 666java.com】.mp4
- 时长 7分44秒（音频 464s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来测试一下支付渠道代理查询支付宝订单状态的接口那么我们怎么测试呢刚才我们是把这个接口实现就写完了吧然后呢接下来我们要测的话怎么测我们用单元进行测试啊用单元测试也就是我们只测这一个方法我们给他造一些参数传给他看一下行不行好那么我们用单元测试的话这里边我们就需要把这个工程啊给他
[00:30] 补齐给它补齐然后呢这里边我们可以看先看这里边是不是有一个test然后呢我们也需要和这个men然后呢评级来一个在这test对吧然后这里边呢我们也是要创建加网看见吗但有时候老是不对你看你看人家的这个test下面加网这图标是这个
[01:02] 绿色的是吧你这个是灰色的我跟你说啊如果你现在写了一个test的这个目录然后有一个加吧你要想让它认啊你必须刷新一下这个POM对现在我们要往里边写这个单元测试类你刷新一下刷新一下它就来认了啊然后呢我们准备现在让它慢慢刷新啊然后我们是要针对这个Service是不是要进行测试呀
[01:28] 那么我们在test的下边建一个和它相同的包对吧然后呢接下来还要建一个我们要测试这个类嘛测试这个类的话我们建一个叫做test这个类然后上边就用我们这个Spring Boot test就行了好spring runner对吧好然后接下来这里我们是要做的事就不是要刚才说吗要测试刚才我们写的这个
[02:03] 叫支付订单状态的查询对吧所以这里边我们就对起这样一个名字那现在我们要测这个Service很显然我们是需要把它注进去的啊注进去然后呢它这个Service叫PayChannelAgentService对吧好那在这个里边各位它是不是就要去调用刚才它的这个查询
[02:31] 对吧查询但调整查询的话你也看到了它需要几个参数啊俩参数嘛那俩参数咱们得把它造出来第一个呢是支付渠道参数那这个怎么造呢原来是我们从数据库查的现在我们还要从数据库查那多麻烦呀那干脆你看啊我们当初是不是测试支付宝接口的时候
[03:00] 咱们应该有一堆的这个静态的参数嘛咱们把它拿过去啊在这儿在这儿有印象吧有这个公司要啊APP ID啊等等等这些东西对吧你把它拷过去然后咱们在这儿放进去反正是个单元测试嘛我们就看这个接口能不能走通然后呢这儿呢你就对把它溜出来是吧然后再往里边填嘛你比如说填APP ID看懂了吗填我们打开讲一样这个填的过程太麻烦
[03:30] 然后呢咱们直接拿过来其实相当于我们去造一个对象往里边填一些什么填一些我们要调支付宝的这个所需要的参数然后这里边还有一个我刚才应该还漏考了一个叫server这个地址这是不是就齐了齐了之后呢你就把它放到这里头这些大家都理解吧反正就是把这些参数都把它放进属性里头嘛然后现在关键是这个订单号填啥
[04:00] 你看这个就又遇到难题了订单号天长那订单号是我们散聚的订单号应该是当我们点击什么立即支付之后生成的订单号对不对那我们是应该在订单表当中去找一个订单号但你找哪个这个订单号这原来这些订单可能都是废单所以我建议这么弄你打开模拟器我们单独再扫一个
[04:26] 我们接着以前的这个利益支付的测试场景啊我们去扫一个这个二维码扫一下扫一下之后呢我们看一下啊来扫一下之后我们就准备去生成一个订单了嘛那生成这个订单了之后那看这里头不就是有订单号了吗你注意看啊你当前是七条记录嘛一会儿呢应该是生成完订单你看我现在比如我填这个三块钱行吧三块钱然后呢咱们支付一下
[04:56] 然后这里头应该有一个新的订单才对然后我们就查这个新的订单如果我现在支付成功他应该最终查的这个支付结果应该是成功状态对不对我们就看这个结果我们让他支付一下稍等一下模拟器呢就成功了成功之后你刷新一下你看现在是八条记录然后往后翻翻一下这个日期应该是最近的日期你看拿一下就这个这是我们散剧平台的订单号你把它贴进去
[05:26] 各位那你说我现在是不是就准备要执行了吗但这个单元测试仍然会加载这个Spring Boot的配置啊因为你也知道我们Spring Boot这个配置当中它是会启动很多的这种什么服务端口啊所以注意所以你在启动单元测试之前你把原来的这个服务给它干掉啊停掉要不然你一起单元测试它的端口会冲突然后呢咱们看一下现在我们的目标啊就是查刚才我们
[05:56] 创建的这个订单大家理解这个目标了我们现在执行你要看看他能不能拿到对吧哎呀弄错了啊我这是我这是弄的是哪个呀你现在要查的是你看啊把它关了我这个窗口有点小来把它往下拉你现在是不是要查询不是交易服务啊是谁呀支付渠道代理服务是不是查询支付宝的这个什么这个订单的状态
[06:28] 结果呀然后我们执行它看好你的脑子里边必须知道老师当前在干啥啊我现在呢就是来测一下刚才我写的查询支付宝订单状态的这个接口到底能不能把它查出来懂吧这个单号是不是也是我刚刚扫的生成了一个新的订单呢那我们来看一下看它最终能不能你看出来结果了出来结果你看咱们最终你看各位看懂了吗
[07:00] 是不是就是业务交付明确成功成功了这就是我们查到的一个什么对订单的结果那你说这个接口我们到这儿是不是就做完了就是支付渠道代理服务先做一个查支付宝的什么这个订单的状态那么有了这个接口那就好办了那我们就开始实现第一步发消息然后他接到消息开始调刚才我们写的调用支付宝的这个
[07:29] 查询拿到结果拿到结果之后再发消息然后交易服务接收消息更新订单状态大家理解了吧好支付渠道代理服务的支付宝交易状态查询接口我们就做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Spring Boot 实现支付宝支付渠道代理服务，包括配置、代码编写、测试和数据库查询。

2) 按时间顺序列出每张画面的要点：
画面1：展示支付代理服务的启动日志，包含多个服务初始化信息，如 `GatewayBootstrap`、`MerchantApplicationBootstrap` 等。
画面2：展示 `AlipayClient` 的使用，代码中定义了 `@Param` 注解的参数，如 `outTradeNo`、`queryOrderByAll`。
画面3：展示 `pom.xml` 文件，其中包含 `parent`、`artifactId`、`groupId`、`version` 等 Maven 配置。
画面4：展示 `PayChannelAgentService` 类的代码，定义了 `@Service` 注解和 `createPayOrderByAll` 方法。
画面5：展示 `TestPayChannelAgentService` 测试类，使用 `@SpringBootTest` 和 `@AutoConfigureWebClient` 注解。
画面6：展示测试类中调用 `payChannelAgentService.queryPayOrderByAll` 方法。
画面7：展示一个文档页面，包含支付宝 SDK 示例代码，如 `AlipayClient`、`AlipayTradeQueryRequest`、`execute` 方法。
画面8：展示测试类中设置 `alipayConfigParam` 的参数，如 `serverUrl`、`charset`、`appID`。
画面9：展示数据库查询结果，包含 `trade_no`、`trade_status`、`pay_channel` 等字段。
画面10：展示测试类中调用 `queryPayOrderByAll` 方法并打印返回结果。
画面11：展示 `bootstrap.yml` 文件，包含 `spring-boot-http.yml`、`spring-boot-mybatis-plus.yml`、`spring-boot-redis.yml` 等配置。
画面12：展示测试类中设置 `APP_ID`、`APP_PRIVATE_KEY`、`ALIPAY_PUBLIC_KEY` 等参数。
画面13：展示测试类中调用 `queryPayOrderByAll` 方法并打印返回结果。
画面14：展示一个文档页面，包含 RocketMQ 的架构图，描述支付渠道代理服务与交易服务通过 RocketMQ 通信的流程。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面3 的 pom.xml：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>shanjupy-parent</artifactId>
        <groupId>com.shanjupay</groupId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>
```

画面4 的 PayChannelAgentService.java：
```java
@Service
public class PayChannelAgentServiceImpl implements PayChannel.AgentService {

    @Autowired
    private AlipayConfigParam alipayConfigParam;

    @Override
    public PaymentResponseDTO createPayOrderByAll(AlipayConfigParam alipayConfigParam) {
        String url = alipayConfigParam.getHttpUrl();
        String appid = alipayConfigParam.getAppId();
        String charset = alipayConfigParam.getCharset();
        String signType = alipayConfigParam.getSignType();
        String format = alipayConfigParam.getFormat();
        String returnUrl = alipayConfigParam.getReturnUrl();
        String notifyUrl = alipayConfigParam.getNotifyUrl();
        String outTradeNo = alipayConfigParam.getOutTradeNo();
        String subject = alipayConfigParam.getSubject();
        String body = alipayConfigParam.getBody();
        String totalAmount = alipayConfigParam.getTotalAmount();
        String timeoutExpress = alipayConfigParam.getTimeoutExpress();
        String productCode = alipayConfigParam.getProductCode();
        String qrCode = alipayConfigParam.getQrCode();
        String buyerLogonId = alipayConfigParam.getBuyerLogonId();
        String buyerUserId = alipayConfigParam.getBuyerUserId();
        String buyerNick = alipayConfigParam.getBuyerNick();
        String buyerRealName = alipayConfigParam.getBuyerRealName();
        String buyerMobile = alipayConfigParam.getBuyerMobile();
        String buyerEmail = alipayConfigParam.getBuyerEmail();
        String buyerAddress = alipayConfigParam.getBuyerAddress();
        String buyerPostCode = alipayConfigParam.getBuyerPostCode();
        String buyerCity = alipayConfigParam.getBuyerCity();
        String buyerProvince = alipayConfigParam.getBuyerProvince();
        String buyerCountry = alipayConfigParam.getBuyerCountry();
        String buyerDistrict = alipayConfigParam.getBuyerDistrict();
        String buyerZipCode = alipayConfigParam.getBuyerZipCode();
        String buyerPhone = alipayConfigParam.getBuyerPhone();
        String buyerFax = alipayConfigParam.getBuyerFax();
        String buyerCompany = alipayConfigParam.getBuyerCompany();
        String buyerTaxId = alipayConfigParam.getBuyerTaxId();
        String buyerTaxType = alipayConfigParam.getBuyerTaxType();
        String buyerTaxCode = alipayConfigParam.getBuyerTaxCode();
        String buyerTaxName = alipayConfigParam.getBuyerTaxName();
        String buyerTaxAddress = alipayConfigParam.getBuyerTaxAddress();
        String buyerTaxPhone = alipayConfigParam.getBuyerTaxPhone();
        String buyerTaxEmail = alipayConfigParam.getBuyerTaxEmail();
        String buyerTaxPostCode = alipayConfigParam.getBuyerTaxPostCode();
        String buyerTaxCity = alipayConfigParam.getBuyerTaxCity();
        String buyerTaxProvince = alipayConfigParam.getBuyerTaxProvince();
        String buyerTaxCountry = alipayConfigParam.getBuyerTaxCountry();
        String buyerTaxDistrict = alipayConfigParam.getBuyerTaxDistrict();
        String buyerTaxZipCode = alipayConfigParam.getBuyerTaxZipCode();
        String buyerTaxPhone = alipayConfigParam.getBuyerTaxPhone();
        String buyerTaxFax = alipayConfigParam.getBuyerTaxFax();
        String buyerTaxCompany = alipayConfigParam.getBuyerTaxCompany();
        String buyerTaxTaxId = alipayConfigParam.getBuyerTaxTaxId();
        String buyerTaxTaxType = alipayConfigParam.getBuyerTaxTaxType();
        String buyerTaxTaxCode = alipayConfigParam.getBuyerTaxTaxCode();
        String buyerTaxTaxName = alipayConfigParam.getBuyerTaxTaxName();
        String buyerTaxTaxAddress = alipayConfigParam.getBuyerTaxTaxAddress();
        String buyerTaxTaxPhone = alipayConfigParam.getBuyerTaxTaxPhone();
        String buyerTaxTaxEmail = alipayConfigParam.getBuyerTaxTaxEmail();
        String buyerTaxTaxPostCode = alipayConfigParam.getBuyerTaxTaxPostCode();
        String buyerTaxTaxCity = alipayConfigParam.getBuyerTaxTaxCity();
        String buyerTaxTaxProvince = alipayConfigParam.getBuyerTaxTaxProvince();
        String buyerTaxTaxCountry = alipayConfigParam.getBuyerTaxTaxCountry();
        String buyerTaxTaxDistrict = alipayConfigParam.getBuyerTaxTaxDistrict();
        String buyerTaxTaxZipCode = alipayConfigParam.getBuyerTaxTaxZipCode();
        String buyerTaxTaxPhone = alipayConfigParam.getBuyerTaxTaxPhone();
        String buyerTaxTaxFax = alipayConfigParam.getBuyerTaxTaxFax();
        String buyerTaxTaxCompany = alipayConfigParam.getBuyerTaxTaxCompany();
        String buyerTaxTaxTaxId = alipayConfigParam.getBuyerTaxTaxTaxId();
        String buyerTaxTaxTaxType = alipayConfigParam.getBuyerTaxTaxTaxType();
        String buyerTaxTaxTaxCode = alipayConfigParam.getBuyerTaxTaxTaxCode();
        String buyerTaxTaxTaxName = alipayConfigParam.getBuyerTaxTaxTaxName();
        String buyerTaxTaxTaxAddress = alipayConfigParam.getBuyerTaxTaxTaxAddress();
        String buyerTaxTaxTaxPhone = alipayConfigParam.getBuyerTaxTaxTaxPhone();
        String buyerTaxTaxTaxEmail = alipayConfigParam.getBuyerTaxTaxTaxEmail();
        String buyerTaxTaxTaxPostCode = alipayConfigParam.getBuyerTaxTaxTaxPostCode();
        String buyerTaxTaxTaxCity = alipayConfigParam.getBuyerTaxTaxTaxCity();
        String buyerTaxTaxTaxProvince = alipayConfigParam.getBuyerTaxTaxTaxProvince();
        String buyerTaxTaxTaxCountry = alipayConfigParam.getBuyerTaxTaxTaxCountry();
        String buyerTaxTaxTaxDistrict = alipayConfigParam.getBuyerTaxTaxTaxDistrict();
        String buyerTaxTaxTaxZipCode = alipayConfigParam.getBuyerTaxTaxTaxZipCode();
        String buyerTaxTaxTaxPhone = alipayConfigParam.getBuyerTaxTaxTaxPhone();
        String buyerTaxTaxTaxFax = alipayConfigParam.getBuyerTaxTaxTaxFax();
        String buyerTaxTaxTaxCompany = alipayConfigParam.getBuyerTaxTaxTaxCompany();
        String buyerTaxTaxTaxTaxId = alipayConfigParam.getBuyerTaxTaxTaxTaxId();
        String buyerTaxTaxTaxTaxType = alipayConfigParam.getBuyerTaxTaxTaxTaxType();
        String buyer

