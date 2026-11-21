# 画面线理解：18-发起申请：代码实现测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\18-发起申请：代码实现测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:11, 00:18, 00:20, 00:23, 00:36, 00:47, 00:56, 01:11, 01:44, 01:46, 02:08, 02:10, 02:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:13:12

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 系统中发起请假流程，从前端点击“申请”按钮，到后端代码创建流程实例和任务，再到数据库中记录相关数据的全过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：在 IntelliJ IDEA 中，展示 `AuditService.java` 文件，代码中调用 `runtimeService.startProcessInstanceById` 启动流程实例，并创建任务 `taskService.createTaskQuery`，最后保存任务实例 `procTaskInstanceDao.save`。
画面 2：iHRM 系统前端界面，显示“工作日历”和“快捷入口”，其中“申请”按钮用于发起请假。
画面 3：点击“申请”后弹出的请假表单，包含“假期类型”、“申请单位”、“开始时间”、“结束时间”和“申请理由”等字段。
画面 4：在浏览器开发者工具的 Network 面板中，查看发起请假请求的 `startProcess` 请求，其响应数据为 JSON 格式。
画面 5：请求成功后，前端页面显示“操作成功！”提示，同时 Network 面板中 `startProcess` 请求的响应数据为 `{"code":18000,"message":"操作成功！","success":true}`。
画面 6：在 SQLyog 数据库工具中，查看 `act_ru_task` 表，显示流程任务数据，其中 `process_id_` 为 `11758551064-65382102`，`task_name_` 为 `请假`。
画面 7：在 SQLyog 数据库工具中，查看 `act_ru_task` 表，显示流程任务数据，其中 `process_id_` 为 `11758551064-65382102`，`task_name_` 为 `审批`。
画面 8：在 SQLyog 数据库工具中，查看 `act_ru_task` 表，显示流程任务数据，其中 `process_id_` 为 `11758551064-65382102`，`task_name_` 为 `审批`。
画面 9：在 SQLyog 数据库工具中，查看 `act_re_procdef` 表，显示流程定义数据，其中 `PROC_DEF_ID_` 为 `380544e-code-11a9-8503-005056000008`，`PROC_DEF_KEY_` 为 `process_leave`。
画面 10：在 SQLyog 数据库工具中，查看 `act_re_procdef` 表，显示流程定义数据，其中 `PROC_DEF_ID_` 为 `380544e-code-11a9-8503-005056000008`，`PROC_DEF_KEY_` 为 `process_leave`。
画面 11：在 SQLyog 数据库工具中，查看 `act_re_procdef` 表，显示流程定义数据，其中 `PROC_DEF_ID_` 为 `380544e-code-11a9-8503-005056000008`，`PROC_DEF_KEY_` 为 `process_leave`。
画面 12：在 SQLyog 数据库工具中，查看 `act_ru_task` 表，显示流程任务数据，其中 `process_id_` 为 `11758551064-65382102`，`task_name_` 为 `审批`。
画面 13：在 iHRM 系统前端界面，显示“我发起的”审批列表，包含“请婚”和“请假”两项申请，状态为“审批中”。
画面 14：在 IntelliJ IDEA 中，展示 `AuditService.java` 文件，代码中调用 `runtimeService.startProcessInstanceById` 启动流程实例，并创建任务 `taskService.createTaskQuery`，最后保存任务实例 `procTaskInstanceDao.save`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceById(definition.getId(), instance.getProcessId(), vars);
//4. 自动执行的节点
Task task = taskService.createTaskQuery().processInstanceId(processInstance.getId()).singleResult();
//5. 保存一个节点数据，填充业务数据中当前审批人
procTaskInstanceDao.save(instance);
procTaskInstance pti = new ProcTaskInstance();
pti.setTaskId(worker.nextId());
pti.setProcessId(instance.getProcessId());
pti.setHandleTime(new Date());
pti.setHandleType("2");
pti.setHandleUserName(user.getUsername());
pti.setTaskKey(task.getTaskDefinitionKey());
pti.setTaskName(task.getName());
pti.setHandleOpinion("发起申请");
procTaskInstanceDao.save(pti);
```
画面 14：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceById(definition.getId(), instance.getProcessId(), vars);
//4. 自动执行的节点
Task task = taskService.createTaskQuery().processInstanceId(processInstance.getId()).singleResult();
//5. 保存一个节点数据，填充业务数据中当前审批人
procTaskInstanceDao.save(instance);
procTaskInstance pti = new ProcTaskInstance();
pti.setTaskId(worker.nextId());
pti.setProcessId(instance.getProcessId());
pti.setHandleTime(new Date());
pti.setHandleType("2");
pti.setHandleUserName(user.getUsername());
pti.setTaskKey(task.getTaskDefinitionKey());
pti.setTaskName(task.getName());
pti.setHandleOpinion("发起申请");
procTaskInstanceDao.save(pti);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
