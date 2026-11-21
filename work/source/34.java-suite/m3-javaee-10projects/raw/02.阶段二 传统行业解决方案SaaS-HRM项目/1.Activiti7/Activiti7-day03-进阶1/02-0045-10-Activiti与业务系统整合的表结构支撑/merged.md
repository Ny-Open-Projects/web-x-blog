# 10-Activiti与业务系统整合的表结构支撑

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\10-Activiti与业务系统整合的表结构支撑_【海量资源尽在 ubkz.com】.mp4
- 时长 4分25秒（音频 265s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那刚才通过我们业务系统和activity整合的一个原理的分析应该我们要清楚的知道我们的这个activity要能够去实现我们的这个业务它的这个流程自动化控制要跟我们具体的业务系统关联起来那这个关键点就是在于我们的这个activity这25张表其中的某一些表或者一张表对吧它肯定是需要将我们的这个
[00:28] 业务系统的ID给它存到我们的activity中去这样当我们的这个activity在不断做流程推进的时候他才能够很清楚的知道是某某员工对吧某某员工他的请假不断的在往后推进对吧这是我们在这个里头给各位做的一个做的一个这个原理上的分析那下面呢我们就从我们的这个数据库的层面上来看
[00:58] 那我们的这个activity背后其实它将来真正关联的这个表呢有这样的一些对吧现在我们直接再去找到我们的这个表结构一起来看一下啊那有像我们的这个RU execution是我们流程实例的执行表对吧那其中呢我们应该在这个地方可以看到啊在RU execution这个表中你可以看到有一个叫做business key
[01:24] 那这个business key就跟我们刚才在这边给各位分析的这个business key是一个道理那我们也可以来看一下啊我们打开我们的这个activity来找一下我们的这个ruruexclusion这个表对吧那现在我们一起来观察一下它这边就是有一个business key那你像刚才我们所介绍的这个请假假如说这里头有某某员工啊要请假那对应的
[01:53] 他的如果他的ID号是1的话那我可以告诉各位将来我们的这条记录的这个组件ID取之1就应该被存到我们这个地方来所以说将来这个地方就应该存的是1那这样我们的这个activity将来在执行的过程中他才能够真正代表我们的1号请假当1号请假当目前他在执行的时候
[02:20] 这个excuse已经执行到哪一步了因为我们这个excuse表中将来是永远执行的都是当前的这个步骤当前你执行到部门经理省批的时候那我们的这个excuse表中就会把这条记录放进来对不对而这条记录将来放进来代表部门经理省那部门经理省是谁的请假单已经进入到部门经理省了比如说我们这个人如果存1的话那将来我们就可以通过这个1的编号又再去回查查我们的这个
[02:50] 请假当是一于是我们就知道是某某员工对吧什么时候开始请假什么时候结束对不对这个就是大致我们的这个数据库表为我们的这个业务系统与我们的这个activity整合所做的一个最为关键性的工作这里头其他的这些表的其实我们之前都给各位基本上都看过像我们有流程历史记录的对吧
[03:18] 任务的历史记录以及我们的这个活动的历史记录啊等等啊那这个部分呢我们就不去特别给各位说了啊那通过刚才给各位介绍的这一段呢主要让各位明白啊我们的这个activity和我们的业务系统整合将来主要是在我们的这个RU execution中会存储以我们的这个business key对不对当这个business key取之为一那代表的是这条记录这条记录
[03:48] 目前它的执行情况是会在execution表中就可以查询到这是我们对于数据库部分和我们的这个业务系统两个库来实现整合的时候我们的activity中主要是通过我们的这个business key来实现我们真正的这个关联主要是这个字段这个部分我们主要是从数据库表的部分给各位大致
[04:18] 看一下我们刚才这个原理与真正的这个数据库实现层面是完全一致的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中流程实例的查询方法，包括数据库表结构、SQL 查询语句和 Java 代码示例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中打开 BPMN 图编辑器，展示一个包含“请假申请审批”、“审批”、“流程结束”三个节点的简单流程图。左侧属性面板显示“异步”选项被勾选。
画面 2: 桌面背景显示“传智播客”和“黑马程序员”联合出品的标志。
画面 3: 在 MySQL GUI 中，连接到本地数据库，显示数据库列表，当前选中“act_hi_procinst”表。
画面 4: 在 MySQL GUI 中，数据库连接状态为“Ready”。
画面 5: 在 MySQL GUI 中，展开“act_ru_execution”表，鼠标悬停在“act_ru_execution”上，显示“for the table”提示。
画面 6: 在 IntelliJ IDEA 中，BPMN 图编辑器显示与画面 1 相同的流程图，但属性面板中“异步”选项未勾选。
画面 7: 在 PDF 文档中，展示“1.5 查询流程实例”章节，包含 SQL 语句“SELECT * FROM act_ru_execution”和“SELECT * FROM act_ru_task”。
画面 8: 在 PDF 文档中，展示“SELECT * FROM act_ru_task”查询结果，其中 USER_ID 为 “zhangsan”，PROC_INST_ID_ 为 “101”。
画面 9: 在 PDF 文档中，展示“SELECT * FROM act_hi_procinst”查询结果，PROC_INST_ID_ 为 “101”。
画面 10: 在 PDF 文档中，展示“1.5 查询流程实例”章节标题页。
画面 11: 在 PDF 文档中，展示“1.5 查询流程实例”章节，包含 Java 代码片段“public void queryProcessInstance()”。
画面 12: 在 PDF 文档中，展示“1.5 查询流程实例”章节，Java 代码片段中“String processDefinitionKey = “holiday”;”被选中。
画面 13: 在 PDF 文档中，展示“1.5 查询流程实例”章节标题页。
画面 14: 在 PDF 文档中，展示“SELECT * FROM act_ru_task”查询结果，其中 USER_ID 为 “zhangsan”，PROC_INST_ID_ 为 “101”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 7:
SELECT * FROM act_ru_execution #流程实例执行表，记录当前流程实例的执行情况
说明：
流程实例执行，如果当前只有一个分支时，一个流程实例只有一条记录且执行表的主键 id 和流程实例 id 相同，如果当前有多个分支正在运行则该执行表中有多条记录，存在执行表的主键和流程实例 id 不相同的记录。不论当前有几个分支总会有一条记录的执行表的主键和流程实例 id 相同一个流程实例运行完成，此表中与流程实例相关的记录删除。
SELECT * FROM act_ru_task #任务执行表，记录当前执行的任务
说明：启动流程实例，流程当前执行到第一个任务节点，此表会插入一条记录表示当前任务的执行情况，如果任务完成则记录删除。
画面 8:
SELECT * FROM act_ru_task #任务执行表，记录当前执行的任务
说明：启动流程实例，流程当前执行到第一个任务节点，此表会插入一条记录表示当前任务的执行情况，如果任务完成则记录删除。
SELECT * FROM act_hi_procinst #流程实例历史表
画面 9:
SELECT * FROM act_hi_procinst #流程实例历史表
流程实例启动，会在表中插入一条记录，流程实例运行完成记录也不会删除。
SELECT * FROM act_hi_taskinst #任务历史表，记录所有任务
开始一个任务，不仅在 act_ru_task 表中插入记录，也会在历史任务表中插入一条记录，任务历史表的主键就是任务 id，任务完成此表记录不删除。
SELECT * FROM act_hi_actinst #活动历史表，记录所有活动
画面 11:
@Test
public void queryProcessInstance() {
// 流程定义key
String processDefinitionKey = "holiday";
// 获取RuntimeService
RuntimeService runtimeService = processEngine.getRuntimeService();
List<ProcessInstance> list = runtimeService.
画面 12:
@Test
public void queryProcessInstance() {
// 流程定义key
String processDefinitionKey = "holiday";
// 获取RuntimeService
RuntimeService runtimeService = processEngine.getRuntimeService();
List<ProcessInstance> list = runtimeService.

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7: PPT 标题为“1.5 查询流程实例”，内容包括 SQL 语句和说明。
画面 8: PPT 标题为“1.5 查询流程实例”，内容包括 SQL 语句和说明。
画面 9: PPT 标题为“1.5 查询流程实例”，内容包括 SQL 语句和说明。
画面 10: PPT 标题为“1.5 查询流程实例”，内容包括标题和说明。
画面 11: PPT 标题为“1.5 查询流程实例”，内容包括 Java 代码片段。
画面 12: PPT 标题为“1.5 查询流程实例”，内容包括 Java 代码片段。
画面 13: PPT 标题为“1.5 查询流程实例”，内容包括标题和说明。
画面 14: PPT 标题为“1.5 查询流程实例”，内容包括 SQL 语句和说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

