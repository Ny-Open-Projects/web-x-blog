# 画面线理解：17.日志规范之slf4j整合JDK14以及Simple的使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\17.日志规范之slf4j整合JDK14以及Simple的使用【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:53, 01:24, 01:42, 01:56, 03:05, 03:42, 04:13, 04:33, 04:47, 05:34, 06:13, 06:34, 07:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:11:22

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
