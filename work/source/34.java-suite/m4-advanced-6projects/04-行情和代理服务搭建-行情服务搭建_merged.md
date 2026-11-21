# 04-行情和代理服务搭建-行情服务搭建 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就开始创建行情服务

在代码工程当中咱们右键

新建一个模块

点击Next

模块名称我们叫bus

stock

quad

点击Next

好,Finish

让它导入生效

工程模块创建完成之后

接着咱们添加它的依赖

咱们从讲义当中将依赖copy进去

放在BOM文件下面

我们看一下在这里加入了哪些依赖

首先的话引进的是SlimBoot依赖

然后是Nakos服务注射发现的依赖

接着是咱们的公用数据层

工具组件

实体的依赖

然后是LockitMQ的依赖

自动化缓存

在这里面也用到了缓存的处理

接着就是多环境版本的配置

这个之前咱们讲解了如何去配置和使用

下面

是打包的一个构建配置

按照SlimBoot插件去生成可执行的SlimBoot的加包

好,BOM依赖配置完成之后

接着我们还要去引进它的多环境配置文件

以及日志配置文件

这一块咱们之前是做过讲解

在这里就不再赘述

我们直接从已经实现的代码当中去copy进来

这是已经实现过的代码

那咱们呢

将它的配置文件以及日志文件引入进来

好

copy完成之后咱们放到工程代码当中

放在Resource目录下面

咱们来大概看一下Foodstrap

下面是它的多环境版本配置

在这里指定的是环境变量

根据咱们的需要

可以指定不同的环境变量去运行

然后是LockitBank的配置文件

这里面是配置日志的输出信息

好

咱们回到讲义当中

依赖添加完成之后咱们要注意一下

要去修改Build里面的Final Name

也就在这里面我们是引入进来了

在Build标签下面有个Final Name

这个名称的话咱们跟模块名称最好保持一致

要和其他应用服有一个区分

下面就是它的多环境的表示

然后咱们是增加了Food相关的一些依赖

工程当中也需要用到缓存以及LockitMQ

通信功能

这里我们就增加了LockitMQ

以及StreetMap Ladies的依赖

好

在这里就是对行情服务的创建和配置

这里讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频是关于一个名为 `bulls-stock` 的股票行情系统的技术实现教程，重点讲解了如何从零开始创建一个名为 `stock-quote` 的 Spring Boot 服务模块。课程内容涵盖了项目初始化、依赖管理、多环境配置文件的引入、日志配置文件的编写，以及如何通过 Maven 插件进行资源复制和打包。整个过程旨在构建一个具备高数据安全性和可靠性的行情服务，能够支持快速稳定的分发。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 开场，展示课程大纲，当前章节为“3.2 创建行情服务”，并介绍目标是新建 `stock-quote` 工程。
*   **00:05 - 00:15**: 展示 `stock-quote` 项目的目录结构，包括 `src/main/java` 和 `src/main/resources` 文件夹。
*   **00:15 - 00:30**: 讲解第一步，引入多环境配置文件（`bootstrap.yml`, `bootstrap-dev.yml`, `bootstrap-uat.yml`）。
*   **00:30 - 00:45**: 讲解第二步，引入日志配置文件 `logback-spring.xml`。
*   **00:45 - 01:00**: 讲解第三步，修改 `pom.xml` 依赖文件，增加 Spring Boot 和 Nacos 依赖。
*   **01:00 - 01:15**: 展示 `pom.xml` 中的依赖配置，包括 Spring Boot Web、Nacos 服务发现等。
*   **01:15 - 01:30**: 展示 `pom.xml` 中的公共工具组件和实体类依赖。
*   **01:30 - 01:45**: 展示 `pom.xml` 中的多环境配置部分，定义了 `dev` 和 `uat` 两个 profile。
*   **01:45 - 02:00**: 展示 `pom.xml` 中的 Maven 插件配置，用于复制资源文件。
*   **02:00 - 02:15**: 展示 `logback-spring.xml` 的配置内容，包括控制台和文件日志输出。
*   **02:15 - 02:30**: 展示 `bootstrap.yml` 的配置内容，定义了应用端口、日志路径等。
*   **02:30 - 02:45**: 讲解 `pom.xml` 中的 `build` 配置，修改 `finalName` 与工程名一致，并增加 RocketMQ 和 Spring Data Redis 依赖。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.2 创建行情服务”。
    *   **步骤列表**: 1. 新建 `stock-quote` 工程；2. 引进多环境配置文件；3. 引进日志配置文件；4. 引进 `pom` 依赖文件。
    *   **关键说明**: “注意修改 `build->finalName`，与工程名一致。增加 Spring Boot、Nacos 与公用组件依赖。工程需要缓存与队列功能，这里增加 RocketMQ 与 Spring Data Redis 的依赖。”

*   **代码关键内容**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <!-- Spring Boot 依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- Nacos 服务注册发现依赖 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>

        <!-- 公共工具组件依赖 -->
        <dependency>
            <groupId>com.icast.trade</groupId>
            <artifactId>bulls-stock-common-utils</artifactId>
            <version>${project.stock.version}</version>
        </dependency>

        <!-- 实体类依赖 -->
        <dependency>
            <groupId>com.icast.trade</groupId>
            <artifactId>bulls-stock-entity</artifactId>
            <version>${project.stock.version}</version>
        </dependency>

        <!-- 多环境配置 -->
        <profiles>
            <profile>
                <id>dev</id>
                <activation>
                    <activeByDefault>true</activeByDefault>
                </activation>
                <properties>
                    <package.environment>dev</package.environment>
                </properties>
            </profile>
            <profile>
                <id>uat</id>
                <properties>
                    <package.environment>uat</package.environment>
                </properties>
            </profile>
        </profiles>

        <!-- Maven 插件配置 -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-resources-plugin</artifactId>
            <executions>
                <execution>
                    <goals>
                        <goal>copy-resources</goal>
                    </goals>
                    <configuration>
                        <outputDirectory>${project.build.outputDirectory}</outputDirectory>
                        <useDefaultDelimiters>false</useDefaultDelimiters>
                        <delimiters>
                            <delimiter>${*}</delimiter>
                        </delimiters>
                        <resources>
                            <resource>
                                <directory>src/main/resources</directory>
                            </resource>
                        </resources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
        ```

    *   **`logback-spring.xml` 日志配置**:
        ```xml
        <configuration>
            <!-- 控制台输出 -->
            <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
                <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
                    <pattern>%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n</pattern>
                </encoder>
            </appender>

            <!-- 按照每天生成日志文件 -->
            <appender name="FILE_INFO" class="ch.qos.logback.core.rolling.RollingFileAppender">
                <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
                    <level>INFO</level>
                </filter>
                <file>${LOG_PATH}/${APP_NAME}/info.log</file>
                <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
                    <fileNamePattern>${LOG_PATH}/${APP_NAME}/info.%d{yyyy-MM-dd}.log</fileNamePattern>
                    <maxHistory>30</maxHistory>
                </rollingPolicy>
                <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
                    <pattern>%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n</pattern>
                </encoder>
            </appender>
        </configuration>
        ```

    *   **`bootstrap.yml` 配置**:
        ```yaml
        server:
          port: 8080

        logging:
          file: ${LOG_PATH}/log.log
          pattern: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
          max-history: 30

        spring:
          application:
            name: bulls-stock-quote
          cloud:
            nacos:
              config:
                server-addr: 127.0.0.1:8848
              discovery:
                server-addr: 127.0.0.1:8848
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与目录结构展示** (00:00-00:15)
    *   讲师在 IntelliJ IDEA 中打开 `bulls-stock` 项目，展示 `stock-quote` 模块的目录结构。
    *   重点演示了 `src/main/resources` 目录下的配置文件，包括 `bootstrap.yml`、`bootstrap-dev.yml`、`bootstrap-uat.yml` 和 `logback-spring.xml`。

*   **场景二：`pom.xml` 依赖管理** (00:30-01:45)
    *   讲师在 IDEA 中打开 `stock-quote` 模块的 `pom.xml` 文件。
    *   依次演示了如何添加 Spring Boot Web、Nacos 服务发现、公共工具组件和实体类的依赖。
    *   展示了如何配置多环境（`dev` 和 `uat`）的 profile。
    *   演示了如何配置 Maven 插件，用于在打包时复制资源文件。

*   **场景三：日志配置文件 `logback-spring.xml`** (01:45-02:15)
    *   讲师在 IDEA 中打开 `logback-spring.xml` 文件。
    *   详细讲解了配置文件中定义的两个 appender：一个用于控制台输出，另一个用于按天
