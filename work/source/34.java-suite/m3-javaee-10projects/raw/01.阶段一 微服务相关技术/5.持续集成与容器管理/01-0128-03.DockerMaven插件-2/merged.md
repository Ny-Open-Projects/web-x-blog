# 03.DockerMaven插件-2

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\03.DockerMaven插件-2_【海量资源尽在 666java.com】.mp4
- 时长 5分52秒（音频 353s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才我们已经完成了我们 Maven 插件的一个配置那么接下来咱们就来使用 Maven 命令来调用插件实现我们说这个 Docker 镜像的一个创建与上传那么如何实现 Docker 的镜像的上传这个时候我们就需要在我们的 id 中打开我们的命令行窗口如何打开大家看一下
[00:31] 这个左下角有个timinal点开之后大家会看到一个命令行窗口对吧哎这个呢其实就是这个IDR自带的一个命令行窗口当然我们直接另外再打开这个cmd啊cmd然后呢在命令行方式进入到这个目录下也是可以的啊这两个方式都可以达到相同的效果那么我们在这个命令行下就可以输入mail命令啊来这个
[01:00] 来实现对这个Maven的这个对Maven工程的一个各种生物周期这种命令的一个调用那比如说我们现在当前的目录就是在paren下比如我们现在输入mvn install那么这条命令执行之后这时候就把整个这个工程下的所有的子工程进行什么进行一个安装安装到本地仓库了当然包括其中包括了这个ten square
[01:34] common这个工程这工程实际上是什么呢是我们整个这个微服务的一个通用的一个小模块那么这里主要包括的是一些通用的事业类以及我们的工具类我们先把它安装本地仓库因为接下来我们这样进行打包的话其实他要去什么去到本地仓库去找这个东西那么我们现在把整个的工程都安装之后接下来我们就要实现什么呢实现对这个这个base这个工程
[02:03] 对base这工程进行什么进行这个Dark镜像的一个创建那么怎么样才能到当前的到这个base这一级呢我们可以在这去打CD然后接下来就是这个工程名称当然说我们也可以有更简洁的方法比如说我们现在可以这样把这个鼠标点中这个工程然后怎么呢拖向这个窗口
[02:34] 这时候大家看一下这个窗口是不是多了一个选项卡并且当前的目录是在这个ten square 这一级目录那么我们现在就可以去操作这个工程了在这一级目录操作这个工程怎么办呢m1然后这个命令就是我们的Docker build build就表示什么呢表示这个Docker插件中的一个构建的这么一个命令这个其实就是在我们刚才配置信息里我们刚才配置信息里这个里头提供的这么一个类
[03:07] 来实现这么一个命令那么如果说我们不光要创建这个镜像我们还要去上传这时候我们要加上这个参数加什么参数呢-D注意D大写然后呢Push注意是连着的中间没有空格的Push Image注意大小写Di是大写的好我们现在回车好现在正在创建这个镜像然后呢它可以上传很快这个就传完了
[03:39] 大家看到这个build success表示是我们已经完成这个操作了那么完成这个操作之后接下来咱们再看一下我们的这个这个速度机上这个镜像到底有没有大家看一下现在是不是多了一个镜像啊10 square 杠 base然后呢版本是1.0啊快照吧这样一个啊这个镜像就创建好了那当然这个地方有不代表说私有仓库里就有对吧
[04:12] 所以我们还得打开我们的私有仓库来查看一下,冒号5000v2,大家看一下是不是这个时候我们也可以在这个链网上看到这个这个这个ten square ground base这个微服务已经创建出来了对不对所以说这就是我们通过这个maven Docker maven的插件来实现什么呢来实现我们微服务的一个部署我们就讲解到这里
[04:45] 那么当然说这个微服务能不能启动创建容器呢很简单我们试一下就行了我们接下来来输这个命令来这个试一下看到底能不能成功Docker run-di然后-name等于base这是我们起个名然后-p9001冒号9001比如说我们这个端口是9001因为我们说在这工程里我们可以看一眼这个工程呢
[05:15] 我让他启动的端口就是901所以说我们在这里把901映射的901那么接下来我们再输入我们的镜像的名称对吧这个镜像名称然后接下来就是帽号接下来就是我们的这个targ好我回车好现在我们快看这个容器是不是就已经创建出来了我们现在一看这个容器已经创建成功了好这就是我们说的
[05:45] 整个的这个Docker没人插件的一个使用咱们就讲解到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置 Maven 项目以使用 Docker Maven 插件，构建并推送镜像到本地 Docker Registry，并通过浏览器访问服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 IntelliJ IDEA 中 `pom.xml` 文件内容，包含 Spring Boot 和 Docker Maven 插件依赖。
画面2：展示 `pom.xml` 中 Docker Maven 插件的 `<configuration>` 部分，配置了镜像名、基础镜像和入口点。
画面3：切换到 IntelliJ IDEA 的欢迎界面。
画面4：打开 Windows 命令提示符。
画面5：在 IntelliJ IDEA 的终端中，显示了 Maven 构建命令的执行状态。
画面6：在 SecureCRT 中执行 `Docker images` 命令，列出本地镜像。
画面7：在浏览器中访问 `http://192.168.184.141:5000/v2/`，显示服务列表。
画面8：在浏览器中访问 `http://192.168.184.141:5000/v2/catalog`，显示服务目录。
画面9：在 Typora 文档中，展示 Docker 镜像列表和 `Docker run` 命令。
画面10：在 Typora 文档中，展示“持续集成工具-Jenkins”章节标题。
画面11：在 IntelliJ IDEA 中，执行 Maven 构建命令，终端显示构建完成。
画面12：在 SecureCRT 中，执行 `Docker images` 命令，列出本地镜像。
画面13：在 SecureCRT 中，执行 `Docker run -d --name=base -p 9001:9001 192.168.184.141:5000/tenquare_base:1.0-SNAPSHOT` 命令，启动容器。
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
                <artifactId>Docker-maven-plugin</artifactId>
                <version>0.4.13</version>
                <configuration>
                    <imageName>192.168.184.141:5000/${project.artifactId}:${project.version}</imageName>
                    <baseImage>JDK 8</baseImage>
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
    <artifactId>Docker-maven-plugin</artifactId>
    <version>0.4.13</version>
    <configuration>
        <imageName>192.168.184.141:5000/${project.artifactId}:${project.version}</imageName>
        <baseImage>JDK 8</baseImage>
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
[root@localhost ~]# Docker images
REPOSITORY                                 TAG                 IMAGE ID            CREATED             SIZE
192.168.184.141:5000/tenquare_base        1.0-SNAPSHOT        2f21e7cfcac6        23 seconds ago      617MB
192.168.184.141:5000/JDK 8                latest              4b0fa8b87a03f        16 hours ago        587MB
mysql                                     5.7.22              77e4727a673b        20 hours ago        322MB
centos                                    latest              7f04f8722298        10 days ago         44MB
```

画面9：
```bash
输出加上内容，表示服务已经集成成功
(7) 启动容器：
Docker run -d --name=base -p 9001:9001 192.168.184.141:5000/tenquare_base:1.0-SNAPSHOT
```

画面13：
```bash
[root@localhost ~]# Docker run -d --name=base -p 9001:9001 192.168.184.141:5000/tenquare_base:1.0-SNAPSHOT
7f04f8722298
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面9：PPT标题为“微服务访问 http://192.168.184.141:5000/v2/catalog，输出”，表格数据为：
| REPOSITORY | TAG | IMAGE ID | CREATED |
| --- | --- | --- | --- |
| 192.168.184.141:5000/tenquare_base | 1.0-SNAPSHOT | 83e6a04478c | 10 minutes ago |
| 192.168.184.141:5000/JDK 8 | latest | 507438a0158f | 6 hours ago |

画面14：PPT标题为“2 持续集成工具-Jenkins”，子标题为“2.1 什么是持续集成”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

