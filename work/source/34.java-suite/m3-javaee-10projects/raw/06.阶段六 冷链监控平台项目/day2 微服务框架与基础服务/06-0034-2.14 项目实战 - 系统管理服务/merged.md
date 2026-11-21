# 2.14 项目实战 - 系统管理服务

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.14 项目实战 - 系统管理服务_【海量资源尽在 666java.com】.mp4
- 时长 5分50秒（音频 350s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好,下面我们来给大家介绍一下冷链设备监控平台的系统管理服务也就是我们的Code-Admin这个系统那么系统管理服务主要包括以下这么几个功能第一个来讲的话是我们的企业管理那么企业管理就是针对于企业的增山改查的一些操作仓库管理是针对于仓库的增山改查操作那么主机的管理就是针对于主机的增山改查
[00:27] 而设备管理的就是针对于设备的增长改查操作整个项目呢是一个Spring Boot的应用它在我们的Unicore服务注册中心里边来进行配置或者说注册到我们的Unicore服务注册中心里边去那么这几个实体的关系是什么呢一个企业它可能包含有几个或者拥有了几个仓库那么一个仓库呢会拥有几个或一个或多个的这样的一个主机那么一个主机呢它管理的多个设备
[00:56] 那么还有一块是我们的设备模拟器设备模拟器我们会详细给大家讲解那么前面这四个主体这四个实体呢其实都是基本的登山改查操作我们在这里不给大家做代码的一个演示了那么我们先看一下这几个的呃业务模型或数据模型第一个来讲的话叫CZ CompanyCZ Company就是公司企业它的一些基本的一些属性啊字段那么CZ
[01:22] warehouse指的是我们的仓库仓库的一些基本的属性和基本的一些字段那么cchost就是我们的主机了ccmatter就是我们的设备另外一个是我们的ccmessage realtimeccmessage realtime我们在系统管理里边并没有用到它它是在我们的Flink的实时计算的结果会放到我们的ccmessage realtime里边去
[01:47] 我们看一看代码结构代码结构和我们的code user的代码结构是一样的前端调用请求请求的是我们整个服务它的一个Controller而这个Controller层会调用我们的Service层Service层会引用我们整个的这个实体层和道层而实体层和道层呢是放在我们的code common这个工程里面去的那么我们code common工程里面的resultpager utils这些这几个类呢其实会
[02:16] 被我们整个code admin工程调用的我们来看一下我们的实战步骤首先呢我们需要创建我们的数据库这个数据库的名字呢就叫做code-admin然后呢我们需要在我们的这个mycircle客户端里边导入我们的code-admin这个circle文件而这个文件在我们原代码的一个dock
[02:42] 文件夹里边有一个src文件夹这个src文件夹里边有一个code-admin这个src文件那么第二步的话我们创建一个sprintboot的工程我们可以使用starter.spring.io这个网站来创建这个网站里边我们可以选择我们的sprintboot的工程路径工程的一个版本然后呢输入我们的group id和
[03:12] artifact idartifact id我们可以输入code-admin然后相应的在这里边的我们code-admin的话也是一个点然后相应的我们需要添加的是什么需要添加因为本身这个服务要注册到我们的服务处的中心里边所以我们需要选择一个Uric的discovery client而紧接着下一步的话我们要在我们的POM文件里边创建完了我们的工程之后
[03:40] 紧接着我们需要在我们的泡沫文件里边添加对于code common的一个引用那么code common中这个工程里边我们要添加一些实体和道层而这些实体呢就是刚才我们给大家看到的数据模型里边的CZ companyCZ warehouseCZ host和CZ matter那接着下一步我们在我们code admin这个工程里边添加controllercontroller里边其实就是一个增删改查对吧然后
[04:09] 查询的话会查询单条的和查询一个list那么Service就是对于到层的操作我查进行查询进行登山改查操作那么创建完之后我们可以把服务启动起来看看服务是否在我们的优势可服务处的中心里面添加上然后我们用postman测试每一个接口那么这些测试完成之后呢我们在网关服务里面也就是说我们上面讲的前面讲的我们的code gateway这个工程里面
[04:37] 添加对于codeadmin的工程的路由配置而这个路由配置其实和我们其他的这个路由配置可以参照我们对user路由配置的一个添加在这里边我们添加一个新的ID比如说我们叫做codecodeadmin而这个codeadmin大家要注意这个对齐方式如果它不对齐的话它会有问题的然后这里边其实就叫codeadmin
[05:10] 然后我们的工程名字就codeadmin然后剩下的其实就是我们的codeadmin里边的URL这个URL的话我们大家自己写的其实就可以自己来做的一些codeadmin这样的一个路径当然这个路径依赖于自己我们自己添加的工程的到底是什么样子的那么添加完了之后我们再执行一遍测试看看调用我们的网关然后调用相应的接口是否能正确的返回结果
[05:41] 这是我们的一个实战的情况给大家做的一个讲解大家在操作过程中具体来开发我们代码就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲冷云（cold-admin）系统管理模块的架构设计、数据模型、代码结构及实战部署步骤。

2) 按时间顺序列出每张画面的要点：
画面1：展示“7 系统管理 (cold-admin)”模块的架构图，包含“企业管理”、“仓库管理”、“主机管理”、“设备管理”、“设备模拟器”等子模块，以及对应的数据模型（cc_company, cc_warehouse, cc_host, cc_meter, cc_message_realtime）。
画面2：展示数据模型的详细字段，包括各表的主键、字段名、类型和注释。
画面3：展示代码结构图，包含cold-ui、cold-user、Spring Boot容器、cold-common等模块，以及Controller、Service、Dao、Entity等组件。
画面4：展示代码结构图的细节，包括cold-user模块中的Controller、ServiceImpl、Service，以及cold-common模块中的Dao、Entity、Result、PageUtils、TokenGenerator。
画面5：展示实战步骤，包括创建数据库、导入cold-admin.sql文件、创建Spring Boot工程、添加依赖、添加实体和dao、添加Controller和服务代码、运行测试工程。
画面6：展示Eureka服务注册中心页面，显示已注册的服务实例，包括COLD-EUREKA-SERVER、COLD-GATEWAY、COLD-USER。
画面7：展示Spring Initializr创建项目页面，选择包名com.ithema.cold.gateway，打包方式为Jar，Java版本为11，选择依赖Gateway和Eureka Discovery Client。
画面8：展示Spring Initializr创建项目页面，选择包名com.ithema.cold.admin，打包方式为Jar，Java版本为11，选择依赖Gateway和Eureka Discovery Client。
画面9：展示实战步骤，包括创建数据库、导入cold-admin.sql文件、创建Spring Boot工程、添加依赖、添加实体和dao、添加Controller和服务代码、运行测试工程、完成配置。
画面10：展示数据模型的详细字段，包括各表的主键、字段名、类型和注释。
画面11：展示cold-gateway项目的application.yml配置文件，包含predicates和filters的配置。
画面12：展示实战步骤，包括创建数据库、导入cold-admin.sql文件、创建Spring Boot工程、添加依赖、添加实体和dao、添加Controller和服务代码、运行测试工程、完成配置。
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

