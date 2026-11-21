# 15.获取支付结果-支付渠道代理支付宝订单查询-接口定义

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\15.获取支付结果-支付渠道代理支付宝订单查询-接口定义【海量资源尽在 666java.com】.mp4
- 时长 6分15秒（音频 376s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢,我们就来实现支付渠道代理来查询支付宝的交易状态。
[00:06] 根据刚才技术方案,我们知道最终是由支付渠道代理服务来调用支付宝的接口来查询支付结果。
[00:15] 所以现在呢,我们先把这个查询支付宝支付结果的这个接口我们先实现,到后边我们再去发消息,让他自己消费,最后呢,和交易服务做通信等等整个过程。
[00:29] 好我们先做一个最基础的啊就是要来查询支付宝的定单的支付结果那大家打开支付宝的文档啊这里边各位支付宝提供了好多的接口前边我们统一下单其实都已经学过是这个接口对吧那么下边这个支付交易状态的查询应该是用这个接口好那么这个接口各位我们说
[01:00] 接口我们已经看了好多了怎么样去看一个接口理解一个接口的定义我们首先要知道这个接口的职责以及请求响应参数没错吧这个接口呢就是支付宝提供的用来查询订单支付状态的一个接口对吧好那我们来看吧它的参数是什么前面呢我们学过下单接口我们知道那请求参数是不是有一部分是公共参数
[01:29] 这部分公共参数比如说APP ID公司要等等这些我们前边了解过就不再说了然后接下来我们再看支付状态查询的接口它需要额外的自己的一些请求三数各位这是有四个对吧这里边大家看到我圈了一个这一个是我们要传的因为我们要查询咱们订单的支付状态
[01:58] 当初在下单的时候我们散剧平台的订单号是不是传给了支付宝所以我们去查询的时候呢仍然可以拿着散剧平台的订单号去查这个他的支付状态大家理解吗有时候老师后边还有好几个参数难道我们不用管吗不用管我们只需要传我们散剧平台的订单号就行了就可以查到什么他的支付结果好请求参数我们搞定了啊就是公共的参数以及一个散剧平台的
[02:27] 订单号那么请求过去之后呢我们就拿到响应响应仍然是有一些公共的响应前面我们也说过了那里面是不是有一个代码对吧如果是你这次请求成功那么这个代码呢就是一万应该还有同学有印象你可以查一下这个详细的文档有说明那么当他是一万的情况下呢各位他这时候呢就是我们请求成功了嘛他就会给我们响应这个订单的状态这个订单状态大家可以看到有四个
[02:57] 有四个这四个状态呢我们还需要去解析对吧那这四个状态到底是啥呢我们先看一下吧这表示刚开始订单创建的时候等待付款这个是一个状态还有一个叫交易关闭还有交易成功然后呢交易结束这是四个状态后面我们就要把这个这个叫trade state这个状态这个值给它取到然后呢
[03:24] 我们把它解析成我们自己系统所要的结果对吧我们自己系统想要什么结果你看我们系统自己的状态你看叫订单生成支付中支付成功处理完成关闭对不对所以这几个呢都是最终我们要根据支付宝的这个渠道的状态我们把咱们这个数据库的这个订单状态呢把它更新一下好回头我们再解析啊先不看它那么这个接口各位
[03:54] 我们是不是基本上就捋完了请求响应的参数大家都知道了吧那接下来呢我们就可以来定义接口吧这个接口呢是支付渠道代理他所提供的那么我们要想请求支付宝的订单结果查询刚才你也看到了他是不是需要一堆公共参数以及一个散剧平台的订单号对吧所以这个接口在定义的时候就是支付渠道代理服务要提供一个参数各位
[04:24] 是啥参数啊那肯定是首先得有一个订单号其次呢还得有什么就是我们配置的那一堆支付渠道参数对吧好那下面呢我们就来定义打开我们的支付渠道代理服务那下面我们是在支付渠道代理服务定一个查询将来这个接口呢会去查询什么支付宝的订单结果
[04:55] 好在这儿其实到这个支付这儿呢各位一般来说我们查这个支付的这个状态呢我们都用这个返回值是payment response DTO啊然后呢它的这个参数呢刚才咱也说了需要这个支付渠道的参数支付渠道参数阿里的这个支付渠道参数不就是在这里头吗这是支付宝的支付渠道参数是吧那还有一个刚才你也看到了是啥呀是
[05:24] 订单号这订单号是我们散聚平台的订单号然后呢咱们把这个接口描述写一下这就是我们说的查询支付宝的什么订单状态那么这个呢因为你要调支付宝接口嘛这就是支付渠道的参数当初我们配置的一堆比如说APP ID公司要这是散聚平台的什么
[05:56] 订单号这个接口各位我们是不是就定义好了那么有了这个接口后边我们是不是就可以去查看样例代码然后呢调支付宝的订单状态查询接口来查询了那我们呢先把接口定义好好先到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何通过支付宝交易状态查询接口，结合 RocketMQ 消息队列，实现支付结果异步通知与订单状态更新的完整技术方案。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示技术文档目录，定位到“6.4.1 支付宝交易状态查询接口”章节，介绍其核心功能。
画面 2: 展示支付流程图，说明支付渠道代理服务通过 RocketMQ 异步通知交易服务，完成订单状态更新。
画面 3: 展示“6.4.1.1 请求参数”表格，列出公共请求参数，如 app_id、method、format、sign_type、timestamp、version、app_auth_token、biz_content。
画面 4: 展示“6.4.1.1 请求参数”表格，重点突出业务请求参数 out_trade_no，并附带一个图片链接。
画面 5: 展示“6.4.1.2 响应参数”表格，列出公共响应参数 code、msg、sub_code、sub_msg、sign，以及响应参数 trade_no、out_trade_no、buyer_logon_id、trace_status、total_amount。
画面 6: 展示数据库表结构，表名为 `shop_pay_transaction`，包含字段如 TRADE_NO、MERCHANT_ID、STORE_ID、APP_ID、PAY_CHANNEL、PAY_CHANNEL_MCH_ID、PAY_CHANNEL_MCH_APP_ID、PAY_CHANNEL_TRADE_NO、OUT_TRADE_NO、SUBJECT。
画面 7: 展示“6.4.1.2 响应参数”表格，重点展示响应参数 trace_status 的值及其含义。
画面 8: 展示接口定义代码，定义了 `queryPayOrderByAli` 方法，参数为 `AliConfigParam` 和 `String outTradeNo`。
画面 9: 展示“6.4.1.1 请求参数”表格，再次强调业务请求参数 out_trade_no。
画面 10: 展示 IDE 中的项目结构，包含 `shanjiuyapay-payment-agent-Service` 模块，以及 `WxPayConfigCustom` 类的代码，用于配置微信支付参数。
画面 11: 展示 IDE 中的项目结构，包含 `shanjiuyapay-payment-agent-Service` 模块，以及 `AliConfigParam` 类的代码，用于配置支付宝参数。
画面 12: 展示 `AliConfigParam` 类的代码，定义了配置参数如 appid、rsaPrivateKey、notifyUrl、returnUrl、url、charset、format。
画面 13: 展示接口实现部分，引用了 `AliCodeConstants` 类，用于定义支付宝返回的状态码常量。
画面 14: 展示接口实现部分，再次强调 `AliCodeConstants` 类用于定义支付宝返回的状态码常量。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```text
参数	类型	是否必填	最大长度	描述	示例值
app_id	String	是	32	支付宝分配给应用的ID	201407230
0007148
method	String	是	128	接口名称	aliPay_trade_query
format	String	否	40	请求的编码格式，如UTF-8,gbk,gb2312等	JSON
charset	String	否	10	请求字符集编码，如UTF-8,GBK等	UTF-8
sign_type	String	是	10	签名类型，详见签名	RSA2
timestamp	String	是	344	商户请求参数的时间，格式“yyyy-MM-dd HH:mm:ss”	2014-07-24
03:07:50
version	String	是	3	调用的接口版本，目前为：1.0	1.0
app_auth_token	String	否	40	详见应用授权地址
biz_content	String	否	40	详见应用授权地址
```

画面 4:
```text
业务请求参数中out_trade_no即闪聚支付平台订单号，根据此订单号查询支付状态。
```

画面 5:
```text
公共响应参数
参数	类型	是否必填	最大长度	描述	示例值
code	String	是	-	网关返回码	详见文档	40004
msg	String	是	-	网关返回信息	详见文档	Business Failed
sub_code	String	否	-	业务返回码，详见具体的API接口文档	AQO_TRADE_HAS_SUCCESS
sub_msg	String	否	-	业务返回信息，详见具体的API接口文档	交易已返回支付
sign	String	是	-	签名	详见文档	DXNk8eTuhAYE3r1v...（省略）
响应参数
参数	类型	是否必填	最大长度	描述	示例值
trade_no	String	必填	64	支付交易号	2013112011001004300
out_trade_no	String	必填	64	商户订单号	6823788399979248
buyer_logon_id	String	必填	100	买家支付宝账号	159****5032
trace_status	String	必填	32	交易状态，详见文档	TRADE_CLOSED
total_amount	String	必填	11	交易金额，单位为元，两位小数。该笔交易的支付金额	88.88
```

画面 8:
```java
/**
 * 支付交易状态查询
 * @param aliConfigParam 支付渠道参数
 * @param outTradeNo 闪聚平台订单号
 * @return
 */
PaymentResponseDTO queryPayOrderByAli(AliConfigParam aliConfigParam, String outTradeNo);
```

画面 10:
```java
class WxPayConfigCustom extends WxPayConfig{
    @Override
    protected String getAppID() { return appID; }
    @Override
    protected String getMCHID() { return mchId; }
    @Override
    protected String getKey() { return key; }
}
```

画面 11:
```java
public class AliConfigParam implements Serializable {
    //应用ID
    public String appid;
    //私钥
    public String rsaPrivateKey;
    //异步通知地址
    public String notifyUrl;
    //同步通知地址
    public String returnUrl;
    //支付平台
    public String url;
    //编码方式 UTF-8
    public String charset;
    //格式 JSON
    public String format;
}
```

画面 13:
```java
package com.shanjiuyapay.paymentagent.common.constant;

/**
 * 支付宝查询返回状态码常量类
 */
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 架构图
- 支付渠道代理服务 → 1. 发送支付结果查询消息 → RocketMQ
- 支付渠道代理服务 → 2. 支付结果查询消息 → 并发支付结果消息
- RocketMQ → 4. 消费支付结果查询消息 → 并更新订单支付结果 → 交易服务
- 交易服务 ← 3. 支付渠道代理服务 → 支付结果 → 更新订单状态

画面 3: 表格数据
- 参数: app_id, method, format, charset, sign_type, timestamp, version, app_auth_token, biz_content
- 类型: String
- 是否必填: 是, 是, 否, 否, 是, 是, 是, 否, 否
- 最大长度: 32, 128, 40, 10, 10, 344, 3, 40, 40
- 描述: 支付宝分配给应用的ID, 接口名称, 请求的编码格式, 请求字符集编码, 签名类型, 商户请求参数的时间, 调用的接口版本, 详见应用授权地址, 详见应用授权地址
- 示例值: 201407230007148, aliPay_trade_query, JSON, UTF-8, RSA2, 2014-07-24 03:07:50, 1.0, 详见应用授权地址, 详见应用授权地址

画面 5: 表格数据
- 公共响应参数: code, msg, sub_code, sub_msg, sign
- 响应参数: trade_no, out_trade_no, buyer_logon_id, trace_status, total_amount

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

