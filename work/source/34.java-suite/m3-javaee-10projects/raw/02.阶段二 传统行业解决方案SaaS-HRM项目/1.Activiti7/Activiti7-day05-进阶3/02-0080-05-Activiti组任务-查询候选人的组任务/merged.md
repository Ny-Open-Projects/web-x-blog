# 05-Activiti组任务-查询候选人的组任务

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\05-Activiti组任务-查询候选人的组任务_【海量资源尽在 ubkz.com】.mp4
- 时长 8分41秒（音频 522s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好我们做完了前期的这个准备工作啊保证了我们的这个张商啊应该是保证了我们的这个请填写请假单的这个用户完成了他的任务对吧目前呢我们已经执行到部门经理审核对吧但是部门经理审核的时候他并没有一个真正的这个assign对不对那现在我们作为这个主任务的话作为这个主任务啊那我们就可以让我们的这个候选用户去查找他自己的任务对不对
[00:31] 现在呢我们就一起来看一下啊我们的这个候选候选用户啊怎么去查主任务啊那你比如说我们对应的这个process definition key你可以指令好candidate user作为候选人指令好各位呢然后我们再去用的就是我们的这个task Service用task Service去执行correct task query得到一个查询器啊不太一样的是什么啊
[01:00] 是我们的这个流程定义的key还有一个就是我们的这个task candidate user是我们的这个候选用户的设置而我们原来在写这个代码的时候只是在这个上写的是assign对吧跟原来的代码前面基本是一样的就只有这个上不一样但我们查完之后是一个用户这个主任务对吧主任务这个task有些什么就是这个候选人
[01:28] 它到底有哪些主任务对吧这样我们就可以查出来当我们查询出这个主任务之后啊我们可以把这个主任务的信息便利一下对吧那现在我们也可以一起来做一下这个操作啊那就回到我们的这个group test中我们来搞一下这个代码啊好那现在啊我把这个注意一下啊回到我们这上面来啊这是我们的第三个环节啊那现在我们要做第四个环节
[01:58] 第四个环节主要是查询候选用户查询我们的这个候选用户的主任务查询我们候选用户主任务那这时候我们直接把这些部分都可以都可以重新再搞一下对不对那这次我们要去做这个用户任务的查询我们看一下它在这里头用的是Task Service来解决问题对吧
[02:26] 好那我们要得到的就是我们的这个task Service啊task Service得到我们的task Service对象啊那如何去得到这个task Service的对象呢对吧那我们可以啊这样做等于我们的processengine.get task Service对吧好这样我们就得到了我们的这个task Service啊那第三个就是可以去设置一些参数对吧那有哪些参数啊这个地方主要包括我们的一个是我们的流程
[02:57] 流程定义的key我可以设置还有一个就是我们的候选用户到底是谁候选用户现在我们就可以来做这个工作我们的流程定义的key这一次我们主要用的是还是这个地方叫myprocess下滑线1就是这个这是我们的第一个下滑线1
[03:26] 好了我们除了这个还有一个就是我们的这个候选用户要设置对吧那候选用户其实也是一个自如创对不对比如说我们来一个叫做CondiCondiDag的下滑线U轴子等于这个时候呢你可以再去设置一个值那你咱们一起来看一下开始我们在这个设置我们的这个CondiDag的应该是叫张商对不对
[03:52] 张商是其中候选用户组里头的一个人嘛对吧CountDag的CountDag的CountDag的好然后呢我们这里面真正给的应该是张商这样就相当于我们的候选用户的哪一个用户是张商的任务对不对然后第四个工作我们就可以来执行我们的查询叫执行查询对吧按我们开始所写所讲的这个步骤来执行查询
[04:27] 执行查询呢我们主要是查到它的这个类似的对不对好这时候呢我们就可以啊用这样的方式来做啊执行查询嘛然后用的是我们的这个task Service去调用它的这个credit task query的对象然后呢再去指定我们的process definition key对不对我们直接啊设置为我们的key就可以了啊好下一个工作就是呢
[04:56] 我们可以进一步在这里面再去设置一个就是我们的这个叫做set叫做candidate的叫做candidate的我们在这里头有一个叫做taskcandidate的user对吧那这时候其实我们就可以用这个方法对不对我们来看一下我们就可以用这个方法来指定我们的这个候选人好那我这边呢应该用的是叫做candidate
[05:24] Duck的U字就是它对吧最后我们就可以执行我们的查询那我们执行完这个查询呢就可以得到一个激活对不对好这时候我们就得到一个类似的激活啊它里面就放了有我们的这个若干个任务那后面我们只需要把这个任务中的数据再去输出一下就行了对不对好这时候呢我们啊再来便利一下啊我们便利的是Task任务啊对吧
[05:54] 这样呢我们就是按照刚才给各位介绍的这个步骤在做操作啊查询任务然后呢再去做便利对吧我们到这边呢也是这样的啊输出一下那输出的这个信息将来包括什么啊task.get你可以把我们的这个流程这个任务的所对应的这个流程实例的信息输出一下你也可以输出啊比如说还有哪些信息啊task.
[06:22] 可以把它的ID输出一下对吧这就是任务的编号还有一个还有一个就是你也可以把我们的这个任务名称可不可以输出一下任务名称比如说我就输出这样的一些信息当然你也可以把这个任务我再加一个叫做任务的task.getAssign好那我们一起来观察一下它输出的这个结果现在我们可以看到其中前面都有值
[06:53] 就是我们的这个真正的这个assign没有值那这说明我们的这个用户还真正有没有他的这个执行人啊或者是负责人啊没有因为我们只是设置为主任务对不对这个组里头到底谁去执行是不是并不清楚啊所以说目前这个任务我们目前能够查到有一个任务啊就是说张商目前是有一个任务要做对吧但是呢他现在还不是真正的执行者所以说这个地方呢
[07:23] 为浪说明说明当前的张商当前的张商只是一个候选人吧只是一个候选人并不是任务的执行人说明了这一点意义这样我们呢就给各位把我们的这个作为一个候选人怎么去看他自己有没有任务给各位啊
[07:54] 说清楚了啊那这个地方主要就是叫做设置设置我们的这个候选用户对不对候选用户啊总体上呢各位啊我们就基本上完成了我们的这个啊主任务的一个查询啊我们一起再整洁一下他真正在执行的时候主要就是用到我们的这个task Service对吧用task Service来执行执行的时候呢我们要去真正设置的
[08:22] 与前面的代码唯一不一样的代码就在这叫TaskCandidate的U找设置的是好选用户既然是好选用户所以说我们将在真正的执行的时候查出的这个结果Sign其实唯空因为它并没有真正的执行者

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码调用 Activiti 工作流引擎的 TaskService 来查询和处理用户任务。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Activiti Designer 中的流程图，包含“开始事件”、“用户任务”、“用户任务”、“结束事件”等节点，左侧属性面板显示任务名称为“请假申请任务”，候选用户为“zhangsan,li”。
画面2: 展示一个 PPT 页面，内容为 Java 代码片段，用于演示如何通过 TaskService 查询任务，代码中定义了流程定义 key 为 “holiday4”，候选用户为 “zhangsan”。
画面3: 展示 Java 代码，用于演示如何通过 ProcessEngine 获取 TaskService，然后创建任务查询并完成任务。
画面4: 展示 Java 代码，用于演示如何通过 ProcessEngine 获取 TaskService，然后创建任务查询并完成任务。
画面5: 展示 Java 代码，用于演示如何通过 ProcessEngine 获取 TaskService，然后创建任务查询并完成任务。
画面6: 展示 Activiti Designer 中的流程图，包含“开始事件”、“用户任务”、“用户任务”、“结束事件”等节点。
画面7: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面8: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面9: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面10: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面11: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面12: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面13: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。
画面14: 展示 Java 代码，用于演示如何通过 TaskService 查询任务。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
public void findGroupTaskList() {
    // 流程定义key
    String processDefinitionKey = "holiday4";
    // 任务候选人
    String candidateUser = "zhangsan";
    // 创建TaskService
    TaskService taskService = processEngine.getTaskService();
    // 查询任务
    List<Task> list = taskService.createTaskQuery()
        .processDefinitionKey(processDefinitionKey)
        .taskCandidateUser(candidateUser)//根据候选人查询
        .list();
}
```

画面3:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面4:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面5:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面6:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面7:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面8:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面9:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面10:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("xiaozhang")
        .singleResult();
    //4.处理任务，结合当前用户任务列表的激活操作，任务ID:task.getId()
    if(task != null) {
        taskService.complete(task.getId());
    }
    //5.输出任务的id
    System.out.println(task.getId());
}
```

画面11:
```java
//3.编写请假申请的任务执行方法
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户的任务
    Task task = taskService.createTaskQuery()
        .processDefinitionKey("myProcess_1")
        .taskAssignee("

