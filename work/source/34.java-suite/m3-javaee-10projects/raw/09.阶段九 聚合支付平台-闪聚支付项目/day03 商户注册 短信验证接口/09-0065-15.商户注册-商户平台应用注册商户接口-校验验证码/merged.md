# 15.商户注册-商户平台应用注册商户接口-校验验证码

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\15.商户注册-商户平台应用注册商户接口-校验验证码【海量资源尽在 666java.com】.mp4
- 时长 11分59秒（音频 719s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们来继续来编写商户注册的接口当前呢我们是在商户平台应用来写的商户注册的接口它是给前端提供的一个http的一个接口刚才接口定义我们已经做完了现在呢我们再回到这个接口的序列图上边我们来看接口三的定义写完了现在呢我们要写实现我们看实现第一步要什么第二步是什么
[00:29] 第一步呢是要拿到我们说的验证码他要请求验证码服务来完成验证码的校验对不对校验通过之后他在远程调用double服务的接口来保存商务信息所以我们先做第一步再做第二步好第一步就是校验验证码没错吧所以各位我们看怎么写这个校验验证码呢我们回顾一下吧当初我们是怎么发送验证码的
[00:58] 当初我们是不是在Service这个smsservice当中写了一个叫发送验证码的方法然后这方法是不是给ctrl了它就调用那现在呢我们也可以参考原来的我们这里边来一个什么呀叫校验验证码你觉得行不行可以吧好校验验证码校验不通过呢就抛一层校验通过呢就这个方法正常执行所以呢返回值我不要了校验验证码
[01:29] 注意啊规则我告诉你了教验不通过抛一长教验通过这方法正常执行完成那教验验证码它需要什么参数呢一个是验证码一个是啥验证码的key大家还有印象吧对一个是验证码一个是验证码的key所以这个就是验证码对吧那还有一个啥验证码的key这个key我当时是不是说过就表示验证码
[01:58] 校验的依据还有印象吗对好那这个呢就是我们的什么参数这是验证码的key就是它的依据这是验证码对不对这个呢就是表示校验手机验证码那在这个接口写完了之后呢那笔葫芦画条吧原来你看您是咋写的原来发送的时候你是不是要在这使用
[02:29] rest template来发送请求啊对不对那现在呢我们是不是也可以比着葫芦画瓢啊怎么做呀首先呢我们得定义什么呀校验验证码的URLURL从哪拿呢那你得看验证码服务的这个手外格你看它这里头是不是有一个校验验证码看见吗这个是不是就是它的URL大家看懂了吗
[02:57] 对所以这就是它的URL搞进去但这里面大家看到啊它有很多的这个什么参数啊这个参数需要我们去把它给拼装起来你看这个内幕呢这是写死的那这个是我们说的验证码验证码验证码你这儿各位是不是得拼装量对不对然后呢还有啥验证码的key那你是不是在这儿是不是也要拼装量各位
[03:30] 我写到这大家清楚吗对吧也就是说我们拿到了这条验证码的URL然后呢把这两个参数呢放到URL准备怎么弄准备使用什么呀REST template来请求验证码服务对不对请求验证码服务是不是就请求这个URL嘛然后接下来REST template这个是get请求吧是不是那看一下是get请求吗
[04:01] 不要猜啊好像不是啊你看post的嘛两个都是post的所以原来你发送验证码的时候是怎么写的现在就可以这么写你看原来发送是这么做的我们是不是也可以这么做对不对这是URL这是post的对吧原来你发送验证码的时候你会发现我们是需要写一个请求头还有一个请求的体现在你校验验证码你看看校验验证码
[04:29] 那你会发现这个验证校验验证码它的参数都是在这个什么URL里面它并没有请求体是不是啊也并没有特殊的请求头啊所以我们觉得这儿就不需要了不需要了那你就写一个ampday为空是不是就完事了这就是校验验证码的请求大家看懂了吗那好那现在呢写到这儿的话原来你看人家是咋写的你参考你看
[04:59] 这儿是不是就你用一个什么try catch把它给捕获住为啥捕获住啊我不是跟你说了吗这里边我们是不是简单做一个简单的异常处理啊对原来人家是怎么写的咱们参考行不行哎现在呢这儿我们就这不就不是发送验证码失败了这叫验证校验验证码如果你报错了那就是校验验证码失败行不行
[05:28] 那当然你看原来人家是得到一个body对不对你把它提外边咱们是不是也提外边提外边那你这儿我们是不是就可以这么弄等于get a body是不是啊所以大家写代码的时候要多去参考啊多去参考那你这个响应我觉得也可以去把它拷过来你看可以吧这就是请求拿到响应然后呢补货一趟好那现在呢我们来看一下接下来要做的事呢
[06:01] 就和上面不太一样了上面做的你看它这是不是有一个叫如果它为空然后呢如果它result得不到然后就发送验证码错误是不是失败那现在呢我们来看那你这不能操量你这要看了这个校验验证码的结果你看是不是它你看这是不是响应的结果呀你想要的结果你看你最重要要的是resultresult等于true就表示校验通过result等于false就表示校验失败
[06:33] 对不对所以这里边我们要怎么写如果这就是body吗这个body是不是就是响应的内容响应的内容如果它为空或者说它get它为空或者或者啥或者它的值不是处那么我们认为它就教养失败我说的对吧那也就是它的值你要注意它是一个布尔类型
[07:03] 大家理解吗它是个布尔类型啊对如果这个布尔类型它为force为force我前面加一个非那是不是就为真的所以也就是或者它为真那么就表示交易业证码失败那这个代码你看懂吗如果它失败了这是一个force呀那么force非一下这是不是就是一个true啊大家理解吗就我这么写了看好啊好这就是我们说的
[07:32] 校验验证码如果这两个异常都不抛出我们你这个校验的过程这个方法是不是就顺利执行完成顺利执行完成就说明校验通过了对吧好那你这个校验验证码的方法写完了之后那你在哪调用还是肯错了所以在这呢我们先要去校验验证码校验验证码呢就刚才我们写SMSService然后呢你把
[08:02] 校验验证码的这个什么一个是key一个是code你把它传进来是不是就完事了如果校验通过如果不通过这就跑一场了就下面的代码就不执行了如果这通过了那这就开始调用double服务的结果大家看懂了吗好现在这就校验验证码了我就写完了那写完了之后有人说老师呢怎么测试一下看好啊我给你测试一下
[08:31] 原来我们发送验证码我们是不是已经测试过了发送验证码现在呢注意看啊我把它起起来我就开始发一下发完了之后呢我开始校验看好啊发送一个嗯这有个断点走看好这时候呢这里面是不是就拿到了这个key是不是有了再发一个这个key是不是有了那现在呢我们要去校验验证码我们要测试那怎么做
[09:04] 还是啊我们这里边新建一个叫校验验证码行吧然后呢在这个里边还是post啊校验验证码的URL是外个看好打开这是不是就是商户注册呀我们现在要校验验证码你是不是要测试这个商户注册了对不对我们要直接测试这个接口啊好那这个接口的话注意看
[09:34] 我里面要提交一些数据对不对然后呢执行一下其实就是执行它所以这个应该是这儿要改一下这叫商户注册是吧商户注册然后呢这写没问题吧然后呢body里边你现在因为现在我们注册的时候这提交这堆数据我们现在只用到了什么呀只用到了一个手机号对吧所以这里边你看好啊
[10:05] 这Jason写进去手机号随便输行吧验证码这里边不要随便输了刚才你发送验证码的这个key你是不是得写进去对吧验证码你再看验证码服务的这个控制台是不是他你把它写进去这是不是就是验证码这是不是就验证码的key然后现在呢我准备开始发送了对一发送啊它就会到我们刚才说的这个control这了
[10:36] 注意看啊就到这了然后呢点就进来了吧进来了之后现在你先看这个数据进来没有数据看这是请求的数据你看这是腌制码可以这是腌制码没错吧那现在呢我们注意看啊写进去然后呢我们在这打断点了啊在这注意看注意看点点然后呢我们让它放行走
[11:06] 是不是就进来了进来了之后大家来看吧现在你看看这个跟踪的数据校验最终是不是正常包在里边各位告诉我是不是校验通过这是不是就是我们说的校验验证码的测试就完事了对不对好那现在呢注意看啊注意看啊我再给你演示一个
[11:30] 演什么呀不是测成功了吗通常来说我们测试的时候你不用光测成功啊你得测异常呀比如说这个验证码我写错了再看我就执行同样的道理这里边你再跟踪你看看这个result是不是就变成false了验证码校验是不是就失败了看懂了吗对以上呢就是我们说的校验验证码的实现和测试我们就写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲商户注册流程中的短信验证码校验功能实现，包括前端接口、服务层代码、调用流程及测试验证。

2) 按时间顺序列出每张画面的要点：
画面1: 展示PPT页面“2.1.1 系统交互流程”，图中包含“消费者”、“商户平台”、“商户服务”、“Sms平台”、“验证到服务”等节点，通过箭头展示商户注册流程。
画面2: IDE中展示MerchantController.java文件，其中包含获取手机验证码和商户注册的两个接口方法，注解为@ApiOperation和@ApiModelProperty。
画面3: IDE中展示SmsServiceImp.java文件，代码中使用RestTemplate调用短信服务，处理响应并抛出异常。
画面4: IDE中展示SmsServiceImp.java文件，代码中定义了checkVerifyCode方法，用于校验验证码，其中包含URL拼接逻辑。
画面5: Postman中展示发送验证码的请求，参数为verifyKey和verifyCode，响应为200状态码。
画面6: IDE中展示SmsServiceImp.java文件，代码中处理短信服务响应，抛出异常。
画面7: IDE中展示SmsServiceImp.java文件，代码中定义了checkVerifyCode方法，用于校验验证码，其中包含URL拼接逻辑。
画面8: IDE中展示SmsServiceImp.java文件，代码中使用RestTemplate调用短信服务，处理响应并抛出异常。
画面9: IDE中展示MerchantController.java文件，代码中调用smsService.checkVerifyCode方法进行验证码校验。
画面10: Postman中展示响应头和响应体，响应体为JSON格式，包含code、msg、result字段。
画面11: Postman中展示发送短信验证码的请求，参数为phone，请求方法为GET。
画面12: IDE中展示MerchantController.java文件，代码中调用smsService.checkVerifyCode方法进行验证码校验。
画面13: IDE中展示调试信息，显示验证码校验成功，返回结果为true。
画面14: PPT页面“2.4.3.2 校验验证码实现”，展示在SmsService中定义校验验证码的Service接口和实现方法。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2:
```java
@ApiOperation("获取手机验证码")
@ApiModelProperty(value = "手机号", name = "phone", required = true, dataType = "String")
public String getVerifyCode(@RequestParam("phone") String phone) {
    return smsService.sendMsg(phone);
}

@ApiOperation("商户注册")
@ApiModelProperty(value = "商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
@PostMapping("/merchant/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    smsService.checkVerifyCode(merchantRegisterVO.getVerifyKey(), merchantRegisterVO.getVerifyCode());
    return null;
}
```

画面3:
```java
Map bodyMap = null;
try {
    exchange = restTemplate.exchange(sms_url, HttpMethod.POST, httpEntity, Map.class);
    Log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
    bodyMap = exchange.getBody();
} catch (RestClientException e) {
    throw new RuntimeException("发送验证码失败");
}
if (bodyMap == null || bodyMap.get("result") == null) {
    throw new RuntimeException("发送验证码失败");
}
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
Log.info("得到发送验证码对应的key:{}", key);
return key;
```

画面4:
```java
@Override
public void checkVerifyCode(String verifyKey, String verifyCode) {
    //校验验证码的url
    String url = "http://localhost:56085/sailing/verify?name=sms&verificationCode=" + verifyCode + "&verificationKey=" + verifyKey;
```

画面6:
```java
Log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
bodyMap = exchange.getBody();
} catch (RestClientException e) {
    throw new RuntimeException("发送验证码失败");
}
if (bodyMap == null || bodyMap.get("result") == null) {
    throw new RuntimeException("发送验证码失败");
}
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
Log.info("得到发送验证码对应的key:{}", key);
return key;
```

画面7:
```java
@Override
public void checkVerifyCode(String verifyKey, String verifyCode) {
    //校验验证码的url
    String url = "http://localhost:56085/sailing/verify?name=sms&verificationCode=" + verifyCode + "&verificationKey=" + verifyKey;
```

画面8:
```java
@Override
public void checkVerifyCode(String verifyKey, String verifyCode) {
    //校验验证码的url
    String url = "http://localhost:56085/sailing/verify?name=sms&verificationCode=" + verifyCode + "&verificationKey=" + verifyKey;
    //使用restTemplate请求验证码服务
    ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
    Log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
    bodyMap = exchange.getBody();
    if (bodyMap == null || bodyMap.get("result") == null) {
        throw new RuntimeException("校验验证码失败");
    }
}
```

画面9:
```java
@ApiOperation("商户注册")
@ApiModelProperty(value = "商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
@PostMapping("/merchant/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    smsService.checkVerifyCode(merchantRegisterVO.getVerifyKey(), merchantRegisterVO.getVerifyCode());
    return null;
}
```

画面12:
```java
@ApiOperation("商户注册")
@ApiModelProperty(value = "商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
@PostMapping("/merchant/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    smsService.checkVerifyCode(merchantRegisterVO.getVerifyKey(), merchantRegisterVO.getVerifyCode());
    return null;
}
```

画面13:
```java
try {
    //使用restTemplate请求验证码服务
    ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
    Log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
    bodyMap = exchange.getBody();
    if (bodyMap == null || bodyMap.get("result") == null) {
        throw new RuntimeException("校验验证码失败");
    }
    if (bodyMap.get("result").equals("true")) {
        Log.info("验证码校验成功");
        return true;
    }
}
```

画面14:
```java
/**
 * 校验验证码，抛出异常则校验无效
 * @param verifyKey 验证码key
 * @param verifyCode 验证码
 */
void checkVerifyCode(String verifyKey, String verifyCode);

public void checkVerifyCode(String verifyKey, String verifyCode) {
    //实现校验验证码的逻辑
    String url = smsUrl + "/verify?name=sms&verificationCode=" + verifyCode + "&verificationKey=" + verifyKey;
    ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
    try {
        //请求校验验证码
        ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: 标题“2.1.1 系统交互流程”，图中“消费者”指向“商户平台”，“商户平台”指向“商户服务”，“商户服务”指向“Sms平台”，“Sms平台”指向“验证到服务”，“验证到服务”指向“商户平台”。
画面14: 标题“2.4.3.2 校验验证码实现”，图中“在SmsService中定义校验验证码的Service接口”指向“在SmsServiceImpl中定义校验验证码的Service实现方法”。

5) 无。

