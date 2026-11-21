# 画面线理解：16.获取支付结果-支付渠道代理支付宝订单查询-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\16.获取支付结果-支付渠道代理支付宝订单查询-接口实现【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:06, 02:10, 03:31, 04:39, 06:21, 08:05, 09:07, 10:07, 11:40, 13:15, 15:06, 16:09, 17:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:14:14

1) 这一组画面整体在讲如何通过 Java 代码实现对支付宝交易状态的查询，并将支付宝返回的状态码转换为内部定义的 TradeStatus 枚举状态。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了项目结构和核心方法 `queryOrderByAll` 的定义，其中包含对 `alipayBean`、`allConfigParam` 和 `outTradeNo` 的注解说明。
画面 2: 展示了 `queryOrderByAll` 方法的实现，创建了 `AlipayClient` 并构造了 `AlipayTradeQueryRequest`，调用 `execute` 方法查询订单状态。
画面 3: 展示了 `AlipayClient` 的初始化代码，设置了 `outTradeNo`、`trade_no`、`org_pid` 等参数，并构造了 `AlipayTradeQueryRequest`。
画面 4: 展示了方法签名和抛出的异常类型，包括 `BufferOverflowException`、`BufferUnderflowException` 等。
画面 5: 展示了 `success` 方法的声明，用于返回 `PaymentResponseDTO` 对象。
画面 6: 展示了 `TradeStatus` 枚举类，包含 `SUCCESS`、`FAILED`、`UNKNOWN`、`USERPAYING`、`REVOKED` 等状态。
画面 7: 展示了 `AlipayClient` 的初始化代码，设置了 `outTradeNo` 和 `model`，并构造了 `AlipayTradeQueryRequest`。
画面 8: 展示了 `ALiCodeConstants` 类，定义了支付宝交易状态码，如 `SUCCESSCODE`、`PAYMENTCODE`、`FAILED CODE`、`ERRORCODE`。
画面 9: 展示了 `queryOrderByAll` 方法中，通过 `AllCodeConstants.SUCCESSCODE` 判断交易成功，并调用 `convertAllTradeStatusToShanjuCode` 方法。
画面 10: 展示了 `convertAllTradeStatusToShanjuCode` 方法的 `switch` 语句，用于将支付宝状态码转换为内部状态。
画面 11: 展示了 `switch` 语句中 `case` 分支，将 `TRADE_FINISHED`、`TRADE_SUCCESS`、`TRADE_CLOSED` 等状态映射到内部枚举。
画面 12: 展示了 `convertAllTradeStatusToShanjuCode` 方法中，将 `TradeStatus` 转换为 `PaymentResponseDTO` 对象。
画面 13: 展示了 `AlipayClient` 的初始化代码，设置了 `outTradeNo` 和 `model`，并构造了 `AlipayTradeQueryRequest`。
画面 14: 展示了 PPT 页面，标题为“6.4.2.3 接口测试”，内容为 `convertAllTradeStatusToShanjuCode` 方法的代码实现。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
/**
 * @param alipayBean 业务参数（商户订单号，订单地址，订单描述。）
 * @return 一组统一PaymentResponseDTO
 */
public PaymentResponseDTO queryOrderByAll(ALLConfigParam allConfigParam, String outTradeNo) {
```

画面 2:
```java
public PaymentResponseDTO queryOrderByAll(ALLConfigParam allConfigParam, String outTradeNo) {
    AlipayClient alipayClient = new DefaultAlipayClient("https://openapi.alipay.com/gateway.do", 
        "app_id", "private_key", "format", "charset", "alipayPublicKey");
    AlipayTradeQueryRequest request = new AlipayTradeQueryRequest();
    request.setBizContent("{" +
        "\"out_trade_no\":\"2015032001010001\", " +
        "\"trade_no\":\"2014112611001004680 079556707\", " +
        "\"org_pid\":\"208810111952222\", " +
        "\"query_options\":\"TRADE_SETTLE_INFO\" " +
        "}");
    AlipayTradeQueryResponse response = alipayClient.execute(request);
    if (response.isSuccess()) {
        System.out.println("调用成功");
    } else {
        System.out.println("调用失败");
    }
    return null;
}
```

画面 3:
```java
//根据商户订单号查询订单
AlipayClient alipayClient = new DefaultAlipayClient(url, appid, realPrivatekey, format, charset, alipayPublicKey);
AlipayTradeQueryRequest request = new AlipayTradeQueryRequest();
AlipayTradeQueryModel model = new AlipayTradeQueryModel();
model.setOutTradeNo(alipayBean.getOutTradeNo()); //商户的订单，就是闪购平台的订单
model.setTradeNo(alipayBean.getTradeNo());
model.setTotalAmount(alipayBean.getTotalAmount());
model.setSubject(alipayBean.getSubject());
model.setBody(alipayBean.getBody());
model.setProductCode("QUICK_MSEC_PAY"); //产品代码，返回QRTZC_MSEC_PAY
model.setTimeoutExpress(alipayBean.getExpireTime()); //订单超时时间
model.setNotifyUrl(returnUrl);
try {
```

画面 4:
```java
public PaymentResponseDTO queryOrderByAll(ALLConfigParam allConfigParam, String outTradeNo) throws biz
```

画面 5:
```java
success(String, String, TradeStatus) (in com.shanju.pay.payment.agent.dto.PaymentResponseDTO)
success(String, String, TradeStatus, String) (in com.shanju.pay.payment.agent.dto.PaymentResponseDTO)
```

画面 6:
```java
package com.shanju.pay.payment.agent.api.dto;

public enum TradeStatus {
    SUCCESS, // 业务交易支付 明确成功
    FAILED, // 业务交易支付 明确失败，
    UNKNOWN, // 业务交易状态未知，
    USERPAYING, // 交易待，等待支付
    REVOKED, // 交易已撤销
}
```

画面 7:
```java
AlipayClient alipayClient = new DefaultAlipayClient(url, appid, realPrivatekey, format, charset, alipayPublicKey);
AlipayTradeQueryRequest request = new AlipayTradeQueryRequest();
AlipayTradeQueryModel model = new AlipayTradeQueryModel();
model.setOutTradeNo(outTradeNo); //商户的订单，就是闪购平台的订单
request.setBizModel(model);
```

画面 8:
```java
public static final String SUCCESSCODE = "10000"; // 支付成功时返回的接口调用成功
public static final String PAYMENTCODE = "10001"; // 用户付款
public static final String FAILED CODE = "40004"; // 失败
public static final String ERRORCODE = "20000"; // 异常
```

画面 9:
```java
//String tradeNo(支付订单号) String outTradeNo(闪购平台的订单号) TradeStatus tradeState(订单状态) String msg(返回信息)
PaymentResponseDTO success(String tradeNo, String outTradeNo, TradeStatus tradeState, String msg) {
```

画面 10:
```java
private TradeStatus convertAllTradeStatusToShanjuCode(String aliTradeStatus) {
    switch (aliTradeStatus) {
```

画面 11:
```java
case AliCodeConstants.TRADE_FINISHED:
    return TradeStatus.TRADE_SUCCESS;
case AliCodeConstants.TRADE_SUCCESS:
    return TradeStatus.SUCCESS;
case AliCodeConstants.TRADE_CLOSED:
    return TradeStatus.TRADE_CLOSED;
```

画面 12:
```java
//String tradeNo(支付订单号) String outTradeNo(闪购平台的订单号) TradeStatus tradeState(订单状态) String msg(返回信息)
PaymentResponseDTO success(String tradeNo, String outTradeNo, TradeStatus tradeState, String msg) {
    PaymentResponseDTO response = new PaymentResponseDTO();
    response.setTradeNo(tradeNo);
    response.setOutTradeNo(outTradeNo);
    response.setTradeState(tradeState);
    response.setMsg(msg);
    return response;
}
```

画面 13:
```java
//根据商户订单号查询订单
AlipayClient alipayClient = new DefaultAlipayClient(url, appid, realPrivatekey, format, charset, alipayPublicKey);
AlipayTradeQueryRequest request = new AlipayTradeQueryRequest();
AlipayTradeQueryModel model = new AlipayTradeQueryModel();
model.setOutTradeNo(outTradeNo); //商户的订单，就是闪购平台的订单
request.setBizModel(model);
```

画面 14:
```java
/**
 * 将支付宝查询订单状态trade_status 转换为 闪购订单状态
 * @param aliTradeStatus 支付宝交易状态
 * WAIT_BUYER_PAY (交易创建，等待买家付款)
 * TRADE_CLOSED (未付款交易超时关闭，或支付完成后全额退款)
 * TRADE_SUCCESS (交易支付成功)
 * TRADE_FINISHED (交易结束，不可退款)
 * @return
 */
private TradeStatus convertAllTradeStatusToShanjuCode(String aliTradeStatus) {
    switch (aliTradeStatus) {
        case AliCodeConstants.WAIT_BUYER_PAY:
            return TradeStatus
