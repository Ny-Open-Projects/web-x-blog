# 画面线理解：21.使用SpringBoot整合WebSocket

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\21.使用SpringBoot整合WebSocket【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:44, 01:10, 01:52, 02:18, 03:25, 04:22, 05:09, 05:53, 06:46, 07:37, 08:25, 09:13, 10:14, 10:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:31:46

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中整合 WebSocket，包括添加依赖、编写处理器、配置类和启动应用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面，标题为“6.5. SpringBoot整合WebSocket”，并开始讲解导入依赖。
画面2：在 IDEA 中编辑 pom.xml 文件，添加了 Spring Boot 的父依赖和自定义的 websocket 依赖。
画面3：在 pom.xml 中，继续编辑依赖部分，移除了注释的 javaee-api 依赖，并添加了 spring-boot-starter-websocket 依赖。
画面4：在 MyWebSocket.java 文件中，定义了 @ServerEndpoint 注解的类，包含 onOpen、onClose、onMessage 方法。
画面5：在 MyHandler.java 文件中，定义了 TextWebSocketHandler 的子类，重写了 handleTextMessage 方法，用于处理文本消息。
画面6：在 MyHandler.java 文件中，继续编辑，添加了 afterConnectionEstablished 和 afterConnectionClosed 方法。
画面7：在 IDEA 中，显示了 PPT 页面，其中包含多个代码截图和一个“运行”按钮。
画面8：在 WebSocketConfig.java 文件中，定义了 @Configuration 和 @EnableWebSocket 注解的类，用于配置 WebSocket。
画面9：在 WebSocketConfig.java 文件中，编辑 registerWebSocketHandlers 方法，准备注册处理器。
画面10：在 MyApplication.java 文件中，定义了 @SpringBootApplication 注解的主类，包含 main 方法。
画面11：在浏览器中打开 index.html 页面，显示了 WebSocket 的前端界面。
画面12：在 IDEA 中，显示了 MyHandler.java 文件的代码，并在控制台中显示了应用启动日志。
画面13：在 PPT 页面中，展示了 MyApplication.java 的代码，用于启动 Spring Boot 应用。
画面14：在 PPT 页面中，展示了 6.5.2 节“编写WebSocketHandler”的内容，包括需要实现的接口和导入的包。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
    <groupId>cn.itcast.websocket</groupId>
    <artifactId>itcast-websocket</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-websocket</artifactId>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.2</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
            <!-- 配置tomcat插件 -->
        </plugins>
    </build>
</project>
```

画面2：
```xml
<dependency>
    <artifactId>javaee-api</artifactId>
    <version>7.0</version>
    <scope>provided</scope>
</dependency>
```

画面3：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-websocket</artifactId>
</dependency>
```

画面4：
```java
@ServerEndpoint("/websocket/{uid}")
public class MyWebSocket {
    @OnOpen
    public void onOpen(Session session, @PathParam(value = "uid") String uid) {
        System.out.println("websocket已经连接：" + session);
        session.getBasicRemote().sendText("uid:" + uid + "，你好！欢迎登陆系统");
    }

    @OnClose
    public void onClose(Session session) {
        System.out.println("websocket已经关闭：" + session);
    }

    @OnMessage
    public void onMessage(String message, Session session) throws IOException {
        System.out.println("收到客户端发来的消息 --> " + message);
        try {
            session.getBasicRemote().sendText("收到消息：" + message);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

画面5：
```java
import java.io.IOException;

public class MyHandler extends TextWebSocketHandler {
    @Override
    public void handleTextMessage(WebSocketSession session, TextMessage message) throws IOException {
        System.out.println("收到消息：" + message.getPayload());
        if (message.getPayload().equals("10")) {
            for (int i = 0; i < 10; i++) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                session.sendMessage(new TextMessage("消息：" + i));
            }
        }
    }
}
```

画面6：
```java
@Override
public void afterConnectionEstablished(WebSocketSession session) throws Exception {
    session.sendMessage(new TextMessage("欢迎连接到ws服务"));
}

@Override
public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
    System.out.println("断开连接！");
}
```

画面8：
```java
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.config.annotation.EnableWebSocket;
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry;

@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
    }
}
```

画面9：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry;
import org.springframework.web.socket.config.annotation.WebSocketMessageHandler;
import org.springframework.web.socket.config.annotation.WebSocketTransportRegistration;
import org.springframework.web.socket.server.support.HttpSessionHandshakeInterceptor;
import org.springframework.web.socket.server.support.HttpSessionHandshakeInterceptor;

public class WebSocketConfig implements WebSocketConfigurer {
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(myHandler(), "/websocket").addInterceptors(new HttpSessionHandshakeInterceptor());
    }
}
```

画面10：
```java
package cn.itcast.websocket;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

画面12：
```java
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

@Component
public class MyHandler extends TextWebSocketHandler {
    @Override
    public void handleTextMessage(WebSocketSession session, TextMessage message) throws IOException {
        System.out.println("获取到消息：" + message.getPayload());
        if (message.getPayload().equals("10")) {
            for (int i = 0; i < 10; i++) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                session.sendMessage(new TextMessage("消息：" + i));
            }
        }
    }
}
```

画面13：
```java
@Bean
public WebsocketHandler myHandler() {
    return new MyHandler();
}
```

画面14：
```java
package cn.itcast.websocket.spring;

import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.WebSocketHandler;

public class MyWebSocketHandler implements WebSocketHandler {
    @Override
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {
        session.sendMessage(new TextMessage("欢迎连接到ws服务"));
    }

    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
        System.out.println("断开连接！");
    }

    @Override
    public void handleMessage(WebSocketSession session, WebSocketMessage<?> message) throws Exception {
        if (message.getPayload().equals("10")) {
            for (int i = 0; i < 10; i++) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                session.sendMessage(new TextMessage("消息：" + i));
            }
        }
    }

    @Override
    public void handleTransportError(WebSocketSession session, Throwable exception) throws Exception {
        System.out.println("传输错误：" + exception.getMessage());
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“6.5. SpringBoot整合WebSocket”，内容为“Spring
