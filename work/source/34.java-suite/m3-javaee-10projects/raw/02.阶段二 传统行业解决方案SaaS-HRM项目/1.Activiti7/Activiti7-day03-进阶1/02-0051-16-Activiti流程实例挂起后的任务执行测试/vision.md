# 画面线理解：16-Activiti流程实例挂起后的任务执行测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\16-Activiti流程实例挂起后的任务执行测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:20, 00:40, 01:17, 01:37, 01:57, 02:16, 02:49, 04:20, 05:19, 05:31, 06:10, 06:21, 06:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:47:45

1) 这一组画面整体在讲如何通过 Java 代码操作 Activiti 工作流引擎，实现对流程实例的挂起与激活，以及对任务的完成操作。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 `SuspendProcessInstance.java` 文件中获取 `ProcessEngine` 和 `RuntimeService` 的代码，以及注释“//1.获取ProcessEngine对象”、“//2.获取RuntimeService对象”。
画面2: 展示了通过 `createProcessInstanceQuery().processInstanceId("2581").singleResult()` 查询流程实例，并通过 `isSuspended()` 判断其状态，终端显示“Process finished with exit code 0”。
画面3: 展示了 `SuspendProcessInstance.java` 文件中根据流程实例是否挂起，分别调用 `activateProcessInstanceById` 或 `suspendProcessInstanceById` 方法，并输出相应提示。
画面4: 展示了 `SuspendProcessInstance.java` 文件中 `processInstanceId` 的值为 "2581"，终端显示“Process finished with exit code 0”。
画面5: 展示了 `SuspendProcessInstance.java` 文件中代码区域被选中，右下角有“天猫双11 尖端好货 第2件半价”的广告弹窗。
画面6: 展示了 `ActivitiCompleteTask.java` 文件，代码中获取 `TaskService`，并创建一个任务查询，指定流程定义键为 "holiday"，任务负责人是 "shangsan"。
画面7: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，并输出任务ID。
画面8: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，并输出任务ID。
画面9: 展示了 `SuspendProcessInstance.java` 文件中 `main` 方法的代码，终端显示“Process finished with exit code 0”。
画面10: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，并输出任务ID。
画面11: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，终端显示异常信息：“org.activiti.engine.ActivitiException: Cannot complete a suspended task”。
画面12: 展示了 `SuspendProcessInstance.java` 文件中代码区域被选中，终端显示“Process finished with exit code 0”。
画面13: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，终端显示异常信息：“org.activiti.engine.ActivitiException: Cannot complete a suspended task”。
画面14: 展示了 `ActivitiCompleteTask.java` 文件中 `else` 分支代码，终端显示异常信息：“org.activiti.engine.ActivitiException: Cannot complete a suspended task”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
public static void main(String[] args) {
    //1.获取ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
```

画面2:
```java
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
    .processInstanceId("2581")
    .singleResult();
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
if(suspended){
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "激活");
}else{
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "挂起");
}
```

画面3:
```java
//3. 实例化任务查询
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
    .processInstanceId("2581")
    .singleResult();
//4. 判断当前流程定义的实例是否为挂起状态
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
//5. 判断
if(suspended){
    //如果挂起，就可以激活操作
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "激活");
}else{
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "挂起");
}
```

画面4:
```java
//3. 实例化任务查询
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
    .processInstanceId("2581")
    .singleResult();
//4. 判断当前流程定义的实例是否为挂起状态
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
//5. 判断
if(suspended){
    //如果挂起，就可以激活操作
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "激活");
}else{
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "挂起");
}
```

画面6:
```java
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户的任务
        Task task = taskService.createTaskQuery()
            .processDefinitionKey("holiday")
            .taskAssignee("shangsan")
            .singleResult();
        //4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
        taskService.complete(task.getId());
        //5.输出任务的Id
        System.out.println("任务ID：" + task.getId());
    }
}
```

画面7:
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holiday")
    .taskAssignee("shangsan")
    .singleResult();
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
//5.输出任务的Id
System.out.println("任务ID：" + task.getId());
```

画面8:
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holiday")
    .taskAssignee("shangsan")
    .singleResult();
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
//5.输出任务的Id
System.out.println("任务ID：" + task.getId());
```

画面9:
```java
public static void main(String[] args) {
    //1.获取ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
```

画面10:
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holiday")
    .taskAssignee("shangsan")
    .singleResult();
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
//5.输出任务的Id
System.out.println("任务ID：" + task.getId());
```

画面11:
```java
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
```

画面12:
```java
//5.判断
if(suspended){
    //如果挂起，就可以激活操作
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "激活");
}else{
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "挂起");
}
```

画面13:
```java
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
```

画面14:
```java
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
