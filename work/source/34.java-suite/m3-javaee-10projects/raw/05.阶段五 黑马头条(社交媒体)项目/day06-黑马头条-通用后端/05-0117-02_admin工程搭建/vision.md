# 画面线理解：02_admin工程搭建

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\02_admin工程搭建【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:34, 01:03, 01:18, 01:44, 02:03, 02:25, 02:47, 03:00, 03:22, 03:51, 04:11, 04:28, 05:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:58:44

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中创建并配置 admin 端项目，实现登录功能，包括搭建模块、配置文件、主程序和安全配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT，标题为“admin端功能开发&通用后端封装”，目标包括完成 admin 登录、通用后端封装和熟悉开发流程。
画面 2: 在 IntelliJ IDEA 中，弹出“New Module”对话框，准备创建新模块，父模块为 `com.heima.heima-leadnews:1.0-SNAPSHOT`。
画面 3: 编辑 `pom.xml` 文件，显示父模块配置，`artifactId` 为 `heima-leadnews-admin`，`version` 为 `1.0-SNAPSHOT`。
画面 4: 编辑 `pom.xml` 文件，显示 `dependencies` 部分，引入 `heima-leadnews-model`、`heima-leadnews-common` 和 `heima-leadnews-api` 依赖。
画面 5: 编辑 `application.properties` 文件，配置 `server.port=8080` 和 `spring.application.name=sn.admin`。
画面 6: 在 `heima-leadnews-common` 模块的 `application.properties` 文件中，同样配置 `server.port=8080` 和 `spring.application.name=sn.admin`。
画面 7: 在项目结构中选中 `heima-leadnews-common` 模块，准备进行后续操作。
画面 8: 在 `heima-leadnews-admin` 模块中，弹出“Create New Class”对话框，准备创建 `AdminApplication` 类。
画面 9: 编辑 `AdminApplication.java` 文件，显示 Spring Boot 主类代码，包含 `@SpringBootApplication` 注解和 `main` 方法。
画面 10: 在 `AdminApplication.java` 文件中，右键选择“Run”选项，准备运行程序。
画面 11: 在项目结构中，选中 `heima-leadnews-behavior` 模块，准备进行后续操作。
画面 12: 编辑 `IntConfig.java` 文件，显示 `@Configuration` 注解和 `@ComponentScan` 注解，扫描包 `com.heima.common.common.init`。
画面 13: 在项目结构中，选中 `heima-leadnews-media` 模块，准备进行后续操作。
画面 14: 编辑 `SecurityConfig.java` 文件，显示 `@Configuration` 注解和 `@ComponentScan` 注解，扫描包 `com.heima.common.web.admin.security`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>heima-leadnews</artifactId>
        <groupId>com.heima</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>heima-leadnews-admin</artifactId>
</project>
```

画面 4:
```xml
<dependencies>
    <!-- 引入依赖 -->
    <dependency>
        <groupId>com.heima</groupId>
        <artifactId>heima-leadnews-model</artifactId>
    </dependency>
    <dependency>
        <groupId>com.heima</groupId>
        <artifactId>heima-leadnews-common</artifactId>
    </dependency>
    <dependency>
        <groupId>com.heima</groupId>
        <artifactId>heima-leadnews-api</artifactId>
    </dependency>
</dependencies>
```

画面 5:
```properties
server.port=8080
spring.application.name=sn.admin
```

画面 6:
```properties
server.port=8080
spring.application.name=sn.admin
```

画面 9:
```java
package com.heima.admin;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AdminApplication {
    public static void main(String[] args) {
        SpringApplication.run(AdminApplication.class, args);
    }
}
```

画面 12:
```java
package com.heima.admin.config;

import org.springframework.context.annotation.ComponentScan;

@Configuration
@ComponentScan("com.heima.common.common.init")
public class IntConfig {

}
```

画面 14:
```java
package com.heima.admin.config;

import org.springframework.context.annotation.ComponentScan;

@Configuration
@ComponentScan("com.heima.common.web.admin.security")
public class SecurityConfig {

}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“admin端功能开发&通用后端封装”，下方列出“今日目标”，包括三个目标：
- 目标一：能够完成admin端的登录功能
- 目标二：能够清晰通用后端的好处
- 目标三：能够完成通用后端的代码开发
- 目标四：熟悉前端的开发流程

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
