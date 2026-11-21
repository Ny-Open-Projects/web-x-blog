# 16-Activiti流程变量案例-测试流程的第一个分支

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\16-Activiti流程变量案例-测试流程的第一个分支_【海量资源尽在 ubkz.com】.mp4
- 时长 9分22秒（音频 562s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那刚才我们完成了启动流程实例的时候同时呢我们还设置了我们的这个流程变量的值对吧并且呢我们也观察了它真正背后呢会给我们的这个ruvaluable这个表以及我们的这个betterarray这个表中真正去序列化我们想要的这个变量的值那好下面呢我们一起来执行一下当我们的这个请假请假的这个执行者张三完成任务
[00:29] 并且我们的这个理事完成任务对吧那这个时候下一步再走就应该是要么走总经理要么走人事了对吧而根据我们刚才在这里面所设置的这个请假天数只是一天对不对我们请一天的话按照这个图流程定义的图那就应该直接是小于抖一三对吧将来这根线就是复活条件了所以会直接进入到人事存档所以现在我们把这些任务让他每个用户都去
[00:58] 执行一下它的任务对吧然后呢我们可以观察一下它运行的效果啊好比如说我这个时候把它住掉啊住掉了我们这个时候重新再回到顶上来啊回到这上面来那我们这个地方再去啊执行的是呃让我们的这个呃是是完成我们的任务啊完成我的任务好走啊那要去做我们的这个完成任务的话各位啊这个地方我们呃后续的这个代码
[01:25] 又有具体的一些变化了对吧好我们来看一下啊将来谁去完成任务呢我们在这里头主要就是我们的这个张商要完成任务对吧当张商完成任务之后下一步就应该是我们的李四要完成任务对不对当李四完成任务之后下面就应该是要去判断我们的流程变量的流程变量的请假天数对吧如果请假天数是小于等于三的话那这个时候
[01:54] 这个时候就会开始分支出来了分支其中一个分支是走我们小于等于3一个是大于3对吧所以我们将来这边就可以观察我们具体怎么去走的对吧判断请假天数而我们目前的请假天数是一天对不对而一天的话按照这个流程进一步走的话一天的话就会走这个分支对不对然后说明是我们的人事经历存档就会被走对不对
[02:21] 所以它再去走的话我们就会走这一个分支这个分支就是叫做人事经理存档这就是我们将来这个流程它会按这个顺序不断的往后去走好我们一起来看一下你来看一下现在我们就可以得到的不再是我们的这个run time Service而应该是我们的任务而就是task Service那么我们的task Service可以通过processengine.get task Service
[02:51] 一样我们就可以得到我们的这个task Service这个也比较简单好当我们拿到task Service我们的第三步就应该去查询查询当前用户是否有任务是否有任务这一点我们最好这样做有任务就执行任务对吧没有任务那就不需要去执行任务对不对所以这个时候我们可以先去做一下这样的查询那就用我们的task Service去点provid
[03:21] task.pure对吧然后呢再去设置我们这个条件对不对比如说我们这里头设置我们的这个task.assign除了设置task.assign之外我们看看还可以设置我们的这个process.definition.key对不对我们的这个process.definition.key注意啊它不是叫做它不是叫做holiday4啊而是呢因为我们在早期的时候忘了改了对不对所以这一行呢
[03:51] 叫做my process下滑键1这个是我们目前的key是不是叫做process definition key我们就直接是key而我们的task assign真正的任务的执行者应该就是我们这里面设置的叫做张商张商这样我们就把我们的条件设置出来了设置完条件它的返回值
[04:21] 它的这个返回值应该是应该是张商只有自己唯一的一个任务对吧叫single result对吧这样呢我们就查到了一个具体的任务比如说就是叫做task好这样我们就知道这个task是否有值如果张商真的有任务来了那于是第四个是不是就判断判断这个task是否等等于none是不是如果不等于none说明什么问题
[04:50] 说明当前的用户有任务对吧这个就说明当前用户有任务对吧如果当前用户有任务我们直接让他去执行任务就可以了对吧所以我这时候可以写上如果他不懂云浪对不对那这个时候我们就可以执行我们的任务叫做task Service.我们这时候就直接来一个叫做completed对吧然后就执行我们的task.get id对吧
[05:18] 这样我们就会把当前的这个任务执行完成对不对好如果他没有任何问题啊比如说这个地方我就是啊我就是直接写上嘛比如说sout比如说任务任务执行啊叫做完毕对吧任务执行完毕如果他不走是不是说明当前这个用户用户就没有任务对吧好这时候我们呢可以一会儿呢把张商设置进来啊把李四是不是设置进来
[05:44] 让我们的任务不断往后推进对吧我们一边来观察一边往后走好这时候我们来看一下我们这边就可以看到有一个任务执行完毕对吧那这个任务执行完毕其实是我们的张三的任务就执行完毕了我们可以看一下张三的任务去看这个表这时候各位就可以看到我们ArchitEinstance可以看到张三的任务就已经执行完毕了
[06:15] 已经目前这个节点呢已经走入到我们的理事但是理事的这个任务并没有直接结束对吧所以他的end time目前没有值啊那我们要做的就是那理事也完成他的任务对吧好所以呢我们可以在这个地方直接把张商改成理事啊好这时候重新再去执行我们的任务对吧好这时候我们再看一下效果这时候各位可以看到啊理事也把他的任务完成了对吧好于是我们再回到这个表中发行
[06:47] 我们这时候就会看到李氏他的这个end time也已经有了各位注意啊当李氏走完之后直接由部门经理进入到人事存档了进入到照6各位这时候你就会看到为什么是直接进入到人事经理存档呢对不对而不是直接进入到我们的这个总经理审评原因就是因为我们的这个holiday.number真正取的值其实是1
[07:13] 1小于等于3所以这时候走这个节点1大于3吗1不大于3所以这个节点它不走明白了吗这时候我们就是走这种分支的时候完全由我们的这个流程定义的变量取值来决定所以这时候我们呢只要让我们的这个造6就完成它的人物就可以了让造6完成它的人物所以这时候我们再去执行这个效果的话那应该就是走我们的人事经历存档对吧
[07:41] 而人事经理呢我们在这里其实就是我们的照六对吧现在我只要去把照六再更新到我们这个部分来我们这时候再执行照六各位我们就可以看到整个这个流程就全都跑完了它完全它的这个具体的走向由我们的这个有我们的这个请假天数流程定义的变量完全来决定具体怎么走对不对好我们这时候可以再看一下啊照六这时候人事经理
[08:10] 人事经理是我们的赵六赵六也进行了存档最后可以看到有一个end event也执行结束了这就是整个这个节点就全都执行结束了这一次我们为什么这么走主要原因是我们的这个流程定义的变量我们当时设置的是一天对不对如果你把它设置为比如说设置为五天那这个时候走法肯定就是直接将来会走这个节点对吧走完这个节点然后才走它
[08:40] 明白是吧这是我们在这里边给各位测了一个我们的流程定义变量在每个任务不断往后推进的时候我们所看见的这个效果好那我们再回顾一下具体怎么走是完全以我们的流程变量的请假天数来决定对吧当我们的任务张商理事在不断往后推进的时候当理事一旦推进完了我们再走是不是就直接会
[09:09] 根据流程定义变量的曲子来决定是走它还是这个分支就走它对不对这一点呢我们基本上给各位演示到这里边

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Activiti 工作流引擎中通过 Java 代码设置流程变量、查询任务并完成任务。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Java 代码，通过 RuntimeService 启动流程实例并传入变量 map。
画面2：展示 BPMN 图，流程从 StartEvent 开始，经过用户任务、条件判断、并行网关，最终到 EndEvent。
画面3：展示 Java 代码，定义流程变量 key 为 "myProcess_1"。
画面4：展示 BPMN 图，流程图与画面2相同。
画面5：展示 Java 代码，通过 processEngine 获取 TaskService。
画面6：展示 Java 代码，通过 TaskService 查询当前用户任务。
画面7：展示 Java 代码，查询用户 "zhangsan" 的任务。
画面8：展示 Java 代码，通过 processEngine 获取 TaskService。
画面9：展示 MySQL 命令行，创建数据库 activiti 和表 act_ge_bytearray、act_ru_variable。
画面10：展示 Java 代码，判断任务是否为空并完成任务。
画面11：展示 BPMN 图，流程图与画面2相同。
画面12：展示 Java 代码，查询用户 "zhaoliu" 的任务。
画面13：展示 BPMN 图，流程图与画面2相同。
画面14：展示 Java 代码，查询用户 "zhaoliu" 的任务。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```java
public class VariableTest {
    public static void main(String[] args) {
        //1.得到ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key值
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(1);
        map.put("holiday", holiday);
        //4.启动流程实例，并且设置流程变量值
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
    }
}
```

画面5：
```java
//1.得到ProcessEngine
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户是否有任务
taskService.createTaskQuery().processDefinitionKey("").taskAssignee()
```

画面6：
```java
//1.得到ProcessEngine
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户是否有任务
String key = "myProcess_1";
Task task = taskService.createTaskQuery().processDefinitionKey(key)
        .taskAssignee("zhangsan").singleResult();
```

画面7：
```java
//1.得到ProcessEngine
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到TaskService
TaskService taskService = processEngine.getTaskService();
//3.查询当前用户是否有任务
String key = "myProcess_1";
Task task = taskService.createTaskQuery().processDefinitionKey(key)
        .taskAssignee("zhangsan").singleResult();
```

画面10：
```java
//4.判断task!=null,说明当前用户有任务
if(task!=null){
    taskService.complete(task.getTaskId());
    System.out.println("任务执行完毕");
}
```

画面9：
```sql
drop database activiti;
create database activiti;
act_ge_bytearray
act_ru_variable
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2、4、11、13：BPMN 图，结构为：
StartEvent → 用户任务 → 条件判断（holiday>0） → 并行网关 → 用户任务 → EndEvent。

画面11：BPMN 图，结构与画面2相同。

画面13：BPMN 图，结构与画面2相同。

画面14：BPMN 图，结构与画面2相同。

5) 无。

