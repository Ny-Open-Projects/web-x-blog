# 19.GraphQL入门之工程搭建

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\19.GraphQL入门之工程搭建【海量资源尽在 ubkz.com】.mp4
- 时长 7分3秒（音频 423s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们就正式来使用这个WebQL Java这个工程啊来去看一下它具体的一些这个用法那么如何去通过这个工具包然后来实现我们WebQL的这样的一个接口的一些定义啊好,那么下面我们首先来创建工程啊那么创建工程呢,就叫itcast webql-java由于我这个位置呢,它已经有这个工程了所以呢,我名字呢就会起的有点不太一样啊大家注意一下,那么
[00:28] 国牌D呢我们就叫cn.itcast.grepql对吧hql啊有个h啊别别把这个h丢掉啊然后呢写一个itcast-什么呢grepql然后呢-java-2啊呃我就后面加一个2吧这样的一个工程名OK那么我们点击这个下一步啊然后呢到这然后呢点击这个finish完成
[00:56] 那么我这个工程呢就创建好了我在新的窗口中把它打开那么打开之后啊打开之后呢我们首先呢要需要给它去导入这个依赖啊把这个依赖导入进来就是webql-java这个依赖那么咱们把它放到这儿放到这里来然后呢我们来看一下它有没有去导入相关的依赖呢并没有那就说明我们那个enable auto input没有打开开启一下
[01:25] 那么这个时候他就会去自动导入这个依赖看到没有是不是已经导进来了OK那么在这个点呢特别要给大家去强调一下啊就是GrabQL这个杠加了这个工程啊他的这个包呢并没有啊并没有发布到我们的这个MEMO的那个中央仓库里面去所以说如果你不做一些额外的一些配置那么你这样直接去写的话那么他是找不到啊下载不到这个加包的啊那么需要怎么样的个设置呢是这样的
[01:55] 我们需要给他配置一个第三方的一个这个仓库啊才能够使用啊那么呃我们在前面所看到呃国外不可以要杠加了这个项目啊他的这个叫呃stata啊这个这个文档中啊在最后也说了这个问题就是说你需要去添加这样的一个第三方的一个这个仓库那么才能够去下载到这个包要不然你下载不到的啊那么其实我们可以把这个地址的我们打开来看一下那么我们打一下走
[02:24] 那么在这个里面呢它有一个com然后呢有一个webq2.java然后呢再有还有一个它然后再点进去等待啊有点慢啊这会儿有点慢等待一下那么我们就可以看到在这个里面呢有它的很多的一些这个所发布的一些版本啊那么可以看到那么最新的这个版目前最新这个版本呢是11.0
[02:46] 那么我们现在所用的呢就是最新的这个版本就11.0就这个版本那么也就是说你不配置这个地址它肯定下载不到价格包的啊那么怎么配置呢所以需要我们特别注意一下那么我的配置呢是在这的做一个配置啊是在我的在一般下面的在这个位置啊有一个我这个man的一个仓库啊我是做了这样的一个配置大家一定要去注意一下啊那么在之前呢在之前呢我们去配置我们的这个
[03:14] 呃配置我们这个伺服我们都是使用这个Mirror去做一个配置那么我们在这个位置就不能够去采用这个Mirror去做一个配置了为什么呢呃无论你是在这个位置配置我们本地的这个镜像啊就是我们这个呃本地的一个这个Mirror那么我们会把它设置为什么呢这个Mirror Off会设置为新啊会设置为这种新的配置那么我相信啊很多的同学都是这样的一种配置那么这样的一个配置呢就是说无论你
[03:43] 无论你去下载什么样的一些jar 包都会通过这个Mirror去做一个下载那么即使你配置了一些第三方的一些这个仓库那么它呢也不会从这个第三方这个仓库去做一些这个下载所以我们不能通过这种方式配置那么这个呢大家也要注意一下那么我们正确的一种配置方式呢是我们需要在我们的这个Profile中配置你的这个私服配置你的私服
[04:12] 以及什么呢它的这个第三方的这个就是GraphQL-Java第三方的这个仓库啊然后呢我们在下面的这个位置呢我们去把它的这个激活把这个profile给它做一个激活因为我本地呢我配置了有两个我的一个仓库啊本地配的两个师傅一个是我本机上面的一个师傅另外一个呢是阿里云的这个师傅
[04:36] 那么再往下走的是这个第三方这个伺服那么要配置的时候要注意它的顺序那么我下载价包的优先是通过我本地去下载本地如果没有就走这个阿里云那么阿里云要是没有的话就去走这个第三方的这个Grabqrk2这个java这个他的这个仓库所以我按照这样的顺序去做那个配置然后我下面做一个激活这样的话我们才能够去正常的去下载到他这个价包要不然的话是下载不了的这个点一定要注意
[05:06] 那么在讲一周呢我给大家只贴出了这个第三方的这个他的这个这个配置有个配置啊那么大家也要去可以基于这个配置做一些参考然后呢去把你的一些所配置的一些这个
[05:22] 我们的师傅去做一些这样的一个配置参考这样的配置去做配置刚刚大家也看到我这样的配置就这样去配好那么这个我得重点去强调了因为如果你不这样去配的话那么这个加包你是下不到的下不到加包你们这个项目是没法去写的好嘞那么我们接着继续接着继续那么接下来我们在这个工程下面创建一个包来创建一个优惠对象那么我们一会要去用到这个优惠对象OK
[05:51] 把包创建出来然后我们在包下面去创建一个优惠对象创建一个类就叫一个优惠对象好那么优惠对象创建好了那么下面我们把它的一些属性我们拿过来这样我们这样拷拷过来然后可以看到拷过来之后在这个里面它已经有了一些有了一些三个属性
[06:19] 包括有两个构造方法一个是没有参数的一个是全参数的构造方法下面就是一些get和set方法OK好那么我们这个类就搞定了那么到这里我们的这个工程就已经搭建完成了就搭建完成了那么接下来我们就要去编写它对应的代码的实现那么我们放到下一个视频来做一个讲解好那么关于我们的这个WebQL-Java的这个
[06:46] 工程的一个搭建呢我们就先讲到这里那么在这个里面呢大家一定要注意我们刚刚所讲的这个关于它的一个仓库这样的一个配置啊一定要注意如果不这样去配置的话那很有可能是你的那个价包下载不到的好那么关于这个工程搭建我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中创建一个 GraphQL Java 项目，并配置 Maven 依赖以解决 graphQL-java 包未发布到中央仓库的问题。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 Adobe Reader 中查看 PDF 讲义，显示“7.1.1、创建工程”章节，弹出的“New Project”对话框中填写了 GroupId: cn.itcast.GraphQL，ArtifactId: itcast-GraphQL-java，Version: 1.0-SNAPSHOT。
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
GroupId: cn.itcast.GraphQL
ArtifactId: itcast-GraphQL-java
Version: 1.0-SNAPSHOT

画面 2:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.GraphQL</groupId>
    <artifactId>itcast-GraphQL-java</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>

画面 3:
<dependency>
    <groupId>com.GraphQL-java</groupId>
    <artifactId>GraphQL-java</artifactId>
    <version>11.0</version>
</dependency>

画面 4:
<profile>
    <id>bintray</id>
    <repositories>
        <repository>
            <id>bintray</id>
            <url>http://dl.bintray.com/andimarek/GraphQL-java</url>
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
            <url>http://dl.bintray.com/andimarek/GraphQL-java</url>
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
            <url>http://dl.bintray.com/andimarek/GraphQL-java</url>
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
            <url>http://dl.bintray.com/andimarek/GraphQL-java</url>
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
        <groupId>com.GraphQL-java</groupId>
        <artifactId>GraphQL-java</artifactId>
        <version>11.0</version>
    </dependency>
</dependencies>

画面 12:
package cn.itcast.GraphQL.vo;
public class User {

画面 13:
type UserQuery {
    user: User
}

画面 14:
<dependency>
    <groupId>com.GraphQL-java</groupId>
    <artifactId>GraphQL-java</artifactId>
    <version>11.0</version>
</dependency>

4) 出现的 PPT 标题、架构图/流程图的

