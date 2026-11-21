# 画面线理解：20.WebSocket服务之编写js客户端

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\20.WebSocket服务之编写js客户端【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:24, 00:54, 01:44, 02:14, 02:36, 02:54, 03:19, 03:32, 03:48, 04:04, 04:34, 04:58, 05:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:30:53

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java Spring Boot 实现 WebSocket 服务端，并编写前端 JavaScript 客户端进行连接、收发消息和异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 WebSocket 在线测试工具界面，服务器地址为 ws://127.0.0.1:8082/websocket/1，状态为“尚未创建”，并有“开启连接”按钮。
画面 2：在 IntelliJ IDEA 中，展示 MyWebSocket.java 服务端代码，包含 @ServerEndpoint 注解和 onOpen、onClose 方法。
画面 3：在 PDF 文档中，展示编写 JavaScript 客户端的代码片段，包含创建 WebSocket 实例和 onopen 事件。
画面 4：在 IntelliJ IDEA 中，展示 index.html 文件，其中包含创建 WebSocket 实例的代码。
画面 5：在 PDF 文档中，展示 JavaScript 客户端代码，包含 onmessage 事件处理。
画面 6：在 PDF 文档中，展示 JavaScript 客户端代码，包含 onclose 事件处理。
画面 7：在 IntelliJ IDEA 中，展示 index.html 文件，其中包含 onclose、onerror 事件处理。
画面 8：在 IntelliJ IDEA 中，展示 index.html 文件，其中包含 setTimeout 设置发送消息和断开连接的代码。
画面 9：浏览器打开 Google 搜索页面，准备访问 WebSocket 服务。
画面 10：在 IntelliJ IDEA 的终端中，执行 Maven 命令启动项目。
画面 11：浏览器开发者工具 Console 面板显示 WebSocket 连接建立和关闭事件。
画面 12：在 IntelliJ IDEA 中，展示 index.html 文件，其中包含完整的 JavaScript 客户端代码。
画面 13：在 PDF 文档中，展示 JavaScript 客户端代码，包含注释和测试结果。
画面 14：在 PDF 文档中，展示“6.5、SpringBoot整合WebSocket”章节，介绍如何在 SpringBoot 中使用 WebSocket。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
import java.io.IOException;
import javax.websocket.server.ServerEndpoint;
import java.io.IOException;
import javax.websocket.server.ServerEndpoint;
@ServerEndpoint("/websocket/{uid}")
public class MyWebSocket {
    @OnOpen
    public void onOpen(Session session, @PathParam(value = "uid")String uid) {
        System.out.println("websocket已经连接" + session);
        // 必客户端响应，欢迎登陆（连接）系统
        session.getBasicRemote().sendText("uid="+uid+", 你好！欢迎登陆系统");
    }
    @OnClose
    public void onClose(Session session) {
        System.out.println("websocket已经关闭" + session);
    }
}
```

画面 3：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<script>
const socket = new WebSocket("ws://localhost:8082/websocket/1");
socket.onopen = (ws) => {
console.log("建立连接！", ws);
}
socket.onmessage = (ws) => {
console.log("接收到消息 >> ", ws.data);
}
</script>
</body>
```

画面 4：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<script>
const socket = new WebSocket("ws://localhost:8082/websocket/1");
socket.onopen = (ws) => {
console.log("建立连接！", ws);
}
</script>
</body>
```

画面 5：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<script>
const socket = new WebSocket("ws://localhost:8082/websocket/1");
socket.onopen = (ws) => {
console.log("建立连接！", ws);
}
socket.onmessage = (ws) => {
console.log("接收到消息 >> ", ws.data);
}
</script>
</body>
```

画面 6：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<script>
const socket = new WebSocket("ws://localhost:8082/websocket/1");
socket.onopen = (ws) => {
console.log("建立连接！", ws);
}
socket.onmessage = (ws) => {
console.log("接收到消息 >> ", ws.data);
}
socket.onclose = (ws) => {
console.log("连接已断开！", ws);
}
</script>
</body>
```

画面 7：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<script>
const socket = new WebSocket("ws://localhost:8082/websocket/1");
socket.onopen = (ws) => {
console.log("建立连接！", ws);
}
socket.onmessage = (ws) => {
console.log("接收到消息 >> ", ws.data);
}
socket.onclose = (ws) => {
console.log("连接已断开！", ws);
}
socket.onerror = (ws) => {
console.log("发送错误！", ws);
}
</script>
</body>
```

画面 8：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<script>
const socket = new WebSocket("ws://localhost:8082/websocket/1");
socket.onopen = (ws) => {
console.log("建立连接！", ws);
}
socket.onmessage = (ws) => {
console.log("接收到消息 >> ", ws.data);
}
socket.onclose = (ws) => {
console.log("连接已断开！", ws);
}
socket.onerror = (ws) => {
console.log("发送错误！", ws);
}
// 2秒后向服务端发送消息
setTimeout(() => {
socket.send("发送一条消息测试");
}, 2000);
// 5秒后断开连接
setTimeout(() => {
socket.close();
}, 5000);
</script>
</body>
```

画面 10：
```bash
"C:\Program Files\Java\jdk1.8.0_144\bin\java.exe" -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dclassworlds.conf=C:\Program Files\Java\jdk1.8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-websocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\jdk1.8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-websocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\jdk1.8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-websocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\jdk1.8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-websocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\jdk1.8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-websocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\jdk1.8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-websocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\jdk1.8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\101
