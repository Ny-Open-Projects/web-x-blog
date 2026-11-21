# 画面线理解：21.功能开发之JWT的快速入门

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\21.功能开发之JWT的快速入门_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 01:18, 02:19, 02:40, 02:52, 02:55, 03:02, 04:06, 04:45, 04:48, 05:06, 05:20, 05:26, 05:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:11:55

1) 这一组画面整体在讲什么（一句话）：
讲解 JWT（JSON Web Token）的原理、格式、流程，并通过代码示例演示如何生成和解析 JWT。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中 JWT 章节的“简介”部分，说明 JWT 是用于应用程序用户身份验证的标记，替代了传统的 cookie 或 session。
画面2：展示 Typora 文档中 JWT 章节的“流程”图，图示用户通过 HTTP POST 发送用户名和密码，服务器创建 JWT Token，用户在后续请求中通过 Authorization Header 传递 Token，服务器验证 Token 合法性并返回数据。
画面3：展示 Typora 文档中 JWT 章节的“示例”部分，包含导入依赖的 Maven 代码片段，用于引入 jjwt 库。
画面4：展示 IntelliJ IDEA 中项目结构和 pom.xml 文件，其中包含父项目依赖和 spring-boot-starter-web 依赖。
画面5：展示 IntelliJ IDEA 中 pom.xml 文件，添加了 rocketmq-spring-boot-starter 和 jjwt 依赖。
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
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
    <version>2.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-client</artifactId>
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
package com.tanhua.sso.service;

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
