# 17.日志规范之slf4j整合JDK14以及Simple的使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\17.日志规范之slf4j整合JDK14以及Simple的使用【海量资源尽在 ubkz.com】.mp4
- 时长 8分8秒（音频 488s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来讲一下Sullivan4j的一个具体的使用那么首先呢我们需要创建一个工程去做一个使用那么下面呢我们在ID里面呢去创建我们的一个新的工程那么我们这个工程的名字呢就叫itcast这个Sullivan4j那么先写这个artifact id那么就叫itcast然后呢Sullivan4j然后呢我们这个国牌id呢就叫cn.itcast
[00:30] 点什么呢就叫沙拉芬吧然后呢我们把这个呢artifact id呢拷贝一下然后呢去粘贴一下然后呢走那么这功能呢基本上就创建好了那么创建好之后呢我们需要去在我们这个里面是不是写一些具体的依赖啊那么先去把这个呢先导入进来就是我们启用一个自动的一个导入啊导入功能OK好然后呢我们来看一下
[00:56] 那么下面我们需要导入一个依赖那么就导入这个Salaven4j的依赖那么它的依赖呢国牌ID叫做org-salaven4j那么这个artifact ID是salaven4j-api这样的一个依赖那么版本是1.7.26这个版本OK那么把它导入进来那么我们就写到这吧OK好嘞好那么接下来我们就可以去编写我们的具体代码了我们来看一下检查一下有没有去导入进来
[01:26] 发现它已经导进来了OK没有问题那么下面我们来编写代码那么代码我们写到这个位置来对吧那么我们来看代码代码比较简单那么我先创建一个包那么我们应该先创建的是一个就这个包把这个包先创建出来然后我们再去编写这个类那么这个类我们就是写一个demo这个类这个类非常简单那我们就直接来拷贝
[01:54] 这个类把它拷贝到这个里面来我们来看一下这个类中的一些内容那么在这个里面呢我们其实可以看到我们写了一个非常简单的一个这个demo啊然后呢在这个demo中呢我们有一个这个man方法啊然后呢我们在这个里面首先呢执行我们的这个man方法第一句呢我们就去打印一个日志这个日志对象呢是这个logger这个对象调用他的info去打印一个info级别的这样的一个日志
[02:20] 然后我们其实可以看到这个logger是通过这个什么的logger factory然后get a logger去拿到的这样一个logger对象而这个logger factory它的来源其实是我们这个salafan4j中的一个类而并不是我们具体的这个logger4j里面的这样的一个类那么拿到的是它那么我们来回顾一下前面我们所说到的我们的一个手册在这个阿里巴巴这个手册中
[02:49] 他是不是告诉我们说应该是这样去应该是这样去写我们的一个引用我们的一个这个log这个对象对吧通过一个log factory去做引用这个log factory呢就是我们这个Sarafn4J中的这个APIOK那么推荐这样去写那么我们也是这样去写然后呢我们在这个位置呢去打印一句话其实就在模拟我们正常的这个代码的编写然后下面这个呢就是去输出一个错误的一个日志依然使用的是这个对象
[03:18] 去做一个输出哎OK好嘞好那么这个呢是一个非常简单的个代码但是要注意的是现在呢我们只是写了一个这样的个代码也使用了一下这个Sarafn但是呢我们并不能够去输出日志因为什么呢我们前面说过这个Sarafn4j呢他呢并不是一个具体的一个日志的一个实现的框架那么他还需要去整合一些其他的日志框架才能够完成所以下面呢我们就需要
[03:44] 去不断的去整合整合多个这个日子框架去做一个这个编写那么首先第一个呢我们来看一下整合的是这个JDK14这个框架这个是原生的一个框架那么怎么样去整合呢我们只需要在我们的依赖中导入一个这个Sarafn4J-JDK14这个包那么就可以了这个版本跟我们的这个Sarafn4J API的版本的保持一致都是这个1.7.26来看一下
[04:12] 那么都是这个版本那么我们就把这个JDK14这个依赖呢也拷贝一下然后呢我们往这里一丢OK那么这样的话呢我们看检查一下依赖那么这个是不是还没导入进来啊刷一下那么是不是导入进来呢就会有一个JDK14叫哪个依赖那么接下来呢我们就可以去运行我们代码了要注意啊要注意观察那么我们走运行那么这个时候呢它就会调用什么呢
[04:39] 调用我们的JDK14的这个具体的一个时线然后呢把我们的这个日志呢打印出来那么可以看到呢是这样的一个日志那么前面的这个是不是就是我们这个日志对吧然后后面这个是不是也是这样的一个日志啊哎OK好那么这个时候呢我们要注意的是那么这个日志我们是调用的是我们的这个JDK14去打印出来的这样的一个这样的一个日志那么我们在
[05:07] 这个位置所引用的呢是谁呢是这个Sarafen里面的API那么我们引用的是它但是真正底层去执行的是不是还是我们这个JDK14的这个包呀OK所以说它只是一个什么呢门面或者说只是一个门面这种模式去做一个实现那么真正底层干活的并不是它还是我们需要去整合具体的一些日志框架那么OK好这个呢就是我们整合了JDK14的一个这样的一个这个演示啊
[05:37] 好那么接下来呢我们就来整合一下这个simple这个框架那么它呢和我们JDK14一样也是一个日制框架啊那么我们如果我们底层呢想使用这个simple这个具体的一个实现的话那我们就需要去导入在那个依赖就可以了就是这个salafin4j-simple这个依赖就可以了哎OK下面呢我们就来去测试一下那我们把这个依赖呢拷贝一下然后呢进入到我们这个pub文件中要注意的是要把之前的这个去掉
[06:07] 去掉或者是把它注射掉那么都可以那么我就把它注射掉然后往这一call那么我们来检查一下我们这个依赖那么刷一下那么它就变成这个sample了那么然后我们去做一个执行那么要注意的是我们代码不做任何的修改注意不做任何的修改我们依然还是使用Salaven4J它的一个API去做一个使用我们点击右键走运行那么来看一下
[06:33] 那么运行的结果呢我们来等待它的一个执行那么OK那么运行的结果是不是就是这样的一个结果呀那么就是可以看到这个日志打印的一个格式啊跟我们之前的所看到的这个JDK14中的这个日志格式是不一样的那就说明我们在底层真正的日志呢已经就使用到了什么这个simple这个框架OK那么在这我们需要强调的一点是
[07:00] 那么我们的这个代码呢并没有做任何的修改注意代码是并没有做任何的修改啊那我们底层的日志呢就使用了谁使用了这个sample那么这个其实就是salafun4j它的一个好处那么我们在使用它之后呢那我们底层的这个具体实现那么想要做变更的时候就会变得非常的容易那么只需要去引入它的一些这个具体这个包是不是就可以了那么代码不需要做任何的修改那么这个呢就是我们之前在
[07:29] 说的时候就说如果我们选用了一个日志框架那么以后我想再去换一个其他的日志框架的话那么我代码的一个修改的程度到底有多少那么如果你使用的是一个Salaven4J API的话那么你的代码是不需要做任何修改的OK那么没有任何修改那么就可以实现一个日志框架的变更OK
[07:55] 好那么我们呢以这两个为例是不是给大家做了一个演示啊哎OK好那么关于这个Sarapen4J的一个基本使用呢我们就先讲到这里那么关于其他框架的一个整合呢我们后面再讲哎OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建一个 Maven 项目，集成 SLF4J 日志框架，并分别与 JDK14、Simple、Log4j 等日志实现进行整合，展示日志输出效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：创建新项目，设置 GroupId 为 cn.itcast.slf4j，ArtifactId 为 itcast-slf4j，Version 为 1.0-SNAPSHOT。
画面 2：打开 pom.xml 文件，显示项目的基本 Maven 配置，包括 modelVersion、groupId、artifactId 和 version。
画面 3：在 pom.xml 中添加 <dependencies> 标签，准备引入 SLF4J 的 API 依赖。
画面 4：展示编写日志代码的步骤，包括导入 SLF4J 包、创建 Logger 实例、使用 info 和 error 方法输出日志。
画面 5：在 IntelliJ IDEA 中打开 Demo.java 文件，准备编写日志代码。
画面 6：展示《阿里巴巴 Java 开发手册》中关于日志规范的内容，包括禁止直接使用 Log4j/Logback API、日志文件至少保存 15 天、日志文件命名规范等。
画面 7：在 Typora 文档中展示与 JDK14 整合的依赖配置。
画面 8：在 Typora 文档中展示与 JDK14 整合的依赖配置，与画面 7 内容相同。
画面 9：在 IntelliJ IDEA 中展示完整的 Demo.java 代码，包含 SLF4J 的导入、Logger 实例创建和 info/error 日志输出。
画面 10：在 IntelliJ IDEA 中运行 Demo.java，终端显示日志输出结果，包含 info 和 error 信息。
画面 11：在 Typora 文档中展示与 Simple 整合的依赖配置。
画面 12：在 IntelliJ IDEA 中展示 pom.xml 文件，添加了 SLF4J-simple 依赖。
画面 13：在 IntelliJ IDEA 中运行 Demo.java，终端显示日志输出结果，包含 info 和 error 信息。
画面 14：在 Typora 文档中展示与 Log4j 整合的依赖配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
GroupId: cn.itcast.slf4j
ArtifactId: itcast-slf4j
Version: 1.0-SNAPSHOT

画面 2：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.slf4j</groupId>
    <artifactId>itcast-slf4j</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>

画面 3：
<dependencies>
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-api</artifactId>
        <version>1.7.26</version>
    </dependency>
</dependencies>

画面 4：
System.out.println("测试代码");
LOGGER.info("这是info日志信息，代码之前进行打印信息。");
LOGGER.error("这是error日志信息，代码之后进行打印信息。");

画面 7：
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>1.7.26</version>
</dependency>

画面 11：
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-simple</artifactId>
    <version>1.7.26</version>
</dependency>

画面 14：
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
    <version>1.7.26</version>
</dependency>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6：PPT 标题为“（二）日志规约”，内容包括三条强制性规定：
1. 【强制】应用中不可直接使用日志系统（Log4j、Logback）中的 API，而应依赖使用日志框架 SLF4J 中的 API，使用门面模式的日志框架，有利于维护和各个类的日志处理方式统一。
2. 【强制】日志文件保存至少保存 15 天，因为有些异常具备以“周”为频次发生的特点。
3. 【强制】应用中的扩展日志（如打点、临时监控、访问日志等）命名方式：appName_logType_logName.log。logType:日志类型，推荐分类有 stats/dest/monitor/visit 等；logName:日志描述。这种命名的好处：通过文件名就可知日志文件属于什么应用，什么类型，什么目的，也有利于归类查找。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

