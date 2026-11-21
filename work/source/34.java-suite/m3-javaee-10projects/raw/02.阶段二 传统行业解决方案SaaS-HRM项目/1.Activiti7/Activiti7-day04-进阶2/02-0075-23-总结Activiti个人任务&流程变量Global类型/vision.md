# 画面线理解：23-总结Activiti个人任务&流程变量Global类型

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\23-总结Activiti个人任务&流程变量Global类型_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:23, 00:35, 01:12, 01:46, 02:45, 03:13, 03:34, 04:08, 04:30, 04:49, 05:12, 05:45, 06:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:07:55

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中任务分配、流程变量类型及使用方法，包括 UEL 表达式、流程变量设置与查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 标题：2.1.1 固定分配
- 内容：在进行业务流程建模时指定固定的任务负责人。
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 展示了属性面板：Name: 任务处理节点, Assignee: 张三丰, Multi Instance: false。

画面 2:
- 标题：2.1.1.1 UEL 表达式
- 内容：Activiti 使用 UEL 表达式，UEL 是 Java EE6 规范的一部分，UEL (Unified Expression Language) 即统一表达式语言。
- 内容：Activiti 支持两个 UEL 表达式：UEL-value 和 UEL-method。
- 内容：UEL-value 定义如下。

画面 3:
- 内容：Create: 任务创建后触发
- 内容：Assignment: 任务分配后触发
- 内容：Delete: 任务完成后触发
- 内容：All: 所有事件发生都触发
- 内容：java 逻辑 或 表达式；表达式参考上边的介绍的 UFL 表达式，这里主要介绍监听使用。

画面 4:
- 代码：
```java
@Test
public void findPersonalTaskList() {
    // 流程定义key
    String processDefinitionKey = "holiday";
    // 任务负责人
    String assignee = "张三丰";
    // 创建TaskService
    TaskService taskService = processEngine.getTaskService();
    List<Task> list = taskService.createTaskQuery()
        .processDefinitionKey(processDefinitionKey)
        .includeProcessVariables().taskAssignee(assignee).list();
    for (Task task : list) {
        System.out.println("-------------");
        System.out.println("流程实例Id: " + task.getProcessInstanceId());
        System.out.println("任务负责人: " + task.getAssignee());
        System.out.println("任务名称: " + task.getName());
    }
}
```

画面 5:
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 任务处理节点之间有连线，标注了条件表达式：${holiday.num==1}。

画面 6:
- 标题：3.2 流程变量类型
- 表格：Table 15.9. Variable Types
- 表格内容：
| Type | name | Description |
|---|---|---|
| string | Value is threaded as a java.lang.String. Raw JSON text. | Value is threaded as a java.lang.String. Raw JSON text. |
| integer | Value is threaded as a java.lang.Integer. When writing, text. | Value is threaded as a java.lang.Integer. When writing, text. |
| short | Value is threaded as a java.lang.Short. When writing, text. | Value is threaded as a java.lang.Short. When writing, text. |
| long | Value is threaded as a java.lang.Long. When writing, text. | Value is threaded as a java.lang.Long. When writing, text. |
| double | Value is threaded as a java.lang.Double. When writing, text. | Value is threaded as a java.lang.Double. When writing, text. |
| boolean | Value is threaded as a java.lang.Boolean. When writing, text. | Value is threaded as a java.lang.Boolean. When writing, text. |
| date | Value is threaded as a java.util.Date. When writing, the text. | Value is threaded as a java.util.Date. When writing, the text. |
| binary | Binary variable, threaded as an array of bytes. The value stream. | Binary variable, threaded as an array of bytes. The value stream. |
| serializable | Serializable representation of a Serializable Java-object. | Serializable representation of a Serializable Java-object. |

画面 7:
- 标题：3.4 流程变量的使用方法
- 内容：第一步：设置流程变量
- 内容：第二步：通过 UEL 表达式使用流程变量
- 内容：> 可以在 assignee 处设置 UEL 表达式，表达式的值为任务的负责人。比如：${assignee}，assignee 就是一个流程变量名称。
- 内容：Activiti 获取 UEL 表达式的值，将流程变量 assignee 的值，作为任务的负责人进行任务分配。
- 内容：> 可以在连线上设置 UEL 表达式，决定流程走向。
- 内容：比如：${price>=10000} 和 ${price<10000}；price 就是一个流程变量名称，uel 表达式结果类型为布尔类型。
- 内容：如果 UEL 表达式是 true，要决定 流程执行走向。

画面 8:
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 任务处理节点之间有连线，标注了条件表达式：${holiday.num==1}。
- 展示了属性面板：Name: 任务处理节点, Assignee: 张三丰, Multi Instance: false。

画面 9:
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 任务处理节点之间有连线，标注了条件表达式：${holiday.num==1}。
- 展示了属性面板：Name: 任务处理节点, Assignee: 张三丰, Multi Instance: false。

画面 10:
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 任务处理节点之间有连线，标注了条件表达式：${holiday.num==1}。
- 展示了属性面板：Name: 任务处理节点, Assignee: 张三丰, Multi Instance: false。

画面 11:
- 代码：
```java
Map<String, Object> variables = new HashMap<String, Object>();
// 变量名num，变量值是holiday.getNum()，变量名也可以是一个对象
variables.put("num", holiday.getNum());

RuntimeService runtimeService = processEngine.getRuntimeService();
ProcessInstance processInstance = runtimeService
    .startProcessInstanceByKey(processDefinitionKey, variables);

System.out.println("流程实例Id: " + processInstance.getProcessInstanceId());
```
- 说明：startProcessInstanceByKey(processDefinitionKey, variables) 流程变量作用域是一个流程实例，流程变量使用 Map 存储，同一个流程实例设置 map 中 key 相同，后者覆盖前者。

画面 12:
- 代码：
```java
public void setGlobalVariableByExecutionId() {
    // 当前流程实例执行 id，通常设置为当前执行的流程实例
    String executionId = "2681";

    RuntimeService runtimeService = processEngine.getRuntimeService();
    Holiday holiday = new Holiday();
    holiday.setNum(3);

    // 通过流程实例 id 设置流程变量
    runtimeService.setVariable(executionId, "holiday", holiday);

    // 一次设置多个值
    // runtimeService.setVariables(executionId, variables)
}
```

画面 13:
- 代码：
```java
TaskService taskService = processEngine.getTaskService();
Holiday holiday = new Holiday();

// 通过任务设置流程变量
taskService.setVariable(taskId, "holiday", holiday);
// 一次设置多个值
// taskService.setVariables(taskId, variables)
```
- 注意：任务必须是当前待办任务，如果任务已经结束，报错。

画面 14:
- 内容：设置流程变量会在当前执行流程变量表插入记录，同时也会在历史流程变量表也插入记录。
- 内容：SELECT * FROM act_ru_variable #当前流程变量表
- 内容：记录当前运行流程实例可使用的流程变量，包括 global 和 local 变量
- 内容：Id: 主键
- 内容：Type: 变量类型
- 内容：Name: 变量名称
- 内容：Execution_id: 所属流程实例执行 id，global 和 local 变量都存储
- 内容：Proc_inst_id: 所属流程实例 id，global 和 local 变量都存储
- 内容：Task_id: 所属任务 id，local 变量存储
- 内容：Bytearray_: serializable 类型变量存储对应 act_ge_bytearray 表的 id
- 内容：Double_: double 类型变量值
- 内容：Long_: long 类型变量值
- 内容：Text_: text 类型变量值
- 内容：SELECT * FROM act_hi_varinst #历史流程变量表
- 内容：记录所有已创建的流程变量，包括 global 和 local 变量
- 内容：字段意义参考当前流程变量表。
