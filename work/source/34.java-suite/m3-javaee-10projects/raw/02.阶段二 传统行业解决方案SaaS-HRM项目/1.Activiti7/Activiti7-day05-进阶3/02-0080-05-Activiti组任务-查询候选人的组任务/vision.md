# 画面线理解：05-Activiti组任务-查询候选人的组任务

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\05-Activiti组任务-查询候选人的组任务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:52, 01:53, 02:18, 02:42, 03:46, 04:41, 05:01, 05:45, 06:07, 06:26, 06:40, 07:13, 08:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:15:43

1) 这一组画面整体在讲如何通过 Java 代码调用 Activiti 工作流引擎的 TaskService 来查询和处理用户任务。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Activiti Designer 中的流程图，包含“开始事件”、“用户任务”、“用户任务”、“结束事件”等节点，左侧属性面板显示任务名称为“请假申请任务”，候选用户为“zhangsan,li”。
画面2: 展示一个 PPT 页面，内容为 Java 代码片段，用于演示如何通过 TaskService 查询任务，代码中定义了流程定义 key 为 “holiday4”，候选用户为 “zhangsan”。
画面3: 展示 Java 代码，用于演示如何通过 ProcessEngine 获取 TaskService，然后创建任务查询并完成任务。
画面4: 展示 Java 代码，用于演示如何通过 ProcessEngine 获取 TaskService，然后创建任务查询并完成任务。
画面5: 展示 Java 代码，用于演示如何通过 ProcessEngine 获取 TaskService，然后创建任务查询并完成任务。
画面6: 展示 Activiti Designer 中的流程图，包含“开始事件”、“用户任务”、“用户任务”、“结束事件”等节点。
画面7: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面8: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面9: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面10: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面11: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面12: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面13: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面14: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
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

画面3:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面4:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面5:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面6:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面7:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面8:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面9:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面10:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面11:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("
