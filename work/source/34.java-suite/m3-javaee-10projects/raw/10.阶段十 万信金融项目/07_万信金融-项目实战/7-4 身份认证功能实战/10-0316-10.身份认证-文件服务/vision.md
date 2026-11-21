# 画面线理解：10.身份认证-文件服务

- 阶段：10.阶段十 万信金融项目
- 章节：07_万信金融-项目实战/7-4 身份认证功能实战
- 源文件：10.阶段十 万信金融项目\07_万信金融-项目实战\7-4 身份认证功能实战\10.身份认证-文件服务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 02:04, 03:28, 03:59, 04:57, 05:59, 06:56, 08:04, 08:28, 09:19, 10:03, 11:00, 12:23, 13:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:56:36

1) 这一组画面整体在讲如何部署和配置一个用于处理文件上传下载的微服务，包括初始化数据库、配置数据源、注册七牛云对象存储服务、配置文件存储等步骤。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程文档目录，当前章节为“3 部署文件服务”，并提及“参考‘文件服务部署指南.pdf’”。
画面2: 展示初始化数据库的SQL语句，用于创建数据库和表。
画面3: 展示IDE中修改配置的步骤，标题为“2.3 修改配置(数据库)”。
画面4: 展示IDE中application.yml文件的配置内容，包含数据库连接参数。
画面5: 展示PPT页面，标题为“2.3 修改配置(数据库)”和“2.4 注册七牛云对象存储服务”，并包含七牛云官网链接。
画面6: 展示七牛云控制台界面，正在“新建存储空间”。
画面7: 展示七牛云控制台的“安全设置”页面，正在配置AccessKey和SecretKey。
画面8: 展示PPT页面，标题为“2.5 修改配置(文件存储)”。
画面9: 展示PPT页面，标题为“2.3 修改配置(数据库)”和“2.4 注册七牛云对象存储服务”，并包含七牛云官网链接。
画面10: 展示需求分析流程图，包含“网贷APP”、“用户中心”、“文件服务”、“百度AI平台”等模块及其交互。
画面11: 展示Apollo配置中心界面，显示“micro_service.files”命名空间下的配置项。
画面12: 展示Apollo配置中心界面，显示“micro_service.files”命名空间下的配置项。
画面13: 展示PPT页面，标题为“2.5 修改配置(文件存储)”。
画面14: 展示课程文档目录，当前章节为“4 使用百度AI服务”，并提及“4.1 注册并登录百度AI”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2 SQL:
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
CREATE DATABASE `p2p_file` CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
use p2p_file;
DROP TABLE IF EXISTS `fileobject`;
CREATE TABLE `fileobject` (
`ID` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
`Filename` varchar(20) DEFAULT NULL COMMENT '原文件名',
`origin` varchar(20) DEFAULT NULL COMMENT '存疑图',
`resourcekey` varchar(100) NOT NULL COMMENT '文件key',
`flag` varchar(10) NOT NULL COMMENT '正反面',
`downloadurl` varchar(200) DEFAULT NULL COMMENT '文件下载地址',
`isprotect` tinyint(1) NOT NULL COMMENT '公有还是私有',
`uploadate` datetime NOT NULL COMMENT '上传日期',
PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

画面4 application.yml:
add-mappings: true
mvc:
throw-exception-if-no-handler-found: true
servlet:
multipart:
max-request-size: 40
max-file-size: 40
datasource:
url: jdbc:mysql://localhost:3306/p2p_file?useUnicode=true
driver-class-name: com.mysql.cj.jdbc.Driver
username: root
password: 123
type: com.alibaba.druid.pool.DruidDataSource
druid:
max-pool-prepared-statement-per-connection-size: 20
min-idle: 3
web-stat-filter:
session-stat-enable: false
principal-cookie-name: admin
url-pattern: /*
session-stat-max-count: 1000

画面11/12 Apollo配置:
Key: my.file.url
Value: qiniu
Key: my.file.bucket
Value: p2p

4) PPT 标题、架构图/流程图的结构、表格数据：
画面10 流程图：
- “网贷APP” → “用户中心” → “文件服务” → “百度AI平台”
- “用户中心” → “文件服务” → “百度AI平台”
- “文件服务” → “百度AI平台”
- “百度AI平台” → “文件服务”
- “文件服务” → “用户中心”
- “用户中心” → “网贷APP”

画面11/12 Apollo配置表格：
| 发布状态 | Key | Value | 备注 | 最后修改人 | 最后修改时间 |
| --- | --- | --- | --- | --- | --- |
| 已发布 | my.file.url | qiniu | 七牛云存储地址 | apollo | 2019-06-27 18:42:28 |
| 已发布 | my.file.bucket | p2p | 七牛云中存储空间名称和项目名称一致 | apollo | 2019-06-27 18:44:28 |

5) 无
