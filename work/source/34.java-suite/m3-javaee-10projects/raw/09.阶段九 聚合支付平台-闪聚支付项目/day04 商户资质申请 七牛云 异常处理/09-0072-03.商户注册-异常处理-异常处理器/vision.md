# 画面线理解：03.商户注册-异常处理-异常处理器

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\03.商户注册-异常处理-异常处理器【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:15, 02:20, 02:54, 05:42, 07:47, 08:45, 10:07, 11:57, 12:55, 13:40, 14:35, 15:15, 15:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:03:13

1) 这一组画面整体在讲什么（一句话）：
在 Spring Boot 项目中，通过自定义异常类和全局异常处理器，实现对业务异常和系统异常的统一处理和响应。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：讲解在 shanjupay-common 工程的 com.shanjupay.common.domain 包下添加错误响应包装类 RestErrorResponse。
画面2：展示 RestErrorResponse 类的完整代码，包含 @ApiModel 注解和构造方法。
画面3：在 IDE 中展示 shanjupay-common 模块的目录结构，选中了 com.shanjupay.common 包。
画面4：讲解全局异常处理器使用 @ControllerAdvice 注解实现，介绍其用法。
画面5：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 @ControllerAdvice 注解上。
画面6：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 @ExceptionHandler 注解上。
画面7：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 @ResponseBody 注解上。
画面8：回顾定义全局异常处理器的讲解内容。
画面9：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 if (e instanceof BusinessException) 语句上。
画面10：在 IDE 中展示 CommonErrorCode.java 文件，展示自定义的错误码枚举。
画面11：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 return new RestErrorResponse(String.valueOf(code), CommonErrorCode.UNKNOWN.getDesc()) 语句上。
画面12：在 IDE 中展示 GlobalExceptionHandler.java 文件，光标位于 return new RestErrorResponse(String.valueOf(code), CommonErrorCode.UNKNOWN.getDesc()) 语句上。
画面13：讲解抛出自定义异常的流程，指出需要在接口中抛出 BusinessException。
画面14：回顾在 shanjupay-common 工程的 com.shanjupay.common.domain 包下添加错误响应包装类 RestErrorResponse。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
package com.shanjupay.common.domain;
import io.swagger.annotations.ApiModel;
@ApiModel(value = "RestErrorResponse", description = "错误响应参数包装类")
@Data
public class RestErrorResponse {
private String errCode;
private String errMessage;
public RestErrorResponse(String errCode,String errMessage){
this.errCode = errCode;
this.errMessage = errMessage;
}
}

画面2：
package com.shanjupay.common.domain;
import io.swagger.annotations.ApiModel;
@ApiModel(value = "RestErrorResponse", description = "错误响应参数包装类")
@Data
public class RestErrorResponse {
private String errCode;
private String errMessage;
public RestErrorResponse(String errCode,String errMessage){
this.errCode = errCode;
this.errMessage = errMessage;
}
}

画面3：
Project Structure:
shanjupay
├── shanjupay-common
│   ├── pom.xml
│   ├── shanjupay-merchant-api
│   ├── shanjupay-merchant-service
│   └── src
│       └── main
│           └── java
│               └── com
│                   └── shanjupay
│                       └── common
│                           └── domain
│                               ├── BusinessException
│                               ├── CommonErrorCode
│                               ├── ErrorCode
│                               ├── PageVO
│                               ├── RestErrorResponse
│                               └── RestResponse

画面4：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面5：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面6：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面7：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面8：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面9：
package com.shanjupay.merchant.common.intercept;
@ControllerAdvice
@ExceptionHandler(value = Exception.class)
@ResponseBody
public class GlobalExceptionHandler {

}

画面10：
public enum CommonErrorCode implements ErrorCode {
    _10001("10001", "商户名与账户不匹配"),
    _10002("10002", "验证码错误"),
    _10003("10003", "查询结果为空"),
    _10004("10004", "ID格式不正确或超出long范围"),
    _10005("10005", "上传失败"),
    _10006("10006", "发送短信失败"),
    _10007("10007", "传入对象为空"),
    _10008("10008", "手机号格式不正确"),
    _10009("10009", "商户名为空"),
    _10010("10010", "商户名已存在"),
    _10011("10011", "手机号为空"),
    _10012("10012", "手机号已存在"),
    _10013("10013", "密码为空"),
    _10014("10014", "密码不正确"),
    _10015("10015", "账号不存在"),
    _10016("10016", "账号已存在"),
    _10017("10017", "密码长度不正确"),
    _10018("10018", "验证码已过期"),
    _10019("10019", "验证码错误"),
    _10020("10020", "验证码已过期"),
    _10021("10021", "验证码错误"),
    _10022("10022", "验证码已过期"),
    _10023("10023", "验证码错误"),
    _10024("10024", "验证码已过期"),
    _10025("10025", "验证码错误"),
    _10026("10026", "验证码已过期"),
    _10027("10027", "验证码错误"),
    _10028("10028", "验证码已过期"),
    _10029("10029", "验证码错误"),
    _10030("10030", "验证码已过期"),
    _10031("10031", "验证码错误"),
    _10032("10032", "验证码已过期"),
    _10033("10033", "验证码错误"),
    _10034("10034", "验证码已过期"),
    _10035("10035", "验证码错误"),
    _10036("10036", "验证码已过期"),
    _10037("10037", "验证码错误"),
    _10038("10038", "验证码已过期"),
    _10039("10039", "验证码错误"),
    _10040("10040", "验证码已过期"),
    _10041("10041", "验证码错误"),
    _10042("10042", "验证码已过期"),
    _10043("10043", "验证码错误"),
    _10044("10044", "验证码已过期"),
    _10045("10045", "验证码错误"),
    _10046("10046", "验证码已过期"),
    _10047("10047", "验证码错误"),
    _10048("10048", "验证码已过期"),
    _10049("10049", "验证码错误"),
    _10050("10050", "验证码已过期"),
    _10051("10051", "验证码错误"),
    _10052("10052", "验证码已过期"),
    _10053("10053", "验证码错误"),
    _10054("10054", "验证码已过期"),
    _10055("10055", "验证码错误"),
    _10056("10056", "验证码已过期"),
    _10057("10057", "
