# 06-Activiti组任务-拾取组任务的代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\06-Activiti组任务-拾取组任务的代码实现_【海量资源尽在 ubkz.com】.mp4
- 时长 7分55秒（音频 475s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:05] 好下面我们就开始继续来学习我们的这个用户拾取主任务啊我们刚刚已经完成了这个用户查询自己的主任务对吧在我们呢这个张商查询到自己有主任务的时候但是呢张商并不是这个任务的真正的这个assign执行人对吧所以下一步呢我们可以让我们的这个张商变成我们的这个任务的负责人
[00:33] 所以张商就需要去拾取任务那我们张商拾取任务的话按照一个什么样的步骤来走那我们首先一起来看一下这里面用到的是Task ServiceTask ServiceCreate Task QueueTask ID以及我们的Task Conduct User那做这个工作主要是查询当前的用户是否有主任务对不对
[01:01] 如果当前的用户有主任务的话那么他的这个task就不为空那不为空我们就可以来拾取任务那这一行代码就是我们拾取任务最为关键的一个代码啊就是叫做climb那我们呢稍加改造就可以来实现当前的这个用户拾取主任务的过程啊好咱们可以一起来测试一下啊那还是这样的步骤啊copy一下我呢复制一下啊
[01:32] 那让当前的这个用户来拾取我们的主任务啊好这里头主要就是测试啊测试我们的应该我们这里边用的是张商啊测试张商啊这个用户来拾取啊来拾取我们的这个主任务拾取主任务那好我们control v啊扔过来扔过来的话首先呢我们一样是可以去查询作为张商的这个用户
[01:59] 是否有自己的这个主任务要去做对不对好咱们可以啊把下面这个方法重新给他再再注意一下对吧当然我们这边呢没有给各位去使用我们的这个genunit啊目标就是讲activity我就只给各位讲activity啊那现在呢我们就可以回过头来啊我们是myprocess1对吧candidag的user
[02:25] 这样查了我们就可以查询到我们当前的这个具体的任务对吧其实我们在测试之后刚才也看见啊我们真正张商的这个主任务只有一个对不对只有一个主任务所以呢会看到就这个主任务啊对吧就这种人他没有多余的任务啊那我们如果只有一个任务的话为了将来减少我们去便利的情况啊那我们可以在这边做一个工作就是呢直接
[02:54] 用它的这个点叫single result这个方法用它的single result我们也一样可以去查询得到一个任务对不对好比如说我们这个时候就给它起一个名字就叫task就叫task这样我们基本上就完成了我们的这个完成了我们的当前用户的任务的查询这是之前的所有的代码我们基本上没有去做任何的改变对吧
[03:24] 就是把当前张三的这个候选用户他具有的任务先查出来那查出来呢按照我们刚刚给各位讲过的步骤就应该立即做出判断如果不违控拾取主任务对吧做完这个工作就可以了好那我们这个地方啊就可以一起来看一下这个拾取主任务的过程
[03:50] 那这样我就可以在这里面if做出犯状如果我们的task不为空的情况下那这时候我们就可以来拾取我们的主人物对吧那可以使用的是我们的这个叫做task Service去调用它的claim这个方法第一个参数应该是我们当前的这个任务的ID你直接输出就是task.g的ID那这样就可以拿到啊第二个应该是我们的这个candidat
[04:18] Candidat的user对吧好这样呢我们就可以让当前的用户来拾取我们的任务啊当拾取完成后我们就可以直接输出一个比如说啊任务拾取任务拾取完毕是吧任务拾取完毕这样就可以了我们这时候来看一下啊测试的这个效果是什么样的啊好现在各位就可以看到我们的确进入到我们的这个EF了对吧
[04:51] 而且输出了我们的任务拾取完毕对吧那任务拾取完毕的话我们这边将来会有什么样的影响对不对这是我们现在比较关注的那任务拾取完毕我们接着一起来分析一下我们后台的这个库真正会发生什么样的变化我们这个时候再去看我们的这个部门经理作为审核各位这个时候你会发现我们的这个张三
[05:21] 作为他的这个assign对吧原来我们分析的时候部门经理他真正这个任务到底谁去执行呢当时我们这个地方并没有执对不对那现在我们这个部分张商就已经作为我们的这个任务的执行人了他由候选人变成了这个执行者对不对但是虽然他变成了这个执行者但是这个任务执行完了吗对吧没有啊这一点各位要注意啊
[05:49] 也就是说我们刚才做的这个工作只是让我们的张商作为由候选人变成了这个任务的负责人但是这个部门经理审核的工作依然没有完成明白意思吗依然没有完成部门经理审核的工作所以说如果我们下面再要去做工作的话那肯定是希望我们的这个张商作为这个任务的负责人他要去完成这个任务对不对好那刚才呢我们基本上给各位啊
[06:19] 讲了我们的这个任务如果要拾取主要就是这一行代码那拾取的这个关键点呢就会使得我们的这个assign我们的这个county tag的user变成我们的这个assign对吧所以说我们执行拾取也就是说拾取拾取任务拾取任务的过程就是将候选人就是将我们的这个候选用户
[06:48] 候选用户转化为转化为我们的这个真实任务真正啊真正任务的这个负责人这个任务的负责人其实呢说白了一点就是什么呢让任务的assign让我们的任务的这个assignassign有值对不对有值它的主要目标就是这个那基本上啊
[07:17] 我们在这里面就完成了我们想要的这个目标我们目前的这个assign已经有值了对吧具体的步骤就是这一行代码那这一行代码我们也给各位说一下第一个参数是什么第一个参数是我们的这个任务ID对吧任务ID第二个呢第二个参数为我们的第二个参数为候选候选具体的具体的
[07:46] 候选用户对不对候选用户名啊你的候选用户是谁你就写谁对吧就是这个意思啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中，通过 Java 代码实现用户拾取组任务（Claim Task）功能，并展示相关代码逻辑和数据库表数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“4.1.1.3 用户拾取组任务”，并显示代码片段，其中定义了拾取任务的方法 claimTask()，包含任务 ID "6302"、候选人 ID "lisi"，并调用 taskService.claim() 方法。
画面2：展示 IDE 中 GroupTest.java 文件，main 方法中设置流程定义 key 为 "myProcess_1"，候选人用户为 "zhangsan"，并执行查询任务列表。
画面3：展示 PPT 页面“4.1.1.3 用户拾取组任务”，代码片段中展示 taskService.claim(taskId, userId) 的调用逻辑。
画面4：展示 IDE 中 GroupTest.java 文件，main 方法中执行查询任务列表的代码块被高亮。
画面5：展示 IDE 中 GroupTest.java 文件，鼠标悬停在“Run”按钮上，准备执行代码。
画面6：展示 IDE 中 GroupTest.java 文件，main 方法中设置流程定义 key 和候选人用户。
画面7：展示 IDE 中 GroupTest.java 文件，main 方法中设置流程定义 key 为 "myProcess_1"，候选人用户为 "zhangsan"。
画面8：展示 IDE 中 GroupTest.java 文件，main 方法中执行查询任务列表的代码块被高亮，下方终端显示了查询结果。
画面9：展示 IDE 中 GroupTest.java 文件，main 方法中执行查询任务列表的代码块被高亮，下方终端显示了查询结果。
画面10：展示 PPT 页面“4.1.1.3 用户拾取组任务”，代码片段中展示 taskService.claim(taskId, userId) 的调用逻辑，并附有说明文字。
画面11：展示 IDE 中 GroupTest.java 文件，main 方法中执行查询任务列表的代码块被高亮。
画面12：展示 IDE 中 GroupTest.java 文件，main 方法中调用 taskService.claim(task.getId(), candidate_users) 并打印“任务拾取完毕！”。
画面13：展示数据库管理工具，查询 act_hi_actinst 表，显示了流程实例 ID、任务 ID、执行人等信息。
画面14：展示 IDE 中 GroupTest.java 文件，main 方法中调用 taskService.claim(task.getId(), candidate_users) 并打印“任务拾取完毕！”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
@Test
public void claimTask(){
    TaskService taskService = processEngine.getTaskService();
    //要拾取的任务id
    String taskId = "6302";
    //任务候选人id
    String userId = "lisi";
    //拾取任务
    //即使该用户不是候选人也能拾取(建议拾取时校验是否有资格)
    //校验该用户有没有拾取任务的资格
    Task task = taskService.createTaskQuery()//
            .taskId(taskId)
            .taskCandidateUser(userId)//根据候选人查询
            .singleResult();
    if(task!=null){
        taskService.claim(taskId, userId);
        System.out.println("任务拾取成功");
    }
}

画面2：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面3：
@Test
public void claimTask(){
    TaskService taskService = processEngine.getTaskService();
    //要拾取的任务id
    String taskId = "6302";
    //任务候选人id
    String userId = "lisi";
    //拾取任务
    //即使该用户不是候选人也能拾取(建议拾取时校验是否有资格)
    //校验该用户有没有拾取任务的资格
    Task task = taskService.createTaskQuery()//
            .taskId(taskId)
            .taskCandidateUser(userId)//根据候选人查询
            .singleResult();
    if(task!=null){
        taskService.claim(taskId, userId);
        System.out.println("任务拾取成功");
    }
}

画面4：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面5：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面6：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面7：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){
        System.out.println(task.getProcessInstanceId());
        System.out.println(task.getId());
        System.out.println(task.getName());
        System.out.println(task.getAssignee());//null，说明当前的zhangsan只是一个候选人，并不是任务的执行人
    }
}

画面8：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.设置一些参数：流程定义的key，候选用户
    String key = "myProcess_1";
    String candidate_users="zhangsan";
    //4.执行查询
    List<Task> list = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskCandidateUser(candidate_users)//设置候选用户
            .list();
    //5.输出
    for(Task task : list){

