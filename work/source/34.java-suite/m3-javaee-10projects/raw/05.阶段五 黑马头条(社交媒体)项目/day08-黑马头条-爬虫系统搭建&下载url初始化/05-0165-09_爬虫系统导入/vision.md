# 画面线理解：09_爬虫系统导入

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\09_爬虫系统导入【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:23, 00:39, 00:55, 01:11, 01:41, 01:59, 02:12, 02:27, 02:42, 02:59, 03:29, 03:51, 04:29, 05:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:33:54

1) 这一组画面整体在讲什么（一句话）：
演示如何初始化并配置一个名为“heima-leadnews-crawler”的爬虫项目，包括项目结构、POM文件依赖、配置文件内容及代码结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文件资源管理器中“heima-leadnews-crawler”项目文件夹，包含“chrome-driver_win32.zip”和“heima-leadnews-crawler.zip”两个压缩包，右侧显示PPT标题“5 导入 heima-leadnews-crawler 项目”和小节“6.1 初始化URL的获取”。
画面2：在文件资源管理器中，选中“heima-leadnews-crawler.zip”文件，准备解压。
画面3：在IntelliJ IDEA中打开“heima-leadnews”项目，显示项目结构和Maven Projects面板，提示“Invalid VCS root mapping”。
画面4：在IDEA中打开“heima-leadnews”项目的根目录下的“pom.xml”，显示父模块的配置，包括groupdId、artifactId、version和modules。
画面5：在IDEA中打开“heima-leadnews-crawler”模块的“pom.xml”，显示该模块的父级配置和依赖声明。
画面6：在“pom.xml”中，显示对“spring-cloud-starter-netflix-eureka-client”依赖的配置。
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
        <module>service-myst</module>
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
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
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
画面6：IDEA中显示“spring-cloud-starter-netflix-eureka-client”依赖配置。
画面7：IDEA中显示“spring-boot-starter-test”依赖配置。
画面8：IDEA中显示项目结构，选中“src”目录下的“main”和“test”目录。
画面9：IDEA中显示“application.properties”文件内容。
画面10：IDEA中显示“crawler.properties”文件内容。
画面11：IDEA中选中“CrawlerConfig.java”文件。
画面12：IDEA中选中“process”包下的“Process.java”文件。
画面13：IDEA中选中“process”包下的“Process.java”文件。
画面14：IDEA中选中“process”包下的
