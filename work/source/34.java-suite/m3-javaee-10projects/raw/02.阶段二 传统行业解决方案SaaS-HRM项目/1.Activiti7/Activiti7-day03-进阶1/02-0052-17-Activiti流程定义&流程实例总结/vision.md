# 画面线理解：17-Activiti流程定义&流程实例总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\17-Activiti流程定义&流程实例总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:08, 01:19, 01:53, 02:03, 03:00, 03:17, 04:21, 04:43, 04:51, 04:54, 05:46, 05:52, 06:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:48:32

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti7 工作流引擎中流程定义、流程实例、历史信息的查询与挂起/激活操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：标题页，显示“SaaS-IHRM 项目-Activiti7 工作流引擎”。
画面2：讲解“6.5 流程定义资源查询”，展示通过流程定义对象获取流程定义资源的代码示例。
画面3：展示 BPMN 图形界面，包含 StartEvent、UserTask 等节点，并显示控制台日志。
画面4：在 MySQL GUI 中查询 act_ru_execution 表，展示流程实例的 ACT_ID_、PROC_INST_ID_ 等字段。
画面5：讲解如何通过 HistoryService 查询历史活动实例，展示相关代码。
画面6：讲解“1.3 Businesskey(业务标识)”，说明业务标识的用途，并展示代码和数据库表中存储的业务标识。
画面7：与画面6内容相同，展示“1.3 Businesskey(业务标识)”的代码和数据库表。
画面8：在 MySQL GUI 中查询 act_ru_execution 表，展示流程实例的 ACT_ID_、PROC_INST_ID_ 等字段。
画面9：与画面6内容相同，展示“1.3 Businesskey(业务标识)”的代码和数据库表。
画面10：讲解“1.5 查询流程实例”，展示通过 RuntimeService 查询流程实例的代码。
画面11：讲解“1.5.1 关联 businessKey”，说明在实际应用中查询流程实例列表时可能需要显示业务系统信息。
画面12：讲解“1.6.1 全部流程实例挂起”，展示通过 RepositoryService 挂起流程定义的代码。
画面13：继续讲解“1.6.1 全部流程实例挂起”，展示判断流程定义是否挂起并激活的代码。
画面14：讲解“1.6.2 单个流程实例挂起”，展示通过 RuntimeService 挂起单个流程实例的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
@Test
public void getProcessResources() throws IOException {
    // 流程定义id
    String processDefinitionId = "";
    // 获取 repositoryService
    RepositoryService repositoryService = processEngine
            .getRepositoryService();
    // 流程定义对象
    ProcessDefinition processDefinition = repositoryService
            .createProcessDefinitionQuery()
            .processDefinitionId(processDefinitionId)
            .singleResult();
}

画面3：
select single component to edit its properties

画面4：
Query: 1

画面5：
public void testHistoric01() {
    HistoryService historyService = pe.getHistoryService();
    HistoricActivityInstanceQuery query = historyService
            .createHistoricActivityInstanceQuery();
    query.processInstanceId("1501");
    List<HistoricActivityInstance> list = query.list();
    for(HistoricActivityInstance ai : list){
        System.out.println(ai.getActivityId());
        System.out.println(ai.getActivityName());
    }
}

画面6：
// 根据流程定义的key启动一个流程实例
ProcessInstance processInstance = runtimeService
        .startProcessInstanceByKey(processDefinitionKey,
        businessKey);

画面7：
// 根据流程定义的key启动一个流程实例
ProcessInstance processInstance = runtimeService
        .startProcessInstanceByKey(processDefinitionKey,
        businessKey);

画面8：
Query: 1

画面9：
// 根据流程定义的key启动一个流程实例
ProcessInstance processInstance = runtimeService
        .startProcessInstanceByKey(processDefinitionKey,
        businessKey);

画面10：
@Test
public void queryProcessInstance() {
    // 流程定义key
    String processDefinitionKey = "holiday";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    List<ProcessInstance> list = runtimeService
            .createProcessInstanceQuery()
            .processDefinitionKey(processDefinitionKey)
            .list();
}

画面12：
@Test
public void suspendOrActivateProcessDefinition() {
    // 流程定义id
    String processDefinitionId = "";
    // 获取 repositoryService
    RepositoryService repositoryService = processEngine
            .getRepositoryService();
    // 获取流程定义
    ProcessDefinition processDefinition = repositoryService
            .createProcessDefinitionQuery()
            .processDefinitionId(processDefinitionId)
            .singleResult();
}

画面13：
// 是否挂起
boolean suspend = processDefinition.isSuspended();
if(suspend){
    // 如果是挂起状态，这里将流程定义下的所有流程实例全部激活
    repositoryService.activateProcessDefinitionById(processDefinitionId,
            true, null);
    System.out.println("流程定义："+processDefinitionId+"激活");
}else{
    // 如果是激活状态，这里将流程定义下的所有流程实例全部挂起
    repositoryService.suspendProcessDefinitionById(processDefinitionId,
            true, null);
    System.out.println("流程定义："+processDefinitionId+"挂起");
}

画面14：
@Test
public void suspendOrActiveProcessInstance() {
    // 流程实例id
    String processInstanceId = "";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    // 根据流程实例id查询流程实例
    ProcessInstance processInstance = runtimeService
            .createProcessInstanceQuery()
            .processInstanceId(processInstanceId)
            .singleResult();
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：标题“6.5 流程定义资源查询”，子标题“6.5.1 方式 1”。
画面3：BPMN 图形界面，StartEvent 指向 UserTask。
画面4：MySQL GUI 中的表结构，包含 ACT_ID_、PROC_INST_ID_、START_TIME、END_TIME 等字段。
画面5：PPT 标题“1.5 查询流程实例”，内容说明流程实例的状态和运行节点。
画面6：PPT 标题“1.3 Businesskey(业务标识)”，内容说明业务标识的用途和存储位置。
画面7：与画面6相同。
画面8：MySQL GUI 中的表结构，包含 ACT_ID_、PROC_INST_ID_、BUSINESS_KEY、PROC_DEF_ID 等字段。
画面9：与画面6相同。
画面10：PPT 标题“1.5 查询流程实例”，内容说明如何查询流程实例。
画面11：PPT 标题“1.5.1 关联 businessKey”，内容说明在实际应用中查询流程实例列表时可能需要显示业务系统信息。
画面12：PPT 标题“1.6.1 全部流程实例挂起”，内容说明如何挂起流程定义。
画面13：PPT 标题“1.6.1 全部流程实例挂起”，内容说明如何判断流程定义是否挂起并激活。
画面14：PPT 标题“1.6.2 单个流程实例挂起”，内容说明如何挂起单个流程实例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
