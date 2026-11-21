# 02-Activiti系统体系架构图

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\02-Activiti系统体系架构图_【海量资源尽在 ubkz.com】.mp4
- 时长 6分0秒（音频 361s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们把这个表结构的这个规范说清楚之后我们下面就再次回到我们的这个程序代码还是这一段对吧这一段本身是比较简单的那我们现在一起来看一下如果我们的表结构也生成出来了那我们下面也有了这个process engine的这个流程引擎的这个对象对不对那下面其实我们要做的工作就是就是要保证我们的这个流程可以接着一步一步往后去
[00:29] 跑起来对吧那我们的流程又能够跑起来呢在activity里头它后面就会提供很多相关的这个类来为我们提供各种各样的服务所以呢我们现在可以一起给各位来介绍一下我们的这个activity的这个服务架构图这个服务架构图里头将我们的这个activity整个提供的这一堆服务给咱们做了一个大体的描述
[00:57] 那你可以看到整个这个服务里头我们刚才已经完成了哪些工作呢像我们的activityconfigure.xml这个作为我们activity的配置文件以及我们的这个processengineconfiguration作为我们的这个流程引擎的一个配置的类对吧而由我们的这个processengineconfiguration产生出来的processengine那这个类的实例其实我们刚才已经得到了对吧已经得到了一个processengine的对象
[01:25] 那于是下一步我们就可以通过Process Engine去得到过种各样的服务那这些服务对于我们其实也非常简单假如说我们现在还要往后续去写的话其实这个过程也就是很简单的我们这个时候就可以去get你会得到一堆Service你可以看到有一个叫Dynamical BPM ServiceGet History Service以及我们Get Management Service
[01:51] 还可以有很多啊比如说Repository ServiceLong Time ServiceTask Service对吧这都是我们在这边给各位啊可以得到的各种各样的Service服务那有了这些Service服务将来我们后续的这些工作呢就可以开场了对吧比如说我们可以用如果我要查找历史信息我就可以用History了对吧如果我要查找我们的Repository就是我们的这个部署信息我就可以用Repository
[02:21] 如果我要去得到我们运行整个运行的状态对吧我就可以用long time我想查询某个用户的任务比如说作为张商张商目前他的任务是要做什么那我就可以用task Service这就是大致上我们在这里头将来可以通过我们的process engine提供出来的过总管的服务来帮助我们解决我们想要做的事情那刚才我们在这所说的这个
[02:50] 所说的这个Gate Service我再简单给各位引申一下吧比如说GateHistoryService那这个时候我就可以拿到我们的历史记录的信息对不对那具体的这个时候它的返回值就应该是一个就应该是一个History的Service我们可以直接加进来那这样我们就有一个History的Service了那HistoryService将来它的本质是在做什么工作呢对吧我们拿到HistoryService之后
[03:19] 它真正的本质就相当于给我们提供了一套操作这些表的一个接口就相当于这些表将来你不都得去做这些表里头的查询一些历史信息比如说这些历史信息我想查出来那我应该怎么去做呢那正常有时候就会思考那我就直接自己搞这个表的DAO我把这张表的domain写出来然后我再去写这张表的DAO
[03:47] 再去写这张表的Service好了于是对于这张表的增伤改查将来我都提供过整各样的方法那你去调用这个其实你这个思考是没错的但是我们用了activity之后呢这些表的增伤改查的这些操作啊很明显不是由我们自己去一个一个写如果这些表的增伤改查操作还有我们自己一个一个去写domain DAO和Service的话那你想想我们还有必要用activity吗
[04:17] 对吧我们还有必要用它吗因为我们用它的主要目标就是希望我们的这一堆表的后续的操作将来都不需要我们自己单独去维护对不对而是它提供专门的Service就可以让我们直接去用比如说我们要操作runtime要操作runtime也很简单我们只需要在这个地方用我们的process engine直接去调用good runtime Service这样的话
[04:47] 我们就可以拿到一个Runtime的serviceRuntime的Service将来就可以把背后的RU开头的这样的一堆表的相关的操作都给我们干完了明白是吧那我们将来相当于只要再去调用的话只要调用我们的Runtime serviceRuntime Service调用它调用它里头的一些方法那这些方法将来就可以背后把这些表的相关操作给我们干完了明白吗
[05:14] 这样我们是不是就大大的节约了我们对于这些表的相关的增长改查操作这也是我们用activity主要目标是让我们的流程管理变得更加简单而不是引入25张表让我们一看感觉都懵了大概就是这个意思所以我们在这边刚才给各位介绍的像Repository ServiceTask Service以及我们的Management ServiceRuntime Service
[05:43] Historic Service这样的一些Service这是我们大概心里的有个数通过这一堆Service我们就可以很轻松的去实现我们后面的这一堆表的相关的操作从而来实现我们流程控制

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码获取 Activiti 流程引擎的各个服务对象，并通过数据库查询验证其对应的表结构。

2) 按时间顺序列出每张画面的要点：
画面1：在 MySQL Workbench 中，选中 act_hi_procinst 表，查询语句为 "1"，显示了该表的字段结构。
画面2：在 IDEA 中，展示 ActivitiTest.java 文件，代码用于创建 ProcessEngineConfiguration 并构建 ProcessEngine 对象。
画面3：IDEA 中，代码高亮显示创建 ProcessEngineConfiguration 的部分，注释说明了配置文件路径。
画面4：PPT 展示了 Activiti 的架构图，ProcessEngineConfiguration 指向 activiti.cfg.xml，ProcessEngine 指向 RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService。
画面5：IDEA 中，代码高亮显示 ProcessEngine 对象的创建部分。
画面6：IDEA 中，通过 ProcessEngine 对象调用 getDynamicBpmnService() 方法，弹出方法列表。
画面7：IDEA 中，光标在 ProcessEngine 对象后，准备调用方法。
画面8：IDEA 中，弹出方法列表，选中 getHistoryService() 方法。
画面9：IDEA 中，光标在 getHistoryService() 方法后，准备调用。
画面10：IDEA 中，代码高亮显示 processEngine.getHistoryService() 方法调用。
画面11：IDEA 中，代码高亮显示 HistoryService historyService = processEngine.getHistoryService(); 的完整语句。
画面12：在 MySQL Workbench 中，选中 act_hi_procinst 表，查询语句为 "domain---dao---Service"，显示了该表的字段结构。
画面13：PPT 展示了 Activiti 的架构图，ProcessEngineConfiguration 指向 activiti.cfg.xml，ProcessEngine 指向 RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService。
画面14：在 MySQL Workbench 中，选中 act_hi_procinst 表，查询语句为 "domain---dao---Service"，显示了该表的字段结构。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2代码：
```java
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngineConfiguration;
import org.junit.Test;

//测试类
//作用：测试Activiti引擎需要的25张表的生成
public class ActivitiTest {

@Test
public void testGenTable(){
    //1.创建ProcessEngineConfiguration对象  第一个参数：配置文件名称  第二个参数是processEngineConfiguration的
    ProcessEngineConfiguration configuration = ProcessEngineConfiguration
            .createProcessEngineConfigurationFromResource("activiti.cfg.xml", beanName: "process"
    //2.创建ProcessEngine对象
    ProcessEngine processEngine = configuration.buildProcessEngine();
    //3.输出processEngine对象
    System.out.println(processEngine);
}
}
```

画面6代码：
```java
public void testGenTable(){
    //1.创建ProcessEngineConfiguration对象  第一个参数：配置文件名称  第二个参数是processEngineConfiguration的
    ProcessEngineConfiguration configuration = ProcessEngineConfiguration
            .createProcessEngineConfigurationFromResource("activiti.cfg.xml", beanName: "process"
    //2.创建ProcessEngine对象
    ProcessEngine processEngine = configuration.buildProcessEngine();
    //3.输出processEngine对象
    System.out.println(processEngine);
}
```

画面11代码：
```java
HistoryService historyService = processEngine.getHistoryService();
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面4 PPT标题：4.1 activiti.cfg.xml
架构图结构：
- ProcessEngineConfiguration 指向 activiti.cfg.xml
- ProcessEngine 指向 RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService

画面13 PPT标题：4.1 activiti.cfg.xml
架构图结构：
- ProcessEngineConfiguration 指向 activiti.cfg.xml
- ProcessEngine 指向 RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService

5) 无。

