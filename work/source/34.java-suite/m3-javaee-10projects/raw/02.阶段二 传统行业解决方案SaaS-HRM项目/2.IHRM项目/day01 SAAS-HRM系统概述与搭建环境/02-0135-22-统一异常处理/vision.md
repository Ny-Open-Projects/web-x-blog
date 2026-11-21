# 画面线理解：22-统一异常处理

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\22-统一异常处理_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:49, 02:27, 03:19, 04:57, 05:44, 06:39, 07:26, 08:31, 09:47, 10:38, 11:28, 12:28, 13:01, 13:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:02:56

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过自定义异常类和全局异常处理器来统一处理控制器层的异常，并展示其在实际接口调用中的响应效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了课程目录结构，当前位于“4.1 创建项目的说明”。
- 代码编辑器中显示了自定义异常类 `CommonException` 的定义，继承自 `RuntimeException`，包含 `ResultCode` 字段和构造方法。
- 代码内容：
  ```java
  package com.ihrm.common.entity;
  import com.ihrm.common.entity.ResultCode;
  import lombok.Getter;
  @Getter
  public class CommonException extends RuntimeException {
      private static final long serialVersionUID = 1L;
      private ResultCode code = ResultCode.SERVER_ERROR;
      public CommonException() {
      }
      public CommonException(ResultCode resultCode) {
          super(resultcode.message());
          this.code = resultCode;
      }
  }
  ```

画面 2:
- 展示了项目结构，当前选中 `BaseExceptionHandler.java`。
- 代码编辑器中显示了 `BaseExceptionHandler` 类的注解和导入语句，准备定义公共异常处理器。
- 代码内容：
  ```java
  package com.ihrm.common.handler;
  import org.springframework.web.bind.annotation.*;
  ```

画面 3:
- 展示了 `BaseExceptionHandler` 类的 `@ControllerAdvice` 注解和 `@ExceptionHandler` 注解。
- 代码内容：
  ```java
  @ControllerAdvice
  public class BaseExceptionHandler {
      public Result error(HttpServletRequest request, HttpServletResponse response, Exception e) {
          return null;
      }
  }
  ```

画面 4:
- 展示了 `BaseExceptionHandler` 类中 `error` 方法的实现，使用了 `@ExceptionHandler` 注解。
- 代码内容：
  ```java
  @ExceptionHandler(value = Exception.class)
  public Result error(HttpServletRequest request, HttpServletResponse response, Exception e) {
      return null;
  }
  ```

画面 5:
- 展示了 `BaseExceptionHandler` 类中 `error` 方法的实现，返回一个 `Result` 对象。
- 代码内容：
  ```java
  @ExceptionHandler(value = Exception.class)
  @ResponseBody
  public Result error(HttpServletRequest request, HttpServletResponse response, Exception e) {
      Result result = new Result(ResultCode.SERVER_ERROR);
      return result;
  }
  ```

画面 6:
- 展示了 `CompanyController` 类中的 `findAll` 方法，用于查询所有公司信息。
- 代码内容：
  ```java
  List<Company> list = companyService.findAll();
  Result result = new Result(ResultCode.SUCCESS);
  result.setData(list);
  return result;
  ```

画面 7:
- 展示了 `ResultCode` 类中的常量定义，包含系统错误码和业务错误码。
- 代码内容：
  ```java
  SUCCESS(true,10000,"操作成功"),
  FAIL(false,10001,"操作失败"),
  UNAUTHORIZED(false,10002,"您还未登录"),
  SERVER_ERROR(false,99999,"抱歉,系统繁忙,请稍后重试");
  ```

画面 8:
- 展示了在 `ResultCode` 类中定义 `SUCCESS` 常量的代码。
- 代码内容：
  ```java
  public static final ResultCode SUCCESS = new ResultCode(true, 10000, "操作成功");
  ```

画面 9:
- 展示了 `ResultCode` 类中的 `SUCCESS` 常量定义。
- 代码内容：
  ```java
  public static final ResultCode SUCCESS = new ResultCode(true, 10000, "操作成功");
  ```

画面 10:
- 展示了 `BaseExceptionHandler` 类中 `error` 方法的实现，判断异常类型并返回相应结果。
- 代码内容：
  ```java
  @ExceptionHandler(value = Exception.class)
  @ResponseBody
  public Result error(HttpServletRequest request, HttpServletResponse response, Exception e) {
      if (e.getClass() == CommonException.class) {
          return new Result(ResultCode.SUCCESS);
      }
      return new Result(ResultCode.SERVER_ERROR);
  }
  ```

画面 11:
- 展示了 `CompanyController` 类中的 `findById` 方法，用于根据 ID 查询公司信息。
- 代码内容：
  ```java
  @RequestMapping(value = "/{id}", method = RequestMethod.GET)
  public Result findById(@PathVariable("id") String id) {
      return new Result(companyService.findById(id));
  }
  ```

画面 12:
- 展示了 `CompanyController` 类中的 `findALL` 方法，用于查询所有公司信息。
- 代码内容：
  ```java
  @RequestMapping(value = "", method = RequestMethod.GET)
  public Result findAll() {
      int i = 1/0;
      List<Company> list = companyService.findAll();
      Result result = new Result(ResultCode.SUCCESS);
      result.setData(list);
      return result;
  }
  ```

画面 13:
- 展示了 `ResultCode` 类中的常量定义，包含系统错误码和业务错误码。
- 代码内容：
  ```java
  public enum ResultCode {
      SUCCESS(true,10000,"操作成功"),
      FAIL(false,10001,"操作失败"),
      UNAUTHORIZED(false,10002,"您还未登录"),
      SERVER_ERROR(false,99999,"抱歉,系统繁忙,请稍后重试");
  }
  ```

画面 14:
- 展示了 Postman 中发送 GET 请求到 `http://localhost:9001/company` 的响应结果。
- 响应内容：
  ```json
  {"success":false,"code":99999,"message":"抱歉,系统繁忙,请稍后重试","data":null}
  ```
