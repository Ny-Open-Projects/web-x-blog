# 18-发起申请：代码实现测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\18-发起申请：代码实现测试_【海量资源尽在 ubkz.com】.mp4
- 时长 2分28秒（音频 148s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那现在呢我这边微服务呢已经启动成功了那接着我们回到页面一起来验证一下这个效果那在这边呢找到我们这边的请假流程好了里面随便填哎这都已经填好了没问题那接下来我们开始点击提交我们打开F12一起来验证一下来提交好了这边呢已经操作成功了那我们来看一下操作成功没问题那接下来验证一下我们自己的数据库那在我们的数据库之前呢
[00:30] 先去看我们自己的这个表那我们的自己流程业务表呢之前有一条现在变成了两条好了这边呢都已经把数据存进去了没什么问题哎没什么问题那接下来呢再来看我们自己的任务表那注意来看是不是有一个叫做提交申请咱们也已经提交过去了没错了好了那这两个表我们看过了之后那接下来呢还有就是由于在activity当中我们自动的
[01:01] 开始了一个流程实例并且完成了第一个操作那这边呢它会在历史表当中记录我们相应的这些数据那我们来看一下这个是我们的历史表相应的数据那第一个节点叫做开始那你会发现我们开始的时间就一共耗时了就是零嘛那接下来开始提交申请耗时了209这应该是好秒啊
[01:25] 好了那初审现在初审是不是还没做啊所以各位你会发现咱们现在的这个请求是不是在activity工作流当中提交申请已经完成了是不是接下来就进入到初审这个阶段了没错了那其实就符合我们之前的要求嘛好了那接下来呢里面还有一些其他的边边角角内容这边简单的我们一起来看一下好了在这边呢你会发现这边呢是我们候选人组相关的
[01:52] 那么候选人物组第一个叫做Applied User指的是提交人第二个是出审的这个组啊没错吧那这样一来呢各位其实能够发现我们现在已经把数据申请提交过去了那只不过我们来看一下页面那审批的时候你发现两条记录但是第二条记录是不是当前审批人是不是还没有所以我们这个代码呢还需要做最后一步完善
[02:20] 就是在中间给他添加上当前审批人的数据其实就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

