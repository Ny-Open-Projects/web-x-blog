# 08-Activiti历史信息的查询

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\08-Activiti历史信息的查询_【海量资源尽在 ubkz.com】.mp4
- 时长 11分16秒（音频 676s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 关于流程定义各方面的内容包括它的部署查询以及我们的流程定义的删除流程资源的查看都给各位介绍了现在我们再一起来看一下我们的MySQL数据库表中的相关记录各位可以看到目前只有我们的HI开头的这一堆表中的数据我们还没有开始真正去查询过
[00:28] 我们的一个流程从开始到最后跑完结束这些相关的表中的记录其实我们将来都可以通过相关的Service来进行查看那我们原来在学习的时候已经给各位讲过这个activity的架构图通过这个activity架构图我们可以看到它有一个叫history Service那现在我们一起来使用一下history Service来实现我们
[00:56] HI开头的这一堆历史记录表中数据的查询那好现在我们呢按照这个大致的步骤我想去查询我们已经跑过的这个请假流程的像我们的这个ACT, INSTOS这一堆表中的相关数据那具体我们大致按一个什么样的步骤来走我们呢一起来学习一下首先第一个我们要用到的是我们的History Service来实现
[01:25] 我们的HI开头的这一堆表中数据的查询而这一次用的是用的是activity里头的historic Service的historic activity instance purely用这个查询对象来实现我们这个数据的查询那查询出来的这个结果呢我们是叫做historic activity instance后续我们就可以来遍历出它相关的这个
[01:54] 节点的名称以及ID等等一些数据下面我们开始编码来实现这个效果我们在这个D03Activity里头我们可以再去新建一个新的类比如说我这样做直接再去创建出一个类比如说我叫做历史我们的历史记录的一个查询HistoricQ类OK
[02:21] 下面我们就直接回到这个问题我们这一次主要完成的任务是叫做历史数据的查看刚才说了我们历史数据的查看主要在这里头用到的是哪个Service呢我们刚才说了应该用的是history叫Service是这一项这是第二个第三个这是
[02:46] 第一个步骤和第二个步骤第三个步骤我们要解决的是我们要得到一个相关的查询器我们这一次用的查询器是Historic Activity Instance Queue那现在我们就去写一下得到我们的叫做Historic Activity Instance Queue
[03:17] activity, use, terms, query得到一个这样的对象这是我们的第三个步骤第四个我们就可以执行执行我们的查询操作第五个我们可以去第五个步骤就是便利我们的查询结果这就是我们五个步骤下面我们就开始来得到我们的history Service我可以通过我们的process engine
[03:46] get historic Service就可以去得到一个historic Service好就得到它这是第二个步骤第三个步骤我们可以通过historic Service去创建出它的一个查询器叫做create historic activity用语同时cure对吧这样我们就可以得到一个
[04:16] Historical Activity Useful Theory得到一个这样的对象好这个对象主要就是去查询我们相关的这个流程它跑的一个历史记录那各位可以看到我这边呢将来这个表里头可以存放的是很多套不同的流程比如说目前我们只搞了一套请假的流程将来我们可以再去搞一套这个调感的流程还可以搞一套我们
[04:45] 薪资调整的流程这样的话我们的Arc的用途是表中就会有很多套不同的流程对吧那我们具体你要查询的是哪一套流程或者是具体的某一个流程实例那如果我们要根据流程实例去查的话那你就应该查这个对吧也就是说这个实例从开始到中间的每个环节到最后结束整个过程我想给它查询出来那我们就需要去设置它的这个查询的条件
[05:15] 这个查询条件怎么去设置我们可以通过HistoricActivityInstanceCurric比如说我们要去设置一个我们的流程实例的一个ID当然你可以是设置我们流程定义的ID这个部分就取决于我们自己去设置不同的条件你像我这里主要就是设置我们的流程实例的ID通过流程实例的ID我就可以
[05:45] 将我们之前所执行的这个流程实例的每一个执行过程都查询出来那好现在我们就可以把刚才这里头的2501的这个实例ID2501直接放进来好当我设置好这个条件那我们下一个环节就可以去执行我们的这个查询操作了那执行查询操作我们可以
[06:12] 再去调用我们的这个查询器中相关的方法对吧来执行这个查询操作在执行这个结果的时候呢我们可以针对整个这个结果啊做一个排序啊但你不排序呢也是可以输出的啊好我们假如说不去做任何的排序我们可以看一下啊点在这里头你就直接可以去调用它的类似的方法这样呢它就可以查到一个类似的列表对吧就是我们的叫做Historical Activity Instance这样的一个列表啊
[06:42] 那得到列表下一步我们就可以来实现我们的这个结果便利输出比如说我就可以通过我们的循环比如说historic就是我们的叫做historicalactivity instance去便利它比如说叫做instance冒号我们得便利的是我们的类似的结果那这时候我就可以来输出我们的这个相关的结果比如说instance.get
[07:10] 我就可以去把我们的这个activity id以及更多的其他信息都可以输出来比如说我们这个时候再去输出其他的输出其他的一些其他的一些内容比如说我们还可以去叫做get点我们的这个activity name把它的名字输出我们还可以去输出我们的这个实例的id以及比如说叫做get process
[07:39] definition id我们流程定义的id以及我们的实例id输出实例id我们可以去调用的是叫做.getProcessInstance id这样我们就可以去将我们2501的实例执行的每一个节点的信息都输出实现一遍在输出每一个之后我打算在这里头用一个
[08:08] 用一个这种杠格开一下好这时候我们就可以来运行跑一下效果好这时候各位就可以看到我们整个这个流程它跑下来它好像第一个节点展示出来的是我们的end event对吧然后是我们的这个start event然后是我们的填写请假单部门经理审核然后是总经理审核这时候我们会发现我们的这个end event它跑到第一个节点上去对吧
[08:41] 这个地方呢是我们可以进行调整的啊那如果我们要去调整的话我们就需要来看一下我们的数据库表啊在我们的这个act-instance表里头呢的确是我们的end event现在目前呢作为我们的第一个第一条记录出现的对吧那如果我要去给它进行调整的话那这个时候其实我们可以去思考一下啊因为我们的每个节点呢都有一个开始时间对吧这个开始时间呢其实是由start event开始的
[09:10] 然后再去执行我们的这个User Task对吧比如说我们的这个填写请假单然后是我们的这个部门经理进行审批以及总经理审批最后一个环节才会进入到我们的这个EventEnd Event这个节点所以这个时候我们可以针对我们的这个Start Time这一列为我们的这个记录来进行排序这样的话这个结果就会是我们预期的这个结果那好我们现在一起来学习一下
[09:40] 如果我在这里头要去排序的话我们就要加入一个叫做AutoBy的字短AutoBy我们是根据我们的StartTime来进行排序所以这个地方我可以把我们的StartTime给它加入进来根据StartTime的升序还是降序我们这个时候应该是应该是ASC不断的由时间点不断的小往后去走一直走到我们的end time
[10:08] 好这是我在这里头加入了我们的这个排序啊加入了排序是主要通过我们的这个start time来实现的啊好下面呢我们就继续看一下运行之后的结果啊好这时候我们可以看到啊这个时候开始节点的start event就作为我们第一个输出的节点啊然后是填写请假单然后是部门经理省总经理省最后一个节点才会是我们的end event对吧
[10:43] 这样我们基本上就完成了我们的这个流程在执行在执行结束后它的这个历史记录的一个查看目前为止应该说我们关于activity这里头很重要的这样的一些表的相关的操作我们大致上都给它介绍了一把主要就是通过各种不同的Service来实现我们的这个activity工作流引擎相关的这个
[11:13] 后续表的一个空字

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码查询 Activiti 工作流的历史实例数据，并在 MySQL 数据库中验证结果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 MySQL GUI 工具中查询到的 activiti 历史表数据，包含流程实例ID、执行ID、任务ID、活动名称等字段。
画面2：在 MySQL GUI 工具中，用户点击“刷新”按钮，重新加载数据。
画面3：切换到 IntelliJ IDEA 开发环境，显示项目结构和主界面。
画面4：在 IntelliJ IDEA 中打开 HistoryQuery.java 文件，代码中初始化 ProcessEngine 对象。
画面5：在 IntelliJ IDEA 中，代码光标位于 HistoryService 的声明处，准备获取历史服务。
画面6：在 IntelliJ IDEA 中，代码光标位于创建历史活动实例查询对象处。
画面7：在 MySQL GUI 工具中，用户点击“刷新”按钮，重新加载数据。
画面8：在 IntelliJ IDEA 中，代码光标位于创建历史活动实例查询对象处，准备执行查询。
画面9：在 IntelliJ IDEA 中，代码光标位于 for 循环中，准备打印历史活动实例的详细信息。
画面10：在 IntelliJ IDEA 中，右键点击代码，弹出“Copy Reference”菜单，准备复制方法或类。
画面11：在 IntelliJ IDEA 中，运行 HistoryQuery.java，终端输出历史活动实例的详细信息。
画面12：在 IntelliJ IDEA 中，代码光标位于设置流程实例ID处，准备执行查询。
画面13：在 IntelliJ IDEA 中，代码光标位于 for 循环中，准备打印历史活动实例的详细信息。
画面14：在 MySQL GUI 工具中，用户点击“刷新”按钮，重新加载数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```java
package com.ithema.day03.activiti;

import ...

public class HistoryQuery {

    public static void main(String[] args) throws IOException {
        //1.博学谷流程引擎对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博学谷历史服务
        HistoryService historyService = processEngine.getHistoryService();
        //3.博学谷历史实例查询对象
        HistoricActivityInstanceQuery historicActivityInstanceQuery = historyService.createHistoricActivityInstanceQuery();
        //4.执行查询
        List<HistoricActivityInstance> list = historicActivityInstanceQuery.list();
        //5.遍历查询结果
        for (HistoricActivityInstance instance : list) {
            System.out.println(instance.getActivityId());
            System.out.println(instance.getProcessDefinitionId());
            System.out.println(instance.getProcessInstanceId());
            System.out.println("==================");
        }
    }
}
```

画面6：
```java
//3.博学谷历史实例查询对象
HistoricActivityInstanceQuery historicActivityInstanceQuery = historyService.createHistoricActivityInstanceQuery();
//4.执行查询
List<HistoricActivityInstance> list = historicActivityInstanceQuery.list();
//5.遍历查询结果
for (HistoricActivityInstance instance : list) {
    System.out.println(instance.getActivityId());
    System.out.println(instance.getProcessDefinitionId());
    System.out.println(instance.getProcessInstanceId());
    System.out.println("==================");
}
```

画面11：
```java
2018-10-29 11:09:24,510 2516 [main] DEBUG wpl.interceptor.LogInterceptor - 
StartEvent
holiday114
2501

审批任务
holiday114
2501

结束任务
holiday114
2501
```

画面12：
```java
//4.执行查询
List<HistoricActivityInstance> list = historicActivityInstanceQuery.processInstanceId("2501");//设置流程实例的id
//5.遍历查询结果
for (HistoricActivityInstance instance : list) {
    System.out.println(instance.getActivityId());
    System.out.println(instance.getProcessDefinitionId());
    System.out.println(instance.getProcessInstanceId());
    System.out.println("==================");
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

