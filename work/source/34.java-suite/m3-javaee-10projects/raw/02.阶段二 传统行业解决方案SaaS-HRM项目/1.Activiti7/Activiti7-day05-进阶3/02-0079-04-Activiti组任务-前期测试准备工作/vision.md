# 画面线理解：04-Activiti组任务-前期测试准备工作

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\04-Activiti组任务-前期测试准备工作_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:39, 01:27, 02:45, 03:19, 03:59, 05:07, 05:49, 06:54, 07:42, 08:17, 08:53, 09:35, 11:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:14:51

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Activiti 工作流引擎部署流程、启动流程实例、查询和完成任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，讲解用户查询组任务的四个步骤：查询任务、拾取任务、查询个人任务、办理个人任务。
画面2：IDE中显示项目结构，包含resources目录下的多个BPMN文件和activiti.cfg.xml配置文件。
画面3：代码中部署流程，使用repositoryService.createDeployment()添加资源并部署。
画面4：部署流程并输出部署名称和ID。
画面5：部署流程并输出部署名称和ID。
画面6：代码中启动流程实例，使用runtimeService.startProcessInstanceByKey()。
画面7：代码中启动流程实例，使用runtimeService.startProcessInstanceByKey()。
画面8：SQLyog中执行SQL语句，删除数据库activiti并创建新数据库activiti。
画面9：IDE中显示启动流程实例的代码和终端输出。
画面10：代码中查询并完成任务，使用taskService.createTaskQuery().taskAssignee("zhangsan").singleResult()。
画面11：展示流程图，包含“开始”、“请假申请”、“提交审批”、“结束”节点。
画面12：代码中查询并完成任务，使用taskService.createTaskQuery().taskAssignee("zhangsan").singleResult()。
画面13：代码中查询并完成任务，使用taskService.createTaskQuery().taskAssignee("zhangsan").singleResult()，并添加if判断。
画面14：展示课程PPT内容，讲解用户查询组任务，代码示例为查询任务列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.进行部署
Deployment deployment = repositoryService.createDeployment()
		.addClasspathResource("diagram/holiday2.bpmn") //添加BPMN资源
		.name("请假申请流程")
		.deploy();
//4.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```

画面4：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.进行部署
Deployment deployment = repositoryService.createDeployment()
		.addClasspathResource("diagram/holiday2.bpmn") //添加BPMN资源
		.name("请假申请流程")
		.deploy();
//4.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```

画面6：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RuntimeService实例
RuntimeService runtimeService = processEngine.getRuntimeService();
//3.创建流程实例（流程定义的key需要知道 holiday）
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess");
//4.输出一些相关信息
System.out.println("流程定义ID:"+processInstance.getDeploymentId());//null
System.out.println("流程实例ID:"+processInstance.getId());//2901
System.out.println("活动ID:"+processInstance.getActivityId());//null
```

画面7：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RuntimeService实例
RuntimeService runtimeService = processEngine.getRuntimeService();
//3.创建流程实例（流程定义的key需要知道 holiday）
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess_1");
//4.输出一些相关信息
System.out.println("流程定义ID:"+processInstance.getDeploymentId());//null
System.out.println("流程实例ID:"+processInstance.getId());//2901
System.out.println("活动ID:"+processInstance.getActivityId());//null
```

画面9：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RuntimeService实例
RuntimeService runtimeService = processEngine.getRuntimeService();
//3.创建流程实例（流程定义的key需要知道 holiday）
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess_1");
//4.输出一些相关信息
System.out.println("流程定义ID:"+processInstance.getDeploymentId());//null
System.out.println("流程实例ID:"+processInstance.getId());//2901
System.out.println("活动ID:"+processInstance.getActivityId());//null
```

画面10：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService实例
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
		.processDefinitionKey("holiday4")
		.taskAssignee("zhangsan")
		.singleResult();
//4.处理任务，结合当前用户任务对象的属性操作，任务ID:task.getId()
taskService.complete(task.getId());
//5.输出任务的id
System.out.println(task.getId());
```

画面12：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService实例
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
		.processDefinitionKey("myProcess_1")
		.taskAssignee("zhangsan")
		.singleResult();
//4.处理任务，结合当前用户任务对象的属性操作，任务ID:task.getId()
taskService.complete(task.getId());
//5.输出任务的id
System.out.println(task.getId());
```

画面13：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService实例
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
		.processDefinitionKey("myProcess_1")
		.taskAssignee("zhangsan")
		.singleResult();
//4.处理任务，结合当前用户任务对象的属性操作，任务ID:task.getId()
if(task!=null){
	taskService.complete(task.getId());
	System.out.println("用户任务执行完毕...");
}
```

画面14：
```java
@Test
public void findGroupTaskList() {
	// 流程定义key
	String processDefinitionKey = "holiday4";
	// 任务候选人
	String candidateUser = "zhangsan";
	// 创建TaskService
	TaskService taskService = processEngine.getTaskService();
	// 查询任务
	List<Task> list = taskService.createTaskQuery()
		.processDefinitionKey(processDefinitionKey)
		.taskCandidateUser(candidateUser)//根据候选人查询
		.list();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.1.1.2 用户查询组任务”，内容为“根据候选人查询组任务”。
画面11：流程图包含“开始”指向“请假申请”，“请假申请”指向“提交审批”，“提交审批”指向“结束”。
画面14：PPT标题为“4.1.1.2 用户查询组任务”，内容为“根据候选人查询组任务”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
