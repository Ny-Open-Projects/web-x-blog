# 09_爬虫系统导入

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\09_爬虫系统导入【海量资源尽在 666java.com】.mp4
- 时长 5分16秒（音频 315s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱接着往下讲然后下面咱们首先是要做一个事就是咱们需要导入咱们的一个爬虫的项目那这项目咱们微服其实已经创建很多了那这次咱们主要是导入这个项目里边已经做了一些内容这个搭建的过程咱们就不再去做了导入其实很简单咱们只需要从这拷贝一下不想哪拷贝到你当前的项目我们可以打开来看一下
[00:31] 比如说找到当前的文件夹然后是拷贝到这儿解压稍等我看看好这个东西这个其实就是项目解压到这之后你可以把这个包包给删了然后你看在这儿就能看得着看得着之后它是一个灰色的是吧它并没有加到当前的项目中怎么办你在这点个加号找到当前的项目然后点跑母文件点OK不行吗我看看
[01:07] 这时候能再这样先在这先在这去加上先在这去加上它的一个模块它也是一个模块模块叫color好加上之后这时候咱们可以再去看一下刷新一下好这个是不是有了找一找是不是有了有了之后你看这东西是不是就变回来了是吧没问题它这时候就是一个项目就是项目那项目咱们可以打开看一眼打开看一眼首先这是有POM文件POM文件里边
[01:41] 大家看它的复工程就是当前这东西是一样的然后下面会引入一些组件model common还有lamborg当然还有一些okhtp这些都是okhtp咱们主要是用的实验用让爬虫去访问去请求的一些东西下面还有一些东西这是最一般的咱们的一个什么微服务搭建的一个stardrive是吧还有什么呢还有test
[02:10] 是吧还有关于这个什么一些东西然后下面还有盘虫所依赖的一些程序啊这时候呢咱们你可以去看一看啊咱们把这个包直接导过来就可以了好吧那行那这个导进来之后呢咱们看看还有没有其他的东西啊首先呢咱们可以看一下配置文件这个配置文件其实三个呢也已经创建出来了是吧这个咱们就不用再去创建了啊那这个resource里边呢其实有三个是吧第一个呢其实没来可熟的是吧那这个呢就是咱们的一个
[02:38] 档块和应用名称然后这一块呢是redis啊redis的话其实咱们现在还没用着啊用到的时候咱们再说好吧这个先放到这用到的时候咱们需要再配置好呃加这个之后呢这还有一个叫color.prox那这是啥哎这个呢其实就是跟当前partners相关的一些这种数据啊或者叫配置那这配置到底怎么用啊什么时候用ok啊那这东西呢咱们也不要不要着急
[03:05] 一会咱们去讲到的时候咱们还会再去说比如说当前的一个悦耳的前缀后缀像这些东西怎么办怎么做一会咱们马上就会讲到这好吧然后除了这些东西还有一些东西它还提供了一些类提供一些类首先这是引导类这个东西都很简单是吧没啥可说的然后Config里边有一个Color Config这里边是空的是吧OK咱们一会会去配置
[03:33] 这个咱们一会再说好吧这是一个init config这里边的内容大家比较熟了啊第一个是init Jackson然后第二个呢是mycircle是吧第三个是卡不卡啊咱们也会用到卡不卡啊所以说这个内容呢咱们都要考过来OK行那这个咱们算是说完了啊然后下面还有些看不懂的包比如factory那这是干嘛的呀OK啊咱们一会呢会用到一个代理是吧主要呢是IP代理这个一会再说一会再说啊
[04:00] Helper呢跟Utils其实都是一些工具都是一些工具那这工具是啥呢咱们一会儿再讲这个工具到底该怎么用里边有什么功能咱们一会儿再说用到的时候咱们再说现在说大家也没有印象说完之后你可能这个印象这个脑子里过一过可能就记不住是吧这时候呢怎么到真正用的时候呢咱们再讲呢可能效果会更好一些好吧行那这个咱们先不说了啊
[04:26] 这里边有一个非常重要的包非常重要的包叫Process就它Processor这里边内容其实咱们最核心的爬虫的代码其实都放到这个里边一会咱们要去开发爬虫系统最重要的其实也是在这个包下边去创建一些类或者接口去完成咱们的爬虫的系统好吧这里边目前的话已经提供好两个类应该是有这几个类应该是有个包这是实体
[04:56] 实体的话现在大家也不用先了解先不用去了解啊当前这两个类呢其实也不用去着急去看一会咱们去用到的时候咱们再说行咱们先放到这儿一会咱们去开发的时候用到哪一块咱们具体再讲OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何初始化并配置一个名为“heima-leadnews-crawler”的爬虫项目，包括项目结构、POM文件依赖、配置文件内容及代码结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文件资源管理器中“heima-leadnews-crawler”项目文件夹，包含“chrome-driver_win32.zip”和“heima-leadnews-crawler.zip”两个压缩包，右侧显示PPT标题“5 导入 heima-leadnews-crawler 项目”和小节“6.1 初始化URL的获取”。
画面2：在文件资源管理器中，选中“heima-leadnews-crawler.zip”文件，准备解压。
画面3：在IntelliJ IDEA中打开“heima-leadnews”项目，显示项目结构和Maven Projects面板，提示“Invalid VCS root mapping”。
画面4：在IDEA中打开“heima-leadnews”项目的根目录下的“pom.xml”，显示父模块的配置，包括groupdId、artifactId、version和modules。
画面5：在IDEA中打开“heima-leadnews-crawler”模块的“pom.xml”，显示该模块的父级配置和依赖声明。
画面6：在“pom.xml”中，显示对“spring-cloud-starter-netflix-Eureka-client”依赖的配置。
画面7：在“pom.xml”中，显示对“spring-boot-starter-test”依赖的配置。
画面8：在IDEA中，项目结构视图中选中“src”目录下的“main”和“test”目录。
画面9：在IDEA中，打开“application.properties”文件，显示配置项如server.port、spring.application.name、redis.host等。
画面10：在IDEA中，打开“crawler.properties”文件，显示配置项如webdriver.chrome.driver、proxy.isUsedProxy、crawler.init.url.prefix等。
画面11：在IDEA中，选中“CrawlerConfig.java”文件，准备查看或编辑其内容。
画面12：在IDEA中，选中“process”包下的“Process.java”文件。
画面13：在IDEA中，选中“process”包下的“Process.java”文件。
画面14：在IDEA中，选中“process”包下的“Process.java”文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4的pom.xml内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.3.4.RELEASE</version>
        <relativePath/>
    </parent>

    <groupId>com.heima</groupId>
    <artifactId>heima-leadnews</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>heima-leadnews-common</module>
        <module>heima-leadnews-utils</module>
        <module>heima-leadnews-article</module>
        <module>heima-leadnews-behavior</module>
        <module>heima-leadnews-model</module>
        <module>heima-leadnews-user</module>
        <module>Service-myst</module>
        <module>heima-leadnews-admin</module>
    </modules>

</project>
```

画面5的pom.xml内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.heima</groupId>
        <artifactId>heima-leadnews</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>heima-leadnews-crawler</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>com.heima</groupId>
            <artifactId>heima-leadnews-model</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        <dependency>
            <groupId>com.heima</groupId>
            <artifactId>heima-leadnews-common</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.dataformat</groupId>
            <artifactId>jackson-dataformat-toml</artifactId>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.dataformat</groupId>
            <artifactId>jackson-dataformat-xml</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
        </dependency>
        <dependency>
            <groupId>us.codecraft</groupId>
            <artifactId>spring-boot-starter-spring-cloud-starter</artifactId>
            <version>1.0.0</version>
        </dependency>
    </dependencies>

</project>
```

画面9的application.properties内容：
```properties
server.port=${port.crawler}
spring.application.name=${sn.crawler}

redis.host=${spring.redis.host}
redis.port=${spring.redis.port}
redis.timeout=${spring.redis.timeout}
redis.password=${spring.redis.password}
```

画面10的crawler.properties内容：
```properties
# windows
webdriver.chrome.driver=D:/develop/chromedriver_win32/chromedriver.exe
# linux
webdriver.chrome.driver=/usr/local/bin/chromedriver

proxy.get.url=http://www.85ip.cn/qp.html?api=1&num=50&port=80&address=BISP
proxy.validate.url=http://www.ipip.net/
proxy.isUsedProxy=true

csdn.comment.url=https://blog.csdn.net/#!/phoenix/comment/list/{id}/{page}#size=10
crux.cookie.name=acw_sc_v2

crawler.init.url.prefix=https://www.csdn.net/nav/
crawler.init.url.suffix=Java,web,arch,db,mobile,ops,sec,cloud,engineering,iot,fund,career
crawler.help.nextPagingSize=10

# 更新时间
crawler.nextupdatehours=4,16,64,128,256
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“5 导入 heima-leadnews-crawler 项目”，小节标题“6.1 初始化URL的获取”。
画面3：IDEA界面中显示“Invalid VCS root mapping”错误提示。
画面4：IDEA中显示项目结构，包含多个模块，如“heima-leadnews-admin”、“heima-leadnews-api”等。
画面5：IDEA中显示“heima-leadnews-crawler”模块的pom.xml文件内容。
画面6：IDEA中显示“spring-cloud-starter-netflix-Eureka-client”依赖配置。
画面7：IDEA中显示“spring-boot-starter-test”依赖配置。
画面8：IDEA中显示项目结构，选中“src”目录下的“main”和“test”目录。
画面9：IDEA中显示“application.properties”文件内容。
画面10：IDEA中显示“crawler.properties”文件内容。
画面11：IDEA中选中“CrawlerConfig.java”文件。
画面12：IDEA中选中“process”包下的“Process.java”文件。
画面13：IDEA中选中“process”包下的“Process.java”文件。
画面14：IDEA中选中“process”包下的

