# 21-Activiti流程变量-通过当前任务ID来设置流程变量

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\21-Activiti流程变量-通过当前任务ID来设置流程变量_【海量资源尽在 ubkz.com】.mp4
- 时长 5分34秒（音频 335s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面我们一起来学习我们通过当前的这个任务来设置我们的这个流程变量这种方式我们必须要知道当前的这个任务的ID在知道任务的ID的情况下我们可以通过我们的这个通过我们的这个Task Service里头的叫做SetValuable这个方法来设置那它在设置的时候也是一样的可以呢比如说第一个参数是我们的
[00:28] task任务的ID第二个是我们的key也就是我们的这个流程定义的变量名第三个是我们的这个value值对不对那这种方式一次性设置也只能够设置一个值如果是设置多个值的话我们第二个参数依然跟的是一个MAP及格就可以了这种方式操作起来也非常简单我们如果要做这个测试工作的话首先第一个你应该让我们的这个流程部署做完对吧部署
[00:58] 也就是说我们应该要完成这样的几个步骤第一步你把这个部署工作给我做完对吧第二步你应该把我们的这个流程实力的启动给我做完对不对那做完这个流程实力的启动第三个步骤我们本来就可以来完成我们具体的某一个任务了那就是做这个任务做这个步骤我们上一次呢是在做这个任务执行的时候是在这个complete这个方法里面去指定参数
[01:27] 那这一次我们就相当于啊我们只需要查到当前的这个任务对不对这个任务并不需要在完成之后或者是完成的时候才去给我们的这个参数复制我们只需要知道有一个这样的任务在这个任务过在这个任务中我们直接去给它设置一个这样的变量啊设置好这个变量完了将来这个变量在没有执行之前
[01:54] 我们就相当于把这个变量直接相当于先绑定到这个任务上面了对吧让它保证我们的这个任务保证我们的这个任务对应的一样也可以给我们的这个流程变量先把这个先把这个key和value建制队给它设置好然后后续你可以再去执行你的任务对吧其实所以我在看的时候我们的通过当前的任务来设置变量的方式跟我们呢
[02:22] 任务办理的时候设置其实呢只是时间点有一些差异对吧但是最终是不是都是绑定在具体的某个任务节点上面最终都是绑定到任务的某某个任务的节点上面去让我们的这个变量有值所以说第二种方式我们的任务办理和我们通过当前的任务来实现我们的这个变量设置这两种方式都是与任务直接绑在一起的对吧
[02:50] 其它们本质上是差不多的那我们的第一种方式在启动实例的时候和我们启动完实例然后再通过实例的ID然后再去设置的方式其实本质上是差不多的所以我们说第一种是通过启动流程实例第三种是通过当前的流程实例再去绑定这个变量的key和value都是与实例相关而我们的第二种和第四种
[03:20] 是不是主要是绑定到任务上面去是与我们的任务相关的第四种方式在这个地方我就不打算再去给各位单独的演示出效果了这是我们关于我们的这个Globe类型的Globe类型的这个流程变量四种设置方式给各位全都介绍过了其实总体上来看的话我认为就是两种
[03:47] 一种呢就是与我们的流程实例绑在一起对吧你可以是启动的时候用也可以是呢把实例启动之后然后呢你再去找到根据这个实例的ID然后你再去绑一个辩论上去对吧这是与实例相关的另外一种呢就是与我们的任务相关的你可以呢是我们你可以是我们完成任务的时候然后把辩论绑好也可以是什么呢也可以是我们呢
[04:15] 先把任务的ID号告诉他然后呢通过任务通过任务然后呢提前把这个倍量绑好对不对提前把这个倍量绑好然后我们后续再去再去执行某个任务就可以了这也是一种方式啊当然这个各位同学在测试的时候一定要注意啊如果你这样绑任务的话任务ID必须是当前任务的ID
[04:42] 这个任务的ID在我们的RU task中存在如果这个任务已经执行结束了那这个时候肯定是报错的所以这一点各位一定要注意就是我们第四种方式在绑这个任务的时候这个任务的ID一定是一个没有结束的任务如果这个任务已经完成了那对不起这个时候绑定这个变量那肯定是不行的对吧就相当于你提前把这个任务
[05:11] 任务上面绑定好一个变量将来你去执行的时候你就可以用了对吧所以总体上来看的话我们也可以归为两类小点来看的话就像我们讲义上写的是归为四类对吧好总体上我们关于第四种就是当前任务上去绑定任务给各位也介绍到这里边

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

