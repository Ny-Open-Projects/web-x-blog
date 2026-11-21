# 17-Activiti流程变量案例-测试流程的num大于3的分支

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\17-Activiti流程变量案例-测试流程的num大于3的分支_【海量资源尽在 ubkz.com】.mp4
- 时长 5分13秒（音频 313s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们可以啊那我们的这个流程啊在执行跑的过程中呢跑到我们的这个分子上面来那我们也可以各位做一下简单的这个测试啊那我这个流程要跑到这个分子上面来呢那我可以再去启动一个流程实例啊各位我们这个时候可以一起来看一下效果啊比如说我把这个这个这个名字我给它改一下啊改成叫慢一啊
[00:29] 这样的话它就不再是一个卖方法对吧好我们这个时候再走啊就是呢把我们早期启动流程实例的这个代码再给它松开对不对好这个时候各位可以看一下啊我再把它松开了那松开注意呢我们把这个请假天数我这里头改成了五天对不对那其他地方其实我们都不需要做任何的改变对吧那这样我们相当于这个流程又会被重新开启一个啊好这时候我们再走啊
[01:01] 那各位这个时候我们在运行跑的这个效果的时候各位就可以看到它又启动了一个新的流程实例对吧那这个实例跑出来我们真正再要去执行这个任务的时候比如说我把这个地方又给各位加了个慢一加了个慢一现在上面这个地方就不能起一个这样的名字了对吧我们这个时候直接去掉按照我们这一次新的执行步骤我们这个地方
[01:30] 应该要改了对吧那应该是首先是我们的张商跑对不对好比如说我们这个再给他拿过来啊张商跑那张商就可以去执行他的任务对不对因为呢如果你去找我们的这个如果你去找我们的这个act instance这个表呢各位可以看到啊目前呢这里边start event就有两个了啊然后我们的张商也有两个了对吧
[01:57] 其中这个end time没有值是因为张商作为一个新的流程他没有执行我们的任务对吧所以我们在这边可以让张商执行完这个任务走好执行执行我们来看一下张商执行已经完成了张商完成我们再次回到表刷新对不对好这时候我们再来看一下张商这里边张商
[02:28] 张商啊不管是哪个张商啊他都已经完成了他的任务对不对好这个工作已经做完了啊那我们下一个步骤就应该是进入到呃李四对不对而李四呢各位可以看到目前呢这个李四他没有执行完这个任务啊部门经理省的时候对吧他还没有走啊那我们现在就可以让我们的李四来完成他的任务对不对好比如说这个时候假如说啊我们李四就登录到这个系统上面来了李四登录到系统之后呢李四一样的也在这里头
[02:57] 然后去看啊李氏一看一查我有没有任务啊李氏一查啊我有任务我有任务于是李氏就完成他的任务对吧我们这个时候执行李氏完成他的任务了完了我们这时候再刷新那这个时候各位就可以看到我们的李氏就已经完成了李氏就已经完成了任务啊这是他的这个任务的结束时间对吧那下一个再走各位同学你就可以看到这时候走的是总经理审批王武了对不对
[03:31] 王武他的这个结束时间还没有那为什么走的是王武呢是因为我们这一次这个请假天数是五天对不对五天是大于三的所以这个时候要走整经理当整经理走完才会进入到人事存档是吧所以呢这个时候我们再次回到这个变量的话各位同学可以看到啊我们再走那就应该是让王武去执行任务对不对让王武执行任务好我们同样让整经理整经理啊王武把他的任务完成
[04:00] 各位同学这个时候已经完成了啊然后我们再回到这边发现一下那总经理王武在这里面目前只会出现一次啊因为我们第一次跑的时候王武没走嘛那这个时候王武的这个结束时间就有了再走是不是走赵六啊那这时候走赵六那赵六一样的啊我们可以让我们的这个赵六完成他的任务对吧好copy啊再放到再来这样呢我们的赵六就完成了这个任务啊好这时候再走
[04:29] 那我们再回到这边来各位同学可以看到啊我们的这个照6两次有两次啊因为上次前面测试有一次嘛这一次照6是不是也完成任务了然后呢under event第一次under event这里面也有一次对不对我们走的应该是这个under event吧under event整体上我们到目前为止啊也就给各位把流程的另外一个峰值是往这个走的峰值也给各位啊从
[04:59] 从流程实力部署一个一个节点走走到这个地方的时候他判断判断完走总经理总经理然后再走人事存档最后结束对吧这个各位呢也给各位测试了一把

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中通过 Java 代码创建流程实例、设置变量、查询任务并完成任务，并通过 MySQL 数据库查看相关运行时数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Java 代码，用于获取流程引擎、任务服务，查询用户任务，并在任务不为空时完成任务并打印“任务执行完毕”。
画面 2: 展示了 Java 代码，用于获取流程引擎、运行时服务，设置流程变量（holiday），并启动流程实例。
画面 3: 展示了 Java 代码，用于获取流程引擎、运行时服务，设置流程变量（holiday），并启动流程实例。
画面 4: 展示了 Java 代码，用于获取流程引擎、运行时服务，设置流程变量（holiday），并启动流程实例。同时，下方的 Run 窗口显示了流程启动成功。
画面 5: 展示了 MySQL 的 Query 窗口，执行了删除数据库和创建数据库的 SQL 语句，并显示了 act_ge_bytearray 和 act_ru_variable 等表。
画面 6: 展示了 Java 代码，右键菜单中选中了“Copy as Main Test”。
画面 7: 展示了 MySQL 的 Query 窗口，显示了 act_ru_task 表中的任务数据，包括任务名称、分配人、开始时间等。
画面 8: 展示了 Java 代码，高亮了查询任务的代码行。
画面 9: 展示了 MySQL 的 Query 窗口，显示了 act_ru_task 表中的任务数据。
画面 10: 展示了 Activiti 的 BPMN 图，流程包含开始事件、用户任务、排他网关、服务任务和结束事件。右侧是元素面板。
画面 11: 展示了 Java 代码，右键菜单中选中了“Run VariableTestmain”。
画面 12: 展示了 MySQL 的 Query 窗口，显示了 act_ru_task 表中的任务数据。
画面 13: 展示了 MySQL 的 Query 窗口，显示了 act_ru_task 表中的任务数据。
画面 14: 展示了 Activiti 的 BPMN 图，流程包含开始事件、用户任务、排他网关、服务任务和结束事件。右侧是元素面板。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
//获取任务
public static void main(String[] args) {
    //1.得到ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取TaskService
    TaskService taskService = processEngine.getTaskService();
    //3.查询当前用户是否有任务
    String key = "myProcess_1";
    Task task = taskService.createTaskQuery().processDefinitionKey(key)
            .taskAssignee("zhaoliu").singleResult();
    if(task!=null){
        taskService.complete(task.getId());
        System.out.println("任务执行完毕");
    }
}
```

画面 2:
```java
//act_ge_bytearray
//act_ru_variable
public static void main(String[] args) {
    //1.得到ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(35);
    map.put("holiday", holiday);
    //4.启动流程实例，并且设置变量值
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
    //5.输出实例信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
}
```

画面 4:
```java
//act_ge_bytearray
//act_ru_variable
public static void main(String[] args) {
    //1.得到ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(35);
    map.put("holiday", holiday);
    //4.启动流程实例，并且设置变量值
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
    //5.输出实例信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
}
```

画面 5:
```sql
drop database activiti;
create database activiti;
act_ge_bytearray
act_ru_variable
```

画面 8:
```java
//3.查询当前用户是否有任务
String key = "myProcess_1";
Task task = taskService.createTaskQuery().processDefinitionKey(key)
        .taskAssignee("zhaoliu").singleResult();
```

画面 10:
```xml
<!-- BPMN 图中未显示具体 XML 配置 -->
```

画面 14:
```xml
<!-- BPMN 图中未显示具体 XML 配置 -->
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 10: BPMN 图中，开始事件（绿色圆圈）指向用户任务（绿色矩形），用户任务指向排他网关（菱形），排他网关指向服务任务（绿色矩形），服务任务指向结束事件（红色圆圈）。
画面 14: BPMN 图中，开始事件（绿色圆圈）指向用户任务（绿色矩形），用户任务指向排他网关（菱形），排他网关指向服务任务（绿色矩形），服务任务指向结束事件（红色圆圈）。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

