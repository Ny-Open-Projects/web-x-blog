# 20-用户管理：搭建系统微服务

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\20-用户管理：搭建系统微服务_【海量资源尽在 ubkz.com】.mp4
- 时长 5分6秒（音频 306s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好了基本的咱们这些概念性和设计思路上的一些内容我们都已经介绍过了之后呢接下来呢就可以把咱们权限设计所涉及到的这些元素的增伤感察咱们都给它搞定那我们接下来就可以给它来一个用户的基本增伤感察那对于用户的基本增伤感察呢其实在我们的系统当中
[00:26] 用户角色权限等等这些内容全部都是给它归纳到我们的系统我们微服务当中所以对于我们来说呢一会儿可能要创建一个新的微服务系统微服务里面包含这些相应的内容OK那接下来呢我们要完成的就是用户的一个管理那对于用户的管理来说呢我们准备从这么几个方面来做首先呢我们简单的做一个用户的一个分析那接着配置用户系统的这个微服务
[00:54] 那我们完成后端的代码和前端用户操作代码的一个实现那对于咱们的用户来说咱们现在完成的是一个用户基本增伸改查的这么一个操作那我们首先看一下它这个表那这边呢已经把这个表的结构跟各位都放到这边了用户表那对于用户表来说呢其中没有什么值得各位特别重点关注的其中有这么一项一个叫做company id企业的id一个叫做company name
[01:24] 就是我们企业名称因为一个用户必然要归属某一个企业那除了这个之外呢还有一个需要各位要注意就是department就是部门那对于一个用户来说必然从属于某一个部门所以到时候我们会做部门分配员工的时候咱们会用到这些资段那对于用户来说没有什么可说的那还有一些表啊比如说呢刚才我们分析到的角色表
[01:51] 比如说我们分析到的权限表菜单表等等等等这些呢全部都在今天的资料当中一并给各位下发了那些表其实都比较简单就是遵守我们刚才下发的这个规则其实就可以了好了那这个基本的需求我们做了一个分析咱们也看了一下这个基本的表那么我们接下来要完成的事情就是可以搭建一个系统微服因为我们刚才说过了所有的这些内容全部是在系统微服当中有体现那我这边呢打开我的
[02:22] idea这些受影响的目录全部都关掉那我在pattern下边创建一个新的模块OK就叫做IHRM下发线SSTM系统微幅模块好了点击nextOK点击finish好了系统微幅模块呢我们创建好了之后接下来呢我们应该引入相应的坐标
[02:48] 那这个坐标呢跟我们企业微服的坐标基本上都是一模一样我就把它Ctrl C直接call到这边了OK这边呢全部都关掉那接下来对于咱们创建一个微服务来说呢咱们还需要创建启动类还有它的配置文件那配置文件跟执行代码基本上都是大同小异的我也从之前的这边Ctrl Ccall过来一个配置文件
[03:18] OK这个配置文件我们现在这个服务启动的端口叫做9002好了指定服务名称System好了这边的访问的数据库呢我们这边呢都用的是一个数据库当然了我们最后会想办法对它做一个分库的一个处理好了这边呢配置文件我们也配置成功了那接着我们需要创建一个启动类好了把这个启动类呢就放到com.ihm.
[03:52] SystemS-Y-S-T-E-M这个包下我就叫做S-Y-S-T-E-MApplicationOK好了那在这个系统微服务当中呢这个代码呢和我们之前搭建企业微服务是一模一样的这边呢代码都是一样我就从上面的代码直接拷过来了Ctrl-C Ctrl-V要做两件事配置包扫描以及GPA注解的包扫描那对于GPA注解的包扫描呢我们现在就不能访问company这个包下了我们现在有了一个新的微服务
[04:26] 那新的微服务呢我就把它放到创建一个包吧com.ihrm.domain.我们这回呢叫做sostemsystem那我这边扫描的就是sostemok那这样一来我基本的注解配置好了那接下来呢给它指定我们的启动方法以及我们的idworker雪花算法这都是一模一样的为了简单我就直接call了
[04:58] OK那这样以来我这个v服务的基本模块搭建咱们就已经搭建成功了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解基于角色的访问控制（RBAC）模型在Saas系统用户权限管理中的设计与实现，包括数据库表结构、权限模型图、项目模块划分及Spring Boot应用配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT第21页，标题为“2.1 什么是RBAC”，内容解释RBAC（Role-Based Access Control）模型，即基于角色的权限访问控制，强调权限与角色关联，用户通过角色获得权限。
画面2：展示PPT第22页，标题为“2.2 基于RBAC的设计思路”，内容说明基于角色的访问控制基本原理是在用户和访问权限之间加入角色层，实现用户和权限的分离。
画面3：展示PPT第4.1节“需求分析”，内容说明用户是Saas企业访问的员工，对员工完成基本的CRUD操作，并列出“bs_user”表结构。
画面4：展示PPT第4.1节“需求分析”，内容为“bs_user”表结构的SQL语句，包含字段定义和注释。
画面5：展示PPT第4.1节“需求分析”，内容为“bs_user”表结构的SQL语句，包含字段定义和注释。
画面6：展示PPT第3.3节“表结构分析”，内容为一个权限模型图，图中包含“孙七”、“周八”、“营销专员”等节点，以及“分配角色”、“分配权限”、“指定权限资源关系”等关系，下方文字说明权限表与权限菜单表、页面元素表与API接口表都是一对一的关系。
画面7：展示IntelliJ IDEA中“BaseExceptionHandler.java”文件的代码，内容为一个异常处理器类。
画面8：展示IntelliJ IDEA中“New Module”对话框，内容为创建新模块的界面。
画面9：展示IntelliJ IDEA中“pom.xml”文件的内容，内容为“ihrm_system”模块的依赖配置。
画面10：展示IntelliJ IDEA中“pom.xml”文件的内容，内容为“ihrm_system”模块的依赖配置。
画面11：展示IntelliJ IDEA中“Project”视图，内容为“ihrm_system”模块的目录结构。
画面12：展示IntelliJ IDEA中“CompanyApplication.java”文件的内容，内容为公司应用的启动类。
画面13：展示IntelliJ IDEA中“SystemApplication.java”文件的内容，内容为系统应用的启动类。
画面14：展示IntelliJ IDEA中“SystemApplication.java”文件的内容，内容为系统应用的启动类。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面3、4、5：
CREATE TABLE `bs_user` (
`id` varchar(40) NOT NULL COMMENT 'ID',
`mobile` varchar(40) NOT NULL COMMENT '手机号码',
`username` varchar(255) NOT NULL COMMENT '用户名',
`password` varchar(255) DEFAULT NULL COMMENT '密码',
`enable_state` int(2) DEFAULT '1' COMMENT '启用状态 0是禁用,1是启用',
`create_time` datetime DEFAULT NULL COMMENT '创建时间',
`department_id` varchar(40) DEFAULT NULL COMMENT '部门ID',
`time_of_entry` datetime DEFAULT NULL COMMENT '入职时间',
`form_of_employment` int(1) DEFAULT NULL COMMENT '聘用形式',
`work_number` varchar(20) DEFAULT NULL COMMENT '工号',
`form_of_management` varchar(8) DEFAULT NULL COMMENT '管理形式',
`working_city` varchar(16) DEFAULT NULL COMMENT '工作城市',
`correction_time` datetime DEFAULT NULL COMMENT '转正时间',
`in_service_status` int(1) DEFAULT NULL COMMENT '在职状态 1.在职 2.离职',
`company_id` varchar(40) DEFAULT NULL COMMENT '企业ID',
`department_name` varchar(40) DEFAULT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `idx_user_phone` (`mobile`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

画面6：
CREATE TABLE `bs_user` (
`id` varchar(40) NOT NULL COMMENT 'ID',
`mobile` varchar(40) NOT NULL COMMENT '手机号码',
`username` varchar(255) NOT NULL COMMENT '用户名',
`password` varchar(255) DEFAULT NULL COMMENT '密码',
`enable_state` int(2) DEFAULT '1' COMMENT '启用状态 0是禁用,1是启用',
`create_time` datetime DEFAULT NULL COMMENT '创建时间',
`department_id` varchar(40) DEFAULT NULL COMMENT '部门ID',
`time_of_entry` datetime DEFAULT NULL COMMENT '入职时间',
`form_of_employment` int(1) DEFAULT NULL COMMENT '聘用形式',
`work_number` varchar(20) DEFAULT NULL COMMENT '工号',
`form_of_management` varchar(8) DEFAULT NULL COMMENT '管理形式',
`working_city` varchar(16) DEFAULT NULL COMMENT '工作城市',
`correction_time` datetime DEFAULT NULL COMMENT '转正时间',
`in_service_status` int(1) DEFAULT NULL COMMENT '在职状态 1.在职 2.离职',
`company_id` varchar(40) DEFAULT NULL COMMENT '企业ID',
`department_name` varchar(40) DEFAULT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `idx_user_phone` (`mobile`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

画面7：
public class BaseExceptionHandler {
@ExceptionHandler
public Result error(HttpServletResponse request, HttpServletRequest response, Exception e) {
if (e.getClass() == CommonException.class) {
CommonException ce = (CommonException) e;
Result result = new Result(ce.getResultCode());
return result;
} else {
Result result = new Result(ResultCode.SERVER_ERROR);
return result;
}
}

画面9：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://maven.apache.org/xsi/schemas/maven-4.0.0.xsd"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<parent>
<artifactId>ihrm_parent</artifactId>
<groupId>com.ihrm</groupId>
<version>1.0-SNAPSHOT</version>
</parent>
<artifactId>ihrm_system</artifactId>
<dependencies>
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
</dependency>
<dependency>
<groupId>com.ihrm</groupId>
<artifactId>ihrm_common_model</artifactId>
<version>1.0-SNAPSHOT</version>
</dependency>
<dependency>
<groupId>com.ihrm</groupId>
<artifactId>ihrm_common_model</artifactId>
<version>1.0-SNAPSHOT</version>
</dependency>
</dependencies>
</project>

画面12：
package com.ihrm.company;
import com.ihrm.company;
//1.配置Spring Boot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm")
//2.配置jpa的扫描
@EntityScan(value = "com.ihrm.domain.company")
public class CompanyApplication {
//启动方法
public static void main(String[] args) { SpringApplication.run(CompanyApplication.class, args); }
@Bean
public IdWorker idWorker() { return new IdWorker(); }
}

画面13：
package com.ihrm.system;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.boot.context.annotation.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
//1.配置Spring Boot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm")
//2.配置jpa的扫描
@EntityScan(value = "com.ihrm.domain.system")
public class SystemApplication {
//启动方法
public static void main(String[] args) { SpringApplication.run(SystemApplication.class, args); }
@Bean
public IdWorker idWorker() { return new IdWorker(); }
}

画面14：
package com.ihrm.system;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.Bean;
//1.配置Spring Boot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm")
//2.配置jpa的扫描
@EntityScan(value = "com.ihrm.domain.system")
public class SystemApplication {
//启动方法
public static void main(String[] args) { SpringApplication.run(SystemApplication.class, args); }
@Bean
public IdWorker idWorker() { return new IdWorker(); }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“2.1 什么是RBAC”，内容为RBAC（Role-Based Access Control）模型的定义和解释。
画面2：标题为“2.

