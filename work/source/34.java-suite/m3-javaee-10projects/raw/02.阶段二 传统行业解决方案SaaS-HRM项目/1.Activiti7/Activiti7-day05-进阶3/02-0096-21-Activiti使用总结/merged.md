# 21-Activiti使用总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\21-Activiti使用总结_【海量资源尽在 ubkz.com】.mp4
- 时长 6分4秒（音频 365s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好那我们啊接着对于本次的这个activity课程啊给各位做一个总结啊那我们这次课程主要给各位讲了啊什么是工作流对吧它主要是计算机啊对我们的这个流程进行自动化管理啊这样的一个过程那我们做工作流管理的过程中呢我们啊为什么要用activity呢对吧因为用activity它可以简化我们整个流程控制的一些操作啊
[00:31] 因为它是用我们的activity也就是进一步做到我们的自动化管理对吧所以activity是一个工作流引擎开源的架构对吧那我们在这里边主要就是用它的BPMN2.0的规范来实现我们的流程定义对吧就是流程定义的图当我们把流程定义的图做好了我们紧接着就需要来开发我们的activity对吧那这个地方涉及到的就是我们activity的开发环境的准备对吧
[01:01] 比如说准备我们的价包那当然我们用marin的话那主要就是一些一些坐标对吧以及我们的这个数据库环境啊默认情况activity7用的是25张表啊那我们还可以做spleen与activity业务系统啊最新业务系统通过spleen与activity来实现整合对吧还有像类似的我们的spleen boot与activity整合来实现我们的工作流引擎的开发啊那这个部分呢
[01:27] 我们会后面会在我们的案例中给各位来进行讲解当我们把整合开发的环境准备好了我们就可以去使用我们的activity提供的流程设计器来实现我们的流程定义对吧而流程定义的时候包括有BPMN文件和PNG文件注意PNG文件不是必须的对吧各位可以看到我们刚才在做这些示例演示的时候其实
[01:55] 都把我们的png文件注掉了因为我们没有去准备我们的png文件好这是我们的这是我们的这一项所以说我们的png文件不是必须的我们再回到这边来第三个步骤就是我们要去将我们的流程定义的文件部署到我们的一个t位体中去部署好了我们就可以查看我们的deployment表对吧
[02:24] 来看我们的这个部署信息而同时呢我们也可以去看我们的这个proceed df来看我们的这个流程定义的信息啊当然我们也可以呢去看我们的这个看我们的这个部署的图啊看我们的部署的图我们呢可以用单个文件部署或这幅文件部署这种这两种方式呢都可以啊那这两种方式在这边呢
[02:51] 一旦我们部署成功我们就可以到BetaRay表中去找我们的这个部署信息对不对但这边也说了我们如果说是直接在这写代码的话我们用单个文件部署方便一些当然我们如果说是Web程序这样你也可以打包对不对打包打成这部文件然后来一起做部署当我们部署完成下一步我们就可以启动流程实例对不对而启动流程实例的过程中
[03:19] 我们也可以去设置我们的这个我们也可以去设置我们的这个流程流程定义的一些变量等等啊当然我们启动流程实例的时候这个一个流程定义对应的这个key就很关键对不对每一套流程都有自己的一个唯一的标识对吧将来如果说我们要去做我们的这个流程我们的业务系统和我们的这个流程和我们的流程实例要整合的话那主要就是通过business key啊
[03:47] 那这个来实现我们业务系统和activity整合的一个关键点对吧那这是我们啊给各位讲过的一个非常重要的一个点啊这个点呢我们也会在后面的中国案例中进一步给各位演示出效果啊那第五个步骤我们就可以来查看自己的任务对吧那查看任务主要我们是通过task Service来做啊指定我们的这个任务执行人对不对这样你就可以查看到用户是否有任务啊
[04:15] 当然你也可以通过我们的这个Candidate User来查询当前的用户是否有自己的代办任务对不对如果我们查到自己有任务下一步就会去办理我们的任务办理任务的话我们通过这个Complete的方法就可以完成某一个任务当然如果是主任务的话我们先要拾取任务对吧那拾取任务我们是通过Task Service的Claim方法来拾取任务最后我们就可以
[04:42] 将我们的这个候选人转换成我们任务的这个负责人对吧这样我们基本上下一步又可以去执行任务了是这意思啊最后呢我们给各位讲到了有这个有这个网关对不对像排他网关主要就是啊只能有一个分支是有效的对吧而我们的并行网关可以有多个分支最后我们的多条分支啊会汇总只有当汇总完成的时候我们的并行并行网关整个执行过程才算是结束啊
[05:12] 最后一个是我们的inclusive gateway包含网关它是排他网关和并行网关的一个结合体对不对它既可以设置条件对吧如果这些条件都成立那他们就会都并行的走对不对所以说它既有排他网关的特点又有并行网关的特点到此我们activity的主要的知识点基本上就给各位
[05:39] 差不多已经给各位说到这里边我们的总结也就说到这里边后续我们主要是将activity跟我们的业务系统很好的结合起来一起去使用对不对好同学们activity我们的基础和我们的进阶内容大致上给各位就说到这里边再见

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程总结了 Activiti 工作流引擎的开发流程，包括环境部署、流程设计、部署到数据库、启动流程实例、查询待办任务和办理任务等六个步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：PPT第37页，标题“第6章 课程总结”，内容包括“什么是工作流”、“什么 activiti?”、“如何使用 activiti 开发?”，并列出第一步：部署 activiti 的环境（环境包括：jar 包和数据库（25 张表））。
画面2：PPT第37页，内容延续画面1，增加第二步：使用 activiti 提供流程设计器（和 idea 或 eclipse 集成的 designer）工具进行流程定义，流程定义生成两个文件：.bpmn 和.png（不是必须的）。
画面3：PPT第37页，内容延续画面2，增加第三步：将流程定义文件部署到 activiti 的数据库，SQL语句为：SELECT * FROM act_re_deployment #流程定义部署表 一次部署插入一条记录，记录流程定义的部署信息。
画面4：PPT第37页，内容延续画面3，补充说明：SELECT * FROM act_re_procdef #流程定义表 一次部署流程定义信息，如果一次部署两个流程定义，插入两条记录。建议：一次部署只部署一个流程定义，这样 act_re_deployment 和 act_re_procdef 一对一关系。常用两个方法：单个文件部署和 zip 文件部署。建议单个文件部署。
画面5：IDEA 中展示 BPMN 流程图，包含 StartEvent、ExclusiveGateway、UserTask、EndEvent 等节点，右侧工具栏列出 BPMN 元素。
画面6：IDEA 中展示 Java 代码，内容为 InclusiveGatewayTest 类，包含 main 方法，用于启动流程实例并完成任务。
画面7：PPT第37页，内容延续画面4，增加第四步：启动一个流程实例。业务系统可以按照流程定义去执行业务流程，执行前需要启动一个流程实例。根据流程定义来启动一个流程实例。指定一个流程定义的 key 启动一个流程实例，activiti 根据 key 找最新版本的流程定义。指定一个流程定义的 id 启动一个流程实例。
画面8：SQLyog 中展示数据库操作，执行了 drop database activiti 和 create database activiti 语句，下方表格显示了 act_re_deployment 和 act_re_procdef 表的数据。
画面9：PPT第37页，内容延续画面7，补充说明：启动一个实例需要指定 businesskey（业务标识），businessKey 是 activiti 和业务系统整合时桥梁。比如：请假流程，businessKey 就是请假单 id。启动一个实例还可以指定流程变量，流程变量是全局变量（生命周期是整个流程实例，流程实例结束，变量就消失）。
画面10：PPT第37页，内容延续画面9，增加第五步：查询待办任务。
画面11：PPT第37页，内容延续画面10，补充说明：查询个人任务：使用 taskService，根据 assignee 查询该用户当前的待办任务。查询组任务：使用 taskService，根据 candidateUser 查询该用户当前的待办组任务。
画面12：PPT第37页，内容延续画面11，增加第六步：办理任务。办理个人任务：调用 taskService 的 complete 方法完成任务。如果是组任务，需要先抢取任务，调用 taskService 的 claim 方法抢取任务，抢取任务之后组任务就变成了个人任务（该任务就有负责人）。
画面13：PPT第37页，内容延续画面12，补充说明：网关。排他网关：任务执行之后的分支，经过排他网关分支只有一条有效。并行网关：任务执行后，可以多条分支，多条分支总会汇聚，汇聚完成，并行网关结束。包含网关：是排他网关和并行网关结合体。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
SELECT * FROM act_re_deployment #流程定义部署表 一次部署插入一条记录，记录流程定义的部署信息

画面4：
SELECT * FROM act_re_procdef #流程定义表 一次部署流程定义信息，如果一次部署两个流程定义，插入两条记录 建议：一次部署只部署一个流程定义，这样 act_re_deployment 和 act_re_procdef 一对一关系 常用两个方法：单个文件部署和 zip 文件部署。建议单个文件部署。

画面6：
//4.处理任务，结合当前用户任务列表内确认操作的话，任务ID:task.getlD()
if(task!=null){
taskService.complete(task.getlD());
}
//5.输出什么id
System.out.println(task.getlD());

//2.启动流程实例
public static void main(String[] args) {
//1.得到ProcessEngine引擎
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RuntimeService服务
RuntimeService runtimeService = processEngine.getRuntimeService();
Integer userType = 2;//代表管理员
Map<String, Object> map = new HashMap<>();

画面8：
drop database activiti
create database activiti

画面12：
//6.办理任务
办理个人任务：调用 taskService 的 complete 方法完成任务。
如果是组任务，需要先抢取任务，调用 taskService 的 claim 方法抢取任务，抢取任务之后组任务就变成了个人任务（该任务就有负责人）。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：BPMN 流程图结构：
StartEvent → ExclusiveGateway → UserTask（“审核请假”）→ ExclusiveGateway → UserTask（“审批”）→ EndEvent
StartEvent → ExclusiveGateway → UserTask（“审核请假”）→ ExclusiveGateway → UserTask（“审批”）→ EndEvent
StartEvent → ExclusiveGateway → UserTask（“审核请假”）→ ExclusiveGateway → UserTask（“审批”）→ EndEvent

画面8：表格数据（act_re_deployment 和 act_re_procdef 表）：
act_re_deployment 表：
| ID_ | ACT_RE_DEPLOYMENT | ACT_RE_PROCDEF | START_TIME | END_TIME | DURATION | BYTE_ARRAY_ID_ |
| --- | --- | --- | --- | --- | --- | --- |
| 12002 | 12002 | 12002 | 2018-11-19 18:50:00 | 2018-11-19 18:50:00 | 0 | 12002 |
| 12003 | 12003 | 12003 | 2018-11-19 18:50:00 | 2018-11-19 18:50:00 | 0 | 12003 |

act_re_procdef 表：
| ID_ | ACT_RE_PROCDEF | ACT_RE_DEPLOYMENT | KEY_ | NAME_ | VERSION_ |
| --- | --- | --- | --- | --- | --- |
| 12002 | 12002 | 12002 | 12002 | 12002 | 1 |
| 12003 | 12003 | 12003 | 12003 | 12003 | 1 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

