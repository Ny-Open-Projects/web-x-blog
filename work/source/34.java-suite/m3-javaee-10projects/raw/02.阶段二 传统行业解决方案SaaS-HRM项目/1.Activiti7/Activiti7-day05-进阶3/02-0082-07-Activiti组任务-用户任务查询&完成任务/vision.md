# 画面线理解：07-Activiti组任务-用户任务查询&完成任务

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\07-Activiti组任务-用户任务查询&完成任务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:25, 00:39, 01:01, 01:25, 02:13, 02:29, 03:15, 03:38, 04:04, 04:35, 04:57, 05:20, 05:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:17:24

1) 这一组画面整体在讲什么（一句话）：
演示如何在Java代码中通过TaskService查询并操作流程任务，包括创建查询、获取任务、领取任务、完成任务等操作，并通过数据库查看任务状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 代码：`//5.让zhangsan用户，充当任务的负责人（让任务的assignee值）`
- 代码：`public static void main(String[] args) {`
- 代码：`//1.得到ProcessEngine对象`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`//2.得到TaskService对象`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`//3.设置一些参数，流程定义的key，候选人`
- 代码：`String key = "myProcess_1";`
- 代码：`String candidate_users = "zhangsan";`
- 代码：`//4.执行查询`
- 代码：`Task task = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskCandidateUser(candidate_users); //设置候选人`
- 代码：`.singleResult();`
- 代码：`if(task!=null){`
- 代码：`taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选人用户名`
- 代码：`System.out.println("任务领取完毕!");`
- 代码：`}`

画面2：
- 代码：`//4.执行查询`
- 代码：`Task task = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskCandidateUser(candidate_users); //设置候选人`
- 代码：`.singleResult();`
- 代码：`if(task!=null){`
- 代码：`taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选人用户名`
- 代码：`System.out.println("任务领取完毕!");`
- 代码：`}`

画面3：
- 代码：`//4.执行查询`
- 代码：`Task task = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskCandidateUser(candidate_users); //设置候选人`
- 代码：`.singleResult();`
- 代码：`if(task!=null){`
- 代码：`taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选人用户名`
- 代码：`System.out.println("任务领取完毕!");`
- 代码：`}`

画面4：
- 代码：`//4.执行查询`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskCandidateUser(candidate_users); //设置候选人`
- 代码：`.list();`
- 代码：`//5.输出`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //为null，说明当前的zhangsan只是一个候选人，并不是任务的执行人`
- 代码：`}`

画面5：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面6：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面7：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面8：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面9：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面10：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
