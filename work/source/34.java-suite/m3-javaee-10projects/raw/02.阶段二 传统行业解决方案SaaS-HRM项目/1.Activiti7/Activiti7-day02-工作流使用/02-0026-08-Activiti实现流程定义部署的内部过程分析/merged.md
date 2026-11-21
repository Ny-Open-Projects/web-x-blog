# 08-Activiti实现流程定义部署的内部过程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\08-Activiti实现流程定义部署的内部过程分析_【海量资源尽在 ubkz.com】.mp4
- 时长 7分27秒（音频 447s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那下面呢我们就接着来分析一下我们的这个流程定义的部署当它完成之后我们真正背后所影响的这个activity的activity的表对吧,的表有哪些这个就是我们要一起深入来分析那怎么样来分析呢我们这个时候可以打开在这边我们的这25张表对吧
[00:29] 其实很简单的步骤就是咋了这些表呢初始状态下我可以告诉各位这些表初始状态下大多数的表都是空表就是表里头没有任何的数据当我们这个工作一旦做完之后如果这个表里头现在有记录了那是不是就说明我们对应的这个工作所起到的效果就是像这个表中插入了一条记录啊所以通过刚才给各位讲的这个思路呢
[00:58] 我们就可以来观察我们的 ACTRE Deployment 的这个表就是我们会多出一个我们的这个部署信息的这个数据除了这个表我们在这边再来观察一下我们的这个Modem表目前可以看到Modem表没有记录我们的这个流程定义的表就是这张表叫 PROC DEF这张表各位可以看到
[01:28] 它其实也多了一条记录而且呢把我们的这个请假流程名字以及我们的这个key啊应该说每一个流程定义都有自己的一个唯一的key是不是因为比如说你请假流程有请假流程的这个key比如说我这个是调薪那就有调薪的这个key啊那现在我调岗位对吧就有调岗位的这个key啊所以这一点呢我们要知道的就是
[01:59] 在我们的这个流程定义的表中它的这个key将来是我们唯一去识别不同流程的一个唯一的关键字这一点呢各位是要知道的除了这两张表的除了这两张表里头有数据那我们还有别的表吗我们一起接着来分析那这一堆表呢这个里头没有数据
[02:27] 这一堆表是我们history是我们的一些历史信息应该说在目前我们找一下你看看这些表这些表中目前这些表都是空表因为还没有我们的流程实力执行真正的一个环节比如说部门经理审核整经理审核财务经理审核将来这样的一些历史数据肯定现在还没有产生这两张表是各位要
[02:56] 值得关注的一个是我们的这个actge byte array这张表各位可以看到它把我们刚才所发布的这个dgram的holode png以及我们的dgram的holode bpmn这两个文件呢给我们保存到我们的这个activity的byte array这张表中来了
[03:26] 那我们也可以看一下各位现在咱们就可以看到了吗这个就可以看到了这是我们的真正的这张图片对吧它已经通过通过我们的这个自截流的方式给它存录到我们的这个activity的bat array这张表中来那我们这边还有一个BPMN文件同样可以告诉各位我们的BPMN文件
[03:56] 也存储过来了我们回来看一下因为我说了BPMN文件你别看在我们的这个activity在这里边BPMN文件在我们的这个ideal工具中BPMN文件是表现为一个真正的图案但其实它的本质就是一个axml对不对这一点我们之前也分析过了现在我们再回到这个回到我们的这个MySQL数据库的
[04:25] Bitrate这张表中各位也可以感受到它其实本身就是一个XML文件所以真正我们这边也把这个XML文件给你存进来了这就是我们做的这个部署已经影响到的三张表对吧那我们再来看这张表那这张表其实早期一上来它本身就有一个就有一个它的这个版本的数据所以这个数据不是我们说要部署的时候才会使得这个表中有数据
[04:55] 这个表是提前只要你25张表一产生这个表中一上来就会有我们的这个activity本身的这个版本的一些信息所以我们这一次真正部署的时候影响的表应该是三张表对吧那好我们再回到我们这边来那这样我们这一次真正影响的表就是这三张表那这三张表各位每张表我们所起到的一个作用对吧那各位其实应该
[05:24] 是要知道的那这个地方主要是我们的这个部署部署信息对吧比如说部署的ID以及我们的这个部署名称对吧那这个部分主要就是我们的这个流程流程定义流程定义的一些信息比如说我们的这个流程定义的唯一的key是不是依他的名字而我们的这个battery这里面主要就是我们的这个流程定义的两个图对吧流程定义的
[05:54] 定义在我们的BPMN文件及我们的这个PNG文件这俩图会给我们放到这里头去好各位现在如果我们再去思考的话应该说我们就能够得到一些启发这些启发就是我们借助于Repository Service我们就可以很快速的完成这三个表的相关的操作对不对那你想一想如果没有这个Repository Service
[06:22] 去提供这样的一些方法那你想想我们要去使得这几张表中有数据的话应该说我们要写大量的这个加码代码才可以实现这个效果这就是我们为了减缓我们的这个工作流开发使用activity其实还是很值得的虽然说我们在学习这个activity的时候要去掌握的内容是比较多的就相当于我们要把activity学好
[06:51] 那我们在这边呢对于它25张表以及它执行的过程原理性的内容我们都得有一个大概的了解对吧要不然的话这25张表其实有很多表你是驾驭不了的对吧那你肯定就不能说我把这个activity完全学好了对吧这个部分我们呢大致就给各位啊分析了一下我们的activity做流程定义的部署的时候部署的时候
[07:19] 我们背后所影响的每一张表及这张表真正的作用给各位整理了一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码部署一个 Activiti 工作流流程定义（BPMN 文件）到数据库中。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 ActivitiDeployment.java 代码，其中创建 ProcessEngine 实例并获取 RepositoryService，然后调用 createDeployment() 方法，添加 BPMN 文件和 PNG 图片资源，最后调用 deploy() 方法部署流程定义。
画面2: 在 MySQL Workbench 中执行 SQL 语句，先删除名为 'activiti' 的数据库，然后创建同名数据库。
画面3: 在 MySQL Workbench 中，选中了 'act_re_procdef' 表，准备查看或操作流程定义相关数据。
画面4: 在 MySQL Workbench 的 "Import/Update Blob Field" 窗口中，显示了 BPMN 文件的 XML 内容，其中包含多个 <bpmn:SequenceFlow> 和 <bpmn:StartEvent> 等元素。
画面5: 在 IntelliJ IDEA 中，显示了 BPMN 图形化流程图，包含 StartEvent、用户任务、服务任务和 EndEvent，流程从 StartEvent 开始，依次经过三个任务，最后到达 EndEvent。
画面6: 在 MySQL Workbench 的 "Import/Update Blob Field" 窗口中，显示了 BPMN 文件的 XML 内容，其中包含多个 <bpmn:SequenceFlow> 和 <bpmn:StartEvent> 等元素。
画面7: 在 IntelliJ IDEA 中，显示了 BPMN 图形化流程图，右侧是 BPMN 元素库，包括 StartEvent、EndEvent、UserTask、ServiceTask 等。
画面8: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中导入了 org.activiti.engine.repository.Deployment 包。
画面9: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。
画面10: 在 MySQL Workbench 中，执行 SQL 语句，创建了 'activiti' 数据库，并查询了 'act_re_procdef' 表，显示了部署的流程定义信息。
画面11: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。
画面12: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。
画面13: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。
画面14: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
public class ActivitiDeployment {
    public static void main(String[] args) {
        //1.创建ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService实例
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.进行部署
        Deployment deployment = repositoryService.createDeployment()
                .addClasspathResource("diagram/holiday.bpmn") //添加BPMN配置
                .addClasspathResource("diagram/holiday.png") //添加图片
                .name("请假申请单流程")
                .deploy();
        //输出部署的一些信息
        System.out.println(deployment.getName());
        System.out.println(deployment.getId());
    }
}
```

画面2:
```sql
drop database activiti;
create database activiti;
```

画面4:
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<bpmn:definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:activiti="http://activiti.org/bpmn" xmlns:flowable="http://flowable.org/bpmn" id="Definitions_1" targetNamespace="http://www.omg.org/spec/BPMN/20100524/MODEL" typeLanguage="http://www.omg.org/spec/BPMN/20100524/MODEL" expressionLanguage="http://www.w3.org/1999/xpath">
  <bpmn:startEvent id="StartEvent_1" name="StartEvent" />
  <bpmn:userTask id="UserTask_1" name="请假申请" />
  <bpmn:serviceTask id="ServiceTask_1" name="审批" />
  <bpmn:endEvent id="EndEvent_1" name="EndEvent" />
  <bpmn:sequenceFlow id="SequenceFlow_1" sourceRef="StartEvent_1" targetRef="UserTask_1" />
  <bpmn:sequenceFlow id="SequenceFlow_2" sourceRef="UserTask_1" targetRef="ServiceTask_1" />
  <bpmn:sequenceFlow id="SequenceFlow_3" sourceRef="ServiceTask_1" targetRef="EndEvent_1" />
</bpmn:definitions>
```

画面10:
```sql
drop database activiti;
create database activiti;
act_re_deployment
act_re_procdef
act_ge_bytearray
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面7: BPMN 元素库，包含 StartEvent、EndEvent、UserTask、ServiceTask、ManualTask、BusinessRuleTask、CallActivity、ReceiveTask、BoundaryEvent、EventGateway、SubProcess、Lane、ParallelGateway、ExclusiveGateway、InclusiveGateway、IntermediateCatchingEvent、IntermediateThrowingEvent、Annotation 等元素。

5) 无。

