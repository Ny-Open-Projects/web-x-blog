# 画面线理解：day16-8-易问技术-配置中心

- 阶段：10.阶段十 万信金融项目
- 章节：06_万信金融-项目总结&就业指导/6-1 项目技术总结
- 源文件：10.阶段十 万信金融项目\06_万信金融-项目总结&就业指导\6-1 项目技术总结\day16-8-易问技术-配置中心_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 04:03, 06:00, 06:07, 06:47, 07:50, 08:40, 09:23, 10:00, 10:04, 10:14, 10:19, 11:41, 12:40, 13:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:43:28

1) 这一组画面整体在讲什么是配置中心、传统配置方式存在的问题以及 Apollo 框架的原理和使用。

2) 按时间顺序列出每张画面的要点：
画面1：PPT标题为“3.1.1 什么是配置中心？为什么要使用它？”，内容为传统配置形式存在的问题，包括：缺少权限控制、缺少版本控制、缺少实时控制、微服务化和分布式带来的挑战。
画面2：PPT标题为“4. 微服务化和分布式带来的挑战”，展示一个简单的架构图，用户请求指向负载均衡（proxy）。
画面3：PPT内容为配置文件分散在各个服务节点的问题，以及配置中心的定义和作用。
画面4：展示一个微服务架构图，包含服务注册发现、配置中心、调用链监控、Metrics监控、健康检查和告警等组件。
画面5：与画面3内容相同，展示配置文件分散的问题和配置中心的定义。
画面6：PPT标题为“3.1.2 请简述Apollo框架原理”，内容为 Apollo 框架的介绍和工作原理图，图示为“应用程序”通过“获取配置、更新通知”与“Apollo客户端”交互。
画面7：浏览器显示 Apollo 登录页面，URL 为 http://111.103.136.242:7285/signin。
画面8：Apollo 配置中心界面，显示项目 application 的配置列表，包括 micro_service.spring-boot-http、micro_service.spring-eureka、micro_service.mybatis-plus、micro_service.spring-cloud-feign、micro_service.spring-hystrix。
画面9：显示 micro_service.spring-boot-http 的配置详情，包含 Key、Value、备注、最后修改人、最后修改时间等信息。
画面10：显示 micro_service.spring-boot-druid 的配置详情，包含 Key、Value、备注、最后修改人、最后修改时间等信息。
画面11：显示 micro_service.mybatis-plus 的配置详情，包含 Key、Value、备注、最后修改人、最后修改时间等信息。
画面12：显示 application 的配置详情，包含 Key、Value、备注、最后修改人、最后修改时间等信息。
画面13：与画面6内容相同，展示 Apollo 框架原理图。
画面14：PPT标题为“三、易问技术 3.1 配置中心 3.1.1 什么是配置中心？为什么要使用它？”，内容与画面1相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
无。

4) PPT 标题、架构图/流程图的结构、表格数据：
画面4架构图：
- 用户请求 → 负载均衡（proxy） → 服务节点（每个节点包含配置文件和服务）
- 服务节点 → 配置中心
- 配置中心 → 服务注册发现、调用链监控、Metrics监控、健康检查和告警等组件

画面6原理图：
- 应用程序 → Apollo客户端 → 获取配置、更新通知

画面8表格数据：
- micro_service.spring-boot-http
- micro_service.spring-eureka
- micro_service.mybatis-plus
- micro_service.spring-cloud-feign
- micro_service.spring-hystrix

画面9表格数据：
- Key: server.servlet.context-path
- Value: /depository-agent
- 备注: 已发布
- 最后修改人: apollo
- 最后修改时间: 2019-05-17 13:58:37

画面10表格数据：
- Key: spring.datasource.url
- Value: jdbc:mysql://111.103.136.242:2977/p/p_depository_agent?useUnicode=true
- 备注: 已发布
- 最后修改人: apollo
- 最后修改时间: 2019-07-16 16:53:39

画面11表格数据：
- Key: aop.aspectj.ajc.ajc
- Value: 10
- 备注: 已发布
- 最后修改人: apollo
- 最后修改时间: 2019-05-15 18:50:44

画面12表格数据：
- Key: p.p.privateKey
- Value: MII...（省略）
- 备注: 已发布
- 最后修改人: apollo
- 最后修改时间: 2019-05-17 10:34:32

5) 无。
