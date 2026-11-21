# 画面线理解：10-审批业务概述：数据库表分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\10-审批业务概述：数据库表分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:51, 02:37, 04:49, 05:22, 05:39, 06:05, 06:35, 07:08, 07:33, 07:50, 08:22, 08:50, 10:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:06:30

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中核心业务数据表（如 proc_instance、proc_task_instance、proc_user_group）的结构与作用，以及如何通过数据库表理解流程实例和任务的存储机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的“2 业务流程概述”页面，介绍流程相关概念，如审批列表查询、流程申请信息查询、发起流程、提交流程等。
画面 2: 在 SQLyog 数据库工具中，展示“proc_instance”表的结构，包含字段如 process_id, process_name, process_state, user_id 等。
画面 3: 在 SQLyog 中，鼠标悬停在“proc_instance”表的“process_id”字段上，弹出字段详细信息。
画面 4: 在画图软件中，展示“Activiti内置数据库”与“iHRM系统的业务数据表”的对比图，用红色箭头标注“proc_instance”指向“当前节点(实时更新)”。
画面 5: 与画面 4 相同，但鼠标光标在“proc_instance”字段上。
画面 6: 与画面 4 相同，但鼠标光标在“proc_instance”字段上。
画面 7: 在 SQLyog 中，展示“proc_task_instance”表的结构，包含字段如 task_id, assignee, handle_user_name 等。
画面 8: 与画面 7 相同，但鼠标光标在“proc_task_instance”表的“task_id”字段上。
画面 9: 与画面 4 相同，但鼠标光标在“proc_task_instance”字段上。
画面 10: 在 SQLyog 中，展示“proc_user_group”表的结构，包含字段如 user_id, department_id 等。
画面 11: 与画面 4 相同，但鼠标光标在“proc_user_group”字段上。
画面 12: 与画面 4 相同，但鼠标光标在“proc_user_group”字段上。
画面 13: 在浏览器中打开 Activiti Editor 的“Procedures”页面，显示“Business Process Models”界面。
画面 14: 与画面 4 相同，但鼠标光标在“proc_user_group”字段上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2 中的 SQL 表结构：
```sql
CREATE TABLE `proc_instance` (
  `process_id` varchar(45) NOT NULL COMMENT '流程ID',
  `process_name` varchar(200) DEFAULT NULL COMMENT '流程名称',
  `process_state` varchar(45) DEFAULT NULL COMMENT '流程状态',
  `user_id` varchar(45) DEFAULT NULL COMMENT '用户ID',
  `proc_apply_time` datetime DEFAULT NULL COMMENT '申请时间',
  `proc_cur_node_user_id` varchar(45) DEFAULT NULL COMMENT '当前节点用户ID',
  `proc_node_id` varchar(45) DEFAULT NULL COMMENT '节点ID',
  `proc_data` text COMMENT '流程数据',
  `department_id` varchar(45) DEFAULT NULL COMMENT '部门ID',
  `department_name` varchar(200) DEFAULT NULL COMMENT '部门名称',
  `time_of_entry` datetime DEFAULT NULL COMMENT '进入时间',
  PRIMARY KEY (`process_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 7 中的 SQL 表结构：
```sql
CREATE TABLE `proc_task_instance` (
  `task_id` varchar(45) NOT NULL COMMENT '任务ID',
  `assignee` varchar(45) DEFAULT NULL COMMENT '任务处理人',
  `handle_user_name` varchar(200) DEFAULT NULL COMMENT '处理人姓名',
  `handle_user_id` varchar(45) DEFAULT NULL COMMENT '处理人ID',
  `handle_type` varchar(45) DEFAULT NULL COMMENT '处理类型',
  `process_id` varchar(45) DEFAULT NULL COMMENT '流程ID',
  `proc_node_id` varchar(45) DEFAULT NULL COMMENT '节点ID',
  `proc_cur_node_user_id` varchar(45) DEFAULT NULL COMMENT '当前节点用户ID',
  `proc_data` text COMMENT '流程数据',
  `department_id` varchar(45) DEFAULT NULL COMMENT '部门ID',
  `department_name` varchar(200) DEFAULT NULL COMMENT '部门名称',
  `time_of_entry` datetime DEFAULT NULL COMMENT '进入时间',
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 10 中的 SQL 表结构：
```sql
CREATE TABLE `proc_user_group` (
  `user_id` varchar(45) NOT NULL COMMENT '用户ID',
  `department_id` varchar(45) DEFAULT NULL COMMENT '部门ID',
  `department_name` varchar(200) DEFAULT NULL COMMENT '部门名称',
  `user_name` varchar(200) DEFAULT NULL COMMENT '用户名',
  `user_type` varchar(45) DEFAULT NULL COMMENT '用户类型',
  `user_status` varchar(45) DEFAULT NULL COMMENT '用户状态',
  `user_role` varchar(45) DEFAULT NULL COMMENT '用户角色',
  `user_position` varchar(200) DEFAULT NULL COMMENT '用户职位',
  `user_phone` varchar(45) DEFAULT NULL COMMENT '用户电话',
  `user_email` varchar(200) DEFAULT NULL COMMENT '用户邮箱',
  `user_avatar` varchar(200) DEFAULT NULL COMMENT '用户头像',
  `user_create_time` datetime DEFAULT NULL COMMENT '用户创建时间',
  `user_update_time` datetime DEFAULT NULL COMMENT '用户更新时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4、5、6、9、11、12、14: 展示“Activiti内置数据库”与“iHRM系统的业务数据表”的对比图，其中：
- “proc_instance”指向“当前节点(实时更新)”。
- “proc_task_instance”指向“当前节点(实时更新)”。
- “proc_user_group”指向“当前节点(实时更新)”。
- “proc_instance”指向“业务流程的用户表”。
- “proc_task_instance”指向“业务流程的任务表”。
- “proc_user_group”指向“业务流程的用户表”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
