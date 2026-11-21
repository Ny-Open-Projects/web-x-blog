# 画面线理解：20-用户管理：搭建系统微服务

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\20-用户管理：搭建系统微服务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:41, 01:00, 01:16, 01:33, 01:50, 02:23, 02:31, 02:57, 03:11, 03:40, 04:11, 04:40, 05:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:37:53

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
//1.配置springboot的包扫描
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
//1.配置springboot的包扫描
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
//1.配置springboot的包扫描
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
