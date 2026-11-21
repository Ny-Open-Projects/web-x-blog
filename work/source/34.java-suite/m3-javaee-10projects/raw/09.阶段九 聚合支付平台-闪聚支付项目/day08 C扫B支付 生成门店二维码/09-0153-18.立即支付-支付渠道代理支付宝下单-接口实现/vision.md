# 画面线理解：18.立即支付-支付渠道代理支付宝下单-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\18.立即支付-支付渠道代理支付宝下单-接口实现【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:50, 01:37, 02:40, 04:15, 04:58, 05:57, 06:41, 07:49, 08:38, 09:50, 11:03, 12:04, 13:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:59:05

1) 这一组画面整体在讲如何在 Java 项目中实现支付宝支付下单接口，包括配置参数、构建请求对象、调用支付API并处理响应。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了项目结构和接口定义，重点是 `PayChannelAgentService` 接口，其中定义了 `createPayOrderByALIPAY` 方法，接收 `AliConfigParam` 和 `AlipayBean` 参数，返回 `PaymentResponseDTO`。
画面2: 展示了 `PayChannelAgentService` 接口的实现类 `PayChannelAgentServiceImpl` 中的 `createPayOrderByALIPAY` 方法，其中构建了 `AlipayTradeWapPayRequest` 对象并设置了参数。
画面3: 展示了 `AliConfigParam` 类的定义，包含 `appId`、`rsaPrivateKey`、`notifyUrl`、`returnUrl`、`url`、`charset`、`format` 等配置字段。
画面4: 展示了 `PayChannelAgentServiceImpl` 中 `createPayOrderByALIPAY` 方法的实现，其中从配置中获取参数并创建 `AlipayClient` 和 `AlipayTradeWapPayRequest` 对象。
画面5: 展示了 `PayChannelAgentServiceImpl` 中 `createPayOrderByALIPAY` 方法的实现，其中设置了 `AlipayTradeWapPayRequest` 对象的参数，包括 `out_trade_no`、`total_amount`、`subject`、`product_code`。
画面6: 展示了 `PayChannelAgentServiceImpl` 中 `createPayOrderByALIPAY` 方法的实现，其中调用 `alipayClient.pageExecute(alipayRequest)` 发起支付请求。
画面7: 展示了 `PayChannelAgentServiceImpl` 中 `createPayOrderByALIPAY` 方法的实现，其中使用 `AlipayTradeWapPayModel` 对象设置订单参数。
画面8: 展示了 `AlipayBean` 类的定义，包含 `body`、`expireTime`、`timestamp`、`storeId`、`attach` 等字段。
画面9: 展示了支付宝支付接口文档中关于 `auth_token` 参数的说明。
画面10: 展示了 `PayChannelAgentServiceImpl` 中 `createPayOrderByALIPAY` 方法的实现，其中调用 `alipayClient.pageExecute(alipayRequest)` 发起支付请求。
画面11: 展示了支付宝支付接口文档中关于 `product_code` 和 `passback_params` 参数的说明。
画面12: 展示了 `PayChannelAgentServiceImpl` 中 `createPayOrderByALIPAY` 方法的实现，其中处理支付响应并返回 `PaymentResponseDTO`。
画面13: 展示了 `PayChannelAgentServiceImpl` 中 `createPayOrderByALIPAY` 方法的实现，其中在捕获异常时抛出 `BusinessException`。
画面14: 展示了支付渠道代理服务的整体执行流程图，包括客户输入金额、请求交易服务、调用支付宝下单接口、支付宝生成支付凭证、返回支付凭证等步骤。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1:
```java
/**
 * 与第三方支付渠道进行交互。
 * Created by Administrator.
 */
public interface PayChannelAgentService {
    /**
     * 调用支付宝的下单接口
     * @param aliConfigParam 支付渠道配置的参数（配置的支付宝的必要参数）
     * @param alipayBean 业务参数（商户订单号，订单标题，订单描述...）
     * @return 返回一个PaymentResponseDTO
     */
    public PaymentResponseDTO createPayOrderByALIPAY(AliConfigParam aliConfigParam, AlipayBean alipayBean) throws Exception;
```
画面2:
```java
String CHARSET = "UTF-8";
//支付主接口，网关地址，正式 https://openapi.alipay.com/gateway.do
String serverUrl = "https://openapi.alipaydev.com/gateway.do";
//签名类型
String sign_type = "RSA2";
@GetMapping("/alipaytest")
public void alipayTest(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse) throws ServletException, IOException {
    //构造支付的客户端对象
    AlipayClient alipayClient = new DefaultAlipayClient(serverUrl, APP_ID, APP_PRIVATE_KEY,
            "json", CHARSET, ALIPAY_PUBLIC_KEY, "RSA2");
    AlipayTradeWapPayRequest alipayRequest = new AlipayTradeWapPayRequest();
    alipayRequest.setCharset("UTF-8");
    alipayRequest.setNotifyUrl("http://doc.51cto.com/CallBack/return_url.jsp");
    alipayRequest.setBizContent("{'out_trade_no':'20150420010101017','total_amount':'88.88','subject':'iPhone6 16G','product_code':'QUICK_WAP_PAY'}");
    String form = "";
    try {
        //请求支付宝下单接口，发起http请求
        form = alipayClient.pageExecute(alipayRequest).getBody(); //调用SDK生成表单
    } catch (AlipayApiException e) {
        e.printStackTrace();
    }
    httpServletResponse.setContentType("text/html;charset=" + CHARSET);
    httpServletResponse.getWriter().write(form);
}
```
画面3:
```java
package com.shanju.pay.paymentagent.spi.conf;
import ...
@Data
public class AliConfigParam implements Serializable {
    //应用id
    public String appId;
    //私钥
    public String rsaPrivateKey;
    //异步回调
    public String notifyUrl;
    //同步回调
    public String returnUrl;
    //支付网关
    public String url;
    //编码方式
    public String charset;
    //格式
    public String format;
    //签名类型
    public String signType;
}
```
画面4:
```java
/**
 * 调用支付宝的下单接口
 * @param aliConfigParam 支付渠道配置的参数（配置的支付宝的必要参数）
 * @param alipayBean 业务参数（商户订单号，订单标题，订单描述...）
 * @return 返回一个PaymentResponseDTO
 */
public PaymentResponseDTO createPayOrderByALIPAY(AliConfigParam aliConfigParam, AlipayBean alipayBean) throws Exception {
    String url = aliConfigParam.getUrl(); //支付宝接口网关地址
    String appId = aliConfigParam.getAppId(); //支付宝应用id
    String alipayPublicKey = aliConfigParam.getAlipayPublicKey(); //支付宝公钥
    //构造支付的客户端对象
    AlipayClient alipayClient = new DefaultAlipayClient(url, appId, aliConfigParam.getRsaPrivateKey(), "json", CHARSET, alipayPublicKey, "RSA2");
    AlipayTradeWapPayRequest alipayRequest = new AlipayTradeWapPayRequest();
    alipayRequest.setCharset("UTF-8");
    alipayRequest.setNotifyUrl("http://doc.51cto.com/CallBack/return_url.jsp");
    alipayRequest.setBizContent("{'out_trade_no':'20150420010101017','total_amount':'88.88','subject':'iPhone6 16G','product_code':'QUICK_WAP_PAY'}");
    String form = "";
    try {
        //请求支付宝下单接口，发起http请求
        form = alipayClient.pageExecute(alipayRequest).getBody(); //调用SDK生成表单
    } catch (AlipayApiException e) {
        e.printStackTrace();
    }
    httpServletResponse.setContentType("text/html;charset=" + CHARSET);
    httpServletResponse.getWriter().write(form);
}
```
画面5:
```java
String format = aliConfigParam.getFormat(); //编码方式
String charset = aliConfigParam.getCharset(); //编码
String alipayPublicKey = aliConfigParam.getAlipayPublicKey(); //支付宝公钥
//构造支付的客户端对象
AlipayClient alipayClient = new DefaultAlipayClient(url, appId, aliConfigParam.getRsaPrivateKey(), format, charset, alipayPublicKey, "RSA2");
AlipayTradeWapPayRequest alipayRequest = new AlipayTradeWapPayRequest();
alipayRequest.setCharset("UTF-8");
alipayRequest.setNotifyUrl("http://doc.51cto.com/CallBack/return_url.jsp");
alipayRequest.setBizContent("{'out_trade_no':'20150420010101017','total_amount':'88.88','subject':'iPhone6 16G','product_code':'QUICK_WAP_PAY'}");
String form = "";
try {
    //请求支付宝下单接口，发起http请求
    form = alipayClient.pageExecute(alipayRequest).getBody(); //调用SDK生成表单
} catch (AlipayApiException e) {
    e.printStackTrace();
}
httpServletResponse.setContentType("text/html;charset=" + CHARSET);
httpServletResponse.getWriter().write(form);
```
画面6:
```java
String format = aliConfigParam.getFormat(); //编码方式
String charset = aliConfigParam.getCharset(); //编码
String alipayPublicKey = aliConfigParam.getAlipayPublicKey(); //支付宝公钥
//构造支付的客户端对象
AlipayClient alipayClient = new DefaultAlipayClient(url, appId, aliConfigParam.getRsaPrivateKey(), format, charset, al
