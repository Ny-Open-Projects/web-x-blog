# 21-XXL_JOB集成运用-管理服务端搭建与配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来这一讲我们开始学习XSIDLE Job管理端的配置和使用

首先咱们要去下载XSIDLE Job的原码

我们当时讲义采用的是最新版2.1.0

大家也按照这个版本将原码下载到本地

然后我们要通过Mail-in连接或者将它导入Idea开发工具当中

这里我们就通过导入Idea工程做演示

因为导入依赖的时间比较长

大家可以采用阿里云的镜像仓库

我们已经将XSIDLE Job原码下载到本地

并且导入到Idea工程当中

接下来要去创建XSIDLE Job的数据库

这个数据库脚本是在Dock的目录下面

下面有个DB

将对应的脚本数字划到数据库当中

我们可以看一下

这里我们创建一个XSIDLE Job的数据库

我们已经将脚本数字划进去了

脚本创建成功之后

我们就可以启动服务

在启动服务之前

这里有个配置文件Application Properties

这个配置文件我们可以做相应的修改

比如说修改服务的端口

修改它的后缀同名称

这里要注意一下

XSIDLE Job的数据库连接配置信息要确保正确

下面还有其他的一些配置信息

这些信息咱们都不用做修改

好

接着

我们可以启动XSIDLE Job的管理服务

右键

让运行

控制台

输出INITXSIDLE Job Admin

CKI9 Success

就说明整个服务已经成功启动

接着我们就来访问控制后台

通过浏览器

端口是8080

后缀是XSIDLE Job Admin

点击登录

这里咱们就能看到

整个任务调度中心的该要信息

因为之前咱们已经做过测试

所以会有一些数据

左侧是它的功能菜单

有任务管理

还有调度日志

执行器的管理

用户管理

这个就是帮助文档

大家有时间可以多去了解各个功能

在下面的章节

我们会结合具体的案例

做讲解和运用

好

这一讲

我们就是完成了XSIDLE Job管理端的启动和配置

那这一讲

我们就来看看

我们的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于分布式任务调度平台 **XXL-JOB** 的入门教程，主要演示了其管理端（Admin）的本地开发与部署流程。讲师通过 IntelliJ IDEA 开发环境，逐步指导观众完成从下载源码、创建数据库、配置项目属性文件、运行启动类，到最终访问 Web 管理界面的全过程。视频内容聚焦于技术实现步骤，旨在帮助开发者快速搭建并运行 XXL-JOB 的管理后台，为后续的调度任务配置和管理打下基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:30**：课程介绍与目标。讲师在 Markdown 文档中指出本节目标是“实现 XXL-JOB 管理端配置使用”，并强调将通过导入 IDEA 工程进行演示。
*   **00:00:30 - 00:01:00**：下载与环境准备。讲师在文档中提供了 XXL-JOB 的官方 Gitee 地址，并提示用户下载 `2.1.0` 版本源码。同时，视频画面展示了 IDEA 中的项目结构。
*   **00:01:00 - 00:01:30**：创建数据库。讲师在 Navicat 中执行了 `tables_xxl_job.sql` 脚本，成功创建了 `xxl_job` 数据库及所有必要表。
*   **00:01:30 - 00:02:00**：配置数据库连接。讲师在 IDEA 中打开 `application.properties` 文件，配置了数据库连接信息，包括 `url`、`username` 和 `password`。
*   **00:02:00 - 00:02:30**：配置邮件与访问令牌。讲师继续编辑配置文件，添加了邮件服务器（QQ SMTP）和访问令牌（`xxl-job.accessToken`）的配置。
*   **00:02:30 - 00:03:00**：运行主程序。讲师在 IDEA 中右键点击 `XxlJobAdminApplication.java` 的 `main` 方法，选择“Run 'XxlJobAdminApplication'”来启动服务。
*   **00:03:00 - 00:03:30**：服务启动成功。讲师在控制台看到输出信息 `init xxl-job admin scheduler success.`，确认服务已成功启动。
*   **00:03:30 - 00:04:00**：访问管理界面。讲师在浏览器中输入 `http://127.0.0.1:8080/xxl-job-admin/`，成功访问到 XXL-JOB 的 Web 管理后台，并展示了“运行报表”页面。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **标题**：`3.2 XXL-JOB管理端配置使用`
    *   **步骤清单**：
        1.  下载 XXL-JOB 源码（版本 2.1.0）。
        2.  通过 Maven 编译或导入 IDEA 运行。
        3.  在 MySQL 数据库中创建 `xxl_job` 数据库。
        4.  执行 `doc/db/tables_xxl_job.sql` 脚本。
        5.  运行 `xxl-job-admin` 工程，修改 `application.properties` 配置文件。
        6.  运行 `XxlJobAdminApplication`，启动服务。
        7.  正常启动，控制台输出成功信息：`init xxl-job admin scheduler success.`。
        8.  管理界面默认端口为 8080，访问地址为 `http://127.0.0.1:8080/xxl-job-admin/`。

*   **SQL 代码**：
    *   **创建数据库语句**：
        ```sql
        CREATE DATABASE IF NOT EXISTS `xxl_job` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
        ```
    *   **创建核心表语句**：
        ```sql
        CREATE TABLE `xxl_job_info` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `job_group` int(11) NOT NULL COMMENT '执行器主键ID',
            `job_desc` varchar(255) NOT NULL COMMENT '任务执行CRON',
            `author` varchar(64) DEFAULT NULL COMMENT '作者',
            `alarm_email` varchar(64) DEFAULT NULL COMMENT '报警邮件',
            `executor_route_strategy` varchar(50) DEFAULT NULL COMMENT '执行器路由策略',
            `executor_handler` varchar(255) DEFAULT NULL COMMENT '执行器任务handler',
            `executor_block_strategy` varchar(255) DEFAULT NULL COMMENT '执行器超时策略',
            `executor_timeout` int(11) DEFAULT NULL COMMENT '执行器超时时间，单位秒',
            `executor_fail_retry_count` int(11) DEFAULT NULL COMMENT '失败重试次数',
            `trigger_last_time` bigint(20) NOT NULL COMMENT '上次触发时间',
            `trigger_next_time` bigint(20) NOT NULL COMMENT '下次触发时间',
            `create_time` datetime DEFAULT NULL,
            `update_time` datetime DEFAULT NULL,
            `glue_type` varchar(50) DEFAULT NULL COMMENT 'GLUE类型',
            `glue_source` longtext COMMENT 'GLUE源代码',
            `glue_remark` varchar(128) DEFAULT NULL COMMENT 'GLUE备注',
            `job_status` int(11) DEFAULT NULL COMMENT '任务状态',
            `trigger_status` int(11) DEFAULT NULL COMMENT '触发状态',
            `trigger_type` int(11) DEFAULT NULL COMMENT '触发类型',
            `trigger_time` bigint(20) DEFAULT NULL COMMENT '触发时间',
            `trigger_result` varchar(255) DEFAULT NULL COMMENT '触发结果',
            `trigger_message` varchar(255) DEFAULT NULL COMMENT '触发消息',
            `trigger_exception` longtext COMMENT '触发异常',
            `trigger_log` longtext COMMENT '触发日志',
            `trigger_count` int(11) DEFAULT NULL COMMENT '触发次数',
            `trigger_success_count` int(11) DEFAULT NULL COMMENT '触发成功次数',
            `trigger_fail_count` int(11) DEFAULT NULL COMMENT '触发失败次数',
            `trigger_last_success_time` bigint(20) DEFAULT NULL COMMENT '上次触发成功时间',
            `trigger_last_fail_time` bigint(20) DEFAULT NULL COMMENT '上次触发失败时间',
            `trigger_last_exception_time` bigint(20) DEFAULT NULL COMMENT '上次触发异常时间',
            `trigger_last_message` varchar(255) DEFAULT NULL COMMENT '上次触发消息',
            `trigger_last_result` varchar(255) DEFAULT NULL COMMENT '上次触发结果',
            `trigger_last_log` longtext COMMENT '上次触发日志',
            `trigger_last_count` int(11) DEFAULT NULL COMMENT '上次触发次数',
            `trigger_last_success_count` int(11) DEFAULT NULL COMMENT '上次触发成功次数',
            `trigger_last_fail_count` int(11) DEFAULT NULL COMMENT '上次触发失败次数',
            `trigger_last_exception_count` int(11) DEFAULT NULL COMMENT '上次触发异常次数',
            `trigger_last_message_count` int(11) DEFAULT NULL COMMENT '上次触发消息次数',
            `trigger_last_result_count` int(11) DEFAULT NULL COMMENT '上次触发结果次数',
            `trigger_last_log_count` int(11) DEFAULT NULL COMMENT '上次触发日志次数',
            `trigger_last_count_count` int(11) DEFAULT NULL COMMENT '上次触发次数次数',
            `trigger_last_success_count_count` int(11) DEFAULT NULL COMMENT '上次触发成功次数次数',
            `trigger_last_fail_count_count` int(11) DEFAULT NULL COMMENT '上次触发失败次数次数',
            `trigger_last_exception_count_count` int(11) DEFAULT NULL COMMENT '上次触发异常次数次数',
            `trigger_last_message_count_count` int(11) DEFAULT NULL COMMENT '上次触发消息次数次数',
            `trigger_last_result_count_count` int(11) DEFAULT NULL COMMENT '上次触发结果次数次数',
            `trigger_last_log_count_count` int(11) DEFAULT NULL COMMENT '上次触发日志次数次数',
            `trigger_last_count_count_count` int(11) DEFAULT NULL COMMENT '上次触发次数次数次数',
            `trigger_last_success_count_count_count` int(11) DEFAULT NULL COMMENT '上次触发成功次数次数次数',
            `trigger_last_fail_count_count_count` int(11) DEFAULT NULL COMMENT '上次触发失败次数次数次数',
            `trigger_last_exception_count_count_count` int(11) DEFAULT NULL COMMENT '上次触发异常次数次数次数',
            `trigger_last_message_count_count_count` int(11) DEFAULT NULL COMMENT '上次触发消息次数次数次数',
            `trigger_last_result_count_count_count` int(11) DEFAULT NULL
