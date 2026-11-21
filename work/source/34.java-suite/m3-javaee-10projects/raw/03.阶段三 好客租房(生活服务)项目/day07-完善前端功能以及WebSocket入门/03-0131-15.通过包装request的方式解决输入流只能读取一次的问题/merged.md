# 15.通过包装request的方式解决输入流只能读取一次的问题

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\15.通过包装request的方式解决输入流只能读取一次的问题【海量资源尽在 ubkz.com】.mp4
- 时长 6分17秒（音频 377s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来通过这个包装request这种方式来解决我们前面所提到这个问题就是我们这个流呢只能读取一次这个问题其实这个问题呢是一个比较经典的问题其实有很多我们在做项目的时候都会遇到这样的问题那么目前一个比较好的一个解决方案呢就是去重新包装这个request那么我们来看一下这个代码的一个实现代码的实现
[00:28] 那么首先呢我们要去写一个这个包装这个类啊这个类呢在我们的这个资料中啊有提供啊有提供那么我来看一下啊那么在这个里面打开来看一下这是一个包装类啊那么我们把这就把这个包装类的内容我们都贴到我们这个呃代码中啊我们来简单的我们去给大家去讲一下它的一个原理啊是怎么回事就是说我们写这样的一个类啊然后呢去
[00:57] 继承了我们的一个Servlet Request的一个Rop这个类然后在这个里面做什么事情呢就是我们去拿到我们的一个这个Body就是我们的一个请求那个流先读取就是说在这个里面其实我们已经读过它了读了一次之后后面的就不能再去读了然后读到之后呢我们把这个Body呢就去New一个我们这个这个我们自己写了个对象内部类然后呢我们去
[01:25] 就相当于带有缓存功能的这样的一个一波的stream然后呢把那个body呢就给到他给到他之后呢就是当我们再去读取这个流的时候啊那么我们直接就拿到他的这个里面的一个body就可以了不需要再去再去真正的去读那个流去了所以说他叫缓存的这个流啊就是这样的一个意思啊就是对我们原生态的request做了这样的一个包装哎OK
[01:52] 那么有了这个包装类之后那么这个问题就容易解决了那么下面我们就需要有这样的一个把我们的过滤器把我们的过滤器去给它去包装给它去做一个我们request对象的一个包装那么这个怎么玩是在这个里面就是说我们需要写一个我们的一个过滤器找一下这个资料这个里面应该也有这个过滤器咱们把这个类的内容也拷贝到
[02:21] 这个里面来那么拷贝到这个里面呢我们可以看到是不是它呢是Spring我们把它注册为Spring的一个component然后呢我们去继承了这个类这个叫once这个类什么意思呢简单的把这个说一下这个我们就不深入展开了就是这个类呢就保证我们这个过滤器呢只执行一次那么什么叫做只执行一次呢是因为我们不同的这个版本的这个
[02:51] 这个JavaE的这个实现就是他们看他或者其他容器的实现他可能会有有点不一样就是我们的过滤器那么在有些实现中的比如说像我们内部的跳转叫FORWARD这种跳转有些过滤器他是不执行那么有些他是执行的那么就是说这个标准的并不统一所以Spring就做了这样的一个事情就是你继承这个类就会保证你这个过滤器他只会执行一次那么就是说我们进入的时候执行一次
[03:20] 在做我们内部做一些跳转的时候就不再做一个执行了就是做这样的一个意思所以说我们就继承这个类然后在这个类里面我们去做这样的一个处理去拿到request那么我们去判断它是不是我们自己写的这个包装的一个类如果不是的话注意取反不是那我们就给他去new一个这个类给他做一个重新指向这个类是不是指向了我们包装这个类去了OK那么在我们这个包装这个类里面你传入一个request
[03:49] 那我是不是就把你包队里面的内容是不是全部都读到了哎OK就是这样的一个意思啊然后呢这个过滤器继续再往下面去走就OK了那么这样的话呢我们就实现了一个request一个包装那包装之后呢我们就再再来重启啊做一个测试啊那我们把这个服务呢重启那我把这个视频呢先暂停一下那么现在我们重启好了我们来测试一下啊那么我们还是按照之前的这个测试就是
[04:19] 我们前面测试这个post请求的时候啊在我们Controller里面是不是就拿不到拿不到我们请求的一个这样的一些参数那么显然他肯定是查询是失败的啊所以呢我们再次做一个测试走那么这个时候呢我们会发现那么这个request对象我们来看一下他呢其实就变成我们自己的这个对象注意啊注意来看一下是不是就刚刚我们所写的这个我们包装的这样的一个request对象哎OK那就说明我们前面所配置的一个过滤器它已经生效了
[04:47] 然后我们继续往下面走走走走那么其实在这个里面呢我们已经就去读取他的这个读取他的这个流读取流那么读取这个流呢其实已经拿到这个内容了对吧来看一下这个这个能看到吗叫pyram可以在这个位置是不是可以看到他的一个内容是不是就这样的一个内容啊然后呢我们继续往下面走走走到这做一个命中
[05:15] 命中没有命中是不是就return然后我们继续走通过那么通过之后可以看到数据结果是不是已经查到了那就说明什么我们这个是不是在我们的Controller这个里面是不是也拿到数据了这样我们为了验证我们在这个位置也打一个断点我们再来重新测试一下然后通过然后你可以看到是不是已经进入到我们的Controller在Controller中是不是也能够拿到数据
[05:42] 拿到一个请求的一个数据OK那就说明我们是不是通过这个包装request这种方式是不是就解决了这个问题这个也是一个比较经典的这样的一个问题也希望大家能够把这种解决方案能够学会其实大家去读一下这个代码也能够读懂它的一个意思OK好那么这样的话我们是不是就
[06:05] 解决了前面这个问题那么也就意味着我们这个添加缓存或者说我们从缓存命中这个逻辑是不是就已经写完了好那么关于这个呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
    String paramStr = request.getRequestURI(); // paramStr = "/GraphQL"
    Map<String, String[]> parameterMap = request.getParameterMap();
    if (parameterMap.isEmpty()) {
        paramStr = IOUtils.toString(request.getInputStream(), encoding);
    } else {
        paramStr += Mapper.writeValueAsString(request.getParameterMap());
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

