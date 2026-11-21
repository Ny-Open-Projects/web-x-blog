# 03-Activiti流程定义信息删除的注意事项

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\03-Activiti流程定义信息删除的注意事项_【海量资源尽在 ubkz.com】.mp4
- 时长 8分2秒（音频 482s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 这是刚才我们在这边把这个流程定义信息我们想把它删掉或者说我们的这个流程部署的定义信息想把它删掉那背后其实也是影响我们这三张表那各位我们现在一起来思考一个问题这个问题是这样的比如说我们现在这个流程呢它已经启动了但是它并没有跑完什么意思呢
[00:28] 别说现在这个流程也起了呢正好走着走着正好进入到部门经理审批这个环节了但是我们这个时候公司的总经理或者说公司的总裁发了一个新的制度说啊原来没有走完的这些流程就暂时先不走了对吧暂时不走了然后呢我们原来没有执行完的这些流程呢也都可以重新打回然后呢
[00:57] 我们需要重新发起新的请求这个是在真实的公司场景中是存在的尤其是这种新制度和老制度替换的时候经常存在的这个新制度老制度替换主要就是这个公司的高层管理者一旦变更的时候那这种几率还是比较高的对吧那我们现在呢如果真的发生了这种情况
[01:25] 这个流程跑到这个地方还没跑完然后呢这个公司的高管就已经下命令了说这个流程不再跑了把流程所有的定义信息我们整个流程的部署整个这套东西都要被删掉那这个时候就比较可危了有的人会思考这时候删到底能不能被删除呢这个时候我就不去给各位做这个演示工作如果各位要去做这个演示工作你可以把这个
[01:55] 最后再删完对吧把我们早期写过的这几个类再去运行一遍先去做我们的部署再去做我们的启动流程实例再去做我们完成任务你只要比如说我就让我们的这个填写请假单完成部门经理省我现在不走了对吧然后呢部门经理不去做这个任务完成省经理不去做任务完成于是你就开始继续去执行我们的这个删除的这个命令
[02:25] 告诉各位的这个结果是啊你直接这么删是不能删除的所以这个地方我给各位呢写上一下啊我们的这个叫做注意啊注意事项主要就是啊比如说当当我们啊正在正在执行的这一套啊流程未完全啊
[03:00] 没有完全没有完全没有完全审批审批结束没有完全结束的时候此时如果要删除我们的这个流程定义信息就会失败这是这个结论就会失败有人会思考为什么就会失败原因很简单
[03:33] 你想一想你的流程定义信息都被删除了那将来我走节点的时候我这个节点比如说张商这个节点走完应该按道理比如说请加单填完了下一步就应该是部门经理省对不对部门经理省就应该省完之后就应该是总经理省现在问题是啥呢你部门经理省这个动作你没执行完你把你把这个流程定义信息给我删了
[03:57] 即便说我们部门经理将来审核完了那部门经理审核完了之后他的下一个环节是整经理你不去看我们的流程定义信息你能够知道他的下一个环节是整经理吗因为这个环节只能够是通过我们的流程定义信息去看你只能够查我们的流程定义的图你才能知道部门经理当他做完这个工作下一个环节就是整经理了
[04:24] 可是现在你把我们的这个流程定义的这个图给我删了那肯定我们将来啊这个这个这个后续的工作就没有办法开展对吧所以说他干脆那你在这里说做这套删除的时候干脆让你失败就告诉你我当前这个流程没走啊那对不起你不能删我的你不能删我的流程定义信息要不然的话后面我就没办法走了对吧所以就会删除失败那有的人会思考如果啊比如说公司啊
[04:54] 公司层面要强制删除对吧要强制删除那我们应该怎么办对不对就是这个领导领导一旦换届之后这套流程就不走了对吧就是强制性的规定或者是命令对吧那我们没有办法我们这套流程可能就不能再跑了那怎么去做回那可以删呢我们这边呢一起再来看一下
[05:20] 那这边有一个专门的介绍就是我们可不可以考虑一下我们的集联删除集联删除就这种方式如果当这个参数第二个参数设置为去的时候我们就可以实现我们的集联删除就是说当我这个流程定义信息一旦被删除的时候那对不起你没有跑完的这些流程这里头的这些记录关联的这些记录对不起也全都一并通通删掉
[05:50] 这个时候就相当于相当于这个表层将来我做删除的时候我先把这里头记录给你删了那是不是意味着之前没有走完的这些流程已经不存在了既然这些流程都不存在了那我们再去把我们的这个部署信息我们的这个流程定义信息我们的这个我们的这个Better Ray表中的这些信息就这时候你再去做删除就不会有影响了
[06:20] 所以这就是我在这里给各位介绍的一个细节如果这个时候还要强制性删除可以使用我们的这个Repository Service里头的DeploymentDeploymentDeleted Deployment将它的参数设置为True那参数设置为True代表是什么意思参数True代表代表几连删除
[06:49] 此时就会先删除未先删除没有完成没有完成的流程没有完成的流程流程节点信息节点就是正在运行的这些没有运行完的这样的一些流程上的节点先给他们都清理掉了清理掉了最后
[07:19] 最后就可以删除我们的流程定义信息这就是这个道理当然你这个也可以设置为force如果设置为force是不是就相当于没写就不会激灵如果选择force参数force的值代表不激灵不激灵那你就不用多此一举在这里写上第二个参数是force
[07:49] 我们可以认为呢如果你不写默认是不是就是fors所以这是这个意思啊好我们把这个呃流程定义信息删除的时候啊他的注意事项给各位啊呃总结了一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码删除已部署的 Activiti 流程定义，并展示相关数据库表结构和流程图元素。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IDEA 编辑器中 DeleteProcessDefinition.java 文件，包含 package 声明和类定义，下方运行日志显示成功删除部署。
画面2：展示 MySQL Workbench 中的 SQL 脚本，用于创建 activiti 数据库和列出相关表结构。
画面3：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，注释说明获取 ProcessEngine 和 RepositoryService。
画面4：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面5：展示 PPT 页面，标题为“6.4 流程定义删除”，内容为 deleteDeployment() 方法的 Java 代码，包含注释说明。
画面6：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面7：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面8：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面9：展示 Activiti Designer 中的 BPMN 流程图，包含 StartEvent、UserTask、EndEvent 等元素，右侧为元素面板。
画面10：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面11：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面12：展示 PPT 页面，标题为“删除已经部署成功的流程定义”，内容为 deleteDeployment() 方法的 Java 代码，包含注释说明。
画面13：展示 MySQL Workbench 中的 SQL 脚本，用于创建 activiti 数据库和列出相关表结构，下方显示了表数据。
画面14：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1", true)。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
package com.itheima.day03.activiti;
import ...
//我已经写好的流程定义
//后面讲解删除
public class DeleteProcessDefinition {

画面3：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngine.getDefaulltProcessEngine();
    //2.创建RepositoryService对象
    RepositoryService repositoryService = processEngine.getRepositoryService();
    //3.执行删除流程定义，参数代表流程部署的id
    repositoryService.deleteDeployment("1");
}

画面5：
public void deleteDeployment() {
    // 流程部署Id
    String deploymentId = "8801";
    // 通过流程引擎获取repositoryService
    RepositoryService repositoryService = processEngine
        .getRepositoryService();
    //删除流程定义，如果该流程定义已有流程实例启动则删除时出错
    repositoryService.deleteDeployment(deploymentId);
    //设置true 级联删除流程定义，即使该流程有流程实例自动也可以删除，设置为false非级联删除方式，如果流程
    //repositoryService.deleteDeployment(deploymentId, true);
}

画面12：
public void deleteDeployment() {
    // 流程部署Id
    String deploymentId = "8801";
    // 通过流程引擎获取repositoryService
    RepositoryService repositoryService = processEngine
        .getRepositoryService();
    //删除流程定义，如果该流程定义已有流程实例启动则删除时出错
    repositoryService.deleteDeployment(deploymentId);
    //设置true 级联删除流程定义，即使该流程有流程实例自动也可以删除，设置为false非级联删除方式，如果流程
    //repositoryService.deleteDeployment(deploymentId, true);
}

画面14：
repositoryService.deleteDeployment("1", true);

画面2：
drop database activiti;
create database activiti;
act_re_deployment 部署信息
act_re_procdef 流程定义的一些信息
act_re_bytearray 流程定义的bpmn文件及png文件
#背后影响的表：
act_hi_actinst 已完成的活动信息
act_hi_identitylink 参与者信息
act_hi_procinst 流程实例
act_hi_taskinst 任务实例
act_ru_execution 执行表

画面13：
drop database activiti;
create database activiti;
act_re_deployment 部署信息
act_re_procdef 流程定义的一些信息
act_re_bytearray 流程定义的bpmn文件及png文件
#背后影响的表：
act_hi_actinst 已完成的活动信息
act_hi_identitylink 参与者信息
act_hi_procinst 流程实例
act_hi_taskinst 任务实例
act_ru_execution 执行表

4) PPT 标题、架构图/流程图的结构、表格数据：
画面5：
标题：6.4 流程定义删除
内容：public void deleteDeployment() { ... } 方法代码，包含注释说明。
画面12：
标题：删除已经部署成功的流程定义
内容：public void deleteDeployment() { ... } 方法代码，包含注释说明。
画面9：
流程图结构：StartEvent → UserTask → EndEvent
元素面板：StartEvent, EndEvent, UserTask, ScriptTask, ServiceTask, ManualTask, BusinessRuleTask, SubProcess, Lane, ParallelGateway, ExclusiveGateway, InclusiveGateway, EventGateway, IntermediateCatchingEvent, IntermediateThrowingEvent。
画面13：
表格数据：包含 PROC_DEF_ID_, DEPLOYMENT_ID_, ACT_ID_, TASK_ID_, ACT_NAME_, ACT_TYPE_, ASSIGNEE_, START_, END_ 等列，显示了多行数据。

5) 无。

