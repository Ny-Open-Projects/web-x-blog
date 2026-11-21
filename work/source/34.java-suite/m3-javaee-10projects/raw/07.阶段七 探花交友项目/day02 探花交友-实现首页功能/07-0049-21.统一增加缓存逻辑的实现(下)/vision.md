# 画面线理解：21.统一增加缓存逻辑的实现（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\21.统一增加缓存逻辑的实现（下）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:17, 00:25, 00:38, 00:41, 00:46, 00:52, 01:08, 01:29, 01:43, 01:52, 02:03, 02:09, 02:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:32:22

1) 这一组画面整体在讲什么（一句话）：
讲解如何通过自定义拦截器包装 HttpServletRequest 对象，以便在拦截器中多次读取请求体，用于实现 Redis 缓存功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程笔记中关于“包装 request 对象”的章节，引出问题：由于拦截器读取了请求体，导致 Controller 中无法再次读取。
画面 2: 展示项目结构，定位到 `interceptor` 包下的 `MyServletResponseAdvice.java` 和 `MyServletRequestWrapper.java` 文件。
画面 3: 展示 `MyServletRequestWrapper` 类的代码，定义了 `body` 字段和构造函数，将原始请求的输入流读取并转换为字节数组。
画面 4: 展示 `MyServletRequestWrapper` 类中重写的 `getReader()` 和 `getInputStream()` 方法，返回包装后的输入流。
画面 5: 展示 `MyServletRequestWrapper` 类中重写的 `isFinished()` 和 `isReady()` 方法，以及 `setReadListener()` 方法。
画面 6: 展示课程笔记中关于“通过过滤器进行包装 request 对象”的章节，引出解决方案：使用 `RequestReplaceFilter`。
画面 7: 展示 `RequestReplaceFilter` 类的代码，判断请求是否为 `MyServletRequestWrapper` 类型，如果是则进行包装。
画面 8: 展示 `RequestReplaceFilter` 类的完整代码，确认其继承自 `OncePerRequestFilter`，并重写 `doFilterInternal` 方法。
画面 9: 展示 `RedisCacheInterceptor` 类中 `preHandle` 方法的代码，判断 `enable` 是否为 true，如果是则返回 true。
画面 10: 展示 `RedisCacheInterceptor` 类中 `preHandle` 方法的代码，判断请求方法是否为 GET 或 POST，如果是则返回 true。
画面 11: 展示使用 Advanced REST Client 发起的 HTTP 请求，请求方法为 GET，包含 Authorization 头。
画面 12: 展示 `RedisCacheInterceptor` 类中 `createRedisKey` 方法的代码，用于构建 Redis 缓存键。
画面 13: 展示课程笔记中关于“通过过滤器进行包装 request 对象”的章节，再次强调解决方案。
画面 14: 展示课程笔记中关于“包装 request 对象”的章节，再次强调问题和解决方案。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@AutoRedCacheInterceptor redisCacheInterceptor;
@Override
public void addInterceptors(InterceptorRegistry registry) {
    registry.addInterceptor(this.redisCacheInterceptor).addPathPatterns("/**");
}
```

画面 2:
```java
package com.tanhua.server.interceptor;
import ...
/**
 * 包装HttpServletRequest
 */
public class MyServletRequestWrapper extends HttpServletRequestWrapper {
    private final byte[] body;

    /**
     * Construct a wrapper for the specified request.
     * @param request The request to be wrapped
     */
    public MyServletRequestWrapper(HttpServletRequest request) throws IOException {
        super(request);
        body = IOUtils.toByteArray(super.getInputStream());
    }

    @Override
    public BufferedReader getReader() throws IOException {
        return new BufferedReader(new InputStreamReader(getInputStream()));
    }

    @Override
    public ServletInputStream getInputStream() throws IOException {
        return new RequestBodyCachingInputStream(body);
    }

    @Override
    public boolean isFinished() {
        return lastIndexRetrieved == body.length - 1;
    }

    @Override
    public boolean isReady() {
        // This implementation will never block
        // We also never need to call the readListener from this method, as this method will never
        return isFinished();
    }

    @Override
    public void setReadListener(ReadListener listener) {
        if (isFinished() && listener != null) {
            try {
                listener.onAllDataRead();
            } catch (IOException e) {
                listener.onError(e);
                throw e;
            }
            return i;
        }
    }
}
```

画面 3:
```java
package com.tanhua.server.interceptor;
import ...
/**
 * 包装HttpServletRequest
 */
public class MyServletRequestWrapper extends HttpServletRequestWrapper {
    private final byte[] body;

    /**
     * Construct a wrapper for the specified request.
     * @param request The request to be wrapped
     */
    public MyServletRequestWrapper(HttpServletRequest request) throws IOException {
        super(request);
        body = IOUtils.toByteArray(super.getInputStream());
    }

    @Override
    public BufferedReader getReader() throws IOException {
        return new BufferedReader(new InputStreamReader(getInputStream()));
    }

    @Override
    public ServletInputStream getInputStream() throws IOException {
        return new RequestBodyCachingInputStream(body);
    }
}
```

画面 4:
```java
@Override
public boolean isFinished() {
    return lastIndexRetrieved == body.length - 1;
}

@Override
public boolean isReady() {
    // This implementation will never block
    // We also never need to call the readListener from this method, as this method will never
    return isFinished();
}

@Override
public void setReadListener(ReadListener listener) {
    if (isFinished() && listener != null) {
        try {
            listener.onAllDataRead();
        } catch (IOException e) {
            listener.onError(e);
            throw e;
        }
        return i;
    }
}
```

画面 5:
```java
package com.tanhua.server.interceptor;
import ...
/**
 * 包装HttpServletRequest
 */
public class MyServletRequestWrapper extends HttpServletRequestWrapper {
    private final byte[] body;

    /**
     * Construct a wrapper for the specified request.
     * @param request The request to be wrapped
     */
    public MyServletRequestWrapper(HttpServletRequest request) throws IOException {
        super(request);
        body = IOUtils.toByteArray(super.getInputStream());
    }

    @Override
    public BufferedReader getReader() throws IOException {
        return new BufferedReader(new InputStreamReader(getInputStream()));
    }

    @Override
    public ServletInputStream getInputStream() throws IOException {
        return new RequestBodyCachingInputStream(body);
    }
}
```

画面 6:
```java
package com.tanhua.server.interceptor;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * 包装request对象
 */
@Component
public class RequestReplaceFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        if (request instanceof MyServletRequestWrapper) {
            request = new MyServletRequestWrapper(request);
        }
        filterChain.doFilter(request, response);
    }
}
```

画面 7:
```java
package com.tanhua.server.interceptor;
import ...
/**
 * 包装request对象
 */
@Component
public class RequestReplaceFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        if (request instanceof MyServletRequestWrapper) {
            request = new MyServletRequestWrapper(request);
        }
        filterChain.doFilter(request, response);
    }
}
```

画面 8:
```java
package com.tanhua.server.interceptor;
import ...
/**
 * 包装request对象
 */
@Component
public class RequestReplaceFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        if (request instanceof MyServletRequestWrapper) {
            request = new MyServletRequestWrapper(request);
        }
        filterChain.doFilter(request, response);
    }
}
```

画面 9:
```java
@Override
public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
    if (!enable) {
        return true;
    }
    String method = request.getMethod();
    if (!StringUtils.equalsIgnoreCase(method, "GET") && !StringUtils.equalsIgnoreCase(method, "POST")) {
        return true;
    }
    return true;
}
```

画面 10:
```java
@Override
public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
    if (!enable) {
        return true;
    }
    String method = request.getMethod();
    if (!StringUtils.equalsIgnoreCase(method, "GET") && !StringUtils.equalsIgnoreCase(method, "POST")) {
        return true;
    }
    return true;
}
```

画面 11:
```json
{
  "code": 0,
  "pages": 1,
  "page": 1,
  "total": 41
}
```

画面 12:
```java
public static String createRedisKey(HttpServletRequest request) throws Exception {
    String paramStr = request.getRequestURI() + request.getParameterMap();
    Map<String, String[]> parameterMap = request.getParameterMap();
    if (parameterMap.isEmpty()) {
        // 请体的数据只能读取一次，需要进行包装request进行解决
    } else {
        paramStr += IOUtils.toString(request.getInputStream(), encoding, "UTF-8");
        String authorization = request.getHeader("Authorization");
        if (StringUtils.isNotEmpty(authorization)) {
            paramStr += "_" + authorization;
        }
    }
    return paramStr;
}
```

画面 13:
```java
package com.tanhua.server.interceptor;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
