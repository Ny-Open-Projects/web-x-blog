# 画面线理解：06-Activiti的个人任务查询及办理的小结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\06-Activiti的个人任务查询及办理的小结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:25, 00:29, 00:42, 01:04, 01:26, 02:21, 02:22, 02:42, 02:57, 02:58, 03:23, 03:26, 03:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:56:55

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中任务监听器的实现、通过 businessKey 关联业务数据以及任务的办理与完成操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：讲解定义任务监听器，需实现 org.activiti.engine.delegate.TaskListener 接口，代码示例为 public class MyTaskListener implements TaskListener { @Override public void notify(DelegateTask delegateTask) { //这里指定任务负责人 delegateTask.setAssignee("张三"); } }。
画面2：标题为“2.2.1 关联 businessKey”，讲解在查询待办任务时，通过 businessKey 关联查询业务系统的请假单表，获取请假天数等信息。
画面3：与画面2内容相同，展示代码实现部分。
画面4：展示代码实现，通过 task 对象获取 processInstanceId，再通过 processInstanceId 获取 processInstance 对象，最后通过 processInstance 对象获取 businessKey。
画面5：与画面4内容相同，展示代码实现。
画面6：标题为“2.3 办理任务”，开始讲解如何完成任务。
画面7：展示完成任务的代码示例：@Test public void completTask() { //任务id }。
画面8：展示完成任务的代码示例，其中 taskId 为 "18035"，并调用 taskService.complete(taskId)。
画面9：与画面8内容相同，展示完成任务的代码示例。
画面10：展示注意事项，指出在实际应用中完成任务前需要校验任务的负责人是否具有该任务的办理权限。
画面11：展示校验任务负责人权限的代码逻辑，通过 createTaskQuery().taskId(taskId).taskAssignee(assignee).singleResult() 获取任务对象，然后判断 task 是否为 null。
画面12：标题为“第3章 流程变量”，开始讲解流程变量。
画面13：与画面12内容相同，标题为“第3章 流程变量”。
画面14：与画面13内容相同，标题为“第3章 流程变量”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
public class MyTaskListener implements TaskListener {
    @Override
    public void notify(DelegateTask delegateTask) {
        //这里指定任务负责人
        delegateTask.setAssignee("张三");
    }
}

画面2：
//2.创建RuntimeService对象
RuntimeService runtimeService = processEngine.getRuntimeService();
TaskService taskService = processEngine.getTaskService();

//3.通过TaskService查询到个人任务
Task task = taskService.createTaskQuery().processDefinitionKey("holiday")
        .taskAssignee("zhangsan").singleResult();

画面4：
//4.通过task对象，得到任务id
String processInstanceId = task.getProcessInstanceId();

//5.通过流程实例id，得到流程实例对象
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
        .processInstanceId(processInstanceId)
        .singleResult();

//6.对processInstance对象，得到businessKey
String businessKey = processInstance.getBusinessKey();

//7.根据businessKey就可以得到请假单的信息
System.out.println("businessKey:"+businessKey);

画面7：
@Test
public void completTask() {
    //任务id
}

画面8：
String taskId = "18035";
// 创建TaskService
TaskService taskService = processEngine.getTaskService();
taskService.complete(taskId);
System.out.println("完成任务");

画面10：
注意：在实际应用中，完成任务前需要校验任务的负责人是否具有该任务的办理权限。

画面11：
// 指定要办理任务id
String taskId = "2802";
// 任务负责人
String assignee = "zhaoliu";

TaskService takService = processEngine.getTaskService();

// 这里只指定任务id并没有指定任务负责人，只要调用complete，该任务就完成
// 所以说必须校验任务权限
// 校验方法：
Task task = takService.createTaskQuery().taskId(taskId)
        .taskAssignee(assignee).singleResult();

if (task != null) {
    takService.complete(taskId);
    System.out.println("完成任务！！！");
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2标题：“2.2.1 关联 businessKey”。
画面6标题：“2.3 办理任务”。
画面12标题：“第3章 流程变量”。
画面11中，代码逻辑中通过 createTaskQuery().taskId(taskId).taskAssignee(assignee).singleResult() 查询任务，如果 task 不为 null，则调用 complete(taskId) 完成任务。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
