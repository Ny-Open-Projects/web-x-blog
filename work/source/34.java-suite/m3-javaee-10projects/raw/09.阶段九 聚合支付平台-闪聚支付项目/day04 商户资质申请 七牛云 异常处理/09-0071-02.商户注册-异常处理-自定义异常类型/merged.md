# 02.商户注册-异常处理-自定义异常类型

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\02.商户注册-异常处理-自定义异常类型【海量资源尽在 666java.com】.mp4
- 时长 3分57秒（音频 237s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们就按照刚才我们分析的异常处理流程来实现整个系统的异常处理首先根据刚才的流程我们知道我们Service也好Controller也好我们都要抛出自定义的叫做business exception这个自定义异常类所以下边呢我们来编写一下这个异常类那么这个异常类呢在所有的工程当中都会使用到所以呢我们准备在我们的common
[00:28] 通用的这个工程当中来写我们这个异常类然后在domain当中我们来定义一个类型这个就是我们的一个自定义的异常类型这个自定义异常类型呢因为它肯定还是要继承run time一个type群对吧好那现在呢在这个自定义类型当中啊我们需要注意一下那么最终我们要怎么去构造它呢
[00:56] 构造的时候我们说了是不是最终要指定错误代码和错误的这个信息啊所以这里边呢我们要给它啊指定这个错误代码和错误信息而这个错误代码和错误信息呢在大家看到啊在common当中有一个叫error code的这么一个接口看见吗对那这个error code的这个接口你看一下它的实现啊其实它将来会写一些什么写一些实现的
[01:25] 比如说这里边就有一个叫做common error code就是通用的里边定义了很多的错误代码和错误类型好那错误代码错误信息这里边呢我们知道最终你是要用到错误的这个自定义异常类当中所以这里边我们要把它写进去叫error code对吧好那error code写进去之后呢当然你将来是不是要进行什么你是不是要进行构造呀对构造的时候呢我们就要干嘛我们就可以来
[01:54] 写一个构造方法对吧写一个构造方法那么这个构造方法呢就可以将来让传进来这个AeroCode将来程序员去抛出异常的时候呢让他来把这个东西传进去好那当然了你这里边肯定还是要像这个调一下负类的构造嘛调一下Runtime的一个Super这个方法好然后呢这里边还有那你不光有这个带餐的构造你还有无餐的构造对不对还有无餐的构造
[02:23] 所以这里边呢我建议你也写一个将来呢方便我们进行这个异常类型的构造好那当然将来如果我们想取出这个异常类型里边AeroCode你肯定还需要定义一个什么get set的方法对不对这是get那么再定义一个set是吧所以其实这就是我们的一个什么自定义异常那将来我们要去抛出的话其实就会去死入new business一个set去
[02:53] 是不是就抛出我们自定义的异常了好那么这个自定义的异常类啊我们就写完了接下来呢我们说刚才你也看到了嘛我们看到这个error code我们是不是有很多的这种自带的这个错误代码和错误信息啊就在这里但是这个类呢这里边你会发现这里边这个代码呢我们随着课程的这个开展呢里边的代码呢会逐渐的给它补的越来越全
[03:21] 所以呢在我们的这个资料文件夹当中啊我们在用到这个代码的时候我都会给你拿过来你呢从资料当中拿过来拷到我们的拷本当中覆盖然后这个时候呢你会发现此时呢我们这个代码呢就会越来越全就刚才那个呢里边代码不太全那你呢拷贝我这个资料文件夹里边的这个里边完善的这个错误代码和错误信息的这么一个配置然后你把它覆盖
[03:49] 好到这儿呢我们这个异常处理的这个自电异常处理类我们就编写完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

