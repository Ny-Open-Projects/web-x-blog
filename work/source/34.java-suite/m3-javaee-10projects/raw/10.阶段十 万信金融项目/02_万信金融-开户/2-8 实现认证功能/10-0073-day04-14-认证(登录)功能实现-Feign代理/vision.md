# 画面线理解：day04-14-认证(登录)功能实现-Feign代理

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-14-认证(登录)功能实现-Feign代理_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:31, 02:37, 02:43, 02:47, 03:08, 03:22, 03:58, 04:05, 04:24, 04:29, 05:17, 05:28, 05:34, 06:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:50:07

1) 这一组画面整体在讲如何通过 Spring Cloud 的 Feign 客户端实现微服务间的远程调用，具体演示了在 UAA 服务中定义接口、在账户服务中实现接口、以及在 UAA 服务中启动 Feign 客户端以调用账户服务的流程。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了“4. 认证(登录)功能实现”的需求分析流程图，图中包含“网关API”、“用户中心服务”、“OAM认证服务”、“账户服务”等模块，以及它们之间的调用关系，如“网关API”调用“用户中心服务”，“用户中心服务”调用“OAM认证服务”和“账户服务”等。
画面 2: 在 IDEA 中显示了项目结构，选中了“wanningzp-uaa-service”模块。
画面 3: 在 IDEA 中显示了“wanningzp-uaa-service”模块的资源目录，其中包含“pom.xml”、“wanningzp-uaa-service.iml”等文件。
画面 4: 在 IDEA 中右键点击“wanningzp-uaa-service”模块，弹出菜单，选中“New” -> “Interface”。
画面 5: 在 IDEA 中打开“AccountApiAgent.java”文件，显示了接口定义的初始状态。
画面 6: 在 IDEA 中“AccountApiAgent.java”文件中，光标位于接口定义处。
画面 7: 在 IDEA 中切换到“wanningzp-account-service”模块，选中“agent”包。
画面 8: 在 IDEA 中显示“AccountController.java”文件，其中包含“register”和“login”两个方法的定义。
画面 9: 在 IDEA 中“AccountController.java”文件中，光标位于“login”方法的注解上。
画面 10: 在 IDEA 中“AccountApiAgent.java”文件中，光标位于“@FeignClient”注解的值上。
画面 11: 在 IDEA 中“AccountApiAgent.java”文件中，光标位于“@PostMapping”注解的值上。
画面 12: 在 IDEA 中显示“Warning2pAccountServiceApplication.java”文件，其中包含“@SpringBootApplication”、“@EnableDiscoveryClient”、“@MapperScan”等注解。
画面 13: 在 IDEA 中显示“UAAService.java”文件，其中包含“@SpringBootApplication”、“@EnableDiscoveryClient”、“@EnableFeignClients(basePackages = “cn.itcast.wanningzp.uaa.agent”)”等注解。
画面 14: 在 IDEA 中“UAAService.java”文件中，光标位于“@EnableFeignClients”注解的值上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 7:
```java
package cn.itcast.wanningzp.account;
import org.springframework.cloud.openfeign.FeignClient;
@FeignClient(value = "account-service")
public interface AccountApiAgent {
}
```

画面 8:
```java
@ApiOperation("用户注册")
@ApiOperation("用户登录")
public RestResponse<AccountDTO> register(@RequestBody AccountRegisteredDTO accountRegisteredDTO) {
    return RestResponse.success(accountService.register(accountRegisteredDTO));
}

@ApiOperation("用户登录")
@ApiOperation("用户登录")
public RestResponse<AccountDTO> login(@RequestBody AccountLoginDTO accountLoginDTO) {
    return RestResponse.success(accountService.login(accountLoginDTO));
}
```

画面 10:
```java
@FeignClient(value = "account-service")
```

画面 11:
```java
@PostMapping(value = "/accounts/session")
```

画面 12:
```java
@SpringBootApplication
@EnableDiscoveryClient
@MapperScan("cn.itcast.wanningzp.account.mapper")
public class Warning2pAccountServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(Warning2pAccountServiceApplication.class, args);
    }
}
```

画面 13:
```java
@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients(basePackages = "cn.itcast.wanningzp.uaa.agent")
public class UAAService {
    public static void main(String[] args) {
        SpringApplication.run(UAAService.class, args);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PPT 标题为“4. 认证(登录)功能实现”，流程图中“网关API”指向“用户中心服务”，“用户中心服务”指向“OAM认证服务”和“账户服务”，“账户服务”指向“OAM认证服务”，“OAM认证服务”指向“网关API”。

5) 不要评价画面美观，不要输出与课程无关的内容。
