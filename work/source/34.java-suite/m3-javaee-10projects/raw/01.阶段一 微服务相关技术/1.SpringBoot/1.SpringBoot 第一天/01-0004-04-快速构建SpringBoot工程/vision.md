# 画面线理解：04-快速构建SpringBoot工程

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\04-快速构建SpringBoot工程_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:42, 01:06, 03:06, 03:42, 04:06, 04:38, 05:06, 05:22, 05:38, 06:20, 06:44, 07:13, 07:24, 08:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:03:24

1) 这一组画面整体在讲如何使用 IntelliJ IDEA 通过 Spring Initializr 创建一个 Spring Boot 项目，并编写一个简单的 RESTful 控制器并运行。

2) 按时间顺序列出每张画面的要点：
画面1：打开 IntelliJ IDEA，显示项目“springboot-helloworld”，运行窗口显示“HelloApplication”已运行。
画面2：点击“New Module”，选择“Spring Initializr”创建 Spring Boot 项目。
画面3：在 Spring Initializr 中选择“Web”依赖。
画面4：显示项目 `pom.xml` 文件，其中包含父依赖和版本信息。
画面5：在 `pom.xml` 中高亮显示 `<build>` 标签内的插件配置。
画面6：显示 `SpringbootinitApplication.java` 文件，包含 `@SpringBootApplication` 注解和 `main` 方法。
画面7：显示 `application.properties` 文件，同时控制台显示 Spring Boot 应用已启动。
画面8：在项目结构中选中 `SpringbootinitApplicationTests.java`，准备编写测试类。
画面9：在 `HelloController.java` 中编写控制器代码，使用 `@RestController` 和 `@RequestMapping` 注解。
画面10：浏览器访问 `http://localhost:8080/hello`，页面显示“hello Spring Boot !”。
画面11：在 IntelliJ IDEA 中，通过“File”菜单打开“Settings”设置。
画面12：在浏览器中搜索“spring.io”，显示搜索结果。
画面13：访问 Spring 官网的“Building an Application with Spring Boot”指南页面。
画面14：在 IntelliJ IDEA 中，显示 `HelloController.java` 文件，代码已编写完成。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面4 `pom.xml`：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.6.RELEASE</version>
        <relativePath/>
    </parent>
    <groupId>com.ithema</groupId>
    <artifactId>springboot-init</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>springboot-init</name>
    <description>demo project for Spring Boot</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
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
</project>
```

画面5 `pom.xml`：
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

画面6 `SpringbootinitApplication.java`：
```java
package com.ithema.springboottinit;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class SpringbootinitApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootinitApplication.class, args);
    }
}
```

画面9 `HelloController.java`：
```java
package com.ithema.springboottinit;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
public class HelloController {
    @RequestMapping("/hello")
    public String hello() {
        return "hello Spring Boot 222!";
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面13：Spring 官网“Building an Application with Spring Boot”页面，包含“Get the Code”区域，提供 HTTPS 和 SSH 两种方式下载代码，以及“Push to Pivotal”按钮。

5) 无。
