# 21.功能开发之JWT的快速入门

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\21.功能开发之JWT的快速入门_【海量资源尽在 666java.com】.mp4
- 时长 5分51秒（音频 351s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续,那么前面呢,我们已经完成了短信验证码的一个发送与对接,那么接下来呢,我们就需要通过这个短信验证码呢,进行登录了,那么登录的时候呢,我们会设计到一个JWT这样的一个标准,或者说这样的一个技术,那么我们把这个技术呢,做一个简单的一个入门。
[00:25] 那么如果有同学已经掌握了这项技术的话那直接可以跳过本小杰OK好那么下面我们来看一下那么JWT呢它呢是它是什么呢它的全称是叫Jason Web Token这样的一个全称那么其实就是会帮助我们更加规范的去生成我们的一个Token了OK那么我们一起来看它的一个格式吧格式呢就这样的格式就是最终它是一个字幕串
[00:55] 其中呢是由三部分来组成的那么每一部分之间呢有一个点去做一个连接啊就是这样的一个结构那么第一部分呢代表的是他的投信息啊投信息那么第二部分呢是他的一些身份认证的验证的一些信息那第三部分呢是他的一些校验的一些信息啊那么所以是由这三部分去组成的那么他整个流程呢是这样的一个流程就是那么我们的用户那么去发起
[01:24] 我们的用户名密码这样的一个请求到服务端那服务端呢通过我们的这个程序然后呢去创建生成这个JWT这样的一个token然后呢把这个token呢返回给我们的一个用户那么用户呢将去做请求我们的API的时候呢需要去携带这个token要注意的是这个token的携带呢并不是跟着我们参数去做一个提交而是把这个token
[01:53] 放到哪里呢放到我们那个投信息就请求的投信息中放到这个里面来然后去提交到我们的服务端那么服务端呢去通过这个投信息中去拿到这个token的值然后呢去校验它是不是一个合法的一个token那么如果是的话就做一些逻辑的处理最后呢去做一个返回啊就是这样的一个逻辑了那么接下来呢我们来通过简单的API来演示一下这个JWT
[02:22] 在我们加码程序中怎么去使用啊那么首先呢我们需要去导入一个依赖那么这个依赖呢就可以帮助我们来生成这个JWT的一些这个token那我们把这个依赖呢来拷贝一下那么我们去找到我们的工程吧那么在这个POM文件中我们加到这吧把这个JWT啊加到这个位置来那么加入之后呢我们就可以去写一个测试用例那么我们就把这个测试用例
[02:52] 拷贝过来吧那么我们只要掌握了它的一个深层和一个解析啊就可以了那么我们先来看一下呃在这个位置啊先来看这个深层啊就是那么我们在这个位置啊定义了一个我们的数据就假设呢我们需要把这个数据啊呃做一个分装或者说做一个编码然后呢把它写到一个token里面最后去返回
[03:18] 那么在这个位置比如说我们的数据有两个一个是mobile一个就是ID那么mobile是135.6.7.8.9ID是v2这个是我们想要去传输的数据然后我们下面就直接通过JWTS的API去生成我们指定我们的一个数据这边的一个数据然后并且指定我们的加密的方法以及我的一个加密的源那么加密方法使用
[03:48] HS256那么然后后面其实就是一个加密的一个源那么就我们前面所提到的那个支付创那么我这个支付创使用就是一个itcast它作为我的一个加密的一个源那么最后去生成那我把它打印出来它就是这样的一个支付创然后我们可以通过这个GWTS去做一个解析解析就可以得到我们这个body中的数据那么就可以拿到我们最原始这个数据了那么
[04:17] 那么要注意的是啊那么呃在我们做解析的时候一定得知道我们的一个这个言啊知道这个言之后呢就能够去解析出来了那么如果你不知道这个言你是解析不出来的所以说前面我提到过这个言这个呢一定要我们要自己怎么呢保存好不能够啊把它泄露出去这是非常危险的啊ok好那么我们来执行一下这个代码呃我们就直接
[04:46] 来看这是个闷方法那么直接去执行这个闷方法我们来等待它的一个执行来看它结果是不是符合我们的一个预期OK那么我们来看一下结果那么第一个打印是不是就打印出我们所生成的token那么前面我们说到这个token其实是有三部分来组成的可以看到是不是你看这个是一部分对吧然后这个是一部分
[05:13] 然后在后面这个也是一部分三部分来组成那么下面的这个是不是就通过我们的 token对吧把 token 给他传递过来那么看一下是不是就是 token那么他是不是就通过一个我们 jwts 这样的一个 API去做一个解析就可以得到一个数据了就是我们存到 token 的数据了ok好那么掌握了基本的使用之后我们就可以来完成我们的一个登录的操作了
[05:43] OK好那么关于这个JWT的一个快速的一个入门那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 JWT（JSON Web Token）的原理、格式、流程，并通过代码示例演示如何生成和解析 JWT。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中 JWT 章节的“简介”部分，说明 JWT 是用于应用程序用户身份验证的标记，替代了传统的 cookie 或 session。
画面2：展示 Typora 文档中 JWT 章节的“流程”图，图示用户通过 HTTP POST 发送用户名和密码，服务器创建 JWT Token，用户在后续请求中通过 Authorization Header 传递 Token，服务器验证 Token 合法性并返回数据。
画面3：展示 Typora 文档中 JWT 章节的“示例”部分，包含导入依赖的 Maven 代码片段，用于引入 jjwt 库。
画面4：展示 IntelliJ IDEA 中项目结构和 pom.xml 文件，其中包含父项目依赖和 spring-boot-starter-web 依赖。
画面5：展示 IntelliJ IDEA 中 pom.xml 文件，添加了 RocketMQ-spring-boot-starter 和 jjwt 依赖。
画面6：展示 IntelliJ IDEA 中 TestJWT.java 文件，开始编写 JWT 生成和解析的测试代码。
画面7：展示 IntelliJ IDEA 中 TestJWT.java 文件，代码中定义了 claims 并调用 Jwt.builder().setClaims().signWith().compact() 生成 JWT。
画面8：展示 IntelliJ IDEA 中 TestJWT.java 文件，代码中调用 Jwt.parser().setSigningKey().parseClaimsJws().getBody() 解析 JWT。
画面9：展示 IntelliJ IDEA 中 TestJWT.java 文件，右键菜单中选择“Run 'TestJWT.main()'”。
画面10：展示 IntelliJ IDEA 中 TestJWT.java 文件，代码中调用 System.out.println(body) 输出解析后的数据。
画面11：展示 Typora 文档中 JWT 章节的“示例”部分，包含导入依赖的 Maven 代码片段。
画面12：展示 IntelliJ IDEA 中 TestJWT.java 文件的运行结果，控制台输出了生成的 JWT 和解析后的数据。
画面13：展示 IntelliJ IDEA 中 TestJWT.java 文件的运行结果，控制台输出了生成的 JWT 和解析后的数据。
画面14：展示 Typora 文档中 JWT 章节的“简介”部分，说明 JWT 是用于应用程序用户身份验证的标记。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```xml
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>
```

画面4：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>my-tanhua-sso</artifactId>
        <groupId>com.itcast.tanhua</groupId>
        <version>1.0.0-SNAPSHOT</version>
        <modelVersion>4.0.0</modelVersion>
    </parent>
    <artifactId>my-lanahua-380</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus</artifactId>
        </dependency>
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面5：
```xml
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
    <version>2.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-client</artifactId>
    <version>4.3.2</version>
</dependency>
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>
```

画面6：
```java
package com.tanhua.sso.Service;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.util.HashMap;
import java.util.Map;

public class TestJWT {

    public static void main(String[] args) {
        String secret = "itcast";
        Map<String, Object> claims = new HashMap<>();
        claims.put("mobile", "12345789");
        claims.put("id", "2");
        // 生成token
        String jwt = Jwts.builder()
                .setClaims(claims) // 设置响应数据体
                .signWith(SignatureAlgorithm.HS256, secret) // 设置加密方法和加密盐
                .compact();
        System.out.println(jwt); // eyJhbGciOiJIUzI1NiJ9.eyJjb250ZXh0IjoiMjAyMC0wMS0wMSAxMjM6MjE6MjIgIiwiYXV0aG9yaXphdGlvbiI6IjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwMjEwM

