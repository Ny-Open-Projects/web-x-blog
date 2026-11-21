# 03-SpringBoot快速入门

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\03-SpringBoot快速入门_【海量资源尽在 ubkz.com】.mp4
- 时长 10分43秒（音频 643s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完Spring Boot的概述
[00:03] 接下来我们来介绍Spring Boot快速入门
[00:07] 在这一小节中
[00:08] 我们将来快速的搭建一个Spring Boot的入门计划工程
[00:12] 我们来体验一下Spring Boot
[00:14] 构建Spring项目到底有多快
[00:18] 好嘞
[00:19] 那么接下来我们来看一下需求以及实现步骤
[00:22] 需求呢说搭建Spring Boot的工程
[00:25] 定义Hello Controller的Hello方法
[00:28] 返回一个字幕串
[00:29] Hello Spring Boot
[00:31] 就可以了
[00:32] 那么对于这个需求
[00:34] 我们先不管是用Spring Boot怎么做
[00:36] 我们先来思考一下使用Spring怎么来完成
[00:41] 我相信如果用Spring来完成这个需求
[00:44] 对于很多同学来说应该是手到擒来的
[00:47] 对吧
[00:48] 那么我们来想
[00:49] 首先呢你可能要去搭建一个Maven的工程吧
[00:52] 然后呢引入一堆的坐标
[00:54] Spring的坐标
[00:55] Spring MVC相关的坐标
[00:57] 对吧
[00:58] 弄完了之后呢
[00:59] 我们写一个Controller
[01:00] 搞个注解
[01:01] 写个方式
[01:01] 做一个方法
[01:02] 最后呢
[01:02] 我们要对Spring MVC进行一个配置
[01:05] 配置完了之后
[01:06] 我们再去引入一个TalentMaker的插件
[01:09] 一起动
[01:10] 一运行
[01:10] 一访问
[01:11] 是不是就可以了
[01:12] OK
[01:12] 那么接下来我们来看一下Spring Boot
[01:15] 它的实现步骤
[01:17] 那么首先同样还是第一件事
[01:19] 创建一个Maven的项目
[01:20] 这个没有什么好说的
[01:22] 第二个呢
[01:22] 要引入Spring Boot的一些起步的依赖
[01:27] 那么这个起步依赖
[01:28] 刚才我们也介绍了
[01:29] 其实就是一些坐标
[01:30] 只不过
[01:31] 比我们之前引坐标要简单一些
[01:33] 第三个呢
[01:35] 定义Controller
[01:36] 跟开发Spring的项目
[01:38] 没有什么区别
[01:39] 第四个
[01:40] 编写一个引导类
[01:42] 那么这个引导类
[01:43] 其实就是我们项目
[01:45] Spring Boot项目的一个入口啊
[01:47] 这个我们待会会重点讲解
[01:49] 然后第五个
[01:50] 启动测试
[01:52] 我们注意发现
[01:53] 在整个这个步骤中
[01:55] 我们没有去写任何的一行配置
[01:58] 我们也没有去引入一个TalentMaker
[02:01] 在这插件
[02:02] 对吧
[02:02] 我们下来就来完成这个快速入门代码的编写
[02:07] 打开idea
[02:09] 在这个地方呢
[02:09] 我们去创建一个模块
[02:12] 好
[02:12] 新的模块
[02:13] 这个模块呢
[02:14] 我们就选用Maven的模块了
[02:16] 然后呢
[02:16] 我们写个包
[02:17] com.it
[02:19] IT黑马
[02:21] 然后呢
[02:21] 叫做Spring Boot-HelloWorld
[02:28] OK
[02:29] 然后呢
[02:30] 这个名呢
[02:30] 我们把它复制一下
[02:31] 因为idea对这个横杠的支撑不太好
[02:34] 他会忽略了横杠
[02:36] finish
[02:37] 创建完这个Spring Boot的快速入门的项目之后
[02:41] 那么我们进入到了PoM文件之间
[02:44] 那么接下来就要引入对应的起步依赖和一些坐标
[02:47] 那么这个坐标在哪找呢
[02:50] OK
[02:50] 那么在这个地方我们有官方的文档
[02:53] 这个文档我们找到这个地方
[02:55] 这个getting started
[02:56] 然后往下看
[02:57] 这个地方有一个Maven installation
[03:00] 就是使用Maven来构建的项目
[03:01] 这个Spring Boot工程该怎么来做
[03:04] 点进去
[03:04] 稍等
[03:06] 点进去之后呢
[03:07] 这个地方他给你提供了一个对应的PoM文件
[03:10] 然后呢
[03:11] 这是他提供的项目的坐标
[03:13] 然后这个地方很重要
[03:14] 提供了一个parent
[03:16] OK
[03:16] 我们把它粘过来
[03:18] 这个parent呢
[03:19] 是一个副项目
[03:21] 好
[03:21] 我们写一下
[03:22] 就是Spring Boot
[03:24] Spring Boot
[03:26] 这个工程
[03:28] 工程
[03:30] 需求
[03:31] 需要继承
[03:33] 继承的副工程
[03:37] 那么至于这个副工程
[03:39] 到底有什么作用
[03:40] 待会我们是下一小节来重点讲解
[03:43] 反正先继承了这么一个副工程
[03:45] OK
[03:45] 那么再往下看
[03:47] 这个地方呢
[03:48] 有一个dependencies
[03:49] dependencies里边有一个坐标
[03:51] 就是dependencies
[03:51] 里边有一个名字
[03:52] 叫做Spring Boot
[03:53] starter-web
[03:54] 这个其实呢
[03:55] 就是web相关的坐标
[03:58] 都在这个坐标里边
[03:59] 被依赖传递进来了
[04:01] 然后最后有一个build
[04:02] 一个工具插件
[04:04] 这个插件我们可以不导
[04:05] 我们就导这么一个dependencies
[04:07] 这个坐标就可以了
[04:09] 这个东西呢
[04:09] 就是我们真正的起步依赖
[04:11] 好
[04:12] 我们可以写个注释
[04:13] 放这
[04:14] web开发的起步依赖
[04:18] OK
[04:19] 那么我们其实呢
[04:20] 只导到这么两个坐标
[04:22] 一个是副工程
[04:23] 一个是web开发的起步依赖
[04:25] 我们整个所需要的坐标就导完了
[04:28] 而且呢
[04:28] 在这个地方
[04:29] 我们并没有规定版本
[04:31] 注意看
[04:31] 对吧
[04:32] 这些东西呢
[04:33] 我们将留到下一小节原理分析
[04:35] 我们再来讲解
[04:36] 那么写完了这个坐标pom文件之后呢
[04:39] 接下来我们就可以写对应的代码了
[04:42] 写代码呢
[04:43] 其实你就跟你之前写Controller一样
[04:46] 我们写一个包
[04:47] com.it
[04:48] 黑码.
[04:50] 比如说叫做hello Controller
[04:54] OK
[04:54] 写完了这个Controller之后呢
[04:57] 我们就可以来写一个注解
[04:59] 比如说rest Controller
[05:01] 然后接下来我们可以写一个request mapping
[05:04] request mapping里边呢
[05:05] 我们写
[05:06] 算了
[05:06] 我们因为是入门级的项目
[05:08] 在这个地方呢
[05:09] 我们就不写这个request mapping了
[05:10] 待会呢
[05:11] 我们直接在方法上来访问就可以了
[05:13] 好
[05:14] 那么接下来我们来写一个方法
[05:16] public string
[05:17] 叫做hello
[05:18] return一个字幕串
[05:21] 叫做hello
[05:23] street
[05:26] boot
[05:27] 好
[05:27] 写个他号
[05:28] 那么这个返回值也写了一个request mapping
[05:31] 写完了之后呢
[05:31] 我们在这个方法上加上这么一个request mapping
[05:35] 然后路径给他规定一下
[05:37] 这个hello就可以了
[05:38] 那么这个Controller非常简单
[05:41] 他就有一个方法啊
[05:42] 返回一个字幕串
[05:43] 然后呢
[05:44] 他的访问路径呢
[05:46] 叫做hello
[05:46] 那么我们这个Controller也就写完了
[05:48] 那么接下来这个Controller写完了之后呢
[05:51] 我们要启动这个项目
[05:53] 要来访问他该怎么启动呢
[05:54] 我们就需要来编写
[05:56] Spring boot里边非常有特点的这么一个东西
[05:59] 叫做引导类啊
[06:01] 这个地方呢
[06:01] 我们这个包我们改一下
[06:03] 比如说我们叫做Controller
[06:04] 好
[06:05] 改个包啊
[06:08] 改个包
[06:09] OK一下
[06:10] 改完了之后呢
[06:11] 我们在这个里边呢
[06:12] 我们再写一个
[06:13] 再写一个类吧
[06:15] 写个引导类啊
[06:16] 引导类呢
[06:17] 我们com.it
[06:19] 我们把它放到这个根目录下
[06:21] 比如说叫做hello
[06:23] applicto
[06:26] 那么这个地方要注意啊
[06:28] 就是说这个引导类啊
[06:30] 一般情况下
[06:31] 它的后缀结尾都是application结尾的
[06:34] 然后这个引导类第一步要求
[06:36] 好我们先来说一下引导类干啥呢
[06:39] 这是引导类
[06:41] 引导类
[06:42] 你可以简单的先把它理解为Spring boot
[06:47] Spring boot项目的入口
[06:52] 那么这个入口呢
[06:53] 首先第一个我们要在这个工程上加一个注解
[06:56] 叫做Spring boot application
[06:58] 这是第一件事儿
[06:59] 编写引导类呢
[07:00] 要注意这个事儿
[07:01] 然后第二件事儿
[07:02] 我们写个MEM方法
[07:04] MEM方法里边就一行代码
[07:06] 这行代码呢
[07:07] 相对来说比较固定
[07:09] Spring application
[07:11] 第二run方法
[07:12] 还有静态方法是run方法
[07:14] run方法里边传餐就传这个hello application
[07:17] 第二class就可以了
[07:19] OK
[07:19] 当然了
[07:20] 如果你想传的话
[07:21] 可以把这个args也传进去
[07:23] 这个参数就是这个地方的args也传进去
[07:26] 那么至于这行代码是干啥的
[07:28] 待会儿我们会在原理分析的时候呢
[07:30] 重点讲解哈
[07:32] OK
[07:32] 那么这个引导类也写完了
[07:34] 里边有个MEM方法
[07:35] 将来我们要运行Spring boot的项目
[07:37] 就直接运行这个MEM方法就可以了
[07:41] 那么整个代码我们就写完了
[07:43] 你会发现啊
[07:43] 非常简单
[07:44] 我们创建了个MEM工程
[07:46] 然后呢
[07:46] 导入了个坐标
[07:48] 写了一个control
[07:49] 然后写了个引导类
[07:50] 其他的事儿我们都没干
[07:52] 然后接下来我们来运行一下
[07:53] 点这个绿色的箭头运行一下
[07:58] 稍等他正在构建
[07:59] 好
[07:59] 运行一下之后呢
[08:00] 我们就写了个Ctrl-2
[08:00] 然后写了个引导类
[08:01] 运行一下之后呢
[08:02] 我们来看控制台的打印情况
[08:03] 你注意看哈
[08:05] 这个idea
[08:07] 这个工具啊
[08:08] 对Spring boot的项目支撑啊
[08:10] 还是比较友好的
[08:11] 你看这个控制台里边的日志啊
[08:13] 五颜六色的
[08:13] 非常的友好
[08:14] 对吧
[08:15] 然后呢
[08:16] Spring boot项目在启动的时候呢
[08:18] 有个启动的日志
[08:19] 这个日志呢
[08:20] 你注意看
[08:20] 我相信大家应该都能看懂
[08:22] 这是啥意思
[08:23] Spring
[08:24] 然后呢
[08:25] 下边有个一只箭
[08:26] 离弦的箭
[08:28] 说明Spring boot
[08:29] 可以让Spring
[08:30] 跑得很快
[08:31] 下边是Spring boot的版本
[08:33] 2.1.8
[08:34] release版本
[08:35] 那么这个版本呢
[08:36] 是最新的
[08:37] 这么一个Spring boot的版本
[08:39] 那么启动完成了之后呢
[08:41] 接下来我们要来访问
[08:43] 访问
[08:44] 怎么来访问呢
[08:45] 我们又没有Tomcat
[08:46] 我们怎么访问呢
[08:47] 其实你要看这个日志信息
[08:49] 最下边他给你说的有啊
[08:51] Tomcat started on port 8080
[08:55] 已经内置的Tomcat
[08:57] 已经启动了
[08:58] 在那个端口呢
[08:59] 8080
[09:00] 这么一个端口
[09:01] 那么接下来
[09:02] 我们就可以打开浏览器
[09:03] 访问一下
[09:05] localhost
[09:06] 冒号8080-hello
[09:09] 好访问一下
[09:10] 你看hello
[09:11] Spring boot
[09:12] 那么这样呢
[09:13] 我们Spring boot
[09:14] 这个工程就访问成功了
[09:17] 并且呢
[09:17] 我们写了一个Controller
[09:18] 也在浏览器上
[09:19] 成功的访问到了
[09:20] 这么一串字符串
[09:23] 整体的感觉还是比较快速的
[09:26] OK
[09:26] 写完了快速入门的Spring boot的工程
[09:29] 我们来做一个简单的
[09:31] 小节
[09:32] 首先第一个事
[09:34] Spring boot在创建项目的时候
[09:36] 使用炸的打包方式
[09:38] 这个地方要注意啊
[09:39] 使用炸的打包方式
[09:40] 你看我们在我们的PoM文件里边
[09:43] 有没有去指定打包方式啊
[09:45] 是不是没有啊
[09:46] 在之前其实我们创建web项目的时候
[09:49] 这个地方是不是都需要用package
[09:51] 指定他的WAR的打包方式
[09:53] 而Spring boot并没有
[09:54] 它是炸的打包方式
[09:56] 因为呢
[09:57] 它是通过这个MEM方法来启动的
[10:00] 跟我们之前的MEM方法一样
[10:00] 跟我们之前稍微有一点差距
[10:02] 第二个Spring boot的引导类是项目的入口
[10:07] 运行MEM方法就可以启动项目了
[10:09] 刚才我们也看到了这个引导类
[10:12] 其实就是那么一行代码啊
[10:14] 然后接下来使用Spring boot和Spring构建项目
[10:18] 业务代码编写方式完全一样
[10:21] 刚才我们写Control2
[10:22] 和我们之前使用Spring来构建项目的时候写的Control2
[10:26] 是不是一模一样的
[10:27] 没有什么区别啊
[10:28] 它唯一的区别就在于
[10:29] 我们引入坐标那块稍微有点区别
[10:32] 然后那个引导类稍微有点区别
[10:34] 其实这些呢都非常的简单
[10:36] OK
[10:37] 对于Spring boot的快速入门
[10:39] 我们就详细完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 IntelliJ IDEA 创建一个 Spring Boot 项目，配置 pom.xml 文件，编写控制器和主类，并启动应用访问 HTTP 接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 标题页，显示“Spring Boot 快速入门”，下方列出“案例：需求”和“案例：实现步骤”。
画面 2: IntelliJ IDEA 中打开的 pom.xml 文件，内容为一个基础的 Maven 项目配置，包含 <groupId>、<artifactId> 和 <version>。
画面 3: 浏览器中打开的 Spring 官方文档页面，展示了一个包含 <parent> 和 <dependencies> 的 pom.xml 示例，其中 <parent> 的 <groupId> 为 org.springframework.boot。
画面 4: 浏览器中 Spring 官方文档页面，展示 <dependencies> 和 <build> 部分，其中 <dependency> 的 <groupId> 为 org.springframework.boot。
画面 5: IntelliJ IDEA 中的 pom.xml 文件，光标位于 <dependencies> 标签内，准备添加依赖。
画面 6: IntelliJ IDEA 中打开的 HelloController.java 文件，光标位于 package com.ithema; 后，准备编写代码。
画面 7: IntelliJ IDEA 中的 HelloController.java 文件，已导入 org.springframework.web.bind.annotation.RequestMapping 和 @RestController 注解。
画面 8: IntelliJ IDEA 中右键点击 HelloController.java，弹出菜单，选择“Run HelloController”。
画面 9: IntelliJ IDEA 中打开的 HelloApplication.java 文件，内容为 Spring Boot 项目的主类，包含 @SpringBootApplication 注解和 main 方法。
画面 10: IntelliJ IDEA 中，点击“Run”按钮，弹出“Run: HelloApplication”对话框。
画面 11: IntelliJ IDEA 中，控制台显示 Spring Boot 应用启动日志，包括 Tomcat 初始化和启动成功信息。
画面 12: 浏览器地址栏输入 localhost，准备访问应用。
画面 13: IntelliJ IDEA 中，控制台显示 Spring Boot 应用已启动，Tomcat 在 8080 端口启动成功。
画面 14: PPT 标题页，显示“小结”，内容为“Spring Boot在创建项目时，使用jar的打包方式。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.ithema</groupId>
    <artifactId>Spring Boot-helloworld</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>myproject</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <!-- Inherit defaults from Spring Boot -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.8.RELEASE</version>
    </parent>
    <!-- Add typical dependencies for a web application -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
    <!-- Package as an executable jar -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.ithema</groupId>
    <artifactId>Spring Boot-helloworld</artifactId>
    <version>1.0-SNAPSHOT</version>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.8.RELEASE</version>
    </parent>
    <dependencies>
        <!-- 添加起步依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面 7:
```java
package com.ithema;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
```

画面 9:
```java
package com.ithema;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloApplication {
    public static void main(String[] args) {
        SpringApplication.run(HelloApplication.class, args);
    }
}
```

画面 13:
```java
package com.ithema.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @RequestMapping("/hello")
    public String hello() {
        return "hello spring Boot !";
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题“Spring Boot 快速入门”，下方两个要点：“案例：需求”和“案例：实现步骤”。
画面 14: PPT 标题“小结”，下方一个要点：“Spring Boot在创建项目时，使用jar的打包方式。”

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

