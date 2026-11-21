# 画面线理解：05-SpringBoot自动配置-Enable注解原理

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\05-SpringBoot自动配置-Enable注解原理_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:37, 03:14, 04:00, 04:42, 04:59, 05:43, 06:16, 07:30, 08:45, 10:58, 11:41, 12:25, 13:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 08:54:01

1) 这一组画面整体在讲什么（一句话）：
演示 Spring Boot 中 @Enable* 注解的原理，通过创建示例项目、配置类和主类，展示如何使用 @ComponentScan 和 @Import 注解来实现自动装配和组件扫描。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IDEA 项目结构，选中 com.ithema.springbootcondition 包，准备创建或修改相关代码。
画面 2: PPT 标题页，显示“SpringBoot 自动配置”和“@Enable*注解”，说明本节内容。
画面 3: 在 IDEA 中创建新模块，选择 Spring Boot 2.1.8 版本，准备构建项目。
画面 4: 在 IDEA 中通过“Project Structure”菜单创建新模块，选择依赖项。
画面 5: 显示项目 pom.xml 文件内容，包含 Spring Boot Starter Parent 和 Spring Boot Starter Web 依赖。
画面 6: 在 IDEA 中编辑 pom.xml 文件，显示 Spring Boot Starter Web 依赖。
画面 7: 显示 UserConfig.java 文件内容，包含 @Configuration 注解和类定义。
画面 8: 显示 pom.xml 文件内容，包含 Spring Boot Maven Plugin 依赖。
画面 9: 显示 SpringbootEnableApplication.java 文件内容，包含 @ComponentScan 注解和 main 方法，运行后报错“没有名为 'user' 的 bean”。
画面 10: 显示 SpringbootEnableApplication.java 文件内容，修改 @ComponentScan 扫描包路径，运行后成功启动。
画面 11: 显示 SpringbootEnableApplication.java 文件内容，添加 @Import 注解导入 UserConfig 类，运行后成功启动。
画面 12: 显示 EnableUser.java 文件内容，包含 @Import 注解导入 UserConfig 类，运行后成功启动。
画面 13: 显示 SpringbootEnableApplication.java 文件内容，添加 @Import 注解导入 UserConfig 类，运行后成功启动。
画面 14: 显示 Import.java 文件内容，包含 @Import 注解的源码，说明其作用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ithema</groupId>
    <artifactId>springboot-enable-other</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>springboot-enable-other</name>
    <description>Domain project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
    </dependencies>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.5.8.RELEASE</version>
        <relativePath/>
    </parent>
</project>
```

画面 8:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>com.ithema</groupId>
        <artifactId>springboot-enable-other</artifactId>
        <version>0.0.1-SNAPSHOT</version>
    </dependency>
</dependencies>

<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

画面 10:
```java
package com.ithema.springbootenable;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.ithema.config")
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        Object user = context.getBean("user");
        System.out.println(user);
    }
}
```

画面 11:
```java
package com.ithema.springbootenable;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.ithema.config")
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        Object user = context.getBean("user");
        System.out.println(user);
    }
}
```

画面 12:
```java
package com.ithema.config;

import org.springframework.context.annotation.Import;

@Import(UserConfig.class)
public class EnableUser {
}
```

画面 14:
```java
package org.springframework.context.annotation;

import java.lang.annotation.*;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface Import {

    Class<?>[] value();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题页，标题为“SpringBoot 自动配置”，副标题为“@Enable*注解”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
