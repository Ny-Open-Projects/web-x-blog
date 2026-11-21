# 画面线理解：day02-7-测试统一账户微服务

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-7-测试统一账户微服务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:02, 01:43, 02:21, 03:04, 04:29, 05:06, 06:29, 06:58, 07:21, 08:23, 09:47, 10:22, 10:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:17:10

1) 这一组画面整体在讲如何使用 Apollo 配置中心为微服务项目（account-service 和 gateway-server）配置并管理运行时参数，包括在 IDE 中编写代码、配置文件、启动服务并验证配置生效。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示 Apollo 配置中心界面，展示 account-service 项目下多个配置项（如 micro_service.spring-boot-http, micro_service.spring-eureka 等），当前环境为 DEV。
画面 2: 显示 IntelliJ IDEA 项目结构，选中 consumer-service 模块，展示其目录结构。
画面 3: 显示 IntelliJ IDEA 项目结构，选中 account-service 模块，展示其 resources 目录下的配置文件（apollo-env.properties, application.yml, log4j2-dev.xml）。
画面 4: 显示 SwaggerConfiguration.java 代码，其中定义了 Swagger API 文档的配置，包括 title 和 description。
画面 5: 显示 AccountController.java 文件，光标位于 @author 注释行。
画面 6: 显示 AccountController.java 文件，光标位于 @Api 注解行，准备添加或修改注解。
画面 7: 显示 AccountController.java 文件，添加了 @Api 和 @GetMapping 注解，并定义了 hello 方法。
画面 8: 显示 Run/Debug Configurations 界面，配置了 Wanning2pAccountServiceApplication 的启动参数，包括环境变量 -Denv=dev -Dapollo.cluster=DEFAULT -Dserver.port=8080。
画面 9: 显示控制台日志，显示服务启动成功，包括 Tomcat 初始化和 Spring Boot 启动信息。
画面 10: 显示浏览器地址栏，输入 localhost:8070 并访问 Apollo 配置中心。
画面 11: 显示浏览器访问 http://localhost:8080/account/hello，页面内容模糊，但可见部分文本。
画面 12: 显示 IntelliJ IDEA 中 gateway-server 项目的 application.yml 配置文件，内容包括 app、apollo、spring 等配置。
画面 13: 显示 Apollo 配置中心界面，展示 gateway-server 项目下的 application 配置项，包括 zuul.routes.* 等配置。
画面 14: 显示 IntelliJ IDEA 中 gateway-server 项目的 application.yml 配置文件，内容与画面 12 相同，但下方显示了控制台日志，包含服务器启动和路由信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 4:
```java
public class SwaggerConfiguration {
    @Bean
    public Docket buildDocket() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(buildApiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("cn.itcast.wanning2p"))
                .paths(PathSelectors.any())
                .build();
    }

    private ApiInfo buildApiInfo() {
        Contact contact = new Contact(name: "黑马程序员", url: "", email: "");
        return new ApiInfoBuilder()
                .title("万信金融P2P平台-用户服务API文档")
                .description("包含...服务api")
                .contact(contact)
                .version("1.0.0")
                .build();
    }
}
```

画面 5:
```java
package cn.itcast.wanning2p.account.controller;

/**
 * @author
 * @since 2019/7/20
 */
public class AccountController {

}
```

画面 6:
```java
package cn.itcast.wanning2p.account.controller;

import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "统一账户服务的API")
public class AccountController {

}
```

画面 7:
```java
package cn.itcast.wanning2p.account.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "统一账户服务的API")
public class AccountController {

    @ApiOperation("测试")
    @GetMapping("/hello")
    public String hello() {
        return "hello";
    }
}
```

画面 8:
```
Name: Wanning2pAccountServiceApplication
Main class: cn.itcast.wanning2p.account.Wanning2pAccountServiceApplication
Environment: -Denv=dev -Dapollo.cluster=DEFAULT -Dserver.port=8080
```

画面 12:
```yaml
app:
  id: gateway-server
apollo:
  bootstrap:
    enabled: true
    namespaces: application,micro_service.spring-boot-http,micro_service.spring-eureka,micro_service.spring-hystrix,micro_service.spring-ribbon,micro_service.spring-boot-druid
spring:
  application:
    name: gateway-server
logging:
  config: classpath:log4j2-dev.xml
```

画面 13:
| Key | Value | 备注 | 最后修改人 | 最后修改时间 |
| --- | --- | --- | --- | --- |
| zuul.routes.consumer-service.stripPrefix | false |  | apollo | 2019-07-20 17:28:27 |
| zuul.routes.account-service.stripPrefix | false |  | apollo | 2019-07-20 17:28:27 |
| zuul.routes.account-service.path | /account/** |  | apollo | 2019-07-20 17:28:27 |
| zuul.add-host-header | true |  | apollo | 2019-07-20 17:28:27 |
| zuul.ignoredServices | * |  | apollo | 2019-07-20 17:28:27 |

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
