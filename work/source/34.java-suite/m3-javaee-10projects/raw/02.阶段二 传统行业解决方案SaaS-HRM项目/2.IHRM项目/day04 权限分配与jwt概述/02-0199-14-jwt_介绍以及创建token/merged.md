# 14-jwt：介绍以及创建token

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\14-jwt：介绍以及创建token_【海量资源尽在 ubkz.com】.mp4
- 时长 7分47秒（音频 467s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们聊过了常见的这种认证机制,那接下来呢就是一起来看一下,在我们这个人力资源管理系统当中,其中也有用户的认证以及用户的健全的这么一些要求或者一些需求。
[00:19] 那我们这个系统当中如何去做的呢?
[00:22] 其实我们要从两个角度上来讲。
[00:25] 基于教学第一个呢我们是一起来看一下如何借助我们token的方式以JWT的形式完成用户的健全以及用户的认证那第二个呢就是我们之后会讲一个share安全框架其实通过share也可以完成用户的认证和健全的一些操作那么首先呢来看一下就是基于JWT的
[00:48] 那刚才说过了基于JWT其实JWT是我们刚才说的认证机制里面的最后一种叫做Token刚才说过它有一个标准叫做Jason Web Token那我们先来回顾一下这个JWT呢咱们之前的很多朋友其实都有所了解那么先来回顾一下JWT呢它究竟是什么它其实就是刚才说的Jason Web Token三个单词的简写
[01:12] 它是一个非常轻巧的这么一套规范这个规范允许我们使用JWT这种认证机制在我们的客户端以及我们的服务端进行传递数据并且传递的数据是安全可靠的一些内容不容易被篡改那在我们的Java世界当中要想去实现JWT规范很简单我们可以依赖一个开源的类库叫做JJWT去进行创建和进行它的解析等等相关的操作
[01:42] 那我们来看一下这个JWT如何去使用它那我们简单的一起来回顾一点就可以了首先呢这个JWT呢我们需要引入香的依赖因为它是一个开源的一个类库引进来那引进来之后呢我们可以写一些简单的代码去看一下如何用这个类库去生成一个token我们JW字符串以及如何对这个JWT字符串进行解析
[02:09] 那好了接下来呢我们就一起来看一下这个token如何进行创建好了在这边呢我找到我们的工程在我的common包下我在pub文件当中我可以引入我们这个jwt它的坐标那我这个坐标呢其实我就直接从我们的文件当中copy过来就可以我们的讲义当中拷过来
[02:34] 好了这个奖励当中靠过来这个坐标呢可能会有一些简单的问题我们简单的调一下就可以了OK简单的调了一下他这个坐标OK现在已经没有问题了那我已经把坐标引进来了接下来呢我就可以在common这边呢写一个我自己的简单的测试类咱们来完成token他的生成以及token他的一个解析
[03:03] 好了在这边呢我去创建一个我们第一个测试类把它放到com.ihim.demo这个包下比如说我起一个名字叫做第一个crete JWT test那我在这个测试类当中呢我就以mint方法的形式来进行测试了psvm来mint方法那在mint方法当中我们要验证的就是通过JJWTWT创建一个JWT字符串token字符串
[03:39] 那通过JWT创建token自付创呢其实很简单它的规格呢基本上都是一样的我们可以一起来看一下讲义来做一个简单的了解那我们其实可以记住它的一个工具类叫做JWTS这么一个工具类它里面的build方法
[03:55] 帮助我们去创建好了这里面的列式表达式的形式从头到尾一直写里面呢比如说你想存储一些你个人的一些ID比如说就是set ID比如说想存储一些自己的一些用名那就subject当然这里面不一定就要放ID不一定就要放小白这是我们约定俗成的一些做法比如说呢这边还有一个isot这个指的是我们签名的签发时间当然了最后还有一个就是我们签名的就是我们
[04:24] 签名的这种加密的一种算法和我们的一个私钥的一个信息那好了接下来呢我们就一起来看一下我们可以借助JWTS这么一个工具类打点叫做build那构建一个对象那好了可以往里面存放一些你私有的一些数据比如说呢我可以set id那set id比如说呢就我们就叫88好了再打点点setset subject比如说你自己的一些
[04:52] 用户信息比如说呢我们就叫小白好了那接下来呢我们还可以去设置就是当前你这个token它的一个创建时间就可以打点继续set好了我们找到签名的一个时间at好了接着new一个date就是我们当前的一个签名的一个时间嘛ok那接下来呢就是说我们放了这些内容之后由于我们要进行网络相互的一个传输放到头当中进行传输所以呢这玩意必然不可能被篡改
[05:23] 不能要求它被篡改那我们怎么防备呢就需要设置一些签名那设置签名主要是为了我们这个串不容易被篡改那么设置签名呢如何去做呢也比较简单我们可以找到设置签名的方法SI3位置OK好了那我们这个签名呢如何去做呢其实也不难也不难我们可以指定你当前签名的类型打点抱歉
[05:57] 抱歉好了我们这边The NatureS i j n a t u r e抱歉S i j n a t u r eOK好了我们这边它的加密的这种算法呢其实有很多其实有很多我们就用这个我们就用这个
[06:28] 256 HS256进行加密签名就可以了那当然了我们进行加密签名的时候呢可以加密加上我们自己定义的一个私钥那这个私钥呢我们可以随便写随便写比如说呢就叫做IHMOK那这样一来呢我们就可以通过
[06:46] JWT帮我生成这么一个JWBuilder这么一个对象那接下来我们可以通过Builder对象帮我们去创建真正的我们需要的这个字符串了OK这边呢Compact帮我们进行创建好了创建之后呢可以得到这么一个字符串比如说就叫Token那我们一起打印出来这个Token看一下效果以及各位能不能认识好了这边呢我们执行论闷方法走
[07:16] 这个执行起来还是比较快的我们一起来来去等待一下好了各位来看现在呢它生成的一个创呢其实已经有了那这个创呢其实就是包含了我们自己定义的一些素有数据比如88比如说小白比如说呢我们当前的签证的签名的一个时间还有我们以及包含了HRM我们私有MEO生成的这么一个加密的token资付创那这样一来我们的token就已经创建好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

