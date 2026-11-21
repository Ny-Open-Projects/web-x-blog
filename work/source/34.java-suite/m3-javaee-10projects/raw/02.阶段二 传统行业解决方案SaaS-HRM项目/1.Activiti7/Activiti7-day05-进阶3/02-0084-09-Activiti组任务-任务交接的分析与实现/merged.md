# 09-Activiti组任务-任务交接的分析与实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\09-Activiti组任务-任务交接的分析与实现_【海量资源尽在 ubkz.com】.mp4
- 时长 7分53秒（音频 473s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:04] 好刚才呢我们对于这个用户的主任务的归还我们没有去测试那主要是原因主要原因是因为它特别简单主要是设置一个run就可以了那我们现在呢再来给各位介绍一下我们的这个任务交接因为任务交接和我们主任务的归还在这一点上是很像的知道吧我给各位演示一个各位一起来看一下那任务交接首先我们一起看它是要做什么工作
[00:33] 任务的负责人将任务交给其他的候选人来办理这个任务我们就叫做任务交接就相当于现在我是这个任务的负责人我呢说我不干了然后找一个人对吧他来替代我这就叫交接就是这个意思啊那我们现在呢大致上可以一起来看一下如果我们要去做这个任务交接的话应该怎么去做啊那
[01:02] 做任务交接呢我们也是一样的先呢要去看一下真正的这个用户的执行人把他的任务查出来对不对如果说他查出来这个任务之后不为空啊就不为空那我们这个时候就可以把这个用户交给我们的候选人对不对让候选人去完成这个工作那各位思考一下啊我们做这个工作最终影响的是什么呢各位啊真正的本质我可以告诉各位啊
[01:32] 真正的本质就是我们早期的这个原来部门经理执行任务他的这个执行人assign是张商但是我们这一次我们把这个任务的这个交接工作一旦做完那部门经理审核的这个任务将来就不再是张商对不对也说assign的取职不是张商而应该变成我们另外一个候选人比如说设置为理事那就是我们理事是我们的这个这个任务的执行人了是这个意思
[02:02] 所以说我们这一次做这个工作真正本质上就是要去改变我们的这个assign的取值对吧好那我们同样的回到这个地方来再去实现一把那现在我们第八个如果要去做这个任务交接任务交接如果要做这个工作前提是什么呢前提要保证要保证当前用户
[02:31] 当前用户是这个任务的执行人对不对是这个任务的负责人这时候他这时候他才可以有权限对吧有权限去将去将任务将我们的任务交接给其他候选人对不对交接给我们的其他
[03:01] 叫其他我们的候选其他候选人对吧这个是我们要完成的工作那如果我要完成这个工作呢我们可以基本上诚心再次做一个先做一个查询对不对好那这个就是用户查自己的任务对吧那我可以省一点事就直接把这个地方的copy拿过来再次放到我们的上面来我们来看一下
[03:29] 那这个就是当让我们的这个张商来查询自己的任务对不对那查任务的时候但是啊这个人是有些变化啊这个人应该用的是task对不对用我们的这个task注意啊这个人应该选他啊这是我们的task好没说叫做task那查如果说只是查一个任务的话那我们这个人就不能够用我们的这个类似的方法对吧那应该考虑我们的single result对吧那
[03:57] 查到我们的这个任务single result查到这个任务下一步我们可以做什么呢对吧那下一步我们就可以做出判断对不对判断是否是否有这个任务比如说我们的这个执行人是否有这个任务如果我们的执行人有这个任务那他就不等于空所以说我们就可以直接按我们刚才给各位介绍过的这个具体的步骤对不对就可以来分配这个任务的执行人就可以了
[04:27] 好那我们直接就是用task servicetask Service点再去调用我们的set assign的这个方法第一个参数写我们task.gay的ID对吧而第二个参数就应该写的是我们的这个候选人对吧我们这一次这个候选人其实就是李氏对不对那这样我们基本上就可以完成说把这个任务交给李氏来做这个地方就是交接交接任务
[04:57] 交接交接我们的任务为理事对吧为我们的理事这样理事就成为成为了这个任务的负责人注意这个地方的隐含有一层意思交接任务交接任务就是一个候选候选人拾取用户的过程拾取用户的过程的过程
[05:25] 因为我们之前做这个候选人拾取用户的时候真正改变的也是我们的这个assign的取值对不对你像我们张商拾取任务这个assign的值就是由空变成了张商对不对那我们做交接的话不就是由张商早期的这个用户应该要变成李四对吧那这个过程其实就是拾取用户的过程所以说我们当我们做完这个工作一样的我们也可以啊来一个啊叫sout来一个我们看看啊
[05:55] 就是叫做交接交接任务完成我们可以看一下这个效果好看起来是保存一下那现在我们可以一起再去执行看一下效果看是否达到了我们预期的这个目标各位可以看到这边就出了一个交接任务完成那我们再回到我们的库中来看一下对吧我们只需要刷一下它应该这个时候就会由张商变成李氏的这个 assign对吧好各位可以看到
[06:25] 我们目前就可以做到我们的任务就已经交接给理事了对不对按照道理的话理事可以继续来完成他自己的任务对不对如果说我们的理事要去进一步完成他的任务的话那我们早期应该已经做过这个当前用户完成任务啊所以说我们只需要把这样的代码重新放开对不对放开之后我们的这个理事就可以来完成自己的任务了那我们应该把这个张商改成理事
[06:55] 李氏就可以完成自己任务了好这时候我们再去测试一下基本上我们可以看到这个效果就应该是李氏可以完成自己的任务了那李氏如果完成自己的任务我们来刷一下数据库走走好这时候我们的这个部门经理李氏是否完成了自己的任务呢各位可以看到他的end time就有值了对吧并且我们的这个任务已经执行到总经理来进行审核的这个节点了对吧
[07:25] 但是他目前没有做这个任务啊这样我们基本上给各位演示了一把我们的任务交接如何去做做任务交接各位会看到和我们任务的归还其实真正都是调用同一个方法只是在这里面设置的这个值不一样而已对不对一个是设置为long一个是设置为我们的这个候选用户就是这一点不一样那好这个交接用户就给各位啊说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中任务交接（Task Assignment）的 Java 代码实现与操作流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 页面“4.1.1.7 任务交接”，包含代码示例 `@Test public void setAssigneeToCandidateUser() { // 查询任务使用TaskService }` 和 `TaskService taskService = processEngine.getTaskService();`。
画面 2: 展示 PPT 页面“4.1.1.7 任务交接”，包含代码示例 `Task task = taskService.createTaskQuery().taskId(taskId).taskAssignee(userId).singleResult(); if (task != null) { // 如果设置为null，归还任务，该 任务没有负责人 taskService.setAssignee(taskId, null); }` 和说明文字。
画面 3: 展示 PPT 页面“4.1.1.7 任务交接”，包含代码示例 `TaskService taskService = processEngine.getTaskService(); // 当前待办任务 String taskId = "6004"; // 任务负责人 String userId = "zhangsan"; // 将此任务交给其它候选人办理 任务 String candidateuser = "zhangsan";`。
画面 4: 展示 IDE 中的 `GroupTest.java` 文件，代码为 `//7.当前用户完成自己的任务 public static void main(String[] args) { //1.得到ProcessEngine对象 ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); //2.得到TaskService对象 TaskService taskService = processEngine.getTaskService(); //3.设置一些参数，流程定义的key,用户 String key = "myProcess_1"; String assignee = "zhangsan"; //4.执行查询 Task task = taskService.createTaskQuery() .processDefinitionKey(key) .taskAssignee(assignee) //设置任务的负责人 .singleResult(); //5.执行当前任务 if(task!=null){ taskService.complete(task.getTaskId()); System.out.println("任务执行完毕!"); } }`。
画面 5: 展示 IDE 中的 `GroupTest.java` 文件，代码为 `//7.当前用户完成自己的任务 public static void main(String[] args) { //1.得到ProcessEngine对象 ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); //2.得到TaskService对象 TaskService taskService = processEngine.getTaskService(); //3.设置一些参数，流程定义的key,用户 String key = "myProcess_1"; String assignee = "zhangsan"; //4.执行查询 Task task = taskService.createTaskQuery() .processDefinitionKey(key) .taskAssignee(assignee) //设置任务的负责人 .singleResult(); //5.执行当前任务 if(task!=null){ taskService.complete(task.getTaskId()); System.out.println("任务执行完毕!"); } }`。
画面 6: 展示 IDE 中的 `GroupTest.java` 文件，代码为 `//7.当前用户完成自己的任务 public static void main(String[] args) { //1.得到ProcessEngine对象 ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); //2.得到TaskService对象 TaskService taskService = processEngine.getTaskService(); //3.设置一些参数，流程定义的key,用户 String key = "myProcess_1"; String assignee = "zhangsan"; //4.执行查询 Task task = taskService.createTaskQuery() .processDefinitionKey(key) .taskAssignee(assignee) //设置任务的负责人 .singleResult(); //5.执行当前任务 if(task!=null){ taskService.complete(task.getTaskId()); System.out.println("任务执行完毕!"); } }`。
画面 7: 展示 IDE 中的 `GroupTest.java` 文件，代码为 `//7.当前用户完成自己的任务 public static void main(String[] args) { //1.得到ProcessEngine对象 ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); //2.得到TaskService对象 TaskService taskService = processEngine.getTaskService(); //3.设置一些参数，流程定义的key,用户 String key = "myProcess_1"; String assignee = "zhangsan"; //4.执行查询 Task task = taskService.createTaskQuery() .processDefinitionKey(key) .taskAssignee(assignee) //设置任务的负责人 .singleResult(); //5.执行当前任务 if(task!=null){ taskService.complete(task.getTaskId()); System.out.println("任务执行完毕!"); } }`。
画面 8: 展示 PPT 页面“4.1.1.7 任务交接”，包含代码示例 `TaskService taskService = processEngine.getTaskService(); // 当前待办任务 String taskId = "6004"; // 任务负责人 String userId = "zhangsan2"; // 将此任务交给其它候选人办理 任务 String candidateuser = "zhangsan"; // 校验userId是否是taskId的负责人，如果是负责人才可以归还任务 Task task = taskService.createTaskQuery().taskId(taskId) .taskAssignee(userId).singleResult(); if (task != null) { taskService.setAssignee(taskId, candidateuser); }`。
画面 9: 展示 IDE 中的 `GroupTest.java` 文件，代码为 `//7.当前用户完成自己的任务 public static void main(String[] args) { //1.得到ProcessEngine对象 ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); //2.得到TaskService对象 TaskService taskService = processEngine.getTaskService(); //3.设置一些参数，流程定义的key,用户 String key = "myProcess_1"; String assignee = "zhangsan"; //4.执行查询 Task task = taskService.createTaskQuery() .processDefinitionKey(key) .taskAssignee(assignee) //设置任务的负责人 .singleResult(); //5.执行当前任务 if(task!=null){ taskService.complete(task.getTaskId()); System.out.println("任务执行完毕!"); } }`。
画面 10: 展示 IDE 中的 `GroupTest.java` 文件，代码为 `//7.当前用户完成自己的任务 public static void main(String[] args) { //1.得到ProcessEngine对象 ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); //2.得到TaskService对象 TaskService taskService = processEngine.getTaskService(); //3.设置一些参数，流程定义的key,用户 String key = "myProcess_1"; String assignee = "zhangsan"; //4.执行查询 Task task = taskService.createTaskQuery() .processDefinitionKey(key) .taskAssignee(assignee) //设置任务的负责人 .singleResult(); //5.执行当前任务 if(task!=null){ taskService.complete(task.getTaskId()); System.out.println("任务执行完毕!"); } }`。
画面 11: 展示 IDE 中的 `GroupTest.java` 文件，代码为 `//7.当前用户完成自己的任务 public static void main(String[] args) { //1.得到ProcessEngine对象 ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); //2.得到TaskService对象 TaskService taskService = processEngine.getTaskService(); //3.设置一些参数，流程定义的key,用户 String key = "myProcess_1"; String assignee = "zhangsan"; //4.执行查询 Task task = taskService.createTaskQuery() .processDefinitionKey(key) .taskAssignee(assignee) //设置任务的负责人 .singleResult(); //5.执行当前任务 if(task!=null){ taskService.complete(task.getTaskId()); System.out.println("任务执行完毕!"); } }`。
画面 12: 展示 IDE 中的 `GroupTest.java` 文件，代码为 `//7.当前用户完成自己的任务 public static void main(String[] args) { //1.得到ProcessEngine对象 ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); //2.得到TaskService对象 TaskService taskService = processEngine.getTaskService(); //3.设置一些参数，流程定义的key,用户 String key = "myProcess_1"; String assignee = "lisi"; //4.执行查询 Task task = taskService.createTaskQuery() .processDefinitionKey(key) .taskAssignee(assignee) //设置任务的负责人 .singleResult(); //5.执行当前任务 if(task!=null){ taskService.complete(task.getTaskId()); System.out.println("任务执行完毕!"); } }`。
画面 13: 展示 PPT 页面“4.1.1.8 数据库表操作”，包含代码示例 `TaskService taskService = processEngine.getTaskService(); // 当前待办任务 String taskId = "6004"; // 任务负责人 String userId = "zhangsan2"; // 将此任务交给其它候选人办理 任务 String candidateuser = "zhangsan"; // 校验userId是否是taskId的负责人，如果是负责人才可以归还任务 Task task = taskService.createTaskQuery().taskId(taskId) .taskAssignee(userId).singleResult(); if (task != null) { taskService.setAssignee(taskId, candidateuser); }`。
画面 14: 展示 PPT 页面“4.1.1.8 数据库表操作”，包含代码示例 `TaskService taskService = processEngine.getTaskService(); // 当前待办任务 String taskId = "6004"; // 任务负责人 String userId = "zhangsan2"; // 将此任务交给其它候选人办理 任务 String

