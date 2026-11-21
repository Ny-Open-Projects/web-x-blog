# 画面线理解：14-SpringBoot监控-actuator基本使用

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\14-SpringBoot监控-actuator基本使用_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:26, 01:21, 01:58, 02:19, 02:56, 03:36, 03:59, 04:27, 05:36, 06:16, 06:35, 07:23, 07:33, 08:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:03:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SpringBoot 项目中集成并使用 Actuator 监控端点，包括添加依赖、配置属性和访问健康检查与信息端点。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 标题页，介绍 SpringBoot 监控概述，说明 Actuator 可用于监控程序内部运行情况。
画面 2: IDEA 中创建新模块，选择初始化服务 URL 为 https://start.spring.io。
画面 3: 显示 pom.xml 文件内容，包含 spring-boot-starter-actuator 依赖和 spring-boot-maven-plugin 插件。
画面 4: 显示 SpringBootActuatorApplication.java 主类，包含 @SpringBootApplication 注解和 main 方法。
画面 5: 浏览器访问 http://localhost:8080/hello，页面显示百度首页，表明应用已启动并能响应请求。
画面 6: 浏览器访问 http://localhost:8080/actuator/info，页面为空白，表示该端点尚未配置或未启用。
画面 7: IDEA 中显示 application.properties 文件内容，包含 info.name 和 info.age 属性，以及 management.endpoint.info.enabled=true。
画面 8: 浏览器访问 http://localhost:8080/actuator/health，页面为空白，表示健康检查端点尚未配置或未启用。
画面 9: IDEA 中显示 application.properties 文件内容，添加了 management.endpoint.health.show-details=always。
画面 10: IDEA 中显示项目结构，展开 src/main/java 和 src/main/resources 目录。
画面 11: IDEA 中显示 pom.xml 文件内容，包含 spring-boot-starter-redis 依赖。
画面 12: 浏览器访问 http://localhost:8080/actuator/health，页面显示 JSON 格式的健康检查信息，包含 diskSpace 和 redis 等组件状态。
画面 13: 浏览器访问 http://localhost:8080/actuator/health，页面显示 JSON 格式的健康检查信息，包含 diskSpace 和 redis 等组件状态。
画面 14: 浏览器访问 http://localhost:8080/actuator，页面显示 JSON 格式的端点列表，包含 health、info、metrics 等端点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
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

画面 7:
```properties
info.name=zhangcan
info.age=2
management.endpoint.info.enabled=true
```

画面 9:
```properties
info.name=zhangcan
info.age=2
# 并且健康检查的详细信息
management.endpoint.health.show-details=always
```

画面 11:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-redis</artifactId>
    </dependency>
</dependencies>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“SpringBoot 监控”，副标题为“SpringBoot 监控概述”，内容说明 Actuator 可用于监控程序内部运行情况。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
