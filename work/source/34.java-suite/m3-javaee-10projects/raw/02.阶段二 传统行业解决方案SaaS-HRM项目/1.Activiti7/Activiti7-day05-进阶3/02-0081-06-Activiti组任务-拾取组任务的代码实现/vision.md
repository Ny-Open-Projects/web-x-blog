# 画面线理解：06-Activiti组任务-拾取组任务的代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\06-Activiti组任务-拾取组任务的代码实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:27, 00:57, 01:27, 02:01, 02:08, 02:22, 02:40, 03:16, 03:33, 04:06, 04:41, 05:07, 07:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:16:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中，通过 Java 代码实现用户拾取组任务（Claim Task）功能，并展示相关代码逻辑和数据库表数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“4.1.1.3 用户拾取组任务”，并显示代码片段，其中定义了拾取任务的方法 claimTask()，包含任务 ID "6302"、候选人 ID "lisi"，并调用 taskService.claim() 方法。
画面2：展示 IDE 中 GroupTest.java 文件，main 方法中设置流程定义 key 为 "myProcess_1"，候选人用户为 "zhangsan"，并执行查询任务列表。
画面3：展示 PPT 页面“4.1.1.3 用户拾取组任务”，代码片段中展示 taskService.claim(taskId, userId) 的调用逻辑。
画面4：展示 IDE 中 GroupTest.java 文件，main 方法中执行查询任务列表的代码块被高亮。
画面5：展示 IDE 中 GroupTest.java 文件，鼠标悬停在“Run”按钮上，准备执行代码。
画面6：展示 IDE 中 GroupTest.java 文件，main 方法中设置流程定义 key 和候选人用户。
画面7：展示 IDE 中 GroupTest.java 文件，main 方法中设置流程定义 key 为 "myProcess_1"，候选人用户为 "zhangsan"。
画面8：展示 IDE 中 GroupTest.java 文件，main 方法中执行查询任务列表的代码块被高亮，下方终端显示了查询结果。
画面9：展示 IDE 中 GroupTest.java 文件，main 方法中执行查询任务列表的代码块被高亮，下方终端显示了查询结果。
画面10：展示 PPT 页面“4.1.1.3 用户拾取组任务”，代码片段中展示 taskService.claim(taskId, userId) 的调用逻辑，并附有说明文字。
画面11：展示 IDE 中 GroupTest.java 文件，main 方法中执行查询任务列表的代码块被高亮。
画面12：展示 IDE 中 GroupTest.java 文件，main 方法中调用 taskService.claim(task.getId(), candidate_users) 并打印“任务拾取完毕！”。
画面13：展示数据库管理工具，查询 act_hi_actinst 表，显示了流程实例 ID、任务 ID、执行人等信息。
画面14：展示 IDE 中 GroupTest.java 文件，main 方法中调用 taskService.claim(task.getId(), candidate_users) 并打印“任务拾取完毕！”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
@Test
public void claimTask(){
    TaskService taskService = processEngine.getTaskService();
    //要拾取的任务id
    String taskId = "6302";
    //任务候选人id
    String userId = "lisi";
    //拾取任务
    //即使该用户不是候选人也能拾取(建议拾取时校验是否有资格)
    //校验该用户有没有拾取任务的资格
    Task task = taskService.createTaskQuery()//
            .taskId(taskId)
            .taskCandidateUser(userId)//根据候选人查询
            .singleResult();
    if(task!=null){
        taskService.claim(taskId, userId);
        System.out.println("任务拾取成功");
    }
}

画面2：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面3：
@Test
public void claimTask(){
    TaskService taskService = processEngine.getTaskService();
    //要拾取的任务id
    String taskId = "6302";
    //任务候选人id
    String userId = "lisi";
    //拾取任务
    //即使该用户不是候选人也能拾取(建议拾取时校验是否有资格)
    //校验该用户有没有拾取任务的资格
    Task task = taskService.createTaskQuery()//
            .taskId(taskId)
            .taskCandidateUser(userId)//根据候选人查询
            .singleResult();
    if(task!=null){
        taskService.claim(taskId, userId);
        System.out.println("任务拾取成功");
    }
}

画面4：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面5：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面6：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面7：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面8：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
