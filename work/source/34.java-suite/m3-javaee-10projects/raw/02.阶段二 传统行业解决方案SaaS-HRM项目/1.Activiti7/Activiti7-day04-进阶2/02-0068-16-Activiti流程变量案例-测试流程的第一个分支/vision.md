# 画面线理解：16-Activiti流程变量案例-测试流程的第一个分支

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\16-Activiti流程变量案例-测试流程的第一个分支_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:52, 01:23, 02:13, 02:49, 03:41, 04:31, 05:28, 06:01, 06:37, 07:15, 07:57, 08:36, 09:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:02:14

1) 这一组画面整体在讲如何在 Activiti 工作流引擎中通过 Java 代码设置流程变量、查询任务并完成任务。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Java 代码，通过 RuntimeService 启动流程实例并传入变量 map。
画面2：展示 BPMN 图，流程从 StartEvent 开始，经过用户任务、条件判断、并行网关，最终到 EndEvent。
画面3：展示 Java 代码，定义流程变量 key 为 "myProcess_1"。
画面4：展示 BPMN 图，流程图与画面2相同。
画面5：展示 Java 代码，通过 processEngine 获取 TaskService。
画面6：展示 Java 代码，通过 TaskService 查询当前用户任务。
画面7：展示 Java 代码，查询用户 "zhangsan" 的任务。
画面8：展示 Java 代码，通过 processEngine 获取 TaskService。
画面9：展示 MySQL 命令行，创建数据库 activiti 和表 act_ge_bytearray、act_ru_variable。
画面10：展示 Java 代码，判断任务是否为空并完成任务。
画面11：展示 BPMN 图，流程图与画面2相同。
画面12：展示 Java 代码，查询用户 "zhaoliu" 的任务。
画面13：展示 BPMN 图，流程图与画面2相同。
画面14：展示 Java 代码，查询用户 "zhaoliu" 的任务。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```java
public class VariableTest {
    public static void main(String[] args) {
        //1.得到ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key值
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(1);
        map.put("holiday", holiday);
        //4.启动流程实例，并且设置流程变量值
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
    }
}
```

画面5：
```java
//1.得到ProcessEngine
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户是否有任务
taskService.createTaskQuery().processDefinitionKey("").taskAssignee()
```

画面6：
```java
//1.得到ProcessEngine
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户是否有任务
String key = "myProcess_1";
Task task = taskService.createTaskQuery().processDefinitionKey(key)
        .taskAssignee("zhangsan").singleResult();
```

画面7：
```java
//1.得到ProcessEngine
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户是否有任务
String key = "myProcess_1";
Task task = taskService.createTaskQuery().processDefinitionKey(key)
        .taskAssignee("zhangsan").singleResult();
```

画面10：
```java
//4.判断task!=null,说明当前用户有任务
if(task!=null){
    taskService.complete(task.getTaskId());
    System.out.println("任务执行完毕");
}
```

画面9：
```sql
drop database activiti;
create database activiti;
act_ge_bytearray
act_ru_variable
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2、4、11、13：BPMN 图，结构为：
StartEvent → 用户任务 → 条件判断（holiday>0） → 并行网关 → 用户任务 → EndEvent。

画面11：BPMN 图，结构与画面2相同。

画面13：BPMN 图，结构与画面2相同。

画面14：BPMN 图，结构与画面2相同。

5) 无。
