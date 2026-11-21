# 画面线理解：10-Activiti与业务系统整合的表结构支撑

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\10-Activiti与业务系统整合的表结构支撑_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:34, 01:03, 01:06, 01:33, 01:42, 02:24, 02:59, 03:07, 03:13, 03:21, 03:35, 03:56, 04:03, 04:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:42:39

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
