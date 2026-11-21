# 画面线理解：08-Activiti组任务-当前用户归还组任务

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\08-Activiti组任务-当前用户归还组任务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:52, 02:00, 02:17, 02:46, 03:21, 03:46, 04:15, 04:52, 05:06, 05:28, 05:43, 06:16, 08:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:18:16

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中通过 Java 代码操作任务，包括查询、完成、分配、归还和交接任务等核心功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 `GroupTest.java` 文件中用于完成任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则完成任务并打印提示。
- 代码片段：
  ```java
  //2.创建TaskService对象
  TaskService taskService = processEngine.getTaskService();
  //3.设置一些参数，流程定义的key，用户
  String key = "myProcess_1";
  String assignee = "zhangsan";
  //4.执行查询
  task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskAssignee(assignee) //设置任务的负责人
  .singleResult();
  //5.找到当前的任务
  if(task!=null){
  taskService.complete(task.getId());
  System.out.println("任务执行完毕！");
  }
  ```

画面2：
- 展示了 SQLyog 数据库客户端中查询 `act_hi_actinst` 表的结果。
- 查询结果包含任务执行实例的详细信息，如执行ID、任务名称、分配人、开始和结束时间等。
- 表格数据：
  ```
  EXECUTION_ID_ | ACT_ID_ | CALL_PROC_INST_ID_ | ACT_NAME_ | ACT_TYPE_ | ASSIGNEE_ | START_TIME_ | END_TIME_ | DURATION_
  2002 | 4 | 2000 | 请假审批中审核 | userTask | wanshang | 2018-11-16 16:17:26 | 2018-11-16 16:17:26 | 24
  2002 | 5 | 7002 | 请假审批中审核 | userTask | zhangsan | 2018-11-16 16:19:00 | 2018-11-16 16:19:00 | 0
  ```

画面3：
- 展示了 Activiti Designer 中的 BPMN 图，包含 StartEvent、UserTask、ScriptTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、SubProcess、ParallelGateway、ExclusiveGateway 等节点。
- 画面中未展示具体流程图结构。

画面4：
- 展示了 `GroupTest.java` 文件中用于启动流程实例的代码片段。
- 代码逻辑：获取运行时服务，通过流程定义键启动流程实例，并打印流程定义ID和流程实例ID。
- 代码片段：
  ```java
  //2.博得RuntimeService实例
  RuntimeService runtimeService = processEngine.getRuntimeService();
  //3.创建流程实例，流程定义的key需要知道 holiday
  ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess_1");
  System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
  System.out.println("流程实例ID:"+processInstance.getId());//2001
  ```

画面5：
- 展示了 `GroupTest.java` 文件中用于部署流程定义的代码片段。
- 代码逻辑：获取仓库服务，创建部署对象，添加流程图文件，部署流程。
- 代码片段：
  ```java
  //1.博得ProcessEngine实例
  ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
  //2.博得RepositoryService实例
  RepositoryService repositoryService = processEngine.getRepositoryService();
  //3.创建部署对象
  Deployment deployment = repositoryService.createDeployment()
  .addClasspathResource("diagram/holidays.bpmn") //添加bpmn流程
  .name("请假申请流程")
  .deploy();
  ```

画面6：
- 展示了 `GroupTest.java` 文件中用于启动流程实例的代码片段。
- 代码逻辑：获取运行时服务，通过流程定义键启动流程实例，并打印流程定义ID和流程实例ID。
- 代码片段：
  ```java
  //2.博得RuntimeService实例
  RuntimeService runtimeService = processEngine.getRuntimeService();
  //3.创建流程实例，流程定义的key需要知道 holiday
  ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess_1");
  System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
  System.out.println("流程实例ID:"+processInstance.getId());//2001
  ```

画面7：
- 展示了 `GroupTest.java` 文件中用于完成任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则完成任务并打印提示。
- 代码片段：
  ```java
  //2.创建TaskService对象
  TaskService taskService = processEngine.getTaskService();
  //3.设置一些参数，流程定义的key，用户
  String key = "myProcess_1";
  String assignee = "zhangsan";
  //4.执行查询
  task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskAssignee(assignee) //设置任务的负责人
  .singleResult();
  //5.找到当前的任务
  if(task!=null){
  taskService.complete(task.getId());
  System.out.println("用户任务执行完毕...");
  }
  ```

画面8：
- 展示了 `GroupTest.java` 文件中用于完成任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则完成任务并打印提示。
- 代码片段：
  ```java
  //2.创建TaskService对象
  TaskService taskService = processEngine.getTaskService();
  //3.设置一些参数，流程定义的key，用户
  String key = "myProcess_1";
  String assignee = "zhangsan";
  //4.执行查询
  task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskAssignee(assignee) //设置任务的负责人
  .singleResult();
  //5.找到当前的任务
  if(task!=null){
  taskService.complete(task.getId());
  System.out.println("用户任务执行完毕...");
  }
  ```

画面9：
- 展示了 `GroupTest.java` 文件中用于查询用户任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和候选用户查询任务，遍历任务列表并打印任务ID和流程实例ID。
- 代码片段：
  ```java
  //4.执行查询
  List<Task> list = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskCandidateUser(candidate_users) //设置候选用户
  .list();
  //5.输出
  for(Task task : list){
  System.out.println(task.getId());
  System.out.println(task.getProcessInstanceId());
  }
  ```

画面10：
- 展示了 `GroupTest.java` 文件中用于查询用户任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和候选用户查询任务，遍历任务列表并打印任务ID和流程实例ID。
- 代码片段：
  ```java
  //4.执行查询
  List<Task> list = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskCandidateUser(candidate_users) //设置候选用户
  .list();
  //5.输出
  for(Task task : list){
  System.out.println(task.getId());
  System.out.println(task.getProcessInstanceId());
  }
  ```

画面11：
- 展示了 `GroupTest.java` 文件中用于任务认领的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则认领任务并打印提示。
- 代码片段：
  ```java
  //4.执行查询
  Task task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskCandidateUser(candidate_users) //设置候选用户
  .singleResult();
  //5.认领任务
  if(task!=null){
  taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选用户名
  System.out.println("任务已领取完毕！");
  }
  ```

画面12：
- 展示了 `GroupTest.java` 文件中用于任务认领的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则认领任务并打印提示。
- 代码片段：
  ```java
  //4.执行查询
  Task task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskCandidateUser(candidate_users) //设置候选用户
  .singleResult();
  //5.认领任务
  if(task!=null){
  taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选用户名
  System.out.println("任务已领取完毕！");
  }
  ```

画面13：
- 展示了 PDF 文档中关于任务交接
