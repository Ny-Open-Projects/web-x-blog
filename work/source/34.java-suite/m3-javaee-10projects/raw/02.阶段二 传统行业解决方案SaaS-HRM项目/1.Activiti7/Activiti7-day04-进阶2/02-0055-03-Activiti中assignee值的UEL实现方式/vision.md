# 画面线理解：03-Activiti中assignee值的UEL实现方式

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\03-Activiti中assignee值的UEL实现方式_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:59, 01:41, 02:15, 03:46, 03:59, 04:24, 04:37, 05:30, 06:30, 07:21, 07:44, 08:11, 08:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:55:01

1) 这一组画面整体在讲如何在 Activiti 工作流中通过代码动态设置流程变量（assignee）并启动流程实例。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PPT 页面，标题为“2.1.2.3 注意事项”，内容是关于在启动流程实例时设置流程变量的代码示例，包含 Java 代码片段：// 定义流程变量 Map<String, Object> variables = new HashMap<String, Object>(); // 设置流程变量assignee variables.put("assignee", "张三"); ProcessInstance processInstance = runtimeService .startProcessInstanceByKey(processDefinitionKey, variables);
画面2: 展示 PPT 页面，标题为“改变中国IT教育，我们正在行动”，内容与画面1相同。
画面3: 展示 IntelliJ IDEA 中的项目结构和 BPMN 图编辑器，显示了 holiday2.bpmn 文件的流程图，包含 StartEvent、UserTask、EndEvent 等节点。
画面4: 展示 IntelliJ IDEA 中的 AssigneeEL.java 文件，代码中调用 runtimeService.startProcessInstanceByKey 方法启动流程实例，并注释说明第一个参数是流程定义的 key，第二个参数是业务标识。
画面5: 展示 IntelliJ IDEA 中的 AssigneeEL.java 文件，代码中注释说明“//3. 设置assignee的取值”，并显示了 Map<String, Object> 的声明。
画面6: 展示 IntelliJ IDEA 中的 AssigneeEL.java 文件，代码中正在声明 Map<String, Object> 变量。
画面7: 展示 IntelliJ IDEA 中的 holiday2.bpmn 文件，流程图中包含 StartEvent、UserTask、EndEvent 等节点。
画面8: 展示 IntelliJ IDEA 中的 holiday2.bpmn 文件，属性面板中 Assignee 设置为 “(Assignee0)”。
画面9: 展示 IntelliJ IDEA 中的 holiday2.bpmn 文件，属性面板中 Assignee 设置为 “(Assignee0)”。
画面10: 展示 IntelliJ IDEA 中的 AssigneeEL.java 文件，代码中调用 runtimeService.startProcessInstanceByKey 方法，并显示了方法签名。
画面11: 展示 IntelliJ IDEA 中的 AssigneeEL.java 文件，代码中设置了 Map<String, Object> 变量，并调用 runtimeService.startProcessInstanceByKey 方法。
画面12: 展示 IntelliJ IDEA 中的 holiday2.bpmn 文件，流程图中包含 StartEvent、UserTask、EndEvent 等节点。
画面13: 展示 IntelliJ IDEA 中的 AssigneeEL.java 文件，代码中设置了 Map<String, Object> 变量，并调用 runtimeService.startProcessInstanceByKey 方法。
画面14: 展示 IntelliJ IDEA 中的 AssigneeEL.java 文件，代码中设置了 Map<String, Object> 变量，并调用 runtimeService.startProcessInstanceByKey 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
// 定义流程变量
Map<String, Object> variables = new HashMap<String, Object>();
// 设置流程变量assignee
variables.put("assignee", "张三");
ProcessInstance processInstance = runtimeService
.startProcessInstanceByKey(processDefinitionKey, variables);

画面4:
//1. 获取ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2. 获取RuntimeService对象
RuntimeService runtimeService = processEngine.getRuntimeService();
//3. 设置assignee的取值，用户可以在界面上设置流程的执行人
Map<String, Object> map = new HashMap<String, Object>();
map.put("assignee0", "zhangsan");
map.put("assignee1", "lishi");
map.put("assignee2", "wangwu");
//4. 启动流程实例，同时动态设置流程定义的assignee的值
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", map);
//5. 输出
System.out.println(processEngine.getName());

画面10:
Map<String, Object> map = new HashMap<String, Object>();
map.put("assignee0", "zhangsan");
map.put("assignee1", "lishi");
map.put("assignee2", "wangwu");
//4. 启动流程实例，同时动态设置流程定义的assignee的值
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", map);
//5. 输出
System.out.println(processEngine.getName());

画面13:
Map<String, Object> map = new HashMap<String, Object>();
map.put("assignee0", "zhangsan");
map.put("assignee1", "lishi");
map.put("assignee2", "wangwu");
//4. 启动流程实例，同时动态设置流程定义的assignee的值
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", map);
//5. 输出
System.out.println(processEngine.getName());

画面14:
Map<String, Object> map = new HashMap<String, Object>();
map.put("assignee0", "zhangsan");
map.put("assignee1", "lishi");
map.put("assignee2", "wangwu");
//4. 启动流程实例，同时动态设置流程定义的assignee的值
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", map);
//5. 输出
System.out.println(processEngine.getName());

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1: PPT 标题为“2.1.2.3 注意事项”，内容是关于在启动流程实例时设置流程变量的代码示例。
画面3: BPMN 图中，StartEvent 指向第一个 UserTask，第一个 UserTask 指向第二个 UserTask，第二个 UserTask 指向 EndEvent。
画面8: 属性面板中，Assignee 设置为 “(Assignee0)”。
画面12: BPMN 图中，StartEvent 指向第一个 UserTask，第一个 UserTask 指向第二个 UserTask，第二个 UserTask 指向 EndEvent。
画面13: 属性面板中，Assignee 设置为 “(Assignee0)”。
画面14: 属性面板中，Assignee 设置为 “(Assignee0)”。

5) 不要评价画面美观，不要输出与课程无关的内容。
