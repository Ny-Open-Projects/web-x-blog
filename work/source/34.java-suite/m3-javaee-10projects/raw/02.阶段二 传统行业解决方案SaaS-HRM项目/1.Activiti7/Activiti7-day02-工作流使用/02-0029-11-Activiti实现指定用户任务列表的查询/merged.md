# 11-Activiti实现指定用户任务列表的查询

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\11-Activiti实现指定用户任务列表的查询_【海量资源尽在 ubkz.com】.mp4
- 时长 10分8秒（音频 609s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那在我们把这个流程实例启动之后下一个任务我们就可以进入到我们的个人用户的一个任务查询什么意思就是每个负责人或者是每个用户这个流程实例中的每一个用户将来在执行某一个操作之前他需要先查一下他自己是否有任务要去执行比如说我们回到这个里头
[00:29] 我们当时填写请假单想说这个任务是张商去做的话那张商在进入到系统之后那张商就应该可以查到他自己是否有任务需要去执行对吧或者说到这个部分我们的部门经理当他如果说部门经理要去做任务的时候他首先也需要去查询他自己是否有任务对不对当他有任务的时候那他就需要去执行这个任务
[00:59] 所以我们应该是分两个步骤来看啊那第一个步骤就是先做任务的查询第二个步骤就是做任务的处理那现在我们先啊来走一下这个任务查询那任务查询呢各位我们从这里头基本上也可以看出来啊它主要用到的是我们的另外的一个Service是叫做task servicetask Service将来调用它的collate task query方法就可以得到
[01:28] 就再去根据我们的这个流程定义的key啊以及我们的负责人对吧就可以得到我们当前这个用户要去执行的任务有哪些这样我们就可以查询到一个列表然后呢我们后续再通过这个列表的一些数据的展示我们就可以啊真实显示出我们的这个列用户的这个执行任务数据这个就是大概的一个思路啊
[01:54] 下面我们也一起编码来实现这个效果再次回到我们的这个包厦现在我就可以再去比如说再去新建一个新的class叫做activity我们这里头主要是查询叫做task query这样我们基本上就可以创建出一个这样的类它的主要作用就是
[02:23] 查询当前用户的任务列表这就是我们要完成的工作下面我们就可以具体来实现具体的步骤有些代码我可以借助于前期我们这边所写的一些代码比如说task query我这个卖方法我就不去重新打了然后这里边的这一堆内容肯定要改的
[02:54] 那我们都已经拿到了这个process engine下一步我们就应该是叫做得到我们的叫做task Service得到一个这样的对象那再去往后呢我们就应该去我们就应该去使用我们的这个实现我们的这个具体的第三个就是将得到task Service的对象第三个就是根据
[03:26] 我们的这个流程定义的key啊以及我们的这个负责人负责人啊也就是我们的这个assign对吧也是我们的这个assign然后呢通过这两个通过这两个啊我们就可以来实现我们的这个任务的查询啊那我们这个时候再回到这边来啊assign实现来实现
[03:56] 当前用户当前用户的任务列表查询这就是我们要完成的第三个工作那第四个工作主要就是完成我们的任务列表的展示对吧任务列表的展示完成这个工作这是我们大致上分这几个步骤来走第一个步骤就是process engine对吧那有了process engine我们就可以通过我们的process engine
[04:26] 去调用它的getTaskService这样我们就可以得到一个TaskService的具体的实例对吧TaskService好这样就搞定了然后它的下一个步骤我们就希望用这个Service去调用它的调用它的TaskCurric的方法比如说我们这个时候就可以用TaskService.createTaskCurric
[04:55] 这样我们就可以去得到一个任务列表的查询对象通过这个查询对象呢我们可以进一步在这里打点去调用比如说我们将来还有还有设置我们的这个条件嘛对吧就是我们的这个流程流程定义的key以及我们的执行者对吧那这个时候我们就再回到这边叫点流程啊是process定义对吧process
[05:23] 定义是definition而我们要根据我们流程定义的key是不是而这个key我们用的是请假这一套流程请假这一套流程用的是holiday对吧这样我们就搞定了这个process definitionkey的设置还有一个就是我们的这个任务将来到底是交给具体的某一个执行者对吧那这个时候我们就可以进一步去调用它的点叫做task or sign对吧
[05:52] 那我们这一次这个task assign应该是交给我们的这个张商对不对那这个时候我就写上张商啊好然后呢再上去再让他去做这个查询这时候我们就调用他的类似的方法那类似的方法查询的这个结果呢就会是一个我们想要的这个类似的列表所以呢我这个时候用一个类似的列表比如说我们就是叫做task list这样我们就查到了一个任务列表
[06:22] 当我们的任务列表确定了那下一步我就可以去使用循环对吧来便利我们的这个任务列表啊task 冒号类似的task类似的这样呢我们就可以去便利出我们的这个任务列表中的每一项任务啊每一个任务那每个任务我就可以用sout来实现我们这个任务信息的输出对吧你比如说这次我们就可以task点get好
[06:50] 比如说我们要去输出process比如说我们要去输出我们的这个process相关的一些信息啊包括我们哪些内容我们一起来看一下流程实例任务负责人名称对吧那我们这一次呢也可以按照这个套路来搞啊我在这里头应该是第一个是叫做我们的叫做流程实例对吧好流程实例ID啊除了这个流程实例ID我们看看还有没有其他项对吧
[07:19] 应该还会有其他项啊那我们看一下这个其他项包括有哪些内容呢对吧我先给他多搞几个过来啊然后呢好这样我们基本上就有了四项啊那我们来看一下这里头包括有流程实例的ID任务ID负责人名称我们把这个部分给他改一下啊流程实例的ID然后还有我们的这个任务的ID对吧任务的ID
[07:52] 还有我们的这个名称是吧我再看一下啊负责人的名称啊任务负责人和我们的这个任务名称对吧好叫做任务负责人啊还有一个就是叫做任务名称对吧我们把这个地方全都给它改号啊任务名称那这四项要输出那现在呢我们就可以直接到这边呢
[08:22] 去调用我们task点叫做get我们来看一下有一个process instance id是不是那翻译过来就是叫做流程实例的id对吧那除了这个我们还有一个就是任务自己本身也是有id对吧比如说任务自己本身的id对吧然后呢还有一个就是它的这个负责人我们继续调用这个task点get叫做assign对吧get
[08:52] 三引这一下还有最后一个就是我们的这个任务的名称对不对我们这个时候再去打点叫get看一下啊task name好没有啊那么应该就直接get name对吧这样我们就把这个任务的详细信息可以做一个输出展示那这是我们呢在这里边啊实现的我们的这个流程当前用户的这个任务列表的查询对吧
[09:22] 我们也一起来执行一下这个效果啊好我们看一下好这时候呢各位就可以看到我们当前呢就有一堆输出的内容对吧这个时候应该这个任务的执行者就是张商对不对他要完成的任务就是把请假单要填好对吧那现在我们应该说就完成了当前这个张商这个用户他自己有的任务他现在的这个任务名称就是要去做一个
[09:56] 填写请假单的工作吧这是我们在这边呢给各位实现我们当前用户任务列表的一个查询工作啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Activiti 工作流引擎查询当前用户待办任务的 Java 代码实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示“5.4 任务查询”章节，代码片段为查询个人待办任务的方法 findPersonalTaskList()，其中任务负责人设为 "zhangsan"。
画面2：展示创建 TaskService 的代码，使用 processEngine.createTaskQuery() 并设置 processDefinitionKey 为 "myholiday01" 和 taskAssignee 为 "zhangsan"。
画面3：展示 Activiti Designer 的 BPMN 图编辑界面，包含 StartEvent、UserTask 和 EndEvent，右侧为元素面板。
画面4：展示 ActivitiTaskQuery.java 文件的开头部分，导入了 Activiti 的核心包。
画面5：展示 ActivitiTaskQuery.java 文件中 main 方法的开头，获取 ProcessEngine 对象。
画面6：展示在 main 方法中调用 processEngine.getTaskService() 获取 TaskService 对象。
画面7：展示调用 taskService.createTaskQuery() 创建任务查询对象。
画面8：展示调用 .processDefinitionKey("holiday") 设置流程定义键。
画面9：展示调用 .taskAssignee("zhangsan") 设置任务负责人。
画面10：展示 for 循环遍历任务列表，并打印流程实例 ID、任务 ID、任务负责人和任务名称。
画面11：展示“5.5 任务处理”章节标题，说明任务负责人查询并处理任务。
画面12：展示 ActivitiTaskQuery.java 文件中 main 方法的完整代码，包含创建 TaskService、创建查询对象、设置流程定义键和任务负责人、遍历并打印任务信息。
画面13：展示运行程序后控制台输出的调试日志，包含 SQL 语句执行和任务查询结果。
画面14：展示运行程序后控制台输出的最终结果，显示了流程实例 ID、任务 ID、任务负责人和任务名称。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
// 查询当前个人待执行的任务
@Test
public void findPersonalTaskList() {
    // 任务负责人
    String assignee = "zhangsan";
}
```

画面2：
```java
// 创建TaskService
TaskService taskService = processEngine.getTaskService();
List<Task> list = taskService.createTaskQuery()//
        .processDefinitionKey("myholiday01")//
        .taskAssignee(assignee)//只查询该任务负责人的任务
        .list();
for (Task task : list) {
```

画面4：
```java
package com.ithema.activiti;
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.RuntimeService;
import org.activiti.engine.TaskService;
```

画面5：
```java
public class ActivitiTaskQuery {
    public static void main(String[] args) {
        //1.得到ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    }
```

画面6：
```java
//2.得到TaskService对象
TaskService taskService = processEngine.getTaskService();
```

画面7：
```java
//3.根据流程定义key,在该流程定义下查询当前用户的任务列表
taskService.createTaskQuery()
```

画面8：
```java
//4.设置流程定义key
.processDefinitionKey("holiday")
```

画面9：
```java
//5.设置任务负责人
.taskAssignee("zhangsan")
```

画面10：
```java
for (Task task : list) {
    System.out.println("流程实例ID：" + task.getProcessInstanceId());
    System.out.println("任务ID：" + task.getId());
    System.out.println("任务负责人：" + task.getAssignee());
    System.out.println("任务名称：" + task.getName());
}
```

画面12：
```java
public class ActivitiTaskQuery {
    public static void main(String[] args) {
        //1.得到ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService对象
        TaskService taskService = processEngine.getTaskService();
        //3.根据流程定义key,在该流程定义下查询当前用户的任务列表
        List<Task> taskList = taskService.createTaskQuery()
                .processDefinitionKey("holiday")
                .taskAssignee("zhangsan")
                .list();
        //4.遍历任务列表并打印
        for (Task task : taskList) {
            System.out.println("流程实例ID：" + task.getProcessInstanceId());
            System.out.println("任务ID：" + task.getId());
            System.out.println("任务负责人：" + task.getAssignee());
            System.out.println("任务名称：" + task.getName());
        }
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PPT 标题为“5.4 任务查询”，下方有文字说明“流程启动后，各各任务的负责人就可以查询自己当前需要处理的任务，查询出来的任务都是该用户的待办任务。”
画面10：PPT 标题为“5.5 任务处理”，下方有文字说明“任务负责人查询待办任务，选择任务进行处理，完成任务。”
画面3：BPMN 图中 StartEvent 指向 UserTask，UserTask 指向 EndEvent。右侧元素面板列出各种 BPMN 元素。
画面13：控制台输出调试日志，包含 SQL 语句执行和任务查询结果。

5) 无。

