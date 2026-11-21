# 10-Activiti组任务-数据库表的影响分析及总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\10-Activiti组任务-数据库表的影响分析及总结_【海量资源尽在 ubkz.com】.mp4
- 时长 3分34秒（音频 215s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:04] 好,下面我们一起再给各位来分析一下,我们在做这个任务拾取,以及我们任务交接,这样的一些工作的时候,其实真正本质上影响的,不只是我们的这个ActUnsuch,这个表,这个表呢,它已经是一个历史的记录表了,对吧,而真正影响的表还会有像我们的这个RU Task,我们的任务表,我们的任务表中的这个Assign的取值肯定是会变的,
[00:34] 假如说现在我们是部门经理审核的话那早期如果这个人是张商的话那我们做任务交接的时候张商就会变成理事对吧如果说我们这个人是部门经理而这个人assign早期是在空为空职的时候如果我们去做任务拾取的时候任务拾取的过程其实也就是为给我们的这个assign负值的一个过程所以说我们真正
[01:01] 将来在这边不管是做任务拾取还是做任务的交接或者是做任务的归还其实真正本质就是要去改变的是ACTRU task这个表中我们的这个assign的取值对不对当然我们在这个地方还有一个就是我们的这个ACTRU identity link这个表呢将来各位也是要注意的啊这个表呢早期我们假如说我们的这个用户是一个候选人的话他在这个表中
[01:29] 真正它的取词是一个Countedact这个地方也是我们特别要注意的地方我们可以看一下叫做Adandidate Link这个时候各位可以看到我们的这个我们的这个李氏现在目前他是一个参与者对吧如果说我们将来他只是候选人的话那这个他不是这个不是这个当词那他应该是叫做Countedact是这个取词这一点的各位也是要注意的当然我们
[01:58] 最终影响的还会有我们的历史记录对吧历史记录表也一样的会有变化所以我们可以一起来看一下这是我们目前找的这张表我们可以看一下我们的identity的历史记录表各位这个时候你就可以看到我们的张商曾经就是一个候选人对不对我们的李四曾经也是一个候选人但是现在的李四由候选人已经变成了我们的真正的任务执行人
[02:28] 变成一个真正的参与者对不对所以说这个部分是我们特别要去注意的一个地方这是我们的这是我们用户由候选用户变成我们真正的这个用户负责人之后真正我们的这个表中也是特别有记录的主要呢我们做这个任务拾取以及我们这个任务的这个任务的这个转交主要影响的这个表大概就是这样的
[02:57] 我们关于我们的这个主任务在这里面主要就给各位啊介绍到这里面那我们这个部分呢给各位介绍的主要就是我们的这个Conditech的Uter我们在这个部分大体上啊这个章节呢主要就是设置了我们的这个Conditech的Uter来实现我们主任务的主任务的设置以及我们主任务的这个拾取对吧主任务的这个归还
[03:26] 和任务的交接这个环节啊我们大致上啊就给各位啊完全介绍完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

