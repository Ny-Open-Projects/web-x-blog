# 画面线理解：14-jwt：介绍以及创建token

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\14-jwt：介绍以及创建token_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:53, 01:51, 02:22, 03:06, 04:24, 05:03, 05:09, 05:40, 05:53, 06:16, 06:22, 06:29, 07:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:57:38

1) 这一组画面整体在讲什么（一句话）：
讲解JWT（JSON Web Token）的原理与在Java项目中的创建与使用方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT第21页，内容为HTTP Basic Auth、Cookie Auth和OAuth三种认证机制的对比与优缺点，重点说明Token机制的优势。
画面2：展示课程PPT第22页，继续讲解Token机制的优势，包括支持跨域、无需存储session、可配合CDN、去中心化、支持移动端、免CSRF、性能高、无需登录页面特殊处理、基于标准化的JSON Token（JWT）等。
画面3：展示课程PPT第22页，内容为“5.1 什么是JWT”和“5.2 JWT的快速入门”，并开始介绍如何创建JWT。
画面4：在IntelliJ IDEA中展示项目结构，打开`pom.xml`文件，显示`<parent>`标签和`<dependencies>`标签内的依赖配置。
画面5：在IntelliJ IDEA中，鼠标悬停在`<version>1.8-SNAPSHOT</version>`上，弹出“Create New Class”对话框。
画面6：展示课程PPT第22页，内容为“5.2.1 token的创建”，并列出创建maven工程、引入依赖、创建测试类等步骤。
画面7：在IntelliJ IDEA中，展示`CreateJwtTest.java`文件，代码中使用`Jwts.builder()`方法创建JWT。
画面8：在IntelliJ IDEA中，鼠标悬停在`setIssuedAt(new Date())`方法上，弹出方法参数提示。
画面9：在IntelliJ IDEA中，鼠标悬停在`signWith`方法上，弹出方法参数提示。
画面10：在IntelliJ IDEA中，鼠标悬停在`signWith`方法上，弹出方法参数提示。
画面11：在IntelliJ IDEA中，鼠标悬停在`SignatureAlgorithm`类上，弹出其所有子类和方法。
画面12：在IntelliJ IDEA中，鼠标悬停在`SignatureAlgorithm`类上，弹出其所有子类和方法。
画面13：在IntelliJ IDEA中，代码中使用`SignatureAlgorithm.HS256`作为签名算法。
画面14：在IntelliJ IDEA中，代码中添加了`String token = jwtBuilder.compact();`并输出token，控制台显示生成的token。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```xml
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.6.0</version>
</dependency>
```
```java
public class CreateJwtTest {
    public static void main(String[] args) {
        JwtBuilder builder = Jwts.builder().setId("888")
                .setSubject("小白")
                .setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "itcast");
        System.out.println(builder.compact());
    }
}
```
画面4：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <artifactId>ihrm_parent</artifactId>
        <groupId>com.ihrm</groupId>
        <version>1.8-SNAPSHOT</version>
    </parent>
    <artifactId>ihrm_common</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
    </dependencies>
</project>
```
画面6：
```xml
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.6.0</version>
</dependency>
```
```java
public class CreateJwtTest {
    public static void main(String[] args) {
        JwtBuilder builder = Jwts.builder().setId("888")
                .setSubject("小白")
                .setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "itcast");
        System.out.println(builder.compact());
    }
}
```
画面7：
```java
package com.ihrm.demo;
import io.jsonwebtoken.Jwts;
public class CreateJwtTest {
    public static void main(String[] args) {
        Jwts.builder().setId("888").setSubject("小白")
    }
}
```
画面13：
```java
public class CreateJwtTest {
    public static void main(String[] args) {
        JwtBuilder jwtBuilder = Jwts.builder().setId("888").setSubject("小白")
                .setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "itcast");
    }
}
```
画面14：
```java
public class CreateJwtTest {
    public static void main(String[] args) {
        JwtBuilder jwtBuilder = Jwts.builder().setId("888").setSubject("小白")
                .setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "itcast");
        String token = jwtBuilder.compact();
        System.out.println(token);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.1 HTTP Basic Auth”、“4.2 Cookie Auth”、“4.3 OAuth”。
画面2：PPT标题为“4.3 OAuth”。
画面3：PPT标题为“5.1 什么是JWT”、“5.2 JWT的快速入门”。
画面6：PPT标题为“5.2.1 token的创建”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
