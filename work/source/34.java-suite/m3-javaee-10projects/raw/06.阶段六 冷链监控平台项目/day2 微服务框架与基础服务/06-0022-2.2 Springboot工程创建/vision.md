# 画面线理解：2.2 Springboot工程创建

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.2 Springboot工程创建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 02:16, 04:47, 05:30, 06:16, 07:04, 07:37, 08:09, 08:39, 09:25, 09:57, 10:33, 11:01, 11:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:50:59

1) 这一组画面整体在讲如何使用 IntelliJ IDEA 创建 Spring Boot 项目，并通过 Spring Initializr 选择依赖项，最终导入并配置 Maven 项目结构。

2) 按时间顺序列出每张画面的要点：
画面1：打开 IntelliJ IDEA，准备创建新项目，左侧显示课程目录，右侧显示 Spring Boot 项目结构图。
画面2：在文件资源管理器中，显示“cold-project”文件夹，准备导入项目。
画面3：在 Spring Initializr 网站上，选择“Spring Session”和“Rest Repositories HAL Browser”依赖项。
画面4：在 Spring Initializr 网站上，展开“Security”分类，选择“Spring Security”和“OAuth2 Client”依赖项。
画面5：显示下载的“cold-common.zip”压缩包内容，其中包含 pom.xml 文件，内容如下：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.2.RELEASE</version>
        <relativePath/>
    </parent>
    <groupId>com.ithema</groupId>
    <artifactId>cold-common</artifactId>
    <version>1.0-SNAPSHOT</version>
    <name>cold-common</name>
    <description>公共组件库</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.apache.camel</groupId>
            <artifactId>camel-spring-boot-starter</artifactId>
            <version>3.0.0</version>
        </dependency>
    </dependencies>
</project>
画面6：在文件资源管理器中，显示“cold-project”和“cold-common.zip”两个文件。
画面7：在 IntelliJ IDEA 中，打开“Project Structure”对话框，设置源码目录和测试目录。
画面8：在 Spring Initializr 网站上，选择“Spring for Apache Kafka Streams”依赖项。
画面9：在浏览器中，搜索“mvnrepository”。
画面10：在 Maven Repository 网站上，搜索“Spring Boot Starter :: Camel :: Spring Boot”。
画面11：在 Maven Repository 网站上，搜索“springboot”，显示搜索结果。
画面12：在 IntelliJ IDEA 中，打开“cold-common”项目，显示 pom.xml 文件内容，其中“<version>3.0.0</version>”被选中。
画面13：在浏览器中，搜索“baidu.com”。
画面14：在 IntelliJ IDEA 中，显示“cold-common”项目的 pom.xml 文件，其中“<version>3.0.0</version>”被选中。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面5：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.2.RELEASE</version>
        <relativePath/>
    </parent>
    <groupId>com.ithema</groupId>
    <artifactId>cold-common</artifactId>
    <version>1.0-SNAPSHOT</version>
    <name>cold-common</name>
    <description>公共组件库</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.apache.camel</groupId>
            <artifactId>camel-spring-boot-starter</artifactId>
            <version>3.0.0</version>
        </dependency>
    </dependencies>
</project>

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：右侧显示服务注册中心、服务发现、定时任务等组件的架构图。
画面3：显示 Spring Initializr 网站的依赖项选择界面。
画面4：显示 Spring Initializr 网站的“Security”分类下的依赖项。
画面8：显示 Spring Initializr 网站的“Messaging”分类下的依赖项。
画面10：显示 Maven Repository 网站的“Spring Boot Starter :: Camel :: Spring Boot”页面。
画面11：显示 Maven Repository 网站的“springboot”搜索结果页面。

5) 无。
