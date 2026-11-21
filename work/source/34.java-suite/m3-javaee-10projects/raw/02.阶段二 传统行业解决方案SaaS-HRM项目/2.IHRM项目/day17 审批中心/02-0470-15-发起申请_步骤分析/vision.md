# 画面线理解：15-发起申请：步骤分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\15-发起申请：步骤分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:32, 00:51, 00:57, 01:12, 01:49, 02:11, 02:43, 03:22, 03:39, 03:56, 04:14, 06:58, 07:41, 08:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:10:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 系统中发起请假申请，追踪其在后端（Controller、Service、Activiti 流程引擎）的处理流程，并通过数据库查看相关数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 iHRM 系统的“员工请假”页面，日历视图中显示了请假日期（如 2019-09-02）。
画面 2: 在请假申请表单中，填写了请假类型为“请假”，申请单位为“按天”，开始时间为“2019-09-02 00:00:00”，结束时间为“2019-09-03 00:00:00”，请假时长为“1”，申请理由为“xxxxxxxx”。
画面 3: 浏览器开发者工具中显示，提交请假申请的 POST 请求（URL: http://127.0.0.1:8085/api/user/process/startProcess）返回了 404 Not Found 错误。
画面 4: 在记事本中粘贴了用于发起请假申请的 JSON 数据，内容为：
{
  "applyUnit": "技光",
  "duration": "1",
  "emailTime": "2019-09-02 00:00:00",
  "holidayType": "1",
  "processKey": "process_leave",
  "processId": "1",
  "reason": "xxxxxxxx",
  "startTime": "2019-09-02 00:00:00",
  "userId": "118178950026271668"
}
画面 5: 在 SQLyog 数据库工具中，查看了 `proc_instance` 表，但数据为空。
画面 6: 在 Typora 中绘制了流程图，显示“controller”组件。
画面 7: 在 Typora 中绘制了流程图，显示“controller”接收参数后调用“service”组件。
画面 8: 在 Typora 中绘制了流程图，显示“controller”调用“service”，并指向“ihrm系统数据库”和“activiti数据库”。
画面 9: 在 SQLyog 数据库工具中，查看了 `proc_instance` 表的结构，包含字段如 `process_id`, `user_id`, `proc_apply_time`, `proc_state`, `proc_task_instance_id` 等。
画面 10: 在 Typora 中绘制了流程图，显示了多个窗口（SQLyog、iHRM、Typora、项目文件夹等）的布局。
画面 11: 在 Typora 中绘制了流程图，显示“controller”调用“service”，并标注了“ihrm系统数据库”和“activiti数据库”。
画面 12: 在 PPT 中显示了“1.4 离职流程分析”章节，其中包含“业务流程概述”和流程图，流程图显示了“当事人发起离职申请”→“直属领导审批”→“人事部审批”→“人事负责人审批”→“财务部审批”的顺序。
画面 13: 在 iHRM 系统中，页面显示了“审批”页面，但内容为空。
画面 14: 在 Typora 中绘制了流程图，显示“controller”调用“service”，并标注了“ihrm系统数据库”和“activiti数据库”，并添加了文字说明：
1. 构造业务数据 ProcInstance
2. 根据 processKey 查询流程定义
3. 开启流程（activitiAPI调用）
4. 执行第一个用户任务(Task)，用户申请
5. 获取下一个用户任务，获取执行候选人数据，设置到ProcInstance中

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
{
  "applyUnit": "技光",
  "duration": "1",
  "emailTime": "2019-09-02 00:00:00",
  "holidayType": "1",
  "processKey": "process_leave",
  "processId": "1",
  "reason": "xxxxxxxx",
  "startTime": "2019-09-02 00:00:00",
  "userId": "118178950026271668"
}

画面 9:
proc_instance 表结构：
Field          Type          Collation     Null     Key     Default     Extra     Privileges     Comment
process_id     varchar(45)  utf8_general_ci  NO      PRI     NULL     (NULL)     select,insert,update,references     流程实例ID
process_key    varchar(45)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程定义key
process_type   varchar(45)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程类型
process_state  varchar(3)   utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程状态
user_id        varchar(3)   utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     申请人ID
proc_apply_time datetime     utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     申请时间
proc_task_instance_id varchar(45)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     任务实例ID
proc_end_time   datetime     utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程结束时间
proc_data       longtext     utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程数据
department_id   varchar(40)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     部门ID
user_name       varchar(40)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     申请人姓名
proc_instance_id varchar(45)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程实例ID

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 12:
标题：1.4 离职流程分析
子标题：业务流程概述
流程图结构：
- 开始 → 当事人发起离职申请 → 直属领导审批 → 人事部审批 → 人事负责人审批 → 财务部审批 → 结束
表格数据：
- 无表格数据，仅包含流程描述。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
