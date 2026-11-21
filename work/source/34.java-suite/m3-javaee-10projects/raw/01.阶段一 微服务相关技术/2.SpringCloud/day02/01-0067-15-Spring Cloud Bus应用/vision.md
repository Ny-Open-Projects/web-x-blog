# 画面线理解：15-Spring Cloud Bus应用

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\15-Spring Cloud Bus应用_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:49, 02:45, 04:51, 06:40, 07:16, 08:46, 09:18, 10:06, 11:24, 12:20, 13:35, 14:20, 15:02, 15:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:30:08

1) 这一组画面整体在讲如何通过 Spring Cloud Bus（基于 RabbitMQ）实现配置中心的配置文件热更新，无需重启服务。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程PPT的第14、15、16节标题，其中第15节“Spring Cloud Bus应用”目标是“自动RabbitMQ通过修改码云中的配置文件后发送Post请求实现及时更新用户微服务中的配置项”。
画面2: 展示了IDEA中 config-server 项目的结构，以及其 bootstrap.yml 配置文件内容，包含服务端口、Eureka 注册中心地址等。
画面3: 展示了 config-server 的 application.yml 配置文件，其中定义了 Git 仓库地址、用户名密码、Eureka 注册中心地址等。
画面4: 展示了 Spring Cloud 配置中心的架构图，包含 Git 仓库、配置中心、RabbitMQ、Eureka 以及多个服务实例，箭头表示数据流向。
画面5: 展示了 config-server 的 application.yml 配置文件中 management.endpoint.web.exposure.include 配置项，用于暴露 /bus-refresh 端点。
画面6: 展示了 user-service 的 UserController.java 代码，其中包含一个测试方法 queryById，用于模拟查询用户信息。
画面7: 展示了 user-service 的 UserController.java 代码，其中 queryById 方法中添加了打印配置文件中 name 值的逻辑。
画面8: 展示了浏览器访问 http://127.0.0.1:12000/user/5 的结果，返回了用户信息 JSON 数据。
画面9: 展示了码云（Gitee）上 user-devm.yml 配置文件的内容，包含数据库连接、服务名、Eureka 地址等。
画面10: 展示了课程PPT的第4.6节“Spring Cloud 体系技术综合应用概览”。
画面11: 展示了课程PPT的第15节“Spring Cloud Bus应用”中的“实现步骤”和“小结”，并列出了 config-server 需要添加的依赖。
画面12: 展示了课程PPT的第15节“Spring Cloud Bus应用”中的“小结”，并列出了 user-service 需要添加的依赖。
画面13: 展示了 user-service 的 pom.xml 文件，其中添加了 Spring Cloud Bus 和 RabbitMQ 的依赖。
画面14: 展示了课程PPT的第15节“Spring Cloud Bus应用”中的“实现步骤”和“小结”，并列出了 config-server 需要添加的依赖。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2 bootstrap.yml:
spring:
  config:
    import:
      - classpath:/application.yml
  cloud:
    config:
      server:
        git:
          uri: https://gitee.com/goheima/heima-config.git
          # 配置rabbitmq消息：如果是想与默认值一致则不需要配置
          rabbitmq:
            host: localhost
            port: 5672
            username: guest
            password: guest
      service-url:
        defaultZone: http://127.0.0.1:10086/eureka

画面3 application.yml:
server:
  port: 12000
spring:
  application:
    name: config-server
  cloud:
    config:
      git:
        uri: https://gitee.com/goheima/heima-config.git
        # 配置rabbitmq消息：如果是想与默认值一致则不需要配置
        rabbitmq:
          host: localhost
          port: 5672
          username: guest
          password: guest
      service-url:
        defaultZone: http://127.0.0.1:10086/eureka
      management:
        endpoints:
          web:
            exposure:
              # 暴露触发消息总线的地址
              include: bus-refresh

画面4 架构图无代码。
画面5 application.yml:
management:
  endpoints:
    web:
      exposure:
        # 暴露触发消息总线的地址
        include: bus-refresh

画面6 UserController.java:
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    @Autowired
    private UserService userService;
    private String name;
    @GetMapping("/user")
    public User queryById(Long id) {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return userService.queryById(id);
    }
}

画面7 UserController.java:
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    @Autowired
    private UserService userService;
    private String name;
    @GetMapping("/user")
    public User queryById(Long id) {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("配置文件中的name值：" + name);
        return userService.queryById(id);
    }
}

画面8 无代码。
画面9 user-devm.yml:
server:
  port: ${port:9001}
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/springcloud
    username: root
    password: root
  application:
    name: user-service
  mybatis:
    type-aliases-package: com.itheima.user.pojo
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
      instance:
        prefer-ip-address: true
    ip-address: 127.0.0.1

画面11 config-server 依赖：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-bus</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-stream-binder-rabbit</artifactId>
</dependency>

画面12 user-service 依赖：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-bus</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-stream-binder-rabbit</artifactId>
</dependency>

画面13 pom.xml:
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-bus-rabbit</artifactId>
</dependency>

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面4 架构图结构：
- Git 仓库 → 配置中心（通过“获取”指向）
- 配置中心 → 服务A、服务B、服务X（通过“配置”指向）
- 服务A、服务B、服务X → 本地配置缓存（通过“获取”指向）
- 配置中心 → RabbitMQ（通过“监听”指向）
- RabbitMQ → 服务A、服务B、服务X（通过“监听”指向）
- 服务A、服务B、服务X → 配置中心（通过“注册”指向）
- 配置中心 → Eureka（通过“注册”指向）
- Eureka → 服务A、服务B、服务X（通过“监控”指向）
- 服务A、服务B、服务X → 配置中心（通过“监听配置”指向）
- 配置中心 → 服务A、服务B、服务X（通过“推送、修改”指向）
- 服务A、服务B、服务X → 配置中心（通过“配置中心启动后会缓存到本地”指向）

画面10 标题：4.6 Spring Cloud 体系技术综合应用概览

画面11 标题：15. Spring Cloud Bus应用
内容：
目标：自动RabbitMQ通过修改码云中的配置文件后发送Post请求实现及时更新用户微服务中的配置项
分析：
需求：在码云的git仓库中修改user-dev.yml配置文件，实现不重启user-service的情况下可以及时更新配置文件。
实现步骤：
1. 启动RabbitMQ；
2. 修改配置中心(config-server)；
3. 修改服务提供工程user-service；
4. 测试
小结：
- config server的依赖添加内容
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-bus</artifactId>
  </dependency>
  <dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-stream-binder-rabbit</artifactId>
  </dependency>

画面12 标题：16. Spring Cloud 体系技术综合应用说明
目标：了解Spring Cloud中的Eureka、GateWay、Config、Bus、Feign等技术的综合应用

5) 无。
