# 画面线理解：23.立即支付-整体流程测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\23.立即支付-整体流程测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:26, 02:51, 03:52, 05:25, 06:27, 07:42, 08:34, 09:12, 10:13, 11:24, 12:29, 13:33, 14:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:03:30

1) 这一组画面整体在讲什么（一句话）：
演示如何通过支付代理服务调用支付宝下单，并展示相关代码、数据库配置和测试流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档中“5.4.2.2 请求代理服务调用支付宝下单”章节，代码片段为：
```java
return PayOrderConvert.INSTANCE.entity2dto(entity);
```
以及私有方法：
```java
//调用支付宝接口
private PaymentResponseDTO alipayH5(String tradeNo) {
    //构建支付实体
    AlipayBean alipayBean = new AlipayBean();
    //根据订单号查询订单详情
    PaymentDTO paymentDTO = queryPayOrder(tradeNo);
    alipayBean.setOutTradeNo(tradeNo);
    alipayBean.setSubject(paymentDTO.getSubject());
    String totalAmount = null;//支付宝账单入参是元
    try {
```

画面2：展示文档中“5.4.3 测试”章节，以及支付渠道代理服务的流程图，流程为：
用户 → 商户 → 代理服务 → 支付宝 → 支付凭证生成 → 返回支付凭证 → 返回用户。

画面3：展示IDE中`PayController.java`文件，代码片段为：
```java
//支付结果
PaymentResponseDTO paymentResponseDTO = transactionService.submitOrderByAli(paymentOrderDTO);
String content = paymentResponseDTO.getContent();
response.setContentType("text/html;charset=UTF-8");//设置响应的编码格式
response.getWriter().write(content);
response.getWriter().close();
```

画面4：展示IDE中`PaymentAgentServiceTool.java`文件，代码片段为：
```java
try {
    alipayBean.setTotalAmount(amount, change2Yuan(payOrderDTO.getTotalAmount()).toString());
} catch (Exception e) {
    e.printStackTrace();
    throw new BusinessException(CommonErrorCode.E_300008);
}
alipayBean.setSubject(payOrderDTO.getSubject());
alipayBean.setBody(payOrderDTO.getBody());
alipayBean.setExpireTime("30m");
//请求支付通道，从数据库查询
//String appId, String platformChannel, String payChannel
PayChannelParaDTO payChannelParaDTO = payChannelService.queryParaByPlatformAndPayChannel(payOrderDTO);
String paraJson = payChannelParaDTO.getPara();
//支付请求参数
AliConfigParam aliConfigParam = JSON.parseObject(paraJson, AliConfigParam.class);
//字符编码
aliConfigParam.setCharset("utf-8");
```

画面5：展示网页端“应用设置”页面，其中包含支付ID、支付名称、支付通道等配置信息，以及右侧的HTML代码片段：
```html
<div class="box-container">
    <script type="text/javascript">
        var body = document.body;
        body.style.height = '100%';
        body.style.margin = '0';
        body.style.padding = '0';
        body.style.border = '0';
        body.style.overflow = 'hidden';
        body.style.position = 'absolute';
        body.style.top = '0';
        body.style.left = '0';
        body.style.width = '100%';
        body.style.height = '100%';
        body.style.zIndex = '9999';
    </script>
</div>
```

画面6：展示数据库表`pay_channel_para`的查询结果，包含ID、CHANNEL_NAME、MERCHANT_ID、PAY_CHANNEL、PARAM等字段。

画面7：展示IDE中`PaymentAgentServiceTool.java`文件，代码片段为：
```java
//构造支付客户端对象
AlipayClient alipayClient = new DefaultAlipayClient(url, appId, rsaPrivateKey, format, charset, alipayPublicKey);
AlipayTradeWapPayRequest alipayRequest = new AlipayTradeWapPayRequest();
model.setTradeNo(alipayBean.getOutTradeNo()); //商户的订单号，就是闪聚平台的订单号
model.setTotalAmount(alipayBean.getTotalAmount()); //订单金额（元）
model.setSubject(alipayBean.getSubject());
model.setBody(alipayBean.getBody());
model.setProductCode("QUICK_WAP_PAY"); //产品码，固定为QUICK_WAP_PAY
model.setTimeoutExpress("30m"); //订单超时时间
alipayRequest.setReturnUrl(returnUrl);
alipayRequest.setNotifyUrl(notifyUrl);
//请求支付宝下单接口，发起http请求
PaymentResponseDTO paymentResponseDTO = new PaymentResponseDTO();
```

画面8：展示IDE中`PaymentAgentServiceTool.java`文件，代码片段为：
```java
//请求支付下单接口，发起http请求
PaymentResponseDTO paymentResponseDTO = new PaymentResponseDTO();
```

画面9：展示HTML代码片段，包含表单和JavaScript代码：
```html
<form name="punchout_form" method="post" action="https://openapi.alipaydev.com/gateway.do?charset=utf-8">
    <input type="hidden" name="service" value="alipay.trade.wap.pay">
    <input type="hidden" name="partner" value="2088102183007750">
    <input type="hidden" name="out_trade_no" value="2020011513533000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
