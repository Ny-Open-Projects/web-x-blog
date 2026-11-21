# 画面线理解：16-企业微服务：实现crud操作之创建实体类

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\16-企业微服务：实现crud操作之创建实体类_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:01, 02:19, 02:40, 02:59, 03:37, 04:06, 04:31, 04:45, 05:04, 06:59, 07:18, 07:41, 08:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:58:57

1) 这一组画面整体在讲什么（一句话）：
讲解企业信息表（co_company）的数据库结构分析与对应的 Java 实体类（Company）的开发，包括表结构定义、字段映射、注解配置及数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程目录，当前位于“5.2 企业管理-CRUD”下的“5.2.1 表结构分析”，并显示了创建公司表的 SQL 语句，包含字段如 id, name, manager_id, version, renewal_date, expiration_date, company_area, company_address, business_license_id, legal_representative, company_phone, mailbox, company_size, industry, remarks 等，以及 audit_state, state, balance, create_time 等字段。

画面 2: 继续展示公司表的 SQL 语句，包含字段如 audit_state, state, balance, create_time，并显示了表的 ENGINE 为 INNODB 和 CHARSET 为 utf8mb4。

画面 3: 展示 IntelliJ IDEA 中的项目结构，选中 application.yml 文件，显示了 Spring Boot 的配置，包括 server.port=9001，spring.application.name=ihrm-company，以及数据源配置（driver-class-name, url, username, password）和 JPA 配置（database, show-sql, open-in-view）。

画面 4: 展示了 SQLyog Ultimate 的启动界面，准备连接数据库。

画面 5: 展示了 SQLyog 中连接到本地数据库后的表结构，显示了 co_company 表的字段及其数据类型、索引、默认值等信息。

画面 6: 展示了课程目录，当前位于“5.2.2 完成企业增删改查操作”下的“（1）实体类（domain）”，并显示了 Company 类的 Java 代码，包含 @Entity、@Table、@Data、@AllArgsConstructor 等注解。

画面 7: 展示了 IntelliJ IDEA 中的 application.yml 文件，显示了 Spring Boot 的配置，包括 server.port=9001，spring.application.name=ihrm-company，以及数据源配置（driver-class-name, url, username, password）和 JPA 配置（database, show-sql, open-in-view）。

画面 8: 展示了 IntelliJ IDEA 中的 Company.java 文件，显示了实体类的代码，包括 @Entity、@Table、@Data、@AllArgsConstructor 等注解，以及字段如 id, name, managerId, version, renewalDate 等。

画面 9: 展示了 Notepad++ 中的 Company.java 文件，显示了实体类的代码，包括 @Entity、@Table、@Data、@AllArgsConstructor 等注解，以及字段如 id, name, managerId, version, renewalDate 等。

画面 10: 展示了 IntelliJ IDEA 中的 Company.java 文件，显示了在编写 Date 类型字段时，IDE 提示了多个 Date 相关的类选项，如 Date (java.util)，Date (java.sql)，Date in BaseCalendar 等。

画面 11: 展示了 IntelliJ IDEA 中的 Company.java 文件，显示了实体类的代码，包括 @Entity、@Table、@Data、@AllArgsConstructor 等注解，以及字段如 id, name, managerId, version, renewalDate 等。

画面 12: 展示了 SQLyog 中连接到本地数据库后的表结构，显示了 co_company 表的字段及其数据类型、索引、默认值等信息。

画面 13: 展示了 IntelliJ IDEA 中的 Company.java 文件，显示了实体类的代码，包括 @Entity、@Table、@Data、@AllArgsConstructor 等注解，以及字段如 id, name, managerId, version, renewalDate 等。

画面 14: 展示了 IntelliJ IDEA 中的 Company.java 文件，显示了实体类的代码，包括 @Entity、@Table、@Data、@AllArgsConstructor 等注解，以及字段如 id, name, managerId, version, renewalDate 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
CREATE TABLE `co_company` (
`id` varchar(40) NOT NULL COMMENT 'ID',
`name` varchar(255) NOT NULL COMMENT '公司名称',
`manager_id` varchar(255) NOT NULL COMMENT '企业登录账号ID',
`version` varchar(255) DEFAULT NULL COMMENT '当前版本',
`renewal_date` datetime DEFAULT NULL COMMENT '续期时间',
`expiration_date` datetime DEFAULT NULL COMMENT '到期时间',
`company_area` varchar(255) DEFAULT NULL COMMENT '公司地区',
`company_address` text COMMENT '公司地址',
`business_license_id` varchar(255) DEFAULT NULL COMMENT '营业执照-照片ID',
`legal_representative` varchar(255) DEFAULT NULL COMMENT '法人代表',
`company_phone` varchar(255) DEFAULT NULL COMMENT '公司电话',
`mailbox` varchar(255) DEFAULT NULL COMMENT '邮箱',
`company_size` varchar(255) DEFAULT NULL COMMENT '公司规模',
`industry` varchar(255) DEFAULT NULL COMMENT '所属行业',
`remarks` text COMMENT '备注',
`audit_state` varchar(255) DEFAULT NULL COMMENT '审核状态',
`state` tinyint(2) NOT NULL DEFAULT '1' COMMENT '状态',
`balance` double DEFAULT NULL COMMENT '当前余额',
`create_time` datetime NOT NULL COMMENT '创建时间',
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4;

画面 3:
#服务配置
server:
port: 9001
spring:
application:
name: ihrm-company #指定服务名
#2.数据源配置
datasource:
driver-class-name: com.mysql.jdbc.Driver
url: jdbc:mysql://localhost:3306/ihrm_parent?useUnicode=true&characterEncoding=utf8
username: root
password: 111111
#3.JPA配置
jpa:
database: MySQL
show-sql: true
open-in-view: true

画面 6:
@Entity
@Table(name = "co_company")
@Data
@AllArgsConstructor
public class Company implements Serializable {
private static final long serialVersionUID = 59482932079158219L;
//ID
private String id;
/**
* 公司名称
*/
private String name;
/**
* 企业登录账号ID
*/
private String managerId;
/**
* 当前版本
*/
private String version;
/**
* 续期时间
*/
private Date renewalDate;

画面 8:
@Entity
@Table(name = "co_company")
@Data
@AllArgsConstructor
public class Company implements Serializable {
private static final long serialVersionUID = 59482932079158219L;
//ID
private String id;
/**
* 公司名称
*/
private String name;
/**
* 企业登录账号ID
*/
private String managerId;
/**
* 当前版本
*/
private String version;
/**
* 续期时间
*/
private Date renewalDate;

画面 10:
private Date create_time;

画面 13:
@Entity
@Table(name = "co_company")
@Data
@AllArgsConstructor
public class Company implements Serializable {
private static final long serialVersionUID = 59482932079158219L;
//ID
private String id;
/**
* 公司名称
*/
private String name;
/**
* 企业登录账号ID
*/
private String managerId;
/**
* 当前版本
*/
private String version;
/**
* 续期时间
*/
private Date renewalDate;

画面 14:
@Entity
@Table(name = "co_company")
@Data
@AllArgsConstructor
public class Company implements Serializable {
private static final long serialVersionUID = 59482932079158219L;
//ID
private String id;
/**
* 公司名称
*/
private String name;
/**
* 企业登录账号ID
*/
private String managerId;
/**
* 当前版本
*/
private String version;
/**
* 续期时间
*/
private Date renewalDate;

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6: PPT 标题为“5.2.2 完成企业增删改查操作”，子标题为“（1）实体类（domain）”。

画面 11: PPT 标题为“5.2.2 完成企业增删改查操作”，子标题为“（1）实体类（domain）”，并显示了注解的说明，如 @Entity、@Table、@Data、@AllArgsConstructor 等。

画面 13: PPT 标题为“5.2.2 完成企业增删改查操作”，子标题为“（1）实体类（domain）”，并显示了注解的说明，如 @Entity、@Table、@Data、@AllArgsConstructor 等。

画面 14: PPT 标题为“5.2.2 完成企业增删改查操作”，子标题为“（1）实体类
