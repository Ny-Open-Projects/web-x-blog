# 画面线理解：14-Activiti中单个流程实例的挂起与激活

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\14-Activiti中单个流程实例的挂起与激活_【海量资源尽在 ubkz.com】.mp4
- 抽帧：12 帧 @ 00:08, 01:50, 01:56, 02:02, 02:09, 02:11, 02:48, 02:58, 03:01, 03:03, 03:26, 03:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:45:58

1) 这一组画面整体在讲如何通过代码操作 Activiti 流程引擎，实现对单个流程定义或流程实例的挂起与激活操作。

2) 按时间顺序列出每张画面的要点：
画面1: 展示一个流程图，包含“StartEvent”、“用户请假申请”、“部门经理审批”、“总经理审批”和“EndEvent”节点，右侧文字框提出“公司制度发生变化”时的两个问题。
画面2: 展示 IntelliJ IDEA 中的 Java 代码，内容为通过 RepositoryService 挂起流程定义，代码中包含注释“//说明是假，就可以激活”。
画面3: 展示 IntelliJ IDEA 中的 Java 代码，内容为通过 RepositoryService 挂起流程定义，代码中包含注释“//说明是假，就可以激活”。
画面4: 展示一个流程图，包含“StartEvent”、“用户请假申请”、“部门经理审批”、“总经理审批”和“EndEvent”节点，右侧文字框提出“公司制度发生变化”时的两个问题。
画面5: 展示一个流程图，包含“StartEvent”、“用户请假申请”、“部门经理审批”、“总经理审批”和“EndEvent”节点，右侧文字框提出“公司制度发生变化”时的两个问题。
画面6: 展示一个流程图，包含“StartEvent”、“用户请假申请”、“部门经理审批”、“总经理审批”和“EndEvent”节点，右侧文字框提出“公司制度发生变化”时的两个问题。
画面7: 展示 PPT 页面，标题为“1.6.2 单个流程实例挂起”，内容为“操作流程实例对象，针对单个流程执行挂起操作，某个流程实例挂起则此流程不再继续执行，完成该流程实例的当前任务将报异常。”，下方代码为 `@Test public void suspendOnActiveProcessInstance() { ... }`。
画面8: 展示一个流程图，包含“StartEvent”、“用户请假申请”、“部门经理审批”、“总经理审批”和“EndEvent”节点，右侧文字框提出“公司制度发生变化”时的两个问题。
画面9: 展示 PPT 页面，标题为“1.6.2 单个流程实例挂起”，内容为“操作流程实例对象，针对单个流程执行挂起操作，某个流程实例挂起则此流程不再继续执行，完成该流程实例的当前任务将报异常。”，下方代码为 `@Test public void suspendOnActiveProcessInstance() { ... }`。
画面10: 展示 PPT 页面，标题为“1.6.2 单个流程实例挂起”，内容为“操作流程实例对象，针对单个流程执行挂起操作，某个流程实例挂起则此流程不再继续执行，完成该流程实例的当前任务将报异常。”，下方代码为 `@Test public void suspendOnActiveProcessInstance() { ... }`。
画面11: 展示 PPT 页面，标题为“1.6.2 单个流程实例挂起”，内容为“操作流程实例对象，针对单个流程执行挂起操作，某个流程实例挂起则此流程不再继续执行，完成该流程实例的当前任务将报异常。”，下方代码为 `@Test public void suspendOnActiveProcessInstance() { ... }`。
画面12: 展示 PPT 页面，标题为“1.6.2 单个流程实例挂起”，内容为“操作流程实例对象，针对单个流程执行挂起操作，某个流程实例挂起则此流程不再继续执行，完成该流程实例的当前任务将报异常。”，下方代码为 `@Test public void suspendOnActiveProcessInstance() { ... }`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2代码：
```java
public class SuspendProcessInstance {
    public static void main(String[] args) {
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        RepositoryService repositoryService = processEngine.getRepositoryService();
        ProcessDefinition processDefinition = repositoryService.createProcessDefinitionQuery()
                .processDefinitionKey("holidays").singleResult();
        boolean suspended = processDefinition.isSuspended();
        String processDefinitionId = processDefinition.getId();
        if (suspended) {
            //说明是假，就可以激活
            repositoryService.activateProcessDefinitionById(processDefinitionId, true, date: null);
            System.out.println("流程定义：" + "激活");
        } else {
            repositoryService.suspendProcessDefinitionById(processDefinitionId, true, date: null);
            System.out.println("流程定义：" + "挂起");
        }
    }
}
```

画面7代码：
```java
@Test
public void suspendOnActiveProcessInstance() {
    // 流程实例Id
    String processInstanceId = "";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    // 根据流程实例Id查询流程实例
    ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
            .processInstanceId(processInstanceId).singleResult();
    boolean suspend = processInstance.isSuspended();
    if (suspend) {
        // 如果暂停则激活
        runtimeService.activateProcessInstanceById(processInstanceId);
        System.out.println("流程实例：" + "激活");
    } else {
        // 否则挂起
        runtimeService.suspendProcessInstanceById(processInstanceId);
        System.out.println("流程实例：" + "挂起");
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面7 PPT 标题：1.6.2 单个流程实例挂起
画面7 PPT 内容：操作流程实例对象，针对单个流程执行挂起操作，某个流程实例挂起则此流程不再继续执行，完成该流程实例的当前任务将报异常。
画面7 代码块：`@Test public void suspendOnActiveProcessInstance() { ... }`

5) 无
