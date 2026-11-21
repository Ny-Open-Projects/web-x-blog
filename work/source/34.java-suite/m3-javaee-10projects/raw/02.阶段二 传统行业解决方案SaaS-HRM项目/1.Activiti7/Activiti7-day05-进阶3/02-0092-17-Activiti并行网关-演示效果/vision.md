# 画面线理解：17-Activiti并行网关-演示效果

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\17-Activiti并行网关-演示效果_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:35, 02:29, 03:36, 04:27, 05:06, 05:46, 06:22, 06:51, 07:44, 09:36, 12:01, 14:28, 15:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:24:18

1) 这一组画面整体在讲什么（一句话）：
演示并行网关（Parallel Gateway）在流程中的应用，包括流程图设计、Java测试代码编写、数据库操作及流程执行结果分析。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示BPMN流程图，包含并行网关（ParallelGateway）和排他网关（ExclusiveGateway），并显示“holidayParallel”流程定义的属性设置界面。
画面2：展示Java测试类ParallelGatewayTest的代码，包含启动流程引擎、创建流程实例、输出流程定义ID和流程实例ID的逻辑。
画面3：在MySQL命令行中执行SQL语句，删除名为“activiti”的数据库并创建同名数据库。
画面4：在MySQL命令行中执行SQL语句，删除名为“activiti”的数据库并创建同名数据库，但未执行成功，提示“Table 'activiti' doesn't exist”。
画面5：展示Java测试类ParallelGatewayTest的代码，创建流程实例并输出流程定义ID和流程实例ID。
画面6：展示Java测试类ParallelGatewayTest的代码，创建流程实例并输出流程定义ID和流程实例ID，终端显示执行成功。
画面7：展示Java测试类ParallelGatewayTest的代码，查询当前用户任务并处理任务。
画面8：展示Java测试类ParallelGatewayTest的代码，查询当前用户任务并处理任务，终端显示执行成功。
画面9：展示Java测试类ParallelGatewayTest的代码，查询当前用户任务并处理任务，终端显示执行成功。
画面10：展示BPMN流程图，包含并行网关（ParallelGateway）和排他网关（ExclusiveGateway），并显示“holidayParallel”流程定义的属性设置界面。
画面11：在MySQL命令行中执行SQL语句，查询act_ru_task表，显示当前任务数据。
画面12：展示Java测试类ParallelGatewayTest的代码，查询当前用户任务并处理任务，终端显示执行成功。
画面13：展示PDF文档“5.2.3 测试”章节，说明当前任务表和流程实例表的数据查询语句及含义。
画面14：展示PDF文档“5.3 包含网关”章节，介绍包含网关的概念。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
//4.处理任务,结合当前用户任务对应的流程操作的语句,任务ID:task.getId();
if(task!=null){
    taskService.complete(task.getId());
    System.out.println("用户任务执行完毕...");
}

//5.输出任务id
System.out.println(task.getId());
j++;
```

画面5：
```java
//3.创建流程实例 流程定义的key需要知道 holiday
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holidayParallel",map);
//4.输出流程的相关信息
System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
System.out.println("流程实例ID:"+processInstance.getId());//2501
```

画面6：
```java
//3.创建流程实例 流程定义的key需要知道 holiday
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holidayParallel",map);
//4.输出流程的相关信息
System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
System.out.println("流程实例ID:"+processInstance.getId());//2501
```

画面7：
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holidayParallel")
    .taskAssignee("zhangsan")
    .singleResult();
```

画面8：
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holidayParallel")
    .taskAssignee("wangwu")
    .singleResult();
```

画面9：
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holidayParallel")
    .taskAssignee("zhaozhi")
    .singleResult();
```

画面12：
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holidayParallel")
    .taskAssignee("xiaoWu")
    .singleResult();
```

画面3：
```sql
drop database activiti;
create database activiti;
```

画面4：
```sql
drop database activiti;
create database activiti;
```

画面11：
```sql
SELECT * FROM act_ru_task #当前任务表
```

画面13：
```sql
SELECT * FROM act_ru_execution #流程实例的执行表
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13：
标题：“5.2.3 测试”
表格数据：
当前任务表：SELECT * FROM act_ru_task #当前任务表
流程实例表：SELECT * FROM act_ru_execution #流程实例的执行表

画面14：
标题：“5.3 包含网关”
子标题：“5.3.1 什么是包含网关”
内容：包含网关可以看做是排他网关和并行网关的结合体，和排他网关一样，你可以在外出顺序上定义分支。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
