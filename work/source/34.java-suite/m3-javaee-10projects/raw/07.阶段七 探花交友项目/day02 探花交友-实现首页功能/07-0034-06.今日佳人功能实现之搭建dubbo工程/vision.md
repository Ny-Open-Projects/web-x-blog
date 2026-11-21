# 画面线理解：06.今日佳人功能实现之搭建dubbo工程

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\06.今日佳人功能实现之搭建dubbo工程_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 01:52, 02:50, 03:16, 03:51, 04:08, 04:37, 05:34, 05:54, 06:14, 06:29, 06:45, 07:04, 07:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:21:07

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建 Dubbo 服务工程，并配置 Maven 依赖，包括接口、服务模块及所需组件（如 Spring Boot、Dubbo、Zookeeper、MongoDB 等）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 空白桌面，任务栏可见，无其他内容。
画面 2: 展示一个流程图，包含三个方框：“前端系统（apk）”、“后台系统，通过服务”、“服务系统”，并用箭头表示“前端系统（apk）”指向“后台系统，通过服务”。
画面 3: 显示 Typora 文档，标题为“2.3、搭建工程”，内容提到“系统采用Dubbo构建，首先开发的是dubbo服务工程”。同时，弹出“New Module”对话框，显示 Parent 为 “cn.ictanhuai.cast-tanhuai-1.0-SNAPSHOT”，ArtifactId 为 “cast-tanhuai-dubbo”，Version 为 “1.0-SNAPSHOT”。
画面 4: 显示 IntelliJ IDEA 中的“New Module”对话框，正在加载 archetype 列表，准备创建新模块。
画面 5: 显示 IntelliJ IDEA 中的 `my-tanhuai-dubbo` 模块的 `pom.xml` 文件内容，其中包含父模块配置：
```xml
<xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>my-tanhua</artifactId>
        <groupId>cn.ictanhuai</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-tanhua-dubbo</artifactId>
</project>
```
画面 6: 显示 IntelliJ IDEA 中的 `my-tanhuai-dubbo-interface` 模块的 `pom.xml` 文件内容，其中包含父模块配置：
```xml
<xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>my-tanhua-dubbo</artifactId>
        <groupId>cn.ictanhuai</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-tanhua-dubbo-interface</artifactId>
</project>
```
画面 7: 显示 IntelliJ IDEA 中的 `my-tanhuai-dubbo-service` 模块的 `pom.xml` 文件内容，其中包含父模块配置：
```xml
<xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>my-tanhua-dubbo</artifactId>
        <groupId>cn.ictanhuai</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-tanhua-dubbo-service</artifactId>
</project>
```
画面 8: 显示 IntelliJ IDEA 中的 `my-tanhuai-dubbo-interface` 模块的 `pom.xml` 文件内容，其中包含父模块配置：
```xml
<xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>my-tanhua-dubbo</artifactId>
        <groupId>cn.ictanhuai</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-tanhua-dubbo-interface</artifactId>
</project>
```
画面 9: 显示 IntelliJ IDEA 中的 `my-tanhuai-dubbo-interface` 模块的 `pom.xml` 文件内容，其中包含依赖部分：
```xml
<dependencies>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-mongodb</artifactId>
    </dependency>
</dependencies>
```
画面 10: 显示 Typora 文档，标题为“2.3、搭建工程”，内容提到“系统采用Dubbo构建，首先开发的是dubbo服务工程”。同时，显示 `pom.xml` 文件内容，其中包含依赖部分：
```xml
<dependencies>
    <dependency>
        <groupId>cn.ictanhuai</groupId>
        <artifactId>my-tanhua-dubbo-interface</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <!-- dubbo对springboot支持 -->
    <dependency>
        <groupId>com.alibaba.boot</groupId>
        <artifactId>dubbo-spring-boot-starter</artifactId>
        <version>0.2.0</version>
    </dependency>
    <!-- dubbo核心 -->
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>dubbo</artifactId>
        <version>2.6.4</version>
    </dependency>
    <!-- zk -->
    <dependency>
        <groupId>org.apache.zookeeper</groupId>
        <artifactId>zookeeper</artifactId>
        <version>3.4.13</version>
    </dependency>
    <!-- zkclient -->
    <dependency>
        <groupId>com.github.sgroschupf</groupId>
        <artifactId>zkclient</artifactId>
        <version>0.1</version>
    </dependency>
    <!-- mongodb -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-mongodb</artifactId>
    </dependency>
</dependencies>
```
画面 11: 显示 Typora 文档，标题为“2.3、搭建工程”，内容提到“系统采用Dubbo构建，首先开发的是dubbo服务工程”。同时，显示 `pom.xml` 文件内容，其中包含依赖部分：
```xml
<!-- dubbo对springboot支持 -->
<dependency>
    <groupId>com.alibaba.boot</groupId>
    <artifactId>dubbo-spring-boot-starter</artifactId>
    <version>0.2.0</version>
</dependency>
<!-- dubbo核心 -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dubbo</artifactId>
    <version>2.6.4</version>
</dependency>
<!-- zk -->
<dependency>
    <groupId>org.apache.zookeeper</groupId>
    <artifactId>zookeeper</artifactId>
    <version>3.4.13</version>
</dependency>
<!-- zkclient -->
<dependency>
    <groupId>com.github.sgroschupf</groupId>
    <artifactId>zkclient</artifactId>
    <version>0.1</version>
</dependency>
<!-- mongodb -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
```
画面 12: 显示 IntelliJ IDEA 中的 `my-tanhuai-dubbo-service` 模块的 `pom.xml` 文件内容，其中包含依赖部分：
```xml
<dependency>
    <groupId>com.alibaba.boot</groupId>
    <artifactId>dubbo-spring-boot-starter</artifactId>
    <version>0.2.0</version>
</dependency>
<!-- dubbo核心 -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dubbo</artifactId>
    <version>2.6.4</version>
</dependency>
<!-- zk -->
<dependency>
