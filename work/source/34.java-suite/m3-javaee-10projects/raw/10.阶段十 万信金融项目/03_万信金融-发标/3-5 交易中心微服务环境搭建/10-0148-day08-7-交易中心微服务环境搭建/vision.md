# 画面线理解：day08-7-交易中心微服务环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-5 交易中心微服务环境搭建
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-5 交易中心微服务环境搭建\day08-7-交易中心微服务环境搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:24, 02:17, 03:08, 04:02, 05:08, 05:55, 06:40, 07:30, 08:36, 09:17, 10:11, 10:27, 10:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:47:33

1) 这一组画面整体在讲如何在 P2P 项目中搭建并配置 ShardingSphere 分库分表的交易服务模块，包括导入工程、配置 Apollo 和编写 application.yml。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 Word 文档中查看课程内容，指出需在 Apollo 中配置 transaction-service 项目。
画面 2: 展示分库分表的架构图，说明以 ID % 2 为分片策略，将数据分到 p2p_transaction_0 和 p2p_transaction_1 两个库。
画面 3: 在 IDEA 中导入模块，设置导入 Maven 项目并自动创建模块组。
画面 4: 在 IDEA 中查看 pom.xml，高亮显示添加了 sharding-jdbc-spring-boot-starter 依赖。
画面 5: 在 IDEA 中浏览项目结构，定位到 transaction-service 模块。
画面 6: 打开浏览器，准备访问 Apollo 配置中心。
画面 7: 在 Apollo 配置中心，查看 micro_service.spring-boot-http 等多个命名空间。
画面 8: 在 Apollo 中编辑 application 配置，设置 ShardingSphere 的分片策略和数据源。
画面 9: 在 Word 文档中再次展示需要在 Apollo 中配置的 application.yml 内容。
画面 10: 打开 SQLyog，查看数据库结构，准备执行 SQL。
画面 11: 在 IDEA 中查看 application.yml，配置 Apollo 的 namespaces 和 spring.application.name。
画面 12: 在 IDEA 控制台中，启动项目，显示 Spring Boot 启动日志。
画面 13: 控制台显示 Quartz Scheduler 初始化成功，服务启动完成。
画面 14: 回到 Word 文档，再次强调在 Apollo 中配置 transaction-service 项目。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```
swagger.enable = true
spring.mvc.throw-exception-if-no-handler-found = true

spring.shardingsphere.datasource.names = ds0,ds1

spring.shardingsphere.datasource.ds0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds0.driver-class-name = com.mysql.cj.jdbc.Driver
spring.shardingsphere.datasource.ds0.url = jdbc:mysql://localhost:3306/p2p_transaction_0?useUnicode=true
spring.shardingsphere.datasource.ds0.username = root
spring.shardingsphere.datasource.ds0.password = 123

spring.shardingsphere.datasource.ds1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds1.driver-class-name = com.mysql.cj.jdbc.Driver
spring.shardingsphere.datasource.ds1.url = jdbc:mysql://localhost:3306/p2p_transaction_1?useUnicode=true
```

画面 4:
```xml
<dependency>
    <groupId>org.apache.shardingsphere</groupId>
    <artifactId>sharding-jdbc-spring-boot-starter</artifactId>
</dependency>
```

画面 8:
```
spring.shardingsphere.datasource.ds0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds0.driver-class-name = com.mysql.cj.jdbc.Driver
spring.shardingsphere.datasource.ds0.url = jdbc:mysql://localhost:3306/p2p_transaction_0?useUnicode=true
spring.shardingsphere.datasource.ds0.username = root
spring.shardingsphere.datasource.ds0.password = 123

spring.shardingsphere.datasource.ds1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.ds1.driver-class-name = com.mysql.cj.jdbc.Driver
spring.shardingsphere.datasource.ds1.url = jdbc:mysql://localhost:3306/p2p_transaction_1?useUnicode=true
spring.shardingsphere.datasource.ds1.username = root
spring.shardingsphere.datasource.ds1.password = 123

spring.shardingsphere.sharding.default-database-strategy.inline.sharding-column = CONSUMER_ID
spring.shardingsphere.sharding.default-database-strategy.inline.algorithm-expression = ds${CONSUMER_ID % 2}
spring.shardingsphere.sharding.tables.project.actual-data-nodes = ds${0..1}.project
spring.shardingsphere.sharding.tables.project.table-strategy.inline.sharding-column = project_id
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression = project_${project_id % 2}
```

画面 11:
```yaml
app:
  id: transaction-service
apollo:
  bootstrap:
    enabled: true
    # superLoad:
    #   enabled: true
    namespaces: application,micro_service.spring-boot-http,micro_service.spring-eureka,micro_service.spring-ribbon,micro_service.mybatis-plus,micro_service.spring-cloud-feign,micro_service.spring-rocketmq
spring:
  application:
    name: transaction-service
  main:
    allow-bean-definition-overriding: true
logging:
  config: classpath:log4j2-dev.xml
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 2:
架构图结构：
- 顶层：p2p_transaction（蓝色框）
- 两个分支指向：
  - 左侧：p2p_transaction_0（橙色框）包含“标的的信息表”和“投标信息表”
  - 右侧：p2p_transaction_1（橙色框）包含“标的的信息表”和“投标信息表”

画面 14:
PPT 标题：“3.3 开发环境搭建”
内容：
1. 把资料文件夹中的 wanning2p-transaction-service 工程导入到当前 P2P 项目中
2. 检查 maven 依赖和工程中的基本代码
3. 在 Apollo 中创建 transaction-service 项目，在 application 名称空间中进行如下配置：

5) 无
