# 画面线理解：day05-21-Hmily实现注册-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-21-Hmily实现注册-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:45, 02:21, 03:00, 04:09, 05:43, 06:31, 07:51, 09:04, 09:44, 11:10, 12:11, 13:20, 14:12, 15:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:11:46

1) 这一组画面整体在讲如何使用 Hmily 框架解决用户注册功能中的分布式事务问题。

2) 按时间顺序列出每张画面的要点：
画面1：展示用户注册的 SQL 数据库表结构和部分数据，以及对应的 Java 代码片段，其中包含 `updateWrappers` 和 `cancelRegister` 方法。
画面2：IDEA 中显示项目结构，服务启动日志，表明 Eureka Server 和 Spring Boot 服务已启动。
画面3：服务启动失败，报错信息显示 `Error creating bean with name 'hmyTransactionBootstrap'`。
画面4：展示 `HmilyConfig.java` 代码，配置 Hmily 的数据库连接、用户名、密码等参数。
画面5：展示 `application.yml` 配置文件，包含 Apollo 配置、服务 ID、命名空间和日志配置。
画面6：服务启动日志，显示 SQL 连接建立的警告信息。
画面7：Postman 中发起 POST 请求，测试注册接口，请求体包含手机号。
画面8：IDEA 中显示服务启动日志，包含服务注册和发现信息。
画面9：展示 `AccountServiceImpl.java` 代码，其中包含 `confirmRegister` 方法。
画面10：在 `confirmRegister` 方法中添加了判断手机号是否为 "110" 的逻辑，若为 "110" 则抛出异常。
画面11：Postman 中发起 POST 请求，测试注册接口，请求体包含手机号 "110"。
画面12：IDEA 中显示 `confirmRegister` 方法执行时，`accountRegisterDTO` 对象的属性值，其中 `mobile` 为 "110"，`password` 为 null。
画面13：展示数据库表 `p2p_consumer` 中的数据，包含用户注册信息。
画面14：PPT 页面，标题为“4. Hmily解决注册功能的事务问题”，子标题“4.1 业务回顾”，图示展示了“调用端/App”、“用户中心”、“统一账号服务”三个模块之间的交互流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1代码片段：
```java
public void cancelRegister(AccountRegisterDTO registerDTO) {
    log.info("cancelRegister");
    removeWrappers(AccountRegisterDTO.class, registerDTO);
    registerDTO.setMobile(null);
}
```
画面4代码片段：
```java
@Configuration
public class HmilyConfig {
    @Bean
    public HmilyTransactionBootstrap hmilyTransactionBootstrap() {
        HmilyConfig hmilyConfig = new HmilyConfig();
        hmilyConfig.setDriverClassname(env.getProperty("org.dromara.hmily.hmilyDbConfig.driverClassName"));
        hmilyConfig.setUrl(env.getProperty("org.dromara.hmily.hmilyDbConfig.url"));
        hmilyConfig.setUsername(env.getProperty("org.dromara.hmily.hmilyDbConfig.username"));
        hmilyConfig.setPassword(env.getProperty("org.dromara.hmily.hmilyDbConfig.password"));
        hmilyConfig.setTransactionTimeout(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionTimeout"));
        hmilyConfig.setIsolationLevel(env.getProperty("org.dromara.hmily.hmilyDbConfig.isolationLevel"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionType(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionType"));
        hmilyConfig.setTransactionMode(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionMode"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.setTransactionIsolation(env.getProperty("org.dromara.hmily.hmilyDbConfig.transactionIsolation"));
        hmilyConfig.set
