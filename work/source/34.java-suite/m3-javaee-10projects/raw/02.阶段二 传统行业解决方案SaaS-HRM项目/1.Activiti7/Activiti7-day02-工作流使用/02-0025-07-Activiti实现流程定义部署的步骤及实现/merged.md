# 07-Activiti实现流程定义部署的步骤及实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\07-Activiti实现流程定义部署的步骤及实现_【海量资源尽在 ubkz.com】.mp4
- 时长 12分6秒（音频 726s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才我们已经把请假的流程定义已经做完了而且也已经将请假的流程的定义转换成了我们的PNG的图片对吧那下面我们要做的工作就是通过我们的编写加码代码将我们的流程定义部署到我们的数据库里头去部署到这个activity库里头去这就是我们现在要来完成的工作
[00:29] 我们要去做流程定义的部署其实就是要将我们的BPM和偏激文件部署到我们的相关的表里去下面我们就按照代码的要求我们来做这个工作好我们切到我们的Java代码部分来第一个我可以去创建一个新的package比如说我们起名字叫做com.it黑马
[00:59] 然后actvict activity然后OK这样我们就创建好了包下一步我们就可以再去创建一个类这个地方我起名字比如说叫做activity test这就是我搞的这个activity叫做deployment叫这个名字叫做流程部署OK
[01:28] 那这样呢我们就可以啊真正去将我们这个流程定义部署到我们的这个相关的表里了去啊这就叫流程啊流程部署流程定义的部署啊我们现在一起来完成这个工作那我到这边呢去搞一个啊卖方法啊咱们用这个卖方法来测试的是我们的这个流程定义部署啊流程定义的一个部署
[02:00] 具体怎么去部署可以在这边第一个还是要求去创建我们的叫做Process Engine通过我们前期所介绍的简单创建的方法后面我们应该是有它的要求然后第二个当我们得到Process Engine这个对象之后
[02:29] 那我们下一个步骤就是要求去得到我们相关的一些Service那这里面我们是与部署相关的这个Service那其实是由我们的这个repository Service来完成这个工作好下面呢我们再回到这边来那就是得到我们的一个叫做repository Service得到一个这样的实例那这是第二个部分
[03:00] 当我们得到了这个RepositoryService之后第三个工作就是进行部署进行部署第四个工作我们就可以叫做输出我们的这个部署部署的一些信息这就是我们整个要做的四个工作通过这四个工作基本上我们就可以完成我们的这个流程定义的部署
[03:31] 当然第四个工作不是必须要做的是因为我们想去检查一下我们这个部署的结果信息我们这个时候可以输出一些信息显示出来我们一起来关注一下现在我们来看第一个步骤怎么去做就是我们的这个process engine之里头有一个叫做get default process engine这个时候它的返回值就是一个process engine的对象就是一个process engine的对象
[04:01] 咱们就完成这个工作了这是第一个工作那第二个工作第二个工作我们就是通过我们的这个Process Engine去调用它的一个叫做Git叫做Repository Service通过调用它的Git Repository Service完了我们就可以在这边达到一个效果就是在这里头得到我们的这个Repository Service好我们完成这个Repository Service
[04:31] 实例啊得到这个实例之后其实我们背后就可以去操作我们相关的跟我们部署相关的这些表了比如说把我们的这些文件直接扔到我们的这个表里头进行存储那这个工作就不需要程序员自己去写DAO写Service完了还需要去写我们文件的这个存储啊这个就大大简化了我们对于这个这个流程定义的一个部署的工作对吧
[05:00] 那我们怎么来部署呢我们这边呢可以通过Repository Service里头有一个叫做Create Deployment这样呢如果你要分步走写的话我们呢它的反复词就是一个Deployment这样的一个实例当然我们在这边呢很多时候在写工作流的时候我们这个时候啊很多时候我们这个开发者都追求这样去写那你比如说我在这边就可以Add Class Pass Resource这样我就会去添加一个
[05:30] 我们真正要部署的是具体的一个什么样的文件对吧那好我就可以直接把我们的这个holidayholo.bpmn这样呢这个就会在另路径下去找到我们的这个文件当然我们这个文件它还有一层目录对吧那我们这个时候就可以直接去把我们的这个叫做diamdgram就是它
[05:59] 把这一层目录也给它加进来当然这只是加的第一个我们这边其实还有一个对不对那就是我们的这个BP就是我们的这个PNG文件对吧这个PNG文件其实我们也一样的可以在这个地方按照这种套路直接contraway对吧扔到这里头来这样就相当于我们加好了我们的这个PNG文件对吧PNG文件
[06:28] 这一段加完我们下一步还可以进一步去调用它的方法比如说来一个叫点deploy这样我们就做到了真正完成我们的部署工作这个各位应该也都比较好理解那你像这一行代码在这里头主要就是添加资源对吧添加我们的资源而这一行代码其实是添加我们的添加我们的BPMN资源对吧
[06:56] 而这一行是添加我们的PNG资源对吧而这一行就是真正来做到我们的这个部署对不对而这一行主要是创建我们的deployment的对象对吧好这样我们基本上呢就完成了我们刚才在这里所说的啊我们要去做这个具体的这个部署的工作对吧你发现我们最最最最后这个地方还有一个就是.lem这个其实就是将我们的这个部署对象的这个名字给他加入进来
[07:25] 那我们要去按照这个步骤的话我们可以直接在这个地方呢加入一个啊比如说我这个地方还可以进一步打点啊我们来看一下它还可以点出具体的哪一些方法啊像刚才我们这里边所添加的就是我们的一个Name吧添加的是我们的Name如果我们仔细观察呢上面除了这些方法之外啊我们这边呢应该还包括一个是它的Key的信息对吧
[07:54] 一个就是刚才我们所说的它的这个LIM的信息对吧这些呢我们都直接可以去点比如说我们要去设置名字那就可以直接在这边加入比如说我在写上叫做请假请假申请的流程请假申请单流程或者请假流程都可以的那这样我们就完成了最终我们的这个部署工作那各位如果
[08:24] 你去你放到这个地方呢我们一样的也可以给它找出一个找出一个变量比如说我们就是叫做deployment叫一个这样的名字这样呢我们基本上就完成了我们的这个部署工作当部署工作一旦做完我们就可以进一步去用我们的sout来实现deployment中的相关属性的输出比如说我们的这个名称就可以输出了
[08:53] 同样的我们的这个ID也可以输出了啊比如说deployment.data还可以比如说像我们的这个ID属性如果刚才我们设置了有key那是不是这个key将来输出也就会有值啊好这样我们就可以啊完成了我们的这个流程的这个部署工作啊那完成流程部署工作注意啊因为我们这一行呢使用的是process engine之用它默认的方式
[09:21] 这就要求我们一定要具备两个前提第一个我们的activity配置文件默认应该是叫activityconfigure.xml除了这一点之外还有一个我们的processengineconfiguration的bin的ID必须起名字叫processengineconfiguration不能是其他名字我们来看的话这些条件也都是具备的现在我们就可以一起来运行
[09:50] 看一下我们部署的这个结果信息好这时候各位就可以看到啊他重新给我创建了表啊那是因为我开始的在这里头执行了一个job啊我把这些表呢给他删了然后我们这一次的创建不仅要创建完表而且呢你还会发现我们的这个deployment的这个num他已经有值了而且他的id也已经有值了那要注意的就是啊这个id的值并不是我自己给的啊
[10:28] 不是我给的我们并没有去设置它的ID的值对不对那这个ID的值怎么来的呢很明显啊它的ID的值从你看它的这个取值是1啊我的感受可能就是我们的MySeq数据库啊它走了这个1234567的这个自动增长导致它的这个ID有值了啊那下面呢我们就可以来刷新一下我们的这个表那各位就可以来关注一下啊
[10:56] 我们的deployment为什么它的ID就是1现在各位看到了吗它的ID是1它的名字就是叫做请假申请单的流程这就是刚才我们在这里头从控制台所看见的两个输出的结果那我们再去回到我们的数据库表的话其实你好好去研究的话我们这一次做部署工作不只是deployment的表里头
[11:27] 多了一条记录其实还有一些表也会多出相关的记录我们先再来总结一下我们刚才在这个部分所做的部署工作大致的步骤就是第一个还是以我们创建Process Engine的对象第二步我们要去得到我们的Report Service的实力第三个就是进一步做我们的部署工作
[11:55] 第四个就可以去输出我们的这个部署信息大致上就是这个流程定义部署的四个步骤

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Activiti 工具部署一个 BPMN 流程定义并验证其数据库表结构。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Activiti 项目结构和一个名为 "holiday.bpmn" 的流程图，流程包含开始事件、两个用户任务和一个结束事件。
画面2: 显示了项目结构，右键菜单展开，准备进行操作。
画面3: 项目结构视图，显示了资源目录下的 BPMN 文件和 Java 类。
画面4: 编辑器中显示了 ActivitiDeployment.java 文件，代码中导入了 ProcessEngine 和 RepositoryService。
画面5: 代码中展示了 RepositoryService 的方法，用于部署流程。
画面6: 代码中调用 repositoryService.createDeployment() 方法，准备部署流程定义。
画面7: 代码中调用 .addClasspathResource() 方法添加资源。
画面8: 代码中调用 .deploy() 方法部署流程。
画面9: 代码中添加了打印部署信息的语句。
画面10: 右键菜单中选择“Run 'ActivitiDeployment_main()'”。
画面11: 控制台输出了 Activiti 部署过程中的 SQL 语句和表结构信息。
画面12: 控制台输出了部署成功的信息，包括部署名称和 ID。
画面13: MySQL Workbench 中执行了删除数据库和创建数据库的 SQL 语句。
画面14: 代码中添加了打印部署信息的语句，控制台输出了部署成功的信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面4:
```java
package com.ithema.activiti;
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.RepositoryService;
```

画面5:
```java
repositoryService.createDeployment()
activateProcessDefinitionById(String s, boolean b, Date date)
activateProcessDefinitionByKey(String s, String s1)
activateProcessDefinitionByKey(String s, boolean b, Date date, String s1)
addCandidateStarterUser(String s, String s1)
addModelEditorSource(String s, byte[] bytes)
```

画面6:
```java
repositoryService.createDeployment()
.addClasspathResource("diagram/holiday.bpmn")
```

画面7:
```java
DeploymentBuilder deploymentBuilder = repositoryService.createDeployment();
deploymentBuilder
    .addClasspathResource("diagram/holiday.bpmn")
    .addClasspathResource("diagram/holiday.png")
    .deploy();
```

画面8:
```java
Deployment deployment = repositoryService.createDeployment()
    .addClasspathResource("diagram/holiday.bpmn")
    .addClasspathResource("diagram/holiday.png")
    .deploy();
```

画面9:
```java
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```

画面11:
```sql
references ACT_GE_BYTEARRAY (ID_)
references ACT_GE_PROPERTY (ID_)
references ACT_ID_GROUP (ID_)
references ACT_ID_MEMBERSHIP (ID_)
references ACT_ID_USER (ID_)
references ACT_RE_DEPLOYMENT (ID_)
references ACT_RE_MODEL (ID_)
references ACT_RE_PROCDEF (ID_)
references ACT_RU_EXECUTION (ID_)
references ACT_RU_IDENTITYLINK (ID_)
references ACT_RU_JOB (ID_)
references ACT_RU_TASK (ID_)
references ACT_RU_VARIABLE (ID_)
```

画面13:
```sql
drop database activiti;
Create database activiti;
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。

