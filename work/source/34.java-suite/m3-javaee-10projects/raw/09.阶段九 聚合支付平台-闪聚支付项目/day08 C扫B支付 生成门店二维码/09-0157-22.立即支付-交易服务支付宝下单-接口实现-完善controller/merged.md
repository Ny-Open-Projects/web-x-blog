# 22.立即支付-交易服务支付宝下单-接口实现-完善controller

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\22.立即支付-交易服务支付宝下单-接口实现-完善controller【海量资源尽在 666java.com】.mp4
- 时长 9分4秒（音频 544s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下边呢我们继续来实现交易服务的支付宝下单那么刚才我们已经实现了交易服务的保存订单然后呢调支付渠道代理服务下单那接下来是不是就剩了一个肯错了就是当前台呢一点确认立即支付然后呢就请求到这里这里呢是不是就要调我们刚才写的那个方法了那么调这个我们说的Submit Order by Ali这个方法
[00:29] 我们就需要注因为当前都是交易服务所以这个注入呢我们就auto wear就行了transaction Service好然后呢这儿呢我们就可以在这儿来让它掉对吧还掉一下你看掉的时候这里边你看它需要一个参数它需要一个参数是啥参数呢叫做pay order DTO需要这个参数需要这个参数的话那你就在这儿给它溜一个
[01:00] 拗完了之后主要是往里边放数据嘛他需要什么数据呢他需要的数据你得看接口他需要就是拿到订单的信息保存然后呢再干嘛再去调这个你看这是不是支付渠道代理服务的然后呢支付渠道代理服务调支付宝的是吧所以这里边各位就是你这拿到几个信息啊
[01:28] 你看你接收到的是它吧所以我们我觉得可以这么玩就是咱们这么做咱们直接我直接呢我们看有可以可以给它转一下那就用converter我们把它转一下你看行不行对吧里头你看你点开然后呢我们把这个给它放开当初我们考的工具类嘛就这个转换那么我们现在呢把它把它放开了之后呢各位你看
[01:57] 这个方法是不是就是把我们接收前台的订单信息转成我们pay order的DTO啊对但是有一点你看你这个你看能看懂吗叫啥呀对忽略金额的转换不要转金额为啥啊为啥因为支付宝需要的是什么支付宝要的是原哎我们呢可能是需要去特殊处理一些东西的怎么做呀注意看啊然后呢我们先把它给转换一下得到得到我们要的
[02:28] 这个DTO这个转换是不是就完工了完工了之后呢我们就可以把它放进去这样我们是不是就得到了这个响应对吧拿到了这个响应这儿的代码还有啊你点点点啊一会儿我还写然后呢拿到了这个响应刚才调这个过程是不是就实现了保存订单然后呢调用支付渠道代理服务的
[02:57] 支付宝下单各位你告诉我咱们前边讲的是不是就是这方法然后呢你最终是不是就得到了响应啥响应这是什么响应啥响应这个就是支付宝下单它的接口的响应而这个接口的响应是非常重要的为什么因为最终我们它响应的就是一个HTML
[03:26] 对吧因为我们要把它输出一下懂吧这就是我们完善这个方法的目的啊哎我们把它输出一下那输出的话那你就把它直接填进去就行了对不对哎把它填进去这样的话我们是最终啊把它输出完了之后呢我们就可以去怎么弄去把它给哎响应给前端响应到前端了之后呢啊我们是不是就可以
[03:57] 前端的用户去支付了对来我们把这个异常给他抛一下直接这么弄好这么弄是吧然后呢他需要了一些这个这个这个这我加一个这样行吧好好可以了然后各位这个方法大家都知道是啥意思了然后也就是说现在我们做的这个东西啊就是最终要向前端去响应一个html
[04:39] 对吧那么拿到一个天然爆客户端呢就可以去支付但是现在呢前面我还空着呢前面是啥就是要准备一些数据然后这个方法我们是需要一些订单信息由他的保存订单还有去调用这个支付渠道代理服务的让他去调支付宝是吧所以这里边呢我们就把它给补充一下这里边需要什么呢页面有的你不用填就是这里边有的你不用填因为你都已经给他转换
[05:08] 到这里头了你看掉了一个converter是吧没有的你需要填没有啥商户ID没有你就需要填那商户ID没有的话那怎么拿到呢那你就需要去先拿到应用ID有人说老师你咋知道商户ID没有那还不简单吗你打开页面瞧瞧就知道了你看一下这就是页面你给我看看你看这里头没有商户ID吧
[05:35] 没有是吧所以其实我们说这个页面的参数是正好对应这个VO的在VO里边没有商户ID它就是没有所以这里边我们就拿到了应用ID获得应用ID干啥呢因为我们就是为了拿商户因为应用所属的商户我们可以查出来对不对那我就可以去调用我们这应用这个服务这个服务是在商户平台所以我这肯定是reference
[06:05] 远程调用所以这里面我们就可以得到应用的信息拿到应用信息之后我们就可以从中取出商户这是不是就是商户的ID我是不是就搞定了这里头还需要传啥信息呢商户的ID没有各位你再点开你看这里头商户我们是不是搞定了知道ID这个是什么叫做
[06:34] 支付渠道的编码基本上这些信息是不是都有了还有一个东西你得设还有啥还有一个就是说你从前端传进来的是这个金额是什么单位啊大家思考一下前端传进来的是元对不对那前端传进来是元但是你要保存数据库保证到我们散去平台数据库的是分啊所以你这里边呢还要把
[07:03] 你别忘了刚才我转换的时候都让你看了这个把这个什么金额的这个复制给忽略了吗是吧因为你前端页面写的用户写的是元嘛所以这里边呢我们要往里边放一个金额哎这个金额呢从前端这拿过来这个金额要做一件事是啥事啊对转换这个转换的话就需要怎么弄啊对就需要我们来调用由元转成分对不对
[07:32] 所以这样的话我们是不是就可以得到了这个金额了你看需要啥这是个integerinteger的话我们就需要来转换一下我们是不是就可以把它填进去我问你这一步大家理解吧这就是我们说是将前端输入的语言转成分因为分最终是存到我们这个散据数据库的没错吧
[08:02] 好然后还需要什么呢还需要一些比如说这个IP地址也就是客户端的这个IP我们可以从request当中来拿到对IPIP的话这里边在这里边我们找一下它这里边是不是有一个叫client IP吧client IP这里边呢我们是需要有一个工具类我们可以去拿到的request我们就拿到了这个客户端的IP基本上信息
[08:32] 就是说页面就是我们需要的页面上基本上都有的因为没有的我们你看在这去处理一下就行了这是我们说的客户端的IP好这样的话我们是不是就完善了这个支付宝门店下单的这个接口这是什么意思你把它要写进去好那这样的话我们就完成了整个的这个交易服务支付宝下单的开发稍后呢我们就可以来进行
[09:02] 测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring MVC 项目中实现支付宝支付功能，包括控制器方法、订单数据转换、调用支付服务以及前端页面交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示 PayController.java 文件中的 @PostMapping("/createAllPayOrder") 方法。
- 方法接收 OrderConfirmVO 和 HttpServletRequest、HttpServletResponse 参数。
- 方法内调用 PayOrderConvert.INSTANCE.vo2to() 方法转换对象。
- 方法内调用 transactionService.submitOrderByAll() 方法提交订单。
- 方法内设置响应内容类型并写入 HTML 页面。

画面2：
- 展示 PayController.java 文件中的 @RequestMapping("/pay-entry/{ticket}") 方法。
- 方法接收 ticket 参数并进行 Base64 解码。
- 方法内创建 PayOrderDTO 对象并进行 JSON 解析。
- 方法内设置 PayOrderDTO 的属性。
- 方法内调用 PayOrderConvert.INSTANCE.vo2to() 方法转换对象。

画面3：
- 展示 PayController.java 文件中的 @Override public PaymentResponseDTO submitOrderByAll(PayOrderDTO payOrderDTO) throws BusinessException 方法。
- 方法内设置 payOrderDTO 的 tradeNo、channel、body、subject、totalAmount 等属性。
- 方法内调用 paymentService.submitOrderByAli() 方法提交订单。
- 方法内返回 PaymentResponseDTO 对象。

画面4：
- 展示 PayController.java 文件中的 @PostMapping("/createAllPayOrder") 方法。
- 方法内调用 PayOrderConvert.INSTANCE.vo2to() 方法转换对象。
- 方法内调用 transactionService.submitOrderByAll() 方法提交订单。
- 方法内设置响应内容类型并写入 HTML 页面。

画面5：
- 展示 PayController.java 文件中的 @PostMapping("/createAllPayOrder") 方法。
- 方法内调用 PayOrderConvert.INSTANCE.vo2to() 方法转换对象。
- 方法内调用 transactionService.submitOrderByAll() 方法提交订单。
- 方法内设置响应内容类型并写入 HTML 页面。

画面6：
- 展示 Typora 编辑器中的文档内容。
- 文档标题为“5.4.3 测试”。
- 文档内容包括测试步骤：1. 扫码进入支付入口，进入支付确认页面；2. 输入金额，点击确认支付。
- 文档内容还包括“5.4.3.2 请求代理服务调用支付下单”、“5.4.3.3 完整交易服务下单接口”等小节。

画面7：
- 展示 PayController.java 文件中的 @PostMapping("/createAllPayOrder") 方法。
- 方法内调用 PayOrderConvert.INSTANCE.vo2to() 方法转换对象。
- 方法内调用 transactionService.submitOrderByAll() 方法提交订单。
- 方法内设置响应内容类型并写入 HTML 页面。

画面8：
- 展示 OrderConfirmVO.java 文件中的类定义。
- 类包含多个私有属性，如 appId、tradeNo、openId、storeid、channel、body、subject、totalamount。
- 类包含注释说明每个属性的含义。

画面9：
- 展示 pay.html 文件中的 HTML 代码。
- 代码包含表单元素，如 input、button。
- 代码包含 JavaScript 脚本，用于处理支付逻辑。
- 代码包含注释说明支付流程。

画面10：
- 展示 PayController.java 文件中的 @RequestMapping("/pay-entry/{ticket}") 方法。
- 方法接收 ticket 参数并进行 Base64 解码。
- 方法内创建 PayOrderDTO 对象并进行 JSON 解析。
- 方法内设置 PayOrderDTO 的属性。
- 方法内调用 PayOrderConvert.INSTANCE.vo2to() 方法转换对象。

画面11：
- 展示 PayOrderDTO.java 文件中的类定义。
- 类包含多个私有属性，如 merchantId、storeId、appId、tradeNo、subject、body、totalAmount、currency、extra、authCode、device、clientIp、psChannel、tradeState。
- 类包含注释说明每个属性的含义。

画面12：
- 展示 PayController.java 文件中的 @PostMapping("/createAllPayOrder") 方法。
- 方法内调用 PayOrderConvert.INSTANCE.vo2to() 方法转换对象。
- 方法内调用 transactionService.submitOrderByAll() 方法提交订单。
- 方法内设置响应内容类型并写入 HTML 页面。

画面13：
- 展示 PayController.java 文件中的 @PostMapping("/createAllPayOrder") 方法。
- 方法内调用 PayOrderConvert.INSTANCE.vo2to() 方法转换对象。
- 方法内调用 transactionService.submitOrderByAll() 方法提交订单。
- 方法内设置响应内容类型并写入 HTML 页面。

画面14：
- 展示 Typora 编辑器中的文档内容。
- 文档标题为“5.4.3 测试”。
- 文档内容包括测试步骤：1. 扫码进入支付入口，进入支付确认页面；2. 输入金额，点击确认支付。
- 文档内容还包括“5.4.3.2 请求代理服务调用支付下单”、“5.4.3.3 完整交易服务下单接口”等小节。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
// 支付宝下单接口，跳转订单确认页面，点击确认支付，请求进来
@Param orderConfirmVO 订单信息
@Param request
@Param response
@ApiOperation("支付宝门店下单付款")
@PostMapping("/createAllPayOrder")
public void createAllPayOrderForStore(OrderConfirmVO orderConfirmVO, HttpServletRequest request, HttpServletResponse response) {
    // 使用支付通道代理服务，实现第三方支付的下单
    // 跳转到确认.html (h5) 页面
}
```

画面2：
```java
@RequestMapping("/pay-entry/{ticket}")
public String payEntry(@PathVariable("ticket") String ticket, HttpServletRequest request) throws Exception {
    // 准备默认支付需要的数据
    String jsonStr = EncryUtil.decodeUTF8StringBase64(ticket);
    // 将对象的属性转成json字符串
    PayOrderDTO payOrderDTO = JSON.parseObject(jsonStr, PayOrderDTO.class);
    // 原始客户端的类型（请求、支付）
    String params = ParseUtil.parseURLParam(payOrderDTO);
}
```

画面3：
```java
@Override
public PaymentResponseDTO submitOrderByAll(PayOrderDTO payOrderDTO) throws BusinessException {
    payOrderDTO.setChannel("ALIPAY_WAP"); // 交付渠道
    // 存在订单时，不重复提交
    PayOrderDTO save = save(payOrderDTO);
    // 调用支付通道代理服务，实现第三方支付的下单
    PaymentResponseDTO paymentResponseDTO = alipayHS(save.getTradeNo());
    return paymentResponseDTO;
}
```

画面4：
```java
// 支付宝门店下单接口，跳转订单确认页面，点击确认支付，请求进来
@Param orderConfirmVO 订单信息
@Param request
@Param response
@ApiOperation("支付宝门店下单付款")
@PostMapping("/createAllPayOrder")
public void createAllPayOrderForStore(OrderConfirmVO orderConfirmVO, HttpServletRequest request, HttpServletResponse response) {
    PayOrderDTO payOrderDTO = PayOrderConvert.INSTANCE.vo2to(orderConfirmVO);
    // 调用支付通道代理服务，实现第三方支付的下单
    // 跳转到确认.html (h5) 页面
}
```

画面5：
```java
// 支付宝门店下单接口，跳转订单确认页面，点击确认支付，请求进来
@Param orderConfirmVO 订单信息
@Param request
@Param response
@ApiOperation("支付宝门店下单付款")
@PostMapping("/createAllPayOrder")
public void createAllPayOrderForStore(OrderConfirmVO orderConfirmVO, HttpServletRequest request, HttpServletResponse response) {
    PayOrderDTO payOrderDTO = PayOrderConvert.INSTANCE.vo2to(orderConfirmVO);
    // 调用支付通道代理服务，实现第三方支付的下单
    // 跳转到确认.html (h5) 页面
}
```

画面6：
```text
5.4.3 测试
1、扫码进入支付入口，进入支付确认页面
2、输入金额，点击确认支付
```

画面7：
```java
// 支付宝门店下单接口，跳转订单确认页面，点击确认支付，请求进来
@Param orderConfirmVO 订单信息
@Param request
@Param response
@ApiOperation("支付宝门店下单付款")
@PostMapping("/createAllPayOrder")
public void createAllPayOrderForStore(OrderConfirmVO orderConfirmVO, HttpServletRequest request, HttpServletResponse response) {
    PayOrderDTO payOrderDTO = PayOrderConvert.INSTANCE.vo2to(orderConfirmVO);
    // 调用支付通道代理服务，实现第三方支付的下单
    // 跳转到确认.html (h5) 页面
}
```

画面8：
```java
/**
 * @Author Administrator
 * @Version 1.0
 * @description 订单确认信息
 */
public class OrderConfirmVO {

    private String appId; // 应用ID
    private String tradeNo; // 订单号
    private String openId; // 客户ID
    private String storeId; // 店铺ID
    private String channel; // 订单类型
    private String body; //

