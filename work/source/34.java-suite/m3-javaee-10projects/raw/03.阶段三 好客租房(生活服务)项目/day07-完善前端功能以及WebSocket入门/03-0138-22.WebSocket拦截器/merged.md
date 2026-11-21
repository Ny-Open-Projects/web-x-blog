# 22.WebSocket拦截器

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\22.WebSocket拦截器【海量资源尽在 ubkz.com】.mp4
- 时长 7分25秒（音频 445s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢我们来介绍一下WebSocket的拦截器其实这个呢是我们所讲的是在Spring中为我们的WebSocket提供了一个它的拦截器就是可以在我们建立连接之前呢编写一些业务逻辑比如说做一些这个登录教验啊等等一些相关的逻辑其实这个它的表达一个意思其实跟我们前面所学的在Spring MVC中的
[00:24] 那个拦截器的这个意思是一样的就是在你起球之前对吧进入control之前呢去先去做一个拦截那么ok那么道理是相通的啊所以呢我们下面来看一下它的这个一个实现啊那么我们去写这样的一个是写这样的一个类然后去实现一个这样的一个呃intercept这样的一个接口然后呢我们去编写具体逻辑啊就可以了好那么我们创建一个类然后呢我们去实现啊这个接口啊去实现一下
[00:54] 实现这个接口然后我们把它的方法去实现一下那么实现是有两个方法两个方法然后我们来看这两个方法的编写首先我们需要把它加入到我们的spin容器加一个component然后我们把这两个方法我们就call过来这个就不做编写了然后我们call一下到这我们去拷贝一下在这然后我们来看一下这两个方法到底是干嘛的
[01:24] 那么首先第一个这个方法是第一个这个方法那么这个方法是在我们的握手之前就是我们在建立我们那个连接之前那么会执行我们这个方法如果我们这个方法返回值返回是true的话那么就会建立连接如果返回false的话就不会建立连接所以这个是在我们连接之前去做这个事情而下面这个方法是在我们这个连接就是握手成功之后
[01:54] 去执行我们这个方法OK那么在我们的这个里面呢我们写了一个小这个逻辑啊就是呃我在这个位置拿到一个attributes这个attributes呢它是一个map它其实呢是啊它其实是呃呃我们这个绘画就是我们这个session的一个绘画中的一个一个对象啊attribute的一个对象那么我们可以在这个里面去丢一些数据到我们那个session中所以呢我在这个位置呢去通过这个attributes点put
[02:23] 放一个UID1001进去当然了我这个只是做一个简单的一个demo所以我就把这个1001是不是写死了我把它写进去然后我就直接建立连接那么建立好retin2是不是就去让它去建立连接那么建立连接之后它肯定就会进入我们这个myhander那么在这个里面显然我们是不是就可以去拿到我那个UID那么怎么拿是不是通过这个通过这个sense去拿OK
[02:50] 那么应该是在这个位置吧在这个位置那么通过我这个session那个session点get什么attributes然后呢点get什么uid对吧那么我是不是就可以在这个位置来写一个谁是谁你好比如写到这这样吧我们写一个street uid id等于这个uid然后呢他呢去咱们去做一个强转把它转成这个uid然后呢在这个位置呢我们去写一个这个叫uid
[03:20] 就是谁是谁是不是你好不是逗号应该是家到这个位置是逗号你好然后欢迎连接到ws服务大家能够理解这个意思吧就是说在我们前面的intercept中就是我们拦截器中那么我们去放入了一个uid数据然后在我们的handle中在我们连接之后的方法里面它就能够去获取到我们uid
[03:49] 那么拿这个UID那么下面就可以去做一些其他的逻辑的一些处理了那么现在我们这个拦截器是不是已经是已经是有了对吧已经是我们创建好了但是我们并没有把它加入到我们的整加入WebSocket中那么怎么样加入我们来看一下我们就需要在我们的这个位置就是我们刚刚去添加这个handle这个位置给它添加一个添加我们这个拦截器我们来看一下那么找到我们configure page
[04:18] 在config page的后面在下面把它回测一下然后在这个位置去点什么呢end intercepts这个就是我们刚刚所写的我们需要把它注入进来叫my什么呢my hinder intercept把它拿过来把它注入下面我们就调用把它加进来
[04:48] 添加进来那么我们这个拦截器它是不是就会有生效了那么一会我们来看一下那么如果我们能够在我们这个里面是不是拿到拿到我们的UID那说明拦截器是不是就生效了当然了我们是不是也可以去加这样的一个断点我们来做一个调试对吧然后我把这个先给它这个已经先停掉然后我把它做一个debug的一个启动我们来做一个测试看它会怎么样等待它的一个启动
[05:20] 那么现在它就已经启动好了那么下面我来做一个测试点击这个连接走点击这个连接可以看到请求现在是不是已经就进入了我们的这个拦截器那么那就说明我们这个拦截器配置是不是已经生效了然后我们下面走放了在那个attribute的时钟是不是放了一个uid然后我们去打印一句话就是开始这个握手retin true就是让他去握手就是去建立连接走那么这样的话我们来看一下
[05:51] 我不能去转化我们看一下我这块web放的是一个int是吧所以在这个位置转化是有点问题的那么这样我把它停掉在我们的这个myhand中那么拿到的这个不是那应该用int吧去做一个接收然后呢我再来重启一下刚刚是类型转化的一个问题好那我们再去开启这个链接这样我刷新一下页面
[06:28] 然后我在这个位置点击开启连接那么它进入了然后走然后通过这样的话看一下控制台是不是开始握手握手成功了然后我们来看一下在我们的客户端这个位置是不是可以看到1001那么显然在我们这个my这个handle里面它是不是已经拿到了我们session中的一个attribute对吧ok那么我们是不是就已经学会一个知识是不是就是通过这个拦截器可以向我们的这个handle是不是去传递我们的一些数据
[06:57] 怎么传呢是不是丢到一个attribute里面去从这个里面是不是就可以拿到传的这个数据啊ok好那么这样的话呢我们是不是就去已经建立连接了然后呢我们尝试发一个实看一下会怎么样跟我们刚刚的效果是不是一样的ok有了这个拦截器那么就可以在建立连接之前呢去做一些业务逻辑的处理ok好那么这个呢就是拦截器的一个这个使用好那么关于拦截器呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package cn.itcast.WebSocket.spring;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.server.HandshakeInterceptor;
import java.util.Map;

画面 2:
package cn.itcast.WebSocket.spring;
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
package cn.itcast.WebSocket.spring;
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
2018-12-05 12:10:07.906 INFO 2396 --- [main] o.s.w.servlet.ServletRegistrationBean : Servlet /WebSocket mapped to [/*]
2018-12-05 12:10:07.922 INFO 2396 --- [main] o.s.w.servlet.FilterRegistrationBean : Mapping filter: 'WebSocket' to: [/*]
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

