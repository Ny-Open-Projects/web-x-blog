# 14.支付入口-解析ticket-测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\14.支付入口-解析ticket-测试【海量资源尽在 666java.com】.mp4
- 时长 4分5秒（音频 246s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下面呢我们就来测试一下啊这个支付入口然后呢对我们说这个ticket的进行解析那我们要测试这个对ticket的解析啊我们就需要先生成这个支付入口的url对吧你只有生成了这个url之后呢我们是不是就可以去请求一下然后呢去跟踪代码了那么这个生成的啊我们啊最早期我们是其实已经啊生成过一个url在这儿对吧
[00:29] 当然现在呢咱们也可以再去生成一遍对吧那你要生成URL的话那怎么做呢怎么做呢那肯定是需要我们在哪里啊因为现在还是我们还没有实现完整的功能啊只是做了一半我们想先测一下那我们找到我们当初做的这个什么代码然后呢就在这儿这儿是不是一个生成二维码呀然后呢我建议你在这打断点
[00:57] 然后我们打开我们的postman我们是不是就可以来生成一个二维码是不是那么生成二维码这时候我们是不是就拿到了这个二维码这个url拿到url你把它拷出来然后呢放在这那现在呢各位我们是不是就可以去浏览器去请求这个地址对那请求的话我们提前在
[01:26] 这个支付入口站呢我们打一个断点然后呢咱一步一步的让他走然后看好好就没有进来啊看见了吗所以现在我们要做的事是不是要走这个地址啊对吧走这个地址他现在没有进来啊那现在呢我们把它重启一下啊我们写完了之后需要把它重启一下看一下大家可以看到现在你后边请求的一堆是不是就是贝斯六四边嘛
[02:02] 然后当请求到我们说的这个地址上来的话那么它就会解析这个tag先对base64进行这个解码然后呢转对象好咱们来看进来了进来之后我们先看一下它这个json数据能不能解对这个一定要你看是不是就解析出来了解析出来这个json数据之后呢现在它是不是要转对象然后呢拿参数看好现在你看好因为这个是我们调的工具类嘛
[02:33] 你现在看它这个参数得到一个什么结果你看你把它考出来看看好它是不是就是把我们刚才说对象里面的属性一个一个的拼成这种key value然后key valuekey value是不是这种方式然后呢就可以对完成那看懂了吧就这么一个过程其实现在你会发现这个数据都已经显示出来了为什么因为页面
[03:03] 当初我们是从资料文件夹直接拿过来要求大家会读得懂里面的这个代码就行了那么各位你可以看到你比如说这里边有一个什么叫做你看这个像三家副管这是一个title你看最上边是不是有一个叫取subject而取subject这事不就是从请求当中拿参数你看这一堆当中
[03:29] 这一堆这个KVL串当中这个参数串里面是不是有一个叫subject你看见吗有吧那这个subject是不是就是被我们说这个free market的页面取到然后呢在这展示大家能看到吗对这就是我们说的一个支付入口的一个什么整个take it解析部分我们是不是就把这个效果测试出来了好那么
[03:58] 这个第一部分就是这个解析ticket我们就完成了后边我们再说解析客户端好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

