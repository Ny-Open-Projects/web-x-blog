# 画面线理解：day13-1-可靠消息实现最终一致性-入门案例-环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-1-可靠消息实现最终一致性-入门案例-环境搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:17, 02:18, 02:43, 03:51, 04:16, 05:50, 06:09, 06:26, 07:00, 07:31, 07:54, 08:25, 08:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:00:05

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 RocketMQ 实现分布式事务消息的最终一致性，通过模拟银行转账场景，讲解环境搭建、数据库创建、服务配置及消息流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 第 5.2 节“RocketMQ 可靠消息”，解释其原子性保证机制，图示本地事务、发送方、服务端、接收方四部分交互流程。
画面 2: 展示 PPT 第 5.3.1 节“业务说明”，图示银行转账流程：Bank1 发送转账消息 → RocketMQ 接收 → Bank2 接收并处理 → Bank1 确认 → RocketMQ 设置消息状态 → Bank2 读取消息。
画面 3: 展示 PPT 第 5.3.1 节“业务说明”，图示流程中“消息接受成功，此时消息对银行系统不可见”步骤。
画面 4: 展示 PPT 第 5.3.1 节“业务说明”，图示流程中“本地事务，完成账户减操作”步骤。
画面 5: 展示 PPT 第 5.3.2 节“环境需求”，列出数据库、JDK、微服务框架、RocketMQ 服务端和客户端的版本要求。同时展示“创建数据库”部分，包含 SQL 语句。
画面 6: 展示 SQLyog 界面，正在执行 SQL 语句，用于创建或修改数据库表。
画面 7: 展示 PPT 第 5.3.4 节“Maven 工程”，图示 IDEA 中的 Maven 项目结构，包含三个子模块：ensure-message-demo-bank1、ensure-message-demo-bank2 和父工程。
画面 8: 展示 IDEA 中父工程的 pom.xml 文件，高亮显示 Spring Boot 和 Swagger 的依赖配置。
画面 9: 展示 IDEA 中父工程的 pom.xml 文件，高亮显示 Spring Cloud 的依赖配置。
画面 10: 展示 ensure-message-demo-bank1 的 application.properties 配置文件，设置服务名、端口、数据库连接、RocketMQ 生产者组和名称服务器。
画面 11: 展示 ensure-message-demo-bank1 的 AccountChangeEvent.java 类，定义了账户变更事件的实体结构，包含 accountNo、amount、txNo 字段。
画面 12: 展示 ensure-message-demo-bank2 的 application.properties 配置文件，设置服务名、端口、数据库连接、RocketMQ 生产者组和名称服务器。
画面 13: 展示 PPT 第 5.3.2 节“环境搭建”，重复展示数据库创建 SQL 和启动 RocketMQ 的命令。
画面 14: 展示 PPT 第 5.3.2 节“环境搭建”，图示银行转账流程，与画面 2、3、4、5、6、7、8、9、10、11、12、13 中的流程图一致。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```
5.3.2.1 环境需求
• 数据库：MySQL 5.7+
• JDK：64位 jdk1.8+
• 微服务：spring-boot 2.1.3、spring-cloud-Greenwich.RELEASE
• RocketMQ 服务端：RocketMQ 4.5.0
• RocketMQ 客户端：RocketMQ-spring-boot-starter 2.0.2-RELEASE

5.3.2.2 创建数据库
本案例需要两个数据库，一个是bank1，一个是bank2，无需创建，直接使用Hmily快速入门案例中的数据库即可。另外，为了实现幂等性，需要分别在bank1、bank2数据库中新增de_duplication表，即交易记录表(去重表)。

DROP TABLE IF EXISTS `de_duplication`;
CREATE TABLE `de_duplication` (
  `tx_no` bigint(20) NOT NULL,
  `create_time` datetime(0) NOT NULL DEFAULT NULL,
  PRIMARY KEY (`tx_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
```

画面 6:
```
DROP TABLE IF EXISTS `de_duplication`;
CREATE TABLE `de_duplication` (
  `tx_no` bigint(20) NOT NULL,
  `create_time` datetime(0) NOT NULL DEFAULT NULL,
  PRIMARY KEY (`tx_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
```

画面 7:
```
set ROCKETMQ_HOME=[RocketMQ服务端解压路径]
start [RocketMQ服务端解压路径]/bin/mqnamesrv.cmd

启动broker:
set ROCKETMQ_HOME=[RocketMQ服务端解压路径]
start [RocketMQ服务端解压路径]/bin/mqbroker.cmd -n 127.0.0.1:9876
autoCreateTopic=true
```

画面 8:
```
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>io.springfox</groupId>
      <artifactId>springfox-swagger2</artifactId>
      <version>2.8.0</version>
    </dependency>
    <dependency>
      <groupId>io.springfox</groupId>
      <artifactId>springfox-swagger-ui</artifactId>
      <version>2.8.0</version>
    </dependency>
    <dependency>
      <groupId>org.projectlombok</groupId>
      <artifactId>lombok</artifactId>
      <version>1.18.0</version>
    </dependency>
  </dependencies>
</dependencyManagement>
```

画面 9:
```
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-dependencies</artifactId>
  <version>Greenwich.SR1</version>
  <type>pom</type>
  <scope>import</scope>
</dependency>
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-dependencies</artifactId>
  <version>2.1.3.RELEASE</version>
</dependency>
```

画面 10:
```
spring.application.name = ensure-message-demo-bank1
server.port=56081
server.servlet.context-path = /bank1
spring.http.encoding.enabled = true
spring.http.encoding.charset = UTF-8
spring.mvc.throw-exception-if-no-handler-found = true

spring.datasource.type = com.alibaba.druid.DruidDataSource
spring.datasource.driver-class-name = com.mysql.jdbc.Driver
spring.datasource.url = jdbc:mysql://localhost:3306/bank1?useUnicode=true
spring.datasource.username = root
spring.datasource.password = 123

swagger.enable = true

rocketmq.producer.group = producer_ensure_bank1
rocketmq.name-server = 127.0.0.1:9876
```

画面 11:
```
@Data
@AllArgsConstructor
@NoArgsConstructor
public class AccountChangeEvent implements Serializable {
    private String accountNo;
    private double amount;
    private long txNo;
}
```

画面 12:
```
spring.application.name = ensure-message-demo-bank2
server.port=56082
server.servlet.context-path = /bank2
spring.http.encoding.enabled = true
spring.http.encoding.charset = UTF-8
spring.mvc.throw-exception-if-no-handler-found = true

spring.datasource.type = com.alibaba.druid.DruidDataSource
spring.datasource.driver-class-name = com.mysql.jdbc.Driver
spring.datasource.url = jdbc:mysql://localhost:3306/bank2?useUnicode=true
spring.datasource.username = root
spring.datasource.password = 123

swagger.enable = true

rocketmq.producer.group = producer_ensure_bank2
rocketmq.name-server = 127.0.0.1:9876
```

画面 13:
```
5.3.2.2 创建数据库
本案例需要两个数据库，一个是bank1，一个是bank2，无需创建，直接使用Hmily快速入门案例中的数据库即可。另外，为了实现幂等性，需要分别在bank1、bank2数据库中新增de_duplication表，即交易记录表(去重表)。

DROP TABLE IF EXISTS `de_duplication`;
CREATE TABLE `de_duplication` (
  `tx_no` bigint(20) NOT NULL,
  `create_time` datetime(0) NOT NULL DEFAULT NULL,
  PRIMARY KEY (`tx_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
```

画面 14:
```
5.3.2 环境搭建
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题“5.2 RocketMQ 可靠消息”，图示中“本地事务”指向“发送方”，“发送方”指向“服务端”，“服务端”指向“
