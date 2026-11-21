# 画面线理解：22.WebSocket拦截器

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\22.WebSocket拦截器【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:55, 01:11, 01:25, 02:37, 03:08, 04:07, 04:34, 05:05, 05:25, 05:51, 06:21, 06:44, 07:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:32:37

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring WebSocket 中自定义握手拦截器（HandshakeInterceptor），包括实现拦截器类、配置拦截器并处理用户 ID，以及在连接建立后向客户端发送欢迎消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 PDF 讲义的目录结构，当前章节为“6.4.1 创建自定义拦截器”，并显示了 MyHandshakeInterceptor 类的代码开头。
画面 2: 在 IntelliJ IDEA 中，展示了 MyHandshakeInterceptor 类的完整代码，其中包含了实现 HandshakeInterceptor 接口的注释和方法签名。
画面 3: 展示了 MyHandshakeInterceptor 类中 beforeHandshake 方法的实现，用于在握手前将用户 ID 设置到会话属性中，并打印“开始握手”日志。
画面 4: 在 IntelliJ IDEA 中，展示了 MyHandshakeInterceptor 类的 beforeHandshake 方法，其中注释和代码与画面 3 相同。
画面 5: 展示了 MyHandshakeInterceptor 类中 beforeHandshake 方法的实现，其中注释和代码与画面 3 相同。
画面 6: 展示了 MyHandler 类中 afterConnectionEstablished 方法的代码，其中光标位于方法体内部，准备编写代码。
画面 7: 展示了 WebSocketConfig 类的代码，其中包含了 @Configuration、@EnableWebSocket 注解，以及注册处理器和拦截器的代码。
画面 8: 展示了 WebSocketConfig 类的代码，其中包含了 @Configuration、@EnableWebSocket 注解，以及注册处理器和拦截器的代码。
画面 9: 展示了 MyHandshakeInterceptor 类中 beforeHandshake 方法的实现，其中注释和代码与画面 3 相同。
画面 10: 展示了 MyHandshakeInterceptor 类中 beforeHandshake 方法的实现，其中注释和代码与画面 3 相同。
画面 11: 展示了控制台日志，其中包含“开始握手”日志和一个错误日志：“java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.String”，表明在 afterConnectionEstablished 方法中尝试将属性值转换为 String 类型时出错。
画面 12: 展示了 MyHandler 类中 afterConnectionEstablished 方法的代码，其中将 session.getAttribute("uid") 转换为 Integer 类型，并调用 session.sendMessage 发送欢迎消息。
画面 13: 展示了 MyHandler 类中 afterConnectionEstablished 方法的代码，其中将 session.getAttribute("uid") 转换为 Integer 类型，并调用 session.sendMessage 发送欢迎消息。
画面 14: 展示了 PDF 讲义的目录结构，当前章节为“6.4.1 创建自定义拦截器”，并显示了 WebSocketConfig 类的代码开头。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
package cn.itcast.websocket.spring;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.server.HandshakeInterceptor;
import java.util.Map;

画面 2:
package cn.itcast.websocket.spring;
public class MyHandshakeInterceptor implements HandshakeInterceptor {
    @Override
    public boolean beforeHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler wsHandler, Map<String, Object> attributes) throws Exception {
        //将用户id放入socket处理器的会话(WebSocketSession)中
        attributes.put("uid", 1001);
        System.out.println("开始握手。。。。。。");
        return true;
    }

    @Override
    public void afterHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler wsHandler, Exception exception) {
        System.out.println("握手成功啦。。。。。。");
    }
}

画面 3:
package cn.itcast.websocket.spring;
//将用户id放入socket处理器的会话(WebSocketSession)中
attributes.put("uid", 1001);
System.out.println("开始握手。。。。。。");
return true;

画面 4:
@Override
public boolean beforeHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler wsHandler, Map<String, Object> attributes) throws Exception {
    //将用户id放入socket处理器的会话(WebSocketSession)中
    attributes.put("uid", 1001);
    System.out.println("开始握手。。。。。。");
    return true;
}

@Override
public void afterHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler wsHandler, Exception exception) {
    System.out.println("握手成功啦。。。。。。");
}

画面 5:
@Override
public boolean beforeHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler wsHandler, Map<String, Object> attributes) throws Exception {
    //将用户id放入socket处理器的会话(WebSocketSession)中
    attributes.put("uid", 1001);
    System.out.println("开始握手。。。。。。");
    return true;
}

画面 6:
@Override
public void afterConnectionEstablished(WebSocketSession session) throws Exception {
    // 代码未完成
}

画面 7:
import org.springframework.web.socket.config.annotation.WebSocketConfigurer;
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry;
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    @Autowired
    private MyHandshakeInterceptor myHandshakeInterceptor;

    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(this.myHandler, "/ws")
                .setAllowedOrigins("*")
                .addInterceptors(this.myHandshakeInterceptor);
    }
}

画面 8:
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.config.annotation.EnableWebSocket;
import org.springframework.web.socket.config.annotation.WebSocketConfigurer;
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry;

@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    @Autowired
    private MyHandler myHandler;

    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(this.myHandler, "/ws")
                .setAllowedOrigins("*")
                .addInterceptors();
    }
}

画面 9:
//将用户id放入socket处理器的会话(WebSocketSession)中
attributes.put("uid", 1001);
System.out.println("开始握手。。。。。。");
return true;

画面 10:
//将用户id放入socket处理器的会话(WebSocketSession)中
attributes.put("uid", 1001);
System.out.println("开始握手。。。。。。");
return true;

画面 11:
2018-12-05 12:10:07.906 INFO 2396 --- [main] o.s.w.servlet.ServletRegistrationBean : Servlet /websocket mapped to [/*]
2018-12-05 12:10:07.922 INFO 2396 --- [main] o.s.w.servlet.FilterRegistrationBean : Mapping filter: 'websocket' to: [/*]
2018-12-05 12:10:08.248 INFO 2396 --- [main] o.s.c.concurrent.ThreadPoolTaskExecutor : Initializing ExecutorService 'taskExecutor'
2018-12-05 12:10:08.419 INFO 2396 --- [main] o.s.b.e.t.TomcatWebServer : Tomcat initialized with port(s): 8080 (http)
2018-12-05 12:10:14.191 INFO 2396 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet : Initializing Servlet 'dispatcherServlet'
2018-12-05 12:14:19.906 INFO 2396 --- [nio-8080-exec-1] w.s.h.ExceptionWebSocketHandlerDecorator : Closing WebSocket session
java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.String

画面 12:
@Override
public void afterConnectionEstablished(WebSocketSession session) throws Exception {
    Integer uid = (Integer) session.getAttributes().get("uid");
    session.sendMessage(new TextMessage (payload: uid+", 你好！欢迎连接到ws服务"));
}

画面 13:
@Override
public void afterConnectionEstablished(WebSocketSession session) throws Exception {
    Integer uid = (Integer) session.getAttributes().get("uid");
    session.sendMessage(new TextMessage (payload: uid+", 你好！欢迎连接到ws服务"));
}

画面 14:
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.config.annotation.EnableWebSocket;
import org.springframework.web.socket.config.annotation.WebSocketConfigurer;
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry;

@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    @Autowired
    private MyHandshakeInterceptor myHandshakeInterceptor;

    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(this.myHandler, "/ws")
                .setAllowedOrigins("*")
                .addInterceptors(this.myHandshakeInterceptor);
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向
