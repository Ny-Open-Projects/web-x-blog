# 画面线理解：16.功能开发之设计数据库以及编写配置文件

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\16.功能开发之设计数据库以及编写配置文件_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:39, 02:08, 02:16, 02:38, 03:09, 03:29, 04:12, 04:31, 04:59, 05:10, 05:18, 06:28, 06:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:07:57

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目（itcast-tanhua-ss0）的数据库表结构设计、配置文件编写及基础代码编写过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 Typora 文档，内容为“3.3. 数据库表”，展示创建用户表 `tb_user` 的 SQL 语句。
- SQL 语句：
  ```sql
  CREATE TABLE `tb_user` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `mobile` varchar(15) DEFAULT NULL COMMENT '手机号',
    `password` varchar(32) DEFAULT NULL COMMENT '密码，需要加密',
    `created` datetime DEFAULT NULL,
    `updated` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `mobile` (`mobile`) USING BTREE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';
  ```

画面 2：
- 显示 Navicat Premium 连接数据库的界面，左侧树状结构中选中了数据库 `mytanhua`。
- 数据库连接地址为 `127.0.0.1:3306`。

画面 3：
- 在 Navicat Premium 中，选中了 `mytanhua` 数据库下的 `tb_user` 和 `tb_user_info` 两个表。
- 表信息显示：`tb_user` 和 `tb_user_info` 均为 InnoDB 引擎，占用空间 16 KB。

画面 4：
- 显示 Typora 文档，内容为“3.4. 编写配置”，展示 `application.properties` 文件的开头部分。
- 配置内容：
  ```properties
  spring.application.name = itcast-tanhua-ss0
  server.port = 18080
  ```

画面 5：
- 显示 IntelliJ IDEA 的项目结构，右键点击 `src/main/java`，弹出创建新文件的菜单。
- 菜单中包含 Kotlin、Java、XML、YAML 等多种文件类型选项。

画面 6：
- 显示 IntelliJ IDEA 中 `application.properties` 文件的内容，包含数据库连接配置。
- 配置内容：
  ```properties
  spring.application.name = itcast-tanhua-ss0
  server.port = 18080
  spring.datasource.driver-class-name=com.mysql.jdbc.Driver
  spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mytanhua?useUnicode=true&characterEncoding=utf8&autoReconnect=true&multiQueries=true&useSSL=false
  spring.datasource.username=root
  spring.datasource.password=root
  ```

画面 7：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，下方有一个 Typora 文档的缩略图预览。
- 预览图中包含多个视频画面，其中一张显示了 `application.properties` 文件。

画面 8：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，选中了 MyBatis-Plus 的配置项。
- 配置内容：
  ```properties
  # 表名前缀
  mybatis-plus.type-enums-package=com.tanhua.sso.enums
  mybatis-plus.global-config.db-config.table-prefix-th_
  # id策略为自增
  mybatis-plus.global-config.db-config.id-type-auto
  ```

画面 9：
- 显示 Typora 文档，内容为“3.4. 编写配置”，展示 `application.properties` 文件中 Redis 和 RocketMQ 的配置。
- 配置内容：
  ```properties
  # Redis相关配置
  spring.redis.jedis.pool.max-wait = 5000ms
  spring.redis.jedis.pool.maxIdle = 100
  spring.redis.jedis.pool.minIdle = 10
  spring.redis.timeout = 10s
  spring.redis.cluster.nodes = 192.168.31.81:6379,192.168.31.81:6380,192.168.31.81:6381
  spring.redis.cluster.max-redirects=5

  # RocketMQ相关配置
  spring.rocketmq.nameServer=192.168.31.81:9876
  spring.rocketmq.producer.group=tanhua
  ```

画面 10：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，选中了 Redis 配置部分。
- 配置内容：
  ```properties
  # Redis相关配置
  spring.redis.jedis.pool.max-wait = 5000ms
  spring.redis.jedis.pool.maxIdle = 100
  spring.redis.jedis.pool.minIdle = 10
  spring.redis.timeout = 10s
  spring.redis.cluster.nodes = 192.168.31.81:6379,192.168.31.81:6380,192.168.31.81:6381
  spring.redis.cluster.max-redirects=5
  ```

画面 11：
- 显示 Navicat Premium 中 `mytanhua` 数据库的表结构，下方有一个 Typora 文档的缩略图预览。
- 预览图中包含多个视频画面，其中一张显示了 `application.properties` 文件。

画面 12：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，选中了 RocketMQ 配置部分。
- 配置内容：
  ```properties
  # RocketMQ相关配置
  spring.rocketmq.nameServer=192.168.31.81:9876
  spring.rocketmq.producer.group=tanhua
  ```

画面 13：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，选中了 JWT 密钥配置。
- 配置内容：
  ```properties
  jwt.secret=76bd425b6f29f7fcc2e0bfc286043df1
  ```

画面 14：
- 显示 Typora 文档，内容为“3.5. 编写基础代码”，展示 `SexEnum` 的 Java 类代码。
- Java 代码：
  ```java
  package com.tanhua.sso.enums;

  public enum SexEnum {
      MALE(1, "男"),
      FEMALE(2, "女"),
      UNKNOW(3, "未知");
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
见上文第 2 点中各画面的要点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 画面 1、4、6、7、9、10、12、13、14 中的 Typora 文档标题分别为：
  - 画面 1：3.3. 数据库表
  - 画面 4：3.4. 编写配置
  - 画面 9：3.4. 编写配置
  - 画面 14：3.5. 编写基础代码
- 画面 1 中的架构图：
  - 上层：`注册登录`
  - 中层：`状态变更`
  - 下层：`RocketMQ`
  - 无明确指向关系，但结构上是自上而下的流程。

5) 不要评价画面美观，不要输出与课程无关的内容。
- 无。
