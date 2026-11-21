# 04.商户注册-异常处理-抛出自定义异常测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\04.商户注册-异常处理-抛出自定义异常测试【海量资源尽在 666java.com】.mp4
- 时长 5分28秒（音频 329s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们就来测试一下我们要抛出自定义异常是否可以让全局异常处理器呢帮助我们捕获然后呢返回给前端所需要的error code和error message好那现在呢我们来看怎么去抛出异常呢这个抛出的异常就是我们抛出可预知的异常就是程序员在编写代码的时候呢抛出对吧所以大家来看啊当初啊我们去写的时候呢
[00:27] 我们是不是写了一个叫做校验验证码的这个方法对不对对吧校验验证码在哪呢这是发送验证码下面是不是校验验证码这里边有很多异常抛出的点这里边我给大家举一个例子其他的大家可以自己去把它改成抛出自定义一场首先抛出自定义一场大家一定记着在接口上边我们要声明我们抛出的是business exception就是这个然后呢
[00:58] 生命完了之后呢我们在这儿好然后在这里边呢它你看这儿我们就要把它给注射掉了这是不是就是验证码骄厌失败啊那这里边我们要让它抛啊抛什么就是另一个business特别简单你看对吧但是这个构造方法你看它是不是要error code呀对吧error code刚才我给大家考了一个叫做comer error code你还记不记了
[01:30] 这里边有很多现成的错误代码你看比如说验证码校验失败你看验证码错误是不是有一个看见了吗所以这里边你就可以直接在这写看对这就是抛出了一个什么一个自定义场这个东西大家看到它是一个加码的枚具类型里边是不是就定义了很多的这种什么错误代码和错误的信息看懂吗
[01:59] 媒体类型大家加码技术是不是应该学过忘掉的可以再复习一下那这里边呢我们就可以因为这个媒体类型它就是一个error code的类型嘛所以呢我们就可以直接呀在这儿你看也用这个error code因为它的构造方法要的就是error code好这个error code里面是不是有两个嘛一个是code一个是message好那现在呢我们看让它抛出一个验证码失败这个也是验证码失败行不行可以吧那有时候老师那你这个
[02:28] 抛出验证码失败怎么测可以这么多我们把它重启一下看我重启完了之后现在我们就要来测原来验证码失败它是不是抛了这么一个错误信息现在我们要测试一下它是不是能够返回error code和error message同时我们也在我们刚才写的异常处理器当中打断点我们要来看一下它能不能来拦截住这个异常懂我意思吗好执行
[02:57] 这时候就进来了就进到了异常处理器现在他拿到的各位你看一下现在拿到的是不是就是business一个sepc这是不是我们自己抛出的自定义一场是不是被他拿到了拿到了之后呢就进到这个方法看打印日志然后看拿到我们的错误代码这错误代码是不是你在代码当中抛出的100102和验证码错误对不对那你说各位
[03:24] 这我是不是就轻而易举的拿到了我们当初在写代码的时候程序员所主动抛出的这个什么100102我是不是拿到了对那我现在拿到了之后呢各位我们是不是刚才也把这个全局异常处理器这个断点一根根中是不是也进来了那这个时候它是不是就可以最终返回我们要的这个错误代码错误信息这就是我们说的以后我们要
[03:52] 在程序代码当中程序员编写代码的时候要主动抛出我们说的自定义异常类型的异常懂吧好这是我们抛出的可预知的自定义异常类型那如果说不可预知呢啥意思啥是不可预知你比如说数据库连接不上了比如说我们说的这个什么这个这个这个除零除零异常大家应该不莫证吧我定义个变量
[04:21] 1除0这是不是不允许的这是不是就会抛出了对不对好我把这个异常写到我们刚才写的这个三户注册的接口中在这好我再次把这个程序起一下如果遇到不可预知的这种异常我们刚才学过异常处理流程是怎么说的我们会把它统一格式化为啥对99999系统未知错误异常所以我们现在就再次在我们的全局异常处理器里边来打断点
[04:51] 看好啊这时候我要打断点你看他他报一个啥错这时候我们也捕获到异常了但是你看这个捕获的异常你看是不是我们系统抛出的出令异常那么它不是我们系统自定义的异常但是呢我们也把它捕获到了我们就要把它统一为什么99999系统未知错误异常最终你看是不是也拿到了一个前端所要求的这个格式啊error code error message对这就是我们说的
[05:20] 抛出自定义异常最终由全局异常处理器来捕获来解析整个过程的测试我们就测试完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现自定义异常的抛出与全局异常处理器的处理流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档中“2.4.5.5 抛出自定义异常”章节，说明需修改 SmsService 接口抛出 BusinessException。
画面2：在 SmsServiceImpl.java 中，展示校验验证码的逻辑，使用 restTemplate 发送请求并处理响应。
画面3：在 SmsServiceImpl.java 中，展示抛出 RuntimeException 的代码，用于处理验证码失败的情况。
画面4：展示 CommonErrorCode.java 文件，定义了多个自定义错误码常量。
画面5：展示 CommonErrorCode.java 文件，继续定义错误码常量，包括用户不存在等。
画面6：在 SmsServiceImpl.java 中，展示抛出 BusinessException 的代码，使用 CommonErrorCode.E_100102。
画面7：在项目结构中，展示 SmsService 接口和 SmsServiceImpl 实现类。
画面8：展示 GlobalExceptionHandler.java 文件，定义了处理 BusinessExcepion 的方法。
画面9：展示 CommonErrorCode.java 文件，继续定义错误码常量。
画面10：在 GlobalExceptionHandler.java 中，展示解析自定义异常并返回 RestErrorResponse 的代码。
画面11：在 MerchantController.java 中，展示商户注册接口的代码，调用 smsService.checkVerifyCode 方法。
画面12：展示课程文档中“2.4.5.5 抛出自定义异常”章节，说明如何在异常处理器中直接抛出自定义异常。
画面13：在 GlobalExceptionHandler.java 中，展示处理异常的代码，包括日志记录和返回 RestErrorResponse。
画面14：在 SmsServiceImpl.java 中，展示请求验证码的逻辑，包括发送请求和处理响应。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
public void checkVerifyCode(String verifyKey, String verifyCode) throws BusinessException;

画面2：
e.printStackTrace();
throw new RuntimeException("验证码失败");
if (bodyMap == null || bodyMap.get("result") == null)
throw new RuntimeException("验证码失败");

画面3：
String url = "http://localhost:8080/sms/send";
try {
//使用restTemplate请求短信服务
ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, HttpEntity.EMPTY, Map.class);
Map bodyMap = exchange.getBody();
log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
bodyMap = exchange.getBody();
e.printStackTrace();
throw new RuntimeException("验证码失败");
}

画面4：
public enum CommonErrorCode implements ErrorCode {
E_10001(10001, "传入参数与接口不匹配"),
E_10002(10002, "验证码为空"),
E_10003(10003, "验证码格式不正确"),
E_10004(10004, "查询结果为空"),
E_10005(10005, "ID格式不正确或超出Long存储范围"),
E_10006(10006, "上传错误"),
E_10007(10007, "发送验证码错误"),
E_10008(10008, "传入对象为空"),
E_10009(10009, "手机号格式不正确"),
E_10010(10010, "用户名为空"),
E_10011(10011, "密码为空"),
E_10012(10012, "手机号已存在"),
E_10013(10013, "用户名已存在"),
E_10014(10014, "密码不正确"),
E_110001(110001, "帐号不存在");

画面5：
E_110001(110001, "帐号不存在");

画面6：
throw new BusinessException(CommonErrorCode.E_100102);
if (bodyMap == null || bodyMap.get("result") == null || !(Boolean) bodyMap.get("result")) {
throw new RuntimeException("验证码失败");
}

画面7：
SmsService

画面8：
@ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
public RestErrorResponse processException(HttpServletRequest request, HttpServletResponse response, Exception e) {
//解析异常信息
if (e instanceof BusinessException) {
//解析系统自定义异常，直接返回ErrorCodeMessage
BusinessException businessException = (BusinessException) e;
ErrorCode errorCode = businessException.getErrorCode();
//错误码
int code = errorCode.getCode();
//错误描述
String desc = errorCode.getDesc();
return new RestErrorResponse(String.valueOf(code), desc);
}
LOGGER.error("系统异常：", e);
return new RestErrorResponse(CommonErrorCode.UNKNOWN.getDesc(), CommonErrorCode.UNKNOWN.getCode());
}

画面9：
E_10001(10001, "传入参数与接口不匹配"),
E_10002(10002, "验证码为空"),
E_10003(10003, "验证码格式不正确"),
E_10004(10004, "查询结果为空"),
E_10005(10005, "ID格式不正确或超出Long存储范围"),
E_10006(10006, "上传错误"),
E_10007(10007, "发送验证码错误"),
E_10008(10008, "传入对象为空"),
E_10009(10009, "手机号格式不正确"),
E_10010(10010, "用户名为空"),
E_10011(10011, "密码为空"),
E_10012(10012, "手机号已存在"),
E_10013(10013, "用户名已存在"),
E_10014(10014, "密码不正确"),
E_110001(110001, "帐号不存在");

画面10：
Exception e) {
//解析异常信息
if (e instanceof BusinessException) {
//解析系统自定义异常，直接返回ErrorCodeMessage
BusinessException businessException = (BusinessException) e;
ErrorCode errorCode = businessException.getErrorCode();
//错误码
int code = errorCode.getCode();
//错误描述
String desc = errorCode.getDesc();
return new RestErrorResponse(String.valueOf(code), desc);
}
LOGGER.error("系统异常：", e);
return new RestErrorResponse(CommonErrorCode.UNKNOWN.getDesc(), CommonErrorCode.UNKNOWN.getCode());
}

画面11：
@ApiImplicitParam(value = "手机号", name = "phone", required = true, dataType = "string", paramType = "query")
public String getSCode(String phone) {
return smsService.sendSms(phone);
}

画面12：
//捕获异常后处理方法
@ExceptionHandler(value = Exception.class)
@ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
public RestErrorResponse processException(HttpServletRequest request, HttpServletResponse response, Exception e) {
//如果抛出自定义异常则直接抛出异常
if (e instanceof BusinessException) {
LOGGER.info(e.getMessage(), e);
BusinessException businessException = (BusinessException) e;
ErrorCode errorCode = businessException.getErrorCode();
//错误码
int code = errorCode.getCode();
//错误描述
String desc = errorCode.getDesc();
return new RestErrorResponse(errorCode(), String.valueOf(errorCode.getCode()));
}
LOGGER.error("系统异常：", e);
return new RestErrorResponse(CommonErrorCode.UNKNOWN.getDesc(), String.valueOf(CommonErrorCode.UNKNOWN.getCode()));
}

画面13：
if (e instanceof BusinessException) {
LOGGER.info(e.getMessage(), e);
BusinessException businessException = (BusinessException) e;
ErrorCode errorCode = businessException.getErrorCode();
//错误码
int code = errorCode.getCode();
//错误描述
String desc = errorCode.getDesc();
return new RestErrorResponse(String.valueOf(code), desc);
}
LOGGER.error("系统异常：", e);
return new RestErrorResponse(CommonErrorCode.UNKNOWN.getDesc(), CommonErrorCode.UNKNOWN.getCode());

画面14：
String url = smsUrl + "/verify?" + "verifyCode=" + verifyCode + "&verificationKey=" + verifyKey;
try {
//请求验证码
ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, HttpEntity.EMPTY, Map.class);
Map responseMap = exchange.getBody();
log.info("校验验证码，响应内容:{}", JSON.toJSONString(responseMap));
} catch (Exception e) {
e.printStackTrace();
throw new RuntimeException("验证码失败");
}
if (responseMap == null || responseMap.get("result") == null || !(Boolean) responseMap.get("result")) {
throw new BusinessException(CommonErrorCode.E_100102);
throw new RuntimeException("验证码失败");
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT标题为“2.4.5.5 抛出自定义异常”，内容为“按照异常处理流程，应用层抛出自定义异常由异常处理器进行解析。”
画面12：PPT标题为“2.4.5.5 抛出自定义异常”，内容为“如果抛出自定义异常则直接抛出异常”。

5) 不要评价画面美观，不要输出与课程无关的内容。

