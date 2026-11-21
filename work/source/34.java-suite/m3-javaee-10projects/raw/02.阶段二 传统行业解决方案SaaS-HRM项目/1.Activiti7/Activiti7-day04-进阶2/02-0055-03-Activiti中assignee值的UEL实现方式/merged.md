# 03-Activiti中assignee值的UEL实现方式

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\03-Activiti中assignee值的UEL实现方式_【海量资源尽在 ubkz.com】.mp4
- 时长 8分51秒（音频 531s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 通过刚才我们在这个地方对于我们的这个assign动态的去设置我们的这个UEL表达式各位可以看到我们的填写请加单部门经理审批总经理审批目前都已经被我设置为我们的这个UEL表达式了对吧那UEL表达式具体刚才就是我们在这边用这种方式来硬设置对吧那设置好这个表达式之后具体的这个表达式其实真正
[00:28] 意义上现在只是一个相当于是一个我们学Java里的那个站位服务式的你可以这么理解就是类似的这只是一个key是不是这个key真正对应的这个value值目前我们并没有去设置那我们在什么地方去设置这个value值呢对吧那这一次我们主要就是通过在我们将来的这个Java代码里头去动态的给我们的这个assign设置它的值
[00:56] 那在什么时候去设置啊这个地方是我们在这个流程实例啊启动的时候我们呢就需要去给我们的这个变量去设置相应的值啊所以呢我们这边呢主要是用的是runtime Service在启动流程实例的时候我们呢给上第二个参数而第二个参数它可以是一个map及格这样我们将来就可以给很多对应的key指定它的value啊
[01:26] 这是大致实现思路是这样的那好现在呢我们可以重新回到我们这个部分来那我可以这样首先我在我们的这个D04部分我可以这样做copy我现在去添加一个新的类进来这个类呢其实主要就是给我们的这个assigngme assign去复制对不对给我们的UEL给达式来进行
[01:55] 设置一个相关的值所以我这边主要是我们的流程实例在启动的时候同时我们还要做一件事情那就是设置动态设置我们的这个ASIGN的取值这个部分都可以留在这就相当于我们的这个process engine以及我们的这个long time Service都可以留在这
[02:22] 那下一个步骤就是我们的第三个步骤就是去设置我们的这个assignassign的取值对吧当然啊各位我们这边的目前给的这个值就直接给一个死的值而具体将来我们的这个assign取什么值大家思考一下啊正常的流程可不可以让用户在界面上去选取啊就是用户啊可以
[02:52] 在界面上设置流程的执行人对不对比如说我就可以去选对吧比如说我们部门经理部门经理假如说有三个有一个部门的总经理还有部门的副总经理或者是部门助理比如说部门经理有一个然后经理底下配了有俩助理对吧这个时候将来我在执行任务的时候如果说
[03:21] 我一看这个经理经理批的可能比较严或者是其他原因我也可以同时去选择我们的助理对吧这就是我们相当于一个流程执行下来可能将来会有很多个assign对吧很多个执行人的时候其实我们这种方式是可以的用户在界面上选最终他选完之后就会把这个界面上的值
[03:50] 最终是都要传给我们的后台那我们的后台在接收这个值的时候我可以这样各位可以看一下我就直接用一个用一个这种方式比如说来一个MAP集合等于用一个HashiMap对吧HashiMap然后呢这样我们就可以把这个集合创建出来了那下一步要做的就是MAP.put对吧去真正给值而这个key要注意这个地方这个key咱们在写的时候
[04:19] 你要看清楚你看我这个地方给的第一个值就是叫做assign0那注意assign0从哪来的是这个地方的这个assign0那如果这个地方将来我们的这个流程我们的这个流程里头的这个key它不叫assign0那比如说叫abc你把这个改成abc了那好我们这个地方也要写成abc就是我们这个pool
[04:47] MAP机构的key就是我们UEL表达室里头那个key好比如说这个上我就可以来一个比如说我就还是按这个写吧我就假如说用户在界面上填的这个值就是张商对吧那这样我们第一个值就有了而我们还可以有第二个值就是我们的这个assign应该我们这里头应该是还有个assign1还有一个assign2对吧所以呢我这边呢就可以直接assign1assign2
[05:17] 对吧然后这个地方呢就应该是叫做我们的张商啊这个叫李四啊这个地方就是叫做王武啊王武对吧好这样我们就有了一个给我们的这个流程啊流程的这个assign的UEL表达式0assign1assign2在我们对应的这个加码代码部分呢给这三个key都指定了一个子对不对那这是第三个步骤
[05:45] 第四个步骤我们就可以叫做启动启动我们的流程实例好具体怎么样来启动流程实例对吧同时我这里还要做一个工作同时还要设置我们的流程定义流程定义的 assign 的值我们具体怎么来做可以通过 runtime 里头有一个叫做 start
[06:15] ProcessUstanceByKey好各位注意一下那我们这一次设置的时候呢你就可以有带用带两个参数的这个构造啊你看一下我们第一个正好是String第二个是Map那你就可以选择它而第一个还是我们的这个流程定义的KeyHoliday2我这里应该是这个Holiday2好逗号
[06:41] 而我们的第三个参数我在这里就是MAP集合这样我们就完成了我们的流程具体的启动工作比如说这个时候我就可以得到一个Processing Instance得到Processing Instance之后我们第五个步骤其实你可以去设置你可以去做其他的一些工作比如说做一些输出的工作这个当然各位
[07:09] 如果我们不去做这个输出的工作也没关系的比如说processing用途上是点get你就可以去输出一下我们整个这个流程比如说get name对吧然后我这里头要做的是一个输出的工作把这个代码直接x直接control v扔到这来这样我们基本上就完成了我们想要的这个效果这是我们这边跑的这个
[07:38] 好的这个执行的代码基本上就这样的啊那我们如果要去执行这个效果的话要注意啊我们的这一套流程首先你这个Holler2这个流程呢要保证在我们的这个要保证啊它呢在我们的这个Architivity工作流的这个表中应该是有的对吧所以呢我们如果要去做这个工作的话我们要借助于之前讲过的这个流程部署啊来实现这个部署的效果对吧部署完了之后再启动看效果啊
[08:08] 那这是我们先把这个UEL表达式设置值的代码大致给各位说到这里边主要大致的步骤就是我们在启动Processing用途同时的时候还可以给一个MAP结果作为第二个参数这是我们给我们的这个Assign动态分配值大致实现的主要步骤其实新的步骤就这个地方对吧就这个地方
[08:37] 然后关键点还有一个就是我们key要求要跟这里边的key是保持一致的对吧跟UEL给它设的key是一致的这个也比较简单

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

