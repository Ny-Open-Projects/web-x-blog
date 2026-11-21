# 画面线理解：01-Activiti流程变量-Local类型变量的介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\01-Activiti流程变量-Local类型变量的介绍_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:25, 01:22, 01:32, 01:45, 02:00, 02:40, 03:21, 04:51, 05:28, 05:59, 06:05, 06:23, 06:47, 07:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:13:10

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中如何在任务办理时设置 local 变量，包括代码实现、流程图示意及历史变量查询方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“3.6.1 任务办理时设置”，代码示例为在 `completeTask()` 方法中定义并设置 local 变量 `holiday`。
画面2：同画面1，鼠标光标在代码区域。
画面3：同画面1，鼠标光标在代码区域。
画面4：同画面1，鼠标光标在代码区域，底部显示公司地址和电话。
画面5：展示 PPT 页面“黑马程序员”Logo及文字“改变中国IT教育，我们正在行动”，代码示例为设置 local 变量 `holiday` 并调用 `setVariablesLocal` 方法。
画面6：同画面5，鼠标光标在代码区域，下方有说明文字“设置作用域为该任务的 local 变量，每个任务可以设置同名的变量，互不影响。”
画面7：展示 Activiti Designer 软件界面，显示 BPMN 流程图，包含 StartEvent、用户任务、结束事件等节点。
画面8：展示 PPT 页面“3.6.2 通过当前任务设置”，代码示例为通过 `setVariableLocal` 方法设置 local 变量。
画面9：同画面7，显示 Activiti Designer 软件界面。
画面10：展示 PPT 页面“3.6.4 Local 变量测试 2”，文字说明可通过 `historyService` 查询历史任务的 local 变量。
画面11：同画面10，代码示例为创建 `HistoricTaskInstanceQuery` 对象并调用 `includeTaskLocalVariables()` 方法。
画面12：同画面11，代码示例为遍历查询结果并打印任务 ID、名称、负责人及 local 变量。
画面13：同画面10，文字说明“Local 变量在任务结束后无法在当前流程实例执行中使用，如果后续的流程执行需要用到此变量则会报错。”
画面14：展示 PPT 页面“3.6.3 Local 变量测试 1”，代码示例为通过 `setVariableLocal` 方法设置 local 变量，并附有注意事项“任务 id 必须是当前待办任务 id，act_ru_task 中存在。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Test
public void completTask() {
    //任务id
    String taskId = "";
    TaskService taskService = processEngine.getTaskService();
    // 定义流程变量
    Map<String, Object> variables = new HashMap<String, Object>();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    // 定义流程变量
}
```

画面5：
```java
Map<String, Object> variables = new HashMap<String, Object>();
//变量名是holiday，变量值是holiday对象
variables.put("holiday", holiday);
// 设置local变量，作用域为该任务
taskService.setVariablesLocal(tasked, variables);
taskService.complete(taskId);
```

画面8：
```java
@Test
public void setLocalVariableByTaskId(){
    //当前待办任务id
    String taskId="1404";
    TaskService taskService = processEngine.getTaskService();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    //通过任务设置流程变量
    taskService.setVariableLocal(taskId, "holiday", holiday);
    //一次设置多个值
    //taskService.setVariablesLocal(taskId, variables)
}
```

画面10：
```java
// 创建历史任务查询对象
HistoricTaskInstanceQuery historicTaskInstanceQuery = historyService
    .createHistoricTaskInstanceQuery();
// 查询结果包括 local 变量
historicTaskInstanceQuery.includeTaskLocalVariables();
```

画面11：
```java
for (HistoricTaskInstance historicTaskInstance : list) {
    System.out.println("============== 任务 Id ：" + historicTaskInstance.getId());
    System.out.println("任务 名 称 ：" + historicTaskInstance.getName());
    System.out.println("任务 负 责 人 ：" + historicTaskInstance.getAssignee());
    System.out.println("任务 local 变 量 ：" + historicTaskInstance.getTaskLocalVariables());
}
```

画面14：
```java
@Test
public void setLocalVariableByTaskId(){
    //当前待办任务id
    String taskId="1404";
    TaskService taskService = processEngine.getTaskService();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    //通过任务设置流程变量
    taskService.setVariableLocal(taskId, "holiday", holiday);
    //一次设置多个值
    //taskService.setVariablesLocal(taskId, variables)
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面7：流程图结构：
- StartEvent → 用户任务（“部门经理审批”）→ 用户任务（“总经理审批”）→ EndEvent
画面10：标题“3.6.4 Local 变量测试 2”，文字说明“在部门经理审核、总经理审核、人事经理审核时设置 local 变量，可通过 historyService 查询每个历史任务时将流程变量的值也查询出来。”
画面13：标题“3.6.4 Local 变量测试 2”，文字说明“Local 变量在任务结束后无法在当前流程实例执行中使用，如果后续的流程执行需要用到此变量则会报错。”
画面14：标题“3.6.3 Local 变量测试 1”，文字说明“任务 id 必须是当前待办任务 id，act_ru_task 中存在。”

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
