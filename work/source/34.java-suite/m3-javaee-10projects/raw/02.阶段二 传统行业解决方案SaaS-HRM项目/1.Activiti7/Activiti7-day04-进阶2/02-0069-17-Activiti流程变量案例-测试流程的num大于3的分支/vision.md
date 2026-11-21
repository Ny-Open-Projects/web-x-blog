# 画面线理解：17-Activiti流程变量案例-测试流程的num大于3的分支

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\17-Activiti流程变量案例-测试流程的num大于3的分支_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:38, 00:53, 01:13, 01:45, 02:09, 02:20, 03:01, 03:12, 03:39, 03:55, 04:09, 04:31, 05:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:02:53

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中通过 Java 代码创建流程实例、设置变量、查询任务并完成任务，并通过 MySQL 数据库查看相关运行时数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Java 代码，用于获取流程引擎、任务服务，查询用户任务，并在任务不为空时完成任务并打印“任务执行完毕”。
画面 2: 展示了 Java 代码，用于获取流程引擎、运行时服务，设置流程变量（holiday），并启动流程实例。
画面 3: 展示了 Java 代码，用于获取流程引擎、运行时服务，设置流程变量（holiday），并启动流程实例。
画面 4: 展示了 Java 代码，用于获取流程引擎、运行时服务，设置流程变量（holiday），并启动流程实例。同时，下方的 Run 窗口显示了流程启动成功。
画面 5: 展示了 MySQL 的 Query 窗口，执行了删除数据库和创建数据库的 SQL 语句，并显示了 act_ge_bytearray 和 act_ru_variable 等表。
画面 6: 展示了 Java 代码，右键菜单中选中了“Copy as Main Test”。
画面 7: 展示了 MySQL 的 Query 窗口，显示了 act_ru_task 表中的任务数据，包括任务名称、分配人、开始时间等。
画面 8: 展示了 Java 代码，高亮了查询任务的代码行。
画面 9: 展示了 MySQL 的 Query 窗口，显示了 act_ru_task 表中的任务数据。
画面 10: 展示了 Activiti 的 BPMN 图，流程包含开始事件、用户任务、排他网关、服务任务和结束事件。右侧是元素面板。
画面 11: 展示了 Java 代码，右键菜单中选中了“Run VariableTestmain”。
画面 12: 展示了 MySQL 的 Query 窗口，显示了 act_ru_task 表中的任务数据。
画面 13: 展示了 MySQL 的 Query 窗口，显示了 act_ru_task 表中的任务数据。
画面 14: 展示了 Activiti 的 BPMN 图，流程包含开始事件、用户任务、排他网关、服务任务和结束事件。右侧是元素面板。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
//获取任务
public static void main(String[] args) {
    //1.得到ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取TaskService
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户是否有任务
    String key = "myProcess_1";
    Task task = taskService.createTaskQuery().processDefinitionKey(key)
            .taskAssignee("zhaoliu").singleResult();
    if(task!=null){
        taskService.complete(task.getId());
        System.out.println("任务执行完毕");
    }
}
```

画面 2:
```java
//act_ge_bytearray
//act_ru_variable
public static void main(String[] args) {
    //1.得到ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(35);
    map.put("holiday", holiday);
    //4.启动流程实例，并且设置变量值
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
    //5.输出实例信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
}
```

画面 4:
```java
//act_ge_bytearray
//act_ru_variable
public static void main(String[] args) {
    //1.得到ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(35);
    map.put("holiday", holiday);
    //4.启动流程实例，并且设置变量值
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
    //5.输出实例信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
}
```

画面 5:
```sql
drop database activiti;
create database activiti;
act_ge_bytearray
act_ru_variable
```

画面 8:
```java
//3.查询当前用户是否有任务
String key = "myProcess_1";
Task task = taskService.createTaskQuery().processDefinitionKey(key)
        .taskAssignee("zhaoliu").singleResult();
```

画面 10:
```xml
<!-- BPMN 图中未显示具体 XML 配置 -->
```

画面 14:
```xml
<!-- BPMN 图中未显示具体 XML 配置 -->
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 10: BPMN 图中，开始事件（绿色圆圈）指向用户任务（绿色矩形），用户任务指向排他网关（菱形），排他网关指向服务任务（绿色矩形），服务任务指向结束事件（红色圆圈）。
画面 14: BPMN 图中，开始事件（绿色圆圈）指向用户任务（绿色矩形），用户任务指向排他网关（菱形），排他网关指向服务任务（绿色矩形），服务任务指向结束事件（红色圆圈）。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
