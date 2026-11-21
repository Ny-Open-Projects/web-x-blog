# 画面线理解：11-工程搭建：搭建父工程

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\11-工程搭建：搭建父工程_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 00:41, 01:50, 01:58, 02:16, 02:27, 02:50, 03:28, 03:37, 03:46, 04:10, 04:27, 04:48, 05:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:55:05

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中导入并查看一个 Spring Boot 项目的父 POM 文件（pom.xml），并重点展示其中的依赖管理、插件配置和仓库设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Windows 开始菜单，选中 IntelliJ IDEA 2017.3.2 启动程序，背景为一个包含项目描述的文档。
画面 2: IntelliJ IDEA 启动后，显示“Welcome to IntelliJ IDEA”窗口，鼠标悬停在“Import Project”选项上，左侧是项目结构大纲。
画面 3: 鼠标点击“Import Project”选项，准备导入项目。
画面 4: 项目导入完成，显示 `pom.xml` 文件内容，弹出“Tip of the Day”提示框，提示快捷键 Ctrl+Alt+Shift+L 可以格式化代码。
画面 5: 点击菜单栏的“File” -> “New” -> “Project”，准备新建项目。
画面 6: 项目结构视图中显示“External Libraries”，鼠标悬停在“ihm_parent”项目上。
画面 7: 项目结构视图中选中“ihm_parent”项目，准备查看其内容。
画面 8: 黑马程序员和博学谷的加载界面。
画面 9: Notepad++ 编辑器中显示 `ihm/day/pom.xml` 文件内容，重点高亮了 `org.projectlombok` 依赖。
画面 10: IntelliJ IDEA 中打开 `pom.xml` 文件，光标位于 `<plugins>` 标签内，准备编辑插件配置。
画面 11: `pom.xml` 文件内容，高亮显示 `<description>黑马程序员</description>`。
画面 12: `pom.xml` 文件内容，高亮显示 `<dependency>` 标签，其中包含 `spring-boot-starter-web` 依赖。
画面 13: `pom.xml` 文件内容，高亮显示 `<dependency>` 标签，其中包含 `org.projectlombok` 依赖。
画面 14: `pom.xml` 文件内容，光标位于 `<repositories>` 标签内，准备编辑仓库配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ihm</groupId>
    <artifactId>ihm_parent</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

画面 9:
```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.16.16</version>
</dependency>
```

画面 10:
```xml
<pluginRepositories>
    <pluginRepository>
        <id>spring-milestones</id>
        <name>Spring Milestones</name>
        <url>https://repo.spring.io/milestone</url>
        <snapshots>
            <enabled>false</enabled>
        </snapshots>
    </pluginRepository>
</pluginRepositories>
<plugins>
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.1</version>
        <configuration>
            <source>${java.version}</source>
            <target>${java.version}</target>
        </configuration>
    </plugin>
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>2.1.7</version>
        <configuration>
            <skipTests>true</skipTests>
        </configuration>
    </plugin>
</plugins>
```

画面 11:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ihm</groupId>
    <artifactId>ihm_parent</artifactId>
    <version>1.0-SNAPSHOT</version>
    <description>黑马程序员</description>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.5.RELEASE</version>
        <relativePath/>
    </parent>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
        <fastjson.version>1.2.47</fastjson.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-logging</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>${fastjson.version}</version>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.16.16</version>
        </dependency>
    </dependencies>

    <repositories>
        <repository>
            <id>spring-snapshots</id>
            <name>Spring Snapshots</name>
            <url>https://repo.spring.io/snapshot</url>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
        </repository>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
