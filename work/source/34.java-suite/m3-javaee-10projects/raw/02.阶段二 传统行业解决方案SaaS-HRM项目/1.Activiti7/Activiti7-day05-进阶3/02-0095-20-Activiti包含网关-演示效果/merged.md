# 20-Activiti包含网关-演示效果

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\20-Activiti包含网关-演示效果_【海量资源尽在 ubkz.com】.mp4
- 时长 17分53秒（音频 1073s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:04] 那我们刚才已经把这个example的流程定义的图已经画好了我们现在可以把这个把这个ID也给它改一下给它改成叫做example对吧这样我们基本上就完成了我们这个体检的流程那下面我们就可以对它来进行测试我们可以到这个部分把我们的这个parallel gateway test把它直接考一下拿过来
[00:33] 我们这个地方应该是叫做inclusive对吧inclusive就是叫做包含inclusive这个意思现在可以Countryway来到这来然后把这个给它改一下改成叫做inclusivegetwaytest然后OK
[01:00] 这样我们测试的是我们的包含网关包含网关我们的包含网关它的主要的特点各位我们可以一起再来回顾一下它的特点既具有我们的排他网关具有我们的排他网关和我们的并行网关的一些共同点
[01:29] 一些共同点那它的特点是什么第一个可以设置我们的可以设置我们的流程流程变量这是第一个我们如果有很多过分支的时候当我们的流程变量当流程变量取值比如说取值都成历史都成历史
[01:58] 此时若干个峰值都可以执行此时若干个峰值都可以此时若干个峰值都可以执行这是它的一个特点都可以执行这是它的特点是这样的下面我们就可以来做出一个测试在测试之前我们也一样先来考虑一下我们的库比如说我先
[02:27] 把我们整个库给它清理了然后我们这个时候再来做一个创建再回到这边现在我就可以去把我们部署的代码重新再给它跑一下对吧但是这一次我们部署主要是部署的是我们的Holo底6这个是没错的然后紧接着还有一项工作就是我们早期之前所做的执行任务的卖方法
[02:57] 直接给它去掉注掉现在我们就可以来做我们的Holo6应该是example现在已经是example了我们把这个称改一下叫做exampleBPMN而我们的PNG你可以去加也可以不加这个称就应该变成我们的体检叫做体检流程叫做体检体检流程
[03:27] 那再往后我们就可以啊基本上就可以来部署了吧现在呢我们走一下啊那我们来看一下这个库啊这个数据库中啊是否已经把这套流程啊部署好了对吧我们这个时候可以重新再刷一下啊那这时候你就可以打开我们的这个byte array来看一下啊流程已经部署进来了对吧已经变成我们的这个常规体检抽血了变成这样的一些内容了啊这个证明已经部署好了对吧
[03:56] 好那我们部署好了下一个环节我们就可以直接来看啊直接来看我们这个具体的那我们的这个流程实例启动对不对这一次启动的这个流程实例呢同时带上的这个流程变量啊那我们这一次的这个变量主要是我们的U座太后对吧所以说我可以把这个地方给它改了啊比如说搞出一个实践类型的叫做啊U座太后等于那这个我们
[04:26] 开始在设计的时候这个地方这个Uso type好像是一和二是数字对吧如果是数字的话我可以改一下比如说改成integer对吧Uso type比如说我取之为二可以吗那取之为二代表的是代表的是我们的这个管理者对吧是我们的管理者好那将来真正放到这里边来应该有我们的这个Uso type这个是我们的key对吧
[04:55] 所以说我在这边呢也应该是叫做user type啊而真正取的值就是我们后面放的这个user type对吧这样我们基本上啊就完成了我们的这个流程变量啊复职的工作当然我们的这个流程定义的key已经变了啊我们叫做example对吧copy啊直接lend到这边来那就是它啊那现在我们又可以重新去启动我们的这个流程实例对吧
[05:22] 启动流程实例MAP里头放的是我们的U做type而代表的是管理者那各位啊我们在还没有真正去执行这个代码的时候你猜测一下我们将来如果是一个U做type取之为二的话那我们应该说这一项这一项这一项都满足条件那这个时候就相当于将来我们会这三个任务将来应该同时都可以走对吧好
[05:48] 我们来看一下啊这时候我再去让我们的这个流程实例启动一下啊我们来看一下效果好现在呢这个流程实例就已经启动起来了对吧启动起来我们下一个环节再走的话主要就是来搞定我们的这个来搞定我们的这个当事人啊执行他自己的任务对吧好这个时候我们可以一起来看一下啊我们在这里边这个当事人完成自己的任务主要就是
[06:20] 就是任务我们这边啊就是任务执行啊任务执行完成那将来具体是哪样的一些任务要执行完成呢对吧第一个我们的key啊这个改一下啊那还是这个用户吗对吧那这个地方呢我们可以这样做啊把我们的这个example啊copy给他直接往我们这边control v啊lend to一份我们这边呢就可以直接打开来看啊那填写
[06:48] 我们的这个请假单应该是张商来完成啊所以呢我在这边呢可以直接把我们的这个任务执行人康小微啊搞成我们的张商对吧那这个时候我们的任务就可以跑了啊当然你除了看这个之外呢你也可以去看我们的这个RU task表申请单是谁呢是张商对不对这样也可以看啊其实是一样的啊然后我们走
[07:15] 好这时候我就可以让张三完成他自己的任务对吧我们可以看到张三的任务就已经执行完了我们这时候再刷一下数据库啊那于是现在就变成了比较多啊这时候各位可以看到我们的李四王五赵六是同时都上来了为什么会是一个这样的结果呢那是因为我们刚才在这边张三完成的任务就是这个节点走完了当这个节点走完的时候走我们的包行网关
[07:42] 而我们的包含网关将来在这里面设置了这三个条件那过去思考我们刚刚在这个流程实例启动的时候给的这个U字type取值其实是等于2对不对所以说我们的这三个条件将来去走的话U字type等于2这个条件是成立的所以常规体检项要走那同样的这个条件也成立对吧所以抽血化验的这个节点要走那一样的我们的U字type等于2
[08:11] 附加项就也应该要走啊所以说现在我们可以看到啊这三个节点啊都放在这里面就变成了我们现有的这个情况啊这三个节点啊都要走对吗好这三个节点都走那下一步我们可以进一步来看啊进一步来看那我们这个时候这三个节点目前都要走啊那你肯定要选取其中一个让他先去走对不对
[08:36] 比如说这个管理者这个管理者到这里头来做这个体检他先检的是我们的常规体检那如果先检我们常规体检的话就相当于是李四要去完成任务对不对因为常规体检项目是他来做嘛他来审嘛对吧他来审那于是我们这个时候就相当于李四要对他进行常规体检对不对所以说我们呢
[09:02] 可以把我们的代码进一步给他更改一点点就可以了把这个地方改成我们的当事人李四对吧这样其实就相当于他在这里头完成的是我们的常规体检项对不对完成常规体检项当然你除了看这个之外你也可以去看我们的Arcadus也可以看这个你看这个的时候你可以看到我们的inclusive gateway现在已经开始了
[09:31] start time end time都已经走了但是我们现在要去执行的这个常规体检项没有结束时间抽血化验没有结束时间我们的附加项也没有结束时间那我如果执行刚才的这个理事做完这个工作应该说我们的这个常规体检项就有结束时间了对不对好我们这个时候可以重新再看一下效果那它就已经完成了对不对那就是说理事完成了这个常规体检项目所以你刷的时候
[10:00] 你刷的时候我们这个常规体检项目在这个地方就会有结束时间了对吧但是我们的抽血化验和我们的附加项目这两个部分还没有结束时间当然除了看这个表我们也可以去看我们的这个RU task表在这个task表中你会发现又少了一下我们的这个理事已经完成了他的任务所以少了一下当然你也可以去看我们的这个execution表这个表里头目前你可以看到
[10:29] 有一个要做两个要做三个要做四个要做也就是说他这里头目前真正要执行的还很多那我们接着往后走接着来思考来看那就相当于如果按照我们的这个流程继续来分析的话常规体检像做完了其实他已经会走到这个部分来了对吧也就是说我们的inclusive gateway他应该会走了然后我们的初学化验和我们的早餐这两个都没做对吧这俩都没做
[10:59] 那我们呢也可以根据刚才我们讲的啊我们的这个inclusive2是不是这个时候各位也会看到啊它已经有一次了对不对已经有一个加入进来但是呢它并没有我们的end time这个结束时间啊那是因为啊它在这里面呢我们的这个抽血化验和附加项目还没做完对吧那我们现在可以来完成它可以吧那现在我先来完成我们的这个抽血
[11:28] 先来完成我们的附加项目吧最后我们做这个抽血化验吧那附加项目要做的话我们应该让赵六去完成他的任务对吧所以说呢我们也可以到这边直接啊去完成我们赵六的任务啊再回到这边让我们的赵六来完成他的任务走来看一下效果啊好现在呢我们可以看到赵六已经完成了任务啊于是我们再刷一下我们再刷一下啊刷新这时候呢我们可以看到我们的这个赵六
[12:01] 附加体检项目对应的这个结束时间就有了对吧我们的抽血化验还是没有完成对不对因为抽血化验没有完成所以呢我们这个inclusive对应的end time是不是一直还没有还没有值这是inclusive gateway 2是我们的这个节点是这个量这个节点它一直还没有值那我们呢也可以现在做这个抽血化验的工作对不对好那我们继续来做
[12:30] 抽血化验的工作你要跟进我们的task表我们task表中现在也只有抽血化验可以去做了比如说王武给他来做我们的抽血化验工作抽血化验工作是王武来做所以我们把这个部分Country V拿过来这时候王武就可以给他做抽血化验的工作抽血化验工作做好按照我们的流程图来看的话就相当于这个工作做好应该这个时候就会去比如说小王来执行
[13:00] 来给他提供早餐对不对所以说现在我们这个时候再走的话就应该执行到这个节点这个节点我们也可以看一下来刷一下我们的这个task表现在就进入到我们的这个早餐对吧是小王来提供我们同时也可以看一下我们的看一下我们的这个asq型表asq型表的现在这里面这些节点还依然都停留在这里头这是我们的包含网关对不对
[13:29] 这四个相对这些任务一直还包含在这里面因为你还没有并没有全都执行完对不对好我们也可以看一下这个部分我们的inclusive gateway对应的他的end time是不是一直还是没有值目前我们的end我们的早餐是不是也没有end time那你想一下我们的早餐是不是还没完成当我们的早餐完成的时候我们的
[13:56] inclusive gateway应该整理上这几个任务是不是就全都执行完了所以说现在我们可以接着让我们的这个小王啊来完成他的这个给他提供这个早餐对不对所以说呢到这上copy一下啊然后回到我们的这个回到我们的这个任务执行人啊把它改一下这时候我们重新再去执行一把各位这个时候你再去看啊当小王完成这个任务的时候
[14:25] 当这个任务一旦完成的时候那是不是就相当于这个任务已经完成了在汇聚到这里面来的时候我们的这些任务是不是都执行完了在汇聚到这边应该说这个时候它就会有我们的end time对吧我们来看一下好再刷新一下这时候各位可以看到我们的这个inclusive gateway2各位可以看到它的end time就已经有了它是它的这个时间点如果你去看的话
[14:54] 会跟我们早餐的这个完成时间点几乎是一样的对不对185832185832对不对这样呢我们基本上啊就完成了我们的这个整个这个流程的执行啊最后就会进入到我们的n的event对吧所以说当我们的这个呃包含网关里头的各个节点都全都只有他们全都执行完我们的这个inclusive gateway对应了他的这个时间点才会有对不对
[15:22] 那这一点跟我们的并行网关是不一样的啊并行网关只要有一个到达对应的他是不是就会有一个有一个这样的值啊那你再到达对应的是对应的他这个地方又有个值啊所以总体上跟我们的这个并行网关是有区别的啊当我们的这些工作全都执行完那对应的我们的inclusive gateway2这个这个节点啊这个任务相当于这个网关在这里的汇聚汇聚认为我们总体上这些
[15:51] 包含的内容全都完成然后呢我们的流程才会进一步往后推进一个节点如果这个节点是一个N的节点N的event节点那就意味着结束了对吧当然这个节点也可以是其他的另外一个比如说普通的任务节点啊那它就没有结束啊这样呢我们基本上啊就给各位把我们的这个包含网关啊给各位大致上啊给它全都啊搞了一遍
[16:20] 通过这个网关过一会可以看到啊它可以设置条件这是啊这是一个点啊那这些条件呢将来如果都成立那就都执行成立一个就走一个明白是吧只有当我们包含网关所包含的这样的一些任务节点全都完成的时候我们的这个inclusive gateway在这里头才会真正的跟你啊汇聚汇聚起来啊汇聚起来之后认为当前的这个包含的
[16:49] 包含的所有的任务都已经完成于是他可以向下进一步推进一个把我们的流程继续往后推进一个步骤这是我们大致上啊呃就是这样的好呃关于我们的这个网关部分呢在这边呢我们也可以各位啊基本上啊就全都已经啊呃讲到了啊那最终我们的这个网关部分呢呃各位也可以看一下如果说呃这里头的测试啊如果所有的条件都不成立也一样的啊
[17:18] 会去报一个这样的会去如果说网关中设置的这个条件流程变量不存在那他也一样会给我们报一个异常啊当然我们如果说啊整个这个网关在执行的过程中他将来除了影响我们的exclusion表影响我们的task表还有一个就是我们的这个历史记录也可以去查看对吧就是这两张表可以去看我们的这个包含网关他真正执行的每一个环节啊
[17:47] 好了那我们的网关部分啊就全都给各位啊就结束了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Activiti 工作流引擎中的包含网关（Inclusive Gateway）实现并行任务，并通过 Java 代码部署流程、启动流程实例、查询和完成任务，同时展示数据库中相关流程和任务数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示 BPMN 图编辑器界面，流程图包含“开始事件”、“用户任务”、“包含网关”、“用户任务”、“并行网关”和“结束事件”。
- 属性面板显示当前选中元素的 ID 为 3，名称为“体检项目”，异步为 false，排他为 false。
- 画面右侧工具栏显示 BPMN 元素列表，包括 StartEvent、EndEvent、UserTask、ScriptTask、ServiceTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、Subprocess、Lane 和 ParallelGateway。

画面2：
- 展示 Java 代码文件 InclusiveGatewayTest.java，内容为部署 BPMN 流程定义。
- 代码中使用 repositoryService.createDeployment() 方法添加资源文件 "diagram/day05/examine.bpmn"，并设置名称为“体检流程”。
- 项目结构显示在左侧，包含多个 BPMN 文件，如 examine.bpmn、holiday.bpmn 等。

画面3：
- 代码中使用 repositoryService.createDeployment() 方法添加资源文件 "diagram/day05/examine.bpmn"，并设置名称为“体检流程”。
- 代码中使用 deployment.deploy() 方法部署流程定义。

画面4：
- 代码中使用 runtimeService.startProcessInstanceByKey("holidayParallel", map) 方法启动流程实例。
- 代码中输出流程定义 ID 和流程实例 ID。

画面5：
- 代码中使用 runtimeService.startProcessInstanceByKey("examine", map) 方法启动流程实例。
- 代码中输出流程定义 ID 和流程实例 ID。

画面6：
- 代码中使用 runtimeService.startProcessInstanceByKey("examine", map) 方法启动流程实例。
- 代码中输出流程定义 ID 和流程实例 ID。
- 代码中使用 taskService.createTaskQuery().processDefinitionKey("examine").taskAssignee("lisi").singleResult() 方法查询任务。
- 代码中使用 taskService.complete(task) 方法完成任务。
- 代码中使用 System.out.println(task.getId()) 方法输出任务 ID。

画面7：
- 代码中使用 taskService.createTaskQuery().processDefinitionKey("examine").taskAssignee("lisi").singleResult() 方法查询任务。
- 代码中使用 taskService.complete(task) 方法完成任务。
- 代码中使用 System.out.println(task.getId()) 方法输出任务 ID。

画面8：
- 展示 BPMN 图编辑器界面，流程图包含“开始事件”、“用户任务”、“包含网关”、“用户任务”、“并行网关”和“结束事件”。
- 属性面板显示当前选中元素的 ID 为 3，名称为“体检项目”，异步为 false，排他为 false。
- 画面右侧工具栏显示 BPMN 元素列表，包括 StartEvent、EndEvent、UserTask、ScriptTask、ServiceTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、Subprocess、Lane 和 ParallelGateway。

画面9：
- 代码中使用 taskService.createTaskQuery().processDefinitionKey("examine").taskAssignee("lisi").singleResult() 方法查询任务。
- 代码中使用 taskService.complete(task) 方法完成任务。
- 代码中使用 System.out.println(task.getId()) 方法输出任务 ID。

画面10：
- 代码中使用 taskService.createTaskQuery().processDefinitionKey("examine").taskAssignee("lisi").singleResult() 方法查询任务。
- 代码中使用 taskService.complete(task) 方法完成任务。
- 代码中使用 System.out.println(task.getId()) 方法输出任务 ID。
- 画面底部显示“Process finished with exit code 0”。

画面11：
- 展示 MySQL 数据库管理工具界面，显示数据库 activiti 的表结构。
- SQL 语句为：drop database activiti; create database activiti;
- 数据库表中显示了流程实例和任务数据。

画面12：
- 展示 BPMN 图编辑器界面，流程图包含“开始事件”、“用户任务”、“包含网关”、“用户任务”、“并行网关”和“结束事件”。
- 属性面板显示当前选中元素的 ID 为 3，名称为“体检项目”，异步为 false，排他为 false。
- 画面右侧工具栏显示 BPMN 元素列表，包括 StartEvent、EndEvent、UserTask、ScriptTask、ServiceTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、Subprocess、Lane 和 ParallelGateway。

画面13：
- 展示 BPMN 图编辑器界面，流程图包含“开始事件”、“用户任务”、“包含网关”、“用户任务”、“并行网关”和“结束事件”。
- 画面右侧工具栏显示 BPMN 元素列表，包括 StartEvent、EndEvent、UserTask、ScriptTask、ServiceTask、ManualTask、ReceiveTask、BusinessRuleTask、CallActivity、Subprocess、Lane 和 ParallelGateway。

画面14：
- 展示 PDF 文档内容，内容为 Activiti 工作流引擎的包含网关相关说明。
- 文档中提到如果包含网关设置的条件中，流程变量不存在，会抛出异常。
- 文档中提到当执行到包含网关时，会查询 ACT_RU_EXECUTION 表和 ACT_RU_TASK 表。
- 文档中提到第一记录是包含网关分支，第二条记录是两个分支，常规项体检和抽血化验。
- 文档中提到当前任务表 ACT_RU_TASK 中的记录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();

//3.进行部署
Deployment deployment = repositoryService.createDeployment()
    .addClasspathResource("diagram/day05/examine.bpmn") //添加bpmn资源
    .name("体检流程")
    .deploy();
```

画面3：
```java
//3.进行部署
Deployment deployment = repositoryService.createDeployment()
    .addClasspathResource("diagram/day05/examine.bpmn") //添加bpmn资源
    .name("体检流程")
    .deploy();
```

画面4：
```java
//4.输出流程的相关信息
System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
System.out.println("流程实例ID:"+processInstance.getId());//2501
```

画面5：
```java
//4.输出流程的相关信息
System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
System.out.println("流程实例ID:"+processInstance.getId());//2501
```

画面6：
```java
//4.输出流程的相关信息
System.out.println("流程定义ID:"+processInstance.getProcessDefinitionId());//holiday:1:4
System.out.println("流程实例ID:"+processInstance.getId());//2501
```

画面7：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面8：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面9：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面10：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面11：
```sql
drop database activiti;
create database activiti;
```

画面12：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面13：
```java
//4.处理任务，给当前用户任务对应的流程执行的语句，任务ID:task.getId()
if(task!=null){
    taskService.complete(task);
    System.out.println("用户任务执行完毕...");
}
//5.输出任务的id
System.out.println(task.getId());
```

画面14：
```text
如果包含网关设置

