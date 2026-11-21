# 画面线理解：2.14 项目实战 - 系统管理服务

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.14 项目实战 - 系统管理服务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:03, 01:36, 01:48, 02:16, 02:39, 02:58, 03:01, 03:23, 03:35, 03:51, 04:47, 05:31, 05:43, 05:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:59:49

1) 这一组画面整体在讲冷云（cold-admin）系统管理模块的架构设计、数据模型、代码结构及实战部署步骤。

2) 按时间顺序列出每张画面的要点：
画面1：展示“7 系统管理 (cold-admin)”模块的架构图，包含“企业管理”、“仓库管理”、“主机管理”、“设备管理”、“设备模拟器”等子模块，以及对应的数据模型（cc_company, cc_warehouse, cc_host, cc_meter, cc_message_realtime）。
画面2：展示数据模型的详细字段，包括各表的主键、字段名、类型和注释。
画面3：展示代码结构图，包含cold-ui、cold-user、SpringBoot容器、cold-common等模块，以及Controller、Service、Dao、Entity等组件。
画面4：展示代码结构图的细节，包括cold-user模块中的Controller、ServiceImpl、Service，以及cold-common模块中的Dao、Entity、Result、PageUtils、TokenGenerator。
画面5：展示实战步骤，包括创建数据库、导入cold-admin.sql文件、创建spring boot工程、添加依赖、添加实体和dao、添加controller和服务代码、运行测试工程。
画面6：展示Eureka服务注册中心页面，显示已注册的服务实例，包括COLD-EUREKA-SERVER、COLD-GATEWAY、COLD-USER。
画面7：展示Spring Initializr创建项目页面，选择包名com.ithema.cold.gateway，打包方式为Jar，Java版本为11，选择依赖Gateway和Eureka Discovery Client。
画面8：展示Spring Initializr创建项目页面，选择包名com.ithema.cold.admin，打包方式为Jar，Java版本为11，选择依赖Gateway和Eureka Discovery Client。
画面9：展示实战步骤，包括创建数据库、导入cold-admin.sql文件、创建spring boot工程、添加依赖、添加实体和dao、添加controller和服务代码、运行测试工程、完成配置。
画面10：展示数据模型的详细字段，包括各表的主键、字段名、类型和注释。
画面11：展示cold-gateway项目的application.yml配置文件，包含predicates和filters的配置。
画面12：展示实战步骤，包括创建数据库、导入cold-admin.sql文件、创建spring boot工程、添加依赖、添加实体和dao、添加controller和服务代码、运行测试工程、完成配置。
画面13：展示“7.1.1 需求分析”和“7.1.2 具体实现”部分，包括创建表cold_cc_company的SQL语句。
画面14：展示“7.1.1 需求分析”和“7.1.2 具体实现”部分，包括前端代码结构（cold-ui）和后端代码结构（cold-admin）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面11：
predicates:
  - Path=/cold/user/**
画面12：
CREATE TABLE `cold`.`cc_company` (
  `id` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '主键',
  `companyName` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '公司名称',
  `abbreviation` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '简称',
  `companyType` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '企业类型',
  `createdTime` timestamp(8) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updateTime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '修改时间',
  `status` int(11) NOT NULL DEFAULT '1' COMMENT '状态',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '备注',
  `companyCode` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '企业编码',
  `companyAddress` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '地址',
  `companyPhone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '联系电话',
  `managementName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '管理员姓名',
  `managementPhone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '管理员电话',
  `loader` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '负责人姓名',
  `loaderPhone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '负责人电话',
  `webAddress` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '网站',
  `companyLogo` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司logo',
  `companyEmail` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司邮箱',
  `companyUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网址',
  `companyWebsite` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT NULL COMMENT '公司网站链接',
  `companyWebsiteUrl` varchar(180) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
