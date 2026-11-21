# 画面线理解：11-Activiti实现指定用户任务列表的查询

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\11-Activiti实现指定用户任务列表的查询_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:14, 02:05, 02:51, 04:27, 04:54, 05:28, 05:50, 06:48, 07:59, 08:50, 09:21, 09:45, 10:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:25:47

1) 这一组画面整体在讲如何使用 Activiti 工作流引擎查询当前用户待办任务的 Java 代码实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示“5.4 任务查询”章节，代码片段为查询个人待办任务的方法 findPersonalTaskList()，其中任务负责人设为 "zhangsan"。
画面2：展示创建 TaskService 的代码，使用 processEngine.createTaskQuery() 并设置 processDefinitionKey 为 "myholiday01" 和 taskAssignee 为 "zhangsan"。
画面3：展示 Activiti Designer 的 BPMN 图编辑界面，包含 StartEvent、UserTask 和 EndEvent，右侧为元素面板。
画面4：展示 ActivitiTaskQuery.java 文件的开头部分，导入了 Activiti 的核心包。
画面5：展示 ActivitiTaskQuery.java 文件中 main 方法的开头，获取 ProcessEngine 对象。
画面6：展示在 main 方法中调用 processEngine.getTaskService() 获取 TaskService 对象。
画面7：展示调用 taskService.createTaskQuery() 创建任务查询对象。
画面8：展示调用 .processDefinitionKey("holiday") 设置流程定义键。
画面9：展示调用 .taskAssignee("zhangsan") 设置任务负责人。
画面10：展示 for 循环遍历任务列表，并打印流程实例 ID、任务 ID、任务负责人和任务名称。
画面11：展示“5.5 任务处理”章节标题，说明任务负责人查询并处理任务。
画面12：展示 ActivitiTaskQuery.java 文件中 main 方法的完整代码，包含创建 TaskService、创建查询对象、设置流程定义键和任务负责人、遍历并打印任务信息。
画面13：展示运行程序后控制台输出的调试日志，包含 SQL 语句执行和任务查询结果。
画面14：展示运行程序后控制台输出的最终结果，显示了流程实例 ID、任务 ID、任务负责人和任务名称。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
// 查询当前个人待执行的任务
@Test
public void findPersonalTaskList() {
    // 任务负责人
    String assignee = "zhangsan";
}
```

画面2：
```java
// 创建TaskService
TaskService taskService = processEngine.getTaskService();
List<Task> list = taskService.createTaskQuery()//
        .processDefinitionKey("myholiday01")//
        .taskAssignee(assignee)//只查询该任务负责人的任务
        .list();
for (Task task : list) {
```

画面4：
```java
package com.ithema.activiti;
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.RuntimeService;
import org.activiti.engine.TaskService;
```

画面5：
```java
public class ActivitiTaskQuery {
    public static void main(String[] args) {
        //1.得到ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    }
```

画面6：
```java
//2.得到TaskService对象
TaskService taskService = processEngine.getTaskService();
```

画面7：
```java
//3.根据流程定义key,在该流程定义下查询当前用户的任务列表
taskService.createTaskQuery()
```

画面8：
```java
//4.设置流程定义key
.processDefinitionKey("holiday")
```

画面9：
```java
//5.设置任务负责人
.taskAssignee("zhangsan")
```

画面10：
```java
for (Task task : list) {
    System.out.println("流程实例ID：" + task.getProcessInstanceId());
    System.out.println("任务ID：" + task.getId());
    System.out.println("任务负责人：" + task.getAssignee());
    System.out.println("任务名称：" + task.getName());
}
```

画面12：
```java
public class ActivitiTaskQuery {
    public static void main(String[] args) {
        //1.得到ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.根据流程定义key,在该流程定义下查询当前用户的任务列表
        List<Task> taskList = taskService.createTaskQuery()
                .processDefinitionKey("holiday")
                .taskAssignee("zhangsan")
                .list();
        //4.遍历任务列表并打印
        for (Task task : taskList) {
            System.out.println("流程实例ID：" + task.getProcessInstanceId());
            System.out.println("任务ID：" + task.getId());
            System.out.println("任务负责人：" + task.getAssignee());
            System.out.println("任务名称：" + task.getName());
        }
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PPT 标题为“5.4 任务查询”，下方有文字说明“流程启动后，各各任务的负责人就可以查询自己当前需要处理的任务，查询出来的任务都是该用户的待办任务。”
画面10：PPT 标题为“5.5 任务处理”，下方有文字说明“任务负责人查询待办任务，选择任务进行处理，完成任务。”
画面3：BPMN 图中 StartEvent 指向 UserTask，UserTask 指向 EndEvent。右侧元素面板列出各种 BPMN 元素。
画面13：控制台输出调试日志，包含 SQL 语句执行和任务查询结果。

5) 无。
