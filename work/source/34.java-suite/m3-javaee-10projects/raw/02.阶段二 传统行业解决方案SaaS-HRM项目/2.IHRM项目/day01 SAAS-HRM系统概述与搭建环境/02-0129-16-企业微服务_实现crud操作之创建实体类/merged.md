# 16-企业微服务：实现crud操作之创建实体类

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\16-企业微服务：实现crud操作之创建实体类_【海量资源尽在 ubkz.com】.mp4
- 时长 8分11秒（音频 491s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了,实体类我们已经搭建成功了,那接下来我们就开始完成企业管理的基本CRUD操作。
[00:11] 那首先呢,需要跟各位来简单的介绍一下,那我们这个企业它的表究竟是什么样的?
[00:19] 在这边呢,已经对企业表的一个鉴表语句给各位准备好了,那其中对于一个企业来说,咱们有ID,还有企业的名称。
[00:30] 这边还有企业什么登录账号的ID还有当前使用的版本什么续期的时间因为我们说过我们这个企业来说是租用我们这个SaaS平台你租用我SaaS平台可能有一个你什么时候续的期什么时候到期等等
[00:47] 还有呢比如说你公司的地址在哪你公司的在什么区域华东华南等等你公司的地址还有你营业执照你的法人是谁你公司的联系电话邮箱公司规模10到15人还是一个大型公司这边呢还有你公司的所属行业备注是否已经审核那这个审核我需要跟各位来聊一下是这样的如果说你一个企业想要使用我这套SaaS平台
[01:16] 那你需要把你的企业资质提交给我那我验证没问题的话你才能使用所以我这边有一个审核状态那审核状态比如说零未审核未审核你就用不了那一审核审核才能用吗OKHello这边有一个还有一个叫做状态那这个状态其实指的是我当前企业是否可用是否不可用和这个审核是不一样的OK那接下来呢还有你当前企业的
[01:45] 余额因为我们说过了你要租租的话你得充点值充完值之后看一下你当这个月缴费之后还剩多少钱那其实这个余额是这样的就是说有可能到月之后按月你续租自动续租到月了我就从这个余额里面扣到月就可以从这个余额里面扣嘛
[02:04] 好了还有一个就是你当前企业的一个创建时间那这个实体这个企业表相对来说比较简单也没什么可说的那对于各位要做的事情呢很简单我们刚才配置当前企业的时候是不是指定了他这个数据库的一个地址啊那你在你相应的数据库下运行运行我们相应的这个伺候运行这个伺候语句创建数据库表哎就可以了
[02:33] 那当然了,我已经把我们这个数据库表所有的都已经把它创建到我的MySQL数据库里。
[02:43] 好了,在这边,我们现在用的表是CO下划线,这一边呢,我简单的创建了这么几套数据。
[02:53] OK,这个表结构是一模一样的,并且我配置也是叫做IHRM。
[03:00] 这个数据库当然了我们这边呢它的数据库表会比较多这些数据库表随着我们课程的深入我们一个一个的都会给各位讲解我们今天只用第一章competyok那数据库表做了一个分析我们回到我们的讲义里表做好了之后我们根据数据库表就开始要去完成我们企业的一个增产改查了那要想完成企业增产改查我们要做的事情呢其实一共就这么四步
[03:31] 这四步是我们很明确的四件事第一件事根据数据固表我们要创建实体类那实体类创建好了之后接着第二件事我们要写DODO写好了之后接着第三件事我们要写业务逻辑层Service那Service写好了之后我们就可以写我们的控制器也就是我们的Controller所以这四件事我们先明确那明确了这四件事我们一个一个的来看首先第一件事写一实体类
[04:00] 那我们这个实体类呢其实放到什么地方大家都比较明确我们需要把实体类放到我们抽取的一个公共模块下model那在这个model里面我们找到company模块名company没问题company这是我们的实体类刚才写了一半剩下的事情就是按照数据库表的字段名咱们去写属性了当然了这个过程它比较耗时
[04:29] 比较麻烦所以呢这个代码我也就不退一行一行去写在今天的资料当中我已经根据数据库表把基本的属性全部都写好了并且以注释的形式给各位提供好了Ctrl C把这段内容我直接拷过来Ctrl C把这段内容拷到我company这边Ctrl V
[05:00] 好了,拷过来之后呢,我需要倒下包,OK,那接着呢,对于我们而言,注意,对于我们而言,这是一实体类不假,但是我内部其实是使用,叫做使用GPA,GPA操作数据库,那要使用GPA招作数据库,我们应该要配置实体类和数据库表的叫做映射关系。
[05:39] 那配置映射关系我们借助的是JPA注解那JPA注解使用起来呢相对来说不难一共要做两方面的内容第一个实体类和表的映射关系第二个字段和属性的映射关系那当然了对于字段和属性映射关系我们关注的两方面第一个方面主件属性的映射
[06:14] 好了当然了还有第二个方面第二个方面就是普通属性的映射好了这些呢映射就是帮助各位回顾一下那当然了普通属性的映射如果说我们满足一定的写法的话比如说属性名和数据库字段有图封标志的这么一个对应有图封标志一个对应普通属性这些映射我们其实不写也可以OK好了这些我们基本都看过了之后接下来注意我们就可以首先来干第一件事实体内
[06:48] 和表的映射关系那实体类和表的映射关系首先ata entity注意别选错包JPA规范ata entity代表我要映射实体类接着at table你这个实体类和哪个数据库表创建映射关系table里面我们的写法其实比较简单来一name等于我们的数据库表的名称就可以了我数据库表叫做co下划线company我这边直接call过来
[07:23] 好了那这样一来第一个映射我们搞定了接下来第二个字段和属性字段和属性映射首先第一件事主键映射那主键映射不用多想就叫ID那怎么映射很简单就用一个注解ata ID即可当然了普通属性也可以去映射使用atacolum那里面可以指定你当前这个属性要映射成数据库里面的哪个字段比如说那一部属性我想映射成
[07:51] 数据库表里面的内幕好了我这边就写内幕字段即可当然了我说过普通属性如果满足一定的写法属性名一样或者满足图风标志的写法这边就可以省略OK那这样一来我实体内就已经创建好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

