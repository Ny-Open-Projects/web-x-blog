# 20.WebSocket服务之编写js客户端

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\20.WebSocket服务之编写js客户端【海量资源尽在 ubkz.com】.mp4
- 时长 5分28秒（音频 328s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么前面呢我们是通过使用了谷歌的这个一个插件还有就是一个在线的工具进行做了一个测试就是作为我们的一个客户端做一个测试那么接下来呢我们自己来写一个这个JS的一个客户端去做这样的一个测试那么其实这个代码也是相对比较简单的我们就一起来看一下那么我们就需要呢是在这个SRC这个门下面呢是不是创建一个目录叫web什么的APP
[00:30] 然后在这个下面我们需要去写一个我们的html的页面对吧html页面就叫index.html然后在index.html中我们就需要写一些我们的一些脚本那么在这个位置直接写一个script然后我们给大家看一下这个WebSocket怎么样去使用其实我们就是直接就可以去做这样的一个定义
[00:58] 那么要注意的是我们去使用这个WebSocket其实是不需要去不需要去引入一些额外的一些这个什么js或者说什么组件因为这个是浏览器内置就用这样的一个对象WebSocket的这个对象所以说我们直接去这样去写就可以了然后呢我们把它切换成一个这个ES6的版本要不然它这个cost不识别OK
[01:24] 好那么有了它之后啊那么我们就可以在这个里面去写一些类似于我们服务器刚刚所写的这样些代码有个叫什么的on一个什么的openonopen它呢其实是要去做什么呢是它它是在我们是不是建立连接的时候要去做一个事情对吧做什么事情呢我们来看一下咱们把这个给它抠过来哎直接写吧就呃后面呢它其实onopen的是所对应的是一个回到函数啊
[01:51] 所以在这个位置呢我们采用的是箭头函数然后呢ws然后呢箭头到什么呢就这然后呢我们是拿到这个ws然后呢就可以去做一些这个事情了对吧当然我可以打一句话点log是不是已经建立连接建立这个连接哎ok好那么这样的话呢我们是不是就已经建立这个连接当然了你可以把这个ws是不是也打印出来啊连接就建立了
[02:20] 其实跟我们服务端这个代码呢非常的相像啊这个是on这个open那还有一个呢是on这个message那么我就直接来call了啊然后呢这个就是一个on message拿到消息那我就打印把这个消息呢打印出来然后呢还有呢就是叫做on一个close然后呢on一个error把这两个拿过来那么on close呢就是关闭的时候on error呢就是发生错误的时候当然了在我们服务端呢它也有这个on error啊on一个error
[02:50] 它也是做一个错误这个我们就不做演示了这个大家也都能够理解好那么下面呢我们去写这两个逻辑就是我们在建立连接之后然后呢我们去两秒之后所以我们写一个这个定时器就两秒之后呢因为2000毫秒两秒之后我们向服务端去发一条消息就是发一条消息试试
[03:16] 然后在5秒之后我们去尝试把 socket给它断开close掉断开好那么我们去做这样的一个测试然后我们去访问一下我们的访问一下我们这个页面是不是就是http直接写吧就1270.0.18082然后下面的index.html找不到那么也就是说我这个加入之后它现在暂时没有识别
[03:48] 所以需要我把浏览器把服务端我去重启一下好那么现在重启好了我们来看一下他拿到我们这个页面了吗是不是拿到了那么我就可以来看一下它的控制台的一个输出ok那么我们再来刷新一下看我这样先把这个先清一下然后我去刷新看一下效果走首先建立连接对吧然后是不是服务端
[04:17] 给我们发了一个消息过来说一你好欢迎登录系统为什么是一呢原因是我们在建立联机的时候是不是传递的是一所以说他给我们发消息说一你好欢迎登录系统然后呢我们是不是接收到消息消息有收到就是说我们给他发我们给他发了一个消息叫什么呢叫发一条消息试试你看服务端是不是就收到一个说发一条消息试试这个内容然后呢我们是不是接收到一个服务端给我们的一个响应就是消息已收到
[04:46] 然后在5秒之后我们去断开我们连接去把连接断开然后我们的服务端是不是就显示WebSocket已关闭OK好那么这个其实就是一个客户端的编写其实代码的逻辑和代码编写跟我们的服务端非常的相像就是一些unopen
[05:07] on close这样的一些方法还有on message大家基本上把这几个注解还有客户端这么几个方法掌握那么这样的话我们就可以自己去编写服务端和我们的客户端了还是比较简单的OK好那么关于我们JS的客户端编写我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java Spring Boot 实现 WebSocket 服务端，并编写前端 JavaScript 客户端进行连接、收发消息和异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 WebSocket 在线测试工具界面，服务器地址为 ws://127.0.0.1:8082/WebSocket/1，状态为“尚未创建”，并有“开启连接”按钮。
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
画面 14：在 PDF 文档中，展示“6.5、Spring Boot整合WebSocket”章节，介绍如何在 Spring Boot 中使用 WebSocket。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
import java.io.IOException;
import javax.WebSocket.server.ServerEndpoint;
import java.io.IOException;
import javax.WebSocket.server.ServerEndpoint;
@ServerEndpoint("/WebSocket/{uid}")
public class MyWebSocket {
    @OnOpen
    public void onOpen(Session session, @PathParam(value = "uid")String uid) {
        System.out.println("WebSocket已经连接" + session);
        // 必客户端响应，欢迎登陆（连接）系统
        session.getBasicRemote().sendText("uid="+uid+", 你好！欢迎登陆系统");
    }
    @OnClose
    public void onClose(Session session) {
        System.out.println("WebSocket已经关闭" + session);
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
const socket = new WebSocket("ws://localhost:8082/WebSocket/1");
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
const socket = new WebSocket("ws://localhost:8082/WebSocket/1");
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
const socket = new WebSocket("ws://localhost:8082/WebSocket/1");
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
const socket = new WebSocket("ws://localhost:8082/WebSocket/1");
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
const socket = new WebSocket("ws://localhost:8082/WebSocket/1");
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
const socket = new WebSocket("ws://localhost:8082/WebSocket/1");
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
"C:\Program Files\Java\JDK 8.0_144\bin\java.exe" -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dclassworlds.conf=C:\Program Files\Java\JDK 8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-WebSocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\JDK 8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-WebSocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\JDK 8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-WebSocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\JDK 8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-WebSocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\JDK 8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-WebSocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\JDK 8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\1016\Documents\GitHub\itcast-WebSocket -Dmaven.home=E:\1016\apache-maven-3.2.3 -Dmaven.conf=C:\Program Files\Java\JDK 8.0_144\bin\maven.conf -Didea.version=2018.3 -Dfile.encoding=UTF-8 -Dmaven.multiModuleProjectDirectory=C:\Users\101

