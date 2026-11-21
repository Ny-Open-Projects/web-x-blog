# 画面线理解：day05-15-Hmily实现转账-bank1

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-15-Hmily实现转账-bank1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 01:58, 02:31, 04:54, 05:34, 06:17, 06:49, 08:35, 09:42, 12:13, 13:02, 13:52, 14:43, 15:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:07:04

1) 这一组画面整体在讲什么（一句话）：
演示如何在分布式事务场景中，通过 Hmily 框架实现银行转账业务的事务管理，包括配置文件、服务类和主启动类的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的目录结构，当前章节为“3.3.4 功能实现”，子章节“3.3.4.1 hmily-demo-bank1工程”和“(1) application.yml配置（只显示hmily部分）”。
画面 2: 在 IntelliJ IDEA 中打开 `application.yml` 文件，展示 Hmily 相关配置，包括 `registry-fetch-interval-seconds`、`serviceUrl`、`spring.application.name`、`datasource` 和 `hmily` 配置块。
画面 3: 在 `application.yml` 中高亮显示 `hmily` 配置块，包括 `serializer`、`retryMax`、`repositorySupport`、`started` 和 `hmilyDbConfig`。
画面 4: 在 `application.yml` 中高亮显示 `hmilyDbConfig` 的 `driverClassName`、`url`、`username` 和 `password`。
画面 5: 在 IntelliJ IDEA 中打开 `DatabaseConfiguration.java` 文件，展示 `@Configuration` 注解和 `HmilyTransactionBootstrap` 的初始化代码。
画面 6: 在 `application.yml` 中高亮显示 `hmily` 配置块，包括 `serializer`、`retryMax`、`repositorySupport`、`started` 和 `hmilyDbConfig`。
画面 7: 在 `DatabaseConfiguration.java` 中高亮显示 `HmilyTransactionBootstrap` 的 `setSerializer`、`setRetryMax`、`setRepositorySupport`、`setHmilyDbConfig` 方法调用。
画面 8: 展示课程 PPT 的“(3) feign代理”和“(4) 转账业务”部分，包含 `@FeignClient` 注解的接口定义和 `AccountInfoTcImpl` 类的结构。
画面 9: 在 IntelliJ IDEA 中打开 `Bank1Controller.java`，展示 `@RestController` 注解和 `transfer` 方法。
画面 10: 在 `AccountInfoTcImpl.java` 中高亮显示 `@Hmily(confirmMethod = "commit", cancelMethod = "rollback")` 注解和 `prepare` 方法。
画面 11: 在 `AccountInfoTcImpl.java` 中高亮显示 `if(!bank2Client.transfer(amount)) { throw new RuntimeException("bank2 exception"); }` 代码。
画面 12: 在 `AccountInfoTcImpl.java` 中高亮显示 `public void commit(String accountNo, double amount) { System.out.println("******* Bank1 Service commit..."); }` 代码。
画面 13: 在 `AccountInfoTcImpl.java` 中高亮显示 `public void rollback(String accountNo, double amount) { accountInfoDao.updateAccountBalance(accountNo, amount); System.out.println("******* Bank1 Service rollback..."); }` 代码。
画面 14: 在 IntelliJ IDEA 中打开 `BankHmilyServer.java`，展示 `@SpringBootApplication`、`@EnableDiscoveryClient`、`@EnableFeignClients` 注解和 `main` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```yaml
registry-fetch-interval-seconds: 5 # 获取服务列表
serviceUrl:
defaultZone: http://localhost:50080/eureka/
spring:
application:
name: hmily-demo-bank1
datasource:
url: jdbc:mysql://localhost:3306/hack?useUnicode=true
username: root
password: 123
type: com.alibaba.druid.pool.DruidDataSource
driver-class-name: com.mysql.cj.jdbc.Driver
```

画面 3:
```yaml
org:
dromara:
hmily:
serializer: kryo # 序列化工具
retryMax: 30 # 最大重试次数
repositorySupport: db # 持久化方式
started: true # 事务发起方
hmilyDbConfig:
driverClassName: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://localhost:3306/hack?useUnicode=true
username: root
password: 123
```

画面 4:
```yaml
hmilyDbConfig:
driverClassName: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://localhost:3306/hack?useUnicode=true
username: root
password: 123
```

画面 5:
```java
package cn.itcast.wanxint.hmily.demo.bank1.config;

import org.dromara.hmily.common.config.HmilyDbConfig;
import org.dromara.hmily.core.bootstrap.HmilyTransactionBootstrap;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy(proxyTargetClass=true);

@Configuration
@EnableAspectJAutoProxy(proxyTargetClass=true)
public class DatabaseConfiguration {

    @Autowired
    private Environment env;

    @Bean
    public HmilyTransactionBootstrap hmilyTransactionBootstrap(HmilyService hmilyService) {
        HmilyTransactionBootstrap hmilyTransactionBootstrap = new HmilyTransactionBootstrap(hmilyService);
        hmilyTransactionBootstrap.setSerializer(env.getProperty("org.dromara.hmily.serializer"));
        hmilyTransactionBootstrap.setRetryMax(Integer.parseInt(env.getProperty("org.dromara.hmily.retryMax")));
        hmilyTransactionBootstrap.setRepositorySupport(env.getProperty("org.dromara.hmily.repositorySupport"));
        HmilyDbConfig hmilyDbConfig = new HmilyDbConfig();
        hmilyDbConfig.setDriverClassName(env.getProperty("org.dromara.hmily.hmilyDbConfig.driverClassName"));
        hmilyDbConfig.setUrl(env.getProperty("org.dromara.hmily.hmilyDbConfig.url"));
        hmilyDbConfig.setUsername(env.getProperty("org.dromara.hmily.hmilyDbConfig.username"));
        hmilyDbConfig.setPassword(env.getProperty("org.dromara.hmily.hmilyDbConfig.password"));
        hmilyTransactionBootstrap.setHmilyDbConfig(hmilyDbConfig);
        return hmilyTransactionBootstrap;
    }
}
```

画面 6:
```yaml
org:
dromara:
hmily:
serializer: kryo # 序列化工具
retryMax: 30 # 最大重试次数
repositorySupport: db # 持久化方式
started: true # 事务发起方
hmilyDbConfig:
driverClassName: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://localhost:3306/hack?useUnicode=true
username: root
password: 123
```

画面 7:
```java
@Configuration
@EnableAspectJAutoProxy(proxyTargetClass=true)
public class DatabaseConfiguration {

    @Autowired
    private Environment env;

    @Bean
    public HmilyTransactionBootstrap hmilyTransactionBootstrap(HmilyService hmilyService) {
        HmilyTransactionBootstrap hmilyTransactionBootstrap = new HmilyTransactionBootstrap(hmilyService);
        hmilyTransactionBootstrap.setSerializer(env.getProperty("org.dromara.hmily.serializer"));
        hmilyTransactionBootstrap.setRetryMax(Integer.parseInt(env.getProperty("org.dromara.hmily.retryMax")));
        hmilyTransactionBootstrap.setRepositorySupport(env.getProperty("org.dromara.hmily.repositorySupport"));
        HmilyDbConfig hmilyDbConfig = new HmilyDbConfig();
        hmilyDbConfig.setDriverClassName(env.getProperty("org.dromara.hmily.hmilyDbConfig.driverClassName"));
        hmilyDbConfig.setUrl(env.getProperty("org.dromara.hmily.hmilyDbConfig.url"));
        hmilyDbConfig.setUsername(env.getProperty("org.dromara.hmily.hmilyDbConfig.username"));
        hmilyDbConfig.setPassword(env.getProperty("org.dromara.hmily.hmilyDbConfig.password"));
        hmilyTransactionBootstrap.setHmilyDbConfig(hmilyDbConfig);
        return hmilyTransactionBootstrap;
    }
}
```

画面 8:
```java
@FeignClient(value = "hmily-demo-bank2")
public interface Bank2Client {
    @RequestMapping("/bank2/transfer")
    @Hmily
    Boolean transfer(@RequestParam("amount") Double amount);
}
```

画面 9:
```java
@RestController
public class Bank1Controller {

    @Autowired
    AccountInfoService accountInfoService;

    @RequestMapping("/transfer")
    public String test(@RequestParam("amount") Double amount) {
        this.accountInfoService.updateAccountBalance("accountNo.1", amount);
        return "bank1向bank2转账" + amount;
    }
}
```

画面 10:
```java
@Hmily(confirmMethod = "commit", cancelMethod = "rollback")
public class AccountInfoTcImpl implements AccountInfoTc {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Autowired
    private Bank2Client bank2Client;

    @Override
    public void prepare(String accountNo, double amount) {
        System.out.println("******* Bank1 Service prepare...");
        if(!bank2Client.transfer(amount)) {
            throw new RuntimeException("bank2 exception");
        }
    }
```

画面 11:
```java
if(!bank2Client.transfer(amount
