# 18.WebSocket简介

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\18.WebSocket简介【海量资源尽在 ubkz.com】.mp4
- 时长 6分59秒（音频 419s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面呢我们来了解一下什么是WebSocket那么WebSocket呢它呢是HTML5中的一种新的一个协议那么这个协议呢现在已经被W3C认定为是一个标准那么也就是它是已经成为是一个标准了所以说我们是有必要去学习它包括我们现在一些主流的一些浏览器呢对它都做了一些很好的支持那么它实现了一个什么样的一个通信呢
[00:28] 它是实现了我们的浏览器注意是浏览器啊与服务器之间的一个什么呢全双工通信那么什么叫做全双工通信呢一会儿我们去来解释一下什么是全双工有什么叫单工的一个区别啊那么一开始握手的时候呢需要借助于http请求完成那么也就是说WebSocket它其实它其实是要借助于http
[00:56] 然后呢他呢也是在TCP这个协议的基础之上进行去做这样的一个实现的啊那么WebSocket他是实现了真正的具全双工通信的一个这样的一个技术啊哎OK你看他是一种在单个TCP连接的连接上进行全双工的一个通信的一个协议OK那么下面我们就来了解一下什么是全双工什么是单工的一个区别啊那么全双工的就是
[01:24] 它允许我们在两个方向上面同时进行传输同时做一个传输那么单公的或者说半双公是什么意思呢就是说在一个时间内只能有一个动作发生其实我们可以举一个例子在这个里面举一个例子就是说比如说我们有一个比较狭窄的一个马路同时只能过一辆车那么当目前有两辆车的时候那么这种情况下只能先过一辆
[01:51] 另外一辆呢是不是等着再过去对吧OK那么其实我们在早期的时候我们这种对讲机是不是也是这种啊呃半双工啊那么对讲机是不是我们去发出这个声音的时候你按住是不是发出声音的时候
[02:07] 然后呢我们在发出发出你这个语音的时候你是不能够去接受这个语音的是不是所以说哎所以说呢它是一个半双功的啊这样的一种方式啊哎OK那么全双功的就是我们可以同时进行双向的一个通信啊双向的一个传输OK这个就是它的一个区别啊好那么下面我们来看一下http与WebSocket的这个区别那么我们知道http它是一个什么呢短连接
[02:36] 在请求之后都会去做一个关闭把这个连接会关闭掉然后下次需要再去使用的时候我们再去把它建立连接再去做一些操作OK这个就是http的一个特点那么我们用图的形式去表示这个http请求过程就是你每一次想要请求这个数据都需要先建立连接然后请求数据这个时候连接就关闭掉了
[03:00] 然后呢当我下一次请求数据的时候呢我再打开连接再获取到数据然后再关闭以此类推啊一直往下面去去走那么WebSocket是怎么玩的呢它呢是一种什么呢注意它是一种长连接就是说我们的客户端就是我们浏览器跟我们的服务端一旦建立连接之后那么这个连接是不断开的啊注意这个连接是不断开的啊那么这个连接它
[03:29] 现在是不断开不断开之后呢我们是不是就可以在这两端是不是进行通信了对吧你他客户端可以向他是不是发消息对吧发数据那么服务端是不是也可以向他是不是去发数据啊OK好那么我们来看一下下面的这个图示啊就是说那么这个是我们的客户端客户端的向我们的服务器去做一个什么的握手就是我们要去打开我们这个连接那么一旦我们这个连接通道打开之后呢我们就建立了这样的一个通道
[03:58] 那么有了这个通道之后呢我们是不是就可以去向我们的服务器或者说服务器向我们去客户端向服务器或者服务器向客户端双向的都可以去发送个数据因为你这个通道是一旦建立就可以去双向发数据了然后呢最后呢如果要去断开这个连接的时候呢我们需要去做一个关闭
[04:20] 去客户端去请求我们的服务端还说我需要把这关闭掉然后服务端就把它关闭掉了那么服务端也可以强制去关闭这个通道OK好这个就是WebSocket大家可以想一想那么我们现在已经了解到什么是WebSocket对不对那么可以想一下那么前面我们所说的这个消息系统的一个或者消息这个功能的一个展现是不是就是当我们的这个浏览器打开的时候对吧那么我们就和服务器端是不是建立一个连接
[04:48] 那么OK建立这个连接之后那么我们这个浏览器是不是就不动了对吧然后我们服务器一旦有新的消息来的时候它是不是就会立刻是推送我们的数据是不是到我们的客户端那么当我们的客户端接收到这个数据的时候那我们在页面中是不是把它展现出来是不是就OK了OK好这个是不是就是通过这个WebSocket就可以解决我们刚刚所说的一个问题那么我们客户端是不需要是不是再去
[05:16] 轮旬去拿这个数据了OK好那么下面我们来看一下浏览器的一个支持情况就是WebSocket它的已经目前被主流的一些浏览器去做了一个支持但是并不是所有的浏览器都能去支持比如说像这个IE6 6到9它是不支持的比如说IE10以上它是支持的Chrome基本上都支持
[05:40] 那么FiveFox的低版本的不支持高版本的一般都支持这个是大家也可以去点击一下这个链接地址去查看一下这个浏览器的一些支持的情况来看一下可能他得稍微等一下查不到吗我们来我们把它call一下然后call到这
[06:12] 那么要查询的呢就是WebSocket它的一些支持的情况好那么其实我们可以看到现在一些目前的主流的一些浏览器是不是都对这个WebSocket做了支持所以说我们就现在它也是相对比较成熟的这样的一个通信的一个技术了我们也可以直接去使用它了
[06:33] 那么要注意的是在我们的服务器这一端在我们的服务器这一端那么对WebSocket的支持呢比如说我们要使用Tomcat你必须要使用这个7.0.47以上才能够去支持这个WebSocket的那么如果我们的服务器端不支持那么客户端支持那也没用那么你这个服务器就跑不起来啊哎OK好那么关于我们WebSocket的一个介绍或者说了解我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 WebSocket 技术的基本概念、与 HTTP 协议的区别、浏览器支持情况以及快速入门的 Maven 工程配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 PDF 文档中“6.1. 什么是WebSocket?”章节，解释了 WebSocket 是 HTML5 新的协议，实现了浏览器与服务器全双工通信，以及全双工和半双工的区别。
画面 2: 展示了“6.2.1. http”小节，说明 HTTP 协议是短连接，每次请求后会关闭连接，下次请求需重新建立连接。
画面 3: 展示了“6.2.2. WebSocket”小节，说明 WebSocket 协议是长连接，只需一次握手初始化连接，后续请求和响应通过该 TCP 连接进行。
画面 4: 展示了“6.3. 浏览器支持情况”小节，图示了 WebSocket 的握手、数据传输和关闭握手三个阶段。
画面 5: 展示了“6.3. 浏览器支持情况”小节，页面空白，仅显示底部的黑马程序员信息。
画面 6: 展示了“6.4. 快速入门”小节，显示了 caniuse.com 网站上关于 WebSocket 的浏览器支持表格，底部标注“服务器支持情况：Tomcat 7.0.4+以上才支持。”
画面 7: 展示了 caniuse.com 网站的首页，标题为“Can I use”，用于查询 Web 技术的浏览器支持情况。
画面 8: 展示了 caniuse.com 网站的“Support via Patreon”和“Site links”等页面内容。
画面 9: 展示了 caniuse.com 网站的“Index of features”页面，包含最新特性、最常搜索特性等信息。
画面 10: 展示了“6.4.1. 创建itcast-WebSocket工程”的 pom.xml 文件内容。
画面 11: 展示了 caniuse.com 网站的“Index of features”页面，包含最新特性、最常搜索特性等信息。
画面 12: 展示了 caniuse.com 网站关于 WebSocket 的详细支持情况，包含全球和中国使用率、各浏览器版本支持情况及备注。
画面 13: 展示了“6.4.1. 创建itcast-WebSocket工程”的 pom.xml 文件内容。
画面 14: 展示了“6.4. 快速入门”小节，显示了 caniuse.com 网站上关于 WebSocket 的浏览器支持表格，底部标注“服务器支持情况：Tomcat 7.0.4+以上才支持。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 10 和 13 中的 pom.xml 内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.itcast</groupId>
    <artifactId>WebSocket</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <name>WebSocket</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>3.1.0</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-web</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-beans</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-expression</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aop</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context-support</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-web</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-beans</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-expression</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aop</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context-support</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-web</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-beans</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-expression</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aop</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context-support</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-web</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>4.3.14.RELEASE</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-beans</artifactId>
            <

