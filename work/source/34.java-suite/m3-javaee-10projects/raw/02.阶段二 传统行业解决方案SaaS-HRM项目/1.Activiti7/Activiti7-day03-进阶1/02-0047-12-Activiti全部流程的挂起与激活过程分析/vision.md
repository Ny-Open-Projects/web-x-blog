# 画面线理解：12-Activiti全部流程的挂起与激活过程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\12-Activiti全部流程的挂起与激活过程分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:59, 01:03, 01:14, 01:32, 04:48, 05:00, 05:19, 05:54, 05:58, 06:23, 06:32, 06:49, 07:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:44:16

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中流程实例的挂起与激活操作，通过代码演示如何控制流程定义的状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“1.4 操作数据库表”，内容包括查询流程实例表（act_ru_execution）和任务表（act_ru_task）的 SQL 语句。
画面2：空白的 PowerPoint 页面，仅显示工具栏。
画面3：IDE 中展示 BusinessKeyAdd.java 文件，包含启动流程实例的代码，其中使用了 processEngine.getRuntimeService().startProcessInstanceByKey("holiday", "1")。
画面4：Activiti Designer 中的 BPMN 图，显示一个简单的流程：开始事件 → 用户任务 → 用户任务 → 结束事件。
画面5：空白的 PowerPoint 页面，仅显示工具栏。
画面6：展示 PPT 页面“1.6 挂起、激活流程实例”，并展开子章节“1.6.1 全部流程实例挂起”。
画面7：PPT 页面“1.6.1 全部流程实例挂起”，展示代码片段，定义了 suspendOnActivateProcessDefinition() 方法，用于挂起流程定义。
画面8：PPT 页面“1.6.1 全部流程实例挂起”，展示代码片段，定义了 suspendOnActivateProcessDefinition() 方法，用于挂起流程定义。
画面9：PPT 页面“1.6.1 全部流程实例挂起”，展示代码片段，定义了 suspendOnActivateProcessDefinition() 方法，用于挂起流程定义。
画面10：PPT 页面“1.6.1 全部流程实例挂起”，展示代码片段，定义了 suspendOnActivateProcessDefinition() 方法，用于挂起流程定义。
画面11：PPT 页面“1.6.1 全部流程实例挂起”，展示代码片段，定义了 suspendOnActivateProcessDefinition() 方法，用于挂起流程定义。
画面12：PPT 页面“1.6.1 全部流程实例挂起”，展示代码片段，定义了 suspendOnActivateProcessDefinition() 方法，用于挂起流程定义。
画面13：PPT 页面“1.6.1 全部流程实例挂起”，展示代码片段，定义了 suspendOnActivateProcessDefinition() 方法，用于挂起流程定义。
画面14：PPT 页面“1.6.1 全部流程实例挂起”，展示代码片段，定义了 suspendOnActivateProcessDefinition() 方法，用于挂起流程定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
SELECT * FROM act_ru_execution #流程实例执行表，记录当前流程实例的执行情况
SELECT * FROM act_ru_task #任务执行表，记录当前执行的任务

画面3：
public class BusinessKeyAdd {
    public static void main(String[] args) {
        //1.得到流程引擎实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到运行时服务
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.启动流程实例，流程当前执行到第一个任务节点，此表会插入一条记录表示当前任务的执行情况，如果任务完成记录删除。
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", "1");
        System.out.println(processInstance.getBusinessKey());
    }
}

画面6：
// 挂起激活流程定义
@Test
public void suspendOnActivateProcessDefinition() {
    // 流程定义Id
    String processDefinitionId = "";
}

画面7：
// 挂起激活流程定义
@Test
public void suspendOnActivateProcessDefinition() {
    // 流程定义Id
    String processDefinitionId = "";
    RepositoryService repositoryService = processEngine
            .getRepositoryService();
    // 获得流程定义
    ProcessDefinition processDefinition = repositoryService
            .createProcessDefinitionQuery()
            .processDefinitionId(processDefinitionId).singleResult();
    // 是否暂停
    boolean suspend = processDefinition.isSuspended();
}

画面9：
// 是否暂停
boolean suspend = processDefinition.isSuspended();
if (suspend) {
    // 如果暂停则激活，这里将流程定义下的所有流程实例全部激活
    repositoryService.activateProcessDefinitionById(processDefinitionId,
            true, null);
}

画面10：
System.out.println("流程定义：" + processDefinitionId + "激活");

画面12：
System.out.println("流程定义：" + processDefinitionId + "挂起");

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题“1.4 操作数据库表”，内容包括两个 SQL 查询语句。
画面4：BPMN 图，结构为：开始事件 → 用户任务 → 用户任务 → 结束事件。
画面6：PPT 标题“1.6 挂起、激活流程实例”，子标题“1.6.1 全部流程实例挂起”。
画面7：PPT 标题“1.6.1 全部流程实例挂起”，内容包括代码片段。
画面9：PPT 标题“1.6.1 全部流程实例挂起”，内容包括代码片段。
画面10：PPT 标题“1.6.1 全部流程实例挂起”，内容包括代码片段。
画面12：PPT 标题“1.6.1 全部流程实例挂起”，内容包括代码片段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
