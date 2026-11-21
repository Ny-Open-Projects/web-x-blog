# 16-Activiti流程实例挂起后的任务执行测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\16-Activiti流程实例挂起后的任务执行测试_【海量资源尽在 ubkz.com】.mp4
- 时长 7分3秒（音频 424s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才我们已经通过了单个的流程实例的挂起和激活的一个测试我们可以在这里头运行这个代码就可以检测出我们当前的流程实例是属于激活状态还是属于挂起状态如果它是属于挂起的状态我们就会直接去走它的激活的方法
[00:27] 这使得我们的这个2501你看这个实例啊这个流程实例目前呢就会被激活了对不对那各位再思考一下啊如果说我们当前的这个流程实例或者是我们整个啊某一个流程定义的所有的实例也好啊只要这些实例呢属于当前正属于挂起的状态那我一起啊我们一起来思考一下啊
[00:54] 我们刚才在这边已经说了如果它已经被挂起那么它就不能够继续往后去执行对不对那现在我们可以一起来思考一下就是说现在我们当前的2501这个流程它的确是已经被我们设置为挂起的状态对吧那下面我们就可以再去编写一个测试的代码来检测一下如果它
[01:22] 如果说它已经被挂起了那现在我想呢那某个用户去执行某一个任务的时候各位思考一下啊那它是否可以啊还真的能够被执行啊那我们这样啊首先呢我把这个我把这个给它住了啊我把这个给它住了然后下一步呢我们在这边呢再去啊给它添加出一个啊添加出一个我们的这个卖方法啊那我们主要做的工作呢
[01:52] 就是来测试一下我们的这个流程啊要去让它完成某个任务对吧那比如说我们现在直接把这样的一段内容直接就可以拿过来啊好我们copy一下啊然后呢再放到我们的这个suspend process用途是2没错control vln到这来那这样我们就可以得到了我们的process engine得到了我们的这个task Service
[02:18] 然后我们还可以去查询某个用户的任务到底是不是张三的任务我们这个时候要去观察一下我们的HIRGTU用户通过这个表我们可以看到当前正在执行的应该是张三张三的这个任务铁血请假单他应该是还没有执行没有执行的话按道理我们直接把这样的代码都是直接拿过来的
[02:48] 几乎就没有改动它对吧然后呢我们就来测试一下运行的这个效果那各位我们思考一下当这个实力已经处于挂起的这个状态下如果我要去让这个任务继续往后执行咱们同学思考一下是否可以成功对吧那这个主要就是当我们的这个流程实力流程实力
[03:18] 已经处于我们的挂起状态如果要此时要让该实力继续执行继续执行
[03:51] 我们要思考的这个问题是要让它继续执行问你的问题是问题是是否可以是否可以成功对吗是否可以成功那如果能够成功那就证明我们的这个讲义肯定是有问题了对吧如果不能成功那我们这个时候要思考一下它
[04:22] 是什么也不做还是报异常对吧如果不能执行是否会抛出异常对吧是否会抛出异常那各位同学呢肯定也有自己的这个结论对吧那我的这个结论应该是肯定是会失败对不对不能成功不能够成功那肯定是要抛异常的对吧
[04:52] 抛的这个异常又会说明一个什么问题呢这个异常的说明问题肯定是说我们当前的这个2501的这个流程实例已经属于挂起的状态所以你不能够对它进行执行去完成说张商要去执行某个任务那是不可能的下面我们就可以直接来测试一下这个效果我们来看一下现在这边就已经执行完了
[05:25] 那同时呢各位也会看到它这边的确是报了一个exception对吧那这个exception表达的是什么样的一个exception是不能够完成一个已经挂起的任务对吧那这个地方各位就可以看到当我们的这个任务已经被挂起之后我们将来抛出的这个异常是activity exception
[05:54] 然后真正表达的这个问题是不能够完成我们已经被挂起的任务对吧但这个时候也有同学会提出一个思考就是那如果说我们的这个流程把这个挂起状态给它改成激活状态那我们再去运行这个代码那这个时候肯定是能成功的对吧因为我们早期的这个代码是测过的对吧所以各位如果说你要再去进一步测试的话你可以把上边的这个代码
[06:24] 进一步升开把下面的这个代码直接注掉对吧把下面这个注掉然后呢先让它激活激活完了之后你再去运行下面这个代码那肯定是可以完成啊张三的这个执行任务这样我们啊就已经给各位测了一下啊我们的这个任务如果处于被挂起的状态那么它就不能够去完成当前的这个流程的执行执行过程了对吧
[06:52] 它就不能够往后一步一步推进了对不对这个是我们在这里边进一步给各位测试了一个反面的势力好我们这个部分到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码操作 Activiti 工作流引擎，实现对流程实例的挂起与激活，以及对任务的完成操作。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 `SuspendProcessInstance.java` 文件中获取 `ProcessEngine` 和 `RuntimeService` 的代码，以及注释“//1.获取ProcessEngine对象”、“//2.获取RuntimeService对象”。
画面2: 展示了通过 `createProcessInstanceQuery().processInstanceId("2581").singleResult()` 查询流程实例，并通过 `isSuspended()` 判断其状态，终端显示“Process finished with exit code 0”。
画面3: 展示了 `SuspendProcessInstance.java` 文件中根据流程实例是否挂起，分别调用 `activateProcessInstanceById` 或 `suspendProcessInstanceById` 方法，并输出相应提示。
画面4: 展示了 `SuspendProcessInstance.java` 文件中 `processInstanceId` 的值为 "2581"，终端显示“Process finished with exit code 0”。
画面5: 展示了 `SuspendProcessInstance.java` 文件中代码区域被选中，右下角有“天猫双11 尖端好货 第2件半价”的广告弹窗。
画面6: 展示了 `ActivitiCompleteTask.java` 文件，代码中获取 `TaskService`，并创建一个任务查询，指定流程定义键为 "holiday"，任务负责人是 "shangsan"。
画面7: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，并输出任务ID。
画面8: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，并输出任务ID。
画面9: 展示了 `SuspendProcessInstance.java` 文件中 `main` 方法的代码，终端显示“Process finished with exit code 0”。
画面10: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，并输出任务ID。
画面11: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，终端显示异常信息：“org.activiti.engine.ActivitiException: Cannot complete a suspended task”。
画面12: 展示了 `SuspendProcessInstance.java` 文件中代码区域被选中，终端显示“Process finished with exit code 0”。
画面13: 展示了 `ActivitiCompleteTask.java` 文件，代码中调用 `taskService.complete(task.getId())` 完成任务，终端显示异常信息：“org.activiti.engine.ActivitiException: Cannot complete a suspended task”。
画面14: 展示了 `ActivitiCompleteTask.java` 文件中 `else` 分支代码，终端显示异常信息：“org.activiti.engine.ActivitiException: Cannot complete a suspended task”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
public static void main(String[] args) {
    //1.获取ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
```

画面2:
```java
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
    .processInstanceId("2581")
    .singleResult();
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
if(suspended){
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "激活");
}else{
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "挂起");
}
```

画面3:
```java
//3. 实例化任务查询
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
    .processInstanceId("2581")
    .singleResult();
//4. 判断当前流程定义的实例是否为挂起状态
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
//5. 判断
if(suspended){
    //如果挂起，就可以激活操作
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "激活");
}else{
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "挂起");
}
```

画面4:
```java
//3. 实例化任务查询
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
    .processInstanceId("2581")
    .singleResult();
//4. 判断当前流程定义的实例是否为挂起状态
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
//5. 判断
if(suspended){
    //如果挂起，就可以激活操作
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "激活");
}else{
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "挂起");
}
```

画面6:
```java
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户的任务
        Task task = taskService.createTaskQuery()
            .processDefinitionKey("holiday")
            .taskAssignee("shangsan")
            .singleResult();
        //4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
        taskService.complete(task.getId());
        //5.输出任务的Id
        System.out.println("任务ID：" + task.getId());
    }
}
```

画面7:
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holiday")
    .taskAssignee("shangsan")
    .singleResult();
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
//5.输出任务的Id
System.out.println("任务ID：" + task.getId());
```

画面8:
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holiday")
    .taskAssignee("shangsan")
    .singleResult();
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
//5.输出任务的Id
System.out.println("任务ID：" + task.getId());
```

画面9:
```java
public static void main(String[] args) {
    //1.获取ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
```

画面10:
```java
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
    .processDefinitionKey("holiday")
    .taskAssignee("shangsan")
    .singleResult();
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
//5.输出任务的Id
System.out.println("任务ID：" + task.getId());
```

画面11:
```java
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
```

画面12:
```java
//5.判断
if(suspended){
    //如果挂起，就可以激活操作
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "激活");
}else{
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程：" + processInstanceId + "挂起");
}
```

画面13:
```java
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
```

画面14:
```java
//4.处理任务，结合当前用户任务的完成情况，任务ID：task.getId()
taskService.complete(task.getId());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

