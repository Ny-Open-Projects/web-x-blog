# 画面线理解：02-Activiti流程定义信息删除及原理分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\02-Activiti流程定义信息删除及原理分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:50, 02:24, 04:00, 04:55, 05:19, 05:54, 07:27, 08:23, 08:56, 09:30, 09:54, 10:39, 13:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:36:26

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码操作 Activiti 工作流引擎，包括查询、启动、完成任务以及删除流程定义，并展示对应的数据库表结构和操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 显示 IntelliJ IDEA 中的 Java 代码，用于查询流程定义。
- 代码片段：
  ```java
  List(ProcessDefinition) list = processDefinitionQuery.processDefinitionKey("holiday")
  .orderByProcessDefinitionVersion()
  .desc().list();
  ```
  ```java
  for(ProcessDefinition processDefinition : list){
      System.out.println("流程定义ID：" + processDefinition.getId());
      System.out.println("流程定义名称：" + processDefinition.getName());
      System.out.println("流程定义的Key：" + processDefinition.getKey());
      System.out.println("流程定义的版本号：" + processDefinition.getVersion());
  }
  ```
- 控制台输出显示流程定义信息，包括 ID、名称、Key 和版本号。

画面 2:
- 显示 MySQL Workbench 中的 `information_schema` 数据库视图，列出 Activiti 的表结构。
- 表结构注释：
  ```
  act_hi_identitylink 参与者信息
  act_hi_procinst 流程实例
  act_hi_taskinst 任务实例
  act_ru_execution 执行表
  act_ru_identitylink 参与者信息
  act_ru_task 任务
  ```
- 注释说明：处理当前用户的任务，背后操作的表包括 `act_hi_actinst`、`act_hi_identitylink`、`act_hi_taskinst`、`act_ru_identitylink`、`act_ru_task`。

画面 3:
- 显示 IntelliJ IDEA 中的 Java 代码，用于删除流程定义。
- 代码片段：
  ```java
  public static void main(String[] args) {
      //1.得到ProcessEngine对象
      ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
      //2.得到RepositoryService对象
      RepositoryService repositoryService = processEngine.getRepositoryService();
      //3.得到ProcessDefinitionQuery对象，它是一个查询器
      ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
      //4.设置条件，查询出当前的所有流程定义，查询条件：流程定义的key=“holiday”
      //orderByProcessDefinitionVersion() 设置排序方式，根据流程定义的版本号进行排序
      List<ProcessDefinition> list = processDefinitionQuery.processDefinitionKey("holiday")
      .orderByProcessDefinitionVersion()
      .desc().list();
      //5.遍历流程定义信息
      for(ProcessDefinition processDefinition : list){
          System.out.println("流程定义ID：" + processDefinition.getId());
          System.out.println("流程定义名称：" + processDefinition.getName());
          System.out.println("流程定义的Key：" + processDefinition.getKey());
          System.out.println("流程定义的版本号：" + processDefinition.getVersion());
      }
  }
  ```

画面 4:
- 显示 IntelliJ IDEA 中的 Java 代码，用于查询流程定义。
- 代码片段：
  ```java
  List(ProcessDefinition) list = processDefinitionQuery.processDefinitionKey("holiday")
  .orderByProcessDefinitionVersion()
  .desc().list();
  ```
  ```java
  for(ProcessDefinition processDefinition : list){
      System.out.println("流程定义ID：" + processDefinition.getId());
      System.out.println("流程定义名称：" + processDefinition.getName());
      System.out.println("流程定义的Key：" + processDefinition.getKey());
      System.out.println("流程定义的版本号：" + processDefinition.getVersion());
  }
  ```
- 控制台输出显示流程定义信息，包括 ID、名称、Key 和版本号。

画面 5:
- 显示 IntelliJ IDEA 中的 Java 代码，用于删除流程定义。
- 代码片段：
  ```java
  public class DeleteProcessDefinition {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到RepositoryService对象
          RepositoryService repositoryService = processEngine.getRepositoryService();
          //3.执行删除流程定义，参数代表流程部署的id
          repositoryService.deleteDeployment("1");
      }
  }
  ```

画面 6:
- 显示 IntelliJ IDEA 中的 Java 代码，用于查询流程定义。
- 代码片段：
  ```java
  public class QueryProcessDefinition {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到RepositoryService对象
          RepositoryService repositoryService = processEngine.getRepositoryService();
          //3.得到ProcessDefinitionQuery对象，它是一个查询器
          ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
          //4.设置条件，查询出当前的所有流程定义，查询条件：流程定义的key=“holiday”
          //orderByProcessDefinitionVersion() 设置排序方式，根据流程定义的版本号进行排序
          List<ProcessDefinition> list = processDefinitionQuery.processDefinitionKey("holiday")
          .orderByProcessDefinitionVersion()
          .desc().list();
          //5.遍历流程定义信息
          for(ProcessDefinition processDefinition : list){
              System.out.println("流程定义ID：" + processDefinition.getId());
              System.out.println("流程定义名称：" + processDefinition.getName());
              System.out.println("流程定义的Key：" + processDefinition.getKey());
              System.out.println("流程定义的版本号：" + processDefinition.getVersion());
          }
      }
  }
  ```
- 控制台输出显示流程定义信息，包括 ID、名称、Key 和版本号。

画面 7:
- 显示 MySQL Workbench 中的 `information_schema` 数据库视图，列出 Activiti 的表结构。
- 表结构注释：
  ```
  act_hi_identitylink 参与者信息
  act_hi_procinst 流程实例
  act_hi_taskinst 任务实例
  act_ru_execution 执行表
  act_ru_identitylink 参与者信息
  act_ru_task 任务
  ```
- 注释说明：处理当前用户的任务，背后操作的表包括 `act_hi_actinst`、`act_hi_identitylink`、`act_hi_taskinst`、`act_ru_identitylink`、`act_ru_task`。

画面 8:
- 显示 MySQL Workbench 中的 `information_schema` 数据库视图，列出 Activiti 的表结构。
- 表结构注释：
  ```
  act_hi_identitylink 参与者信息
  act_hi_procinst 流程实例
  act_hi_taskinst 任务实例
  act_ru_execution 执行表
  act_ru_identitylink 参与者信息
  act_ru_task 任务
  ```
- 注释说明：处理当前用户的任务，背后操作的表包括 `act_hi_actinst`、`act_hi_identitylink`、`act_hi_taskinst`、`act_ru_identitylink`、`act_ru_task`。

画面 9:
- 显示 IntelliJ IDEA 中的 Java 代码，用于启动流程实例。
- 代码片段：
  ```java
  public class ActivitiStartInstance {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到RuntimeService对象
          RuntimeService runtimeService = processEngine.getRuntimeService();
          //3.创建流程实例，流程定义的key=“holiday”
          ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
          //4.输出流程实例的ID
          System.out.println("流程部署ID：" + processInstance.getDeploymentId());
          System.out.println("流程实例ID：" + processInstance.getId());
          System.out.println("活动ID：" + processInstance.getActivityId());
      }
  }
  ```
- 控制台输出显示流程部署 ID、流程实例 ID 和活动 ID。

画面 10:
- 显示 IntelliJ IDEA 中的 Java 代码，用于完成任务。
- 代码片段：
  ```java
  public class ActivitiCompleteTask {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到TaskService对象
          TaskService taskService = processEngine.getTaskService();
          //3.查询当前用户任务
          Task task = taskService.createTaskQuery()
          .processDefinitionKey("holiday")
          .taskAssignee("wangwu")
          .singleResult();
          //4.处理任务，给当前用户任务列表的查询操作的话，任务ID：task.getId();
          taskService.complete(task.getId());
          //5.输出任务的id
          System.out.println(task.getId());
      }
  }
  ```
- 控制台输出显示任务 ID。

画面 11:
- 显示 IntelliJ IDEA 中的 Java 代码，用于完成任务。
- 代码片段：
  ```java
  public class ActivitiCompleteTask {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到TaskService对象
          TaskService taskService = processEngine.getTaskService();
          //3.查询当前用户任务
          Task task = taskService.createTaskQuery()
          .processDefinitionKey("holiday")
          .taskAssignee("lishi")
          .singleResult();
          //4.处理任务，给当前用户任务列表的查询操作的话，任务ID：task.getId
