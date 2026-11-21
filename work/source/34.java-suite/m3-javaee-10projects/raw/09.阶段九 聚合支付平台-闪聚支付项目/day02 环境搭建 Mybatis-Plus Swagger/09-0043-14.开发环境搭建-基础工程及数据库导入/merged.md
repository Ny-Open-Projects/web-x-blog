# 14.开发环境搭建-基础工程及数据库导入

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\14.开发环境搭建-基础工程及数据库导入【海量资源尽在 666java.com】.mp4
- 时长 7分12秒（音频 432s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢我们开始导入闪聚支付项目的基础工程那么首先呢我们来看一下在我给大家发的资料文件夹当中有一个闪聚ZIP的这个压缩包那我们把它解压开你会发现在这个里边呢有一个common这个目录其实这就是我们的一个基础工程以及一个负的这个POM文件大家可以看到它的
[00:28] 是有一些依赖管理的这里边你看有Spring Cloud的还有这个Spring Cloud的阿里巴巴包括其他我们所用到的一些包那么这些包呢回头我们在课程当中用到的我会给大家说好那么现在呢我们要做的就是把基础工程呢导入到我们的IDL工程
[00:51] 那这里边我要说一下就是在我们到企业里边去开发其实也是一样的首先到企业里边呢会拿到一个Gate账号然后呢会进行工程的这个导入好那来我们来看一下吧这里边我们需要找到我们要导入的工程的目录位置这里边我在咱们的这个code这个目录下啊我把它拷进去好然后呢这里边你看你复制路径然后这里边
[01:20] 我们就怎么弄啊打开这样就可以了好这样的话我们这个工程呢就导入进去了当然啊这个前提呢是我在之前给大家讲的要把这个什么Maven环境啊JDK啊等等这些东西全部配置好那其实到其实大家可以看到我这个Maven环境是好像配的有点有一点点的问题啊我们要用用那个Maven我的这个3.3.9啊其实我要改一下是吧
[01:51] 我要改一下啊F盘好那这个呢是F盘这个下边是吧然后呢那你要改我们用的老师用的是3.3.9这个版本选它OK这样是不是就OK了好然后呢当然你也可以让它去自动的去导入这个依赖把这个钩打上就行好
[02:28] 这样我们的这个基础工程呢就导进去了啊然后呢打开他的这个Maven依赖这个标签我们看一下其实他所依赖的东西都已经进来了好像还不是很我看一下common咱们打开common看一下里面都有啥common这里面呢主要是将来放我们项目的一些通用类这是Jason转换的对吧这是上面是日志的下面是工具包然后呢包括后边我会讲一个swag
[03:00] 好longbook之前我们提过对吧好这是common报其实里边倒没有什么东西回头我们会用里边我们项目当中写好的一些你比如说通用的一些domain这些类包括这个工具你看工具类我们不用去一个一个看了回头我们项目用哪个我给大家说然后在palm插门这是我们的副工程的palm文件
[03:28] 副工程的泡沫文件的话这里边你要注意副工程做的是不是就是版本的依赖控制对吧也就是这个标签Dependency Management是吧那里边呢它其实就是要控制它所有子项目所用的一些什么版本那这边我们看阿里巴巴SpinCloud阿里巴巴SpinCloud好然后呢包括驱动啊包括MapTestPlus这些我们在前面都已经说过了对吧
[03:55] 好包括有一些工具类的包呢其实在这里头的包是所有的包大家可能没有见过回头呢我们用到哪个包我会给大家来说哪个好那这个基础工程我们是不是就导进去了吧导入基础基础工程的目的啊是不是就是在基础工程的基础之上稍后我们要再去创建我们各个微服务的项目对吧好然后呢导入基础工程之后呢我们接下来
[04:24] 我们要导入我们的Circle语句那这个Circle语句就是我们项目的一些初始化的数据啊其实在企业里面开发我们最终的项目发布其实它也有一个安装的一个脚本安装脚本其实里面有一部分就是你的初始化的数据脚本这个数据库的脚本里面包括键表呀默认的表要创建好对吧还有一些初始化的数据那我们来看这里面呢还是在
[04:51] 给大家提供的这个资料文件夹下这个资料文件夹下边呢有一个叫做散具配-init这个circle语句在这个文件当中我们可以看到是不是就是有很多的键表语句但是这里面我要说一下因为我们知道微服务项目每个微服务是不是对应一个数据库那这里边我们有好多微服务呢也需要建很多数据库接下来我们主要是
[05:22] 管理这一块的内容所以这里边我们先把商户的这个数据库商户的这个数据库以及这个交易中心的数据库因为这两个数据是我们马上要用的所以我们呢先把这两个数据库呢给它建起来怎么创建呢其实就是我们要连上我们的数据库啊然后呢执行我们刚才给大家提供资料文件夹下边的这个Circle语句然后我们就可以把
[05:52] 我们要的这个数据库啊表啊包括数据数据的全部自动的就创建好了好你选择它然后呢执行那这个我们执行完毕之后呢我们刷新一下这里边呢我们看闪具开头的啊闪具配开头的大家看到这里边是不是有一个叫闪具配Market Service看见吗这里边是不是有导进去的一些表那这里边表你会发现大部分是没有数据的啊
[06:24] 大部分没有数据的还有transaction其实我们刚才导进去的是这两张表后边就不要管啊后边是回头我们还要重新去导的我们刚才那个脚本呢就这两个数据库好了那么到这儿我们刚才做了一件什么事啊就是把基础工程啊给导进去了后边我们在基础工程的基础之上啊我们要干嘛呀创建我们的微服务工程还有我们把数据库的circle语句初始脚本
[06:52] 是不是也导到我们数据库了这时候我们是数据库也有了对吧基础工程有了那下一步是不是就开始去搭建我们的商户平台的一些微服务了好那么到这里基础工程的导入以及项目数据库的导入就完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中导入和配置 shanjupay 项目，包括查看项目结构、编辑 pom.xml 文件添加依赖、以及查看项目文档中关于数据库和微服务的说明。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：显示 Windows 资源管理器，路径为 D:\teach\shanjupay\model2\output\dao2，包含三个文件夹：generator、shanjupay、shanjupay.zip。
画面2：IntelliJ IDEA 编辑器中显示 pom.xml 文件内容，包含父项目配置、项目构建配置、属性定义和两个依赖项（alibaba-cloud 和 spring-cloud-starter）。
画面3：Windows 资源管理器，路径为 D:\teach\shanjupay\model2\output\dao2\shanjupay，显示为空文件夹。
画面4：IntelliJ IDEA 中打开“Open File or Project”对话框，路径为 D:\teach\shanjupay\model2\code\generator，左侧显示项目结构，包含 src、resources 等目录。
画面5：IntelliJ IDEA 中显示 shanjupay 项目的结构，选中了 shanjupay 目录，右侧编辑器显示 RestResponse.java 文件内容，包含 resource 和 plugin 配置，底部有 VCS 映射错误提示。
画面6：IntelliJ IDEA 中打开“Select Base Settings: File”对话框，显示了 apache-maven-3.5.6-bin.conf 文件夹结构，选中了 settings.xml 文件。
画面7：IntelliJ IDEA 中显示 pom.xml 文件内容，包含多个依赖项，包括 alibaba、spring-cloud、projectlombok 等。
画面8：IntelliJ IDEA 中显示 shanjupay-common 项目的结构，选中了 domain 包下的 BaseException 类。
画面9：IntelliJ IDEA 中显示 pom.xml 文件内容，包含依赖管理部分，包括 alibaba-cloud、spring-cloud、projectlombok 等依赖。
画面10：IntelliJ IDEA 中显示 pom.xml 文件内容，选中了 org.projectlombok 和 org.apache.maven.plugins 依赖项。
画面11：Windows 资源管理器，路径为 D:\teach\shanjupay\model2\output\dao2，显示了三个文件：code、Nacos-repository、output。
画面12：显示一个蓝色背景的空白窗口，可能是某个软件的启动界面或错误提示。
画面13：IntelliJ IDEA 中显示 shanjupay_merchant_service 项目的结构，选中了 shanjupay_merchant_service 目录。
画面14：显示一个文档页面，标题为“1.5 导入项目初始SQL”，内容包括使用客户端连接 MySQL 执行 shanjupay_init.sql 脚本，以及数据库清单和项目服务职责表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.3.RELEASE</version>
        <relativePath/>
    </parent>

    <groupId>com.shanjupay</groupId>
    <artifactId>shanjupay</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>shanjupay</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
        <spring-cloud.version>Finchley.SR1</spring-cloud.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-alibaba-dependencies</artifactId>
            <version>2.1.0.RELEASE</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter</artifactId>
            <version>2.1.0.RELEASE</version>
        </dependency>
    </dependencies>
```

画面5：
```xml
<resource>
    <directory>src/main/java</directory>
    <includes>
        <include>**/*.xml</include>
    </includes>
</resource>

<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
</plugin>

<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <source>1.8</source>
        <target>1.8</target>
    </configuration>
</plugin>
```

画面7：
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-alibaba-dependencies</artifactId>
            <version>2.1.0.RELEASE</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter</artifactId>
            <version>2.1.0.RELEASE</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

画面9：
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-alibaba-dependencies</artifactId>
            <version>2.1.0.RELEASE</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter</artifactId>
            <version>2.1.0.RELEASE</version>
        </dependency>

        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.0</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

画面10：
```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.0</version>
    <scope>provided</scope>
</dependency>

<dependency>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.0</version>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
PPT 标题：1.5 导入项目初始SQL
表格数据：
| 数据库名称            | 数据内容         |
|-----------------------|------------------|
| shanjupay_merchant_service | 用户中心数据     |
| shanjupay_transaction    | 交易服务数据库   |

表格数据：
| 服务名               | 职责             |
|----------------------|------------------|
| shanjupay_merchant_service | 用户中心服务     |
| shanjupay_transaction      | 交易服务         |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

