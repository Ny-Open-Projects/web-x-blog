# 画面线理解：20.统一增加缓存逻辑的实现（中）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\20.统一增加缓存逻辑的实现（中）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:29, 00:55, 01:22, 01:49, 02:22, 04:39, 06:33, 07:05, 07:22, 07:41, 08:09, 08:27, 08:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:31:33

1) 这一组画面整体在讲什么（一句话）：
演示如何通过拦截器（RedisCacheInterceptor）和响应体增强（MyResponseBodyAdvice）在 Spring MVC 中实现基于 Redis 的缓存功能，包括缓存键的生成、缓存值的读取与写入、以及对请求和响应的拦截处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 使用 Advanced REST Client 发送 HTTP 请求。
- 请求 URL：http://172.16.55.13/tanhuai/recommendation/page=2。
- 请求头包含 Authorization 字段，值为 eyJhbGcOUIU1tNUS...（截断）。
- 响应状态码为 200，加载时间为 219 ms。
- 响应头显示 Server 为 nginx17.3，Content-Type 为 application/json;charset=UTF-8。
- 响应体为空。

画面 2：
- 在 IntelliJ IDEA 中查看 RedisCacheInterceptor.java 文件。
- 代码片段：`public static String createRedisKey(HttpServletRequest request) throws Exception { String paramStr = request.getRequestURI(); ... }`
- 调试窗口显示当前执行位置在 `createRedisKey` 方法中，参数为 "/tanhua/recommendation"。

画面 3：
- 在 IntelliJ IDEA 中查看 RedisCacheInterceptor.java 文件。
- 代码片段：`if (StringUtils.isNotEmpty(request.getHeader("Authorization"))) { paramStr += " " + authorization; }`
- 调试窗口显示当前执行位置在 `createRedisKey` 方法中，参数为 "/tanhua/recommendation?page=2"。

画面 4：
- 在 IntelliJ IDEA 中查看 RedisCacheInterceptor.java 文件。
- 代码片段：`String redisKey = createRedisKey(request); redisKey = "SERVER_DATA_5c97329b5e0a4050b5f70d05030f..."; String data = this.redisTemplate.opsForValue().get(redisKey);`
- 调试窗口显示当前执行位置在 `preHandle` 方法中，`data` 为 null。

画面 5：
- 使用 Advanced REST Client 发送 HTTP 请求。
- 请求 URL：http://172.16.55.13/tanhuai/recommendation/page=2。
- 请求头包含 Authorization 字段，值为 eyJhbGcOUIU1tNUS...（截断）。
- 响应状态码为 200，加载时间为 665 ms。
- 响应头显示 Server 为 nginx17.3，Content-Type 为 application/json;charset=UTF-8。
- 响应体为 JSON 格式，内容为：
```json
{
  "counts": 0,
  "pagesize": 10,
  "pages": 2,
  "items": [
    {
      "id": 40,
      "avatar": "https://itcast-tanhuai.oss-cn-shanghai.aliyuncs.com/images/logo/5.jpg",
      "nickname": "helma 40"
    }
  ]
}
```

画面 6：
- 在 Typora 中打开 day02.md 文件。
- 文件内容包含章节标题和子标题，如“2.6.1. 前端请求入口”、“2.6.2. 修改配置”等。
- 当前光标位于“测试：”下方，显示代码片段：
```java
@Override
public Object beforeBodyWrite(Object body, MethodParameter returnType, MediaType selectedContentType, Class<? extends HttpMessageConverter<?>> selectedConverterType, ServerHttpRequest request, ServerHttpResponse response) {
    if (body instanceof String) {
        redisValue = (String) body;
    } else {
        redisValue = mapper.writeValueAsString(body);
    }
    // 保存到redis中
    this.redisTemplate.opsForValue().set(redisKey, redisValue, Duration.ofHours(1));
    return body;
}
```

画面 7：
- 在 IntelliJ IDEA 中查看 MyResponseBodyAdvice.java 文件。
- 代码片段：
```java
@ControllerAdvice
public class MyResponseBodyAdvice implements ResponseBodyAdvice {
    @Autowired
    private RedisTemplate<String, String> redisTemplate;
    private ObjectMapper mapper = new ObjectMapper();

    @Override
    public boolean supports(MethodParameter returnType, Class converterType) {
        // 支持的处理类型，这里仅对get和post进行处理
        return returnType.hasMethodAnnotation(GetMapping.class) || returnType.hasMethodAnnotation(PostMapping.class);
    }

    @Override
    public Object beforeBodyWrite(Object body, MethodParameter returnType, MediaType selectedContentType, Class<? extends HttpMessageConverter<?>> selectedConverterType, ServerHttpRequest request, ServerHttpResponse response) {
        try {
            String redisKey = RedisCacheInterceptor.createRedisKey(((ServletServerHttpRequest) request).getServletRequest());
            // ...（后续代码未完全显示）
        }
    }
}
```

画面 8：
- 在 IntelliJ IDEA 中查看 MyResponseBodyAdvice.java 文件。
- 代码片段：
```java
@Override
public boolean supports(MethodParameter returnType, Class converterType) {
    // 支持的处理类型，这里仅对get和post进行处理
    return returnType.hasMethodAnnotation(GetMapping.class) || returnType.hasMethodAnnotation(PostMapping.class);
}
```
- 调试窗口显示当前执行位置在 `supports` 方法中，`returnType` 为 `CollectingData`，`converterType` 为 `CollectingData`。

画面 9：
- 在 IntelliJ IDEA 中查看 MyResponseBodyAdvice.java 文件。
- 代码片段：
```java
redisValue = mapper.writeValueAsString(body);
```
- 调试窗口显示当前执行位置在 `beforeBodyWrite` 方法中，`redisValue` 为 `"counts":0,"pagesize":10,"pages":2,"items":[{"id":40,"avatar":"https://itcast-tanhuai.oss-cn-shanghai.aliyuncs.com/images/logo/5.jpg","nickname":"helma 40"}]`，`mapper` 为 `ObjectMapper@89579`，`body` 为 `PageResult`。

画面 10：
- 在 IntelliJ IDEA 中查看 RedisCacheInterceptor.java 文件。
- 代码片段：
```java
// 未开启缓存
return true;
```
- 调试窗口显示当前执行位置在 `preHandle` 方法中，`method` 为 `GET`。

画面 11：
- 在 IntelliJ IDEA 中查看 RedisCacheInterceptor.java 文件。
- 代码片段：
```java
// 通过缓存命中，查询redis, redisKey？ 组成：md5（请求的url + 请求参数）
String redisKey = createRedisKey(request); redisKey = "SERVER_DATA_5c97329b5e0a4050b5f70d05030f..."; String data = this.redisTemplate.opsForValue().get(redisKey);
```
- 调试窗口显示当前执行位置在 `preHandle` 方法中，`redisKey` 为 `"SERVER_DATA_5c97329b5e0a4050b5f70d05030f..."`，`data` 为 `null`。

画面 12：
- 在 IntelliJ IDEA 中查看 RedisCacheInterceptor.java 文件。
- 代码片段：
```java
// 将data数据进行响应
response.setCharacterEncoding("UTF-8");
response.setContentType("application/json; charset=utf-8");
response.getWriter().write(data);
return false;
```
- 调试窗口显示当前执行位置在 `preHandle` 方法中，`data` 为 `null`。

画面 13：
- 在 IntelliJ IDEA 中查看 RedisCacheInterceptor.java 文件。
- 代码片段：
```java
// 将data数据进行响应
response.setCharacterEncoding("UTF-8");
response.setContentType("application/json; charset=utf-8");
response.getWriter().write(data);
return false;
```
- 调试窗口显示当前执行位置在 `preHandle` 方法中，`data` 为 `null`。

画面 14：
- 在 Typora 中打开 day02.md 文件。
- 文件内容包含章节标题和子标题，如“2.6.1. 前端请求入口”、“2.6.2. 修改配置”等。
- 当前光标位于“测试：”下方，显示代码片段：
```java
@Override
public Object beforeBodyWrite(Object body, MethodParameter returnType, MediaType selectedContentType, Class<? extends HttpMessageConverter<?>> selectedConverterType, ServerHttpRequest request, ServerHttpResponse response) {
    if (body instanceof String) {
        redisValue = (String) body;
    } else {
        redisValue = mapper.writeValueAsString(body);
    }
    // 保存到redis中
    this.redisTemplate.opsForValue().set(redisKey, redisValue, Duration.ofHours(1));
    return body;
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
public static String createRedisKey(HttpServletRequest request) throws Exception {
    String paramStr = request.getRequestURI();
    if (paramStr == null || paramStr.isEmpty()) {
        paramStr = "/";
    }
    Map<String, String[]> parameterMap = request.getParameterMap();
    if (parameterMap.isEmpty()) {
        paramStr
