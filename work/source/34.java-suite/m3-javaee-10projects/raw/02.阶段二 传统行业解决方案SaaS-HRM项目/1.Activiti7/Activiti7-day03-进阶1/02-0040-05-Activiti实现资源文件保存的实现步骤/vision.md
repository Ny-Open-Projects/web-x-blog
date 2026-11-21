# 画面线理解：05-Activiti实现资源文件保存的实现步骤

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\05-Activiti实现资源文件保存的实现步骤_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:15, 01:09, 01:40, 03:14, 03:21, 03:28, 03:51, 04:02, 04:08, 04:34, 04:48, 06:58, 07:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:38:34

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Activiti 工作流引擎的 API 查询、启动、完成任务及删除流程定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 QueryBpmFile.java 文件，注释说明了两种获取流程定义的方式，当前聚焦于第一种方式（使用 Activiti API）。代码中展示了 public class QueryBpmFile {} 的结构。
画面2：在 QueryBpmFile.java 中，光标位于 public class QueryBpmFile { 语句后，弹出 Java 类的继承方法列表，如 protected Object clone() 等。
画面3：在 QueryBpmFile.java 中，光标位于 main 方法的开头，注释提示“//1.博到ProcessEngine实例”，准备开始编写代码。
画面4：切换到 MySQL Workbench，展示 act_hi_taskinst 表的查询结果，包含 ID、NAME、DEPLOYMENT_ID_、SUSPENSION_STATE_ 等字段。
画面5：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//5.执行查询操作，查询出想要的流程定义”处，准备编写查询逻辑。
画面6：切换到 ActivitiCompleteTask.java 文件，展示如何通过 TaskService 创建并完成一个任务，代码中包含 processEngine.getTaskService()、createTaskQuery()、complete() 等方法。
画面7：在 ActivitiCompleteTask.java 中，光标位于 taskService.complete(task.getId()); 语句后，展示任务完成后的输出。
画面8：切换到 ActivitiStartInstance.java 文件，展示如何通过 RuntimeService 启动流程实例，代码中包含 startProcessInstanceByKey("holiday") 方法。
画面9：切换到 DeleteProcessDefinition.java 文件，展示如何通过 RepositoryService 删除流程部署，代码中包含 deleteDeployment(deploymentId) 方法。
画面10：切换到 QueryProcessDefinition.java 文件，展示如何通过 RepositoryService 查询流程定义，代码中包含 createProcessDefinitionQuery().processDefinitionKey("holiday").orderByProcessDefinitionVersion().desc().list() 方法。
画面11：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//5.执行查询操作，查询出想要的流程定义”处，准备编写查询逻辑。
画面12：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//5.执行查询操作，查询出想要的流程定义”处，准备编写查询逻辑。
画面13：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)”处，准备编写获取流程定义信息的代码。
画面14：在 QueryBpmFile.java 中，光标位于 main 方法的注释“//8.转换成OutputStream流”处，准备编写将流程定义信息转换为输出流的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.ithema.day03.activiti;

/**
 * 1.从Activiti的act_ge_bytearray表中读取两个流程文件
 * 2.按两个流程文件的名称分别到目录：/Activiti/开始/Activiti/day01/资料
 * 技术方案：
 * 1.第一种方式：其实就是使用activiti的api来实现
 * 2.第二种方式：其实就是直接读取，可以使用jdbc的blob类型，clok类型读取数据，并保存
 * 10万条数据，最好commons-io.jar可以轻松解决此问题
 * 真实应用场景：用户想要查看这个请假流程有没有哪些步骤变更？
 *
 * public class QueryBpmFile {
```

画面2：
```java
public class QueryBpmFile {
    protected Object clone()
    public boolean equals(Object obj)
    public int hashCode()
    public String toString()
    protected void finalize()
    static final
    private static final
    main() method declaration
```

画面3：
```java
public class QueryBpmFile {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
    }
```

画面4：
SQL 查询语句未显示，但表结构显示：
```sql
SELECT * FROM act_hi_taskinst;
```

画面5：
```java
public class QueryBpmFile {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        //2.博到RepositoryService对象
        //3.博到查询器：ProcessDefinitionQuery对象
        //4.设置查询条件
        //5.执行查询操作，查询出想要的流程定义
        //6.通过流程定义信息，得到部署ID
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.转换成OutputStream流
        //9.输入流，输出流的转换
    }
```

画面6：
```java
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博到TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户任务
        Task task = taskService.createTaskQuery()
                .processDefinitionKey("holiday")
                .taskAssignee("wanggu")
                .singleResult();
        //4.处理任务，结合当前用户任务的完成操作的流，任务ID.task.getId()
        taskService.complete(task.getId());
        //5.输出任务的id
        System.out.println(task.getId());
    }
}
```

画面7：
```java
//1.博到ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.博到TaskService对象
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户任务
Task task = taskService.createTaskQuery()
        .processDefinitionKey("holiday")
        .taskAssignee("wanggu")
        .singleResult();
//4.处理任务，结合当前用户任务的完成操作的流，任务ID.task.getId()
taskService.complete(task.getId());
//5.输出任务的id
System.out.println(task.getId());
```

画面8：
```java
public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博到RuntimeService对象
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.创建流程实例，流程定义的key需要是 holiday
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
        //4.输出流程实例ID
        System.out.println("流程实例ID:"+processInstance.getId());
        //5.输出流程定义ID
        System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());
        //6.输出活动ID
        System.out.println("活动ID:"+processInstance.getActivityId());
    }
}
```

画面9：
```java
public class DeleteProcessDefinition {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博到RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.删除流程部署，删除流程部署ID
        repositoryService.deleteDeployment(deploymentId);
    }
}
```

画面10：
```java
public class QueryProcessDefinition {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博到RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.博到查询器：ProcessDefinitionQuery对象
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置条件：查询所有流程定义，查询方式：按流程定义的key查询
        List<ProcessDefinition> list = processDefinitionQuery.processDefinitionKey("holiday")
                .orderByProcessDefinitionVersion().desc().list();
        //5.输出流程定义信息
        for(ProcessDefinition processDefinition : list){
            System.out.println("流程定义ID:"+processDefinition.getId());
            System.out.println("流程定义的key:"+processDefinition.getKey());
            System.out.println("流程定义的版本:"+processDefinition.getVersion());
            System.out.println("流程部署的ID:"+processDefinition.getDeploymentId());
        }
    }
}
```

画面13：
```java
public class QueryBpmFile {
    public static void main(String[] args) {
        //1.博到ProcessEngine实例
        //2.博到RepositoryService对象
        //3.博到查询器：ProcessDefinitionQuery对象
        //4.设置查询条件
        //5.执行查询操作，查询出想要的流程定义
        //6.通过流程定义信息，得到部署ID
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.转换成OutputStream流
        //9.输入流，输出流的转换
    }
}
```

画面14：
```java
public class QueryBpmFile {
    public
