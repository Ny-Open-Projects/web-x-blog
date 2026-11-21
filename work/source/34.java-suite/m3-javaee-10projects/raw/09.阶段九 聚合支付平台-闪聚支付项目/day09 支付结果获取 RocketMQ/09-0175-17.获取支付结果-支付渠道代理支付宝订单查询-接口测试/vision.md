# 画面线理解：17.获取支付结果-支付渠道代理支付宝订单查询-接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\17.获取支付结果-支付渠道代理支付宝订单查询-接口测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:47, 01:11, 01:45, 02:15, 02:55, 03:30, 04:06, 04:44, 05:28, 05:54, 06:23, 06:45, 07:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:15:05

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
