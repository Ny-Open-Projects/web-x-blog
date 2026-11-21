# 画面线理解：13-SpringBoot配置-项目外部配置加载顺序

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\13-SpringBoot配置-项目外部配置加载顺序_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:46, 01:39, 02:33, 03:14, 03:31, 04:52, 06:03, 06:36, 07:14, 08:34, 09:49, 10:38, 11:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:32:46

1) 这一组画面整体在讲什么（一句话）：
演示 Spring Boot 外部配置文件的加载顺序和配置方式，包括通过官网文档、IDEA 项目结构、命令行参数和文件系统路径等手段进行配置管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 页面，标题为“外部配置加载顺序”，并提供官方文档链接：https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html。
画面 2: 官方文档页面，展示 Spring Boot 外部配置加载顺序的列表，其中第 1 项为“Devtools global settings properties on your home directory (~/.spring-boot-devtools.properties when devtools is active)”，第 2 项为“TestPropertySource attributes on your tests”，第 3 项为“properties attribute on your tests...”，第 4 项为“Command line arguments”，第 5 项为“Properties from SPRING_APPLICATION_JSON...”，第 6 项为“ServletConfig init parameters”，第 7 项为“ServletContext init parameters”，第 8 项为“JNDI attributes from java:comp/env”，第 9 项为“Java System properties (System.getProperties())”，第 10 项为“OS environment variables”，第 11 项为“A randomValuePropertySource...”，第 12 项为“Profile specific application properties...”，第 13 项为“Profile-specific application properties...”，第 14 项为“Application properties outside your packaged jar...”，第 15 项为“Application properties packaged inside your jar...”，第 16 项为“@PropertySource annotations on your @Configuration classes”，第 17 项为“(Default properties (specified by setting SpringApplication.setDefaultProperties))”。下方示例代码为：
import org.springframework.stereotype.*;
import org.springframework.beans.factory.annotation.*;
画面 3: IDEA 开发环境，显示项目结构，其中包含“application.properties”文件，内容为“server.port=8084”。控制台输出显示 Spring Boot 应用启动成功，端口为 8084。
画面 4: Windows PowerShell 窗口，显示 Spring Boot 应用启动日志，端口为 8084，无活动配置文件，回退到默认配置文件：default。
画面 5: Windows 资源管理器，显示“springboot-config-0.0.1-SNAPSHOT.jar”文件，大小为 16.1 MB，修改时间为 2019-03-12 15:00:00。
画面 6: IDEA 开发环境，显示项目结构，其中包含“application.properties”文件，内容为“server.port=8084”。控制台输出显示 Spring Boot 应用启动成功，端口为 8084。
画面 7: Windows PowerShell 窗口，显示 Spring Boot 应用启动日志，端口为 8084，无活动配置文件，回退到默认配置文件：default。
画面 8: Windows PowerShell 窗口，显示 Spring Boot 应用启动日志，端口为 8082，无活动配置文件，回退到默认配置文件：default。
画面 9: 官方文档页面，展示如何使用 YAML 文件作为配置文件的替代方案，以及如何通过环境变量指定配置文件名和位置。代码示例为：
$ java -jar myproject.jar --spring.config.name=myproject
$ java -jar myproject.jar --spring.config.location=classpath:/default.properties,classpath:/override.properties
画面 10: Windows 资源管理器，显示“application.properties”文件，大小为 1 KB。
画面 11: 官方文档页面，展示如何使用 YAML 文件作为配置文件的替代方案，以及如何通过环境变量指定配置文件名和位置。代码示例为：
$ java -jar myproject.jar --spring.config.name=myproject
$ java -jar myproject.jar --spring.config.location=classpath:/default.properties,classpath:/override.properties
画面 12: Windows 资源管理器，显示“springboot-config-0.0.1-SNAPSHOT.jar”文件，大小为 16.425 KB。下方打开 Windows PowerShell 窗口，提示符为“PS E:\workspace\springboot-config\target>”。
画面 13: Windows PowerShell 窗口，显示 Spring Boot 应用启动日志，端口为 8010，无活动配置文件，回退到默认配置文件：default。
画面 14: PPT 页面，标题为“外部配置加载顺序”，并提供官方文档链接：https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
1 Devtools global settings properties on your home directory (~/.spring-boot-devtools.properties when devtools is active)
2 TestPropertySource attributes on your tests
3 properties attribute on your tests. Available on @SpringBootTest and the test annotations for testing a particular slice of your application
4 Command line arguments
5 Properties from SPRING_APPLICATION_JSON (inline JSON embedded in an environment variable or system property).
6 ServletConfig init parameters
7 ServletContext init parameters
8 JNDI attributes from java:comp/env
9 Java System properties (System.getProperties())
10 OS environment variables
11 A randomValuePropertySource that has properties only in random.*
12 Profile specific application properties outside your packaged jar (application-(profiles).properties and YAML variants)
13 Profile-specific application properties packaged inside your jar (application-(profiles).properties and YAML variants)
14 Application properties outside your packaged jar (application.properties and YAML variants)
15 Application properties packaged inside your jar (application.properties and YAML variants)
16 @PropertySource annotations on your @Configuration classes
17 (Default properties (specified by setting SpringApplication.setDefaultProperties))

下方示例代码为：
import org.springframework.stereotype.*;
import org.springframework.beans.factory.annotation.*;

画面 9:
$ java -jar myproject.jar --spring.config.name=myproject
$ java -jar myproject.jar --spring.config.location=classpath:/default.properties,classpath:/override.properties

画面 11:
$ java -jar myproject.jar --spring.config.name=myproject
$ java -jar myproject.jar --spring.config.location=classpath:/default.properties,classpath:/override.properties

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 和 14: PPT 页面，标题为“外部配置加载顺序”，并提供官方文档链接：https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求完成）
