# 画面线理解：08_项目搭建_原始项目结构介绍及导入

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\08_项目搭建_原始项目结构介绍及导入【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 03:17, 04:06, 04:58, 05:26, 05:45, 06:24, 06:35, 07:02, 07:22, 07:42, 08:27, 09:04, 09:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:29:33

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中导入并配置一个基于 Spring Boot 的多模块项目，重点讲解 pom.xml 文件的结构和依赖管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文件资源管理器中“day01”文件夹下的“图片”子文件夹，其中包含“4.png”和“weex打包图型.png”两个文件。
画面2：展示 Typora 编辑器中的 PPT 内容，标题为“5.2 后端通用工程搭建”，子标题“5.2.1 开发环境说明”，列出项目依赖的工具：IDK 1.8、IntelliJ IDEA、Tomcat 8.5、Git。
画面3：展示文件资源管理器中“day01”文件夹下的“图片”子文件夹，其中包含“4.png”和“weex打包图型.png”两个文件。
画面4：展示 Typora 编辑器中的 PPT 内容，标题为“5.2.3 后端初始项目导入”，说明需解压“heima-leadnews.zip”文件并使用 IDEA 打开。
画面5：展示 IntelliJ IDEA 的“Settings”窗口，路径为“Editor > File Encodings”，显示项目编码为 UTF-8。
画面6：展示 IntelliJ IDEA 的“Settings”窗口，路径为“Build, Execution, Deployment > Build Tools > Maven”，显示 Maven 配置，包括 Maven home directory 为 “D:\apache-maven-3.3.9”，User settings file 为 “D:\apache-maven-3.3.9\conf\settings.xml”，Local repository 为 “D:\apache-maven-3.3.9\repository\heima-leadnews”。
画面7：展示 IntelliJ IDEA 的项目结构，项目名为“heima-leadnews”，包含多个模块，当前选中“pom.xml”。
画面8：展示 IntelliJ IDEA 中打开的“pom.xml”文件，内容为 Spring Boot 项目父级配置，包含版本号“2.1.6 RELEASE”和编码配置“UTF-8”。
画面9：展示 IntelliJ IDEA 中打开的“pom.xml”文件，内容为依赖管理部分，包含 Spring Boot 的日志依赖“spring-boot-starter-log4j2”。
画面10：展示 IntelliJ IDEA 中打开的“pom.xml”文件，内容为排除默认日志依赖的配置，排除了“spring-boot-starter-logging”和“slf4j”。
画面11：展示 IntelliJ IDEA 中打开的“pom.xml”文件，内容为 Maven 插件配置，插件为“maven-compiler-plugin”，版本为“3.7.0”，配置了源码和目标版本。
画面12：展示 IntelliJ IDEA 中打开的“pom.xml”文件，内容为 Maven 插件配置，插件为“maven-compiler-plugin”，版本为“3.7.0”，配置了源码和目标版本。
画面13：展示 IntelliJ IDEA 中打开的“pom.xml”文件，内容为 Maven 插件配置，插件为“maven-compiler-plugin”，版本为“3.7.0”，配置了源码和目标版本。
画面14：展示 IntelliJ IDEA 中打开的“pom.xml”文件，内容为 Maven 插件配置，插件为“maven-compiler-plugin”，版本为“3.7.0”，配置了源码和目标版本。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面8：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.6.RELEASE</version>
        <relativePath/>
    </parent>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
    </properties>
```

画面9：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-log4j2</artifactId>
    </dependency>
</dependencies>
```

画面10：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-logging</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

画面11：
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.7.0</version>
    <configuration>
        <source>${java.version}</source>
        <target>${java.version}</target>
    </configuration>
</plugin>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT 标题为“5.2 后端通用工程搭建”，子标题“5.2.1 开发环境说明”，列出项目依赖的工具：IDK 1.8、IntelliJ IDEA、Tomcat 8.5、Git。
画面4：PPT 标题为“5.2.3 后端初始项目导入”，说明需解压“heima-leadnews.zip”文件并使用 IDEA 打开。
画面6：PPT 标题为“5.2.3 后端初始项目导入”，说明需解压“heima-leadnews.zip”文件并使用 IDEA 打开。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
