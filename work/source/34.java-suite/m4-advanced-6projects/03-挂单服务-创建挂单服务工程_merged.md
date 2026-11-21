# 03-挂单服务-创建挂单服务工程 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始去创建挂单服务工程

挂单服务是作为一个独立运行的服务

它的主要功能是要处理用户的现价挂单

部分成交 测单

以及获取挂单状态等相关功能

它在整个交易的处理流程当中

也是作为一个重要的服务

接着我们去工程当中创建挂单服务工程

这里咱们新建一个服务模块New Model

点击Next

服务名称我们叫Bus Stock Pending

点击Next

挂单服务模块就已经创建完成

咱们回到讲习当中

接下来我们要将多环境的配置文件

日制文件 Home构建配置

从其他工程当中拷贝过来做相应修改

然后再去创建它的包结构

以及它的启动类

好 那咱们从已经实现了代码当中

copy多环境的配置文件 日制文件

找到挂单服务

在Resource资源目录下面

我们将配置文件还有日制文件copy进来

放到Bus Stock Pending的Resource目录下面

这些是Splint Boot多环境的版本配置文件

有DEV Product UAD环境

我们侧重是在

DEV开发配置文件的版本

在这个视频当中做实现

让我们来看一下工程的具体配置

在这里是服务的基本配置信息

下面的话是Lockit MQ消费端的配置信息

注意它的Group名称要做区分

这里名称是采用Stock Pending-1

如果说有多个挂单服务节点

按序号以此类推

订阅的主题为Stock Quota

这些是Lockit MQ的Name Server的服务地址信息

下面是多数据源的配置文件

这个是业务数据源

下面是Ladies的缓存配置

Splint分布式搜索在这里没有用到

可以将它去除

下面是JPA的功能配置文件

然后是MyBetis的配置

这个是GRPC调用配置信息

它调用资金服务的配置

这里调用的是资金服务配置信息

资金服务目前还没有实现

在后面章节

是GDP配置信息的配置信息

实现的过程当中

咱们再做相应的配置

这里可以先把它去除掉

最后就是现任词的配置信息

这个是日制配置文件

接下来咱们再将依赖导入进来

从讲义当中

Hobby Home的依赖

放置在Stockpending的Home文件下面

让它导入生效

这里是多环境的版本配置信息

我们最主要的来看一下

是什么样的依赖

这里有Splitbook的依赖信息

Marcus的服务注册发现的依赖

这个是实体的依赖

Lockit MQ的消息组件依赖信息

以及自动化缓存配置信息

以及自动化缓存配置依赖信息

下面是GRPC的服务依赖

因为咱们挂单服务

是需要提供限价委托的接口

由交易服务去调用挂单服务

所提供的GRPC接口

实现限价委托订单的处理

那咱们还是需要加上

刚才的GRPC服务端的配置信息

在DV的工程配置下面

我们增加GRPC的服务端配置

GRPC Server Port

端口为1996

提供好服务端的配置就可以了

接下来咱们再去创建对应的包

以及启动类New Package

我们先把包创建好

com.idcast

bus

stock

pending

下面我们创建它纸包

openintomino

make dir

config

这个是配置目录

do数据层接口

GRPC

make grpc

这个是实现GRPC的服务端接口

我们把刚才的GRP这个目录删除掉

再创建MQ包

MQ里面是订阅获取推送的行情数据

再创建service业务处理层

创建启动类的包

最后再创建一个vorder包

这里面会存储一些封装的参数对象

用于咱们的service层交互处理

好接着咱们创建启动类

new

gelcast

名称就叫stocker

pending

application

创建启动方法

psvm

spring

application.run

传递当前的class

将参数对象传递进去

然后是spring boot application的注写

再加上enable discovery client的注写

然后是包入进的扫描

company.scan

base.packages

扫描咱们的基础包

com.idcast

好这个就是启动配置类的实现

那咱们回到讲习当中

这里咱们就实现了挂单服务的搭建

以及它的基础配置

我们添加了它必要的依赖

像消息兑电

LockedMQ的依赖

Ladies

GRPC等相关的依赖组件

最后添加了对应的启动配置类

好

那这一讲内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析：

---

### 1) 视频摘要

本视频是“交易平台”系列课程的第15天，主题为“挂单服务工程的搭建与配置”。讲师通过IDEA开发工具，演示了如何从零开始创建一个名为 `stock-pending` 的独立微服务工程。该服务主要负责处理用户的限价挂单、部分成交、撤单及获取挂单状态等核心业务。视频内容涵盖了工程初始化、POM依赖配置、多环境配置文件（`bootstrap.yml`）、日志配置文件（`logback-spring.xml`）、数据库连接池配置、gRPC服务配置以及线程池配置等关键环节。讲师强调了从现有工程中拷贝配置文件的实践方法，并展示了如何通过 `SpringApplication.run` 启动服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开场，展示课程大纲和学习目标，明确本节内容为“创建挂单服务工程”。
*   **00:05 - 00:15**: 讲师在IDEA中创建名为 `stock-pending` 的新项目，并展示其标准的Maven项目结构，包括 `src/main/java` 和 `src/main/resources` 目录。
*   **00:15 - 00:25**: 讲师说明将从其他工程（如 `bulls-stock-deal`）中拷贝配置文件，包括 `pom.xml`、多环境配置文件（`bootstrap-*.yml`）和日志配置文件（`logback-spring.xml`）。
*   **00:25 - 00:35**: 讲师在 `pom.xml` 中添加Spring Boot依赖，并开始配置项目依赖。
*   **00:35 - 00:45**: 讲师配置 `bootstrap-dev.yml` 文件，设置服务端口、Nacos服务发现地址、RocketMQ消费端配置等。
*   **00:45 - 00:55**: 讲师配置 `bootstrap-dev.yml` 文件中的数据库连接池参数，如 `initial-size`, `maxActive`, `maxWait` 等。
*   **00:55 - 01:05**: 讲师配置 `logback-spring.xml` 文件，设置日志输出到控制台（ConsoleAppender）。
*   **01:05 - 01:15**: 讲师继续在 `pom.xml` 中添加 `spring-cloud-starter-stream-rabbitmq` 和 `spring-boot-starter-data-redis` 等依赖。
*   **01:15 - 01:25**: 讲师配置 `bootstrap-dev.yml` 文件中的gRPC服务配置，设置端口为 `19996`。
*   **01:25 - 01:35**: 讲师在终端中执行命令，创建 `mq` 和 `service` 目录。
*   **01:35 - 01:45**: 讲师展示 `StockPendingApplication.java` 的主类代码，其中使用了 `@SpringBootApplication`、`@EnableDiscoveryClient` 注解，并调用 `SpringApplication.run` 方法启动服务。
*   **01:45 - 01:55**: 讲师切换到课程文档，进入下一章节“挂单服务双数据源配置”，为后续内容做铺垫。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   **第1章：挂单服务工程搭建配置**，包含子章节：目标、步骤、实现（3.1 创建挂单服务工程，3.2 双数据源配置等）。
    *   **3.1 创建挂单服务工程**：描述了挂单服务作为独立服务的功能。
    *   **3.2 挂单服务双数据源配置**：说明了挂单服务需要处理多个数据源。

*   **代码关键内容**:
    *   **项目结构**:
        *   `src/main/java/com.itcast.trade.stock.pending`：Java源码包。
        *   `src/main/resources/bootstrap.yml`：主配置文件。
        *   `src/main/resources/bootstrap-dev.yml`：开发环境配置文件。
        *   `src/main/resources/bootstrap-prd.yml`：生产环境配置文件。
        *   `src/main/resources/bootstrap-uat.yml`：预发布环境配置文件。
        *   `src/main/resources/logback-spring.xml`：日志配置文件。
        *   `pom.xml`：项目依赖管理文件。
    *   **配置文件内容**:
        *   `bootstrap-dev.yml`:
            ```yaml
            server:
              port: 10696
            spring:
              application:
                name: stock-pending
              cloud:
                discovery:
                  server-addr: 127.0.0.1:8848
                config:
                  server-addr: 127.0.0.1:8848
            stream:
              bindings:
                quote:
                  consumer:
                    concurrency: 10
                    maxAttempts: 1
                    content-type: application/json
                    destination: stock-quote
            ```
        *   `bootstrap-dev.yml` (数据库配置):
            ```yaml
            url: jdbc:postgresql://192.168.19.150:5432/trade_stock
            # 连接池的配置信息
            initial-size: 5
            minIdle: 5
            maxActive: 20
            maxWait: 60000
            timeBetweenEvictionRunsMillis: 60000
            minEvictableIdleTimeMillis: 30000
            validationQuery: SELECT 1
            testWhileIdle: true
            testOnBorrow: false
            testOnReturn: false
            poolPreparedStatements: true
            maxPoolPreparedStatementPerConnectionSize: 20
            ```
        *   `logback-spring.xml`:
            ```xml
            <configuration debug="false">
              <springProperty scope="context" name="APP_NAME" source="spring.application.name"/>
              <springProperty scope="context" name="APP_PORT" source="server.port"/>
              <springProperty scope="context" name="DEFAULT_APP_PORT" source="spring.application.port"/>
              <property name="OS_NAME" value="${os.name}"/>
              <property name="LOG_PATH" value="${user.home}/logs"/>
              <property name="LOG_MAX_HISTORY" value="30"/>
              <property name="FILE_LOG_PATTERN" value="%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"/>
              <property name="CONSOLE_LOG_PATTERN" value="%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"/>
              <appender name="STDOUT" class="ch.qos.logback.classic.ConsoleAppender">
                <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
                  <pattern>${CONSOLE_LOG_PATTERN}</pattern>
                </encoder>
              </appender>
            </configuration>
            ```
        *   `pom.xml` (依赖部分):
            ```xml
            <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-web</artifactId>
            </dependency>
            <dependency>
              <groupId>org.springframework.cloud</groupId>
              <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
            </dependency>
            <dependency>
              <groupId>org.springframework.cloud</groupId>
              <artifactId>spring-cloud-starter-stream-rabbitmq</artifactId>
            </dependency>
            <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-data-redis</artifactId>
            </dependency>
            <dependency>
              <groupId>com.itcast.trade</groupId>
              <artifactId>bulls-stock-struct-proto</artifactId>
              <version>${project.stock.version}</version>
            </dependency>
            ```
        *   `StockPendingApplication.java`:
            ```java
            @SpringBootApplication
            @EnableDiscoveryClient
            @ComponentScan(basePackages = {"com.itcast"})
            public class StockPendingApplication {
                public static void main(String[] args) {
                    SpringApplication.run(StockPendingApplication.class, args);
                }
            }
            ```

---

### 4) 关键场景与演示描述

*   **场景一：工程创建与结构展示** (00:05-00:15)
    *   讲师在IDEA中创建名为 `stock-pending` 的新项目。
    *   展示了标准的Maven项目结构，包括 `src/main/java` 和 `src/main/resources` 目录。
    *   强调了后续将从其他工程拷贝配置文件。

*   **场景二：配置文件拷贝与修改** (00:15-01:25)
    *   讲师在 `pom.xml` 中添加Spring Boot依赖
