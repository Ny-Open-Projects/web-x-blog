# 画面线理解：04.商户注册-异常处理-抛出自定义异常测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\04.商户注册-异常处理-抛出自定义异常测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:36, 01:02, 01:31, 02:02, 02:23, 02:47, 03:10, 03:38, 03:57, 04:14, 04:38, 04:57, 05:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:04:03

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
