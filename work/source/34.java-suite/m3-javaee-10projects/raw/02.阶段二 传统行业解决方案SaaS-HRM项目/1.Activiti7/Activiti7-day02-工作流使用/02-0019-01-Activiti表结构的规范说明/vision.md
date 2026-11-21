# 画面线理解：01-Activiti表结构的规范说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\01-Activiti表结构的规范说明_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:48, 00:59, 01:18, 01:21, 01:31, 01:38, 02:34, 02:41, 03:00, 03:09, 03:34, 04:24, 04:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:18:10

1) 这一组画面整体在讲什么（一句话）：
演示 Activiti 工作流引擎的数据库表结构及其命名规则，通过 SQLyog 客户端查看表数据并结合 PPT 讲解表名含义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: SQLyog 客户端显示数据库连接，左侧树形结构选中表 act_ge_bytearray，右侧数据表显示 ID、REV、NAME、DEPLOYMENT_ID、BYTES、CREATED 等字段。
画面 2: PPT 页面标题为“3.3.7 数据库表的命名规则”，内容解释 ACT_RE_*、ACT_RU_*、ACT_HI_*、ACT_GE_* 的含义。
画面 3: SQLyog 客户端选中表 act_ge_bytearray，数据表显示字段包括 ID、REV、NAME、DEPLOYMENT_ID、BYTES、CREATED。
画面 4: SQLyog 客户端选中表 act_re_model，数据表显示字段包括 ID、NAME、CATEGORY、KEY、TENANT_ID、DEPLOYMENT_ID、REVISION_VERSION。
画面 5: PPT 页面内容与画面 2 相同，鼠标光标在“ACT_GE_*”条目上。
画面 6: PPT 页面内容与画面 2 相同，鼠标光标在“ACT_GE_*”条目上。
画面 7: SQLyog 客户端选中表 act_re_model，数据表显示字段包括 ID、NAME、CATEGORY、KEY、TENANT_ID、DEPLOYMENT_ID、REVISION_VERSION。
画面 8: PPT 页面标题为“第4章 Activiti 服务架构图”，内容为“3.3.7 数据库表的命名规则”。
画面 9: SQLyog 客户端选中表 act_ru_task，数据表显示字段包括 ID、REV、TYPE、NAME、CREATION_TIME、ASSIGNEE_ID、PARENT_ID、RETRY_COUNT、EXCLUSIVE、TEXT。
画面 10: PPT 页面标题为“第4章 Activiti 服务架构图”，内容为“3.3.7 数据库表的命名规则”。
画面 11: SQLyog 客户端选中表 act_ru_task，数据表显示字段包括 ID、REV、TYPE、NAME、CREATION_TIME、ASSIGNEE_ID、PARENT_ID、RETRY_COUNT、EXCLUSIVE、TEXT。
画面 12: SQLyog 客户端选中表 act_ge_property，数据表显示字段包括 NAME 和 VALUE，内容为：
- act_execution-related-artifacts-count: 1
- next-dbid: 1
- process-history: 7.0.0.0
- activiti-version: [NULL]
画面 13: PPT 页面标题为“第4章 Activiti 服务架构图”，内容为“3.3.7 数据库表的命名规则”。
画面 14: PPT 页面内容与画面 2 相同，鼠标光标在“ACT_GE_*”条目上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
PPT 标题：
- 画面 2: “3.3.7 数据库表的命名规则”
- 画面 8: “第4章 Activiti 服务架构图”
- 画面 10: “第4章 Activiti 服务架构图”
- 画面 13: “第4章 Activiti 服务架构图”
表格数据：
- 画面 2: 无表格数据。
- 画面 12: 表格数据为：
  - NAME: act_execution-related-artifacts-count, VALUE: 1
  - NAME: next-dbid, VALUE: 1
  - NAME: process-history, VALUE: 7.0.0.0
  - NAME: activiti-version, VALUE: [NULL]

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
