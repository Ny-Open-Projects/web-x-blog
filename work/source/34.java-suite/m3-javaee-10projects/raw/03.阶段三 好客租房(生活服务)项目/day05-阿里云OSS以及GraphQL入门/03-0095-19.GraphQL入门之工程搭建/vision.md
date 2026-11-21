# 画面线理解：19.GraphQL入门之工程搭建

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\19.GraphQL入门之工程搭建【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 01:09, 02:00, 02:58, 03:16, 04:01, 04:23, 04:43, 04:58, 05:26, 05:52, 06:11, 06:36, 07:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:01:13

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中创建一个 GraphQL Java 项目，并配置 Maven 依赖以解决 graphQL-java 包未发布到中央仓库的问题。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 Adobe Reader 中查看 PDF 讲义，显示“7.1.1、创建工程”章节，弹出的“New Project”对话框中填写了 GroupId: cn.itcast.graphql，ArtifactId: itcast-graphql-java，Version: 1.0-SNAPSHOT。
画面 2: 在 IntelliJ IDEA 中打开项目，显示 pom.xml 文件内容，其中包含 Maven 项目的基本配置。
画面 3: 在 Adobe Reader 中查看 PDF 讲义，显示“6.5. GraphQL的Schema和类型规范”章节，其中提到需要在 settings.xml 文件中配置第三方仓库。
画面 4: 在 Adobe Reader 中查看 PDF 讲义，显示“6.5. GraphQL的Schema和类型规范”章节，其中包含在 settings.xml 文件中配置 bintray 仓库的示例代码。
画面 5: 在 EditPlus 中打开 Maven 的 settings.xml 文件，显示 <mirrors> 部分的注释和结构。
画面 6: 在 EditPlus 中打开 Maven 的 settings.xml 文件，显示 <profiles> 部分的注释和结构。
画面 7: 在 EditPlus 中打开 Maven 的 settings.xml 文件，显示 <activeProfiles> 部分的配置，其中包含 <activeProfile>bintray</activeProfile>。
画面 8: 在 EditPlus 中打开 Maven 的 settings.xml 文件，显示 <profile> 部分的配置，其中包含 <repository> 和 <pluginRepository> 的 URL。
画面 9: 在 EditPlus 中打开 Maven 的 settings.xml 文件，显示 <activeProfiles> 部分的配置，其中包含 <activeProfile>bintray</activeProfile>。
画面 10: 在 Adobe Reader 中查看 PDF 讲义，显示在 settings.xml 文件中配置 bintray 仓库的示例代码。
画面 11: 在 IntelliJ IDEA 中打开项目，显示 pom.xml 文件中的 <dependencies> 部分，其中包含 graphQL-java 的依赖配置。
画面 12: 在 IntelliJ IDEA 中打开项目，显示 User.java 文件，准备编写 User 对象的实现。
画面 13: 在 Adobe Reader 中查看 PDF 讲义，显示“7.1.3、编写查询User对象实现”章节，其中包含 GraphQL Schema 的定义代码。
画面 14: 在 Adobe Reader 中查看 PDF 讲义，显示“导入依赖”部分，其中包含 graphQL-java 的依赖配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
GroupId: cn.itcast.graphql
ArtifactId: itcast-graphql-java
Version: 1.0-SNAPSHOT

画面 2:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.graphql</groupId>
    <artifactId>itcast-graphql-java</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>

画面 3:
<dependency>
    <groupId>com.graphql-java</groupId>
    <artifactId>graphql-java</artifactId>
    <version>11.0</version>
</dependency>

画面 4:
<profile>
    <id>bintray</id>
    <repositories>
        <repository>
            <id>bintray</id>
            <url>http://dl.bintray.com/andimarek/graphql-java</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>
    <pluginRepositories>
        <pluginRepository>
            <id>bintray</id>
            <url>http://dl.bintray.com/andimarek/graphql-java</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </pluginRepository>
    </pluginRepositories>
</profile>

画面 5:
<mirrors>
    <!-- mirror
    Specifies a repository mirror site to use instead of a given repository. The repository
    that this mirror serves has an ID that matches the mirrorOf element of this mirror. IDs are
    used in Inheritance and direct lookup purposes, and must be unique across the set of mirrors.
    -->
    <mirror>
        <id>mirrorId</id>
        <mirrorOf>repositoryId</mirrorOf>
        <name>Human Readable Name for this Mirror.</name>
        <url>http://my.repository.com/repo/path</url>
    </mirror>
</mirrors>

画面 6:
<profiles>
    <!-- This is a list of profiles which can be activated in a variety of ways, and which can
    modify the build process. Profiles provided in the settings.xml are intended to provide
    local machine-specific paths and repository locations which allow the build to work in the
    local environment.
    -->
    <!-- For example, if you have an integration testing plugin -- like cactus -- that needs to know
    where your Tomcat instance is installed, you can provide a variable such that the variable is
    dereferenced during the build process to configure the cactus plugin.
    -->
    <!-- As noted above, profiles can be activated in a variety of ways. One way -- the activeProfiles
    section of this document (settings.xml) -- will be discussed later. Another way essentially
    relies on the detection of a system property, either matching a particular value for the
    property, or merely testing its existence. Profiles can also be activated by JDK version prefix, where
    the value of '1.4' might activate a profile when the build is executed on a JDK version of
    '1.4.2_07'.
    -->
    <!-- Finally, the list of active profiles can be specified directly from the command line.
    NOTE: For profiles defined in the settings.xml, you are restricted to specifying only
    -->

画面 7:
<activeProfiles>
    <activeProfile>alwaysActiveProfile</activeProfile>
    <activeProfile>anotherAlwaysActiveProfile</activeProfile>
</activeProfiles>

画面 8:
<profile>
    <id>nexus</id>
    <repositories>
        <repository>
            <id>nexus</id>
            <url>http://127.0.0.1:8888/nexus/content/groups/public/</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
        </repository>
    </repositories>
    <pluginRepositories>
        <pluginRepository>
            <id>nexus</id>
            <url>http://127.0.0.1:8888/nexus/content/groups/public/</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
        </pluginRepository>
    </pluginRepositories>
</profile>

画面 9:
<activeProfiles>
    <activeProfile>alwaysActiveProfile</activeProfile>
    <activeProfile>anotherAlwaysActiveProfile</activeProfile>
</activeProfiles>

画面 10:
<profile>
    <id>bintray</id>
    <repositories>
        <repository>
            <id>bintray</id>
            <url>http://dl.bintray.com/andimarek/graphql-java</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>
    <pluginRepositories>
        <pluginRepository>
            <id>bintray</id>
            <url>http://dl.bintray.com/andimarek/graphql-java</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </pluginRepository>
    </pluginRepositories>
</profile>

画面 11:
<dependencies>
    <dependency>
        <groupId>com.graphql-java</groupId>
        <artifactId>graphql-java</artifactId>
        <version>11.0</version>
    </dependency>
</dependencies>

画面 12:
package cn.itcast.graphql.vo;
public class User {

画面 13:
type UserQuery {
    user: User
}

画面 14:
<dependency>
    <groupId>com.graphql-java</groupId>
    <artifactId>graphql-java</artifactId>
    <version>11.0</version>
</dependency>

4) 出现的 PPT 标题、架构图/流程图的
