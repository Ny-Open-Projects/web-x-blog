# 04-Activiti组任务-前期测试准备工作

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\04-Activiti组任务-前期测试准备工作_【海量资源尽在 ubkz.com】.mp4
- 时长 11分32秒（音频 692s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:05] 好那我们把刚才的这个主任务办理的流程说清楚了啊那下面呢我们就可以啊那我们刚刚呢在这里面所写的这个主任务对不对Conduct Users然后呢我们现在就可以来测试一下这个部署啊以及呢我们的这个流程实例先启动起来我们先把这样的准备工作给他做完啊那现在我们可以这样做啊到这边呢我们去做一个我们的这个主任务的测试啊
[00:34] 那在做这个测试的时候我们先可以这样啊到这边呢比如说我这里头就有一个这样的类啊但是它里头什么也没写啊那现在我们来做第一个工作啊就是我们的这个主任务啊主任务的这个测试啊测试好那具体我们怎么样来做啊第一个过程呢我们还是可以啊先到这里边呢将我们的这个流程部署上可以吧那就是啊第一步然后我们来实现我们的这个
[01:04] 部署我们的这个流程定义啊那具体到底怎么样来部署这个流程定义那这个代码我都不想去打了啊那我们因为敲的次数比较多啊那现在呢我打算呢直接从这边呢把我们的这个流程部署的代码复制过来可以吧看小微能的再来啊这样呢我们基本上就可以去做我们的这个流程的部署了啊好各位啊现在我们可以一起来看一下啊
[01:33] 我们的这个流程部署呢在这里面主要改的就是这个部分对吧这一次我们真正部署的是我们的这个holiday5对不对那我这个时候直接可以把这个改成我们的这个holiday5注意啊那这一次我们做这个BPMN文件没有与之对应的这个PNG文件啊注意PNG文件它其实不是必须的明白是吧如果说将来我们在
[02:01] 整个这个工作流运行的过程中我们不不不想看到PNG图片对吧那其实你是可以不加的啊但是一般情况下我们都要加上它那这个地方我做一个省做一个这个省市的步骤可以吧我这个PNG文件我没有自己去制作啊那我们现在呢其实相当于这就是把这个代码注掉了所以PNG文件没加这一点呢跟我们测试过程是没有关系的啊
[02:31] 好那我们这个直接就这样做完了下面呢我就可以直接来看一下啊好跑一下效果我们走一下这时候各位应该就可以看到我们的这个流程啊被部署上了啊我们看一下啊我们的这个请假流程就部署好了那部署好因为我们这里边缺一个这样的文件啊所以呢如果咱们同学再去找我们的找我们的这个数据库来看的话在我们的这个数据库表中呢
[03:00] 叫做byte rate这张表中你可以看到应该会少一条记录对吧它只有我们的这个BPMN文件PNG文件你没有部署进来所以说它这里面就不会存储但是不存储不会影响我们整个工作流的执行过程不会影响工作流执行过程那好当我们把这个流程定义这个部署工作给它做完了那下一步
[03:29] 其实我们就可以来启动我们的这个流程实例对吧好如何来启动我们的流程实例那这个地方呢我也做一个偷懒可以吧因为类似的代码我们写了很多遍了啊那我们启动这个流程实例我在这里边直接啊用我对应的这个方法来做这个工作了啊那好现在我再次回到我们的这个group test那现在呢比如说我就直接到这里头啊再去给各位搞出一个这样的方法
[03:57] 那它的主要作用就是来完成我们这是我们第二个步骤啊就是叫做我们的流程啊流流程实力的启动对吧叫启动流程实力那启动我们的流程实力啊好那我这次启动的这个流程实力的这个key到底应该写什么呢那这个部分应该看你的这个horror里头horror里面指定的这个key是不是我们的这个horror里指定的这个key没有改啊它就是叫my process
[04:27] 下滑线1对吧那我这一次在这里头做这个测试的时候就也应该用这个名字对吧这个地方是当时我没有去改啊那这样我们就完成了我们的这个流程的这个整个的这个流程实例啊当我流程实例做完之后我们就可以拿到我们的这个流程定义流程实例的ID是肯定会拿到的对吧
[04:51] 好下面我们就可以来输出这样的一些信息看一下我们实例启动的效果可以吧对啊实例启动我们用的是run time Service对吧然后调start process use by key对吧就可以启动我们的流程实例啊好那我们可以来看一下效果啊啊这个里边注意一下啊同学们注意一下这个里边呢因为我在这里头啊加的时候这个慢方法好像是多考了一份对吧
[05:22] 去掉就可以了好下面我们可以重新来看一下它的运行的效果来跑一下好现在各位可以看到我们的实例就启动了对吧我们的实例启动了我们要关注的是我们的候选人是否也添加到我们的activity所对应的表中去了我们可以来看一下这里面目前没有我们的实例因为还没有起对吧还没有起我们的实例现在
[06:01] 实力起来但是我们的用户还没有去执行自己的任务对吧那我们可以观察看我们的这个instance对吧start event填写请假单我们这里说的是小张对吧小张来填写我们的这个请假单那这个是没问题的但是小张并没有完成他自己的这个任务对吧所以呢我们相当于真正这个节点在走的时候这个任务还没有完成对吧而这个任务跟我们的这个
[06:30] 今天要讲的这个候选用户是没有关系的这个任务是我们自己本身在这里面设置的任务对吧那下一个工作如果我们要去做测试的话就应该是让我们的真正的这个用户去完成自己的任务就可以了吧好各位我把这个部分再给各位注意一下那现在我们开始来做第三个环节第三个环节做什么呢就是这个地方就
[07:00] 就是让指定的这个用户来完成我们的任务那就是叫做填写请假单填写请假单的任务要执行完成对不对那现在我们就会进一步来把这个代码给他也直接从我们早期所写过的代码中拿过来用吧那如果要去完成一个任务的话我们可以直接是叫做completed
[07:29] task对不对completed task好我们来看一下我们来看一下这里边就是先去查询用户的任务对吧如果不为空我们可以让他这个任务执行对不对好我们可以直接copy一下复制那直接放到我们的这个group test放到这个部分来看小微等到这那现在我们一起来看一下首先是看有没有任务
[07:59] 那我们的这个process definition key应该不叫holo第二对不对因为我们刚才给各位说了啊我们没有改名就直接是叫做my process1对吧那回到这边来应该还是这个名称啊然后呢这个task assign这个真正的这个assign分配者是谁啊这个分配者是谁各位啊呃我们可以到这边直接可以看到应该是叫做小张啊小张当然了
[08:27] 如果咱们同学要去看的话你也可以回到我们的桌面在这个部分你也是可以看到的这个assign是小张然后是我们的候选用户最后一个任务是我们的这个叫小王对不对那再回到我们的这个代码中来我们来看一下那这个地方就应该改名字了应该改成叫小张来执行我们的这个任务的查询
[08:54] 那他查到如果if我就可以判断一下啊叫做if如果我们的这个task不等于none就说明我们的用户查到自己有任务对不对如果查到有任务contra xnone到里头来那这个时候我们就说用户任务执行完毕啊好比如说这个地方就写上啊叫做啊用户任务执行完毕啊执行完毕那这样呢
[09:22] 他的任务就做完了然后我们现在也可以进一步来测试他对不对来让我们的用户执行完自己的任务好我们运行看一下效果那这时候用户就完成了自己的任务对不对那完成任务对于我们而言其实就相当于填写请假单的任务完成了所以这时候再走就已经走到了我们的部门经理的环节对吧
[09:49] 那我们的部门经理环节在操作的时候我们一起来看一下啊我们的这个Arch的Instance啊那这时候各位可以看到Arch的Instance我们呢这边的这个这是我们的这个部门经理而我们的部门经理审核的时候各位可以发现我们的这个Assign里面并没有真正的这个Assign能看到吗并没有真正的这个Assign因为你想一想现在
[10:17] 我们真正的这个任务执行人你能百分之百确定吗对不对他真正在走的时候他可能是我们的候选用户的张商也可能是李氏对不对所以呢他并不能够百分之百确定这个任务到底是谁来干啊所以我们这个时候现在呢要做的工作是我们开始在各位给各位讲的对吧我们呢应该要让候选人去拾取自己的任务
[10:46] 如果候选人不去拾取自己的任务那我们相当于将来后续的工作就没有办法开展了对吧这样呢我们啊给各位讲到这基本上我们把我们刚才呢整个后续要去做候选用户的查询的一些前提啊或者一些准备工作我们基本上就做到位了对吧后面呢我们要再去做工作的话就是做我们的这个
[11:14] 候选用户或者说任务组用户查询组任务对吧或者再去拾取组任务对不对大致就是啊做了一个前期的一些准备工作啊这样我们长时间啊把这个准备工作就到这到这结束啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Activiti 工作流引擎部署流程、启动流程实例、查询和完成任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，讲解用户查询组任务的四个步骤：查询任务、拾取任务、查询个人任务、办理个人任务。
画面2：IDE中显示项目结构，包含resources目录下的多个BPMN文件和activiti.cfg.xml配置文件。
画面3：代码中部署流程，使用repositoryService.createDeployment()添加资源并部署。
画面4：部署流程并输出部署名称和ID。
画面5：部署流程并输出部署名称和ID。
画面6：代码中启动流程实例，使用runtimeService.startProcessInstanceByKey()。
画面7：代码中启动流程实例，使用runtimeService.startProcessInstanceByKey()。
画面8：SQLyog中执行SQL语句，删除数据库activiti并创建新数据库activiti。
画面9：IDE中显示启动流程实例的代码和终端输出。
画面10：代码中查询并完成任务，使用taskService.createTaskQuery().taskAssignee("zhangsan").singleResult()。
画面11：展示流程图，包含“开始”、“请假申请”、“提交审批”、“结束”节点。
画面12：代码中查询并完成任务，使用taskService.createTaskQuery().taskAssignee("zhangsan").singleResult()。
画面13：代码中查询并完成任务，使用taskService.createTaskQuery().taskAssignee("zhangsan").singleResult()，并添加if判断。
画面14：展示课程PPT内容，讲解用户查询组任务，代码示例为查询任务列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.进行部署
Deployment deployment = repositoryService.createDeployment()
		.addClasspathResource("diagram/holiday2.bpmn") //添加BPMN资源
		.name("请假申请流程")
		.deploy();
//4.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```

画面4：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.进行部署
Deployment deployment = repositoryService.createDeployment()
		.addClasspathResource("diagram/holiday2.bpmn") //添加BPMN资源
		.name("请假申请流程")
		.deploy();
//4.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```

画面6：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RuntimeService实例
RuntimeService runtimeService = processEngine.getRuntimeService();
//3.创建流程实例（流程定义的key需要知道 holiday）
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess");
//4.输出一些相关信息
System.out.println("流程定义ID:"+processInstance.getDeploymentId());//null
System.out.println("流程实例ID:"+processInstance.getId());//2901
System.out.println("活动ID:"+processInstance.getActivityId());//null
```

画面7：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RuntimeService实例
RuntimeService runtimeService = processEngine.getRuntimeService();
//3.创建流程实例（流程定义的key需要知道 holiday）
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess_1");
//4.输出一些相关信息
System.out.println("流程定义ID:"+processInstance.getDeploymentId());//null
System.out.println("流程实例ID:"+processInstance.getId());//2901
System.out.println("活动ID:"+processInstance.getActivityId());//null
```

画面9：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RuntimeService实例
RuntimeService runtimeService = processEngine.getRuntimeService();
//3.创建流程实例（流程定义的key需要知道 holiday）
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess_1");
//4.输出一些相关信息
System.out.println("流程定义ID:"+processInstance.getDeploymentId());//null
System.out.println("流程实例ID:"+processInstance.getId());//2901
System.out.println("活动ID:"+processInstance.getActivityId());//null
```

画面10：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService实例
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
		.processDefinitionKey("holiday4")
		.taskAssignee("zhangsan")
		.singleResult();
//4.处理任务，结合当前用户任务对象的属性操作，任务ID:task.getId()
taskService.complete(task.getId());
//5.输出任务的id
System.out.println(task.getId());
```

画面12：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService实例
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
		.processDefinitionKey("myProcess_1")
		.taskAssignee("zhangsan")
		.singleResult();
//4.处理任务，结合当前用户任务对象的属性操作，任务ID:task.getId()
taskService.complete(task.getId());
//5.输出任务的id
System.out.println(task.getId());
```

画面13：
```java
//1.创建ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService实例
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户的任务
Task task = taskService.createTaskQuery()
		.processDefinitionKey("myProcess_1")
		.taskAssignee("zhangsan")
		.singleResult();
//4.处理任务，结合当前用户任务对象的属性操作，任务ID:task.getId()
if(task!=null){
	taskService.complete(task.getId());
	System.out.println("用户任务执行完毕...");
}
```

画面14：
```java
@Test
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

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.1.1.2 用户查询组任务”，内容为“根据候选人查询组任务”。
画面11：流程图包含“开始”指向“请假申请”，“请假申请”指向“提交审批”，“提交审批”指向“结束”。
画面14：PPT标题为“4.1.1.2 用户查询组任务”，内容为“根据候选人查询组任务”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

