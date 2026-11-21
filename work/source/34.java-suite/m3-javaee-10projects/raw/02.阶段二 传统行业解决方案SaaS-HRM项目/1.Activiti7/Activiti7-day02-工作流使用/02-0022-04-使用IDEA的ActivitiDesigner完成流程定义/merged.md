# 04-使用IDEA的ActivitiDesigner完成流程定义

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\04-使用IDEA的ActivitiDesigner完成流程定义_【海量资源尽在 ubkz.com】.mp4
- 时长 8分21秒（音频 501s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面呢我们就一起啊来学习我们的这个activity的入门体验啊那这个入门体验呢我们将从这几个方面给各位来做一下介绍啊首先呢我们要保证自己有一个这样的流程定义的图对不对所以我们这个时候会给各位介绍activity designer通过这个activity designer我们来画这个图啊画流程定义图有了这个流程定义图之后下一步第二个步骤我们就需要去部署这套流程把这套流程呢
[00:29] 我们的这套流程定义呢直接部署到我们的这个数据库表里了去那在我们的数据库表里头有这套流程之后啊下一个我们就可以直接通过我们的启动一个流程实例的方式让这套流程真正运行起来当这套流程运行起来后啊我们流程上面就会有过过不同的节点对不对这一点应该过于去想一想脑子里头去想一想我们之前给过讲的那个请假的流程啊
[00:58] 那我们当我们的流程部署好了我们就可以开始启动了于是张商比如说填写了一个请假当对不对然后这个只要只要你填写完了那下一个作为理事是不是就应该要去去看一下我我可以审批的这个请假当有哪些对不对所以呢这个时候就涉及到一个任务的查询比如说理事作为部门经理那部门经理就可以去批一下我们的这个请假当对吧这是任务的查询
[01:26] 当他查询到自己有任务之后那他就可以进一步处理来实现我们的任务处理对吧比如说你是如果把作为部门经理把这个单子审批完成了那下一步比如说作为总经理又会回到我们总经理总经理进来之后他也需要做任务的查询查到如果有任务就总经理进一步处理当总经理也处理完了之后我们的这个财务经理又要查询自己的任务
[01:52] 当查询完任务之后财务经理进一步进行审批对吧于是整个这个流程我们就认为结束了所以这次我们讲的时候按这个顺序给各位来进行讲解那我们先来看一下我们的这个流程定义要去解决我们的这个流程定义的问题我们就需要来一起看一下activity designer那我们不管使用eclipse还是idea工具来开发我们的都需要去安装我们的这个activity designer那好我们来看一下
[02:21] 在我们的这个idea工具中应该说前期我们已经装完了我们的这个装完了我们的这个acti bpm这个插件啊各位可以看到我们这边已经安装成功了你这次再点都是卸载了对吧好但是我们应该说已经具备了这个前提条件就是已经有了这个插件对吧然后下一步呢我打算在这里面再去创建一个新的这个delict目录比如说叫做dgrim
[02:51] 好OK那这样我们就有了一个这样的文件夹在这个文件夹里头我再去可以创建一个我们的叫做叫做BPMN那各位还能想得起BPMN是什么吗对吧我们前面在介绍的时候已经告诉各位BPMN是叫做我们的这个叫做业务流程model and notation对吧是业务流程的一套标准化的符号对不对有了这一套标准化的符号我们将来去画我们的这个
[03:22] 业务流程定义的时候我们呢就可以借助它来做啊那现在我起一个名字比如说我们有请假的话我们就可以做一个请假的流程对吧好OK这样呢我们这一套流程啊基本上就串联出来了对吧然后呢我们就可以根据自己的情况到这边呢去选取节点对吧比如说这个地方就有一个start event那当然如果你不想看见这个英文啊
[03:49] 你如果不想看见这个英文呢你也可以把这个改成我们的汉字对吧比如说就直接写成开始对吧写成开始汉字俩字也是可以的如果你不想改了你直接用这个名称也是可以的对吧好这是我们的这个叫做start event然后下一个如果你有任务的话那这个时候你就可以把这个任务直接拖到这里边来对吧我们之前也是给各位介绍过好比如说我就把这个任务就可以拖到这边来我们先去做一个简单的流程好吧
[04:18] 比如说我这个地方中间我就可以来一个这就是叫做叫做填写填写我们的叫做请假单对吧填写请假填写请假申请单对吧当我们的这个环节一旦做完我们下一个环节就可以开始了对吧好我这个时候直接需要还需要到这里去拖一个这个
[04:48] 用这个工具不太好的地方就是它这个对齐要靠基本靠我们眼睛去看这一点我们在前期介绍Eclipse的时候应该比这个要好用一些对吧在你拖动的时候它会给你看是否已经对齐了当我们的这个填写完请假当下一步比如说这个地方就应该进入到我们的这个叫做部门经理部门经理审批对吧这是一个环境然后如果
[05:16] 还有其他的环节我们可以再次拖一个节点过来比如说这个地方还有一个就是叫做整经理省批对吧这个就对其一要基本靠眼睛然后最后我们有一个叫做end event对吧整个这个流程这个我认为就基本上已经结束了那我们的这个部分也给它再改一下比如说叫做整经理整经理叫省批对吧这个具体有多少个节点
[05:45] 要根据我们的实际情况自己去选择对吧然后呢我们这个时候就开始连线啊比如说这条线连下来同样的这条线连下来对吧同样的这个呢这条线连下来然后呢这个好变成这个形状之后这条线连下来对吧那我们整个这个流程这就相当于已经定义完了那定义完各位要注意一下啊我们任何一个流程在这里头它都有一个叫做ID这个ID呢不同的流程它的它的这个ID
[06:15] 肯定是不一样的比如说我们的请假流程我在这里头给他起一个名字叫做holiday然后呢我这边也可以给他起一个啊比如说叫做啊请假流程是吧叫做请假啊请假流程啊这就是我写的那这样我们基本上就完成了这个请假流程的这个流程定义对吧当然这个时候你要你要写写成一个n的一问你写成结束两汉字也是可以的啊那这样基本上我们这个流程定义就做完了
[06:45] 那也有个问题就是啊比如说我们的这个填写填写请假申请单将来谁去填写呢那我们这边就有一个叫做assignassign在这里代表的是什么意思啊代表的是我们的这个任务的分配者也就是说这个任务到底分配给谁对吧比如说我这个地方呢我就直接给你写上吧叫做张商可以吧就相当于这个任务将来我们是给张商去做对吧张商来完成我们的任务
[07:14] 那作为部门经理呢我们这个人同样也可以给他起一个名字比如说这个地方来一个叫做领事然后呢作为我们的这个总经理我这个assign我比如说叫做王武对吧那这样我们就相当于这几个任务就丰沛给了三个不同的人由他们来完成我们的这个任务这是我们的这个任务丰沛的问题到目前呢我们基本上
[07:41] 就给各位简单介绍了我们的这个流程定义通过我们的BPMN文件然后呢给它起好给它把这个流程设计出来对吧当然在Eclips里头各位同学在Eclips里头你可以根据我们这个Eclips里头的这个具体的操作方式然后去做然后这一段呢这一段我们大致就给各位说到这吧然后我们如果用Eclips的话我们呢就按它这个走
[08:11] 我们用ideal的话就按我这边这个走就可以了这样我们基本上就完成了我们的流程的定义对吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎的入门体验，包括流程定义、启动流程实例、任务处理、部署流程定义等核心概念与代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：PPT标题页，章节为“第5章 Activiti 入门体验”，子章节“5.1.1.1 Palette（画板）”，介绍Activiti-Designer插件在Eclipse或IDEA中使用，画板包含Connection、Event、Task、Gateway、Container、Boundary event、Intermediate event等元素，流程图设计完毕保存生成.bpmn文件。
画面2：PPT内容页，章节为“5.3 启动一个流程实例”，讲解流程定义部署后可通过工作流管理业务流程，启动流程实例相当于创建一个请假申请对象，代码示例：// 启动一个流程实例 @Test public void startProcessInstance() { RuntimeService runtimeService = processEngine.getRuntimeService(); ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myholiday01"); }
画面3：PPT内容页，章节为“5.5 任务处理”，讲解任务负责人查询待办任务、选择任务进行处理、完成任务，代码示例：// 完成任务 @Test public void completeTask() { //任务id String taskId = "8305"; TaskService taskService = processEngine.getTaskService(); //完成任务 taskService.complete(taskId); System.out.println("完成任务"+taskId); }
画面4：PPT内容页，章节为“5.1.1.1 Palette（画板）”，与画面1内容相同，但下方新增子章节“5.1.1.2 新建流程（IDEA工具）”。
画面5：PPT内容页，章节为“5.1.1.1 Palette（画板）”，与画面4内容相同。
画面6：IDEA开发工具界面，显示ActivitiTest.java文件，代码为：public class ActivitiTest { @Test public void testEnable() { ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); System.out.println(processEngine); } }
画面7：IDEA开发工具界面，显示ActivitiTest.java文件，代码为：//1.创建ProcessEngineConfiguration对象 第一个参数：配置文件名称 第二个参数：processEngineConfiguration.createProcessEngineConfiguration().setJdbcUrl("jdbc:mysql://localhost:3306/activiti").setJdbcUsername("root").setJdbcPassword("root").setJdbcDriver("com.mysql.jdbc.Driver"); //2.创建ProcessEngine对象 ProcessEngine processEngine = configuration.buildProcessEngine(); //3.获取processEngine对象 System.out.println(processEngine); }
画面8：Activiti Designer工具界面，左侧为属性面板，右侧为BPMN画板，画板中包含StartEvent、EndEvent、UserTask、ScriptTask等元素。
画面9：PPT内容页，章节为“5.1.1.2 新建流程（IDEA工具）”，文字说明“首先选中存放图形的目录（本次我们选择 resources下的 bpmn 目录），点击菜单：New-BpmnFile，如下图所示：”，下方显示“New”按钮。
画面10：PPT内容页，章节为“5.1.1.2 新建流程（IDEA工具）”，文字说明“起完名字 holiday 后（默认扩展名为 bpmn），就可以看到进入了流程设计页面，如图所示：”，下方显示Activiti Designer工具界面，画板中包含StartEvent、EndEvent、UserTask、ScriptTask等元素。
画面11：PPT内容页，章节为“5.1.1.2 新建流程（IDEA工具）”，文字说明“创建成功：”，下方显示“Activiti Diagram”和“Activiti Project”等文字。
画面12：PPT内容页，章节为“5.1.1.2 新建流程（IDEA工具）”，显示一个采购流程图，包含“创建采购单”、“部门经理审核”、“总经理审核”、“财务审核”等节点，下方文字说明“图形绘制好后会生成两个文件：”，并列出“purchasingflow01.bpmn”和“purchasingflow01.one”。
画面13：PPT内容页，章节为“5.1.3 指定流程定义 key”，文字说明“流程定义即流程定义的标识。在 eclipse 中通过 properties 视图查看流程的 key”，下方显示“activity.cfg.xml”和“myholiday.bpmn”文件，属性面板中显示“Id: myholiday”、“Name: 请假申请”、“Is Executable: true”、“Is Closed: false”、“Process Type: None”等。
画面14：PPT内容页，章节为“5.2 部署流程定义”，文字说明“部署流程定义就是将上面绘制的图形即流程定义（.bpmn）部署在工作流程引擎 activiti 中，方法如下：”，下方显示代码“// 获取repositoryService”，但未完整显示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面2代码：
// 启动一个流程实例
@Test
public void startProcessInstance() {
RuntimeService runtimeService = processEngine.getRuntimeService();
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myholiday01");
}

画面3代码：
// 完成任务
@Test
public void completeTask() {
//任务id
String taskId = "8305";
TaskService taskService = processEngine.getTaskService();
//完成任务
taskService.complete(taskId);
System.out.println("完成任务"+taskId);
}

画面6代码：
public class ActivitiTest {
@Test
public void testEnable() {
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
System.out.println(processEngine);
}

画面7代码：
//1.创建ProcessEngineConfiguration对象 第一个参数：配置文件名称 第二个参数：processEngineConfiguration.createProcessEngineConfiguration().setJdbcUrl("jdbc:mysql://localhost:3306/activiti").setJdbcUsername("root").setJdbcPassword("root").setJdbcDriver("com.mysql.jdbc.Driver");
//2.创建ProcessEngine对象
ProcessEngine processEngine = configuration.buildProcessEngine();
//3.获取processEngine对象
System.out.println(processEngine);

画面13属性面板内容：
Id: myholiday
Name: 请假申请
Is Executable: true
Is Closed: false
Process Type: None
Candidate Starter Groups:
Candidate Starter Users:
Error Definitions:
Message Definitions:
Signal Definitions:

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1标题：第5章 Activiti 入门体验，子标题：5.1 流程定义，子子标题：5.1.1 Activiti-Designer 使用，子子子标题：5.1.1.1 Palette（画板），内容：在 eclipse 或 idea 中安装 activiti-designer 插件即可使用，画板中包括以下节点：Connection——连接，Event——事件，Task——任务，Gateway——网关，Container——容器，Boundary event——边界事件，Intermediate event——中间事件，流程图设计完毕保存生成.bpmn 文件。
画面2标题：5.3 启动一个流程实例，内容：流程定义部署在 activiti 后就可以通过工作流管理业务流程了，也就是说上线部署的请假申请流程可以使用了。针对该流程，启动一个流程表示发起一个新的请假申请单，这相当于 java 类与 java 对象的关系，类定义好后需要 new 创建一个对象，当然也可以 new 对象。对于请假申请流程，发起一个请假申请单需要启动一个流程实例，请假申请单发起一个请假单也需要启动一个流程实例。代码如下：
画面3标题：5.5 任务处理，内容：任务负责人查询待办任务，选择任务进行处理，完成任务。
画面4标题：5.1.1.1 Palette（画板），内容：在 eclipse 或 idea 中安装 activiti-designer 插件即可使用，画板中包括以下节点：Connection——连接，Event——事件，Task——任务，Gateway——网关，Container——容器，Boundary event——边界事件，Intermediate event——中间事件，流程图设计完毕保存生成.bpmn 文件。下方新增子标题：5.1.1.2 新建流程（IDEA 工具）。
画面5标题：5.1.1.1 Palette（画板），内容：在 eclipse 或 idea 中安装 activiti-designer 插件即可使用，画板中包括以下节点：Connection——连接，Event——事件，Task——任务，Gateway——网关，Container——容器，Boundary event——边界事件，Intermediate event——中间事件，流程图设计完毕保存生成.bpmn 文件。
画面6标题：ActivitiTest.java，内容：public class ActivitiTest { @Test public void testEnable() { ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine(); System.out.println(processEngine); }
画面7标题：ActivitiTest.java，内容：//1.创建ProcessEngineConfiguration对象 第一个参数：配置文件名称 第二个参数：processEngineConfiguration.createProcessEngineConfiguration().setJdbcUrl("jdbc:mysql://localhost:3306/activiti").setJdbcUsername("root

