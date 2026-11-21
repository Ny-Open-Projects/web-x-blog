# 16.获取支付结果-支付渠道代理支付宝订单查询-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\16.获取支付结果-支付渠道代理支付宝订单查询-接口实现【海量资源尽在 666java.com】.mp4
- 时长 17分13秒（音频 1034s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来实现支付渠道代理查询支付宝的接口刚才我们完成了接口的定义下面呢我们找到支付渠道代理的接口实现工程然后呢咱们把这个接口呢实现一下那么这个接口他要做的是什么呢就是要去查询支付宝的订单状态对吧那么有人说老师这个怎么查呢
[00:25] 当初我们研究过下单接口我们也是需要看支付宝的文档对吧然后呢看他的这个文档格式要求等等我们去做所以我们点开他的文档来瞧一瞧这个就是他的这个交易结果的一个查询接口刚才其实我们都已经看过他的公共请求参数和他的额外请求参数等等那我们要看啥呢对我们看这个这是不是就是他提供的针对SDK的一些样例代码呀
[00:54] 所以其实这个很重要对我们可以把这个考到我们这个代码当中我们考过去之后呢各位我们就需要把它改造成我们需要的代码然后呢最终完成查询就OK了吧首先呢各位看第一个还是要去创建一个AliPay Client对吧各位我们前面做过下单其实下单接口当初是不是也创建了这么一个
[01:21] 阿里佩Client有印象吗你看是不是在这儿呢那各位你知道我干啥了吧我们原来做下单的这一堆代码咱们是不是就可以直接拿来用了呀没错就这么做成了吧这是不是就是拿到支付渠道参数然后呢把它取出来然后呢就构造成一个阿里佩Client大家看到了吗
[01:49] 当初我们做下单的时候这个代码我只拿过来重用那么这个搞定了接下来呢接下来你看创建一个请求对象跟原来一样嘛你要是还想看看有没有啥可考的我们再看看对吧这是个请求吧请求对象是吧还有一个东西你看model咱们是不是要往里边放model呀那好呀那么我们看一看我们还是参考原来的拿过来行不行
[02:18] 哎 抱错了不着急啊我们看一下这是个请求对象没有错吧猫的对象我们之前说过猫的对象是不是就和这个里边的接针串是等价的对吧那我们在这个里边准备放什么是不是就放我们的订单号啊订单号在这儿呢你看这不就是订单号吗看到了吗哎 这样这一堆我们就不要了是不是就不要了
[02:43] 不要了有人说老师那你这个model你怎么设置进去你看我们当初说过你可以设BIZ content你也可以设BIZ model懂吧这次效果是一样的你把它给干掉你看马上就快诞生了对吧这是啥呀这不就是我们说的请求吗这一句就是请求支付宝的什么这个
[03:13] 订单的状态查询接口就说白了就是要查询了嘛这还有一个你看它还有一个异常是吧那这个异常的话首先呢我们我觉得咱们这个接口你可以抛出我们一个自定义的异常这是无可厚非的吧因为我们好多的这个接口都要这么做对吧但是呢
[03:40] 你抛出自定义常归你抛出自定义常呀关键你看他这个他这个是不是也要往外抛他自己的这个阿里配的一个异常呀那针对这种情况我就建议你啊对你千万不要把我们方法的这个自定义常给他覆盖了啊我们对单独补一下这大家理解吧好这样的话就相当于我们呢
[04:03] 去请求了支付宝的订单状态查询接口如果有异常那肯定是请求过程出错了对吧出错了要怎么处理那出错了肯定是不能给他返回一个成功对吧出错了一定是给他返回一个什么失败那么我们先说成功再说出错行吧那这个得到响应了之后呢你拿到响应之后你最终你是不是要返回这个类型啊
[04:30] 对我最重要我其实就要返回这里边有一个叫Sexess的一个静态方法你看见吗对我要返回它那这个Sexess这个静态方法大家可以看到它的参数啊它的参数我们呢来一块捋一下你看它这有很多存在方法我们返回这个这个参数我们需要把它填进去看懂了吗那这参数都是啥呀第一个参数是哎你看前两个都是订单号你告诉我第一个是啥
[05:00] 第一个是支付宝的对支付宝的这个什么订单号第二个这是商户的订单号也就是我们散剧平台的订单号懂吧最这第三个参数是什么呢是叫我们的订单的状态注意啊我们现在你看这个类是谁的类是我们的啊是散剧平台的类啊
[05:30] 懂吧我们散去平台的那散去平台我们专门定义的这么一个类型就是用来去去封装这个支付结果的懂了吧所以我们现在要让他传回这个payment response DTO那里面我们要用一个静态方法这个size要干嘛对要让他把这个对象给构建起来而这个静态方法他需要什么他需要几个参数一个是这个订单号你看订单号网上都有应该是你看
[05:57] 原始渠道的订单号就是指的是支付宝或微信的订单号对吧这个是我们散剧平台的订单号自己的订单号所以我们就调用他这个订单方法就把这个对象给他构建出来了对不对那我们还没有说完啊就这儿这个订单状态啊这订单状态我们不妨也点进去瞧一瞧这个订单状态我跟你说这也是我们散剧平台的这是我们系统自己的订单状态懂吧所以各位就问题来了就是你这几个
[06:27] 这个内容你知道了这是返回的这个信息支付宝返回的信息我们怎么往里边填对吧那我们得拿Response我们看看这里头有没有有吧对不对再拿还有是不是那你再往后拿好像就拿不到了这是不是一个订单状态这是我们自己的类型那我们自己的类型这咋弄不太好弄了所以这里边你要注意我们
[06:57] 还要解析支付宝返回的什么状态那最终的目标啊是把它解析成我们散聚对散聚平台的什么这个状态就是这个类型懂我意思吧对我要做这件事啊做这件事好了那么各位什么时候解析呢你刚才也看接口了吗
[07:24] 就是说如果他响应的这个code注意看如果他响应的这个code必须是什么是1万的时候就表示接口调用成功了看见了吗所以各位我们需要做一件事你要拿到他响应的这个code懂吧这个必须是1万才能才能往下继续解析明白吗这是支付宝
[07:52] 响应的什么扣的一万对表示接口调用成功懂了所以这里边呢我们要做一件事那做啥事义父判断就是满足这个一万要求的那义父判断有人说一万那很简单呀那你我这么写不就行了吗你看一万一扣OK了吧对这样写了有点low因为我们知道
[08:22] 它有很多的状态你不能都把它硬编码到我们代码中啊所以这个时候呢我们可以在我们散剧平台配一个什么对配一个常量的类型专门用来把这个状态呢给它统一管理起来我觉得这样比较合适啊所以呢我们在这个支付区道代理这边呀我们准备创建一个专门存放常量的这个包啊然后呢我们建一个常量的类型对
[08:51] 那这个藏量类型大家也看到了里边存的是啥呀对就是支付宝的这些什么状态的标识而这个状态的标识正是我们程序要用到的东西看见了吗里边是不是有一个1万对吧另外下边就是支付宝返回的交易状态懂了吧好所以那我们这呢就可以这么来写了怎么写注意看我们就可以写成这个藏量里边有一个叫Sexes
[09:22] 是不是就是一万对这样我们这个代码写起来是更优雅一些然后呢如果说他借口调用成功那接下来我不是说了吗还要解析他的什么解析他的状态啊而这个解析状态解析什么状态了呀你看借口他解析这个trade state就他你再打开文档你看往上翻往前翻看这是不是他有一个叫做
[09:52] 然后翻啊请求想要有一个叫你看就是他这是我们说的四个状态嘛我们要解析他了他返回的是他自己的状态码嘛我们把它解一层我们散去平台的这个状态嘛散去平台的状态在哪呢在这儿了你看我们专门有一个叫trade states你看对不对所以我们要解析那怎么解析呢怎么解析呢这么弄啊我们打开讲义我们准备这么做
[10:21] 我们专门写一个简单的这个私有方法来做这件事对吧好那这样的话我就在这写一个叫什么解析支付宝的什么订单状态为散具为散具平台的什么状态那怎么解析呢你需要给我传东西吧你给我传支付宝它
[10:51] 得到的什么这个状态然后呢我们把它解析解析解析成什么我们系统自己的这个类型看懂了吧那么这个类型你打开它是一个枚举类型对吧里边是不是有五种状态那好那下面呢我们就做一个解析那咋解析啊那我们是不是就可以用switch然后呢咱们把它放进去我们这里头是不是就可以去去写了呀怎么写呀
[11:20] 大家看一下我switch我是不是就可以把它拿到然后呢case一个一个来判断这样是不是就OK了没错吧好我们来瞧一瞧啊那这里边呢我们呢就需要把它给注意我们把它处理一下把它处理一下啊这儿有点报错我们把它处理一下然后呢这儿是不是就是case然后那你需要解析你看刚才我们是不是添了一个藏料的类型啊那这个藏料的类型正好我们用到你看它这里边有什么呀
[11:50] 有这个有很多的吧有这个比如说这个订单关闭订单完成订单完成应该就是我们说的最终成功了吧你看订单完成你点开是不是就是它那这个呢你还是需要对文档咱们不要在这瞎猜你看这比如交易结束不可退款就说明支付成功了还有一种是交易支付成功对不对这两种所以其实我觉得是这样的我们再回来我们说这一种
[12:19] 还有一种这一种这是这个成功吧对这两个我觉得都应该是什么都应该是对到我们这个系统的状态就是成功这个大家理解吧大家你也看了吗说这两个状态一个是交易结束不可退款就说明成功了一个是交易支付成功所以这两个状态呢对到我们这个系统都是成功对不对那还有什么呢还有
[12:48] 那你得还是还要打开它的接口你看它还有一个叫交易创建还有一个未付款交易超时关闭是吧还有一个关闭那你这也照样写比如说K字然后呢它返回的这个值是关闭那它返回的是关闭呢那对到我们这应该对我们也是要有一个状态吧你看一下是不是有一个叫
[13:19] 明确失败对吧然后我们交易撤销对吧他关闭我们就表示撤销对吧就这样是吧所以按照我们说的我们一个一个把这个状态呢给他给同时把它一个一个的给他我们这还有一个失败失败我们就默认失败吧反正就是总而言之我们把接口里边的这个字母串然后转成我们这个自己的状态我们一个一个看一下关闭
[13:49] 测销然后再来然后还有什么呢刚才你也看到了是还有一个叫做嗯这个是不是就是表示交易中啊是吧交易中那交易中的话对到我们这个订单状态应该是啥呀你看看对到我们的状态应该是应该也有一个你看这个就表示我们的交易新建等待对吧那么还有呢那如果上面都不匹配呢
[14:22] 都不匹配我们目前认为就是订单目前来说是失败了对不对好这样可以吧对这样的话我们是不是就把这个订单的状态给它解析出来了对你把它填进去填进去之后那我问你你是不是就拿到了一个这个订单状态拿到这个订单状态了之后我们是不是就可以把它放进去大家看懂了吗咱们是不是就可以把它放进去然后呢就把这个
[14:51] 状态这是我改一下这是Stream这支不串是吧然后呢你就拿到一个枚举类型的状态枚举类型状态这儿呢我们就可以返回了用了然后呢RaceBounce呢它从事其实也给我们了一个信息我们不管是啥信息反正我们全部给它返回因为是支付渠道代理服调接口它可以把接口的信息呢传回去各位这个是不是就写好了这就是说当我们说调用成功准备返回这个那有时候老师呢如果是失败了
[15:20] 对最后呢最后我觉得他就是失败了对反正这个状态他失败了但是他这个我只是未知吧这个状态属于就不知道这个状态到底是啥是吧所以呢其实我们可以给他一个信息吧比如说叫支付宝订单状态查询失败可以吧那按照他的要求你看是不是还要填订单号吗还有一个
[15:49] 就这个我们系统自己的状态我们有一个unknown就是未知状态大家理解吗对这就是我们的查询支付宝订单结果的一个接口咱们是不是就写完了那么基本的流程很简单就是调支付宝的这个接口来查
[16:10] 但是这点有点小麻烦就是查出来之后支付宝呢它是一堆支付串它有自己的状态码我们呢需要把它转成我们平台自己的这么一个美嘴类型那我们就需要一个一个的判断了我写一个sale方法一个一个判断当支付宝的这个结果它是这个支付串的时候那么我们呢就让它变成我们自己的美嘴类型大家看懂了吗好我给你加个标识吧这个呢就表示我们的
[16:41] 叫啥是不是交易支付明确成功量这个是叫啥是不是交易已撤销就说白了就是关闭了对吧然后呢这个是咱们再回来这个是啥吗是不是就交易新建等待支付对最后是啥就是交易失败对前面如果都不匹配的那就交易失败大家看懂了吗好这就是我们实现的支付渠道代理服务查询支付宝
[17:11] 接口

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

