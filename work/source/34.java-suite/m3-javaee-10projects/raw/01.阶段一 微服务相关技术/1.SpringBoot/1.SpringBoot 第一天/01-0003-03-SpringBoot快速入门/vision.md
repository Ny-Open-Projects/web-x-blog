# 画面线理解：03-SpringBoot快速入门

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\03-SpringBoot快速入门_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 02:43, 03:10, 03:48, 04:25, 04:58, 05:32, 06:14, 07:34, 07:59, 08:39, 09:05, 09:41, 10:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:00:58

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 IntelliJ IDEA 创建一个 Spring Boot 项目，配置 pom.xml 文件，编写控制器和主类，并启动应用访问 HTTP 接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 标题页，显示“SpringBoot 快速入门”，下方列出“案例：需求”和“案例：实现步骤”。
画面 2: IntelliJ IDEA 中打开的 pom.xml 文件，内容为一个基础的 Maven 项目配置，包含 <groupId>、<artifactId> 和 <version>。
画面 3: 浏览器中打开的 Spring 官方文档页面，展示了一个包含 <parent> 和 <dependencies> 的 pom.xml 示例，其中 <parent> 的 <groupId> 为 org.springframework.boot。
画面 4: 浏览器中 Spring 官方文档页面，展示 <dependencies> 和 <build> 部分，其中 <dependency> 的 <groupId> 为 org.springframework.boot。
画面 5: IntelliJ IDEA 中的 pom.xml 文件，光标位于 <dependencies> 标签内，准备添加依赖。
画面 6: IntelliJ IDEA 中打开的 HelloController.java 文件，光标位于 package com.ithema; 后，准备编写代码。
画面 7: IntelliJ IDEA 中的 HelloController.java 文件，已导入 org.springframework.web.bind.annotation.RequestMapping 和 @RestController 注解。
画面 8: IntelliJ IDEA 中右键点击 HelloController.java，弹出菜单，选择“Run HelloController”。
画面 9: IntelliJ IDEA 中打开的 HelloApplication.java 文件，内容为 Spring Boot 项目的主类，包含 @SpringBootApplication 注解和 main 方法。
画面 10: IntelliJ IDEA 中，点击“Run”按钮，弹出“Run: HelloApplication”对话框。
画面 11: IntelliJ IDEA 中，控制台显示 Spring Boot 应用启动日志，包括 Tomcat 初始化和启动成功信息。
画面 12: 浏览器地址栏输入 localhost，准备访问应用。
画面 13: IntelliJ IDEA 中，控制台显示 Spring Boot 应用已启动，Tomcat 在 8080 端口启动成功。
画面 14: PPT 标题页，显示“小结”，内容为“SpringBoot在创建项目时，使用jar的打包方式。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.ithema</groupId>
    <artifactId>springboot-helloworld</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>myproject</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <!-- Inherit defaults from Spring Boot -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.8.RELEASE</version>
    </parent>
    <!-- Add typical dependencies for a web application -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
    <!-- Package as an executable jar -->
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

画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.ithema</groupId>
    <artifactId>springboot-helloworld</artifactId>
    <version>1.0-SNAPSHOT</version>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.8.RELEASE</version>
    </parent>
    <dependencies>
        <!-- 添加起步依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面 7:
```java
package com.ithema;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
```

画面 9:
```java
package com.ithema;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloApplication {
    public static void main(String[] args) {
        SpringApplication.run(HelloApplication.class, args);
    }
}
```

画面 13:
```java
package com.ithema.controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @RequestMapping("/hello")
    public String hello() {
        return "hello spring Boot !";
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题“SpringBoot 快速入门”，下方两个要点：“案例：需求”和“案例：实现步骤”。
画面 14: PPT 标题“小结”，下方一个要点：“SpringBoot在创建项目时，使用jar的打包方式。”

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
