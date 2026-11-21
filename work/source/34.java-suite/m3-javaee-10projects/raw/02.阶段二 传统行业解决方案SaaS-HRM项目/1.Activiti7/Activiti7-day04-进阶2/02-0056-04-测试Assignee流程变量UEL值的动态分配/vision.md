# 画面线理解：04-测试Assignee流程变量UEL值的动态分配

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\04-测试Assignee流程变量UEL值的动态分配_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:36, 00:45, 01:17, 01:28, 01:53, 02:25, 02:52, 03:17, 03:22, 03:44, 04:03, 04:08, 04:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:55:42

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Activiti 工作流引擎部署流程定义、启动流程实例、设置流程变量以及完成任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 ActivitiDeployment.java 文件，代码用于部署名为“请假申请流程”的流程定义，包含添加 BPMN 文件和 PNG 图片资源。
画面2：展示 ActivitiDeployment.java 文件，代码用于打印部署的名称和 ID。
画面3：展示 MySQL GUI 工具，执行 SQL 语句删除名为 'activiti' 的数据库并重新创建。
画面4：展示 MySQL GUI 工具，查询 activiti 表，显示部署的 ID 和资源信息。
画面5：展示 AssigneeUI.java 文件，代码用于启动流程实例并设置 assignee 变量。
画面6：展示 AssigneeUI.java 文件，代码执行后在控制台输出流程引擎名称。
画面7：展示 MySQL GUI 工具，查询 activiti 表，显示部署的 ID 和资源信息。
画面8：展示 MySQL GUI 工具，界面空白，无操作。
画面9：展示 ActivitiCompleteTask.java 文件，代码用于查询并完成任务。
画面10：展示 ActivitiCompleteTask.java 文件，代码执行后在控制台输出日志信息。
画面11：展示 AssigneeUI.java 文件，代码用于启动流程实例并设置 assignee 变量。
画面12：展示 PPT 页面，讲解如何在启动流程实例时设置流程变量，提供代码示例。
画面13：展示 PPT 页面，讲解 user 和 assignee 变量的获取方式。
画面14：展示 PPT 页面，展示流程图中“用户任务”节点的配置选项。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1. 引擎定义
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2. 获取RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3. 部署流程
Deployment deployment = repositoryService.createDeployment()
.addClasspathResource("diagram/holiday2.bpmn") //bpmn文件
.addClasspathResource("diagram/holiday2.png")
.name("请假申请流程")
.deploy();
```

画面2：
```java
//4. 打印出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```

画面3：
```sql
1 drop database activiti;
2
3 create database activiti;
```

画面4：
```sql
ID NAME DEPLOYMENT_ID BINARY/IMAGE GENERATED
0 diagram/holiday2.png 1
```

画面5：
```java
//1. 获取ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2. 获取RuntimeService实例
RuntimeService runtimeService = processEngine.getRuntimeService();
//3. 定义assignee的值，用户可以在界面上设置当前的执行人
Map<String, Object> map = new HashMap<>();
map.put("assignee1", "zhangsan");
map.put("assignee2", "lishi");
map.put("assignee3", "wangwu");
//4. 启动流程实例，同时设置没有定义的assignee的值
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday2", map);
//5. 输出
System.out.println(processEngine.getName());
```

画面6：
```java
//5. 输出
System.out.println(processEngine.getName());
```

画面9：
```java
//1. 获取当前流程引擎的实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2. 获取TaskService实例
TaskService taskService = processEngine.getTaskService();
//3. 查询当前用户任务
Task task = taskService.createTaskQuery()
.processDefinitionKey("holiday2")
.taskAssignee("zhangsan")
.singleResult();
//4. 完成任务，结合当前用户任务完成时的ID，作为ID，task.getId()
taskService.complete(task.getId());
```

画面12：
```java
//启动流程实例时设计流程变量
//定义流程变量
Map<String, Object> variables = new HashMap<String, Object>();
//设置流程变量assignee
variables.put("assignee", "张三");
ProcessInstance processInstance = runtimeService
.startProcessInstanceByKey(processDefinitionKey, variables);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面12：PPT 标题为“2.1.2.2 流程变量”，内容为“设置流程变量”，并提供代码示例。
画面13：PPT 标题为“2.1.2.2 流程变量”，内容为“user 也是 activiti 的一个流程变量，user.assignee 表示通过调用 user 的 getter 方法获取值。”
画面14：PPT 标题为“2.1.2.2 流程变量”，内容为“UEL-method 方式如下：”，并展示流程图中“用户任务”节点的配置选项。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
