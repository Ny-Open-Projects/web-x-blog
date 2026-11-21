# 12-Activiti全部流程的挂起与激活过程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\12-Activiti全部流程的挂起与激活过程分析_【海量资源尽在 ubkz.com】.mp4
- 时长 7分51秒（音频 471s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 通过前边我们关于流程实例的介绍以及我们启动流程实例在启动流程实例的时候带入我们的business key然后我们的business key真正本质所影响的是我们的数据库表的表中记录的一个变化是哪一张表我们在这边特别给各位同学演示了一把
[00:27] 主要影响的主要是我们的这个RU excuse这个真正流程实例在运行的时候我们的excuse表中始终都会去把我们的这个business key给它存录起来的好那我们再回到这边刚才我们基本上也已经把整个这个操作过程给各位演示了一把对吧那下面呢我们就开始给各位来讲一讲一种特殊的情况吧
[00:55] 比如说啊公司中呢他原本已经跑了一套我们的这个请假的流程大概意思是这样的啊我们可以一起啊给各位简单来分析一下我们想表达的这个效果啊大概意思是这样的啊那你比如说我们这边有一套这样的流程啊这套流程呢按道理我们总是会这样啊从头到尾去执行对吧从头到尾给他去执行啊但是呢我们啊
[01:25] 也说了在有一种极端的情况下这个流程呢可能并不会从头到尾执行完整比如说啊这种极端的情况是什么比如说啊公司制度公司制度啊发生了变化对吧公司制度发生了变化比如说我们原来请假流程就是这样的但是呢比如说现在公司啊因为各种原因啊他说原来这个流程是有问题的
[01:53] 原来这个流程是不完整的那于是他们呢比如说这个公司就调整了公司的这个请假制度对吧当这个制度一旦发生调整的时候于是我们的一种特殊情况可能就来了比如说原本原本还没有还没有批完的流程那怎么办对吧这就是一种比较特殊的问题对吧好
[02:25] 这是一个比如说这是第一个问题我再说第二个问题原本还没有批完的流程怎么办对吧比如说其中张三或者是某某叉叉员工叉叉员工过人还没有批完的流程怎么办对不对那如果说我说第一个问题的话我说的是所有的张公司里头比如说现在
[02:55] 有100个人发生了请假的流程这100个人现在可能有比如说有70个人已经批完了其中还有30个人正好走在部门经理或者是走在总经理的这些环节中但是我们的流程公司说制度变了这30个人将来这30个人怎么办这30个人因为他还没有走完流程这30个人如何处理
[03:24] 那这个部分就要看公司的制度怎么来了对吧比如说公司制度说了原来已经走的这个流程按老制度执行完整执行完成对不对如果说另外一种制度变化就是什么呢比如说原来还没有执行完成的这个流程对不起这些流程统一要打回对不对重新再去申请并且
[03:53] 按公司的新制度来执行对吧那这个时候就比较悲怅了对吧这个可能就是新制度和老制度交替的时候会存在这个现象还有一个就是咱们比如说总体上假如说我们对应的流程真正在走的时候最终发现老制度走的流程比如说就只剩下某一个员工了那这个时候可能他只要把这一个流程给他挂
[04:21] 挂起就可以了对不对这个流程那就不用再走了然后这个流程就算结束对吧这样做是针对某个人对吧那我们一旦这种制度性问题一旦发生那我们的这个流程可能就要停止或者是暂时挂起对吧这个部分呢就是我们现在要去给各位进一步讲的我们的这个流程有些时候迫不得已
[04:51] 那就需要进行挂起对吧好那我们一起来看一下就是如果说我们的这个流程要全部挂起对吧全部挂起暂停执行只要涉及到我们的这个制度我刚才说了如果是30个人他正在走但是没走完那对不起我是不是也要把这个也要把这30个人统一全都挂起那这个时候
[05:20] 就可以用我们这边给各位提供的大致的处理过程来做我们可以一起来看一下这个过程第一个你可以看到我们还是去想办法拿到Repository Service对吧然后我们就可以去查询对吧获得我们的流程定义信息比如说我们一旦得到了我们的流程定义信息之后
[05:46] 我们将来就应该是把整个这个流程定义都给它挂起那一旦我们的这个流程定义啊挂起了那整个我们这个流程肯定就将来后续就没有办法去执行了对吧这是第一个环节啊是是A是suspen的啊通过这个我们先去看看啊它是否是暂停的对吧如果
[06:15] 如果暂停则激活对吧这个地方又涉及到有我们的激活的问题如果是处于激活的状态我们这个时候就应该要想办法给它挂起对吧所以在这里边我们主要就是通过这两个办法来给它实现出这个效果我们如果是暂停要激活的话我们主要是用的是active对吧
[06:44] ActiveProcessDefundingById如果说我们是要去给它挂起的话那我们应该用的是Suspend这个方法来实现处理效果这是我们大致上给各位的讲了一下我们的一个流程要能够挂起或者是能够去激活我们在这边
[07:12] 主要就是用active process definition by id对吧或者是我们suspend开头的这个方法对不对来实现我们的这个挂起或者是像这个是激活像这个是挂起对吧而像上面的这个方法a是suspend指的是是否暂停对吧好了如果它的返回值是去就代表的是我们是暂停
[07:40] 这是我们大致给各位分析了一个思路下面我们下一个环节就要动手来实现一把我们思路性的问题暂时就总结到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

