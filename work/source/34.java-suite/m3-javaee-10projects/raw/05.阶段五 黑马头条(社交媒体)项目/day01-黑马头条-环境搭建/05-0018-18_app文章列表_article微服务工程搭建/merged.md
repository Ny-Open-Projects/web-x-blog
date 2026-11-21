# 18_app文章列表_article微服务工程搭建

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\18_app文章列表_article微服务工程搭建【海量资源尽在 666java.com】.mp4
- 时长 6分17秒（音频 377s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们继续往下讲啊呃刚才呢咱们是把这个接口啊给大概说了一下然后下面呢咱们要去写代码之前呢还要去创建一个微服务首先咱们要去创建第一个微服务啊这个微服务名称呢就是当前的这个什么黑马力的news articleok那创建的时候呢咱们在这啊直接去在当前的复工程下去拗一个模块就可以啊好往下走好下一步就是一个jar 包
[00:30] 那这时候这个工程就算是建完了首先呢咱们要去把这个坐标信心的给导入进来做坐标咱们直接考过来咱们再来说一下啊先考过考一下那考过来之后呢咱们来简单说一下看看这个坐标都有哪些首先呢第一个呢是咱们要去依赖于其他的模块modelcommonaps是吧还有咱们去加了一个sprintboot的starterweb就是
[01:06] 起步依赖是吧外部的起步依赖然后下面还有啥呢把这些给过滤掉了啊下面还有啥呢下面还有一个只是测试是吧测试的起步依赖还有三个呢这三个呢主要是用于当前的这种什么JSON的一些账包咱们也导入了进来啊行那这个就是咱们这个工程已经打完了然后下面呢咱们还会去再去定义当前的这种包结构和工程啊那这个包结构呢咱们来一块来写一下啊
[01:37] 这工程好像是没有变色是吧看一下啊啊这个如果说没有变色的话呢你可以右键的去把它给忽略掉啊把它不要忽略掉啊好稍等啊刷新一下也行好刷新完之后就没事了啊那这时候呢咱们可以在这去创建包右键谁呢package.com.黑马叫什么article那这个啊跟当前模块要保持一致啊咱们这个模块就要article好
[02:12] 创建完之后呢咱们在这直接就创建一个引导类好吧Article 这Application我们就叫它然后呢咱们写一个漫方法SpringApplication.1然后就是Article.Application.class当然这个要做成引导类的话这必须加个什么Spring.Application
[02:46] 这个导类就算是创建完了啊但是包几个啊咱们还要继续继续做啊咱们需要在当前那个包下面的去创建两个三个包吧第一个呢是叫config所有的配置呢都放到目前这个包下面然后再往下创建啊咱们会创建一个Service咱们的这种业务代码都放到前的Service包下面当前的咱们有一个Controller控制层代码啊叫Controller
[03:17] 好要加一个V1刚才咱们咱们之前前几节课就已经说过了这个control对外暴露的接触咱们都要去加上这个版本号OK那这样的话咱们就算是做完了做完之后这里边还有一些东西你看这这是不是有三个配置文件的OK那这三个配置文件咱们也要去创建咱们之前也讲过这个需要去需要去
[03:45] 多环境的切换啊在当前的项目的根目录下边去创建这文件好你把咱们把内容啊直接考过来就可以了啊这内容啊咱们一会再去解释啊先考过来好呃当然这是一个是吧还要再去创建两个啊考虑一下叫叫provider是吧好然后再往下创建呢是有一个test咱们开发阶段的用最多的是哪个啊这就是test好
[04:16] 那这个创建完之后啊那这里边呢主要呢是当前某一个或者某一些环境下它不同的日志的级别和日志的格式OK那这个啊创建完之后呢咱们里边还要去再去创建一个什么就是两个配置文件嘛第一个是application properties另外一个是log4j2的特别咱们先把这个创建出来啊这两个文件呢在当前resource目录下边创建一个文件
[04:48] 就是log4j2这个呢就是相当于咱们之前用过的log4j的码一样啊好把这个呢粘贴一下这个也不用去写啊也粘贴就可以好那放进去之后呢咱们这个事就算是做完了啊那这里边还要再去创建另外一个publist就是当前项目的一个什么加载的publist好这里边有啥呢好来看一下啊这里边呢咱们主要是定了两个那这两个是啥打开
[05:21] 放着就能知道了这个是当前项目的一个端口号第二个是当前项目的一个应用名称是吧那这个是从哪读的呢这个呢其实在给你们的项目中的comment下面啊这有一个叫config application这里边config无间下下面这个目录下面有一个叫application.properties
[05:45] 这个里面呢就定义好了这些所有的端口号这个呢我建议大家轻易不要动好吧当然这个里面所有用到的微服务名称呢咱们也提好了名字但你也可以改是没有问题的但是这个你要注意后期这个端口号的话你不要重复就可以好吧那行啊那目前的话呢咱们这个环境呢算是搭建完了OK那么下面呢就来去进入一个这种
[06:14] 功能打开吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置 Maven 依赖、项目结构、日志配置和数据库配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，讲解如何创建一个名为 heima-leadnews-article 的 Maven 模块，并配置其父工程为 heima-leadnews。
画面2：展示 pom.xml 文件中定义的依赖，包括 spring-boot-starter-web、spring-boot-starter-test、jackson-dataformat-xml 等。
画面3：在 pom.xml 中编辑依赖，高亮显示 artifactId 为 heima-leadnews-api。
画面4：继续编辑 pom.xml，添加了 jackson-dataformat-xml 依赖。
画面5：在 Maven Projects 面板中右键点击项目，选择“Reimport”。
画面6：在 ArticleApplication.java 中输入 package 语句。
画面7：在 ArticleApplication.java 中右键，选择“Run ArticleApplication”。
画面8：在 ArticleApplication.java 中添加了 SpringBootApplication 和 SpringApplication.run() 语句。
画面9：在 maven_test.properties 文件中配置日志级别和格式。
画面10：在 resources 目录下创建 log4j2.xml 文件。
画面11：在 log4j2.xml 文件中输入内容。
画面12：在 application.properties 文件中配置 server.port 和 spring.application.name。
画面13：在 heima-leadnews-common 模块的 application.properties 文件中配置多个服务的端口和名称。
画面14：展示 log4j2.xml 的配置内容和 MysqlConfig 类的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
<dependency>
    <groupId>com.heima</groupId>
    <artifactId>heima-leadnews-api</artifactId>
</dependency>

画面2：
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <!-- 排除默认的logback日志，使用log4j2 -->
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-logging</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j2</artifactId>
        </exclusion>
        <exclusion>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-access</artifactId>
        </exclusion>
    </exclusions>
</dependency>

画面3：
<dependency>
    <groupId>com.heima</groupId>
    <artifactId>heima-leadnews-api</artifactId>
</dependency>

画面4：
<dependency>
    <groupId>com.fasterxml.jackson.dataformat</groupId>
    <artifactId>jackson-dataformat-xml</artifactId>
</dependency>

画面5：
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>

画面6：
package com.heima.article;

画面7：
package com.heima.article;

画面8：
package com.heima.article;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

public class ArticleApplication {
    public static void main(String[] args) {
        SpringApplication.run(ArticleApplication.class, args);
    }
}

画面9：
# log4j
log_level=DEBUG
log_pattern=%d{HH:mm:ss} [%t] %-5level %logger{36} - %msg%n

画面10：
Enter a new file name:
log4j2.xml

画面11：
package com.heima.article;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

public class ArticleApplication {
    public static void main(String[] args) {
        SpringApplication.run(ArticleApplication.class, args);
    }
}

画面12：
server.port=8080
spring.application.name=heima.article

画面13：
port.migration=9012
# 全局hostname配置
hostname.Eureka.server=${hostname.Eureka.server}
# 各服务名称
sn.gateway=gateway
sn.admin-boot-admin-server
sn.login-login
sn.article=article
sn.user=user
sn.media-media
sn.admin-admin
sn.crawler=crawler
sn.quartz-quartz
sn.migration-migration
sn.webocket-WebSocket
sn.images-images

画面14：
<PatternLayout pattern="%c{1} [%t] %-5level %logger{36} - %msg%n"/>
<TimeBasedTriggeringPolicy />
<SizeBasedTriggeringPolicy size="100 MB"/>
</Policies>
</RollingFile>
<appenders>
    <Console name="Console" target="SYSTEM_OUT">
        <PatternLayout pattern="%c{1} [%t] %-5level %logger{36} - %msg%n"/>
    </Console>
    <RollingFile name="RollingFileInfo" fileName="logs/info.log" filePattern="logs/$${date:yyyy-MM-dd}/info-%i.log">
        <PatternLayout pattern="%c{1} [%t] %-5level %logger{36} - %msg%n"/>
        <TimeBasedTriggeringPolicy />
        <SizeBasedTriggeringPolicy size="100 MB"/>
    </RollingFile>
</appenders>
<loggers>
    <logger name="org.springframework" level="INFO"/>
    <logger name="org.mybatis" level="INFO"/>
    <logger name="org.apache.http" level="INFO"/>
    <logger name="org.apache.Kafka" level="INFO"/>
    <logger name="org.hibernate" level="INFO"/>
    <root level="${log.level}">
        <appender-ref ref="Console"/>
        <appender-ref ref="RollingFileInfo"/>
    </root>
</loggers>
</configuration>

mysql初始化配置类com.heima.article.config.MysqlConfig
@ComponentScan("com.heima.common.mysql.core")
public class MysqlConfig {

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面2：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面3：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面4：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面5：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面6：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面7：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面8：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面9：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面10：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面11：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面12：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面13：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。
画面14：PPT标题为“7.3 项目开发”，子标题为“7.3.1 定义pom文件中的依赖信息”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

