# 09.搭建后台服务系统

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\09.搭建后台服务系统【海量资源尽在 ubkz.com】.mp4
- 时长 7分43秒（音频 464s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下搭建后台的服务系统那么我们整个后台的服务系统呢我们采用的是SOA的这种架构的思想那么什么是SOA呢它其实就是面向服务的这种架构就是我们把一些这种我们的一些模块都拆分成一个一个的服务就面向服务这种架构然后呢我们的整个的服务的治理呢我们采用的是double这个框架
[00:28] 作为我们的一个服务治理框架做一个这样的一个搭建那么在后台系统的一个架构我们来看一下那么整个后台服务系统或者说后台系统我们都称之为叫做这个ITcast浩克Manager这个是我们的后台的系统那么我们后台系统又会被分为两个系统一个是Manager API系统一个是叫Doubled ServerDoubled服务系统
[00:57] 那么还有最底层的就是MySQL那么最底层MySQL往上面走就是服务往上面走的就是API那么我们有些其他的应用包括我们的一些前端的应用对吧还有前台系统应用手机的应用等等应用他都会去通过这个API这个系统去做一个访问然后呢API系统呢再去调用我们double中的这个一个一个的服务一个一个的服务再去做这样的一个调用OK然后呢在我们这个每一个这个服务呢
[01:27] 他就再去调用我们的这个数据库是这样的一个调用的过程啊好那么接下来呢我们先把这个整个这个项目呢我们先搭建好然后呢我们再去做一个里面的一个功能的一个开发那么在这个double这个服务内部是不是会有很多的这种服务啊所以说我们会认为什么呢哎这个是一个副工程副工程下面呢有两个子工程对不对然后呢
[01:54] 这个又变成一个复工程了对不对它下面的又会有很多的一些子工程OK其实这个还需要再做再做拆分后面我们在讲的过程中我们再说好那么我们接着继续往下面看最终我们创建完的工程结构就这样的一个结构那么首先有一个是manage这个工程然后在这个下面有两个子工程一个是API一个就是double the server作为一个这样的一个
[02:18] 两个子工程好我们先把这个副工程以及这两个子工程先创建出来那么首先我们来创建itcast浩克manager工程这是我们的一个后台系统的一个工程好那么我们在这个位置点击这个new一个project就创建一个新的工程然后点击下一步然后国外日历我们就输入cn.itcast点什么点manager浩克
[02:47] 点什么呢manager然后呢这个artifact id呢就是它然后点击next然后呢去输入这个内容点击finish完成好那么我们来看一下这个工程是不是就创建好了那么我们来看一下它有没有一些提示的信息呢注意一下在这个位置呢其实有一个这个选项就enable这个auto import我们去点一下它
[03:17] 就会自动去引入我们的一些相关的一些依赖好那么现在我们就已经把这个工程创建好了那么其实这个创建的是一个副工程对吧那么我们还需要持续的在下面去创建一些它的子工程然后我们把它的这个依赖我们回过头来我们再来添加我们先把它的一些子工程先创建出来一个是叫做 APIAPI这个server一个叫 double server
[03:46] 好那么我们在这个里面创建一个module然后呢我们点击下一步然后呢拷贝它下一步然后呢拷贝然后点击非净是完成好嘞那么这个子子工程师就创建好了然后呢我们在这个下面继续再创建它的哎错了然后呢继续创建它的这个module然后呢呃在这呢我们要选择这个1.8啊下一步然后呢到这然后呢下一步然后呢点击非净是完成好这样的话我们这个
[04:15] 三个工程是不是就已经创建好了但是没有创建好API Server他说API Server刚刚我们创建的是不是名字是相同的对吧这样我们重来创建一个下面我们创建这个刚刚我们就创建上面去了他是不对的然后点击module重来创建一个点击下一步返回然后点击这个然后下一步然后到这
[04:44] 这个double这个server下一步double server然后点击finish完成那我们可以看到这个工程是不是也创建好了刚刚创建错了创建的是上面这个好那么这样的话呢我们这个工程呢就搞定了那么接下来呢我们给它去导入一些相关的依赖那么我们在最外面这个minds工程中呢我们去导入这么多的依赖咱们把它拷过来拷贝到这个下面那么我们拷过来之后呢来看一下那么我们
[05:14] 也就是说只要是在我们这个里面去导入的一些依赖那么所有的子工程是不是都会去使用这个依赖对吧好那我们来看一下那么首先其实它是需要一个parent就是我们Spring Boot的一个支持好然后给它一个parent然后来靠一下考到这这个是我们Spring Boot的一个parent然后下面我们去引入一些我们具体的一些依赖那么来看一下
[05:45] 那么首先引入的是这个Springboard的test测试框架把它引入进来然后再引入我们的这个double的这个支持因为无论是你这个项目还是这个项目是不是都会使用到这个double对吧然后引入double这个框架然后引入一个Apache下面的工具包这工具包我相信大家应该都认识都认识工具包我们经常像使用的一个StreetUtils等等都在这个下面的所以在我们的工程里面都会用到它基本上都会用到
[06:15] 所以我们在最外面这个副工程中去引入了这个工程OK那么下面我们引入这个ZK的依赖那么引入这个ZK的依赖目的是不是要去使用我们的ZK的注册中心对不对好那么这个无论是我们的这个Double的这个Provider也就是提供者还是Concern是不是都需要去连接到我们的注册中心所以这两个工程都需要这个ZK的依赖OK好嘞
[06:44] 好 那么现在我们就把这个依赖是不是就导入进来了我们来看一下这个是API的工程那么在API里面我们给它引入的是一个web的一个支持因为API是不是对外要提供一些接口服务我们先要实现的就是RESTful服务所以我们需要一个web的支持OK好 然后下面的这个工程它需要的是一个普通的一个工程的支持
[07:13] 非web项目所以我们在这个里面给他去引入一个非web项目的一个这样的支持好那么到这里我们这个工程是不是就创建好了好那么大家来我们大家回顾一下那么前面我们说过那么我们这个工程会被拆分成是不是两个工程对吧一个是API这个工程一个是这个double这个server这个工程两个工程OK在这个下面还会继续做一个拆分好那么关于我们这个系统的这个搭建我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
搭建基于 Spring Boot 和 Dubbo 的后台管理系统，包括创建工程、配置 Maven 依赖和模块结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档内容，标题为“3. 搭建后台服务系统”，说明后台服务系统采用 SOA 架构，使用 Dubbo 作为服务治理框架进行搭建。同时显示了示例用户数据（JSON 格式）。
画面2：展示工程结构图，包含“itcast-haoke-manage”、“itcast-haoke-manage-api-server”和“itcast-haoke-manage-dubbo-server”三个模块。同时显示了 pom.xml 文件的开头部分。
画面3：展示 pom.xml 文件内容，包含父项目配置，<artifactId>spring-boot-starter-parent</artifactId>，<version>2.1.0.RELEASE</version>。
画面4：在 IntelliJ IDEA 中，右键点击项目目录，弹出菜单，选择“Add Framework Support...”。
画面5：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含父项目配置和模块声明。
画面6：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含模块声明。
画面7：展示 PDF 文档内容，显示了 Maven 依赖部分，包括 spring-boot-starter-test、ZooKeeper、agroal、dubbo-spring-boot-starter 等依赖。
画面8：展示 PDF 文档内容，显示了 Maven 依赖部分，包括 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、ZooKeeper、agroal 等依赖。
画面9：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、ZooKeeper、agroal 等依赖。
画面10：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、ZooKeeper、agroal 等依赖。
画面11：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、ZooKeeper、agroal 等依赖。
画面12：展示 PDF 文档内容，显示了 Maven 依赖部分，包括 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、ZooKeeper、agroal 等依赖。
画面13：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含 spring-boot-starter-web 依赖。
画面14：展示 PDF 文档内容，标题为“3. 搭建后台服务系统”，说明后台服务系统采用 SOA 架构，使用 Dubbo 作为服务治理框架进行搭建。同时显示了示例用户数据（JSON 格式）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```json
User{id=1, name=John, age=18, email=test1@acmam300.com}
User{id=2, name=Jack, age=20, email=test2@acmam300.com}
User{id=3, name=Tom, age=28, email=test3@acmam300.com}
User{id=4, name=Family, age=23, email=test4@acmam300.com}
User{id=5, name=Dillo, age=24, email=test5@acmam300.com}
User{id=6, name=li1, age=28, email=zhangan@qgq.com}
```

画面2：
```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>cn.itcast.haoke</groupId>
  <artifactId>itcast-haoke-manage</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>pom</packaging>
  <modules>
    <module>itcast-haoke-manage-api-server</module>
    <module>itcast-haoke-manage-dubbo-server</module>
  </modules>
</project>
```

画面3：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
    <groupId>cn.itcast.haoke</groupId>
    <artifactId>itcast-haoke-manage</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>itcast-haoke-manage-api-server</module>
        <module>itcast-haoke-manage-dubbo-server</module>
    </modules>
</project>
```

画面4：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
    <groupId>cn.itcast.haoke</groupId>
    <artifactId>itcast-haoke-manage</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>itcast-haoke-manage-api-server</module>
        <module>itcast-haoke-manage-dubbo-server</module>
    </modules>
</project>
```

画面5：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
    <groupId>cn.itcast.haoke</groupId>
    <artifactId>itcast-haoke-manage</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>itcast-haoke-manage-api-server</module>
        <module>itcast-haoke-manage-dubbo-server</module>
    </modules>
</project>
```

画面6：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
    <groupId>cn.itcast.haoke</groupId>
    <artifactId>itcast-haoke-manage</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>itcast-haoke-manage-api-server</module>
        <module>itcast-haoke-manage-dubbo-server</module>
    </modules>
</project>
```

画面7：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.ZooKeeper</groupId>
        <artifactId>ZooKeeper</artifactId>
        <version>

