# 画面线理解：17-Jaspersoft Studio：整合springboot搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\17-Jaspersoft Studio：整合springboot搭建环境_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:39, 01:08, 01:52, 02:03, 02:15, 02:33, 02:55, 03:03, 03:16, 03:38, 03:57, 04:20, 04:54, 05:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:32:28

1) 这一组画面整体在讲如何使用 Spring Boot 集成 JasperReports 实现报表功能，包括项目初始化、依赖配置、数据库连接配置、主程序编写和报表模板设计。

2) 按时间顺序列出每张画面的要点：
画面1：展示 JasperReports 报表生成三阶段（设计、编译、填充）的流程图，并附带文字说明各阶段作用。
画面2：在 IntelliJ IDEA 中创建新 Maven 项目，选择 Maven 模板。
画面3：在 Windows 资源管理器中浏览项目目录结构，右键点击“day1”文件夹。
画面4：在 IntelliJ IDEA 中打开 `pom.xml` 文件，展示已添加的 JasperReports 依赖。
画面5：在 IntelliJ IDEA 中显示项目结构，`pom.xml` 文件位于 `src/main/resources` 目录下。
画面6：在 IntelliJ IDEA 中打开 `application.yml` 文件，展示数据库连接配置和 JWT 配置。
画面7：在 IntelliJ IDEA 中编辑 `pom.xml` 文件，展示 JasperReports 依赖的版本号。
画面8：在 IntelliJ IDEA 中打开 `pom.xml` 文件，展示 `shiro-spring`、`shiro-core`、`shiro-redis` 等依赖。
画面9：在 IntelliJ IDEA 中编辑 `application.yml` 文件，展示 Spring Boot 的 server 和 datasource 配置。
画面10：在 IntelliJ IDEA 中打开 `JasperApplication.java` 文件，展示主类的包名。
画面11：在 IntelliJ IDEA 中编辑 `JasperApplication.java` 文件，添加 Spring Boot 启动注解。
画面12：在 IntelliJ IDEA 中编辑 `JasperApplication.java` 文件，设置 `@SpringBootApplication(scanBasePackages = "cn.itcast")`。
画面13：在 JasperReports Studio 中打开一个空白报表模板，左侧显示项目结构。
画面14：在 IntelliJ IDEA 中打开 `templates` 目录下的 `JasperApplication.java` 文件。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
无代码或配置。

画面2：
无代码或配置。

画面3：
无代码或配置。

画面4：
```xml
<dependency>
    <groupId>org.olap4j</groupId>
    <artifactId>olap4j</artifactId>
    <version>1.2.0</version>
</dependency>
<dependency>
    <groupId>com.lowagie</groupId>
    <artifactId>itext</artifactId>
    <version>2.1.7</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml-schemas</artifactId>
    <version>4.0.1</version>
</dependency>
</dependencies>
```

画面5：
无代码或配置。

画面6：
```yaml
driver-class-name: com.mysql.jdbc.Driver
url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
username: root
password: 111111
jpa:
  database: MySQL
  show-sql: true
  open-in-view: true
  redis:
    host: 127.0.0.1
    port: 6379
  jut:
    config:
      key: saas-ihrm
      ttl: 3600000
    ai:
      appId: 15191975
      apiKey: cy0SlGac93Vtdm420ublbpU
      secretKey: yf1GusMvLbD0nyuLFubhyOd9LEDEZH
    qr:
      url: http://localhost:8080/#/facelogin
```

画面7：
```xml
<dependency>
    <groupId>org.olap4j</groupId>
    <artifactId>olap4j</artifactId>
    <version>1.2.0</version>
</dependency>
<dependency>
    <groupId>com.lowagie</groupId>
    <artifactId>itext</artifactId>
    <version>2.1.7</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml-schemas</artifactId>
    <version>4.0.1</version>
</dependency>
</dependencies>
```

画面8：
```xml
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-spring</artifactId>
    <version>1.3.2</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.3.2</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-redis</artifactId>
    <version>3.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml-schemas</artifactId>
    <version>4.0.1</version>
</dependency>
</dependencies>
```

画面9：
```yaml
server:
  port: 8081
spring:
  application:
    name: jasper-springboot #指定服务名
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
```

画面10：
无代码或配置。

画面11：
```java
package cn.itcast;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class JasperApplication {
    public static void main(String[] args) {
        SpringApplication.run(JasperApplication.class, args);
    }
}
```

画面12：
```java
package cn.itcast;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = "cn.itcast")
public class JasperApplication {
    public static void main(String[] args) {
        SpringApplication.run(JasperApplication.class, args);
    }
}
```

画面13：
无代码或配置。

画面14：
无代码或配置。

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：
标题：“4.2 JasperReport原理简述”
流程图：设计阶段（MyReport.jrxml）→ 编译阶段（MyReport.jasper）→ 执行阶段（Data）→ 输出阶段（MyReport.pdf）

5) 不要评价画面美观，不要输出与课程无关的内容。
