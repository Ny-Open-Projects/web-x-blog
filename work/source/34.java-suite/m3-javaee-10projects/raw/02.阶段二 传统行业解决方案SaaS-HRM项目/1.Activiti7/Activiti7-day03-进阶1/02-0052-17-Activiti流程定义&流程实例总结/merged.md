# 17-Activiti流程定义&流程实例总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\17-Activiti流程定义&流程实例总结_【海量资源尽在 ubkz.com】.mp4
- 时长 6分59秒（音频 419s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那下面我们一起来总结一下我们的第三次activity课程给各位介绍的一些内容那第三次这个课程我们主要介绍了这样的一些内容其中包括了我们的流程定义的主要内容流程定义主要包括我们的资源信息的一些查看包括像我们流程定义的删除
[00:30] 删除啊就是可以做到我们的BPMN和PNG整个这个资源信息都会被删除对吧那其中删除的时候我们也讲了一个集联删除的问题对吧那这个流程资源信息的这个查看呢我们在这边呢主要是使得我们的BPMN和PNG文件又可以被下载下来对吧这样呢又可以啊进一步去查看我们的这个流程执行执行的整个这个过程对吧
[00:59] 比如说我们这个请假到底每一步怎么走对不对那这个流程很多时候我们更多的需要看到这个PNG图片对吧为什么需要看到PNG图片呢因为我们在这边在这个部分能够看到这个能够看到这个BPMN文件展示为我们想看到的这个想看到的这个图形主要是因为我们的idea工具装了一个插件对不对主要是这个原因如果我们
[01:29] 如果我们在外面的环境下那你的BPMN文件是不会表现为我们的图片的所以说我们很多时候希望把PNG图片和BPMN文件都给它下载下来这是我们想看到的一个效果还有一个就是我们的流程在执行的过程中所产生的这样的一些历史数据有些时候我们想看对不对
[01:58] 那如果我们想看历史数据的话那这个时候我们也讲了啊我们可以通过historic Service来实现我们的这个数据的这个查看对吧历史记录的查看啊当然我们后面呢又给各位进一步讲到了我们的这个流程实例对吧以及我们的这个流程定义和这个流程实例之间的关系对不对这个关系啊
[02:21] 我们可以认为流程定义就好比是一个类而我们的流程实例好比就是产生了这个类产生了若干个对象对吧而实例与实例之间是不存在相互干扰对吧那就这样做我们就可以达到一个公司如果说比如说有100个员工去请假那每个员工请假他们应该在执行这个流程的时候是相互不干扰的对吧是不会干扰的
[02:48] 后面我们又讲到了我们的流程
[02:52] 如果我们的这个流程流程在往后推进的过程中又真正跟具体的我们的业务系统进行关联呢那我们给各位分析了一个就是我们如何去做这种关联对吧使得我们的这个业务系统和我们的这个activity能够很好的整合在一起使用对不对那这个地方我们主要给各位介绍的就是一个叫做business key对不对那这个business key主要是存放在哪个表中呢
[03:20] 对吧那我们开始也给各位介绍了主要是在我们的这个应该是在我们的这个RU exclusion吧应该是这个表中就会有一个business key那这个business key如果你不去设置的话那我们在流程实例启动的时候那其实它是没有值的那有同学就会思考那我们怎么样去设置我们的这个business key了对不对那好我们这个地方主要通过的是当我们的run time Service在启动一个流程实例的时候
[03:49] 我们除了传第一个参数是我们的这个process definition key我们还可以传入第二个参数就是叫做business key对吧通过第二个参数的传入我们呢就可以很好的将我们的这个业务系统的组件直接存入到所关联的这个流程实例中去对吧比如说我们的这个请假单某一条记录的ID作为它的这个组件我们就直接可以将请假单ID直接存入
[04:17] 存入到我们的这个RU Excusing这个表中去对吧这样呢我们就可以将来可以看到我们的Business Key就真正关联的是某一条记录的这个某一条请假单的这个ID对吧这样我们基本上就完成了我们的这个业务系统和我们的这个Activity进行关联对吧当然这个Activity存入到这个Business Key存入到Activity之后
[04:44] 我们如果要把它取出来的话我们呢这边也是有相关的这个方法啊那就是我们可以先呢查询到我们的这个流程实例对吧当我们查询到我们的流程实例之后只要通过实例点get business key这样呢我们就会很轻松的啊从activity中取出我们的这个业务系统的组件那有了这个业务系统的组件之后我们下一步就可以很轻松的
[05:12] 你像我们这里头如果以请假单为例的话就可以很轻松的来查到我们这个请假单的具体信息对吧从而知道这个请假单它目前已经在activity中已经推进到哪一个节点了对吧这样呢我们就不需要通过这个状态智能一样可以很轻松的管理我们的这个请假的执行流程最后我们给各位讲了一个就是我们的这个流程实例的挂起
[05:42] 与激活对吧那这个部分刚才我们也通过这个示例给各位检测了一下那我们一起来看一下主要就是如果是全部实例的话我们用的是我们用的是Repository Service用这个Actual Process Defunction来实现我们的这个激活对吧用我们的这个Suspend Process DefunctionBy ID或者By Key来实现这个流程所有的这个
[06:10] 所有的相关的实例全都被挂起当然你也可以操作的是某一个如果是某一个的话我们一定是先讲先将我们的Processing Instance要查出来然后再去用Runtime Service中的Archive Processing InstanceByID或者是这个地方只能ByID了这样我们就可以将某一个流程实例激活如果要挂起
[06:38] 通过suspend process instance by id就可以把它进行挂起就可以把它进挂起好我们的这个这一次课程内容大概就是这样的一些内容主要是呢关联到我们的这个流程定义我们的这个流程实例部分

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti7 工作流引擎中流程定义、流程实例、历史信息的查询与挂起/激活操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：标题页，显示“SaaS-IHRM 项目-Activiti7 工作流引擎”。
画面2：讲解“6.5 流程定义资源查询”，展示通过流程定义对象获取流程定义资源的代码示例。
画面3：展示 BPMN 图形界面，包含 StartEvent、UserTask 等节点，并显示控制台日志。
画面4：在 MySQL GUI 中查询 act_ru_execution 表，展示流程实例的 ACT_ID_、PROC_INST_ID_ 等字段。
画面5：讲解如何通过 HistoryService 查询历史活动实例，展示相关代码。
画面6：讲解“1.3 Businesskey(业务标识)”，说明业务标识的用途，并展示代码和数据库表中存储的业务标识。
画面7：与画面6内容相同，展示“1.3 Businesskey(业务标识)”的代码和数据库表。
画面8：在 MySQL GUI 中查询 act_ru_execution 表，展示流程实例的 ACT_ID_、PROC_INST_ID_ 等字段。
画面9：与画面6内容相同，展示“1.3 Businesskey(业务标识)”的代码和数据库表。
画面10：讲解“1.5 查询流程实例”，展示通过 RuntimeService 查询流程实例的代码。
画面11：讲解“1.5.1 关联 businessKey”，说明在实际应用中查询流程实例列表时可能需要显示业务系统信息。
画面12：讲解“1.6.1 全部流程实例挂起”，展示通过 RepositoryService 挂起流程定义的代码。
画面13：继续讲解“1.6.1 全部流程实例挂起”，展示判断流程定义是否挂起并激活的代码。
画面14：讲解“1.6.2 单个流程实例挂起”，展示通过 RuntimeService 挂起单个流程实例的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
@Test
public void getProcessResources() throws IOException {
    // 流程定义id
    String processDefinitionId = "";
    // 获取 repositoryService
    RepositoryService repositoryService = processEngine
            .getRepositoryService();
    // 流程定义对象
    ProcessDefinition processDefinition = repositoryService
            .createProcessDefinitionQuery()
            .processDefinitionId(processDefinitionId)
            .singleResult();
}

画面3：
select single component to edit its properties

画面4：
Query: 1

画面5：
public void testHistoric01() {
    HistoryService historyService = pe.getHistoryService();
    HistoricActivityInstanceQuery query = historyService
            .createHistoricActivityInstanceQuery();
    query.processInstanceId("1501");
    List<HistoricActivityInstance> list = query.list();
    for(HistoricActivityInstance ai : list){
        System.out.println(ai.getActivityId());
        System.out.println(ai.getActivityName());
    }
}

画面6：
// 根据流程定义的key启动一个流程实例
ProcessInstance processInstance = runtimeService
        .startProcessInstanceByKey(processDefinitionKey,
        businessKey);

画面7：
// 根据流程定义的key启动一个流程实例
ProcessInstance processInstance = runtimeService
        .startProcessInstanceByKey(processDefinitionKey,
        businessKey);

画面8：
Query: 1

画面9：
// 根据流程定义的key启动一个流程实例
ProcessInstance processInstance = runtimeService
        .startProcessInstanceByKey(processDefinitionKey,
        businessKey);

画面10：
@Test
public void queryProcessInstance() {
    // 流程定义key
    String processDefinitionKey = "holiday";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    List<ProcessInstance> list = runtimeService
            .createProcessInstanceQuery()
            .processDefinitionKey(processDefinitionKey)
            .list();
}

画面12：
@Test
public void suspendOrActivateProcessDefinition() {
    // 流程定义id
    String processDefinitionId = "";
    // 获取 repositoryService
    RepositoryService repositoryService = processEngine
            .getRepositoryService();
    // 获取流程定义
    ProcessDefinition processDefinition = repositoryService
            .createProcessDefinitionQuery()
            .processDefinitionId(processDefinitionId)
            .singleResult();
}

画面13：
// 是否挂起
boolean suspend = processDefinition.isSuspended();
if(suspend){
    // 如果是挂起状态，这里将流程定义下的所有流程实例全部激活
    repositoryService.activateProcessDefinitionById(processDefinitionId,
            true, null);
    System.out.println("流程定义："+processDefinitionId+"激活");
}else{
    // 如果是激活状态，这里将流程定义下的所有流程实例全部挂起
    repositoryService.suspendProcessDefinitionById(processDefinitionId,
            true, null);
    System.out.println("流程定义："+processDefinitionId+"挂起");
}

画面14：
@Test
public void suspendOrActiveProcessInstance() {
    // 流程实例id
    String processInstanceId = "";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    // 根据流程实例id查询流程实例
    ProcessInstance processInstance = runtimeService
            .createProcessInstanceQuery()
            .processInstanceId(processInstanceId)
            .singleResult();
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：标题“6.5 流程定义资源查询”，子标题“6.5.1 方式 1”。
画面3：BPMN 图形界面，StartEvent 指向 UserTask。
画面4：MySQL GUI 中的表结构，包含 ACT_ID_、PROC_INST_ID_、START_TIME、END_TIME 等字段。
画面5：PPT 标题“1.5 查询流程实例”，内容说明流程实例的状态和运行节点。
画面6：PPT 标题“1.3 Businesskey(业务标识)”，内容说明业务标识的用途和存储位置。
画面7：与画面6相同。
画面8：MySQL GUI 中的表结构，包含 ACT_ID_、PROC_INST_ID_、BUSINESS_KEY、PROC_DEF_ID 等字段。
画面9：与画面6相同。
画面10：PPT 标题“1.5 查询流程实例”，内容说明如何查询流程实例。
画面11：PPT 标题“1.5.1 关联 businessKey”，内容说明在实际应用中查询流程实例列表时可能需要显示业务系统信息。
画面12：PPT 标题“1.6.1 全部流程实例挂起”，内容说明如何挂起流程定义。
画面13：PPT 标题“1.6.1 全部流程实例挂起”，内容说明如何判断流程定义是否挂起并激活。
画面14：PPT 标题“1.6.2 单个流程实例挂起”，内容说明如何挂起单个流程实例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

