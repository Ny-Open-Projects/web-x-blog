# 11_项目搭建_通用的请求和响应对象介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\11_项目搭建_通用的请求和响应对象介绍【海量资源尽在 666java.com】.mp4
- 时长 4分30秒（音频 271s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那咱们下面呢去介绍一下本项目呢是有一个接口的通用的请求和响应那这个讲这个通用请求和响应之前呢咱们还要说一个概念叫DTO那DTO的意思呢就是数据传输对象那它主要呢是用于展现层与服务层之间的这种数据的传输那咱们比如说咱们有一个前端前端想往后台去
[00:28] 微服务上去传数据咱们都应该把这些参数呢都封装到一个DTO的对象当中是这么一个作用啊那下面咱们来去先去说一下这个响应的有哪些对象啊目前的话咱们已经提供好的工程里边呢已经存在了在哪呢在当前的model对象中刚才说了这个model呢主要存放的都是一些实体对象那这个当前的响应也应该在当前这个包下面
[00:58] 打开当前这个包结构里边有一个commoncommon里边有一个叫做dtos里边有三个其中是有两个有一个response result还有一个page response result它两个都是一些响应的类咱们多数用的应该是response result来打开看一下那里边有一些属性属性比如说host code还有错误信息是吧还有一个t
[01:28] 那t呢就是一个范形那范形的话就是你可以传输任何任何的这种类型的对象过来都可以没有问题好那咱们用的最多的呢其实你可以读下这个类啊你看它里边提供了一些这种构造首先有一个呃有两个参数的呃这种构造方法一个是code和date是吧你可以传某一些比如说你想要回去的是一个200是吧呃这里边呢还有一个就是
[01:56] 如果说是date的话呢你可以去返回一个列表啊返回某一个对象啊OK那这个都是可以的然后咱们用的比较多的呢下面是有一个东西就是叫OK result比如增长改的时候咱们有可能会去想比如说你保存成功应该会有一个响应码并且是要提示一个信息OK还有一些比如说在我家看啊还有一些就是error result咱们也可以去
[02:25] 返回一个这种http code enumer这个是啥呢这个在enumer里边呢是有这么个信息是一个枚举你可以返回success那就是0操作成功如果是1的话呢可能需要去登录操作当然这些呢都是自定义的你也可以定义如果说后期开发感觉比较少的话或者说不够的话呢可以在这里边去添加当然这里边呢已经定下了参数比如说你看
[02:53] 成功段是零是吧登录登录段是1到50那token的是5到100那这个数字呢咱们已经定义好了最好是按照这个规范的去走当然每一个项目可能不太一样如果说你以后在项目开发的过程中遇到这样的情况的话你最好是按照当前项目的一些个规范的说明进行定义好那这个咱们先看啊这里边还有一些这种OKOK的话也是简单的返回一个code和一个day
[03:21] 和一个咱们的数据类型就可以了还有返回三个的啊这是都是OK但是呢一个是两个参数一个是三个参数OK行啊那这个呢就是一个统一的响应啊就是response without当然这里边还有一个叫配置require response without是吧它的很显然是一个页面啊是分析键的时候咱们需要用的啊你看它呢是继承了response without也就是继承了当前这个类
[03:49] 然后并且呢它又扩展了三个属性一个是当前页当前的条数是吧还有一个是总条数这样的话你进行分页的时候就是方便非常方便的进行去在前台去处理一些逻辑OK那分页的时候响应当前这个配置response伪造的就可以然后下面还有下面还有一个就是统一的响应的话咱们用到的是配置request DTO用到的是它它里边呢就有两个一个是size和一个配置
[04:18] 当然如果说不够的话咱们后期呢可以再进行扩展好呃那目前的话呢这个这个类呢咱们已经讲解完了啊通用的请求和响应

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

