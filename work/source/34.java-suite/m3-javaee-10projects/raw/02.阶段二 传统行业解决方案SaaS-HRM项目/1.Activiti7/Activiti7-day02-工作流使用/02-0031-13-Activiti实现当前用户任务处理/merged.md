# 13-Activiti实现当前用户任务处理

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\13-Activiti实现当前用户任务处理_【海量资源尽在 ubkz.com】.mp4
- 时长 6分13秒（音频 373s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那刚才我们已经完成了当前这个用户任务列表的一个展示对吧那我们接着往后去做的话各位同学可以思考啊那肯定就是既然他查到他有自己的任务对吧那下一步他就会把自己的任务给他处理掉了对吧所以呢这个时候我们要一起来学习一下在我们的这个activity工作流的过程中怎么样去将自己当前的这个任务给他处理掉了对吧
[00:28] 那好我们现在呢就继续到这边呢比如说我这样做到这个里头我去我去执行一下我们直接把这个名称给他改一下把这个内名给他改一下那这个人应该就是activity task的不是查询的对吧就是叫做task的完成对吧叫做complete完成这个任务叫activity complete task完成任务对不对
[00:58] 翻译过来的啊那下面呢我们就叫做ok对吧好这样呢我就有了一个这样的类啊在这个类里头一样的我们这些步骤性的内容呢肯定是有一些改变的啊那像我们第一步process engine这个是不需要再去改变的啊而刚才我们当我们得到这个任务的时候下一步只需要去调用这个任务的处理处理完的一个方法啊
[01:27] 那这个地方就是叫做处理处理我们的这个任务那具体你处理的是哪一个任务呢那这个部分如果说我们结合我们结合结合用户查询叫做当前用户任务列表的查询操作的话如果我们结合这个操作的话
[01:58] 那应该说通过前一个操作呢我们已经完成了当前用户有哪些任务的一个查询对不对那既然都已经完成了这个用户任务的查询那我们想一想那这个任务的ID号是不是就已经查到了任务的ID号就已经查到了当任务的ID号都有的情况下那我们这个时候看一下在我们的这个task和Service中其实呢这个时候我们
[02:27] 就可以直接去调用它有一个叫做complete这样的一个方法这样的一个方法那这个方法里头啊要求传入一个字幕创那我们就可以直接写上一个字幕创而我这一次2505就是刚刚我们所查询到的一个具体的任务对不对那这样我们就完成了当前这个用户啊对于他自己任务的一个处理对吧
[02:57] 当然这个过程啊这个过程呢如果咱们同学要写的更详细一些的话啊那我们这个地方呢应该是把我们任务列表的查询工作和我们去完成这个任务是结合在一起的对吧应该是结合在一起啊应该写代码就写在一起了对吧好那我先呢在这里头我们刚才已经分布啊先实现了这个任务的ID的查询对吧
[03:23] 那现在我就直接可以把任务的ID2505直接传到这里头来那这个我们的任务我们的这个任务就被处理完了你要注意啊那个这个任务处理完了那你想想会不会影响我们数据库的一些表呢对吧那如果啊咱们能够想得起开始我给各位啊讲的一些内容的话那我就认为啊我们这个地方我们这个地方呢现在肯定是需要对于我们
[03:54] 数据库表做一些处理比如说我们原来填写请单因为这个任务张商没有执行或者说张商没有完成所以我们对这个end time他就不知道什么时候把这个任务做完了但是我们现在把这一行代码写上之后那是不是意味着我们的2505的任务2505的任务2505的任务
[04:24] 那现在它的这个状态就应该是已经完成了对吧如果是已经完成了它的这个它的这个end time肯定是有一个值对不对好这是我在这里头给各位啊分析的一个情况啊那下面呢我们可以一起来看一下啊好现在我再去执行一下这个操作好这边呢这边它就已经把我们的这个任务已经完成了啊
[04:54] 那完成了我们要关注的是我们的数据库的一些表的变化情况对不对好我们可以一起来看一下比如说再回到这个地方再回到这个地方我们这个时候就可以来看一下填写请假单对不对填写请假单开始了我们在填写请假单的时候刚才我们的这个任务的开始时间是有的结束时间你看看早期是没有的现在也有了对吧
[05:22] 这就说明呢我们已经把单前的这个任务已经执行完了而且呢这个表中又多出了一条记录那就是现在已经因为张商已经完成了这个填写请假单的工作所以他的下一个环节自然就是部门经理的环节了对吧所以我们这个时候看到表里头立即就多了一条记录是我们的部门经理开始要进行审批了但是你想部门经理现在审批了吗对吧部门经理现在是应该也是
[05:51] 还没有开始审批对不对所以它只有个开始这个任务因为它还没有完成所以它的end time还是没有值这个就是我们在这里头给各位大致上讲了一下我们当前的用户如何去把自己的一个任务给它处理掉了对吧大致的思路就是这样的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码调用 Activiti 工作流引擎的 TaskService 来查询和完成任务。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 ActivitiTaskQuery.java 文件，代码用于查询指定流程定义键和任务负责人的任务列表，并打印任务的流程实例ID、任务ID、负责人和名称。
画面2: 同画面1，代码高亮部分为任务查询逻辑。
画面3: 同画面1，鼠标悬停在 ActivitiTaskQuery.java 文件上。
画面4: 展示 ActivitiCompleteTask.java 文件，代码用于获取 ProcessEngine 和 TaskService 对象。
画面5: 同画面4，代码高亮部分为获取 TaskService 对象。
画面6: 同画面4，代码高亮部分为获取 TaskService 对象。
画面7: 同画面4，代码高亮部分为调用 TaskService 的 complete 方法。
画面8: 展示 PPT 页面，标题为“完成任务”，内容为一个 @Test 方法，用于完成指定 ID 的任务。
画面9: 同画面4，代码高亮部分为调用 TaskService 的 complete 方法。
画面10: 同画面4，代码高亮部分为调用 TaskService 的 complete 方法。
画面11: 同画面4，代码高亮部分为调用 TaskService 的 complete 方法。
画面12: 同画面4，代码高亮部分为调用 TaskService 的 complete 方法。
画面13: 同画面4，代码高亮部分为调用 TaskService 的 complete 方法。
画面14: 同画面8，PPT 页面展示“完成任务”的代码示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
List<Task> tasklist = taskService.createTaskQuery()
		.processDefinitionKey("holiday")
		.taskAssignee("zhangsan")
		.list();
//4.任务列表遍历
for(Task task : tasklist){
	System.out.println("流程实例ID:"+task.getProcessInstanceId());
	System.out.println("任务ID:"+task.getId());
	System.out.println("任务负责人:"+task.getAssignee());
	System.out.println("任务名称:"+task.getName());
}
```

画面4:
```java
import ...
public class ActivitiCompleteTask {
	public static void main(String[] args) {
		//1.得到ProcessEngine对象
		ProcessEngine processingEngine = ProcessEngines.getDefaultProcessEngine();
		//2.得到TaskService对象
		TaskService taskService = processingEngine.getTaskService();
		//3.处理任务，结合当前用户任务列表的查询操作的话，任务ID:2505
		taskService.
	}
```

画面5:
```java
//2.得到TaskService对象
TaskService taskService = processingEngine.getTaskService();
//3.处理任务，结合当前用户任务列表的查询操作的话，任务ID:2505
for(Task task : tasklist){
	System.out.println("流程实例ID:"+task.getProcessInstanceId());
	System.out.println("任务ID:"+task.getId());
	System.out.println("任务负责人:"+task.getAssignee());
	System.out.println("任务名称:"+task.getName());
}
```

画面7:
```java
//3.处理任务，结合当前用户任务列表的查询操作的话，任务ID:2505
taskService.complete("2505");
```

画面8:
```java
//完成任务
@Test
public void completTask(){
	//任务id
	String taskId = "8305";
	//创建TaskService
	TaskService taskService = processEngine.getTaskService();
	//完成任务
	taskService.complete(taskId);
	System.out.println("完成任务id="+taskId);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8: PPT 标题为“完成任务”，内容为一个 @Test 方法，用于完成指定 ID 的任务。

5) 不要评价画面美观，不要输出与课程无关的内容。

