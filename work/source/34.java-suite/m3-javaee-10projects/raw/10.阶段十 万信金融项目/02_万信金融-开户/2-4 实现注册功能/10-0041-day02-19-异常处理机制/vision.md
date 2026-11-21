# 画面线理解：day02-19-异常处理机制

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-19-异常处理机制_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 03:22, 06:52, 08:18, 08:51, 10:01, 10:14, 10:54, 11:26, 11:48, 12:02, 13:55, 15:33, 15:48, 15:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:27:09

1) 这一组画面整体在讲什么（一句话）：
讲解如何通过自定义异常和 SpringMVC 全局异常处理器来统一处理 API 异常，实现错误码和提示信息的标准化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- PPT 标题：异常处理机制
- 内容：概述传统异常处理存在的问题（项目中有很多地方都进行异常处理、编码规范不统一、提示信息不统一），并引出为了解决这些问题在 P2P 项目中设计了一套好的异常处理机制。
- 图形：展示异常处理流程图，从“前端”接收请求，经过“响应信息封装 RestResponse”，由“SpringMVC 全局异常捕获 GlobalExceptionHandler”处理。

画面 2:
- PPT 标题：二、API 设计
- 内容：1. 自定义错误代码和提示信息。
- 代码：定义接口 ErrorCode.java
  public interface ErrorCode {
      int getErrorCode(); //错误代码
      String getDesc(); //错误提示信息
  }
- 代码：CommonErrorCode.java 实现接口
  public enum CommonErrorCode implements ErrorCode {

画面 3:
- 代码：CommonErrorCode.java 继续展示
  public enum CommonErrorCode implements ErrorCode {
      SUCCESS(0, "成功"),
      /* 传入参数与接口不匹配 */
      E_100101(100101, "传入参数与接口不匹配"),
      /* 验证码错误 */
      E_100102(100102, "验证码错误"),
      /* 验证码为空 */
      E_100103(100103, "验证码为空"),
      /* 查询结果为空 */
      E_100104(100104, "查询结果为空"),
      /* ID格式不正确或超出Long存储范围 */
      E_100105(100105, "ID格式不正确或超出Long存储范围"),
      /* 未知错误 */
      E_100106(100106, "未知错误"),
      /* 未知错误 */
      UNKNOWN(999999, "未知错误");
  }

画面 4:
- 代码：CommonErrorCode.java 继续展示，聚焦在 E_100101 到 E_100106 的定义。

画面 5:
- 代码：展示 AccountErrorCode.java 的定义
  public enum AccountErrorCode implements ErrorCode {
      E_130101(130101, "用户名已存在"),
      E_130104(130104, "用户未注册"),
      E_130105(130105, "用户名或密码错误"),
      E_140141(140141, "注册失败"),
      E_140151(140151, "获取短信验证码失败"),
      E_140152(140152, "验证码错误");
  }

画面 6:
- 代码：AccountErrorCode.java 继续展示，聚焦在 E_130101 到 E_140152 的定义。

画面 7:
- 代码：AccountErrorCode.java 继续展示，聚焦在 E_130101 到 E_140152 的定义。

画面 8:
- 代码：展示 BusinessException 类的构造方法
  public BusinessException(String arg0, Throwable arg1) {
      super(arg0, arg1);
  }
  public BusinessException(ErrorCode errorCode, String arg0, Throwable arg1) {
      super(arg0, arg1);
      this.errorCode = errorCode;
  }
  public BusinessException(String arg0) {
      super(arg0);
  }
  public BusinessException(ErrorCode errorCode, String arg0) {
      super(arg0);
      this.errorCode = errorCode;
  }
  public BusinessException(Throwable arg0) {
      super(arg0);
  }
  public BusinessException(ErrorCode errorCode, Throwable arg0) {
      super(arg0);
      this.errorCode = errorCode;
  }

画面 9:
- 图形：展示异常处理流程图，从“表现层 Controller”、“业务层 Service”、“数据访问层 Mapper”抛出自定义异常（throw new BusinessException(ErrorCode)），经过“SpringMVC 全局异常捕获 GlobalExceptionHandler”，最终封装为“响应信息封装 RestResponse”返回给“前端”。

画面 10:
- 代码：展示 GlobalExceptionHandler.java 的定义
  @ControllerAdvice
  @Slf4j
  public class GlobalExceptionHandler {
      @ExceptionHandler(value = Exception.class)
  }

画面 11:
- 代码：GlobalExceptionHandler.java 继续展示，聚焦在 @ExceptionHandler 注解。

画面 12:
- 代码：CommonErrorCode.java 继续展示，聚焦在 E_100101 到 E_100106 的定义。

画面 13:
- 代码：展示 Controller 中的异常处理方法
  @ResponseBody
  public RestResponse<Null> exceptionGet(HttpServletRequest req, Exception e) {
      if (e instanceof BusinessException) {
          BusinessException be = (BusinessException) e;
          if (CommonErrorCode.CUSTOM.equals(be.getErrorCode())) {
              return new RestResponse<Null>(be.getErrorCode(), be.getMessage());
          } else {
              return new RestResponse<Null>(be.getErrorCode(), be.getDesc());
          }
      } else if (e instanceof NoHandlerFoundException) {
          return new RestResponse<Null>(404, "找不到资源");
      } else if (e instanceof HttpRequestMethodNotSupportedException) {
          return new RestResponse<Null>(405, "method 方法不支持");
      } else if (e instanceof HttpMediaTypeNotSupportedException) {
          return new RestResponse<Null>(415, "不支持媒体类型");
      }
      log.error("【系统异常】" + e.getMessage());
      return new RestResponse<Null>(CommonErrorCode.UNKNOWN.getErrorCode(), CommonErrorCode.UNKNOWN.getDesc());
  }

画面 14:
- 图形：展示异常处理流程图，从“表现层 Controller”、“业务层 Service”、“数据访问层 Mapper”抛出自定义异常（throw new BusinessException(ErrorCode)），经过“SpringMVC 全局异常捕获 GlobalExceptionHandler”，最终封装为“响应信息封装 RestResponse”返回给“前端”。
- 文字：1. 自定义异常类，自定义错误代码和提示信息（统一且友好）；2. 各层只抛异常（建议在业务层），不做异常处理；3. 异常捕获和处理统一交给 SpringMVC 的全局异常捕获类。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
public interface ErrorCode {
    int getErrorCode(); //错误代码
    String getDesc(); //错误提示信息
}
public enum CommonErrorCode implements ErrorCode {

画面 3:
public enum CommonErrorCode implements ErrorCode {
    SUCCESS(0, "成功"),
    /* 传入参数与接口不匹配 */
    E_100101(100101, "传入参数与接口不匹配"),
    /* 验证码错误 */
    E_100102(100102, "验证码错误"),
    /* 验证码为空 */
    E_100103(100103, "验证码为空"),
    /* 查询结果为空 */
    E_100104(100104, "查询结果为空"),
    /* ID格式不正确或超出Long存储范围 */
    E_100105(100105, "ID格式不正确或超出Long存储范围"),
    /* 未知错误 */
    E_100106(100106, "未知错误"),
    /* 未知错误 */
    UNKNOWN(999999, "未知错误");
}

画面 5:
public enum AccountErrorCode implements ErrorCode {
    E_130101(130101, "用户名已存在"),
    E_130104(130104, "用户未注册"),
    E_130105(130105, "用户名或密码错误"),
    E_140141(140141, "注册失败"),
    E_140151(140151, "获取短信验证码失败"),
    E_140152(140152, "验证码错误");
}

画面 8:
public BusinessException(String arg0, Throwable arg1) {
    super(arg0, arg1);
}
public BusinessException(ErrorCode errorCode, String arg0, Throwable arg1) {
    super(arg0, arg1);
    this.errorCode = errorCode;
}
public BusinessException(String arg0) {
    super(arg0);
}
public BusinessException(ErrorCode errorCode, String arg0) {
    super(arg0);
    this.errorCode = errorCode;
}
public BusinessException(Throwable arg0) {
    super(arg0);
}
public BusinessException(ErrorCode errorCode, Throwable arg0)
