# 08-Activiti组任务-当前用户归还组任务

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\08-Activiti组任务-当前用户归还组任务_【海量资源尽在 ubkz.com】.mp4
- 时长 8分56秒（音频 536s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好,下面我们一起来学习一下我们的这个归还组任务刚才呢我们已经啊让当前的这个候选人啊执行完了这个自己的任务对吧那当他执行完我们的任务之后啊那我们的这个整个流程基本上就已经跑完了对吧那现在呢已经到达这个整经历啊那我们如果说要去恢复出我们当前的这个当前的这个用户正在走我们的部门经历
[00:32] 部门经理审核的这个环节的话那我们就需要呢让我们的部门经理啊这个这个节点呢重新拿到我们的当前的用户当前这个让我们的部门经理重新啊把任务由候选用户啊变成我们的任务执行人对吧所以说我们的这个前期的这些流程已经走完了啊那为了能够保证我们的这个现场重新再被还原啊比如说我可以这样做啊
[01:01] 比如说drop database我们把activity直接清掉清完然后我们再去做一个数据库的创建这样我们基本上就可以再次来还原我们早期的现场比如说我这个时候再去创建出我们的activity这样的一个数据库创建出来下面我们再回到这边就是要归还主任对吧
[01:30] 归还主任务那我们必须保证我们当前的这个用户已经成为了当前这个任务的这个负责人对吧但是他现在不想成为这个负责人对不对于是他想把这个任务归还给主里头的其归还到这个主里面那将来其他谁愿意去省那可以重新再去拾取任务对吧大致就是一个这样的失落那我们如果要去测试这个效果的话各位啊
[01:57] 那我们就应该把刚才我们所执行的这个group test里头的一些方法呢需要重新还原回来让它呢可以重新再去执行各位啊这一点呢我们主要就是测试啊在这个代码上呢并没有太多的难度啊我们可以一起来重新恢复一下我们早期的这个现场过程啊那第一个我们要做的就是呢要保证我们的这个流程可以被部署对吧所以说我们
[02:26] 应该把这样的代码重新再去执行一遍对不对这样我们就可以让我们的这个Holiday5对应的这个流程重新呢部署到我们的这个库里面去现在就已经部署进去了对吧这是我们的流程定义就已经重新发布到我们的数据库了好下一个我们要做的就是当我们的流程定义做好那目前我们就可以去启动我们的流程实例对吧
[02:52] 而启动流程实例就是这样的代码我们重新再去执行一下啊这样我们就可以来启动我们的这个流程实例啊那启动流程实例我们对应的这个hihi对应的这个表啊act instance这个表呢就会有填写请加单但是目前呢这个小张并没有完成我们的任务所以他的end time应该是没有时间的啊那我们可以继续做工作对不对
[03:21] 就是让我们的这个小张来完成他的任务对吧所以整个过程啊并不难啊我们只是恢复现场对吧好比如说现在我就可以让我们的小张小张来完成他自己的任务啊好这样我们小张就可以直接去完成自己的任务对不对好来看一下效果啊来看一下效果这边呢就有小张complete的完成自己的任务过一会看到小张目前就完成了他的任务对吧那小张的任务完成了
[03:52] 那自然就会进入到下一个节点就是我们的这个部门经理审核的环节所以我们可以再次刷就进入到部门经理审核部门经理审核呢我们当时只是设置了两个候选用户对吧这个候选用户并不是真正任务执行者所以说目前我们的Assign没有值那我们可以接着来做下一步工作那就是让我们的这个候选用户变成我们的这个真正的这个
[04:21] 真正的这个啊呃任务执行人那这个地方主要就是我们要去做一步这样的工作啊我们可以重新再来看一下效果对吧这个地方我们的这个task啊我们的这个task呃呃不能够导入我们的这个task啊应该是我们没有针对我们的这个task导包吧对吧我们可以把task导入进来啊还是activity里头的task啊这样就可以了对吧
[04:51] 然后下面我们就可以重新来执行一下啊这次执行呢一样的我们主要是那这是查询啊查询我们的这个候选用户对不对他没有成为真正的这个assign所以唯空对吧这一步工作其实主要是做查询的啊对于我们对于我们去拾取任务而言呢意义不大对吧所以我们第五个工作啊就第四个工作到这啊下面我们就来做第五个工作
[05:21] 这个工作主要的任务就是呢让我们当前的这个让我们当前的这个用户啊由候选用户转换成我们的这个转换成我们的真正的任务执行人对吧好我们可以看一下啊这时候好基本上啊那做到这一步我们的这个场景啊就已经恢复完了啊恢复完的主要目标呢就是我们对应的候选用户
[05:48] 一旦拾取用户拾取任务之后他就会变成这个任务的执行人所以呢我们再次刷新各位就可以看到我们的部门经理现在就已经变成张商来执行任务了那张商在拾取完这个任务之后张商现在后悔了就是后悔你现在一看这任务不好搞啊对吧于是他自己想防匪不想去执行这个任务了
[06:16] 他想把这个任务再次归还到这个组里面去那这个时候作为张商他应该怎么做对吧好我们一起来看一下啊他如果要把这个任务真正归还到这个组里面去在张商作为这个真正的这个用户的执行人的时候他只需要去做一步这样的工作重新让这个任务的执行人变为long就可以了
[06:42] 如果我们把这个任务的这个assign设置为long那就相当于我们刚才这个工作是没做这里头还是放了一个空子放了个空子不就是早期我们当我们的这个主任务还没有真正被某一个用户拾取的时候那这个不就是为空吗对吧所以说我们如果这个时候再去给它设置为空的话那其实就相当于用没有任何的用户去拾取任务对不对
[07:12] 没有谁拾取任务那就相当于这个任务还是作为我们的主任务对不对所以说这一步真正的要去归还我们的任务是非常简单的只要将我们的这个assign的取值重新设置为long就可以了那这个部分各位要注意的就是我们这边也给各位写了一点说明就是建议归还任务前要教练一下
[07:40] 这个用户是否是该任务的负责人对不对你比如说张三二张三二是不是这个任务的负责人呢如果是这个任务的负责人那我们查询的时候就可以查到查到的话我们的task就不为空task不为空这个是我们设置设置为将当前的这个任务设置为none这才是合适的对吧当然要注意的就是啊也可以把当前的这个当前的这个任务设置给其他的用户啊那这个地方我们一会儿就会讲它属于啊
[08:09] 委托就是说当前这个用户呢把这个任务委托给另外一个人去执行啊如果说我们只是这样做的话啊我们如果说只是把用户要去归还到组里面去的话那我们尽量就设置为none就可以了啊而不要设置为其他的用户明白是吧你设置为其他用户其实是可以的啊但是我们不建议咱们这么去做明白是吧
[08:36] 好这是我们如果要把这个任务重新再归还到组里面去其实我们只要是主要是再次调用我们的set assign将我们的任务执行能设置为空就可以达到这个效果这一步就只有一行代码就可以搞定对于我们来说应该也比较简单

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中通过 Java 代码操作任务，包括查询、完成、分配、归还和交接任务等核心功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 `GroupTest.java` 文件中用于完成任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则完成任务并打印提示。
- 代码片段：
  ```java
  //2.创建TaskService对象
  TaskService taskService = processEngine.getTaskService();
  //3.设置一些参数，流程定义的key，用户
  String key = "myProcess_1";
  String assignee = "zhangsan";
  //4.执行查询
  task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskAssignee(assignee) //设置任务的负责人
  .singleResult();
  //5.找到当前的任务
  if(task!=null){
  taskService.complete(task.getId());
  System.out.println("任务执行完毕！");
  }
  ```

画面2：
- 展示了 SQLyog 数据库客户端中查询 `act_hi_actinst` 表的结果。
- 查询结果包含任务执行实例的详细信息，如执行ID、任务名称、分配人、开始和结束时间等。
- 表格数据：
  ```
  EXECUTION_ID_ | ACT_ID_ | CALL_PROC_INST_ID_ | ACT_NAME_ | ACT_TYPE_ | ASSIGNEE_ | START_TIME_ | END_TIME_ | DURATION_
  2002 | 4 | 2000 | 请假审批中审核 | userTask | wanshang | 2018-11-16 16:17:26 | 2018-11-16 16:17:26 | 24
  2002 | 5 | 7002 | 请假审批中审核 | userTask | zhangsan | 2018-11-16 16:19:00 | 2018-11-16 16:19:00 | 0
  ```

画面3：
- 展示了 Activiti Designer 中的 BPMN 图，包含 StartEvent、UserTask、ScriptTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、SubProcess、ParallelGateway、ExclusiveGateway 等节点。
- 画面中未展示具体流程图结构。

画面4：
- 展示了 `GroupTest.java` 文件中用于启动流程实例的代码片段。
- 代码逻辑：获取运行时服务，通过流程定义键启动流程实例，并打印流程定义ID和流程实例ID。
- 代码片段：
  ```java
  //2.博得RuntimeService实例
  RuntimeService runtimeService = processEngine.getRuntimeService();
  //3.创建流程实例，流程定义的key需要知道 holiday
  ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess_1");
  System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
  System.out.println("流程实例ID:"+processInstance.getId());//2001
  ```

画面5：
- 展示了 `GroupTest.java` 文件中用于部署流程定义的代码片段。
- 代码逻辑：获取仓库服务，创建部署对象，添加流程图文件，部署流程。
- 代码片段：
  ```java
  //1.博得ProcessEngine实例
  ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
  //2.博得RepositoryService实例
  RepositoryService repositoryService = processEngine.getRepositoryService();
  //3.创建部署对象
  Deployment deployment = repositoryService.createDeployment()
  .addClasspathResource("diagram/holidays.bpmn") //添加bpmn流程
  .name("请假申请流程")
  .deploy();
  ```

画面6：
- 展示了 `GroupTest.java` 文件中用于启动流程实例的代码片段。
- 代码逻辑：获取运行时服务，通过流程定义键启动流程实例，并打印流程定义ID和流程实例ID。
- 代码片段：
  ```java
  //2.博得RuntimeService实例
  RuntimeService runtimeService = processEngine.getRuntimeService();
  //3.创建流程实例，流程定义的key需要知道 holiday
  ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess_1");
  System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
  System.out.println("流程实例ID:"+processInstance.getId());//2001
  ```

画面7：
- 展示了 `GroupTest.java` 文件中用于完成任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则完成任务并打印提示。
- 代码片段：
  ```java
  //2.创建TaskService对象
  TaskService taskService = processEngine.getTaskService();
  //3.设置一些参数，流程定义的key，用户
  String key = "myProcess_1";
  String assignee = "zhangsan";
  //4.执行查询
  task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskAssignee(assignee) //设置任务的负责人
  .singleResult();
  //5.找到当前的任务
  if(task!=null){
  taskService.complete(task.getId());
  System.out.println("用户任务执行完毕...");
  }
  ```

画面8：
- 展示了 `GroupTest.java` 文件中用于完成任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则完成任务并打印提示。
- 代码片段：
  ```java
  //2.创建TaskService对象
  TaskService taskService = processEngine.getTaskService();
  //3.设置一些参数，流程定义的key，用户
  String key = "myProcess_1";
  String assignee = "zhangsan";
  //4.执行查询
  task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskAssignee(assignee) //设置任务的负责人
  .singleResult();
  //5.找到当前的任务
  if(task!=null){
  taskService.complete(task.getId());
  System.out.println("用户任务执行完毕...");
  }
  ```

画面9：
- 展示了 `GroupTest.java` 文件中用于查询用户任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和候选用户查询任务，遍历任务列表并打印任务ID和流程实例ID。
- 代码片段：
  ```java
  //4.执行查询
  List<Task> list = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskCandidateUser(candidate_users) //设置候选用户
  .list();
  //5.输出
  for(Task task : list){
  System.out.println(task.getId());
  System.out.println(task.getProcessInstanceId());
  }
  ```

画面10：
- 展示了 `GroupTest.java` 文件中用于查询用户任务的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和候选用户查询任务，遍历任务列表并打印任务ID和流程实例ID。
- 代码片段：
  ```java
  //4.执行查询
  List<Task> list = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskCandidateUser(candidate_users) //设置候选用户
  .list();
  //5.输出
  for(Task task : list){
  System.out.println(task.getId());
  System.out.println(task.getProcessInstanceId());
  }
  ```

画面11：
- 展示了 `GroupTest.java` 文件中用于任务认领的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则认领任务并打印提示。
- 代码片段：
  ```java
  //4.执行查询
  Task task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskCandidateUser(candidate_users) //设置候选用户
  .singleResult();
  //5.认领任务
  if(task!=null){
  taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选用户名
  System.out.println("任务已领取完毕！");
  }
  ```

画面12：
- 展示了 `GroupTest.java` 文件中用于任务认领的代码片段。
- 代码逻辑：获取任务服务，根据流程定义键和分配人查询任务，若任务存在则认领任务并打印提示。
- 代码片段：
  ```java
  //4.执行查询
  Task task = taskService.createTaskQuery()
  .processDefinitionKey(key)
  .taskCandidateUser(candidate_users) //设置候选用户
  .singleResult();
  //5.认领任务
  if(task!=null){
  taskService.claim(task.getId(),candidate_users); //第一个参数任务ID，第二个参数为具体的候选用户名
  System.out.println("任务已领取完毕！");
  }
  ```

画面13：
- 展示了 PDF 文档中关于任务交接

