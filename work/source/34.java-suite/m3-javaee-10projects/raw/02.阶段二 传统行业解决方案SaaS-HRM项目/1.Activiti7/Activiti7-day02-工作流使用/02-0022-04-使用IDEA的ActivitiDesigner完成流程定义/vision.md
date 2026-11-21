# 画面线理解：04-使用IDEA的ActivitiDesigner完成流程定义

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\04-使用IDEA的ActivitiDesigner完成流程定义_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:45, 01:33, 02:00, 02:17, 02:39, 02:52, 03:36, 07:41, 07:49, 07:56, 08:03, 08:08, 08:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:20:32

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
