# 画面线理解：16.通过ResponseBodyAdvice实现数据写入到Redis

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\16.通过ResponseBodyAdvice实现数据写入到Redis【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:43, 01:54, 03:45, 05:05, 07:24, 08:16, 09:30, 10:29, 11:30, 12:34, 13:21, 14:19, 16:01, 16:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:28:13

1) 这一组画面整体在讲如何通过 Spring 的 ResponseBodyAdvice 实现将 HTTP 响应结果写入 Redis 缓存，并处理相关逻辑和 CORS 问题。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT 第 5.6 节“响应结果写入到缓存”，引出通过 ResponseBodyAdvice 实现将结果写入缓存的思路。
画面 2: 展示 RedisCacheInterceptor.java 文件中 createRedisKey 方法的代码，用于根据请求 URL 和参数生成 Redis 缓存键。
画面 3: 展示 MyResponseBodyAdvice.java 文件中 beforeBodyWrite 方法的代码，用于在响应体写入前将数据写入 Redis。
画面 4: 展示 MyResponseBodyAdvice.java 文件中 supports 方法的代码，用于判断是否支持对特定方法（如 @GetMapping）进行拦截。
画面 5: 展示 MyResponseBodyAdvice.java 文件中 supports 方法的代码，用于判断是否支持对特定方法（如 @PostMapping）进行拦截。
画面 6: 展示 MyResponseBodyAdvice.java 文件中 supports 方法的代码，用于判断是否支持对特定方法（如 @PostMapping）进行拦截。
画面 7: 展示 RedisCacheInterceptor.java 文件中 createRedisKey 方法的代码，用于根据请求 URL 和参数生成 Redis 缓存键。
画面 8: 展示 RedisCacheInterceptor.java 文件中 prehandle 方法的代码，用于判断请求方式并根据 URL 判断是否需要缓存。
画面 9: 展示浏览器开发者工具 Network 面板，显示了 CORS（跨域资源共享）错误，提示 Access-Control-Allow-Origin 头缺失。
画面 10: 展示课程 PPT 第 6 节“WebSocket”，并进入 6.1 节“网站中的消息功能如何实现？”。
画面 11: 展示 RedisCacheInterceptor.java 文件中 prehandle 方法的代码，用于判断请求方式并根据 URL 判断是否需要缓存。
画面 12: 展示 RedisCacheInterceptor.java 文件中 prehandle 方法的代码，用于判断请求方式并根据 URL 判断是否需要缓存。
画面 13: 展示浏览器开发者工具 Network 面板，显示了成功请求的响应信息，包括状态码 200 和响应头。
画面 14: 展示 MyResponseBodyAdvice.java 文件中 supports 方法的代码，用于判断是否支持对特定方法（如 @GetMapping）进行拦截。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
// 将data数据进行响应
response.setCharacterEncoding("UTF-8");
response.setContentType("application/json; charset=utf-8");
response.getWriter().write(data);
return false;

public static String createRedisKey(HttpServletRequest request) throws
        Exception {
    String paramStr = request.getRequestURI();
    Map<String, String[]> parameterMap = request.getParameterMap();
    if (parameterMap.isEmpty()) {
        paramStr += StringUtils.toString(request.getInputStream(), encoding: "UTF-8");
    } else {
        paramStr += mapper.writeValueAsString(request.getParameterMap());
    }
    String redisKey = "WEB_DATA" + DigestUtils.md5Hex(paramStr);
    return redisKey;
}
```

画面 3:
```java
if (returnType.hasMethodAnnotation(PostMapping.class) &&
        StringUtils.equals(GraphQLController.class.getName(), returnType.getExecutable().getDeclaringClass().getName())) {
    return true;
}

@Override
public Object beforeBodyWrite(Object body, MethodParameter returnType, MediaType selectedContentType,
        Class<? extends HttpMessageConverter<?>> selectedConverterType, Map<String, Object> map, ServerHttpRequest request, ServerHttpResponse response) throws Exception {
    String redisKey = RedisCacheInterceptor.createRedisKey((ServletServerHttpRequest) request);
    if (body instanceof String) {
        redisValue = mapper.writeValueAsString(body);
    } else {
        redisValue = mapper.writeValueAsString(body);
    }
    this.redisTemplate.opsForValue().set(redisKey, redisValue, Duration.ofHours(1));
    return body;
}
```

画面 4:
```java
private ObjectMapper mapper = new ObjectMapper();

@Override
public boolean supports(MethodParameter returnType, Class<?> converterType) {
    if (returnType.hasMethodAnnotation(GetMapping.class)) {
        return true;
    }
    if (returnType.hasMethodAnnotation(PostMapping.class) &&
            StringUtils.equals(GraphQLController.class.getName(), returnType.getExecutable().getDeclaringClass().getName())) {
        return true;
    }
    return false;
}
```

画面 5:
```java
package cn.itcast.haoke.dubbo.api.interceptor;

import ...

@ControllerAdvice
public class MyResponseBodyAdvice implements ResponseBodyAdvice {

    @Autowired
    private RedisTemplate<String, String> redisTemplate;
    private ObjectMapper mapper = new ObjectMapper();

    @Override
    public boolean supports(MethodParameter returnType, Class<?> converterType) {
        if (returnType.hasMethodAnnotation(GetMapping.class)) {
            return true;
        }
        if (returnType.hasMethodAnnotation(PostMapping.class) &&
                StringUtils.equals(GraphQLController.class.getName(), returnType.getExecutable().getDeclaringClass().getName())) {
            return true;
        }
        return false;
    }
}
```

画面 6:
```java
package cn.itcast.haoke.dubbo.api.interceptor;

import ...

@ControllerAdvice
public class MyResponseBodyAdvice implements ResponseBodyAdvice {

    @Autowired
    private RedisTemplate<String, String> redisTemplate; redisTemplate: RedisTemplate@8556
    private ObjectMapper mapper = new ObjectMapper(); mapper: ObjectMapper@9152

    @Override
    public boolean supports(MethodParameter returnType, Class<?> converterType) {
        if (returnType.hasMethodAnnotation(GetMapping.class)) {
            return true;
        }
        if (returnType.hasMethodAnnotation(PostMapping.class) &&
                StringUtils.equals(GraphQLController.class.getName(), returnType.getExecutable().getDeclaringClass().getName())) {
            return true;
        }
        return false;
    }
}
```

画面 7:
```java
// 通过缓存命中，查看redis.redisKey； 拼接：md5（请求的url + 请求参数）
String redisKey = createRedisKey(request); redisKey: "WEB_DATA b186676c0de93f3ad35456e027b66df"
String data = this.redisTemplate.opsForValue().get(redisKey); data: "data"|"HouseResources"
if (StringUtils.isEmpty(data)) {
    // 缓存未命中
    return true;
}
```

画面 8:
```java
// 判断请求方式，get还是post还是其他...
if (!StringUtils.equalsIgnoreCase(request.getMethod(), "get")) {
    if (!StringUtils.equalsIgnoreCase(request.getRequestURI(), "/graphql")) {
        return true;
    }
}
// 通过缓存命中，查看redis.redisKey； 拼接：md5（请求的url + 请求参数）
String redisKey = createRedisKey(request); redisKey: "WEB_DATA b186676c0de93f3ad35456e027b66df"
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    // 缓存未命中
    return true;
}
```

画面 11:
```java
// 判断请求方式，get还是post还是其他...
if (!StringUtils.equalsIgnoreCase(request.getMethod(), "get")) {
    if (!StringUtils.equalsIgnoreCase(request.getRequestURI(), "/graphql")) {
        return true;
    }
}
// 通过缓存命中，查看redis.redisKey； 拼接：md5（请求的url + 请求参数）
String redisKey = createRedisKey(request); redisKey: "WEB_DATA b186676c0de93f3ad35456e027b66df"
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    // 缓存未命中
    return true;
}
```

画面 12:
```java
@Override
public boolean prehandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
    // 判断请求方式，get还是post还是其他...
    if (!StringUtils.equalsIgnoreCase(request.getMethod(), "get")) {
        if (!StringUtils.equalsIgnoreCase(request.getRequestURI(), "/graphql")) {
            return true;
        }
    }
    // 通过缓存命中，查看redis.redisKey； 拼接：md5（请求的url + 请求参数）
    String redisKey = createRedisKey(request); redisKey: "WEB_DATA b186676c0de93f3ad35456e027b66df"
    String data = this.redisTemplate.opsForValue().get(redisKey);
    if (StringUtils.isEmpty(data)) {
        // 缓存未命中
        return true;
    }
}
```

画面 14:
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.MethodParameter;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.mvc.method.annotation.ResponseBodyAdvice;

import java.time.Duration;

@ControllerAdvice
public class MyResponseBodyAdvice implements ResponseBodyAdvice {

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    private ObjectMapper mapper = new ObjectMapper();
