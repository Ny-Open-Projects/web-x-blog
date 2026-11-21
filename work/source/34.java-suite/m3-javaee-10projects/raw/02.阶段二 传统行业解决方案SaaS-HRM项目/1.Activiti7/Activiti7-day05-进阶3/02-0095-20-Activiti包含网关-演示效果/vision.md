# 画面线理解：20-Activiti包含网关-演示效果

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\20-Activiti包含网关-演示效果_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 02:32, 03:34, 04:04, 05:08, 05:55, 06:55, 07:38, 09:05, 10:40, 11:56, 12:56, 14:27, 17:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:26:36

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Activiti 工作流引擎中的包含网关（Inclusive Gateway）实现并行任务，并通过 Java 代码部署流程、启动流程实例、查询和完成任务，同时展示数据库中相关流程和任务数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示 BPMN 图编辑器界面，流程图包含“开始事件”、“用户任务”、“包含网关”、“用户任务”、“并行网关”和“结束事件”。
- 属性面板显示当前选中元素的 ID 为 3，名称为“体检项目”，异步为 false，排他为 false。
- 画面右侧工具栏显示 BPMN 元素列表，包括 StartEvent、EndEvent、UserTask、ScriptTask、ServiceTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、Subprocess、Lane 和 ParallelGateway。

画面2：
- 展示 Java 代码文件 InclusiveGatewayTest.java，内容为部署 BPMN 流程定义。
- 代码中使用 repositoryService.createDeployment() 方法添加资源文件 "diagram/day05/examine.bpmn"，并设置名称为“体检流程”。
- 项目结构显示在左侧，包含多个 BPMN 文件，如 examine.bpmn、holiday.bpmn 等。

画面3：
- 代码中使用 repositoryService.createDeployment() 方法添加资源文件 "diagram/day05/examine.bpmn"，并设置名称为“体检流程”。
- 代码中使用 deployment.deploy() 方法部署流程定义。

画面4：
- 代码中使用 runtimeService.startProcessInstanceByKey("holidayParallel", map) 方法启动流程实例。
- 代码中输出流程定义 ID 和流程实例 ID。

画面5：
- 代码中使用 runtimeService.startProcessInstanceByKey("examine", map) 方法启动流程实例。
- 代码中输出流程定义 ID 和流程实例 ID。

画面6：
- 代码中使用 runtimeService.startProcessInstanceByKey("examine", map) 方法启动流程实例。
- 代码中输出流程定义 ID 和流程实例 ID。
- 代码中使用 taskService.createTaskQuery().processDefinitionKey("examine").taskAssignee("lisi").singleResult() 方法查询任务。
- 代码中使用 taskService.complete(task) 方法完成任务。
- 代码中使用 System.out.println(task.getId()) 方法输出任务 ID。

画面7：
- 代码中使用 taskService.createTaskQuery().processDefinitionKey("examine").taskAssignee("lisi").singleResult() 方法查询任务。
- 代码中使用 taskService.complete(task) 方法完成任务。
- 代码中使用 System.out.println(task.getId()) 方法输出任务 ID。

画面8：
- 展示 BPMN 图编辑器界面，流程图包含“开始事件”、“用户任务”、“包含网关”、“用户任务”、“并行网关”和“结束事件”。
- 属性面板显示当前选中元素的 ID 为 3，名称为“体检项目”，异步为 false，排他为 false。
- 画面右侧工具栏显示 BPMN 元素列表，包括 StartEvent、EndEvent、UserTask、ScriptTask、ServiceTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、Subprocess、Lane 和 ParallelGateway。

画面9：
- 代码中使用 taskService.createTaskQuery().processDefinitionKey("examine").taskAssignee("lisi").singleResult() 方法查询任务。
- 代码中使用 taskService.complete(task) 方法完成任务。
- 代码中使用 System.out.println(task.getId()) 方法输出任务 ID。

画面10：
- 代码中使用 taskService.createTaskQuery().processDefinitionKey("examine").taskAssignee("lisi").singleResult() 方法查询任务。
- 代码中使用 taskService.complete(task) 方法完成任务。
- 代码中使用 System.out.println(task.getId()) 方法输出任务 ID。
- 画面底部显示“Process finished with exit code 0”。

画面11：
- 展示 MySQL 数据库管理工具界面，显示数据库 activiti 的表结构。
- SQL 语句为：drop database activiti; create database activiti;
- 数据库表中显示了流程实例和任务数据。

画面12：
- 展示 BPMN 图编辑器界面，流程图包含“开始事件”、“用户任务”、“包含网关”、“用户任务”、“并行网关”和“结束事件”。
- 属性面板显示当前选中元素的 ID 为 3，名称为“体检项目”，异步为 false，排他为 false。
- 画面右侧工具栏显示 BPMN 元素列表，包括 StartEvent、EndEvent、UserTask、ScriptTask、ServiceTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、Subprocess、Lane 和 ParallelGateway。

画面13：
- 展示 BPMN 图编辑器界面，流程图包含“开始事件”、“用户任务”、“包含网关”、“用户任务”、“并行网关”和“结束事件”。
- 画面右侧工具栏显示 BPMN 元素列表，包括 StartEvent、EndEvent、UserTask、ScriptTask、ServiceTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、Subprocess、Lane 和 ParallelGateway。

画面14：
- 展示 PDF 文档内容，内容为 Activiti 工作流引擎的包含网关相关说明。
- 文档中提到如果包含网关设置的条件中，流程变量不存在，会抛出异常。
- 文档中提到当执行到包含网关时，会查询 ACT_RU_EXECUTION 表和 ACT_RU_TASK 表。
- 文档中提到第一记录是包含网关分支，第二条记录是两个分支，常规项体检和抽血化验。
- 文档中提到当前任务表 ACT_RU_TASK 中的记录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();

//3.进行部署
Deployment deployment = repositoryService.createDeployment()
    .addClasspathResource("diagram/day05/examine.bpmn") //添加bpmn资源
    .name("体检流程")
    .deploy();
```

画面3：
```java
//3.进行部署
Deployment deployment = repositoryService.createDeployment()
    .addClasspathResource("diagram/day05/examine.bpmn") //添加bpmn资源
    .name("体检流程")
    .deploy();
```

画面4：
```java
//4.输出流程的相关信息
System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
System.out.println("流程实例ID:"+processInstance.getId());//2501
```

画面5：
```java
//4.输出流程的相关信息
System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
System.out.println("流程实例ID:"+processInstance.getId());//2501
```

画面6：
```java
//4.输出流程的相关信息
System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
System.out.println("流程实例ID:"+processInstance.getId());//2501
```

画面7：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面8：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面9：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面10：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面11：
```sql
drop database activiti;
create database activiti;
```

画面12：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面13：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面14：
```text
如果包含网关设置
