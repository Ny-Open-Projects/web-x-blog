# 01-Activiti流程定义信息查询

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\01-Activiti流程定义信息查询_【海量资源尽在 ubkz.com】.mp4
- 时长 14分31秒（音频 871s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 现在我们一起再来学习我们的流程定义的查询我们刚刚已经把流程定义的部署已经给各位说完了对吧也对我们前面所学的这些activity从它的架构到我们的流程定义的部署实力的启动任务的查询以及任务的处理这些任务都已经完成了
[00:28] 那么下一步就开始来做这个流程定义的查询流程定义的查询能够起到一个什么样的作用因为很多时候我们都想去看一看我们的这个流程定义相关的一些资源信息比如说我想去看一下我们的这个流程定义的ID名称以及它目前的版本对吧那这些我们就可以借助于查流程实例的定
[00:56] 查我们的一个流程定义信息那就可以直接解决解决这个问题啊尤其是我们想查我们流程定义的这两个图对吧就是我们的BPMN和PNG这两个图的时候那我们这个时候就可以借助于我们去查询我们的这个流程定义信息啊就可以解决啊查询我们的这个流程定义信息那下面我们就开始来讲这个流程定义信息按什么样的步骤去查啊
[01:27] 第一个我们在这边呢还是要得到我们的这个Repository Service通过Repository Service去创建一个查询的对象叫做流程定义的查询对象Process Defining Curric的对象再去通过我们的这个设置CurricProcess Defining Curric的这个条件完了我们就可以来实现这个列表的查询最后我们去便利这个列表就可以展示数据了
[01:57] 当然各位注意啊我们讲到目前呢一直都是直接在这里头展示数据来测试看效果对吧但是我们最终啊肯定会去把我们的这些数据将来如果说我查询出这一堆内容肯定是需要交给我们的这个页面去展示对吧所以呢目前我们只是为了去简化我们的这个页面开发啊我们就直接在控制台
[02:25] 去展示我们的这个流程流程定义的一些基本信息这样我们基本上给各位把这个大字情况就说完了那下面我们就编写代码来实现我们的这个流程定义的基本信息的查询好那这样我在这边再去创建一个再去创建一个新的package我到这里面再去留一个新的package
[02:56] 然后叫做com.it黑码比如说叫做d03然后叫做activitactivities然后点ok这样我们这边就多了一个新的目录对吧然后在这个里头d03里头有个activities我们再去创建一个类再去创建一个类比如说这个地方我一样的再去创建一个
[03:25] 是我们查询我们的这个流程定义对吧比如说叫做curry我们的这个流程process叫做定义dfimitndefinitioncurry process definitionok这样呢我们就有了一个专门去去查询我们的这个流程流程定义相关的信息这个就叫做查询我们的流程定义信息好
[03:54] 具体按照一个什么样的步骤来做这个查询呢对吧那我们还是按这个按这个这个最最基本的这个步骤来啊首先呢不管怎么样我们一定是需要去拿到我们的这个process engine的这个对象对吧好这边我还是啊直接呢扔到我这里头来这是我们的第一个步骤就做完了当我们有了这个process engine啊我们接着再去往后走一下这个大体的步骤啊
[04:22] 那我们这一次要去查询我们的这个流程定义的基本信息那我们这个地方用的是什么样的一个Service呢对吧那这个部分我们可以啊再来看一下用的是reported Service对吧这就是我们第二个工作要做的那就是去创建我们的创建我们的叫做repository创建我们的reported Service的对象
[04:48] 有了Repository Service的对象第三个工作我们要创建一个查询器对不对那这个查询器主要就是去查询我们的这个叫做流程定义的信息对吧这个名字应该是叫做得到我们的叫做流程叫做Process叫DefintmProcess Defining Q里的一个对象
[05:14] 当我得到这个对象下一步我就可以去第四个步的设置条件并查询出当前的所有流程实例所有流程定义这个地方各位可以看到假如说我们一个公司里头设置的流程信息流程定义信息有十套比如说有请假的一套流程有我们的调感的一套流程
[05:42] 有我们薪资调整的一套流程对吧比如说我们有我们员工员工培训的一套流程对吧还有等等类似的比如说还有我们的这个类似的财务结算财务报销的一套流程对吧这个时候其实这种类似的流程会比较多假如说我们公司里头有20套这样的流程那我们这一次查询的这个流程定义的信息将来
[06:11] 就会有20套所以呢我们第五个环节第五个环节就是输出我们的流程定义信息流程定义信息只不过我们刚才说了只不过现在我们为了去测试我们的这个activity把重心都关注在我们的这个这个activity本身正常的话这个流程定义信息最好是展示到我们的网页上去对吧在网页上可以看到这个东西有
[06:40] 20套流程每一套流程都是什么对不对这个还是比较好的后续我们可以做这样的工作好我们现在开始来关注我们的第二个就是创建我们的 repository Service我们可以通过 process engine 点去调用它的一个叫做 geta叫做 repository Service这样我们就可以得到一个叫做 repositoryposit repository Service好
[07:09] 这样这个工作就完成了当我们reported Service得到下一个工作我们就可以通过我们的这个reported Service去调用它的有一个叫做corrater possess definition query调它那你调它它的这个真正就会给我们去生成一个叫做possess definition query的这个对象
[07:36] 那这个对象都生成出来了那我们下一步就应该去拿着这个curvy的查询对象对吧要注意啊这个地方其实我们可以认为啊可以认为可以认为啊它就是一个查询器有了这个查询器之后将来我们就可以啊对于我们activity背后的这个流程定义信息啊我们就可以去做大量的这个查询了明白是吧
[08:05] 这样我们就不用自己去搞很多很多这个什么相关的Cycle语句说我要怎么怎么查对吧那这个人就没必要了那好我们呢这具体的这个这个设置查询的条件我们一起来关注一下我们这一次在这里设置的这个条件包括有一个是Process Defaulting Key对不对就是我们流程定义的Key我们流程定义的Key各位注意一下我们这一次我们的这个查询条件查询条件
[08:34] 流程定义的key我们这个key应该是什么对吧这个流程定义的key流程定义的key我们这个流程定义的key其实是等于我们的holiday对吧我说了每一套流程都有自己唯一的一个key那我们的这个holiday就是这样的一个唯一的key就是这个意思啊下面我们就给它来设置这个条件吧好我们下面开始啊
[09:03] 就直接可以去使用我们的这个q类对象对吧然后呢再去点点啊设置我们的这个叫做流程流程定义的key我们看一下叫做process process definition key就这个吧这样我们就设置了我们的这个流程定义的key应该是holiday对吧这个key我就设置完了然后设置完key呢
[09:31] 我们后续的还可以做工作比如说我这个时候还希望进一步去对我们的这个排序做一个要求因为这个查询查询完了之后我将来不仅设置条件我还要设置我们的排序规则对吧根据哪个字段排序呢这个时候我们可以去比如说我们根据我们的这个流程定义的VisionOrder by Process DefinitionVision根据我们的这个流程定义
[10:01] 这个地方我们呢这个地方这个auto by process definition这个方法啊指的是啊设置我们的这个排序设置我们的这个排序方式那目前呢它指定的是根据流程根据流程根据流程定义流程定义的版本号
[10:30] 进行排序对吧进行排序这是这个条件那你既然要做排序的话那下一步我们思考的就是是升序还是降序了对吧那这个时候我们就可以去写上是ASC还是我们的DESC各位呢比如说我用我用这个DSC的方式用DSC的方式就证明了我们是一个降序对吧我们的这个高版本是不是应该优先排在前面
[11:00] 这个是大家可以好理解的然后下一步我们如果说要去把这些数据要去把这样的一些流程全都给它查出来对吧那这个时候我们就可以直接在这个地方叫做点类似的方法这样我们就可以去把我们这一套流程因为在每一个流程可能都会有不断的优化迭代更新对吧比如说我们这个流程请假的这个流程已经更新了三次对不对
[11:27] 那这时候我们查询出来的这个反悔值就应该是一个类似的集合我们可以直接把它申明出来那我就直接来一个类似的集合这样呢我们就查询出我们这个Process Defining流程定义基本信息了那下一步我们就可以来实现这个基本信息的输出比如说我这个地方就来一个叫做Process Defining对吧
[11:55] 叫做Process Defining冒号然后我们便利的是类似的集合对吧这样我们就可以去不断去输出我们的流程定义的基本信息这次我们的流程的基本信息包括有哪些我们一起来看一下应该是有ID还有像Name对吧包括有ID流程定义的ID以及流程定义的名称它的Key以及我们的版本号对吧
[12:25] 好那我们也打算把这些基本信息输出比如说流程定义的ID对吧这是其中一个好后续的我都可以我就直接process直接这样来process definition.既然包括有我们的流程定义的ID那就是它对不对还包括有其他的项对吧我们可以把这个把这个部分直接copy了拿过来搞出4个对吧
[12:55] 好那我们流程定义的系流程定义的ID输出了我还可以输出我们流程定义的名称对不对名称好那名称又是怎么去得到呢我们这边可以可以用它的这个get的方法对吧那这个get的方法应该是get name吧把它的名称输出还有一个就是我们的这个流程定义流程定义的key是不是流程定义的key我们可以把它的key也输出
[13:23] 叫做process definition来一个叫点get key我们还可以去输出流程定义的版本号版本号版本号又是怎么去输出我们这个时候可以进一步到这边来叫做version版本号这样我们基本上就完成了我们这一次对于我目前所发布的流程我们可以去看到它的情况
[13:52] 比如说它的ID它的key以它的name我们现在一起运行一下看一下执行的结果我们现在可以关注一下它已经把我们这一套流程所对应的定义的基本信息流程定义的基本信息完全都可以给我们在这里输出这样我们基本上就完成了我们对于这套流程定义的一个查询

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Activiti 的 RepositoryService 查询已部署的流程定义，并输出其基本信息。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 PPT 页面“6.3 流程定义查询”，代码示例为查询流程定义的 Java 方法，其中定义了流程定义键为 "holiday"，并获取 RepositoryService。
画面2: 展示了 PPT 页面“6.4 流程定义删除”，代码示例为遍历查询结果并打印流程部署 ID、流程定义 ID、名称、键和版本。
画面3: 展示了 PPT 页面“6.3 流程定义查询”，代码示例与画面1相同，但底部有黑马程序员的联系方式。
画面4: 展示了 PPT 页面“6.3 流程定义查询”，代码示例与画面1相同。
画面5: 展示了 IntelliJ IDEA 的项目结构，选中了“holiday.bpmn”文件，准备进行操作。
画面6: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，包含 main 方法，用于获取默认的 ProcessEngine。
画面7: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中获取了 RepositoryService。
画面8: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中创建了 ProcessDefinitionQuery。
画面9: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中设置了查询条件，指定流程定义键为 "holiday"。
画面10: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中调用 .orderByProcessDefinitionVersion().desc() 对查询结果按版本降序排列。
画面11: 展示了 PPT 页面“6.4 流程定义删除”，代码示例为遍历查询结果并打印流程部署 ID、流程定义 ID、名称、键和版本。
画面12: 展示了 MySQL Workbench，显示了 activiti 数据库的表结构，其中 act_hi_procinst 表被选中，下方显示了 holiday 流程定义的记录。
画面13: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中执行了查询并打印了结果。
画面14: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中执行了查询并打印了结果，终端输出了查询到的流程定义信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
// 流程定义查询
@Test
public void queryProcessDefinition() {
    // 流程定义key
    String processDefinitionKey = "holiday";
    // 获取repositoryService
    RepositoryService repositoryService = processEngine
            .getRepositoryService();
    // 查询流程定义
    ProcessDefinitionQuery processDefinitionQuery = repositoryService
            .createProcessDefinitionQuery();
    // 遍历查询结果
    List<ProcessDefinition> list = processDefinitionQuery
            .processDefinitionKey(processDefinitionKey)
```

画面2:
```java
.orderByProcessDefinitionVersion().desc().list();
for (ProcessDefinition processDefinition : list) {
    System.out.println("------------------");
    System.out.println("流程部署id：" + processDefinition.getDeploymentId());
    System.out.println("流程定义Id：" + processDefinition.getId());
    System.out.println("流程定义名称：" + processDefinition.getName());
    System.out.println("流程定义key：" + processDefinition.getKey());
    System.out.println("流程定义版本：" + processDefinition.getVersion());
}
```

画面6:
```java
package com.ithema.day03.activiti;
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
```

画面7:
```java
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
RepositoryService repositoryService = processEngine.getRepositoryService();
```

画面8:
```java
ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
```

画面9:
```java
processDefinitionQuery.processDefinitionKey("holiday")
```

画面10:
```java
processDefinitionQuery.processDefinitionKey("holiday")
.orderByProcessDefinitionVersion().desc()
```

画面13:
```java
List<ProcessDefinition> list = processDefinitionQuery.processDefinitionKey("holiday")
.orderByProcessDefinitionVersion().desc().list();
for(ProcessDefinition processDefinition : list){
    System.out.println("流程定义ID：" + processDefinition.getId());
    System.out.println("流程定义名称：" + processDefinition.getName());
    System.out.println("流程定义的Key：" + processDefinition.getKey());
    System.out.println("流程定义的版本号：" + processDefinition.getVersion());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1: 标题为“6.3 流程定义查询”，副标题为“查询部署的流程定义”。
画面2: 标题为“6.4 流程定义删除”。
画面3: 标题为“6.3 流程定义查询”，底部有黑马程序员的联系方式。
画面4: 标题为“6.3 流程定义查询”，副标题为“查询部署的流程定义”。
画面11: 标题为“6.4 流程定义删除”，代码示例为遍历查询结果并打印流程部署 ID、流程定义 ID、名称、键和版本。
画面12: 表格数据为 activiti 数据库的表结构，其中 act_hi_procinst 表被选中，下方显示了 holiday 流程定义的记录。

5) 不要评价画面美观，不要输出与课程无关的内容。

