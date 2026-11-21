# 画面线理解：18.WebSocket简介

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\18.WebSocket简介【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 02:30, 02:34, 03:12, 05:20, 05:21, 05:25, 05:52, 05:54, 06:00, 06:05, 06:10, 06:14, 06:17, 06:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:29:22

1) 这一组画面整体在讲什么（一句话）：
讲解 WebSocket 技术的基本概念、与 HTTP 协议的区别、浏览器支持情况以及快速入门的 Maven 工程配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 PDF 文档中“6.1. 什么是WebSocket?”章节，解释了 WebSocket 是 HTML5 新的协议，实现了浏览器与服务器全双工通信，以及全双工和半双工的区别。
画面 2: 展示了“6.2.1. http”小节，说明 HTTP 协议是短连接，每次请求后会关闭连接，下次请求需重新建立连接。
画面 3: 展示了“6.2.2. websocket”小节，说明 WebSocket 协议是长连接，只需一次握手初始化连接，后续请求和响应通过该 TCP 连接进行。
画面 4: 展示了“6.3. 浏览器支持情况”小节，图示了 WebSocket 的握手、数据传输和关闭握手三个阶段。
画面 5: 展示了“6.3. 浏览器支持情况”小节，页面空白，仅显示底部的黑马程序员信息。
画面 6: 展示了“6.4. 快速入门”小节，显示了 caniuse.com 网站上关于 WebSocket 的浏览器支持表格，底部标注“服务器支持情况：tomcat 7.0.4+以上才支持。”
画面 7: 展示了 caniuse.com 网站的首页，标题为“Can I use”，用于查询 Web 技术的浏览器支持情况。
画面 8: 展示了 caniuse.com 网站的“Support via Patreon”和“Site links”等页面内容。
画面 9: 展示了 caniuse.com 网站的“Index of features”页面，包含最新特性、最常搜索特性等信息。
画面 10: 展示了“6.4.1. 创建itcast-websocket工程”的 pom.xml 文件内容。
画面 11: 展示了 caniuse.com 网站的“Index of features”页面，包含最新特性、最常搜索特性等信息。
画面 12: 展示了 caniuse.com 网站关于 WebSocket 的详细支持情况，包含全球和中国使用率、各浏览器版本支持情况及备注。
画面 13: 展示了“6.4.1. 创建itcast-websocket工程”的 pom.xml 文件内容。
画面 14: 展示了“6.4. 快速入门”小节，显示了 caniuse.com 网站上关于 WebSocket 的浏览器支持表格，底部标注“服务器支持情况：tomcat 7.0.4+以上才支持。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 10 和 13 中的 pom.xml 内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.itcast</groupId>
    <artifactId>websocket</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <name>websocket</name>
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
