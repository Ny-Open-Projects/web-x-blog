# 07-Activiti组任务-用户任务查询&完成任务

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\07-Activiti组任务-用户任务查询&完成任务_【海量资源尽在 ubkz.com】.mp4
- 时长 5分50秒（音频 350s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 那下面我们继续来学习啊当我们的这个用户由候选用户转换为我们真正的这个用户的assign啊负责人之后那作为这个负责人他可以进一步去查询他自己当前的任务对吧那这个时候我们就开始给各位一起来讲解一下啊我们作为当前的这个用户的候选作为当前的这个用户执行人他可以将自己的任务查询出来对吧
[00:31] 好我们一起来看一下效果啊那我们一起来测试一下那现在我把这个代码啊给他注掉了啊下面呢我们来做我们的第六个步骤做第六个步骤这样做啊那主要是当前啊当前的这个用户查询自己的任务对吧因为他由候选用户已经变成了一个真正的这个任务执行者对吧所以呢他可以啊
[01:00] 来执行来查询自己的任务那在这里面呢我们要做的改造啊其实也比较比较少啊那现在我们可以来看一下啊就是呢原来我们啊这些步骤都是一样的原来我们在做这个操作的时候是用的是候选用户去查对不对但现在呢我们当前的这个用户已经由候选用户变成了真正的任务执行者所以呢我们可以在这里面去设置一个他的这个任务的task assign对吧那这样
[01:29] 就是设置当前用户为真正的我们的任务的执行人就是叫做设置任务的设置任务的负责人对不对那还是写的是我们的注意这个名字也应该要改一下对吧而不是候选用户了而是真正的 assign 对吧所以我们在这里头把变量也给它改一下 assign好现在我就相当于已经设置好了我们的用户的执行人
[01:59] 好我可以copy然后set assign这样我们就执行这样我们就设置好了设置好了将来我们也一样可以去实现我们的相关信息的输出对不对这也是我们设置相关信息输出还可以输出这样的一些内容这是完全没有问题的我们现在直接就可以来测试一下来测试一下当前的用户查询自己的任务对吧
[02:28] 好我们再走一把看一下效果各位这个时候我们就可以看到当前的用户对吧作为部门经理现在他的这个assign就有值了你看看我们上次在测试这个assign的时候是不是他是违空那是因为当前的张商只是一个好选人他并不是真正的知情人对吧我们这里面现在再去测试的话因为当前的张商已经拾取了这个任务所以呢
[03:00] 他就变成了负责人对吧张商既然作为负责人所以他的这个任务的assign执行者那肯定就是我们的张商对不对当我们的张商当我们的张商啊查到自己有任务之后下一步其实张商可以接着做一个工作那是什么呢那就是我们张商可以啊进一步来进一步来完成自己的任务对不对这就是我们啊也是之前其实已经给大家差不多是讲过的啊
[03:29] 那下面我们继续来做这个工作那就是当前用户完成自己的任务啊当前用户完成自己的任务那当前用户怎么样来完成自己的任务呢对吧而且刚才我们在查的时候可以发现张商目前的任务只有一个所以呢我在这里边想呢做一个改造那就是啥呢
[03:51] 那我们的这个地方直接写成踏实了如果要是直接是踏实的话那我们这个部分也要改一下对不对叫做点那就点single result对吧这样我们就可以做到查询出我们的当前用户的任务那当前用户如果有自己的任务那我们这个上也不再是输出应该就是叫做执行执行当前的任务就可以了对吧执行当前的任务啊那
[04:19] 判断一下,如果我们的这个task不等于空的情况下那这个时候我们就可以直接让我们的任务来完成这时候我们可以用task Service.complete的这个方法哪个任务呢?
[04:35] 我们把task.getID放进来这样我们就可以完成当前的这个当前的这个用户完成他自己的任务对吧那我们比如说我们在这要写上
[04:47] 任务执行完毕对吧任务执行完毕好那我们也一起来看一下这个效果来走运行一下好我们看一下观察一下它运行的情况这时候各位就可以看到我们的任务就已经被执行完毕了对吧任务如果一旦被执行完毕了那我们就可以接着来看我们的这个数据库部分好我们刷一下它刷一下它
[05:15] 这时候各位就可以看到我们已经进入到总经理审核的环节对吧而我们的总经理是小王对不对但是这个任务并没有执行完成对吧那基本上我们已经跑完了当前的这个张商完成自己的一个主任务对不对张商完成了一个主任务那基本上我们完成了这个当前用户任务的查询以及
[05:42] 当前用户过人任务的一个伴侣对吧这是我们基本上完成的效果就是这样的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Java代码中通过TaskService查询并操作流程任务，包括创建查询、获取任务、领取任务、完成任务等操作，并通过数据库查看任务状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 代码：`//5.让zhangsan用户，充当任务的负责人（让任务的assignee值）`
- 代码：`public static void main(String[] args) {`
- 代码：`//1.得到ProcessEngine对象`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`//2.得到TaskService对象`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`//3.设置一些参数，流程定义的key，候选人`
- 代码：`String key = "myProcess_1";`
- 代码：`String candidate_users = "zhangsan";`
- 代码：`//4.执行查询`
- 代码：`Task task = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskCandidateUser(candidate_users); //设置候选人`
- 代码：`.singleResult();`
- 代码：`if(task!=null){`
- 代码：`taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选人用户名`
- 代码：`System.out.println("任务领取完毕!");`
- 代码：`}`

画面2：
- 代码：`//4.执行查询`
- 代码：`Task task = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskCandidateUser(candidate_users); //设置候选人`
- 代码：`.singleResult();`
- 代码：`if(task!=null){`
- 代码：`taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选人用户名`
- 代码：`System.out.println("任务领取完毕!");`
- 代码：`}`

画面3：
- 代码：`//4.执行查询`
- 代码：`Task task = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskCandidateUser(candidate_users); //设置候选人`
- 代码：`.singleResult();`
- 代码：`if(task!=null){`
- 代码：`taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选人用户名`
- 代码：`System.out.println("任务领取完毕!");`
- 代码：`}`

画面4：
- 代码：`//4.执行查询`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskCandidateUser(candidate_users); //设置候选人`
- 代码：`.list();`
- 代码：`//5.输出`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //为null，说明当前的zhangsan只是一个候选人，并不是任务的执行人`
- 代码：`}`

画面5：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面6：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面7：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面8：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面9：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`
- 代码：`System.out.println(task.getProcessInstanceId());`
- 代码：`System.out.println(task.getId());`
- 代码：`System.out.println(task.getName());`
- 代码：`System.out.println(task.getAssignee()); //任务的执行人`
- 代码：`}`

画面10：
- 代码：`//6.当前的用户查询自己的任务`
- 代码：`public static void main(String[] args) {`
- 代码：`ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();`
- 代码：`TaskService taskService = processEngine.getTaskService();`
- 代码：`String key = "myProcess_1";`
- 代码：`String assignee = "zhangsan";`
- 代码：`List<Task> list = taskService.createTaskQuery()`
- 代码：`.processDefinitionKey(key)`
- 代码：`.taskAssignee(assignee) //设置任务的负责人`
- 代码：`.list();`
- 代码：`for(Task task : list){`

