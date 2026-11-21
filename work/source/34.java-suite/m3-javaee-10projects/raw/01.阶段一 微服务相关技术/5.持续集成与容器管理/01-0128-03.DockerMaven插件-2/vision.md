# 画面线理解：03.DockerMaven插件-2

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\03.DockerMaven插件-2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:34, 00:46, 00:49, 00:54, 03:56, 04:18, 04:23, 04:39, 04:54, 05:11, 05:19, 05:40, 05:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:16:46

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置 Maven 项目以使用 Docker Maven 插件，构建并推送镜像到本地 Docker Registry，并通过浏览器访问服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 IntelliJ IDEA 中 `pom.xml` 文件内容，包含 Spring Boot 和 Docker Maven 插件依赖。
画面2：展示 `pom.xml` 中 Docker Maven 插件的 `<configuration>` 部分，配置了镜像名、基础镜像和入口点。
画面3：切换到 IntelliJ IDEA 的欢迎界面。
画面4：打开 Windows 命令提示符。
画面5：在 IntelliJ IDEA 的终端中，显示了 Maven 构建命令的执行状态。
画面6：在 SecureCRT 中执行 `docker images` 命令，列出本地镜像。
画面7：在浏览器中访问 `http://192.168.184.141:5000/v2/`，显示服务列表。
画面8：在浏览器中访问 `http://192.168.184.141:5000/v2/catalog`，显示服务目录。
画面9：在 Typora 文档中，展示 Docker 镜像列表和 `docker run` 命令。
画面10：在 Typora 文档中，展示“持续集成工具-Jenkins”章节标题。
画面11：在 IntelliJ IDEA 中，执行 Maven 构建命令，终端显示构建完成。
画面12：在 SecureCRT 中，执行 `docker images` 命令，列出本地镜像。
画面13：在 SecureCRT 中，执行 `docker run -d --name=base -p 9001:9001 192.168.184.141:5000/tenquare_base:1.0-SNAPSHOT` 命令，启动容器。
画面14：在 Typora 文档中，展示“持续集成工具-Jenkins”章节标题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.tensquare</groupId>
    <artifactId>tenquare_base</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.47</version>
        </dependency>
        <dependency>
            <groupId>com.tensquare</groupId>
            <artifactId>tenquare_base</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>com.spotify</groupId>
                <artifactId>docker-maven-plugin</artifactId>
                <version>0.4.13</version>
                <configuration>
                    <imageName>192.168.184.141:5000/${project.artifactId}:${project.version}</imageName>
                    <baseImage>jdk1.8</baseImage>
                    <entryPoint>["java", "-jar", "${project.build.finalName}.jar"]</entryPoint>
                    <resources>
                        <resource>
                            <targetPath>/</targetPath>
                            <directory>${project.build.directory}</directory>
                            <includes>
                                <include>${project.build.finalName}.jar</include>
                            </includes>
                        </resource>
                    </resources>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

画面2：
```xml
<plugin>
    <groupId>com.spotify</groupId>
    <artifactId>docker-maven-plugin</artifactId>
    <version>0.4.13</version>
    <configuration>
        <imageName>192.168.184.141:5000/${project.artifactId}:${project.version}</imageName>
        <baseImage>jdk1.8</baseImage>
        <entryPoint>["java", "-jar", "${project.build.finalName}.jar"]</entryPoint>
        <resources>
            <resource>
                <targetPath>/</targetPath>
                <directory>${project.build.directory}</directory>
                <includes>
                    <include>${project.build.finalName}.jar</include>
                </includes>
            </resource>
        </resources>
    </configuration>
</plugin>
```

画面5：
```bash
[INFO] --- maven-jar-plugin:3.2.0:jar (default-jar) @ tenquare_base ---
[INFO] Building jar: D:\code\blog\tensquare_parent\tensquare_base\target\tensquare_base-1.0-SNAPSHOT.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 7.381 s
[INFO] Finished at: 2018-03-03T21:39:24+08:00
[INFO] Final Memory: 20M/21M
[INFO] ------------------------------------------------------------------------
```

画面6：
```bash
[root@localhost ~]# docker images
REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
192.168.184.141:5000/tenquare_base        1.0-SNAPSHOT        2f21e7cfcac6        23 seconds ago      617MB
192.168.184.141:5000/jdk1.8                latest              4b0fa8b87a03f        16 hours ago        587MB
mysql                                     5.7.22              77e4727a673b        20 hours ago        322MB
centos                                    latest              7f04f8722298        10 days ago         44MB
```

画面9：
```bash
输出加上内容，表示服务已经集成成功
(7) 启动容器：
docker run -d --name=base -p 9001:9001 192.168.184.141:5000/tenquare_base:1.0-SNAPSHOT
```

画面13：
```bash
[root@localhost ~]# docker run -d --name=base -p 9001:9001 192.168.184.141:5000/tenquare_base:1.0-SNAPSHOT
7f04f8722298
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面9：PPT标题为“微服务访问 http://192.168.184.141:5000/v2/catalog，输出”，表格数据为：
| REPOSITORY | TAG | IMAGE ID | CREATED |
| --- | --- | --- | --- |
| 192.168.184.141:5000/tenquare_base | 1.0-SNAPSHOT | 83e6a04478c | 10 minutes ago |
| 192.168.184.141:5000/jdk1.8 | latest | 507438a0158f | 6 hours ago |

画面14：PPT标题为“2 持续集成工具-Jenkins”，子标题为“2.1 什么是持续集成”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
