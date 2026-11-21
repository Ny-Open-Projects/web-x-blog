# 08_项目搭建_原始项目结构介绍及导入

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\08_项目搭建_原始项目结构介绍及导入【海量资源尽在 666java.com】.mp4
- 时长 9分30秒（音频 571s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们一块来看一下这个后端工程的一个结构咱们马上的要去导入咱们的一个工程那这工程的主要来看这个图先来看这个工程结构的一个关系那这个图啊可能不太清楚咱们呢可以打开当前图片里面有一个4打开它啊那这个里面呢就是说明了当前的一个项目的工程的目录结构工程的结构关系
[00:28] 首先呢咱们最顶级的是一个Spring Boot的一个项目啊就是咱们的项目啊这是咱们的项目啊咱们的项目呢主要呢是当前的是继承了继承了当前的一个Spring Boot建成一个这么化啊好那这个GammaBedNews呢它这个工程呢主要呢是去定义了什么呢定义了一些统一的依赖信息它是一个POM工程
[00:58] 是一个聚合工程OK再往下看再往下的话它分别是有五个其实是四个第一个是common第二个是model第三个是util和apis是吧咱们分别说一下它的功能第一个咱们common也是会去继承像这些它其实都会去继承那继承的意思就是咱们也会依赖于当前域sprint boot好那common里边主要定义了一些什么就是
[01:28] 公共配置的一些东西比如说咱们要去封装一个Radius要去封装MySQL要去封装卡不卡那这时候咱们都是在common工程里边去完成好那下面这个呢modo呢modo的话就是去里边提供了一些公共的这种实体类比如说咱们项目中用到的一些具体跟表映射的实体都是放到了modo中
[01:57] 好那Utils呢那很显然这个就是放的一些通用的工具类好那APS呢主要就是对外包录接口的一个这种定义接口的一个项目那还有一个啊就是Test那这个呢就是一个测试的一个代码工程啊那这个工程咱们在项目中并没有使用OK然后下面还有啊下面还有一些微服务那微服务的话呢是基于当前的某一些业务去
[02:24] 分的划分的一些微服务模块那首先呢咱们来看啊里边是包含了这么多到咱们具体开发的时候咱们可以具体再讲啊咱们可以讲一个今天会涉及到应该是两个啊一个是文章一个article还有一个是behaviour这个呢是行为这两个呢咱们今天都会去涉及到那它呢也会去基层上面的四个
[02:51] 那顺便的啊也就去继承了当前黑马Leaders News也就是使用了Spring Boot当前的项目啊OK那这个是根据具体业务去划分的某一个微服务的模块工程好那这个结构啊咱们就先介绍到这里然后下面呢咱们就去干嘛呢就去来去
[03:15] 搭建一些环境啊那这个这里边呢也有文字描述当前某一个模块是干啥的啊OK大家呢可以去读一下那下面咱们就来去设置一些开发环境那开发环境呢首先呢咱们有一些要求啊第一个JDK呢必须是1.8最好是不要用高版本啊
[03:34] 最好是跟项目是保持一致是1.8就可以啊用的是idea然后是他们开始是8.5的啊还有一个是咱们用到的git但这个项目中并没有用git管理咱们要去用的话呢也是会用到这个当前的gitok那好啊那首先呢咱们要去导入啊导入咱们的一些这种工程那这工程的话其实就在哪呢就在咱们这个
[03:58] 当前资料中的有一个这样的文件夹咱们把它放到一个目录下边直接用按键打开哎就可以啊那好那咱们那咱们呢就来去打开当前的文件夹里边第01里边有一个资料资料里边呢有一个后台初始代码ok 把它呢就是他啊把它呢拷贝到一个空目录下边啊呃咱们啊我在这啊去创建了一个呃在地盘创建了一个空的文件夹咱们再去创建一个叫空好吧那么把
[04:28] 刚才复制的代码了好考过来之后呢咱们就有就可以用按D的呢去打开打开啊打开的话就选择当前的目录就是地盘的呃黑马Leader News然后有个code ok就是他啊好点ok好那打开之后呢他需要去加载一些环境啊这环境的话里边是有一个Movie的一些东西咱们不用管他这样插号就可以了啊嗯那首先呢
[04:58] 这里边其实还没有说刚才有一个就是环境的配置那环境配置其实就包含了这几块内容第一块咱们要去设置一个Maven的本地仓库你必须要设置你的仓库那这个仓库到后期会去提供当前的仓库你指定当前资料中提供的仓库就可以这个仓库咱们可以看一下我这仓库已经指定好了就在当前的Settings里边是吧
[05:25] 这有一个什么呢这有一个build里边有一个build tools那这时候呢你需要去配置你的maven的环境这是第一个然后第二个呢第二个呢就是咱们需要去配置一些编码编码那编码的话在哪是吧在有一个view还有settings里边然后找到当前的endingeditor是吧里边有一个view encodings
[05:51] OK那这几项啊首先这两块是UTF-8下面下面这项也是UTF-8OK那这样的话环境就算是导完了那咱们的项目呢也算是导入进来了就这么个效果咱们可以打开看一看啊OK那这个呢就是这么一个效果那咱们呢顺便呢就可以打开这个项目去简单看一眼啊比如说这个呢是一个最顶级的项目其实就是咱们刚才打开的这个图就是黑马Leader News是吧
[06:20] 打开它是一个POM工程打开它的POM文件来看一看里边有啥OK咱们可以看到首先这是定义它的一个坐标是吧然后它有四个模块然后有一块非常重要你看这有一个Parent是吧那这时候它就是继承了当前Spring Boot的一个Parent并且是定义的是比较新的一个2.1.5的一个版本好
[06:46] 当然这里边呢是不仅仅是进行了它刚才开除了这工程呢还有一个最大的功能就是可以定义统一的依赖信息所以说呢下面呢还有很多的这种依赖版本OK那咱们讲到具体某一块业务的时候呢咱们可以大概去讲一讲啊比如说咱们用到的是Spring Boot Log4j2是吧还有一个是Long Book
[07:12] 下面还有一些比如说咱们有一些自己的模块的定义是吧还有啥呢Splendor Boot这种起步依赖外部的起步依赖还有再往下看关于日志的还有关于这种上传下载无线包的一些工具类还有加密的买搜索的等等有很多OK那这个大家可以具体去看一眼好吧但是下面还有一些东西下面还有一些具体的插件
[07:43] 咱们具体用到的时候呢咱们可以具体再再讲好吧那行啊那这个呢就是咱们的这个复工程那复工程里边其实还有这四个这四个刚才也说了啊咱们通用的工程比如封装都是在common里边在common里边打开看一看咱们这个包结构呢都是叫com.黑马甲common跟他们的模块是是对应上的啊里边是目前是封装了一些信息咱们具体讲的时候咱们可以打开再去看一眼
[08:12] 好那么看第二个啊第二个里边非常重要的就是有一个model那model里边呢就是定义了一些实体那目前的话这个实体呢也定义好了绝大部分情况都是根据当前的模块去拆分比如说admin是吧article还有什么media还有咱们的user还有什么呢啊还有咱们的patch ok那还有啊那还有的话就是youtube那这里边呢是已经
[08:39] 已经有存在的工具类啊有那么多啊大家也可以点开看一眼啊咱们具体讲的时候用到的时候呢咱们还可以再去具体说然后还有一个啊就是最后一个就是APIS那这个呢就是咱们通用的接口定义都是在当前的这个工程下面啊现在这里边没有没有任何东西啊没有事啊咱们到具体定义的时候咱们还会再去讲
[09:02] 大家发现了没有啊这里边呢除了一个模块之外呢你看每一个模块下边呢都还有这三个文件那这三个文件是啥OK没有问题咱们一会儿呢再去具体讲模块的时候或者讲通用配置的时候咱们这些呢还会再次去介绍OK那目前的话呢咱们这个工程的结构关系和工程已经到处进来了好那这块就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

