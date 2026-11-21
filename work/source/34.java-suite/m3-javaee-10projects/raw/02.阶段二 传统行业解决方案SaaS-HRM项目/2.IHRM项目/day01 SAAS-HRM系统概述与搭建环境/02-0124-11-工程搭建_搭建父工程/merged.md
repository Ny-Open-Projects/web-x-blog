# 11-工程搭建：搭建父工程

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\11-工程搭建：搭建父工程_【海量资源尽在 ubkz.com】.mp4
- 时长 5分26秒（音频 326s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那么接下来呢就可以对我们整个工程做一个搭建的一个过程那首先我们要做的第一件事呢就是构建一个复工程那复工程构建好了之后在这个复工程的基础之上构建工具类的一个子模块和我们抽取的实体类模块那好了首先一个一个的来看构建复工程那在这边呢我们用的是idea工具我先把我的idea工具启动起来
[00:32] 好了这个idea启动起来呢还是比较快的还是比较快的好了已经打打出来了启动成功的这边我们先去创建一个新的工程create new project好了需要各位注意啊我们是创建的是一个maven工程所以我左边勾选maven那底下呢这边呢会从网络去加载它基本的一些股价当然我们现在创建的是一个基本的一个副工程不需要用股价直接点击next即可
[01:05] 那group id我们叫做com.比如说ihrm那artifact id呢我把它称之为ihrm下滑线parent parentok点击next那这个告诉我你要把你的项目放到哪我就放到了hrm这个包下放到hrm叫做parent当然了我不想放到这里面我让它更看起来更加清晰一点其实也可以比如说呢我就放到
[01:35] 一盘的workspace下我叫做hrm好了这边所有的路径已经做了一个修改点击finish好了他会告诉我这个目标文件夹不存在是否要创建ok好了这样一来呢他就会帮助我创建好了一个新的工程那这个新的工程我们创建好了之后底下这边的勾选上是否要自动的导入一些没问题的一些坐标
[02:06] 那这边呢有跟各位做一个交代就是说啊你这个工程创建好了之后有可能想要对Maven做一个简单的配置那做这个Maven配置呢找到左上角Fill这边找到一个叫做Siting哎错了找到Siting好了那接下来呢在这里面搜索一下Maven找到Maven这里面有Maven的基本的配置当然了
[02:35] 如果你没有配过的话简单的自己做一个配置其实就可以这里面也比较简单这边有什么它的Maven安装目录究竟在哪好了这边呢会有你当前Maven的配置等等等等很多那配置好了之后我们接下来就可以对这个创建好的工程做一个简单的修改那首先呢既然是一个我们叫做复工程那既然是一个复工程的话其实里面不会包含一些什么代码的
[03:03] 那所以我把这个SRC目录先给它删掉因为看起来有点别扭我就把SRC删掉了那接下来在这个工程当中我们就可以导入相应的坐标那导入这个坐标这些坐标在哪呢不需要各位重点记忆导入的这些配置在今天以资料的形式已经给各位下巴好了我们可以一起简单的来看一下IHM第一
[03:31] 资源里面有一个POM.txt我们打开它把这里面的内容Ctrl C全部copy到我们的复工程的POM文件下Ctrl V好了call过来之后呢简单的对这些内容做一个说明做一个说明首先右下角Enable auto import自动的导入好了那接下来呢我们这是一个复工程
[04:01] 复工程我们的打包形式用的是POM文件那我的工程名HRM好了在这边有它的描述那接下来我们用的是Spring Boot的这套开发环境来做的所以把这个包也引进来那接下来呢有一个叫做PropicePropice里面规定了我整个工程的一些配置那继续往下看这里面的内容呢用的是我们的
[04:26] Spring Boot用的是版本是2.0.5.release是最新的一个版本是一个稳定开发版好了那接下来呢继续这里面呢可能会用到它的web的一些环境啊还有日志的一些环境啊还有测试相关的一个支持当然了在里面呢我还导入了一个叫做FastJson阿里巴巴提供的Json类型转化的那除了这个FastJson之外还有一个Debundis这个需要我重点的强调一下这一个叫做Lomabook这么一个插件
[04:56] 这个插件一会会简单的提它主要是为了省略我代码当中的get set方法的但我们之前写get set方法有点啰嗦太麻烦了用这个插件它能自动生成就这么一个点点的一个说明OK那底下的一些配置就不用再多说了直接call过来即可那这样一来我这个复工程其实就已经搭建成功了各位来看比较简单创建工程引入相应的配置这些配置还都是call过来的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

