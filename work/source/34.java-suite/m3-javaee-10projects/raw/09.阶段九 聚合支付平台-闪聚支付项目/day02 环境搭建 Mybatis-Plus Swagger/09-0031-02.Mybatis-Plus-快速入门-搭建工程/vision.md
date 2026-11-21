# 画面线理解：02.Mybatis-Plus-快速入门-搭建工程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\02.Mybatis-Plus-快速入门-搭建工程【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:10, 01:39, 02:33, 03:04, 03:32, 03:58, 04:39, 05:02, 05:31, 05:59, 06:49, 07:38, 08:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:34:51

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MyBatis-Plus 框架快速搭建一个 Spring Boot 项目，包括环境准备、数据库创建、工程结构搭建、配置文件编写和实体类 POJO 的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前位于“2.1 准备环境”，列出所需环境：JDK 8+、Maven 3.3.9、IDEA 2018.2、MySQL 5.7。
画面2：展示创建数据库和表的 SQL 语句，包括创建数据库 `mp`（字符集 utf8，排序规则 utf8_general_ci）和创建表 `tb_user` 的结构。
画面3：展示在 MySQL 数据库管理工具中执行 SQL 语句后，表 `tb_user` 中的数据已成功插入。
画面4：展示项目根目录下的 `pom.xml` 文件，其中包含 Maven 的基本配置信息。
画面5：展示 `pom.xml` 文件中添加了 Spring Boot 的父项目依赖。
画面6：展示 `pom.xml` 文件中添加了 Spring Boot 的测试依赖和 MyBatis-Plus 的依赖。
画面7：展示 `pom.xml` 文件中添加了 MySQL 驱动依赖，并切换到“2.3.3 编写 application.properties”章节。
画面8：展示 `application.properties` 文件中的配置内容，包括应用名称、数据库连接信息和日志配置。
画面9：展示 `application.properties` 文件中数据库密码配置为 `mysql`。
画面10：展示 `application.properties` 文件中数据库密码配置为 `mysql`，光标在配置行上。
画面11：展示 `User.java` 文件的开头部分，包含类注解和字段声明。
画面12：展示 `User.java` 文件中字段声明部分，光标在 `private` 关键字上。
画面13：展示 `User.java` 文件中使用 `@TableField` 注解映射数据库字段。
画面14：展示 `User.java` 文件中使用 `@TableField` 注解映射数据库字段，光标在 `@TableField("user_name")` 注解上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
2.1 准备环境
• JDK 8+
• Maven 3.3.9
• IDEA 2018.2
• MySQL 5.7

画面2：
创建数据库并设置字符集为utf-8：
CREATE DATABASE `mp` CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';

创建表和测试数据：
-- 创建测试表
CREATE TABLE `tb_user` (
`id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
`user_name` varchar(20) NOT NULL COMMENT '用户名',
`password` varchar(20) NOT NULL COMMENT '密码',
`name` varchar(38) DEFAULT NULL COMMENT '姓名',
`age` int(11) DEFAULT NULL COMMENT '年龄',
`email` varchar(50) DEFAULT NULL COMMENT '邮箱',
`birthday` datetime DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- 插入测试数据
insert into `tb_user` (`id`,`user_name`,`password`,`name`,`age`,`email`,`birthday`) values
(1,'zhangsan','123456','张三',18,'test1@itcast.cn','2019-09-26 11:42:01'),
(2,'lisi','123456','李四',20,'test2@itcast.cn','2019-10-01 11:42:08'),
(3,'wangwu','123456','王五',25,'test3@itcast.cn','2019-10-02 11:42:14'),
(4,'zhaozhu','123456','赵六',21,'test4@itcast.cn','2019-10-05 11:42:18'),
(5,'sunqi','123456','孙七',24,'test5@itcast.cn','2019-10-14 11:42:23');

画面3：
-- 插入测试数据
INSERT INTO `tb_user` (`id`,`user_name`,`password`,`name`,`age`,`email`,`birthday`) VALUES
(1,'zhangsan','123456','张三',18,'test1@itcast.cn','2019-09-26 11:42:01'),
(2,'lisi','123456','李四',20,'test2@itcast.cn','2019-10-01 11:42:08'),
(3,'wangwu','123456','王五',25,'test3@itcast.cn','2019-10-02 11:42:14'),
(4,'zhaozhu','123456','赵六',21,'test4@itcast.cn','2019-10-05 11:42:18'),
(5,'sunqi','123456','孙七',24,'test5@itcast.cn','2019-10-14 11:42:23');

画面4：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>cn.itcast.mp</groupId>
    <artifactId>itcast-mp-springboot</artifactId>
    <version>1.0-SNAPSHOT</version>

</project>

画面5：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>cn.itcast.mp</groupId>
    <artifactId>itcast-mp-springboot</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.8.RELEASE</version>
    </parent>

</project>

画面6：
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>

    <!-- 一、开发工具 -->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>

    <!-- 二、MyBatis-Plus支持 -->
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.1.0</version>
    </dependency>

</dependencies>

画面7：
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.1.0</version>
</dependency>

<!-- 一、mysql驱动 -->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.11</version>
</dependency>

画面8：
spring.application.name = itcast-mp-springboot
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
# logger Config
logging.level.root: debug

画面9：
spring.datasource.password=mysql

画面10：
spring.datasource.password=mysql

画面11：
package cn.itcast.mp.pojo;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import java.time.LocalDateTime;

@Data
public class User {

画面12：
package cn.it
