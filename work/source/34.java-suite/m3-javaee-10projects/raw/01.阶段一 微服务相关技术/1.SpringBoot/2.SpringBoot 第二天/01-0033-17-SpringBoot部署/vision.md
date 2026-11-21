# 画面线理解：17-SpringBoot部署

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\17-SpringBoot部署_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:44, 02:30, 03:17, 03:54, 04:35, 05:10, 06:12, 06:54, 07:44, 08:23, 08:53, 09:44, 10:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:05:52

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Maven 将 SpringBoot 项目打包成 jar 和 war 两种格式并部署运行。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 标题页，说明 SpringBoot 项目部署支持 jar 和 war 两种方式。
画面 2: 在 IDEA 中展示项目结构，选中 springboot-deploy 模块，准备进行打包。
画面 3: 在 IDEA 中打开 UserController.java，展示其代码内容。
画面 4: 在 IDEA 中展示 Maven 编译日志，显示项目已成功编译。
画面 5: 展示桌面，有一个名为 "project" 的文件夹。
画面 6: 在浏览器中访问 localhost:8080/user/findAll，页面显示百度首页。
画面 7: 在 IDEA 中展示 Maven 打包日志，显示正在构建 jar 包。
画面 8: 在 IDEA 中展示 SpringBootServiceInitializer 类的代码，显示其构造函数。
画面 9: 在 IDEA 中展示 pom.xml 文件，显示 <packaging>jar</packaging>。
画面 10: 在 IDEA 中展示 pom.xml 文件，显示 <packaging>war</packaging>。
画面 11: 在 Windows 命令行中运行 jar 包，显示 SpringBoot 启动日志。
画面 12: 在命令行中运行 war 包，显示 SpringBoot 部署日志。
画面 13: 在 Windows 资源管理器中展示 apache-tomcat-8.5.46 的 WEB-INF/classes 目录，包含 application.properties 文件。
画面 14: 在 IDEA 中展示 pom.xml 文件，显示 <packaging>war</packaging>，并显示 Maven 打包成功日志。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
SpringBoot 项目开发完毕后，支持两种方式部署到服务器：
① jar包(官方推荐)
② war包

画面 2:
Name: springboot-deploy
Sources: src/main/java
Test Resources: src/test/resources

画面 3:
package com.ithema.springbootdeploy;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RequestMapping("/user")
@RestController
public class UserController {

画面 4:
[INFO] --- maven-resources-plugin:3.0.1:testResources (default-testResources) @ springboot-deploy ---
[INFO] Using UTF-8 encoding to copy filtered resources
[INFO] skip non existing resourcesDirectory
[INFO] --- maven-compiler-plugin:3.0.1:testCompile (default-testCompile) @ springboot-deploy ---
[INFO] Changes detected - recompiling the module...
[INFO] Compiling 1 source file to E:\workspace\springboot02\springboot-deploy\target\test-classes
[INFO] --- maven-surefire-plugin:2.22.1:test (default-test) @ springboot-deploy ---
[INFO] T T T T S
[INFO] Running com.ithema.springbootdeploy.SpringbootDeployApplicationTests

画面 7:
[INFO] --- maven-jar-plugin:3.1.2:jar (default-jar) @ springboot-deploy ---
[INFO] Building jar: E:\workspace\springboot02\springboot-deploy\target\springboot-deploy-0.0.1-SNAPSHOT.jar
[INFO] --- spring-boot-maven-plugin:2.1.0.RELEASE:repackage (repackage) @ springboot-deploy ---
[INFO] Replacing main artifact with repackaged archive

画面 8:
public class SpringBootServiceInitializer {
    public SpringBootServiceInitializer() {
        SpringApplication application = new SpringApplication(SpringbootDeployApplication.class, args);
        application.run(args);
    }
}

画面 9:
<packaging>jar</packaging>

画面 10:
<packaging>war</packaging>

画面 11:
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SwaggerAutoConfiguration on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication in 2.009 seconds (JVM running for 4.448)
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication in 2.009 seconds (JVM running for 4.448)
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication in 2.009 seconds (JVM running for 4.448)
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication in 2.009 seconds (JVM running for 4.448)
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.S
