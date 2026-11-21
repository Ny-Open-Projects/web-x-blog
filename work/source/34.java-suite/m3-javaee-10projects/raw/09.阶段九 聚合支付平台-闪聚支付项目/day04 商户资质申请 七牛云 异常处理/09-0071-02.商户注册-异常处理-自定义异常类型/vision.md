# 画面线理解：02.商户注册-异常处理-自定义异常类型

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\02.商户注册-异常处理-自定义异常类型【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:30, 01:00, 01:24, 01:40, 01:54, 02:17, 02:38, 02:47, 03:02, 03:15, 03:30, 03:42, 03:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:02:20

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Java 项目中自定义业务异常类、定义错误码枚举，并实现异常处理器以统一返回标准的 JSON 格式错误信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了文档内容，说明服务端将异常信息封装成 JSON 格式返回。
- 代码示例：{ "errCode": "000000", "errMessage": "错误说明" }

画面 2：
- 展示了 IDE 中的代码，包含一个 try-catch 块，用于处理请求验证服务异常。
- 代码示例：throw new RuntimeException("发送验证码失败");

画面 3：
- 展示了文档内容，说明返回的 JSON 信息中状态码 500 不符合前端规范，应将错误信息写在 "errMessage" 中。
- 展示了异常处理流程图：响应信息 (errCode, errMessage) → 取出ErrorCode → 统一为99999异常 → BusinessException 自定义异常 → Exception 不可预见异常

画面 4：
- 展示了 IDE 中的代码，定义了 ErrorCode 枚举类。
- 代码示例：public enum ErrorCode implements ErrorCode { E_200301(200301, "传入对象为空"), E_200302(200302, "参数为空"), ... }

画面 5：
- 展示了 IDE 中的代码，定义了 BusinessException 类，继承 RuntimeException。
- 代码示例：public class BusinessException extends RuntimeException { private ErrorCode errorCode; }

画面 6：
- 展示了 IDE 中的代码，BusinessException 类定义。
- 代码示例：public class BusinessException extends RuntimeException { private ErrorCode errorCode; }

画面 7：
- 展示了 IDE 中的代码，右键 BusinessException.java，弹出菜单。
- 代码示例：（无代码，为操作界面）

画面 8：
- 展示了 IDE 中的代码，弹出“Select Fields to Generate Getters”对话框。
- 代码示例：（无代码，为操作界面）

画面 9：
- 展示了 IDE 中的代码，BusinessException 类中添加了构造函数和 setter/getter 方法。
- 代码示例：public BusinessException(ErrorCode errorCode) { super(); this.errorCode = errorCode; } public void setErrorCode(ErrorCode errorCode) { this.errorCode = errorCode; }

画面 10：
- 展示了文档内容，说明在 common 工程中定义了 ErrorCode 接口及 CommonErrorCode 通用代码。
- 代码示例：在 common 工程专门定义了 ErrorCode 接口及 CommonErrorCode 通用代码。

画面 11：
- 展示了 IDE 中的代码，定义了 CommonErrorCode 枚举类。
- 代码示例：// ID格式不正确或超出long存储范围 E_100105(100105, "ID格式不正确或超出long存储范围"); // 上传出错 E_100106(100106, "上传出错"); // 发送验证码失败 E_100107(100107, "发送验证码失败");

画面 12：
- 展示了 IDE 中的代码，弹出“Copy file”对话框，准备复制 CommonErrorCode.java 文件。
- 代码示例：Copy file F:\teach\shanjuipay\node2\output\day03\资料\代码\CommonErrorCode.java

画面 13：
- 展示了文件资源管理器，显示了 CommonErrorCode.java 和 TokenTemp.java 两个文件。
- 代码示例：（无代码，为文件列表）

画面 14：
- 展示了文档内容，说明在 shanjupay-common 工程的 com.shanjupay.common.domain 包下添加业务异常类 BusinessException。
- 代码示例：package com.shanjupay.common.domain; public class BusinessException extends RuntimeException { // 错误代码 private ErrorCode errorCode; }

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
{
  "errCode": "000000",
  "errMessage": "错误说明"
}

画面 2：
exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
log.info("请求验证的服务，响应码为[{}]，JSON为{}", response.getStatusCode(), response.getBody());
if (bodyMap == null || bodyMap.get("result") == null) {
  throw new RuntimeException("发送验证码失败");
}

画面 3：
{
  "timestamp": "2019-12-10T10:06:19.936+0000",
  "status": 500,
  "error": "Internal Server Error",
  "message": "验证码错误",
  "path": "/merchant/merchants/register"
}

画面 4：
public enum ErrorCode implements ErrorCode {
  E_200301(200301, "传入对象为空"),
  E_200302(200302, "参数为空"),
  E_200303(200303, "手机号不存在"),
  E_200304(200304, "商户不存在"),
  E_200305(200305, "支付订单金额不能为0"),
  E_200306(200306, "支付订单金额不能为负数"),
  E_200307(200307, "支付订单金额不能大于1000000000000000000"),
  E_200308(200308, "支付订单金额不能小于0"),
  E_200309(200309, "支付订单金额不能为0"),
  E_200310(200310, "支付订单金额不能为负数"),
  E_200311(200311, "支付订单金额不能大于1000000000000000000"),
  E_200312(200312, "支付订单金额不能小于0"),
  E_200313(200313, "支付订单金额不能为0"),
  E_200314(200314, "支付订单金额不能为负数"),
  E_200315(200315, "支付订单金额不能大于1000000000000000000"),
  E_200316(200316, "支付订单金额不能小于0"),
  E_200317(200317, "支付订单金额不能为0"),
  E_200318(200318, "支付订单金额不能为负数"),
  E_200319(200319, "支付订单金额不能大于1000000000000000000"),
  E_200320(200320, "支付订单金额不能小于0"),
  E_200321(200321, "支付订单金额不能为0"),
  E_200322(200322, "支付订单金额不能为负数"),
  E_200323(200323, "支付订单金额不能大于1000000000000000000"),
  E_200324(200324, "支付订单金额不能小于0"),
  E_200325(200325, "支付订单金额不能为0"),
  E_200326(200326, "支付订单金额不能为负数"),
  E_200327(200327, "支付订单金额不能大于1000000000000000000"),
  E_200328(200328, "支付订单金额不能小于0"),
  E_200329(200329, "支付订单金额不能为0"),
  E_200330(200330, "支付订单金额不能为负数"),
  E_200331(200331, "支付订单金额不能大于1000000000000000000"),
  E_200332(200332, "支付
