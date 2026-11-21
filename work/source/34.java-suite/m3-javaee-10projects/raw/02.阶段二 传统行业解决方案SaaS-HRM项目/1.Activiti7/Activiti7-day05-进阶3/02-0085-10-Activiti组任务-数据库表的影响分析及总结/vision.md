# 画面线理解：10-Activiti组任务-数据库表的影响分析及总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\10-Activiti组任务-数据库表的影响分析及总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:15, 00:19, 01:16, 01:38, 01:53, 02:35, 03:11, 03:19, 03:20, 03:26, 03:28, 03:30, 03:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:19:44

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中任务分配、候选人设置、任务交接和归还组任务等核心数据库操作与 Java 代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 页面“4.1.1.8 数据库表操作”，内容包括对 act_ru_task 表和 act_ru_identitylink 表的说明，以及它们在任务分配和候选人记录中的作用。
画面 2: 展示 SQLyog 数据库管理工具，执行 SQL 语句：drop database activiti; create database activiti;，用于创建或重置 Activiti 数据库。
画面 3: SQLyog 工具界面，显示数据库连接成功，但查询区域为空，左侧显示数据库表结构。
画面 4: PPT 页面“4.1.1.8 数据库表操作”，对 act_ru_identitylink 表中 TYPE 为 'candidate' 的记录进行高亮说明。
画面 5: SQLyog 工具界面，显示 act_ru_identitylink 表的数据，包含多个候选人记录。
画面 6: PPT 页面“4.1.1.8 数据库表操作”，对 act_ru_identitylink 表中 TYPE 为 'candidate' 的记录进行高亮说明。
画面 7: PPT 页面“4.1.1.8 数据库表操作”，对 act_ru_identitylink 表中 TYPE 为 'candidate' 的记录进行高亮说明。
画面 8: IDE 编辑器中显示 Java 代码，用于执行任务并打印“任务执行完毕”。
画面 9: PPT 页面“4.1 候选人”，说明在流程图中设置任务候选人的方法。
画面 10: PPT 页面“4.1 候选人”，在流程图中高亮显示“Candidate Users”属性设置为“zhangsan1”。
画面 11: PPT 页面“4.1.1.6 归还组任务”，展示 Java 代码用于将任务从个人归还给组。
画面 12: PPT 页面“4.1.1.7 任务交接”，展示 Java 代码用于将任务从当前负责人交接给候选人。
画面 13: PPT 页面“4.1.1.7 任务交接”，展示 Java 代码用于将任务从当前负责人交接给候选人。
画面 14: PPT 页面“4.1.1.7 任务交接”，展示 Java 代码用于将任务从当前负责人交接给候选人。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```sql
1 drop database activiti;
2 create database activiti;
```

画面 5:
```sql
ID REV GROUP_ID TYPE USER_ID TASK_ID PROC_INST_ID PROC_DEF_ID
2000 1 (NULL) participant zhangsan 2001 (NULL) (NULL)
2001 1 (NULL) participant zhangsan2 2002 (NULL) (NULL)
2002 1 (NULL) participant zhangsan3 2003 (NULL) (NULL)
```

画面 8:
```java
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //3.执行查询任务
    Task task = taskService.createTaskQuery()
            .taskAssignee("zhangsan")
            .singleResult();
    //4.执行任务
    if(task != null){
        taskService.complete(task.getId());
        System.out.println("任务执行完毕!");
    }
}
```

画面 11:
```java
@Test
public void setAssigneeToGroupTask() {
    // 查询任务使用TaskService
    TaskService taskService = processEngine.getTaskService();
    // 当前待办任务
    String taskId = "6004";
    // 任务负责人
    String userId = "zhangsan2";
    // 校验userId是否是taskId的负责人，如果是负责人才可以归还任务
    Task task = taskService.createTaskQuery().taskId(taskId)
            .taskAssignee(userId).singleResult();
    if (task != null) {
        taskService.setAssignee(taskId, userId);
    }
}
```

画面 12:
```java
@Test
public void setAssigneeToCandidateUser() {
    // 查询任务使用TaskService
    TaskService taskService = processEngine.getTaskService();
    // 当前待办任务
    String taskId = "6004";
    // 任务负责人
    String userId = "zhangsan2";
    // 将此任务交给其它候选人办理任务
    String candidateuser = "zhangsan";
    // 校验userId是否是taskId的负责人，如果是负责人才可以归还任务
    Task task = taskService.createTaskQuery().taskId(taskId)
            .taskAssignee(userId).singleResult();
    if (task != null) {
        taskService.setAssignee(taskId, candidateuser);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 9:
标题：“4.1 候选人”
内容：说明在流程图中任务节点的配置中设置 candidate-users(候选人)，多个候选人之间用逗号分开。
流程图结构：
- Start-event → 任务节点（配置 candidate-users: zhangsan1）
- 任务节点 → End-event

画面 10:
标题：“4.1 候选人”
内容：在流程图中高亮显示“Candidate Users”属性设置为“zhangsan1”。
流程图结构：
- Start-event → 任务节点（配置 candidate-users: zhangsan1）
- 任务节点 → End-event

画面 11:
标题：“4.1.1.6 归还组任务”
内容：说明如果个人不办理该任务，可以归还任务，归还后该用户不再是该任务的负责人。
流程图结构：无。

画面 12:
标题：“4.1.1.7 任务交接”
内容：说明任务交接，任务负责人将任务交给其它候选人办理该任务。
流程图结构：无。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
