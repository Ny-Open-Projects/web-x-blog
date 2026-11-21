# 06.今日佳人功能实现之搭建dubbo工程

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\06.今日佳人功能实现之搭建dubbo工程_【海量资源尽在 666java.com】.mp4
- 时长 7分34秒（音频 454s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那我们这次继续那么接下来呢我们就能够去编写代码了那么前面我们这个数据库呢就是MongoDB呢也提供OK了好,那么下面我们来看一下那么首先呢我们来画一个图啊给大家去说明一下就是我们呢目前这个架构呢是这样的就是这个是我们的一个前端的一个系统这个是我们前端系统那我们来写一下这个就是我们的这个前端前端的一个这个系统
[00:28] 那么其实在这个位置呢我们是使用了安卓的啊安卓的一个这个客户端对吧然后呢我们就使用它好那么这是一个apk啊这样的一个包这是我们的前端系统然后呢前端系统呢会去访问我们后端系统的一个这个服务也就是在这个位置啊我们是后台呢是需要提供我们的一个服务了后台系统的一个后台系统
[00:56] 然后呢提供这种服务啊提供服务这个呢是呃由这个呃前端这个系统然后呢直接去访问啊我们后台系统啊访问他啊做一个这样的一个访问啊访问他呃然后呢我们来写一下这个叫访问啊访问呃访问啊访问好那么呃我们后台在我们后台系统中啊那么我们其实有很多的一些这个业务逻辑需要去做一些这个编写
[01:27] 那我们不可能把所有的这种业务逻辑是不是都丢在这个里面去做一些完成啊那么我们会将我们的一些核心的一些业务功能呢我们再再去什么呢写我们的一些这个呃服务系统而我们这种服务系统啊注意这个我们来写一下啊这个叫什么这个叫我们的服务系统啊服务系统而一些服务的系统呢啊那我们会采用什么呢采用double的形式啊
[01:54] double来完成这种v服务v服务这种架构这个大家应该并不陌生了对吧所以我们使用这个double来做一个完成然后呢在我们这个系统中呢他在去干嘛呢去调用他在去调用我们的后台所写的一些这样的一些这种服务这个叫什么呢调用调用这样的一个服务然后呢我们这个double这个服务呢
[02:24] 他呢再去访问谁了访问我们的一些这个数据库啊或者说说放我访问我们刚刚所写的这个什么mongodb啊啊mongodb他再去做这样的一个访问啊那么大大致的一个流程呢啊他就是这样的一个流程所以说呢接下来呢我们就要去创建一个谁呢创建一个啊这个系统啊创建一个他啊创建一个他好那么下面我们就来创建我们的一个哎呃创我们接下来创建的是这个啊double这个系统
[02:54] 之后我们再创建这个我们先来创建这个double这个系统那么我们来看一下这个double系统的一个创建那么名字就叫这个itcast那么我们这个写的时候叫什么叫my是吧my炭花double好我们就在我们之前的这个中我们来创建一个module然后我们继续往下面去写它的一个artifact id就叫my-什么的炭花-什么的double
[03:23] 然后呢我们点击这个下一步然后呢点击finish完成ok那么这个double呢是不是这个工程呢是不是就创建好了那么接下来呢我们就需要来创建它的子工程那我们知道在使用这个double的时候呢有两个工程那么一个就是interface那么一个呢就是Service这个工程所以说呢我们需要在这个double工程下面呢再创建它的什么子工程啊好那么我们再来写一个
[03:53] 创建它的一个module然后呢下一步那么下面再写一个什么interfaceinterface然后呢我们再去做一个拷贝然后呢finish完成那么这个工程呢就创建好了然后呢我们在这下面呢还是需要再创建它的另外一个子工程就是具体的一个实现类的一个工程那么就是Service这个工程了那么点击下一步那么点击这个finish这个完成
[04:20] OK好那么这样的话呢我们这个呢就创建好了对吧那么创建完成之后啊那我们就需要去导入一些这个相关的一些依赖了那我们就来看一下这个依赖的一些这个导入啊那么首先呢这个是我们的这个double的这个工程那我们来看一下这个里面它是不是自动会添加了两个这个module一个是interface一个呢就是这个Service好那么接下来呢我们就分别来看这两个工程的一些这个依赖
[04:49] 那我们需要在这个interface这个工程中呢去导入两个依赖一个是这个langbook因为我们在这个interface中呢不仅是要定义我们的一些接口而且呢是需要去定义什么呢定义我们的一些这个pozole的一些类所以说它是需要这个langbook去做一个这个定义的
[05:09] 那么还需要什么呢还需要我们这个mongodb的这样的一个依赖那么为什么要使用它呢原因是呢我们需要在我们的一些这个对象中是不是要去引入啊一些这个mongodb的一些这个对象啊比如说那个object id对吧至少你要用到它所以呢要把它引入进来所以说我们就把这个呢来做一个拷贝然后呢我们找到这个interface然后呢往下面一丢也就是说我们需要去引入这两个这个依赖
[05:38] 这两个依赖大家应该并不陌生了对吧好 那我们接着继续往下面看那么下面这个就是我们Service这个工程那么在这个工程中它所引入的一些就比较多了我们一起来看一下那么接下来我们来看一下在Service工程中的一些依赖那么我们来打开这个Service工程那么首先我们需要明确一点是那么在Service工程中它一定需要导入的依赖是谁呢是不是就是我们的interface那么来看一下
[06:09] interface把它的导入进来那么这个是必须要去导入的一个依赖对吧那么在Service中的做实现那么当然他肯定就需要导入了那么接下来我们就来看一下其他的依赖那么这两个依赖大家应该并不陌生了对吧一个是被boot一个就是什么我们这个test这样的一个依赖好那么把这两个我们先导入进来OK好导入进来了没有问题好那么接着继续往下面看
[06:38] 那么这个呢是double对Spring Boot的这样的一个支持还有double的依赖那么这两个呢把下面这给导入进来吧那我们在使用这个double的时候呢我们要有注册中心那我们会使用这个什么DrewKeeper作为我们那个注册中心了所以说呢我们就使用它了好把它呢依赖也导入进来然后呢下面呢我们会访问我们的MongoDB所以在这个位置呢也是需要把MongoDB相关的依赖呢也导入进来
[07:06] OK导入进来然后下面是一些工具类的一些依赖了那么把这个都导入进来导入这好那么这样的话我们所需要的依赖基本上就OK了那么暂时我们就先导入这么多那么如果后期我们会发现有一些依赖没有的话我们再去把它新增进来就可以了好那么关于我们工程的一个搭建我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面 7: 显示 IntelliJ IDEA 中的 `my-tanhuai-dubbo-Service` 模块的 `pom.xml` 文件内容，其中包含父模块配置：
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
    <artifactId>my-tanhua-dubbo-Service</artifactId>
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
    <!-- dubbo对Spring Boot支持 -->
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
        <groupId>org.apache.ZooKeeper</groupId>
        <artifactId>ZooKeeper</artifactId>
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
<!-- dubbo对Spring Boot支持 -->
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
    <groupId>org.apache.ZooKeeper</groupId>
    <artifactId>ZooKeeper</artifactId>
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
画面 12: 显示 IntelliJ IDEA 中的 `my-tanhuai-dubbo-Service` 模块的 `pom.xml` 文件内容，其中包含依赖部分：
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

