# 画面线理解：15-Activiti完成请假流程处理及过程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\15-Activiti完成请假流程处理及过程分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:01, 02:27, 03:06, 04:12, 05:54, 07:51, 08:52, 09:14, 09:59, 11:29, 12:56, 13:45, 15:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:28:40

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码调用 Activiti 工作流引擎的 TaskService 来查询和完成用户任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 ActivitiCompleteTask 类的 main 方法，获取默认流程引擎，调用 taskService.complete() 完成任务 ID 为 "5082" 的任务。
画面 2: 展示 ActivitiTaskQuery 类的 main 方法，获取流程引擎，调用 taskService.createTaskQuery().processDefinitionKey("holiday").taskAssignee("lishi").list() 查询任务。
画面 3: 展示 ActivitiTaskQuery 类的 main 方法，获取流程引擎，调用 taskService.createTaskQuery().processDefinitionKey("holiday").taskAssignee("lishi").list() 查询任务，并通过 for 循环打印任务信息。
画面 4: 展示 ActivitiTaskQuery 类的 main 方法，获取流程引擎，调用 taskService.createTaskQuery().processDefinitionKey("holiday").taskAssignee("lishi").list() 查询任务，并通过 for 循环打印任务信息。
画面 5: 展示 ActivitiTaskQuery 类的 main 方法，获取流程引擎，调用 taskService.createTaskQuery().processDefinitionKey("holiday").taskAssignee("lishi").list() 查询任务，并通过 for 循环打印任务信息。
画面 6: 展示 ActivitiCompleteTask 类的 main 方法，获取流程引擎，调用 taskService.complete("5082") 完成任务。
画面 7: 展示 ActivitiCompleteTask 类的 main 方法，获取流程引擎，调用 taskService.complete("5082") 完成任务。
画面 8: 展示 ActivitiTaskQuery 类的 main 方法，获取流程引擎，调用 taskService.createTaskQuery().processDefinitionKey("holiday").taskAssignee("lishi").list() 查询任务。
画面 9: 展示 ActivitiTaskQuery 类的 main 方法，获取流程引擎，调用 taskService.createTaskQuery().processDefinitionKey("holiday").taskAssignee("lishi").list() 查询任务，并通过 for 循环打印任务信息。
画面 10: 展示 ActivitiCompleteTask 类的 main 方法，获取流程引擎，调用 taskService.complete("5082") 完成任务。
画面 11: 展示 ActivitiCompleteTask 类的 main 方法，获取流程引擎，调用 taskService.createTaskQuery().processDefinitionKey("holiday").taskAssignee("lishi").list() 查询任务。
画面 12: 展示 ActivitiCompleteTask 类的 main 方法，获取流程引擎，调用 taskService.createTaskQuery().processDefinitionKey("holiday").taskAssignee("lishi").list() 查询任务，并通过 for 循环打印任务信息。
画面 13: 展示 MySQL 数据库中 act_ru_task 表的数据，显示任务 ID、任务名称、负责人、开始时间等信息。
画面 14: 展示一个 PPT 页面，标题为“完成任务”，内容为一个 Java 单元测试方法，用于完成任务。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.处理任务，结合当前用户任务列表的查询操作的话，任务ID:5082
        taskService.complete("5082");
    }
}
```

画面 2:
```java
package com.ithema.activiti;

import org.activiti.engine.task.Task;
import org.activiti.engine.task.TaskService;
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;

/**
 * 查询当前用户的任务列表
 */
public class ActivitiTaskQuery {
    public static void main(String[] args) {
        //1.获取ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.根据流程定义的key，负责人assignee来实现当前用户的任务列表查询
        Task task = taskService.createTaskQuery()
                .processDefinitionKey("holiday")
                .taskAssignee("lishi")
                .singleResult();
    }
}
```

画面 3:
```java
//4.任务列表的展示
for(Task task : taskList){
    System.out.println("流程实例ID:"+task.getProcessInstanceId());
    System.out.println("任务ID:"+task.getId());
    System.out.println("任务负责人:"+task.getAssignee());
    System.out.println("任务名称:"+task.getName());
}
```

画面 4:
```java
//4.任务列表的展示
for(Task task : taskList){
    System.out.println("流程实例ID:"+task.getProcessInstanceId());
    System.out.println("任务ID:"+task.getId());
    System.out.println("任务负责人:"+task.getAssignee());
    System.out.println("任务名称:"+task.getName());
}
```

画面 5:
```java
//4.任务列表的展示
for(Task task : taskList){
    System.out.println("流程实例ID:"+task.getProcessInstanceId());
    System.out.println("任务ID:"+task.getId());
    System.out.println("任务负责人:"+task.getAssignee());
    System.out.println("任务名称:"+task.getName());
}
```

画面 6:
```java
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.处理任务，结合当前用户任务列表的查询操作的话，任务ID:5082
        taskService.complete("5082");
    }
}
```

画面 7:
```java
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.处理任务，结合当前用户任务列表的查询操作的话，任务ID:5082
        taskService.complete("5082");
    }
}
```

画面 8:
```java
//3.根据流程定义的key，负责人assignee来实现当前用户的任务列表查询
Task task = taskService.createTaskQuery()
        .processDefinitionKey("holiday")
        .taskAssignee("lishi")
        .singleResult();
```

画面 9:
```java
//4.任务列表的展示
for(Task task : taskList){
    System.out.println("流程实例ID:"+task.getProcessInstanceId());
    System.out.println("任务ID:"+task.getId());
    System.out.println("任务负责人:"+task.getAssignee());
    System.out.println("任务名称:"+task.getName());
}
```

画面 10:
```java
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.处理任务，结合当前用户任务列表的查询操作的话，任务ID:5082
        taskService.complete("5082");
    }
}
```

画面 11:
```java
//3.查询当前用户的任务并根据流程定义的key，负责人assignee来实现当前用户的任务列表查询
taskService.createTaskQuery()
        .processDefinitionKey("holiday")
        .taskAssignee("lishi")
        .list();
```

画面 12:
```java
//3.查询当前用户的任务并根据流程定义的key，负责人assignee来实现当前用户的任务列表查询
taskService.createTaskQuery()
        .processDefinitionKey("holiday")
        .taskAssignee("lishi")
        .list();
```

画面 13:
```sql
CALL PROC_INST_ID  ACT_TASK  ACT_CAUS  ASSIGNEE  START_TIME  END_TIME  LOCATION  SELE_S_REASON  TENANT_ID
1001  1001  1001  zhangsan  2016-10-24 15:24:12  11992075  (NULL)  (NULL)
1002  1002  1002  lishi  2016-10-24 15:24:13  1415575  (NULL)  (NULL)
```

画面 14:
```java
//完成任务
@Test
public void completTask(){
    //任务id
    String taskId = "8395";
    //创建TaskService
    TaskService taskService = processEngine.getTaskService();
    //完成任务
    taskService.complete(taskId);
    System.out
