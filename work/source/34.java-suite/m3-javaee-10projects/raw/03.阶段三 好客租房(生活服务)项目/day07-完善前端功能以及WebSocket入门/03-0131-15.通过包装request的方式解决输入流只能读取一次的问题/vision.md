# 画面线理解：15.通过包装request的方式解决输入流只能读取一次的问题

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\15.通过包装request的方式解决输入流只能读取一次的问题【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:35, 00:46, 01:18, 01:52, 02:03, 02:22, 04:07, 04:35, 04:56, 05:21, 05:38, 05:51, 06:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:27:17

1) 这一组画面整体在讲如何通过自定义拦截器包装 HttpServletRequest 对象，以解决在拦截器中读取请求体数据时因流被读取一次而无法再次读取的问题，并将其应用于 Redis 缓存的预处理。

2) 按时间顺序列出每张画面的要点：
画面1：讲解错误原因，指出在拦截器中读取输入流后，请求进入 Controller 时流已无数据。提出解决方案：通过包装 request 对象。
画面2：展示项目目录结构，定位到 day07 目录。
画面3：展示 GraphQlController 中的 postQuery 方法，用于处理 GraphQL 查询。
画面4：展示 MyServletRequestWrapper 类的构造方法，用于包装 HttpServletRequest。
画面5：展示 MyServletRequestWrapper 类中 getReader 和 getInputStream 方法的实现，用于返回包装后的输入流。
画面6：展示 MyServletRequestWrapper 类中 close 方法的实现，用于在关闭流时清空 body。
画面7：展示项目目录结构，定位到 interceptor 包。
画面8：展示 RequestReplaceFilter 类的代码，用于在请求处理前替换 HttpServletRequest 对象。
画面9：展示 RedisCacheInterceptor 类中 preHandle 方法的代码，用于判断请求方式并创建 RedisKey。
画面10：展示 RedisCacheInterceptor 类中 createRedisKey 方法的代码，用于根据请求参数生成 RedisKey。
画面11：展示使用 Altair GraphQL Client 发送请求并获取响应结果。
画面12：再次展示 GraphQlController 中的 postQuery 方法。
画面13：再次展示使用 Altair GraphQL Client 发送请求并获取响应结果。
画面14：展示 PDF 文档内容，说明在 Controller 中也可以获取到数据，问题解决。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
错误分析：由于在拦截器中读取了输入流的数据，在request中的输入流只能读取一次，请求进去Controller时，输入流中已经没有数据了，导致获取不到数据。
如何解决？
5.5.3、通过包装request解决
编写HttpServletRequest的包装类：
```

画面3：
```
Map<String, Object> error = new HashMap<>();
error.put("status", 500);
error.put("msg", "查询出错");
return error;

@PostMapping
@ResponseBody
public Map<String, Object> postQuery(@RequestBody Map<String, Object> param) {
    try {
        String query = (String) param.get("query");
        Map variables = (Map) param.get("variables");
        String operationName = (String) param.get("operationName");
        return this.executeQuery(query, operationName, variables);
    } catch (Exception e) {
        e.printStackTrace();
    }
    Map<String, Object> error = new HashMap<>();
    error.put("status", 500);
    return error;
}
```

画面4：
```
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

private class RequestBodyCachingInputStream extends ServletInputStream {
```

画面5：
```
@Override
public int available() throws IOException {
    return body.length - lastIndexRetrieved - 1;
}

@Override
public void close() throws IOException {
    lastIndexRetrieved = body.length - 1;
    body = null;
}
```

画面6：
```
通过过滤器进行包装request对象：
package cn.itcast.haoke.dubbo.api.interceptor;

import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
```

画面8：
```
package cn.itcast.haoke.dubbo.api.interceptor;

import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

@Component
public class RequestReplaceFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        if (!(request instanceof MyServletRequestWrapper)) {
            request = new MyServletRequestWrapper(request);
        }
        filterChain.doFilter(request, response);
    }
}
```

画面9：
```
// 判断请求方式，get还是post
if (!StringUtils.equalsIgnoreCase(request.getMethod(), "POST")) {
    return true;
}
// 通过操作符，查询redis
String redisKey = createRedisKey(request);
String data = this.redisTemplate.opsForValue().get(redisKey);
if (StringUtils.isEmpty(data)) {
    return false;
}
```

画面10：
```
public static String createRedisKey(HttpServletRequest request) throws Exception {
    String paramStr = request.getRequestURI(); // paramStr = "/graphql"
    Map<String, String[]> parameterMap = request.getParameterMap();
    if (parameterMap.isEmpty()) {
        paramStr = IOUtils.toString(request.getInputStream(), encoding);
    } else {
        paramStr += mapper.writeValueAsString(request.getParameterMap());
    }
    String redisKey = "WEB_DATA_" + DigestUtils.md5Hex(paramStr);
    return redisKey;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT标题为“5.5.3、通过包装request解决”。
画面6：PPT标题为“通过过滤器进行包装request对象”。
画面14：PPT标题为“5.6、响应结果写入到缓存”。

5) 不要评价画面美观，不要输出与课程无关的内容。
