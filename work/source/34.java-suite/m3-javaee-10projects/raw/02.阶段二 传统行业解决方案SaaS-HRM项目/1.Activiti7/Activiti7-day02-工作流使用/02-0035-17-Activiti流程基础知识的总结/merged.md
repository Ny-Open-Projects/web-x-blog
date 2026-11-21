# 17-Activiti流程基础知识的总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\17-Activiti流程基础知识的总结_【海量资源尽在 ubkz.com】.mp4
- 时长 16分25秒（音频 986s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 各位同学,我们刚才就已经完成了我们以压缩包方式来实现我们的流程定义的部署现在我们先暂时一起来总结一下我们这一段时间所学的知识点我们一起来回顾今天我们主要学习的内容包括有这样的一些
[00:28] 第一个部分是我们对于activity对于我们的这个activity这个架构做了一个大致的说明对吧架构说明这个架构说明里头其中我们可以一起来回顾的话主要包括就是一个是我们的这个process engine configuration对吧这是一个具体的这个类它的主要作用主要作用
[00:59] 是加载我们的这个activity.cfg.xml这个配置文件对吧加载这个配置文件那除了这个类呢我们在这个架构图里头咱们还可以看到有一个重要的类我们也可以一起再回顾看一眼看一眼还有一个重要的类就是叫做我们的process engine对吧那这个时候叫做process engine
[01:25] 这个代表的是我们的一个流程引擎对吧流程引擎的这个类那有了它之后它的作用是什么它的作用作用是帮助我们可以快速得到谁呢得到我们的Google Service接口对不对Google Service接口Google Service接口并且并且
[01:57] 可以的生成activity的工作环境对吧activity的工作环境那有的会思考什么是activity的工作环境呢对吧那我们啊在前面给各位说过啊25张表对不对25张表那你一定啊在创建我们的process engine之后这25张表一定啊已经完成了这个生成对不对必须要生成好
[02:24] 要不然的话我们的activity将来去实现我们的这个业务的这个流程定义图读取过过节点的时候你连后台的数据库表都不存在的情况下那我们读取出来的这些节点以及我们的这些BPMN文件和我们的PNG文件这些文件的内容往哪个表里头存都不知道对吧所以这个时候我们呢
[02:53] Process Engine这个类一旦创建出它的对象那我们将来就可以很轻松的得到各个Service接口的实力并且可以生成我们Activity的工作所需要的全部的环境好那后面我们又给各位在介绍体系结构的时候给各位说了我们的Service接口对吧那这个Service接口其中我们当时讲到的重要的Service接口有四个
[03:22] 那我们一起来看一下我们Service接口的主要作用是什么有了这一堆Service接口作用是可以快速实现数据库数据库这25张表25张表的25张表的操作这样的话
[03:47] 我们activity在工作的时候我们程序员就不需要自己针对这25张表再去搞什么domain DAO以及它的Service对吧一些业务方法这些业务方法我们不需要搞了原因是我们的activity已经给我们提供了这样的一些Service方法但要注意的是我们的最新的版本里头identity serviceform Service
[04:16] 这两个Service已经没有了这个我们同学需要了解一下当然我们很多同学在使用这个activity的时候跟着我在这边的学习的时候用的是我们目前activity 7是它的最新版本当我们用的时候很多公司用的还是5和6这一点要跟各位说明因为7呢
[04:45] 我说了它是2018年9月份才产生了7这个版本应该是9月20号以后了才产生这个版本所以我们这边才真正发布出这个版本我们再回到我们的回顾动态一起来回顾一下既然有了这一堆Service接口我们就可以很方便的去操作我们的这些这25张表对吧让我们一起来看一下
[05:13] 那真正对应的这个Service呢主要包括有repositoryrepository Service这是其中一个Service这是我们关于部署相关的一个Service结构对吧我们还有像我们的这个runtime你部署完了将来我们流程实例一起动我们对应的就会用到相关的这个runtime Service我们还有一个Service就是我们的这个
[05:42] 就是我们的这个Task ServiceTask Service这就是当你一启动对于每个不同的用户它就有自己的任务所以我们这个时候就有一个Task Service那最后我们呢如果想去查看我们的很多历史记录那我们就会有一个History Service要注意啊我们目前演示的这个事例里头啊我们还没有啊去给各位展示History Service的具体用法这个各位不用担心啊
[06:11] 我们在后面的过程里头肯定会给各位去涉及到我们的history Service这就是我们这边关于体系结构的一堆Service的介绍重点就是这几个当我们把这个Service给各位也介绍清楚我们下一步就开始给各位讲了一下我们的这个我们的这个process engine怎么去创建对吧以及我们的这个Service接口每一个接口它的主要作用
[06:41] 那再往后走了我们就开始要去做我们的这个流程定义图对不对流程定义啊那我们这边主要使用的是使用的是我们的这个ideal工具带的这个activity插件对吧所以我们下一个工作就是给各位介绍了我们的这个BPMN的BPMN的叫做activityactivity叫做design
[07:11] 第三呢这个插件对吧这个插件那有了这个插件我们呢其实啊将来再去再去画我们的这个业务流程的时候啊画这种流程定义的时候那我们基本上就可以做得更加漂亮一些对吧但是我们呢在这里边啊要为了使得有这个插件我们这边呢也特别给各位讲了一下就是我们的这个ideal
[07:40] ideal工具中我们安装我们的这个activityactivitydesigner的一些注意细节比如说我们很多时候咱们同学如果按照这种传统的套路你去安装的话应该说这个activitydesigner你都不一定能装上于是我们在这里头给各位讲了一下你可能需要去借助于一些
[08:10] 翻墙软件来做到这个效果这是一个点然后呢我们当我们把这个activity designer这个工具安装好了之后那下面呢我们就需要去自己画出使用我们的这个BPMN的符号画出我们的这个流程定义对吧流程定义图当我们把这个流程定义图画好了于是第四个环节就来了
[08:39] 那你画好了我们下一个环节就可以去部署我们的这个流程定义对吧部署我们的这个流程定义那我们思考一下昨天我们在部署的时候我们是怎么部署的呢对不对那我们目前来看啊部署呢方式一方式一的话是使用我们的这个单个文件对吧单个文件主要对于我们来说就是把BPMN文件和我们的这个PNG文件对吧
[09:07] PNG文件直接部署到我们的这个activity里头去那方式二我们这是刚刚讲完的方式二那是通过什么方式呢是通过先将我们的先将我们的这个BPMN文件以及我们的这个PNG文件先压缩压缩压缩成我们的这个zip文件对吧
[09:37] 我当时也给各位讲了我们为什么要这么做因为你想将来如果说流程定义的图流程定义的图比如说是我们公司的人事或者是行政搞了一套这样的流程定义的图那这个流程定义的图就需要上传到我们的服务器上对吧那这个时候上传到我们的服务器那这个时候我们要借助于文件上传
[10:06] 文件上传如果说你两个文件分开传的话这个地方就涉及到PNG文件和我们的BPMN文件分别都要做文件上传这个时候你要么就用要么就使用我们的多文件上传这个时候操作起来就还不如我们提前打这幅文件搞一个这幅文件然后我们再把这幅文件以一个文件的方式上传到我们的服务器这样
[10:36] 我们的这个文件上传的环节就会变得更加简单而我们昨天呢给各位展示效果的时候呢我们虽然是以这一部文件方式上传过去的但是我们的这个activity最终也是以单个文件形式保存对吧也是以单个文件形式保存说明我们的这个activity会进行几样说明activity
[11:04] 进行了解压对吧进行了解压工作然后呢解压完了再把解压之后的这个文件给我存进去那我们在实现这个流程部署一套流程定义的时候我们还记得吗当时我们在这个地方用到了有一个专门的叫做我们的部署叫做Repository Service对吧所以这个时候我们用的是Repository Service这个接口中提供出来的一套方法对不对
[11:32] 比如说我们在早期实现当过文件上场的时候我们用的是Repository Service里头的叫做Create Deployment对吧这是我们关键的代码对吧然后再去走Add Class Path这一段就是我们在实现我们的部署的工作的时候最为重要的一个环节对吧那就是这样的一个工作当我们部署好了那下一个环节我们就开始说我们用户可以去查询对吧
[12:01] 好于是我们进入到下一个环节下一个环节下一个环节我们具体是怎么搞的我们可以一起来看一下当我们的流程部署好了我们下一步就可以来启动我们的流程实例对吧启动流程实例我们这个时候用的是叫做run time Service启动流程实例最关键我们用的是run time Service然后再去调用它的start process用试同时by key是不是这样我们就启动了一个流程实例
[12:33] 所以呢我们进一步就一起来观察一下就是我们的这个叫做啊启动启动一个流程实地这个工作那如何去启动我们主要用到的是run time Service对吧那这个run time Service我们刚才在这里要看了啊用的是它里头的一个叫做startstart processstart process叫做我们再看一下啊叫start process用词统是by key是不是啊start
[13:02] process use by key这里边我们就要把我们的流程实例的流程定义的唯一的key你就要写到这个样子这样我们就完成了一个流程实例的启动我启动完了下一步我们就可以去应该说可以去做这个工作了比如说我这里要把第6个步骤加入进来第6个步骤我就可以去查看对吧
[13:32] 查看任务对吧查看任务那查看任务的时候我们这个地方用到了一个新的这个Service这个Service就是我们的叫做叫做task Service这样我们就可以去看任务了所以在查看任务的时候我们主要用的是我们的这个task Service那task Service我们将来要去看这个用户是否有自己的任务
[14:01] 那我们主要就是啊用的一个叫做collate task query的方法对不对来执行我们具体的这个查询所以呢这边就这么做的那我们再往后往后走呢就是我们的这个第七个任务了对吧我们的第七个任务是什么呢对吧我们的这个第七个任务就是当我查看到有自己任务的时候于是我们要完成任务对不对或者要处理任务那我们怎么去处理任务
[14:31] 这个人其实还是用task Service还是用这个我们一起看一下这边有我们completed task完成一个任务各位可以看到他还是用task Service但是在这里头主要用的是complete的方法所以我们在这边再拿个来这就是我们还需要借助于我们的task Service但是我们这里头真正用的方法是我们的complete的方法
[14:59] 里头写的就是我们的这个任务ID对吧任务ID这里面是任务ID那这个呢这个呢我们写一下参数为我们的这个任务ID这样呢我们基本上就完成了整个这一次课程我们大致所介绍的这个内容再来看的话我们的重点内容给各位梳理完之后应该说各位同学应该感受会好一些
[15:28] 我再说一说当时我在学activity的时候我最大的感受就是感觉这个东西不是那么好学原因是啥呢原因是我当时学的时候没有一个完整的体系结构还有一个就是这一堆Service背后它在这里头真正到底起了什么作用我当时不是像现在这么明朗
[15:54] 那我们现在可以告诉各位这一堆Service或者说这些process engineconfiguration提供的这样的一些类或者是里头的这样的一些方法它的主要作用就是帮助我们去更加方便的去操作我们背后的这25张表对吧让我们将来去实现这个activity工作流程管理的时候让我们尽可能的去减少我们的这个编写代码的工作量这是我自己过程的一些见解
[16:24] 好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Activiti 工作流引擎，通过 Java 代码部署 BPMN 流程定义、启动流程实例、查询并完成任务。

2) 按时间顺序列出每张画面的要点：
画面1：打开一个空白的 Word 文档，准备编写说明文档。
画面2：在 IntelliJ IDEA 中打开 activiti01 项目，展示 ActivitiCompleteTask.java 文件内容，包含获取 ProcessEngine、TaskService 的代码。
画面3：在 Word 文档中输入“Activiti的架构说明”等文字，介绍 ProcessEngine、RepositoryService、RuntimeService、TaskService。
画面4：在 Word 文档中继续输入内容，同时弹出一个小型窗口，显示一个文本编辑器。
画面5：在 Activiti Designer 中展示 holiday.bpmn 流程图，包含 StartEvent → 请假申请审批 → 通知领导 → EndEvent。
画面6：在 Activiti Designer 中，对流程图进行编辑，调整“通知领导”节点的文本。
画面7：在 Activiti Designer 中，对流程图进行编辑，调整“通知领导”节点的文本。
画面8：在 IntelliJ IDEA 中展示 ActivitiDeployment.java 文件内容，包含部署流程定义的代码。
画面9：在 IntelliJ IDEA 中展示 ActivitiStartInstance.java 文件内容，包含启动流程实例的代码。
画面10：在 IntelliJ IDEA 中展示 ActivitiStartInstance.java 文件内容，包含启动流程实例的代码。
画面11：在 Word 文档中继续输入内容，列出 Activiti 的核心接口和部署流程的代码。
画面12：在 IntelliJ IDEA 中展示 ActivitiCompleteTask.java 文件内容，包含获取 TaskService、查询任务、完成任务的代码。
画面13：在 Word 文档中继续输入内容，列出 Activiti 的核心接口和部署流程的代码。
画面14：在 Word 文档中继续输入内容，列出 Activiti 的核心接口和部署流程的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2：
```java
package com.ithema.activiti;

import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.task.Task;

/**
 * 处理当前用户的任务
 */
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService服务
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户的任务
        Task task = taskService.createTaskQuery()
                .processDefinitionKey("holiday")
                .singleResult();
        //4.处理任务
        taskService.complete(task.getId());
    }
}
```

画面8：
```java
public static void main(String[] args) {
    //1.获取ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到RepositoryService服务
    RepositoryService repositoryService = processEngine.getRepositoryService();
    //3.读取InputStream流
    InputStream is = ActivitiDeployment.class.getClassLoader().getResourceAsStream("diagram/holiday.bpmn");
    ZipInputStream zipInputStream = new ZipInputStream(is);
    //4.部署流程定义
    Deployment deployment = repositoryService.createDeployment()
            .addInputStream("holiday.bpmn", zipInputStream)
            .name("请假申请流程")
            .deploy();
    System.out.println("部署ID：" + deployment.getId());
}
```

画面9：
```java
public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到RuntimeService服务
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.创建流程实例
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
        //4.输出流程相关参数
        System.out.println("流程部署ID：" + processInstance.getDeploymentId());//null
        System.out.println("流程定义ID：" + processInstance.getProcessDefinitionId());//holiday:1:4
        System.out.println("流程实例ID：" + processInstance.getId());//2501
        System.out.println("活动ID：" + processInstance.getActivityId());//null
    }
}
```

画面12：
```java
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.task.Task;

/**
 * 处理当前用户的任务
 */
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService服务
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户的任务
        Task task = taskService.createTaskQuery()
                .processDefinitionKey("holiday")
                .singleResult();
        //4.处理任务
        taskService.complete(task.getId());
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面5：流程图结构：
StartEvent → 请假申请审批 → 通知领导 → EndEvent
画面6：流程图结构：
StartEvent → 请假申请审批 → 通知领导 → EndEvent
画面7：流程图结构：
StartEvent → 请假申请审批 → 通知领导 → EndEvent
画面11：PPT 内容：
1. Activiti的架构说明
   - ProcessEngineConfiguration：主要作用是加载activiti.cfg.xml配置文件
   - ProcessEngine：作用是获取RuntimeService、RepositoryService、TaskService等服务
   - RepositoryService：作用：可以完成流程定义的部署
   - RuntimeService：作用：可以启动流程实例
   - TaskService：作用：可以完成任务的查询、完成
2. BPMN流程图
   - 用 Activiti Designer 工具绘制
3. 部署流程定义
   - 方式一：多个文件（.bpmn、.png文件）
   - 方式二：单个文件（.zip文件）
   - 用 Activiti 最终是以单个文件的形式部署，用 repositoryService 进行了部署工作
   - Deployment deployment = repositoryService.createDeployment()
           .addClasspathResource("diagram/holiday.bpmn") // 添加bpmn流程
           .addClasspathResource("diagram/holiday.png") // 添加png图片
           .name("请假申请流程")
           .deploy();
4. 启动流程实例
   - RuntimeService startProcessInstanceByKey("key")
5. 查询任务
   - TaskService taskService.createTaskQuery()
6. 完成任务
   - TaskService taskService.complete(task.getId());//参数为任务ID

5) 不要评价画面美观，不要输出与课程无关的内容。

