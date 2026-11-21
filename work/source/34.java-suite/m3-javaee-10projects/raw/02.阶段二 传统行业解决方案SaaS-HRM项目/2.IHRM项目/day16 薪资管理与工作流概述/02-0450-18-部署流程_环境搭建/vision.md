# 画面线理解：18-部署流程：环境搭建

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\18-部署流程：环境搭建_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:23, 00:44, 02:58, 03:23, 03:42, 03:50, 04:20, 05:18, 05:59, 06:20, 06:29, 07:06, 07:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:56:24

1) 这一组画面整体在讲如何使用 Activiti 工作流引擎进行请假流程的设计、部署与配置，包括使用官方 Web 工具绘制流程图、在 Spring Boot 项目中集成 Activiti、配置数据库及服务注册等。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Activiti Editor 中的请假流程图，包含“提交申请”、“中间审批”、“复审”三个任务节点，以及一个“否”分支指向“领导审批”节点，最终汇入结束节点。
画面2：PPT 页面，标题为“4.2 流程制作工具”，列出制作流程的几种方式：手写XML文件、基于DEA的activiti插件、通过Java编程生成XML文件、基于Activiti官方提供的activiti-app工具包。
画面3：PPT 页面，标题为“4.4 流程部署”，说明在流程设计完成后，可先上传文件到服务器，再将流程定义文件部署到Activiti引擎中。
画面4：PPT 页面，标题为“4.4.2 流程部署”，展示“网关中加入相应配置”的代码片段，包含“path”、“serviceId”、“stripPrefix”、“customSensitiveHeaders”等配置项。
画面5：IntelliJ IDEA 中打开项目“ihrm_parent”的界面，显示项目结构。
画面6：Windows 资源管理器中，右键点击“04请假流程”文件夹，弹出菜单，显示“复制”、“粘贴”等选项。
画面7：IntelliJ IDEA 中打开“ihrm_audit”模块的“pom.xml”文件，显示引入的依赖项，包括“spring-cloud-starter-openfeign”、“activiti-spring-boot-starter”、“junit”、“commons-fileupload”等。
画面8：IntelliJ IDEA 中弹出“Copy”对话框，提示将文件复制到“E:\ihrm\ihrm_parent\ihrm_audit\src\main\java\com\ihrm\audit”目录。
画面9：IntelliJ IDEA 中弹出“Copy”对话框，提示将文件复制到“E:\ihrm\ihrm_parent\ihrm_audit\src\main\resources”目录，新文件名为“application.yml”。
画面10：IntelliJ IDEA 中打开“application.yml”文件，显示数据库配置（act、ihrm、redis）和Activiti配置（history-level、db-history-used）。
画面11：PPT 页面，标题为“4.4.1 环境搭建”，显示“ihrm_audit”模块的目录结构和依赖项。
画面12：IntelliJ IDEA 中打开“ihrm_gate”模块的“application.yml”文件，显示多个服务的配置，如“ihrm-employee”、“ihrm-social-securitys”、“ihrm-attendance”等。
画面13：SQLyog 数据库管理工具界面，显示“CREATE TABLE”语句，创建“act_ge_bytearray”表，以及“act_re_procdef”表的“ID_”字段值。
画面14：PPT 页面，标题为“4.4.1 环境搭建”，显示“ihrm_audit”模块的目录结构和依赖项。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：无代码或配置。
画面2：无代码或配置。
画面3：无代码或配置。
画面4：
```
ihrm-user-audit:
  path: /user/** #配置URL和URL的请求头
  serviceId: ihrm-audit #指定Eureka注册中心中的服务id
  stripPrefix: false
  sensitiveHeaders:
    customSensitiveHeaders: true
```
画面5：无代码或配置。
画面6：无代码或配置。
画面7：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring-boot-starter</artifactId>
    <version>7.0.0.1</version>
</dependency>
<dependency>
    <groupId>org.junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-image-generator</artifactId>
    <version>7.1.0.M2</version>
    <exclusions>
        <exclusion>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId>
    <version>1.3.3</version>
</dependency>
```
画面8：无代码或配置。
画面9：无代码或配置。
画面10：
```yaml
datasource:
  act:
    jdbc-url: jdbc:mysql://localhost:3306/act?useUnicode=true&characterEncoding=utf8&serverTimezone=GMT
    username: root
    password: 111111
    driver-class-name: com.mysql.jdbc.Driver
  ihrm:
    jdbc-url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8&serverTimezone=GMT
    username: root
    password: 111111
    driver-class-name: com.mysql.jdbc.Driver
  redis:
    host: 127.0.0.1
    port: 6379
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true
  activiti:
    history-level: full
    db-history-used: true
  eureka:
    client:
      serviceUrl: http://localhost:8888/eureka/
      instance:
        preferIpAddress: true
        instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
```
画面11：无代码或配置。
画面12：
```yaml
ihrm-employee:
  path: /employees/** #配置URL的请求规则
  serviceId: ihrm-employee #指定Eureka注册中心中的服务id
  stripPrefix: false
  sensitiveHeaders:
    customSensitiveHeaders: true
ihrm-social-securitys:
  path: /social-securitys/** #配置URL的请求规则
  serviceId: ihrm-social-securitys #指定Eureka注册中心中的服务id
  stripPrefix: false
  sensitiveHeaders:
    customSensitiveHeaders: true
ihrm-attendance:
  path: /cfg/** #配置URL的请求规则
  serviceId: ihrm-attendance #指定Eureka注册中心中的服务id
  stripPrefix: false
  sensitiveHeaders:
    customSensitiveHeaders: true
```
画面13：
```sql
CREATE TABLE `act_ge_bytearray` (
  `ID_` varchar(64) NOT NULL COMMENT '主键',
  `REV_` int(11) DEFAULT NULL COMMENT '版本',
  `NAME_` varchar(255) DEFAULT NULL COMMENT '名称',
  `DEPLOYMENT_ID_` varchar(64) DEFAULT NULL COMMENT '部署ID',
  `BYTES_` longblob COMMENT '字节',
  `CREATE_TIME_` datetime DEFAULT NULL COMMENT '创建时间',
  `UPDATE_TIME_` datetime DEFAULT NULL COMMENT '更新时间',
  `DELETE_TIME_` datetime DEFAULT NULL COMMENT '删除时间',
  PRIMARY KEY (`ID_`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
```
画面14：无代码或配置。

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：PPT 标题为“4.2 流程制作工具”，内容为制作流程的几种方式。
画面3：PPT 标题为“4.4 流程部署”，内容为流程部署的步骤。
画面4：PPT 标题为“4.4.2 流程部署”，内容为网关中加入的配置。
画面11：PPT 标题为“4.4.1 环境搭建”，内容为“ihrm_audit”模块的目录结构和依赖项。
画面12：PPT 标题为“4.4.1 环境搭建”，内容为“ihrm_audit”模块的目录结构和依赖项。
画面13：无PPT标题或架构图。

5) 无评价，无无关内容。
