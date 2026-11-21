# 18.立即支付-支付渠道代理支付宝下单-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\18.立即支付-支付渠道代理支付宝下单-接口实现【海量资源尽在 666java.com】.mp4
- 时长 13分25秒（音频 805s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来实现支付渠道代理服务的支付宝下单接口在刚才我们把这个接口定义好了之后呢下面呢我们就在支付渠道代理服务的实现工程中我们这里边呢我们新建一个包叫Service好然后在这里边呢写一个接口的实现类好由于这个接口将来啊也要被交易服务远程调用所以这里边我们用double的Service注解然后呢我们让它实现
[00:30] 我们刚才定义的这个接口好那我们现在呢来思考一下这个接口要怎么写呢其实这个接口职责很明确就是要调支付宝的下单调支付宝的下单接口呢在当初我们都已经研究过了大家还有印象吗这对代码是不是就是调支付宝的下单接口首先是不是要创建一个SDK的客户端的对象然后准备请求
[01:00] 参数然后这儿是不是就开始调用所以这样我们把这一堆代码呀咱们把它考到咱们要马上要写的这个实现类的工程对吧考进去之后呢很多代码呢我们是把它改造一下就可以了在实际的企业开发当中呢很多情况也是这样啊那大家呢更多的去干嘛去利用以前写的代码可以提高我们的工作效率这里边各位看一下
[01:30] 这需要一些参数啊有私钥呀有APPID根据前面我们的分析这个行参当中第一个行参是不是就存储了这些APPID私钥公钥等这些参数啊所以其实我们的思路很简单我们呢就从第一个行参当中来把这些东西拿到对吧那第一个呢这叫支付宝的什么公钥
[01:57] 我们就这样一个一个的拿你需要什么拿什么你比如说第一个需要一个什么叫URL就是支付宝的这个接口的网关地址所以这个当初我们在支付渠道参数配置的时候都配了那你这里头就可以直接来拿对吧支付宝的什么接口的网关地址对就按照我说的这种方法我们把这些全部的拿到
[02:27] 这是我们说的这个支付宝的应用的ID吧就是沙洋环境你开通了之后是不是给你这么一个ID对然后还需要一个私钥这是应用的私钥好然后呢这个format呢其实我们也配置了这是进行我们说进行格式化的一个什么Jason对吧我们当初在
[02:59] 写这个测试的时候啊这是我们说的一个json格式啊json格式然后还有什么那还有一个算法签名算法的类型还有一个编码那这个编码其实也有那还是虽然这个编码我们一般都是utf-1所以这里边我建议还是要从这个形态当中去取啊因为你毕竟是一个被别人调用的接口然后这里边最后一个其实就是我们说的签名算法
[03:33] 对吧好这样的话我们是不是就把这些参数填进去就可以了吧好format就这样一个一个填因为接口将来是交易服务去调用交易服务调的话你看啊千万不要填错了你看我这刚才就填错了哪填错了你看这是私钥吧你别付出错了你付出错你接口你可就调不通了后边是一个
[04:04] 编码后边是不是材质公要对吧然后最后是一个签名算法好搞定吧搞定了之后呢我们下面再来看这一堆是不是就是业务参数了业务参数当初我们是不是在设置到一个叫BIZ content的这个属性当中是一个json chart对吧其实它还有一个还有一个叫做什么setBIZ看好是不是有一个叫model对那这个呢
[04:31] 这两个方法效果是一样的这个呢只是往里边设尖串这个呢是设对象对吧设对象其实你可以看一下这个你看它其实是有一个什么有一个这个这个这个这个对象的一个类型的对吧那我们打开讲义看一下我们用的是哪个对象的类型啊也就是我们要往里边设model对吧呃设model的话你可以用我们当初的这个例子就是直接往里边放尖串也可以
[05:00] 定义一个专门的model的对象那这个model的对象有什么好处呢你看这里面你看是不是通过属性这些参数都看起来非常明白啊所以这里边呢我们就不用这个了不用这个了以后我现在呢先把它平了以后把它删掉然后呢我们看这里边需要什么呢需要什么呢model里边往里边填什么东西然后你看是不是就放在了BID model里头了你先把下面这四个的补齐了
[05:30] 对吧一个是需要啊out of trade number这是啥这指的是我们商户的订单商户的订单其实就是我们散剧平台的订单懂了意思吧哎所以那业务参数是不是统一都在第二个形态呀所以你从这里边来拿就行了对吧哎然后还有这里边还有一个什么呀你看
[05:59] 有一个什么叫订单的金额对吧订单的金额订单的金额这里面我说一下订单的金额的话因为这也在形态当中啊也在形态当中呢注意这里边有一个问题你要注意这个我们当初定义接口的时候就说了这个类型啊专门是调支付宝接口的时候是不是要用的那支付宝的这个它的这个金额
[06:26] 它这个类型啊我们不妨看一下它应该是有固定的要求的什么固定要求呢就是你要么是元要么是分大家看支付宝要求的是元大家看到了吧所以所以我们呢要在这加一个注释其实这个要求的是元后面将来交易服务掉这个接口给它塞这个金额这个数值的时候一定要把它转换成元
[06:52] 那在这个支部取到代理服务站呢他拿到的数据一定是原所以这里面呢他就直接可以从行山当中来取出放进去就行了这就是订单的什么金额对吧然后金额刚才我也说了它是原这个单位然后还有这是subject就是订单的标题标题呢那就是传什么我取什么就行了然后还有
[07:22] body订单的描述嗯那OK还有什么呢后面是不是还有一个叫产品的代码产品的代码这个下单接口产品的代码其实统一为叫quickwap为这接口上有要求吗所以我们就把它写死就行了然后站上来就把它干掉了嗯你看这个参数我基本上是不是就整理齐了
[07:47] 但是其实还有一些参数啊这还有啥参数你得打开参数列表来瞧然后统一过一下吧你比如说还有一个return URL那虽然这个是你看这是不是必填的吧不是必填你可以不用管它但是你说如果咱们的项目有要求你填那你就需要取其实这个return URL当初我们也是对也是拿到的也是在支付渠道参数配置这里边当初我们就是配置的
[08:16] 对你都可以把它取出来取出来之后呢这儿呢你都可以把它给放进去都可以放进去我看一下return URLreturn URL应该是在这儿应该是在这儿对吧return URL然后呢notify URL对也就是说呀这个接口啊你外边给我传这两个我呢也会给你放进去但是这两个是什么URL啊我说一下啊这个就是说
[08:51] 支付成功跳转的URL跳转到的URL而这个呢就是我们说的支付结果一步通知的URL也就是支付宝要掉这个URL这个URL一定是我们系统的对吧那这两个URL都是我们散去平台的还有什么呢来看一下还有什么再打开这里头这些是不是都设过了
[09:20] 这个也有这个是SDK帮我们弄对吧这个也是SDK帮我们设不用管它Notify这个也有了这个当初我刚才我们是用了BIZ model是吧body这个订单号有了还有一个叫什么呀叫订单的最晚付款时间但是这个是一个否我们先不管它还有一个叫订单金额是不是收过了这个是SDK帮我们弄不用管产品代码
[09:51] 这个也是否啊这也是公用回传的一个参数或者需要了我们再去啊列我们打开讲义看一下我们讲义当中的代码我们大概过一下啊这些参数呢必填项我们是先要首先去看啊还有一个订单的过期时间啊订单的过期时间订单过期时间呢当前我们虽然还暂时用不到但是我们也把它写上去啊订单过期时间呢你也可以从这里头取因为将来交易服务传的时候他也会给你传哎错了啊
[10:21] 也会给你传进来这个吧是吧好这几个是不是都写完了吧那各位那我写完了之后呢咱这儿是不是就开始去请求支付宝来下单了那你请求支付宝下单我们是不是就可以调这个当初我们研究过这个APM我们是不是就可以拿到这个结果了对不对拿到哪个结果拿到
[10:54] 支付宝给我们响应的结果这是不是就是响应了你最终你是不是返回值是这个类型所以你得定义这么一个类型的对象然后呢你把支付宝给你响应的内容放到这个里边的content这个属性中懂我意思吧所以我们将来交易服务是不是就能拿到这个什么
[11:23] 类型了吧拿到这个类型对象里边是不是就有我们说的支付宝的响应内容响应结果看懂这个过程了吧好那这个就不要了吧如果当然如果说在调用的时候出错了你这儿是不是得抛出一个异常呀抛出异常抛出异常呢这里边呢我们得看有没有这个错误代码我们进去看一下你看这是有个
[11:52] 支付渠道代理服务微信确认支付失败那我们再增加一个增加一个比如说叫支付宝确认支付失败对吧那我问你到这儿为止我们这个代码基本上我是不是就写完了但是如果正常情况下的话你是要把这个结果返回的作为这个接口的结果返回这个就不需要了这个接口就是我们说支付渠道代理服务呀
[12:24] 他呢专门提供一个面向支付宝的一个什么下单接口将来根据我们说的接口交互流程字我们要做一件什么事啊就是交易服务拿到用户的请求交易服务要调支付渠道代理服务支付渠道代理服务刚才我们写的接口呢他才会请求支付宝或微信来下单所以支付
[12:49] 渠道代理服务它的作用就是把交易服务和外部系统进行一个结偶合所以所有的这种第三方的接口对接都在支付渠道代理服务这样我们的交易服务就相对稳定很多整个接口的逻辑也比较简单就是汇总数据然后使用支付宝SDK然后最终调支付宝下单接口拿到响应返回这个接口结果
[13:18] 好这个接口的实现这个代码我们就写完了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

