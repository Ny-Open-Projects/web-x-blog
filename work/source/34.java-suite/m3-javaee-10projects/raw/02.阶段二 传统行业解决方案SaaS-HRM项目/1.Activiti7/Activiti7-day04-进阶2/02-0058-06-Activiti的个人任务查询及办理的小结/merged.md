# 06-Activiti的个人任务查询及办理的小结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\06-Activiti的个人任务查询及办理的小结_【海量资源尽在 ubkz.com】.mp4
- 时长 4分12秒（音频 253s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们再走的话就是关于我们的这个任务的查询以及我们的这个business key的关联这个部分呢其实我在前边给各位讲这个给各位讲这个流程实例讲这个流程实例的时候应该是讲这个流程实例的时候在这个部分呢我们就已经把这个business key怎么样去跟我们的业务系统进行关联呢
[00:27] 其实开始我已经大致讲了一下我们再给各位再给各位一起简单说一下那它的这个主要的步骤就是先呢我可以去查询比如说我查询张商是否有任务对吧那如果一旦张商有任务的话那我这个时候就可以通过他的这个task的对象直接去get the process instance id这样我就相当于拿到了我们的流程实例的id对不对
[00:57] 那拿到流程实例ID我们下一步就可以通过这个流程实例的ID进行下一步查询这时候我们通过Runtime Service就可以去查询到我们的这个查询到我们的这个Process Uses这样我就查到了我们的流程实例当流程实例都拿到之后我们就可以通过Process Uses点Get Business Key
[01:25] 我们就可以拿到我们的这个business key这就是我们所谓的给各位一直讲的我们的请假单的这个组件对不对请假单这条记录的组件ID就可以这样拿到了那你想想当我拿到这个请假单的ID之后我根据请假单的ID可不可以重新再次查询数据库这样我就能够得到我们具体这个请假单的详细信息比如说这个请假单
[01:55] 对应的这个请假单的这个请假人员是谁从哪天开始到哪天结束请几天请假类型是试假还是病假对吧还有一个就是请假的理由对不对这样的一些信息都可以给他获取出来当然当我们把这个任务查询出来的时候呢除了可以查询出这个business key之外当我们得到这个用户的任务之后其实我们下一步工作
[02:23] 也可以进一步使用这个Task Service的Complete方法直接去把这个任务执行完了对吧这个其实我们在前期课程中已经给各位详细说过了所以呢关于我们的这个个人任务的查询以及我们个人任务的办理这个部分呢我们只是给各位简单做了一下回顾你看我们的这个任务的办理主要就是通过Task Service的Complete方法
[02:53] 来完成这个具体任务的办理对吧好这个部分啊大致上大致上啊我们就把这个用户的任务啊就给各位简单说到这儿啊当然这边也补充了一下啊就是说我们先最好是查询一下这个任务这个用户有没有这个任务对吧当这个用户有这个任务的时候Task不为空Task不为空我们才有必要把这个任务去执行的对吧
[03:20] 这样照6就可以执行他的任务了大概是这个意思所以我们给各位的这个整结就是将来我们在执行任务之前最好先去查一下这个用户有没有任务一旦这个用户有任务我们才去执行这个任务对不对这样其实就相当于做了一个提前做了一个权限的判断对吧我查一下你有任务完了我才让你去执行任务对吧
[03:49] 而不是一上来就开始执行任务对不对好这是关于我们过人任务整体上我们从这个任务的分配人以及任务的查询以及任务的办理几个部分给各位做了一个详细的说明那过人任务部分我们就暂时给各位说到这里边

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

