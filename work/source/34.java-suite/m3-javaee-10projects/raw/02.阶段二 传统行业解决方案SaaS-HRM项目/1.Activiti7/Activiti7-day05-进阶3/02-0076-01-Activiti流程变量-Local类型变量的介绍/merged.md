# 01-Activiti流程变量-Local类型变量的介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\01-Activiti流程变量-Local类型变量的介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 7分16秒（音频 437s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:05] 那通过我们前边的学习啊我们呢已经给各位介绍了我们的这个流程变量啊这个流程变量呢又包括有我们的这个Global类型的变量代表的是全局变量啊那我们也可以设置我们的这个局部变量就是叫做Local类型的变量那怎么样来去做这个Local类型变量的设置啊以及我们怎么样去给它复制
[00:33] 这是我们现在给各位要来讲解的注意我们在办理任务的时候如果设置的变量是一个local类型的变量它运行的时候只能够是当前的任务结束之前才能够被使用任务结束后这个变量就无法在当前的流程实例中使用但是呢
[00:58] 我们可以通过查询我们的历史任务的方式来查询我们的这个局部变量啊那局部变量呢其实在我们的整个这个activity工作流的这个开发过程中啊相对于我们的这个全局变量而言啊它作用范围因为只是作用于当前的这个任务对吧所以呢我们局部变量它的这个用用场景呢将来应该是有局限性的啊
[01:27] 它只是当前这个任务结束之前对吧一旦当前的这个任务结束之后那我们的这个变量就会失效啊那我们怎么样来给我们的这个局部变量来负值啊那对应的这种方式我们一起来学习一下那各位可以看到啊我们在这边呢首先也是得到我们的这个task Service然后呢给我们的这个holiday付了一个holiday付了一个值啊
[01:55] 这个值复好之后我们这一点前边的这些代码跟我们的早期所学习过的Global类型的变量的使用是一模一样的然后再搞了一个MAP集合给里边存了我们的Holo里对象对吧那要注意的是我们的Task Service在SetValueBall这个方法的时候跟原来就有一些差别了SetValueBall代表的是
[02:25] 我们的这个全局变量啊后面带上一个Local之后那这个时候代表的就是我们现在所设置的这个变量是一个局部变量啊它只能够作用于当前的这个节点然后你可以继续去完成我们的这个任务那这边啊跟我们的这个全局变量的负值相比啊我们只是这里头多了一个Local其他部分没有变化啊
[02:55] 所以这个部分呢我暂时呢不打算给各位啊去演示一下效果了啊因为整个过程呢就只是在这个写代码的时候把原来这个setValue我知后面多了一个local就可以了啊设置作用域为任务的这个local变量每个任务可以设置相同的变量互不影响为什么啊因为我们的这个因为我们如果是一个局部变量的话它比如说
[03:25] 在这个节点上我们设置了在这个任务上面我们设置了一个局部变量的话那将来意味着它只作用于当前这个节点一旦这个节点上的这个任务完成那到这个部分一个新的任务又开始的时候那上面设置的这个变量对下面的这个对下面的这个任务而言是不可见的不可见他就认为这个变量不存在是这个意思所以说
[03:53] 局部类型的变量我们可以比如说我这个节点上我给我们的这个变量设置比如说我设置一个名称叫ABC那这个地方我设置名称还可以叫ABC比如说这里的ABC是1那只作用于当前的这个任务ABC取之为1那这个地方还设置变量是ABC那假如说它的取之为2那这个时候取之为2的这个值就作用于部门经理审核了
[04:23] 因为说到这个地方我们的这个ABC取之是3了那整年里审核的时候那真正它的取到的值就是3每个局部变量啊不会相互干扰是这个意思啊当然我们呢这种方式是通过啊在任务办理的时候对吧办理我们任务的时候我们在这边呢给它去设置我们的这个局部变量啊当然我们也可以呢通过当前的任务来设置
[04:51] 那这个时候你必须要知道我们的这个任务的ID然后呢直接去调用Task Service点Set localSet valuable local然后再去指定啊我们的具体的这个任务这种方式啊也是可以的啊好这两种方式我们在这边呢就给各位啊大致讲了一下啊
[05:15] 那后面如果再去做工作就应该是对于我们的这个局部变量做一些测试对不对我们的局部变量具体怎么来测试啊这个部分呢我们测试的时候各位同学啊在测的时候呢我们其实是可以去启动一个启动完流程实例对吧当流程实例启动完之后呢我们就可以直接在这边设置变量设置一个比如说Holiday取值它的Number取值为3我们取完这个值到这个地方来
[05:44] 来的话到这个上的话那我们的这个取值就将来又不可再用了啊如果你再去你不去不去再去设置我们的这个变量取值那他就认为这个值是不存在的所以局部变量呢我们在这边的测试的话啊也不打算给各位啊多去啰嗦什么了啊那这里边也有啊比如说我们呢也可以用这种方式来实现呢我们的Local局部内局部变量局部变量啊
[06:12] 当我们做完这个操作之后嘛那我将来也可以通过这个Historical Task Instance Query这种方式来查询我们的这个局部变量Lock真正所取到的这个值啊嗯这个部分呢只是给各位做了一个简单的介绍啊因为我们讲全局变量的时候把每个细节怎么去测试的过程都给各位说了啊那这边呢我大致上啊就把我们的这个局部变量
[06:42] 给各位介绍了一点介绍了一下其实对于我们而言最关键的总结的一点就是啥我们在真正设置局部变量的时候会在后面多一个Locker而对于我们的流程图而言对于我们的流程定义图而言它设置还是使用我们的UEL表达式去设置对不对没有任何的其他变化好这样我们基本上给各位完成了我们的
[07:11] 流程变量里头的这个Locker类型的变量啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

