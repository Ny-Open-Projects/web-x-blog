# 画面线理解：19.WebSocket服务之快速入门

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\19.WebSocket服务之快速入门【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:16, 02:03, 04:12, 05:17, 07:56, 09:17, 10:01, 10:56, 12:31, 13:29, 14:31, 16:31, 17:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:30:02

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java WebSocket API 创建一个简单的 WebSocket 服务并进行测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“6.4.1. 创建itcast-websocket工程”章节，其中包含 pom.xml 文件的开头部分，显示了 Maven 项目的基本配置。
画面 2: 在 IntelliJ IDEA 中展示 pom.xml 文件，高亮显示了 <dependency> 标签，其中定义了 <groupId>javaee</groupId> 和 <artifactId>javaee-api</artifactId>。
画面 3: 展示 PDF 文档中关于 Tomcat 配置的 Maven 插件部分，包含 <plugin> 标签内配置的 <configuration>。
画面 4: 展示 PDF 文档中“6.4.2. websocket的相关注解说明”章节，列出了 @ServerEndpoint、@OnOpen、@OnClose、@OnMessage 等注解的用法说明。
画面 5: 在 IntelliJ IDEA 中展示 MyWebSocket.java 文件，高亮显示了 @ServerEndpoint 注解，并在下方显示了 Session 类的自动补全建议。
画面 6: 在 IntelliJ IDEA 中展示 MyWebSocket.java 文件，编写了 onOpen 方法，其中包含 System.out.println 和 session.getBasicRemote().sendText 方法。
画面 7: 在 IntelliJ IDEA 中展示 MyWebSocket.java 文件，光标位于 onMessage 方法的定义处，显示了自动补全的 Session 类相关方法。
画面 8: 在 IntelliJ IDEA 中展示 MyWebSocket.java 文件，完整显示了 onOpen、onClose、onMessage 和 onError 方法的代码。
画面 9: 在 IntelliJ IDEA 中展示 pom.xml 文件，高亮显示了 <build> 标签内的 <plugins> 配置，其中包含 tomcat7-maven-plugin 的配置。
画面 10: 展示 PDF 文档中“6.4.4. 测试”章节，说明可以直接启动 Tomcat 进行测试，并提供了 Simple WebSocket Client 的在线工具链接。
画面 11: 展示 Simple WebSocket Client 浏览器插件界面，URL 设置为 ws://127.0.0.1:8082/websocket，状态为 CLOSED，准备连接。
画面 12: 展示 Simple WebSocket Client 浏览器插件界面，URL 设置为 ws://127.0.0.1:8082/websocket，状态为 OPENED，已连接成功。
画面 13: 展示在线 WebSocket 测试工具 easyswoole 的界面，显示了服务器配置和消息记录，其中包含“CLOSED -> 1006 CLOSE_NORMAL”的状态信息。
画面 14: 展示 PDF 文档中“6.4.1. 创建itcast-websocket工程”章节，再次显示了 pom.xml 文件的开头部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
```

画面 2:
```xml
<dependency>
    <groupId>javaee</groupId>
    <artifactId>javaee-api</artifactId>
    <version>7.0</version>
    <scope>provided</scope>
</dependency>
```

画面 3:
```xml
<configuration>
    <target>1.8</target>
    <encoding>UTF-8</encoding>
</configuration>
```

画面 4:
```text
@ServerEndpoint("/websocket/{uid}")
@OnOpen
public void onOpen(Session session, @PathParam("uid") String uid) throws IOException {
}
@OnClose
public void onClose() {
}
@OnMessage
public void onMessage(String message, Session session) throws IOException {
}
```

画面 5:
```java
package cn.itcast.websocket;
import javax.websocket.OnOpen;
import javax.websocket.server.ServerEndpoint;
@ServerEndpoint("/websocket/{uid}")
public class MyWebSocket {
    @OnOpen
    public void onOpen(Session session) {
    }
}
```

画面 6:
```java
@OnOpen
public void onOpen(Session session) throws IOException {
    System.out.println("websocket已经连接" + session);
    session.getBasicRemote().sendText("欢迎登陆系统");
}
```

画面 7:
```java
public void onMessage(String message, Session session) throws IOException {
    System.out.println("接收到消息：" + message);
    session.getBasicRemote().sendText("消息已收到");
}
```

画面 8:
```java
public void onError(Session session, Throwable error) {
    error.printStackTrace();
}
```

画面 9:
```xml
<plugin>
    <groupId>org.apache.tomcat.maven</groupId>
    <artifactId>tomcat7-maven-plugin</artifactId>
    <version>2.2.2</version>
    <configuration>
        <port>8082</port>
        <path>/</path>
    </configuration>
</plugin>
```

画面 10:
```text
https://chrome.google.com/webstore/detail/simple-websocket-client/pdflhobingboilbdejvdjgjhcodoov
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: PPT 标题为“6.4.2. websocket的相关注解说明”，内容为对 @ServerEndpoint、@OnOpen、@OnClose、@OnMessage 等注解的说明。
画面 10: PPT 标题为“6.4.4. 测试”，内容为测试方法说明和在线工具链接。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
