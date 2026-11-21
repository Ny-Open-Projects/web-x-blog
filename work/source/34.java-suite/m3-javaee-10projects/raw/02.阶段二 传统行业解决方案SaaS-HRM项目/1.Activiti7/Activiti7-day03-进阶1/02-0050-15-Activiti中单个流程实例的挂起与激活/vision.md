# 画面线理解：15-Activiti中单个流程实例的挂起与激活

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\15-Activiti中单个流程实例的挂起与激活_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:10, 01:49, 02:54, 03:31, 04:30, 04:58, 05:39, 05:56, 06:23, 06:39, 07:14, 07:39, 08:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:46:50

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码操作 Activiti 工作流引擎，实现对流程实例的挂起与激活功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个名为 `suspendProcessInstance` 的测试方法，用于根据流程实例 ID 获取流程实例并判断其是否挂起，若挂起则激活，否则挂起。
画面2：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，用于获取流程引擎和运行时服务，查询流程定义并判断其是否挂起。
画面3：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，使用 `createProcessInstanceQuery` 查询流程实例。
画面4：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，调用 `runtimeService.createProcessInstanceQuery()` 方法并查看其方法签名。
画面5：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，判断流程定义是否挂起，并根据结果输出相应信息。
画面6：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，若流程实例挂起则激活，否则挂起。
画面7：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，执行后在控制台输出流程实例 ID 和流程定义 ID。
画面8：展示 MySQL 命令行工具中执行的 SQL 语句，用于创建名为 `activiti` 的数据库。
画面9：展示 `ActivitiDeployment.java` 文件的 `main` 方法，用于部署流程定义，通过 `repositoryService` 读取 `diagram` 文件夹下的 `holiday.bpmn` 文件并部署。
画面10：展示 `ActivitiStartInstance.java` 文件的 `main` 方法，用于启动流程实例，输出流程定义 ID、流程实例 ID 和活动 ID。
画面11：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，执行后在控制台输出异常信息，提示 `NullPointerException`。
画面12：展示 MySQL 命令行工具中执行的 SQL 语句，用于更新 `act_ru_execution` 表。
画面13：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，使用 `runtimeService` 查询流程实例并判断其是否挂起。
画面14：展示 `suspendProcessInstance` 测试方法的完整代码，用于根据流程实例 ID 获取流程实例并判断其是否挂起，若挂起则激活，否则挂起。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Test
public void suspendOrActiveProcessInstance() {
    // 流程实例Id
    String processInstanceId = "";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    // 根据流程实例Id查询流程实例
    ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
            .processInstanceId(processInstanceId).singleResult();
    boolean suspend = processInstance.isSuspended();
    if(suspend){
        // 如果暂停则激活
        runtimeService.activateProcessInstanceById(processInstanceId);
        System.out.println("流程实例："+"processInstanceId"+"激活");
    }else{
        // 如果激活则挂起
        runtimeService.suspendProcessInstanceById(processInstanceId);
        System.out.println("流程实例："+"processInstanceId"+"挂起");
    }
}
```

画面2：
```java
public class SuspendProcessInstance2 {
    public static void main(String[] args) {
        // 获取流程引擎对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        // 获取RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        // 查询流程定义对象
        ProcessDefinition processDefinition = repositoryService.createProcessDefinitionQuery()
                .processDefinitionKey("holiday").singleResult();
        // 判断当前流程定义的实例是否为暂停状态
        boolean suspended = processDefinition.isSuspended();
        String processDefinitionId = processDefinition.getId();
        if(suspended){
```

画面3：
```java
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
        .processInstanceBusinessKey("holiday").singleResult();
```

画面4：
```java
runtimeService.createProcessInstanceQuery()
```

画面5：
```java
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
if(suspended){
    // 如果暂停则激活
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"激活");
}else{
    // 如果激活则挂起
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"挂起");
}
```

画面6：
```java
if(suspended){
    // 如果暂停则激活
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"激活");
}else{
    // 如果激活则挂起
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"挂起");
}
```

画面7：
```java
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
        .processInstanceBusinessKey("holiday").singleResult();
```

画面8：
```sql
drop database activiti;
create database activiti;
```

画面9：
```java
InputStream is = ActivitiDeployment.class.getClassLoader().getResourceAsStream("diagram");
ZipInputStream zipInputStream = new ZipInputStream(is);
```

画面10：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
System.out.println("流程定义ID：" + processDefinition.getId());
System.out.println("流程实例ID：" + processInstance.getId());
System.out.println("活动ID：" + processInstance.getActivityId());
```

画面11：
```java
Exception in thread "main" java.lang.NullPointerException
at line.15
```

画面12：
```sql
alter table act_ru_execution modify column id varchar(64) not null;
```

画面13：
```java
// 获取RuntimeService
RuntimeService runtimeService = processEngine.getRuntimeService();
// 查询流程实例
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
        .processInstanceId("2501").singleResult();
// 判断当前流程定义的实例是否为暂停状态
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
if(suspended){
    // 如果暂停则激活
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"激活");
}else{
    // 如果激活则挂起
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"挂起");
}
```

画面14：
```java
@Test
public void suspendOrActiveProcessInstance() {
    // 流程实例Id
    String processInstanceId = "";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    // 根据流程实例Id查询流程实例
    ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
            .processInstanceId(processInstanceId).singleResult();
    boolean suspend = processInstance.isSuspended();
    if(suspend){
        // 如果暂停则激活
        runtimeService.activateProcessInstanceById(processInstanceId);
        System.out.println("流程实例："+"processInstanceId"+"激活");
    }else{
        // 如果激活则挂起
        runtimeService.suspendProcessInstanceById(processInstanceId);
        System.out.println("流程实例："+"processInstanceId"+"挂起");
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
