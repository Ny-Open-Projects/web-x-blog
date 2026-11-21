# 画面线理解：day05-19-Hmily实现注册-用户中心

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-19-Hmily实现注册-用户中心_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:53, 02:25, 03:21, 04:23, 05:02, 05:31, 06:12, 06:56, 07:48, 10:03, 10:51, 11:23, 12:11, 12:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:10:04

1) 这一组画面整体在讲如何在 Apollo 配置中心为 consumer-service 项目配置 Hmily 分布式事务相关参数，并修改服务端代码以实现注册、确认和取消功能。

2) 按时间顺序列出每张画面的要点：
画面1: 显示文件资源管理器，当前路径为“wanningp2p > day05 > 资料”，包含多个项目文档和图片。
画面2: Apollo配置中心页面，显示“common-template”应用下的多个公共命名空间，包括 micro_service.spring-boot-mysql、micro_service.spring-boot-http 等。
画面3: Apollo配置中心页面，显示“application”应用下的多个公共命名空间，包括 micro_service.spring-boot-mysql、micro_service.spring-boot-http 等。
画面4: SQLyog Professional 64 界面，显示数据库连接和表结构，当前打开的是 p2p_undo_log 表。
画面5: Apollo配置中心页面，显示“consumer-service”应用的配置页面，尚未加载任何配置。
画面6: Apollo配置中心页面，显示“consumer-service”应用的配置列表，包含多个 Hmily 相关配置项，如 org.dromara.hmily.serializer、org.dromara.hmily.retryMax 等。
画面7: IDEA 编辑器界面，显示 Hmily 事务配置代码，包括设置事务启动、配置数据库连接、用户名和密码等。
画面8: IDEA 编辑器界面，显示 Hmily 事务配置代码，包括设置事务启动、配置数据库连接、用户名和密码等。
画面9: IDEA 编辑器界面，显示多个窗口，包括 Apollo 配置中心、adminService、ApolloPortal、configservice 等，以及 ConsumerServiceImpl 代码。
画面10: IDEA 编辑器界面，显示 ConsumerServiceImpl 类的代码，包含 checkMobile、getMobile、register 方法。
画面11: IDEA 编辑器界面，显示 ConsumerServiceImpl 类的代码，包含 register 方法的详细实现，包括设置用户名、密码、保存等操作。
画面12: IDEA 编辑器界面，显示 ConsumerServiceImpl 类的代码，包含 checkMobile、getMobile 方法。
画面13: IDEA 编辑器界面，显示 ConsumerServiceImpl 类的代码，包含 cancelRegister 方法，其中包含日志记录和调用 restResponse 的代码。
画面14: IDEA 编辑器界面，显示“4.3.1 事务发起：consumer-service”章节，包含在 Apollo 中新增的 Hmily 配置项和在 consumer-service 项目中添加的 @Configuration 注解类。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7代码：
```java
hmilyTransactionBootstrap.setRepositorySupport(env.getProperty("org.dromara.hmily.repositorySupport"));
hmilyTransactionBootstrap.setStarted(Boolean.parseBoolean(env.getProperty("org.dromara.hmily.started")));
HmilyDbConfig hmilyDbConfig = new HmilyDbConfig();
hmilyDbConfig.setDriverClassName(env.getProperty("org.dromara.hmily.hmilyDbConfig.driverClassName"));
hmilyDbConfig.setUrl(env.getProperty("org.dromara.hmily.hmilyDbConfig.url"));
hmilyDbConfig.setUsername(env.getProperty("org.dromara.hmily.hmilyDbConfig.username"));
hmilyDbConfig.setPassword(env.getProperty("org.dromara.hmily.hmilyDbConfig.password"));
hmilyTransactionBootstrap.setHmilyDbConfig(hmilyDbConfig);
return hmilyTransactionBootstrap;
```

画面14配置：
```properties
org.dromara.hmily.serializer = kryo
org.dromara.hmily.retryMax = 30
org.dromara.hmily.repositorySupport = db
org.dromara.hmily.started = true
org.dromara.hmily.hmilyDbConfig.driverClassName = com.mysql.cj.jdbc.Driver
org.dromara.hmily.hmilyDbConfig.url = jdbc:mysql://localhost:3306/p2p_undo_log?
org.dromara.hmily.hmilyDbConfig.username = root
org.dromara.hmily.hmilyDbConfig.password = 123
```

```java
@Configuration
@EnableAspectJAutoProxy(proxyTargetClass = true)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14 PPT标题：“4.3 功能实现”、“4.3.1 事务发起：consumer-service”。
表格数据：
| Key | Value | 备注 | 最后修改人 | 最后修改时间 |
| --- | --- | --- | --- | --- |
| org.dromara.hmily.serializer | kryo |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.retryMax | 30 |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.repositorySupport | db |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.started | true |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.hmilyDbConfig.driverClassName | com.mysql.cj.jdbc.Driver |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.hmilyDbConfig.url | jdbc:mysql://localhost:3306/p2p_undo_log? |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.hmilyDbConfig.username | root |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.hmilyDbConfig.password | 123 |  | apollo | 2019-08-07 09:58:54 |
| useUnicode | true |  | apollo | 2019-08-07 09:58:54 |

5) 不要评价画面美观，不要输出与课程无关的内容。
