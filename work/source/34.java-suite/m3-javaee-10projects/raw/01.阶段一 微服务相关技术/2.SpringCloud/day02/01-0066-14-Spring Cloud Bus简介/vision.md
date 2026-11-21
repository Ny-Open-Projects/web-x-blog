# 画面线理解：14-Spring Cloud Bus简介

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\14-Spring Cloud Bus简介_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:42, 01:25, 01:59, 02:37, 02:53, 03:00, 03:11, 03:26, 03:44, 03:53, 05:24, 06:03, 07:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:29:16

1) 这一组画面整体在讲如何通过 Spring Cloud Config 配置中心实现服务的动态配置管理，并演示了配置文件的结构、配置项的修改以及配置刷新的流程。

2) 按时间顺序列出每张画面的要点：
画面1：在码云（Gitee）上查看 user-dev.yml 配置文件，内容包含 application、mybatis、eureka、client、instance、test 等配置项，其中 service-url 指向 Eureka 服务，instance 的 ip-address 设置为 127.0.0.1。
画面2：在码云上编辑 user-dev.yml，光标位于 test 配置块下的 name 字段，准备修改配置。
画面3：在 IntelliJ IDEA 中查看 UserApplication9091 项目的结构，展示 UserController.java 中的 queryById 方法，该方法调用 userService。
画面4：在 IntelliJ IDEA 中，UserController.java 的 queryById 方法中添加了 System.out.println 语句，用于打印 test.name 的值。
画面5：在码云上查看 user-dev.yml 配置文件，内容与画面1相同。
画面6：在 IntelliJ IDEA 中查看 bootstrap.yml 文件，其中 spring.cloud.config 配置块包含 name、profile、label、discovery、enabled、service-id 等配置项，service-id 设置为 config-server。
画面7：在码云上查看 user-dev.yml 配置文件，内容与画面1相同。
画面8：在 IntelliJ IDEA 中，UserApplication9091 服务启动成功，控制台输出日志显示服务注册到 Eureka，配置中心初始化完成。
画面9：在浏览器中访问 http://127.0.0.1:9091/user/5，返回 JSON 格式的用户信息，其中 name 字段值为“张三”。
画面10：在 IntelliJ IDEA 中，UserApplication9091 服务启动成功，控制台输出日志显示服务注册到 Eureka，配置中心初始化完成。
画面11：在 IntelliJ IDEA 中，UserApplication9091 服务启动成功，控制台输出日志显示服务注册到 Eureka，配置中心初始化完成。
画面12：在 PowerPoint 中展示 Spring Cloud 配置中心架构图，图中显示：用户通过 /actuator/bus-refresh 接口推送修改，配置中心（Config Server）从 git 仓库（github/gitee）获取配置，注册中心（Eureka）注册服务，服务A、B、X 从配置中心获取配置，配置中心会将配置推送到本地配置缓存。
画面13：在 PowerPoint 中展示 Spring Cloud 配置中心架构图，图中显示：用户通过 /actuator/bus-refresh 接口推送修改，配置中心（Config Server）从 git 仓库（github/gitee）获取配置，注册中心（Eureka）注册服务，服务A、B、X 从配置中心获取配置，配置中心会将配置推送到本地配置缓存。
画面14：在 Typora 中查看文档，标题为“14. Spring Cloud Bus简介”和“15. Spring Cloud Bus应用”，内容涉及 Spring Cloud Bus 的作用和应用方式。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
```yaml
application:
  name: user-service
mybatis:
  type-aliases-package: com.ithema.user.pojo
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
  instance:
    # 更改可使用ip地址，而不是host名
    prefer-ip-address: true
    # ip地址
    ip-address: 127.0.0.1
    # 端口配置，自定义端口
    port: 9091
    # 租约失效时间，默认30秒
    lease-renewal-interval-in-seconds: 5
    # 租约最大时间，默认90秒
    lease-expiration-duration-in-seconds: 5
test:
  name: "zhangsan"
```

画面2：
```yaml
test:
  name: "zhangsan"
  username: "zhangsan"
```

画面3：
```java
package com.ithema.user.controller;
import com.ithema.user.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping("/user/{id}")
    public User queryById(@PathVariable Long id) {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return userService.queryById(id);
    }
}
```

画面4：
```java
package com.ithema.user.controller;
import com.ithema.user.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping("/user/{id}")
    public User queryById(@PathVariable Long id) {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("配置文件中的test.name为：" + test.name);
        return userService.queryById(id);
    }
}
```

画面5：
```yaml
server:
  port: 9091
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/springcloud
    username: root
    password: root
  application:
    name: user-service
  mybatis:
    type-aliases-package: com.ithema.user.pojo
  eureka:
    client:
      service-url:
        defaultZone: http://127.0.0.1:10086/eureka
    instance:
      # 更改可使用ip地址，而不是host名
      prefer-ip-address: true
      # ip地址
      ip-address: 127.0.0.1
      # 端口配置，自定义端口
      port: 9091
      # 租约失效时间，默认30秒
      lease-renewal-interval-in-seconds: 5
      # 租约最大时间，默认90秒
      lease-expiration-duration-in-seconds: 5
  test:
    name: "zhangsan"
```

画面6：
```yaml
spring:
  cloud:
    config:
      # 要点仓库中的配置文件的application同名一块
      name: user
      # 要点仓库中的配置文件的profile保持一致
      profile: dev
      # 要点仓库中的配置文件所属的版本（分支）一样
      label: master
      discovery:
        # 启用配置中心
        enabled: true
        # 配置中心服务名
        service-id: config-server
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
```

画面7：
```yaml
server:
  port: 9091
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/springcloud
    username: root
    password: root
  application:
    name: user-service
  mybatis:
    type-aliases-package: com.ithema.user.pojo
  eureka:
    client:
      service-url:
        defaultZone: http://127.0.0.1:10086/eureka
    instance:
      # 更改可使用ip地址，而不是host名
      prefer-ip-address: true
      # ip地址
      ip-address: 127.0.0.1
      # 端口配置，自定义端口
      port: 9091
      # 租约失效时间，默认30秒
      lease-renewal-interval-in-seconds: 5
      # 租约最大时间，默认90秒
      lease-expiration-duration-in-seconds: 5
  test:
    name: "zhangsan"
```

画面8：
```yaml
spring:
  cloud:
    config:
      name: user
      profile: dev
      label: master
      discovery:
        enabled: true
        service-id: config-server
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
```

画面9：
```json
{
  "id": 5,
  "username": "zhangsan",
  "password": "123456",
  "age": 21,
  "name": "张三",
  "birthday": "2000-07-07T16:30:00.000+0000",
  "created": "2014-05-20T03:41:15.000+0000",
  "updated": "201
