# 画面线理解：18_app文章列表_article微服务工程搭建

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\18_app文章列表_article微服务工程搭建【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:41, 01:00, 01:17, 01:43, 02:27, 02:53, 03:43, 04:22, 04:49, 05:04, 05:32, 05:58, 06:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:36:46

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
hostname.eureka.server=${hostname.eureka.server}
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
sn.webocket-websocket
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
    <logger name="org.apache.kafka" level="INFO"/>
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
