# 05-行情和代理服务搭建-代理服务搭建 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始创建代理服务

回到代码工程当中

咱们新建一个模块new model

点击next

给它一个名称

bus

stock

proxy

点击next

点击finish

让它导入生效

在这里面可以看到咱们新创建的代理服务模块

代理服务要做哪些配置呢

咱们回到讲习当中

它和行情服务一致

要引进多环境配置文件

日制配置文件

并且要将相关的依赖引入进来

咱们就从之前实现好的代码当中

做一个copy引进

找到代理服务工程

bus.stock.proxy

让它resource下面的配置文件

copy进来

回到咱们的代码工程当中

放置resource目录下面

这里面也涉及到多环境版本的配置

一个是dev

一个是uat

下面是它的日制配置文件

接着咱们还将它的依赖copy进来

从之前的实现代码当中引入进来

在proxy下面的form文件

点击查看文件

咱们从defenses下面做一个copy

让它导入生效

copy完成咱们看一下它有哪些依赖呢

在这里和航行服基本上是一致的

它需要有spring boot依赖

nux服注册发现

以及咱们公用封装的一些工程

包括数据层组件

工具组件

然后实体的一些依赖

自动化缓存

locked mq

以及我们基于latis实现了缓存封装

再往下面就是多环境版本的一个配置

这里面的话有涉及到dev

还有uat

以及product的生产环境

最下面的build标记表格

是整体的打包构件配置

对于这个模块名称

我们要跟其他用户区分开来

这个就是跟咱们的工程模块名称保持一致

前对build咱们就不用再加入进去

通过stock开头的话

就能够区分出来

那么代理服务也已经创建完成

接着咱们先把它的包创建一下

这包就叫comitcast.boss

stock.proxy

我们先创建它的复集包

点击ok

好

后面代码实验过程当中呢

咱们再去做一个具体的创建

那这一讲呢

咱们就完成了代理服务的搭建和配置

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock-proxy` 的 Spring Cloud 代理服务项目的创建与配置过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何从一个压缩包中解压项目、导入 Maven 项目、配置多环境的 `bootstrap.yml` 文件、以及在 `pom.xml` 中引入必要的依赖（如 Nacos 服务发现、RocketMQ 消息、Redis 缓存等）。整个过程旨在为后续的行情服务开发打下基础，强调了配置文件和依赖管理在微服务架构中的重要性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 开场，展示项目结构和 `pom.xml` 文件，介绍 `finalName` 的配置。
*   **00:05 - 00:15**: 导入 Maven 项目，展示 `pom.xml` 的顶层结构和 `parent` 依赖。
*   **00:15 - 00:25**: 展示 `pom.xml` 中的 `dependencies` 部分，引入 Spring Boot Web、Nacos 服务发现、RocketMQ、Redis 等依赖。
*   **00:25 - 00:35**: 配置 `profiles`，定义 `dev`、`uat`、`prd` 三个环境，并设置 `package.environment` 属性。
*   **00:35 - 00:45**: 配置 `maven-resources-plugin`，设置资源文件的输出目录。
*   **00:45 - 00:55**: 展示 `bootstrap.yml` 文件内容，配置服务名、Nacos 地址、RocketMQ 消费者参数等。
*   **00:55 - 01:05**: 总结，强调项目结构和配置文件的标准化。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: `3.3 创建代理服务` 和 `3.4 生成行情服务的实体`。
    *   **关键步骤**: 1. 创建 `stock-proxy` 工程；2. 引入多环境配置文件、日志配置文件及相关依赖。

*   **代码关键内容**:
    *   **`pom.xml` - 项目依赖**:
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-stream-rabbitmq</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        ```
    *   **`pom.xml` - 多环境配置**:
        ```xml
        <profiles>
            <profile>
                <id>dev</id>
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
            <profile>
                <id>prd</id>
                <properties>
                    <package.environment>prd</package.environment>
                </properties>
            </profile>
        </profiles>
        ```
    *   **`pom.xml` - Maven 插件配置**:
        ```xml
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-resources-plugin</artifactId>
            <executions>
                <execution>
                    <id>default-resources</id>
                    <phase>validate</phase>
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
                                <directory>src/main/resources/</directory>
                            </resource>
                        </resources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
        ```
    *   **`bootstrap.yml` - 配置文件**:
        ```yaml
        server:
          port: 10693
        spring:
          application:
            name: stock-quote
          cloud:
            nacos:
              server-addr: 127.0.0.1:8848
            config:
              server-addr: 127.0.0.1:8848
        # RocketMQ 消费配置
        stream:
          bindings:
            quote:
              consumer:
                # 并发数
                concurrency: 10
                # 最大尝试次数
                maxAttempts: 1
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理**
    *   讲师首先在 IDEA 中打开一个名为 `bulls-stock-proxy` 的项目，展示了其 `pom.xml` 文件。
    *   他重点讲解了 `finalName` 配置，用于控制打包后的 jar 文件名。
    *   接着，他展示了 `pom.xml` 中的 `parent` 配置，说明了项目继承的父模块。

*   **场景二：引入服务依赖**
    *   讲师在 `pom.xml` 的 `<dependencies>` 部分，依次添加了 `spring-boot-starter-web`、`spring-cloud-starter-alibaba-nacos-discovery`、`spring-cloud-starter-stream-rabbitmq` 和 `spring-boot-starter-data-redis` 等依赖。
    *   他特别强调了 `spring-cloud-starter-stream-rabbitmq` 用于消息队列，`spring-boot-starter-data-redis` 用于缓存。

*   **场景三：配置多环境**
    *   讲师在 `pom.xml` 中配置了 `<profiles>`，定义了 `dev`、`uat`、`prd` 三个环境。
    *   他解释了 `properties` 中的 `package.environment` 属性，用于在不同环境下区分打包的版本。

*   **场景四：配置资源文件**
    *   讲师配置了 `maven-resources-plugin` 插件，设置了资源文件的输出目录为 `${project.build.outputDirectory}`。
    *   他解释了 `useDefaultDelimiters` 和 `delimiters` 的作用，用于处理资源文件中的占位符。

*   **场景五：配置 `bootstrap.yml`**
    *   讲师展示了 `bootstrap.yml` 文件，配置了服务端口、Nacos 地址、以及 RocketMQ 的消费者参数。
    *   他强调了 `spring.cloud.nacos.config.server-addr` 和 `spring.cloud.nacos.discovery.server-addr` 的配置，用于连接 Nacos 服务注册与配置中心。

*   **场景六：项目结构与总结**
    *   讲师展示了项目的目录结构，包括 `src/main/resources` 下的 `bootstrap-dev.yml`、`bootstrap-uat.yml`、`bootstrap-prd.yml` 等多环境配置文件。
    *   他总结了本节的主要内容，强调了配置文件和依赖管理在微服务项目中的重要性。
