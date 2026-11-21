# 画面线理解：05-搭建zuul运行环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\05-搭建zuul运行环境_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:54, 01:17, 02:06, 03:25, 03:52, 04:35, 05:28, 06:09, 07:32, 08:27, 09:17, 09:43, 10:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:12:21

1) 这一组画面整体在讲什么（一句话）：
创建并配置一个基于 Spring Cloud 的 Zuul 网关服务（ihrm_gate），包括工程搭建、启动类编写和配置文件设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在课程 PPT 中展示“1.3.1 工程搭建”章节，内容为创建工程 ihrm_gate 并导入 zuul 依赖，显示了 Maven 依赖配置片段：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-zuul</artifactId>
</dependency>
```

画面2：在文件资源管理器中，显示了项目目录结构，包含 `ihrm_gate` 文件夹，内含 `application.yml` 和 `pom.xml` 文件。

画面3：在 IntelliJ IDEA 中打开 `pom.xml` 文件，显示了工程的依赖配置，包括 Spring Cloud Zuul、Spring Boot Actuator、MySQL Connector、以及自定义模块 ihrm_common 的依赖。

画面4：在 IntelliJ IDEA 中右键点击项目 `ihrm_gate`，弹出菜单，选中“Replace in Path...”选项，准备进行路径替换操作。

画面5：在 IntelliJ IDEA 中打开 `GateApplication.java`，显示了空的 `main` 方法，光标位于 `public static void main(String[] args) {` 行。

画面6：在 IntelliJ IDEA 中编辑 `GateApplication.java`，添加了 Spring Boot 启动注解 `@SpringBootApplication`。

画面7：在 IntelliJ IDEA 中编辑 `GateApplication.java`，添加了 Zuul 网关注解 `@EnableZuulProxy`。

画面8：在 IntelliJ IDEA 中打开 `application.yml` 文件，显示了服务配置和 Spring 配置的注释，光标位于第 10 行。

画面9：在 IntelliJ IDEA 中编辑 `application.yml`，在第 10 行添加了 `zuul:` 配置项。

画面10：在 IntelliJ IDEA 中编辑 `application.yml`，在 `zuul:` 下添加了 `routes:` 配置，定义了 `ihrm-company` 的路由规则。

画面11：在 IntelliJ IDEA 中编辑 `application.yml`，在 `ihrm-company` 的路由规则中，将 `url` 设置为 `http://127.0.0.1:9001`。

画面12：在 IntelliJ IDEA 中，光标位于 `GateApplication.java` 的 `main` 方法中，准备编写启动代码。

画面13：在 IntelliJ IDEA 中打开 `pom.xml` 文件，显示了父工程 `ihrm_parent` 的配置，以及 `ihrm_gate` 模块的依赖，包括 `spring-cloud-starter-netflix-eureka-client`。

画面14：在 IntelliJ IDEA 的终端中，显示了 `GateApplication` 启动后的日志，包括 Zuul 初始化器启动、端点暴露等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-zuul</artifactId>
</dependency>
```

画面3：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-zuul</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
<dependency>
    <groupId>com.ihrm</groupId>
    <artifactId>ihrm_common</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```

画面6：
```java
import org.springframework.boot.autoconfigure.SpringBootApplication;
```

画面7：
```java
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
```

画面8：
```yaml
#服务配置
server:
  port: 9000
#spring配置
spring:
  application:
    name: ihrm-gate #指定服务名
```

画面9：
```yaml
zuul:
```

画面10：
```yaml
zuul:
  routes:
    ihrm-company:
```

画面11：
```yaml
zuul:
  routes:
    ihrm-company:
      url: http://127.0.0.1:9001
```

画面13：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“1.3 快速入门”，子标题“1.3.1 工程搭建”。

画面8：PPT 展示了三个图表，分别是“无标题 - 建图”、“无标题 - 图表”、“无标题 - 表格”，但未显示具体内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
