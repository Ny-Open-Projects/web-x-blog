# 画面线理解：day05-14-Hmily实现转账-环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-14-Hmily实现转账-环境搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:29, 02:54, 03:22, 03:41, 04:30, 05:12, 05:26, 05:47, 06:20, 06:29, 06:51, 07:00, 08:51, 08:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:06:08

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Hmily 框架实现 TCC 分布式事务，通过创建两个银行账户（张三和李四）的转账业务来说明事务管理机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示 PPT 页面“3.3.1 业务说明”，内容为：本案例通过 Hmily 框架实现 TCC 分布式事务，模拟两个账户的转账交易过程。两个账户分别在不同的银行（张三在 bank1、李四在 bank2），bank1、bank2 是两个微服务。对于交易过程中的每个操作，要么都成功，要么都失败。
- 展示架构图：张三（bank1）→ 转账100元 → 李四（bank2），下方有“事务管理器（协调管理）”，并有箭头分别指向 A账户和 B账户。

画面2：
- 与画面1内容相同，PPT 页面“3.3.1 业务说明”和架构图完全一致。

画面3：
- 展示 PPT 页面“3.3.2.2 数据库”，内容为：创建 bank1 库，并导入以下表结构和数据：
- 代码块：
  CREATE DATABASE 'bank1' CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';

画面4：
- 展示 PPT 页面“3.3.2.2 数据库”，内容为：创建 bank1 库，并导入以下表结构和数据：
- 代码块：
  USE bank1;
  DROP TABLE IF EXISTS 'account_info';
  CREATE TABLE 'account_info' (
    'id' bigint(20) NOT NULL AUTO_INCREMENT,
    'account_name' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '户主姓名',
    'account_no' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '银行卡号',
    'account_password' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '账户密码',
    'account_balance' double NULL DEFAULT NULL COMMENT '账户余额',
    PRIMARY KEY ('id') USING BTREE
  ) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
  INSERT INTO 'account_info' VALUES ('1', '张三', '1', '10000');

画面5：
- 展示 PPT 页面“3.3.2.2 数据库”，内容为：创建 bank2 库，并导入以下表结构和数据：
- 代码块：
  CREATE DATABASE 'bank2' CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
  USE bank2;
  DROP TABLE IF EXISTS 'account_info';
  CREATE TABLE 'account_info' (
    'id' bigint(20) NOT NULL AUTO_INCREMENT,
    'account_name' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '户主姓名',
    'account_no' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '银行卡号',
    'account_password' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '账户密码',
    'account_balance' double NULL DEFAULT NULL COMMENT '账户余额',
    PRIMARY KEY ('id') USING BTREE
  ) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
  INSERT INTO 'account_info' VALUES ('2', '李四', '2', NULL, '0');

画面6：
- 展示数据库管理工具（DBeaver）中 bank2 数据库的 account_info 表，显示数据：
  - account_name: 张三
  - account_no: 1
  - account_password: 1
  - account_balance: 10000

画面7：
- 展示数据库管理工具（DBeaver）中 bank1 数据库的 account_info 表，显示数据：
  - account_name: 李四
  - account_no: 2
  - account_password: 2
  - account_balance: 0

画面8：
- 展示 PPT 页面“3.3.1 业务说明”，内容为：本案例通过 Hmily 框架实现 TCC 分布式事务，模拟两个账户的转账交易过程。两个账户分别在不同的银行（张三在 bank1、李四在 bank2），bank1、bank2 是两个微服务。对于交易过程中的每个操作，要么都成功，要么都失败。
- 展示“黑马程序员”官网信息及链接。

画面9：
- 展示 IntelliJ IDEA 中的项目结构，当前选中 pom.xml 文件。
- 代码块：
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>2.0.0</version>
  </dependency>

画面10：
- 展示 IntelliJ IDEA 中的项目结构，当前选中 pom.xml 文件。
- 代码块：
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>2.0.0</version>
  </dependency>

画面11：
- 展示 IntelliJ IDEA 中的项目结构，当前选中 pom.xml 文件。
- 代码块：
  <dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>hmily-spring-boot-starter</artifactId>
    <version>1.1.16</version>
  </dependency>

画面12：
- 展示 IntelliJ IDEA 中的项目结构，当前选中 pom.xml 文件。
- 代码块：
  <dependency>
    <groupId>commons-lang</groupId>
    <artifactId>commons-lang</artifactId>
    <version>2.6</version>
  </dependency>

画面13：
- 展示 PPT 页面“3.3.2.3 Maven 工程”，内容为：
  (1) 搭建 maven 工程，以 tcc-hmily-demo 为父工程，进行依赖管理，hmily-demo-bank1 负责张三账户操作，hmily-demo-bank2 负责李四账户操作，hmily-demo-discover-server 是服务注册中心。
  (2) pom.xml 导入 hmyl 相关依赖，这里不再详述。
- 展示项目结构：
  tcc-hmily-demo
  ├── idea
  ├── hmily-demo-bank1
  ├── hmily-demo-bank2
  ├── hmily-demo-discover-server
  └── logs
  └── tcc-hmily-demo.iml

画面14：
- 展示 PPT 页面“3.3.2.2 数据库”，内容为：创建 bank1 库，并导入以下表结构和数据：
- 代码块：
  CREATE DATABASE 'bank1' CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
  USE bank1;
  DROP TABLE IF EXISTS 'account_info';
  CREATE TABLE 'account_info' (
    'id' bigint(20) NOT NULL AUTO_INCREMENT,
    'account_name' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '户主姓名',
    'account_no' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '银行卡号',
    'account_password' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '账户密码',
    'account_balance' double NULL DEFAULT NULL COMMENT '账户余额',
    PRIMARY KEY ('id') USING BTREE
  ) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
  INSERT INTO 'account_info' VALUES ('1', '张三', '1', '1', '10000');
