# 14-Activiti中单个流程实例的挂起与激活

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\14-Activiti中单个流程实例的挂起与激活_【海量资源尽在 ubkz.com】.mp4
- 时长 3分49秒（音频 229s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们就一起啊再给各位来讲一个啊就是单个实例的挂起啊单个实例的挂起因为刚才我们在分析的时候是整个制度发生了变化对不对是整个制度发生了变化那这个制度一旦发生变化那是不是这个流程实例不管是谁在跑这个实例只要是我们的请假制度一旦更新那对不起谁走这个流程将来是统一
[00:28] 全都会被挂起对吧除非挂起之后具体将来后续怎么操作比如说公司规定挂起之后这个流程就不再走了谁也不用关注了你的请假单可能要重新再填写具体怎么填写怎么去执行新的流程那是公司的规定当然这个也有可能比如说现在我们因为请假的人数太多比如说这个月已经超标了
[00:57] 每个月我们必须公司里头有100个人请假而这个月都已经1000个人请假了对吧那其中的900人请假你也别请了全都挂起对不对什么时候走呢对吧你们封皮子下个月你们再请100人再下个月再请100人对吧这就是开个玩笑对不对否则的话呢否则的话那我们全都请假了那不行对吧所以它这个总是有一个制度啊
[01:22] 刚才我们这个制度就是如果一百人请假了一千个人同时请假那其中一百个人是执行通过了那其中九百个人是不是要挂起那挂起之后将来他就做不了后续操作了那怎么办呢到下个月的时候对那我又可以开启对不对又可以重新让它激活那激活之后将来比如说又有一百个人批了那其中又有一批人是不是又进一步挂起
[01:48] 挂帖子要等到下个月比如说我再去执行一下这个命令这个流程又会重新被激活又会激活激活好了一旦操作到数量了我又再挂帖这个就看公司的制度到底怎么跑对不对我们也有另外的一种情况比如说这个员工他在填写请假单他一直在填填完了也在走了但是
[02:14] 他走着走着他发现啊走到这个总经理这个部分的时候发现发现其实有问题其实有问题对的总经理他他这个时候总经理他就可以给出一个具体的这个审批啊比如说我们是要么同意就执行完了对吧要么不同意对不对那目前我们这里头没有表述出来不同意的这种做法对吧那我们呢现在可以在这边呢直接用一种另外的手段就是说呢如果
[02:44] 如果是有问题的流程是不是也可以我也可以单个的把单个的实力给你挂起就是你这个实力你不要再跑了跑也是无效的了对吧我可以给你挂起所以这种场景一旦存在的话让我们给各位演示的单个流程实力来挂起就是只针对某一个实力比如说只针对公司的公司的造六请假他请的请的最后这个任务没有跑完
[03:14] 最后出异常了对吧就是这个情况如果这个流程实力一旦被挂起则流程不能够继续执行流程就再也走不了了当然这个流程如果我们修正之后说你将来又可以进一步让它激活这是允许的你可以进一步把这个实力进一步激活这是没问题的那好我们的大致上给简单
[03:44] 分析了一下我们的单个流程实例的挂体以及它的激活

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

