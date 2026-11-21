# 画面线理解：day03-6-校验手机号和验证码功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-6-校验手机号和验证码功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:23, 03:11, 03:59, 04:34, 05:25, 06:34, 07:10, 07:52, 08:23, 09:09, 09:50, 10:27, 11:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:31:28

1) 这一组画面整体在讲什么（一句话）：
演示如何在万能2P项目中，通过 Swagger UI 调用接口获取短信验证码并验证，同时展示相关的代码实现和异常处理机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，标题为“4.5 注册2：校验手机号和验证码”，并指出接口定义在“wanxingp2p-api工程中的AccountAPI接口”。
画面2：展示IDE中OkHttp工具类的代码，用于发送HTTP请求。
画面3：在Swagger UI中，输入手机号参数，准备调用获取短信验证码的接口。
画面4：在Swagger UI中，输入验证码、key和手机号，点击“Execute”按钮。
画面5：展示Swagger UI中请求的Curl命令和响应体，响应体为{"code": 0, "msg": "string", "result": {}}。
画面6：展示多个窗口，包括Swagger UI、Postman、cmd、IDE等，用于调试和测试。
画面7：展示PPT中的异常处理流程图，包括SpringMVC全局异常捕获、自定义异常抛出、表现层、业务层、数据访问层。
画面8：展示Swagger UI中请求的响应体，响应码为40102，响应信息为“验证码错误”。
画面9：展示IDE中SmsService类的代码，用于验证短信验证码。
画面10：展示多个窗口，包括Swagger UI、Postman、cmd、IDE等，用于调试和测试。
画面11：展示IDE中GlobalExceptionHandler类的代码，用于处理异常。
画面12：展示IDE中SmsService类的代码，用于验证短信验证码。
画面13：展示多个窗口，包括Swagger UI、Postman、cmd、IDE等，用于调试和测试。
画面14：在Swagger UI中，输入验证码、key和手机号，点击“Execute”按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public static ResponseBody post(String url, String json) {
    OkHttpClient body = new Request.Builder().post(body).build();
    Request request = new Request.Builder().post(body).build();
    try {
        Response response = okHttp3Client.newCall(request).execute();
        if (responseBody != null) {
            return JSON.parseObject(responseBody.string(), RestResponse.class);
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
    return RestResponse.validFail(CommonErrorCode.E_100106, eDesc);
}
```

画面9：
```java
public void verifySmsCode(String key, String code) {
    if (smsHttp == null) {
        StringBuilder params = new StringBuilder();
        params.append("VerificationKey=").append(key).append("VerificationCode=").append(code);
        RestResponse smsResponse = OkHttpUtil.post(url + params, json, "");
        if (smsResponse.getCode() != CommonErrorCode.SUCCESS || smsResponse.getResult().toString().equals("0")) {
            throw new BusinessException(AccountErrorCode.E_40102);
        }
    }
}
```

画面11：
```java
public RestResponse<Null> exceptionNet(HttpServletRequest request, HttpServletResponse response, Exception e) {
    if (instanceof BusinessException) {
        BusinessException be = (BusinessException) e;
        if (CommonErrorCode.CUSTOM.equals(be.getErrorCode())) {
            return new RestResponse<Null>(be.getErrorCode(), be.getMessage());
        } else {
            return new RestResponse<Null>(be.getErrorCode(), be.getMessage());
        }
    } else if (instanceof JsonBindException) {
        return new RestResponse<Null>(CommonErrorCode.E_100104, "找不到资源");
    } else if (instanceof HttpRequestMethodNotSupportedException) {
        return new RestResponse<Null>(CommonErrorCode.E_100105, "method 方法不支持");
    } else if (instanceof HttpMediaTypeNotSupportedException) {
        return new RestResponse<Null>(CommonErrorCode.E_100106, "不支持的媒体类型");
    } else {
        return new RestResponse<Null>(CommonErrorCode.E_100107, "未知异常");
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面7：
- 标题：SpringMVC 全局异常捕获 GlobalExceptionHandler
- 流程图：
  - SpringMVC 全局异常捕获 GlobalExceptionHandler → 抛出自定义异常（包含自定义错误信息）throw new BussinessException(ErrorCode)
  - 抛出自定义异常（包含自定义错误信息）throw new BussinessException(ErrorCode) → 表现层 Controller
  - 抛出自定义异常（包含自定义错误信息）throw new BussinessException(ErrorCode) → 业务层 Service
  - 抛出自定义异常（包含自定义错误信息）throw new BussinessException(ErrorCode) → 数据访问层 Mapper

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
