# 画面线理解：14.支付入口-解析ticket-测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\14.支付入口-解析ticket-测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:33, 00:50, 01:08, 01:23, 01:36, 01:55, 02:09, 02:19, 02:34, 02:56, 03:09, 03:47, 04:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:55:49

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中，如何通过控制器接收并解析支付票据（ticket），生成支付 URL 并转发到支付页面，同时展示了相关代码、调试过程和前端页面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PayController 中的 @RequestMapping("/pay-entry/{ticket}") 方法，用于处理支付票据，解析 JSON 字符串并生成 URL。
画面 2: 在 PayController 中，高亮显示了将 JSON 字符串解析为 PayOrderDTO 对象的代码。
画面 3: 展示了 TransactionService.java 文件，其中包含生成支付票据的逻辑，包括设置商户信息、编码和返回 URL。
画面 4: 展示了 TransactionService.java 中的 verifyAppIdAndStoreId 方法，用于验证商户 ID 和店铺 ID。
画面 5: 展示了调试器中的变量窗口，显示了生成的支付 URL。
画面 6: 展示了前端支付页面，包含“立即支付”按钮。
画面 7: 展示了 PayController 中的 @RequestMapping("/pay-entry/{ticket}") 方法，用于处理支付票据。
画面 8: 展示了项目启动日志，显示了 Spring Boot 应用的启动过程。
画面 9: 展示了 PayController 中的 @RequestMapping("/pay-entry/{ticket}") 方法，用于处理支付票据。
画面 10: 展示了调试器中的变量窗口，显示了生成的支付 URL。
画面 11: 展示了前端支付页面，包含“立即支付”按钮。
画面 12: 展示了 pay.html 文件，其中包含表单元素和隐藏字段。
画面 13: 展示了 pay.html 文件，其中包含表单元素和隐藏字段。
画面 14: 展示了 Typora 文档，其中包含支付接口测试的目录结构和 IP 配置信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@RequestMapping("/pay-entry/{ticket}")
public String payEntry(@PathVariable("ticket") String ticket, HttpServletRequest request) throws Exception {
    //1.准备确认页面所需要的参数
    String jsonStr = EncryptUtil.decodeUTF8StringBase64(ticket);
    PayOrderDTO payOrderDTO = JSON.parseObject(jsonStr, PayOrderDTO.class);
    //对对象的属性值组成一个url?key=value
    String params = ParseURLPairUtil.parseURLPair(payOrderDTO);
    return "forward:/pay-page?"+params;
}
```

画面 3:
```java
//用表单参数初始化
PayOrderDTO payOrderDTO = new PayOrderDTO();
payOrderDTO.setMerchantId(merchantId);
payOrderDTO.setAppId(merchantId);
payOrderDTO.setStoreId(merchantId);
payOrderDTO.setSubject(ChannelUtil.getChannelName(channelId)); //商户名称
payOrderDTO.setChannel(channelId);
payOrderDTO.setTotalAmount(amount);
//基于json
String json = JSON.toJSONString(payOrderDTO);
//base64编码
String ticket = EncryptUtil.ENCODE_UTF8_STRING_BASE64(json);
return url;
```

画面 4:
```java
//私有，验证商户应用ID和店铺ID的合法性
private void verifyAppIdAndStoreId(Long appId, Long storeId) {
    Boolean boolean = appService.queryAppMerchant(appId, merchantId);
    if (!boolean) {
        throw new BusinessException(CommoErrorCode.E_200005);
    }
}
```

画面 5:
```java
//支付URL
String url = "http://127.0.0.1:56010/transaction/pay-entry?ticket=" + ticket;
```

画面 6:
```html
<html>
<head>
    <title>测试页面</title>
</head>
<body>
    <div class="content">
        <img src="/logo.png" alt="logo" />
        <p class="name">【RequestParameters】subject</p>
    </div>
    <div class="form-container">
        <form id="form" action="" method="post">
            <input type="hidden" id="appId" name="appId" value="【RequestParameters】appId"/>
            <input type="hidden" id="openId" name="openId" value="【RequestParameters】openId"/>
            <input type="hidden" id="channel" name="channel" value="【RequestParameters】channel"/>
            <input type="hidden" id="outTradeNo" name="outTradeNo" value="【RequestParameters】outTradeNo"/>
            <p>商品名称：<span>【RequestParameters】subject</span></p>
            <p>商品数量：<span>【RequestParameters】num</span></p>
            <p>商品单价：<span>【RequestParameters】price</span></p>
            <p>商品总价：<span>【RequestParameters】totalAmount</span></p>
            <p>支付类型：<span>【RequestParameters】payType</span></p>
            <p>支付方式：<span>【RequestParameters】payWay</span></p>
            <p>支付状态：<span>【RequestParameters】payStatus</span></p>
            <p>支付时间：<span>【RequestParameters】payTime</span></p>
            <p>支付备注：<span>【RequestParameters】remark</span></p>
            <p>支付渠道：<span>【RequestParameters】channel</span></p>
            <p>支付商户：<span>【RequestParameters】merchantId</span></p>
            <p>支付店铺：<span>【RequestParameters】storeId</span></p>
            <p>支付金额：<span>【RequestParameters】totalAmount</span></p>
            <p>支付币种：<span>【RequestParameters】currency</span></p>
            <p>支付类型：<span>【RequestParameters】payType</span></p>
            <p>支付方式：<span>【RequestParameters】payWay</span></p>
            <p>支付状态：<span>【RequestParameters】payStatus</span></p>
            <p>支付时间：<span>【RequestParameters】payTime</span></p>
            <p>支付备注：<span>【RequestParameters】remark</span></p>
            <p>支付渠道：<span>【RequestParameters】channel</span></p>
            <p>支付商户：<span>【RequestParameters】merchantId</span></p>
            <p>支付店铺：<span>【RequestParameters】storeId</span></p>
            <p>支付金额：<span>【RequestParameters】totalAmount</span></p>
            <p>支付币种：<span>【RequestParameters】currency</span></p>
            <p>支付类型：<span>【RequestParameters】payType</span></p>
            <p>支付方式：<span>【RequestParameters】payWay</span></p>
            <p>支付状态：<span>【RequestParameters】payStatus</span></p>
            <p>支付时间：<span>【RequestParameters】payTime</span></p>
            <p>支付备注：<span>【RequestParameters】remark</span></p>
            <p>支付渠道：<span>【RequestParameters】channel</span></p>
            <p>支付商户：<span>【RequestParameters】merchantId</span></p>
            <p>支付店铺：<span>【RequestParameters】storeId</span></p>
            <p>支付金额：<span>【RequestParameters】totalAmount</span></p>
            <p>支付币种：<span>【RequestParameters】currency</span></p>
            <p>支付类型：<span>【RequestParameters】payType</span></p>
            <p>支付方式：<span>【RequestParameters】payWay</span></p>
            <p>支付状态：<span>【RequestParameters】payStatus</span></p>
            <p>支付时间：<span>【RequestParameters】payTime</span></p>
            <p>支付备注：<span>【RequestParameters】remark</span></p>
            <p>支付渠道：<span>【RequestParameters】channel</span></p>
            <p>支付商户：<span>【RequestParameters】merchantId</span></p>
            <p>支付店铺：<span>【RequestParameters】storeId</span></p>
            <p>支付金额：<span>【RequestParameters】totalAmount</span></p>
            <p>支付币种：<span>【RequestParameters】currency</span></p>
            <p>支付类型：<span>【RequestParameters】payType</span></p>
            <p>支付方式：<span>【RequestParameters】payWay</span></p>
            <p>支付状态：<span>【RequestParameters】payStatus</span></p>
            <p>支付时间：<span>【RequestParameters】payTime</span></p>
            <p>支付备注：<span>【RequestParameters】remark</span></p>
            <p>支付渠道：<span>【RequestParameters】channel</span></p>
            <p>支付商户：<span>【RequestParameters】merchantId</span></p>
            <p>支付店铺：<span>【RequestParameters】storeId
