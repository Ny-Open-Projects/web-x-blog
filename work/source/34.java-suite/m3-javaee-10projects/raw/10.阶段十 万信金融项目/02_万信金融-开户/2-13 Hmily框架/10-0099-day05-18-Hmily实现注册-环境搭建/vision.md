# 画面线理解：day05-18-Hmily实现注册-环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-18-Hmily实现注册-环境搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 02:39, 02:46, 04:04, 04:50, 05:20, 05:31, 05:46, 05:57, 06:04, 06:13, 06:22, 06:37, 06:46, 06:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:09:22

1) 这一组画面整体在讲什么（一句话）：
讲解如何使用 Hmily 框架解决用户注册功能中的分布式事务问题，包括环境搭建、依赖配置和相关服务的 POM 文件修改。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“4.1 业务回顾”，包含一个流程图，描述用户中心、统一账号服务之间的交互流程。
画面2：展示 PPT 页面“4.2 Hmily环境搭建”，包含“数据库环境”和“Maven环境”两个部分，其中数据库环境给出创建数据库的 SQL 语句，Maven环境给出 Hmily 依赖的 XML 配置。
画面3：展示 PPT 页面“4.2 Hmily环境搭建”，继续展示 Maven 依赖配置，包含对 spring-boot-starter、logback-core、slf4j-api 等依赖的排除配置。
画面4：展示 PPT 页面“4.2 Hmily环境搭建”，继续展示 Maven 依赖配置，包含对 ch.qos.logback、slf4j-api、logback-classic 等依赖的排除配置。
画面5：展示 PPT 页面“4.2 Hmily环境搭建”，继续展示 Maven 依赖配置，包含对 esotericsoftware、logback、slf4j-api 等依赖的排除配置。
画面6：展示 PPT 页面“4.2 Hmily环境搭建”，继续展示 Maven 依赖配置，包含对 esotericsoftware、logback、slf4j-api 等依赖的排除配置。
画面7：展示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 `warningzp-account-service` 项目，包含 `apollo-client` 依赖。
画面8：展示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 `warningzp-account-service` 项目，包含 `rocketmq-spring-boot-starter` 依赖。
画面9：展示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 `warningzp-account-service` 项目，包含 `spring-boot-starter-test` 依赖。
画面10：展示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 `warningzp-account-service` 项目，包含 `spring-cloud-starter-xxl-eureka-client` 依赖。
画面11：展示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 `warningzp-account-service` 项目，包含 `spring-boot-maven-plugin` 插件配置。
画面12：展示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 `warningzp-consumer-service` 项目，包含 `spring-cloud-starter-xxl-eureka-client` 依赖。
画面13：展示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 `warningzp-consumer-service` 项目，包含 `guava` 和 `gson` 依赖。
画面14：展示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 `warningzp-consumer-service` 项目，包含 `spring-retry` 依赖。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：无代码或配置。
画面2：
CREATE DATABASE `p2p_undo_log` CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
画面3：
<dependency>
    <groupId>org.dromara</groupId>
    <artifactId>hmily-springCloud</artifactId>
    <version>2.0.5-RELEASE</version>
    <exclusions>
        <exclusion>
            <artifactId>spring-boot-starter</artifactId>
            <groupId>org.springframework.boot</groupId>
        </exclusion>
        <exclusion>
            <artifactId>spring-boot-starter-test</artifactId>
            <groupId>org.springframework.boot</groupId>
        </exclusion>
        <exclusion>
            <artifactId>logback-core</artifactId>
            <groupId>ch.qos.logback</groupId>
        </exclusion>
        <exclusion>
            <artifactId>slf4j-api</artifactId>
            <groupId>org.slf4j</groupId>
        </exclusion>
        <exclusion>
            <artifactId>logback-classic</artifactId>
            <groupId>ch.qos.logback</groupId>
        </exclusion>
    </exclusions>
</dependency>
画面4：
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <exclusions>
        <exclusion>
            <artifactId>logback-core</artifactId>
            <groupId>ch.qos.logback</groupId>
        </exclusion>
        <exclusion>
            <artifactId>slf4j-api</artifactId>
            <groupId>org.slf4j</groupId>
        </exclusion>
        <exclusion>
            <artifactId>logback-classic</artifactId>
            <groupId>ch.qos.logback</groupId>
        </exclusion>
    </exclusions>
</dependency>
画面5：
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <exclusions>
        <exclusion>
            <artifactId>logback-core</artifactId>
            <groupId>ch.qos.logback</groupId>
        </exclusion>
        <exclusion>
            <artifactId>slf4j-api</artifactId>
            <groupId>org.slf4j</groupId>
        </exclusion>
        <exclusion>
            <artifactId>logback-classic</artifactId>
            <groupId>ch.qos.logback</groupId>
        </exclusion>
    </exclusions>
</dependency>
画面6：
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <exclusions>
        <exclusion>
            <artifactId>logback-core</artifactId>
            <groupId>ch.qos.logback</groupId>
        </exclusion>
        <exclusion>
            <artifactId>slf4j-api</artifactId>
            <groupId>org.slf4j</groupId>
        </exclusion>
        <exclusion>
            <artifactId>logback-classic</artifactId>
            <groupId>ch.qos.logback</groupId>
        </exclusion>
    </exclusions>
</dependency>
画面7：
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
</dependency>
画面8：
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
</dependency>
画面9：
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
画面10：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-xxl-eureka-client</artifactId>
</dependency>
画面11：
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
画面12：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-xxl-eureka-client</artifactId>
</dependency>
画面13：
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
</dependency>
<dependency>
    <groupId>com.google.guava</groupId>
    <artifactId>guava</artifactId>
</dependency>
画面14：
<dependency>
    <groupId>org.springframework.retry</groupId>
    <artifactId>spring-retry</artifactId>
</dependency>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“4.用Hmily解决注册功能的分布式事务问题”，子标题“4.1 业务回顾”。流程图中：
- “调用方/APP” 指向 “用户中心”。
- “用户中心” 指向 “统一账号服务”。
- “统一账号服务” 指向 “用户中心”。
- “用户中心” 指向 “调用方/APP”。
画面2：PPT 标题为“4.2 Hmily环境搭建”，包含“数据库环境”和“Maven环境”两个部分。
画面3：PPT 标题为“4.2 Hmily环境搭建”，继续展示“Maven环境”部分。
画面4：PPT 标题为“4.2 Hmily环境搭建”，继续展示“Maven环境”部分。
画面5：PPT 标题为“4.2 Hmily环境搭建”，继续展示“Maven环境”部分。
画面6：PPT 标题为“4.2 Hmily环境搭建”，继续展示“Maven环境”部分。
画面7：无 PPT 标题，展示 IntelliJ IDEA 中的 `pom.xml` 文件。
画面8：无 PPT 标题，
