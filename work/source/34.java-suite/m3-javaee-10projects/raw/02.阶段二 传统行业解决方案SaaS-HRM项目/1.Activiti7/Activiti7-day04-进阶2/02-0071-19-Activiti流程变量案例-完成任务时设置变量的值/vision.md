# 画面线理解：19-Activiti流程变量案例-完成任务时设置变量的值

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\19-Activiti流程变量案例-完成任务时设置变量的值_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:40, 02:28, 02:50, 03:28, 03:53, 04:11, 04:28, 04:59, 05:49, 06:15, 06:36, 07:13, 08:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:04:38

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流中通过 Java 代码为任务完成时设置流程变量，并展示相关代码实现和类结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 PPT 页面，标题为“3.5.3.2 任务办理时设置”，内容讲解任务完成时设置流程变量的机制，并展示代码示例 `@Test public void completTask() { ... }`。
画面 2: PPT 页面内容延续，展示代码中定义流程变量 `Map<String, Object> variables = new HashMap<String, Object>();` 并设置变量值 `variables.put("holiday", holiday);`。
画面 3: PPT 页面内容延续，展示代码中调用 `taskService.complete(taskId, variables);` 完成任务并设置变量。
画面 4: IDE 界面，展示 `VariableTest2.java` 文件，代码为 `public static void main(String[] args) { ... }`，用于启动流程实例并设置变量。
画面 5: IDE 界面，展示 `VariableTest2.java` 文件，代码中定义了 `RuntimeService runtimeService` 并设置流程变量 `map.put("holiday", holiday);`。
画面 6: IDE 界面，展示 `VariableTest2.java` 文件，代码中调用 `runtimeService.startProcessInstanceByKey(key, map);` 启动流程实例并设置变量。
画面 7: IDE 界面，展示 `VariableTest2.java` 文件，代码中定义了 `RuntimeService runtimeService` 并设置流程变量 `map.put("holiday", holiday);`。
画面 8: IDE 界面，展示 `VariableTest2.java` 文件，代码中定义了 `RuntimeService runtimeService` 并设置流程变量 `map.put("holiday", holiday);`。
画面 9: IDE 界面，展示 `VariableTest2.java` 文件，代码中定义了 `RuntimeService runtimeService` 并设置流程变量 `map.put("holiday", holiday);`。
画面 10: IDE 界面，展示 `Holiday.java` 文件，代码为 `public class Holiday implements Serializable { ... }`，定义了 `Holiday` 类的属性和方法。
画面 11: IDE 界面，展示 `VariableTest2.java` 文件，代码中定义了 `TaskService taskService` 并设置流程变量 `map.put("holiday", holiday);`。
画面 12: IDE 界面，展示 `VariableTest2.java` 文件，代码中定义了 `TaskService taskService` 并设置流程变量 `map.put("holiday", holiday);`。
画面 13: PPT 页面，内容与画面 1 相同，展示 `@Test public void completTask() { ... }` 代码。
画面 14: PPT 页面，内容与画面 1 相同，展示 `@Test public void completTask() { ... }` 代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Test
public void completTask() {
    //任务id
    String taskId = "";
    TaskService taskService = processEngine.getTaskService();
    Holiday holiday = new Holiday();
    holiday.setNum(4);
    // 定义流程变量
    Map<String, Object> variables = new HashMap<String, Object>();
    //变量名是holiday，变量值是holiday对象
    variables.put("holiday", holiday);
    taskService.complete(taskId, variables);
}
```

画面 2:
```java
@Test
public void completTask() {
    //任务id
    String taskId = "";
    TaskService taskService = processEngine.getTaskService();
    Holiday holiday = new Holiday();
    holiday.setNum(4);
    // 定义流程变量
    Map<String, Object> variables = new HashMap<String, Object>();
    //变量名是holiday，变量值是holiday对象
    variables.put("holiday", holiday);
    taskService.complete(taskId, variables);
}
```

画面 3:
```java
@Test
public void completTask() {
    //任务id
    String taskId = "";
    TaskService taskService = processEngine.getTaskService();
    Holiday holiday = new Holiday();
    holiday.setNum(4);
    // 定义流程变量
    Map<String, Object> variables = new HashMap<String, Object>();
    //变量名是holiday，变量值是holiday对象
    variables.put("holiday", holiday);
    taskService.complete(taskId, variables);
}
```

画面 4:
```java
public class VariableTest2 {
    public static void main(String[] args) {
        //1.调用ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.调用TaskService
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户是否有任务
        String key = "myProcess_1";
        Task task = taskService.createTaskQuery().processDefinitionKey(key)
                .taskAssignee("zhaoLiu").singleResult();
        //4.判断task!=null,说明当前用户有任务
        if(task!=null){
            taskService.complete(task.getlD());
        }
        //5.启动流程实例：同时设置流程变量
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
        System.out.println(processInstance.getName());
        System.out.println(processInstance.getProcessDefinitionId());
    }
}
```

画面 5:
```java
public class VariableTest2 {
    public static void main(String[] args) {
        //1.调用ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.调用RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key：myProcess_1
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(5);
        map.put("holiday", holiday);
        //4.启动流程实例，并且设置流程变量
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
        //5.输出流程实例信息
        System.out.println(processInstance.getName());
        System.out.println(processInstance.getProcessDefinitionId());
    }
}
```

画面 6:
```java
public class VariableTest2 {
    public static void main(String[] args) {
        //1.调用ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.调用RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key：myProcess_1
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(5);
        map.put("holiday", holiday);
        //4.启动流程实例，并且设置流程变量
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
        //5.输出流程实例信息
        System.out.println(processInstance.getName());
        System.out.println(processInstance.getProcessDefinitionId());
    }
}
```

画面 7:
```java
public class VariableTest2 {
    public static void main(String[] args) {
        //1.调用ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.调用RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key：myProcess_1
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(5);
        map.put("holiday", holiday);
        //4.启动流程实例，并且设置流程变量
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
        //5.输出流程实例信息
        System.out.println(processInstance.getName());
        System.out.println(processInstance.getProcessDefinitionId());
    }
}
```

画面 8:
```java
public class VariableTest2 {
    public static void main(String[] args) {
        //1.调用ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.调用RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key：myProcess_1
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(5);
        map.put("holiday", holiday);
        //4.启动流程实例，并且设置流程变量
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
        //5.输出流程实例信息
        System.out.println(processInstance.getName());
        System.out.println(processInstance.getProcessDefinitionId());
    }
}
```

画面 9:
```java
public class VariableTest2 {
    public static void main(String[] args) {
        //1.调用ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.调用RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key：myProcess_1
        String key = "myProcess_1";
        Map<String, Object> map = new
