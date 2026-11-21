# 画面线理解：21-Activiti流程变量-通过当前任务ID来设置流程变量

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\21-Activiti流程变量-通过当前任务ID来设置流程变量_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:23, 00:59, 01:10, 01:15, 01:46, 02:31, 03:01, 03:21, 03:28, 04:08, 04:34, 04:57, 05:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:06:25

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中，通过任务 ID、执行实例 ID 和当前任务设置三种方式设置流程变量的代码实现与注意事项。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了课程 PPT 的标题页：“3.5.3.4 通过当前任务设置”。
- 代码片段：
  @Test
  public void setGlobalVariableByTaskId(){
  //当前待办任务id
  String taskId="1404";
  TaskService taskService = processEngine.getTaskService();
  Holiday holiday = new Holiday();
- PPT 底部有“北京市昌平区建材城西路金燕龙办公楼一层 电话：400-618-9090”字样。
- 左侧项目结构中高亮显示了“3.5.3.4 通过当前任务设置”。

画面2：
- 展示了 PPT 的下半部分，内容为“改变中国IT教育，我们正在行动”和“黑马程序员”Logo。
- 代码片段：
  holiday.setNum(3);
  //通过任务设置流程变量
  taskService.setVariable(taskId, "holiday", holiday);
  //一次设置多个值
  //taskService.setVariables(taskId, variables)
- 注释：代码块下方有“注：”字样，但未显示完整注释内容。

画面3：
- 展示了 IntelliJ IDEA 编辑器界面，打开的是 `VariableTest3.java` 文件。
- 代码片段：
  //通过流程实例id，设置全局变量
  public static void main(String[] args) {
  //1.得到ProcessEngine
  ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
  //2.得到RuntimeService
  RuntimeService runtimeService = processEngine.getRuntimeService();
  //3.流程定义的key问题 myProcess_1
  String key = "myProcess_1";
  //Map<String, Object> map = new HashMap<>();
  Holiday holiday = new Holiday();
  holiday.setNum(5);
  //map.put("holiday", holiday);
  //4.通过流程id，来设置流程变量
  //第一个参数：流程实例id
  //第二个参数：流程变量名
  //第三个参数：流程变量值，所对应值
  runtimeService.setVariable("2501", "holiday", holiday);
  }
- 注释：代码块下方有“//启动流程实例”和“//输出流程实例”等注释。

画面4：
- 展示了 IntelliJ IDEA 编辑器界面，打开的是 `VariableTest3.java` 文件。
- 代码片段：
  //通过流程实例id，设置全局变量
  public static void main(String[] args) {
  //1.得到ProcessEngine
  ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
  //2.得到RuntimeService
  RuntimeService runtimeService = processEngine.getRuntimeService();
  //3.流程定义的key问题 myProcess_1
  String key = "myProcess_1";
  //Map<String, Object> map = new HashMap<>();
  Holiday holiday = new Holiday();
  holiday.setNum(5);
  //map.put("holiday", holiday);
  //4.通过流程id，来设置流程变量
  //第一个参数：流程实例id
  //第二个参数：流程变量名
  //第三个参数：流程变量值，所对应值
  runtimeService.setVariable("2501", "holiday", holiday);
  }
- 注释：代码块下方有“//启动流程实例”和“//输出流程实例”等注释。

画面5：
- 展示了 IntelliJ IDEA 编辑器界面，打开的是 `VariableTest3.java` 文件。
- 代码片段：
  //通过流程实例id，设置全局变量
  public static void main(String[] args) {
  //1.得到ProcessEngine
  ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
  //2.得到RuntimeService
  RuntimeService runtimeService = processEngine.getRuntimeService();
  //3.流程定义的key问题 myProcess_1
  String key = "myProcess_1";
  //Map<String, Object> map = new HashMap<>();
  Holiday holiday = new Holiday();
  holiday.setNum(5);
  //map.put("holiday", holiday);
  //4.通过流程id，来设置流程变量
  //第一个参数：流程实例id
  //第二个参数：流程变量名
  //第三个参数：流程变量值，所对应值
  runtimeService.setVariable("2501", "holiday", holiday);
  }
- 注释：代码块下方有“//启动流程实例”和“//输出流程实例”等注释。

画面6：
- 展示了 PPT 的下半部分，内容为“改变中国IT教育，我们正在行动”和“黑马程序员”Logo。
- 代码片段：
  holiday.setNum(3);
  //通过任务设置流程变量
  taskService.setVariable(taskId, "holiday", holiday);
  //一次设置多个值
  //taskService.setVariables(taskId, variables)
- 注释：代码块下方有“注：”字样，但未显示完整注释内容。

画面7：
- 展示了 Activiti Designer 的流程图编辑界面，文件名为 `holiday.bpmn`。
- 流程图结构：
  - 开始节点（绿色圆圈）→ “开始事件” → “任务1：请假审批” → “任务2：经理审批” → “任务3：财务审批” → 结束节点（红色圆圈）。
  - “任务2：经理审批”节点有一个条件判断（菱形），判断条件为“holiday>3”。
  - “任务3：财务审批”节点有一个条件判断（菱形），判断条件为“holiday>3”。
  - “任务3：财务审批”节点有一个条件判断（菱形），判断条件为“holiday>3”。

画面8：
- 展示了 PPT 的标题页：“3.5.3.2 任务办理时设置”。
- 代码片段：
  public void setGlobalVariableByExecutionId(){
  //当前流程实例执行Id，适配设置为当前执行的流程实例
  String executionId="2501";
  RuntimeService runtimeService = processEngine.getRuntimeService();
  Holiday holiday = new Holiday();
  holiday.setNum(3);
  //通过流程实例Id设置流程变量
  runtimeService.setVariable(executionId, "holiday", holiday);
  //一次设置多个值
  //runtimeService.setVariables(executionId, variables)
- 注释：代码块下方有“注意：”字样，内容为“executionId必须当前流程实例未执行完成，流程实例的执行id，通常此id设置流程实例的id。”。

画面9：
- 展示了 PPT 的标题页：“3.5.3.2 任务办理时设置”。
- 代码片段：
  @Test
  public void completTask() {
  //任务id
  String taskId = "";
  TaskService taskService = processEngine.getTaskService();
  Holiday holiday = new Holiday();
  holiday.setNum(4);
  //定义流程变量
  Map<String, Object> variables = new HashMap<String, Object>();
  //变量名是holiday，变量值是holiday对象
  //variables.put("holiday", holiday);
- 注释：代码块下方有“//定义流程变量”和“//变量名是holiday，变量值是holiday对象”等注释。

画面10：
- 展示了 PPT 的标题页：“3.5.3.2 任务办理时设置”。
- 代码片段：
  @Test
  public void completTask() {
  //任务id
  String taskId = "";
  TaskService taskService = processEngine.getTaskService();
  Holiday holiday = new Holiday();
  holiday.setNum(4);
  //定义流程变量
  Map<String, Object> variables = new HashMap<String, Object>();
  //变量名是holiday，变量值是holiday对象
  //variables.put("holiday", holiday);
- 注释：代码块下方有“//定义流程变量”和“//变量名是holiday，变量值是holiday对象”等注释。

画面11：
- 展示了 PPT 的标题页：“3.5.3.2 任务办理时设置”。
- 代码片段：
  @Test
  public void completTask() {
  //任务id
  String taskId = "";
  TaskService taskService = processEngine.getTaskService();
  Holiday holiday = new Holiday();
  holiday.setNum(4);
  //定义流程变量
  Map<String, Object> variables = new HashMap<String, Object>();
  //变量名是holiday，变量值是holiday对象
  //variables.put("holiday", holiday);
- 注释：代码块下方有“//定义流程变量”和“//变量名是holiday，变量值是holiday对象”等注释。

画面12：
- 展示了 PPT 的标题页：“3.5.3.2 任务办理时设置”。
- 代码片段：
  Holiday holiday = new Holiday();
  //通过任务设置流程变量
  taskService.setVariable(taskId, "holiday", holiday);
  //一次设置多个值
  //taskService.setVariables(taskId, variables)
- 注释：代码块下方有“注意：”字样，内容为“任务id必须是当前待办
