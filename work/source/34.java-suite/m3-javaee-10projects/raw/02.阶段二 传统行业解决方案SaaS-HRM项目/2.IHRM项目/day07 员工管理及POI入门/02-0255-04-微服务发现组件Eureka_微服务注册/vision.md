# 画面线理解：04-微服务发现组件Eureka：微服务注册

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\04-微服务发现组件Eureka：微服务注册_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:48, 01:19, 02:03, 02:47, 02:57, 03:16, 03:25, 03:41, 03:55, 04:09, 04:20, 04:38, 05:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:49:11

1) 这一组画面整体在讲什么（一句话）：
演示如何在微服务架构中，通过配置文件将各个服务注册到 Eureka 服务发现中心，实现服务间的互相调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“1.4.2 微服务注册”，内容说明将所有微服务注册到 Eureka 中，以便互相调用。同时展示了一个 Maven 依赖配置片段：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>

画面 2: 在 IntelliJ IDEA 中，展示项目结构，当前选中的是 `ihrm_company` 模块的 `application.yml` 文件，文件中包含服务配置（如 server.port: 9001）和数据源配置。

画面 3: 在 IntelliJ IDEA 中，展示 `application.yml` 文件，光标位于文件顶部，准备进行编辑。

画面 4: 在 IntelliJ IDEA 中，编辑 `application.yml` 文件，添加了 Eureka 客户端配置：
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8888/eureka/
  server:
    port: 9001

画面 5: 在 IntelliJ IDEA 中，展示 `CompanyApplication.java` 文件，其中包含 Spring Boot 启动类的注解配置：
@EnableEurekaClient
@SpringBootApplication(scanBasePackages = "com.ihrm")
public class CompanyApplication {
    public static void main(String[] args) {
        SpringApplication.run(CompanyApplication.class, args);
    }
}

画面 6: 在 IntelliJ IDEA 中，展示项目结构，选中了 `ihrm_company` 模块，准备进行后续操作。

画面 7: 在 IntelliJ IDEA 中，展示 `ihrm_system` 模块的 `application.yml` 文件，光标位于 `jwt` 配置块附近。

画面 8: 在 Notepad++ 中，展示 `eureka服务的配置文件`，其中包含 Eureka 服务的配置：
#eureka服务的配置文件
server:
  port: 8888 #服务端口
eureka:
  client:
    registerWithEureka: false #是否将自己注册到Eureka服务中，本身就是所有无需注册
    fetchRegistry: false #是否从Eureka中获取注册信息
    serviceUrl:
      defaultZone: http://127.0.0.1:8888/eureka/
#微服务注册到eureka配置
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8888/eureka/

画面 9: 在 IntelliJ IDEA 中，展示 `ihrm_employee` 模块的 `pom.xml` 文件，其中包含 Spring Boot Maven 插件配置：
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <configuration>
        <classifier>exec</classifier>
    </configuration>
</plugin>
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <configuration>
        <mainClass>com.ihrm.employee.EmployeeApplication</mainClass>
        <layout>ZIP</layout>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>repackage</goal>
            </goals>
        </execution>
    </executions>
</plugin>

画面 10: 在 IntelliJ IDEA 中，编辑 `ihrm_employee` 模块的 `application.yml` 文件，添加了 Eureka 客户端配置：
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8888/eureka/
  server:
    port: 9003

画面 11: 在 IntelliJ IDEA 中，展示 `SystemApplication.java` 文件，其中包含 Spring Boot 启动类的注解配置：
@EnableEurekaClient
@SpringBootApplication(scanBasePackages = "com.ihrm")
public class SystemApplication {
    public static void main(String[] args) {
        SpringApplication.run(SystemApplication.class, args);
    }
}

画面 12: 在 IntelliJ IDEA 中，展示 `EmployeeApplication.java` 文件，其中包含 Spring Boot 启动类的注解配置：
@EnableEurekaClient
@SpringBootApplication(scanBasePackages = "com.ihrm")
public class EmployeeApplication {
    public static void main(String[] args) {
        SpringApplication.run(EmployeeApplication.class, args);
    }
}

画面 13: 在 IntelliJ IDEA 中，展示 `EmployeeApplication.java` 文件，其中包含 Spring Boot 启动类的注解配置：
@EnableEurekaClient
@SpringBootApplication(scanBasePackages = "com.ihrm")
public class EmployeeApplication {
    public static void main(String[] args) {
        SpringApplication.run(EmployeeApplication.class, args);
    }
}

画面 14: 在浏览器中，访问 Eureka 服务发现页面，显示已注册的服务实例：
Instances currently registered with Eureka
Application | AMIs | Availability Zones | Status
IHMR-COMPANY | n/a (1) | (1) | UP (1) - localhost:ihrm-company:9001
IHMR-EMPLOYEE | n/a (1) | (1) | UP (1) - localhost:ihrm-employee:9003
IHMR-SYSTEM | n/a (1) | (1) | UP (1) - localhost:ihrm-system:9002

General Info
Name | Value
total-available-memory | 629mb
environment | test
num-of-cpus | 4
current-memory-usage | 147mb (23%)
server-uptime | 03:11
registered-replicas | http://127.0.0.1:8888/eureka/
unavailable-replicas | http://127.0.0.1:8888/eureka/
