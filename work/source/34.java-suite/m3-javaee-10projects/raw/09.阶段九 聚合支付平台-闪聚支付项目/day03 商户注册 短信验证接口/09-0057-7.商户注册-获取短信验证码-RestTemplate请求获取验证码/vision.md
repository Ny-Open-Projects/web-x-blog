# 画面线理解：7.商户注册-获取短信验证码-RestTemplate请求获取验证码

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\7.商户注册-获取短信验证码-RestTemplate请求获取验证码【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:07, 02:03, 03:10, 04:28, 05:22, 06:09, 07:49, 08:30, 09:28, 10:03, 11:06, 11:40, 12:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:52:29

1) 这一组画面整体在讲如何使用 Spring 的 RestTemplate 调用远程 HTTP 服务以获取验证码，并演示了相关代码实现和调试过程。

2) 按时间顺序列出每张画面的要点：
画面1：介绍 RestTemplate 技术预研，说明使用 OkHttp 作为 HTTP 客户端，并给出引入依赖的 Maven 配置。
画面2：在 Swagger UI 中配置生成验证码的 POST 请求，参数包括 effectiveTime 和 name。
画面3：在 IDE 中展示 RestTemplateTest.java 代码，调用生成验证码的接口。
画面4：在 IDE 中展示 RestTemplateTest.java 代码，准备调试。
画面5：在 IDE 中展示 RestTemplateTest.java 代码，使用 HttpEntity 构建请求体。
画面6：在 IDE 中展示 HttpHeaders 类的源码，查看其构造函数和 setAccept 方法。
画面7：在 Swagger UI 中展示请求的 curl 命令和响应。
画面8：在 IDE 中展示 RestTemplateTest.java 代码，使用 HttpEntity 构建请求体。
画面9：在 IDE 中展示 RestTemplateTest.java 代码，调试时查看 ResponseEntity 的 bodyMap。
画面10：在 IDE 中展示测试通过的日志。
画面11：在 IDE 中展示 RestTemplateTest.java 代码，调试时查看 Map 的方法。
画面12：在 IDE 中展示 RestTemplateTest.java 代码，调试时查看 ResponseEntity 的 bodyMap。
画面13：在 IDE 中展示 Sailing 应用启动日志。
画面14：展示系统交互流程图，说明商户注册流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<!-- okhttp3依赖 -->
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp3</artifactId>
</dependency>
```

画面3：
```java
String url = "http://www.baidu.com/";
// (1)生成验证码，作为http请求
// http://localhost:56085/sailing/generate/effectiveTime=600&name=sms
String url = "http://localhost:56085/sailing/generate/effectiveTime=600&name=sms";
restTemplate.exchange(url, HttpMethod.GET, null, String.class);
```

画面5：
```java
//请求体
//请求头，传入body，header
HttpEntity httpEntity = new HttpEntity(body, headers);
ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
```

画面6：
```java
public HttpHeaders() {
    this.collection = new LinkedMultiValueMap<>(initialCapacity, Locale.ENGLISH);
}

public HttpHeaders(MultiValueMap<String, String> headers) {
    Assert.notNull(headers, "MultiValueMap must not be null");
    this.headers = headers;
}
```

画面8：
```java
//请求体
//请求头，传入body，header
HttpEntity httpEntity = new HttpEntity(body, httpHeaders);
ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
```

画面9：
```java
Map bodyMap = exchange.getBody();
System.out.println(bodyMap);
```

画面11：
```java
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
System.out.println(key);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
架构图标题：2.1.1 系统交互流程
流程图结构：
- 淘宝商户APP → 商户平台应用 → 商户服务 → SaaS平台 → 验证码服务
- 验证码服务 → 发送于手机端
- 商户平台应用 → 新增商户 → 商户服务 → SaaS平台 → 验证码服务
- 验证码服务 → 发送于手机端
- 商户平台应用 → 新增商户 → 商户服务 → SaaS平台 → 验证码服务
- 验证码服务 → 发送于手机端

5) 不要评价画面美观，不要输出与课程无关的内容。
