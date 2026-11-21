# 画面线理解：21-Activiti使用总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\21-Activiti使用总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:41, 00:52, 01:07, 01:51, 01:54, 02:20, 02:51, 03:07, 03:14, 03:53, 04:02, 04:22, 04:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:27:20

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
