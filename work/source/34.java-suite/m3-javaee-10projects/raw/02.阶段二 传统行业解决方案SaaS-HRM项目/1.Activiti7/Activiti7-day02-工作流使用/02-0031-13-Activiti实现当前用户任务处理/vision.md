# 画面线理解：13-Activiti实现当前用户任务处理

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\13-Activiti实现当前用户任务处理_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:28, 00:33, 01:04, 01:08, 01:22, 02:26, 02:59, 03:16, 04:12, 04:41, 04:47, 04:50, 06:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:26:46

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
