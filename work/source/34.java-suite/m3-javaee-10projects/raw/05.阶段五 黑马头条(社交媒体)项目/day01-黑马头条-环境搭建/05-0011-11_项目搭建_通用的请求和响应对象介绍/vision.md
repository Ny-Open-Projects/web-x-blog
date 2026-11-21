# 画面线理解：11_项目搭建_通用的请求和响应对象介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\11_项目搭建_通用的请求和响应对象介绍【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:43, 01:19, 01:40, 02:04, 02:18, 02:25, 02:42, 02:48, 02:59, 03:17, 03:32, 03:35, 03:50, 04:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:31:31

1) 这一组画面整体在讲什么（一句话）：
讲解一个通用的响应对象 ResponseResult 的代码实现，包括其构造方法、静态工具方法和枚举类 AppHttpCodeEnum 的定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前位于“6.3 接口通用请求和响应”章节，具体到“6.3.1 通用的响应对象”，并显示了 ResponseResult 类的代码片段。
画面 2: 在 IDEA 中展示项目结构，选中了 com.heima.model.common.dto 包下的 ResponseResult.java 文件。
画面 3: 展示 ResponseResult.java 文件的代码，聚焦于类的成员变量和无参构造方法。
画面 4: 展示 ResponseResult.java 文件的代码，聚焦于带参数的构造方法。
画面 5: 展示 ResponseResult.java 文件的代码，聚焦于静态方法 errorResult 和 okResult。
画面 6: 展示 ResponseResult.java 文件的代码，聚焦于静态方法 errorResult 和 setAppHttpCodeEnum。
画面 7: 展示 AppHttpCodeEnum.java 文件的代码，定义了各种 HTTP 错误码和对应的中文描述。
画面 8: 展示 AppHttpCodeEnum.java 文件的代码，聚焦于 NO_OPERATOR_AUTH 错误码。
画面 9: 展示 AppHttpCodeEnum.java 文件的代码，聚焦于 TOKEN_INVALID 错误码。
画面 10: 展示 ResponseResult.java 文件的代码，聚焦于 ok 方法。
画面 11: 展示 ResponseResult.java 文件的代码，聚焦于 ok 方法和 setCode 方法。
画面 12: 展示 ResponseResult.java 文件的代码，聚焦于类的定义和构造方法。
画面 13: 展示 PageResponseResult.java 文件的代码，该类继承自 ResponseResult。
画面 14: 回到课程大纲页面，显示“6.3 接口通用请求和响应”章节。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class ResponseResult<T> implements Serializable {
    private String host;
    private Integer code;
    private String errorMessage;
    private T data;
    public ResponseResult() {
        this.code = 200;
    }
    public ResponseResult(Integer code, T data) {
        this.code = code;
        this.data = data;
    }
```

画面 2:
```java
package com.heima.model.common.dto;
```

画面 3:
```java
private T data;
public ResponseResult() { this.code = 200; }
public ResponseResult(Integer code, T data) {
    this.code = code;
    this.data = data;
}
```

画面 4:
```java
public ResponseResult(Integer code, String msg, T data) {
    this.code = code;
    this.errorMessage = msg;
    this.data = data;
}
```

画面 5:
```java
public static ResponseResult errorResult(int code, String msg) {
    ResponseResult result = new ResponseResult();
    return result.error(code, msg);
}
public static ResponseResult okResult(int code, String msg) {
    ResponseResult result = new ResponseResult();
    return result.ok(code, msg);
}
public static ResponseResult okResult(Object data) {
    ResponseResult result = new ResponseResult();
    if (data != null) {
        result.setData(data);
    }
    return result;
}
```

画面 6:
```java
public static ResponseResult errorResult(AppHttpCodeEnum enum) {
    return setAppHttpCodeEnum(enum, enum.getErrorMessage());
}
public static ResponseResult errorResult(AppHttpCodeEnum enum, String errorMessage) {
    return setAppHttpCodeEnum(enum, errorMessage);
}
public static ResponseResult setAppHttpCodeEnum(AppHttpCodeEnum enums, String errorMessage) {
    return okResult(enums.getCode(), errorMessage);
}
private static ResponseResult setAppHttpCodeEnum(AppHttpCodeEnum enums, String errorMessage) {
    return okResult(enums.getCode(), errorMessage);
}
public ResponseResult(?) error(Integer code, String msg) {
    this.code = code;
    this.errorMessage = msg;
    return this;
}
```

画面 7:
```java
// TOKEN 100
TOKEN_INVALID(50, "无效的TOKEN"),
TOKEN_EXPIRE(51, "TOKEN已过期"),
TOKEN_REQUIRED(52, "TOKEN是必须的"),
// SIGN 100
SIGN_INVALID(100, "无效的SIGN"),
SIGN_TIMEOUT(101, "SIGN已过期"),
// 参数错误 500 2000
PARAM_REQUIRE(500, "缺少参数"),
PARAM_INVALID(501, "无效参数"),
PARAM_IMAGE_FORMAT_ERROR(502, "图片格式有误"),
SERVER_ERROR(503, "服务端内部错误"),
// 数据错误 3000 3500
AP_USER_DATA_NOT_EXIST(301, "ApDeer数据不存在"),
DATA_NOT_EXIST(302, "数据不存在"),
NO_OPERATOR_AUTH(3000, "无权操作");
```

画面 8:
```java
NO_OPERATOR_AUTH(3000, "无权操作");
```

画面 9:
```java
TOKEN_INVALID(50, "无效的TOKEN"),
```

画面 10:
```java
public ResponseResult(?) ok(Integer code, T data) {
    this.code = code;
    this.data = data;
    return this;
}
```

画面 11:
```java
public ResponseResult(?) ok(Integer code, T data, String msg) {
    this.code = code;
    this.data = data;
    this.errorMessage = msg;
    return this;
}
public ResponseResult(?) ok(T data) {
    this.data = data;
    return this;
}
public Integer getCode() { return code; }
public void setCode(Integer code) { this.code = code; }
```

画面 12:
```java
public class ResponseResult<T> implements Serializable {
    private String host;
    private Integer code;
    private String errorMessage;
    private T data;
    public ResponseResult() { this.code = 200; }
    public ResponseResult(Integer code, T data) {
        this.code = code;
        this.data = data;
    }
```

画面 13:
```java
package com.heima.model.common.dto;
public class PageResponseResult extends ResponseResult {
    private Integer currentPage;
    private Integer size;
    private Integer total;
    public PageResponseResult(Integer currentPage, Integer size, Integer total) {
        this.currentPage = currentPage;
        this.size = size;
        this.total = total;
    }
    public int getCurrentPage() { return currentPage; }
    public void setCurrentPage(int currentPage) { this.currentPage = currentPage; }
    public int getSize() { return size; }
    public void setSize(int size) { this.size = size; }
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“6.3 接口通用请求和响应”，子标题为“dto(Data Transfer Object)数据传输对象，用于展示层与服务层之间的数据传输对象”，并列出“6.3.1 通用的响应对象”。
画面 14: PPT 标题为“6.3 接口通用请求和响应”，子标题为“dto(Data Transfer Object)数据传输对象，用于展示层与服务层之间的数据传输对象”，并列出“6.3.1 通用的响应对象”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
