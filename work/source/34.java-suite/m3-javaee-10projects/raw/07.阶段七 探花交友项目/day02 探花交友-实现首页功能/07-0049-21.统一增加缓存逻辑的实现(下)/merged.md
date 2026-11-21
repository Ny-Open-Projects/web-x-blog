# 21.统一增加缓存逻辑的实现（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\21.统一增加缓存逻辑的实现（下）_【海量资源尽在 666java.com】.mp4
- 时长 2分37秒（音频 157s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来讲一下前面我们所提到这个包装request对象的这个逻辑那么其实这个逻辑呢是相对比较固定的一种写法那我们就直接来使用它了那我们把这个所写的这个包装类呢我们就写到我们这个intercept中那我们来看一下那么它呢其实是实现了我们这个http然后servlet request wrapper这样的一个对象然后呢
[00:27] 在我们的下面这个方法中然后去对我们的这个request body中的一些这个输入流然后我们去做一些这种处理说一些这种复制那么这个代码是相对固定的我们可以直接去拿来使用然后下面我们需要做一个注册那么就是我们需要把我们的这个request对象就是包装的request对象然后注册到哪里注册到我们通过孤立器去做一个
[00:55] 注册啊注意它是过滤器啊并不是一个什么呢这个拦截器啊它是过滤器那么这个是我们的这个Servlet级别的对吧好那么接下来呢我们就把它拿过来就可以了那么我们简单来看一下它的逻辑吧就是我们去判断啊判断它是不是属于我们这个类型如果不是的话就做一个包装啊就是做这样的一个事情了好那我们就重新来做一个启动还是打这个断点我们来看一下好那么等待它的一个启动
[01:24] 好那么我们来看一下这个结果啊那么来请求一下然后呢我们往下面走那么其实我们只需要看一下我们的request对象啊它是一个什么对象呢可以看到它是不是已经变成我们的一个叫mySolidRequestRepresent这个对象了那么所以呢我们这个包装的这个
[01:45] 就OK了那么大家可以后面去测试一下什么如果我们发起的是一个Post请求并且我们去提交了一些参数那么如果我们没有去包装Request的话那么在Controller中是获取不到这个指导那么也就是在这个位置的一个逻辑了OK好那么这个我就不做一个演示和测试了大家可以去自行测试一下
[02:09] 那么我建议大家呢在我们的这个项目中呢就把这个包装的这个呢直接加进去然后呢我们就可以统一的完成这样的一个缓存的一个逻辑了那么其实我们这个统一的这个缓存逻辑的一个添加的这样的一些这个逻辑啊那么它是通用的就是我们可以直接移植到我们的项目中去做一些这个使用的OK好那么关于我们的这个包装request对象呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

