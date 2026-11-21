# 07-Activiti7新API介绍及分析-TaskRuntime分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\07-Activiti7新API介绍及分析-TaskRuntime分析_【海量资源尽在 ubkz.com】.mp4
- 时长 10分35秒（音频 635s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:04] 那好,我们下面一起再来学习我们的Task Runtime这个接口我们学习Task Runtime这个接口一样我们也需要找到我们的官方的参考文档官方参考文档是这样去说的So if you are building business applications如果你要去构建你的业务用用你要创建
[00:31] 创建任务为我们的用户或者是组在我们的组织中是吧在我们的组织中需要为用户或组去创建任务的话Is something that you might find handy也就是说你将会变得非常的容易你将会发现非常容易这些Task Runtime API are here to help you
[00:57] 就是说我们的这个task run time将会为你提供很多帮助具体的我们可以参考对应的这样的一个这里面的这个示例来实现然后呢它说这coding from this section就是说我们的这个我们的这部分的代码你将可以通过这样的一个example对吧的mywin模块去找到然后我们这一次运行
[01:29] You are running inside a Spring Boot我们将会使用我们的 Spring Boot一起来整合运行对吧如果你要用 Spring Boot的话我们 needed to aid就必须要去添加我们的activity boot start对吧要添加这个startdefinitive添加相关的activity与Spring Boot整合的start的依赖and DB driver
[01:58] 以及我们的数据库的驱动或者你可以使用我们的H2内存的数据存储系统对应的部分就是我们所添加的activity Supreme boot start所对应的depy对应的依赖这个部分是我们的H2的数据库当然我们
[02:22] 这次肯定用的是MySQL数据库所以说我们这个部分后面还会做一些改变同时它在这里边还可以去添加我们的activity本身所需要用到的一些依赖好这样做好我们就可以在我们的程序中整UVLBeableTo你就可以使用我们的taskLongTime了怎么去使用
[02:51] 那就是这种用ETAWORD的注解来实现注入TaskRuntime的值下面部分就是关于我们的TaskRuntime它所对应的源代码对不对关于源代码我们一会也去分析一下然后当我们看完源代码比如说我们这个再走那好比如说For exampleYou can create a task by doing就是你将可以
[03:21] 创建一个任务然后去执行对不对怎么去做我们可以通过task runtime的grid方法对吧然后里头写的是什么写的是我们的 task task-perioding-builder.grid方法这个部分就可以用一系列的位置来实现我们去添加相关的一些相关的一些activity运行比如说activity
[03:50] 运行的名称以及activity的描述信息它的主信息对吧这样以及它的这个优先级对吧primary都可以进行设置这是这个部分然后再往后往后往后走咱们这个部分还可以还可以在这里面去做更多的工作你可以看到在这个部分它是去输出一些信息
[04:16] 输出一些我们的任务的分配人任务的执行人是这样的这个部分基本上我就给各位看这个官方文档就大概是从我们的坐标引路到我们的源代码到后面我们怎么样去使用我们的task runtime来实现我们的创建任务然后在这后面我们可以去查看我们的任务的
[04:46] 真正的任务真正的执行人或者叫负责人这是我们这一块给各位所看的内容除了看官方文档我们也一样的可以再次回到我们的之前我这里头有这一个工程但如果说有同学说我没有这个工程没关系我们只要搞一个类对不对然后把我们的 task runtime给他ata all the will放进来
[05:15] 因为我真正关注的是对应的task runtime这个类它真正所对应的具体它所对应的具体的实践类它的实践类我们现在是想去看一下它实践类的源码如果说光去看它本身的源码的话它只是一个接口对吗这里边看的信息是有限的我们只能够看到一些方法的声明对不对其他看不着
[05:45] 我们看它的实现内的话各位同学你就可以看到我们的Task Runtime Employment同样也是继承了我们的Task Runtime这个接口我们也可以发现要去做这个工作它也一样与我们的Spring Security整合的是非常的严密的或者说严或者是这种高度的偶合在一起
[06:13] 我们也可以发现这里面有我们想要的一个Service就是我们的task Service这个task Service代表的就是我们要去将来要去执行任务的话其实主要就是靠我们的task Service来执行我们的任务对不对这里面各位这个时候你就可以去找一找真正我们将来要去做更多操作的时候
[06:44] 应该内部用的是我们的 task Service看见了吗这是如果你要做查询查询我们目前有哪些任务我们用的是 task Service的GlueD task queue这样的代码其实我们在早期前面的课程中都给各位讲过了只不过我们的activity7在这里头它进行了进一步的封装各位还可以看到我们
[07:12] 我们的任务是这样的我们的任务具体你看看这个地方是我们的clam拾取任务对吧拾取任务它也是调用的这一次task里头的方法我们可以看到task这个方法你把task id传给我对吧我们可以去找一下或者看一下
[07:41] 他这个人是得到这个部分的信息这个人各位还是可以看到他是调用这次task Service的cruelty task query对吧查到通过这种方式我们可以得到一个curry对象通过curry对象进一步去设置更多的条件从来实现查询对吧所以说他的本质还是用task Service来调用不同的方法
[08:11] 从而实现我们查询的工作对吧你看看这里边如果我们要去完成一个任务的话我们也去看一下它的圆满各位我们要去完成一个任务的话这个部分又是怎么去做的它是调用的是JS task Service的complete方法这个代码其实我们在早期给各位介绍API的时候也是完全学习过的
[08:40] 通过刚才我们对于这个实现类的一些方法的分析其实咱们同学应该已经体验到一个点就是咱们的我们的这个task runtime这个接口只是对于我们早期原生的这样的一些Service中方法的封装对不对他全都给我们再封装了一次所以就变成了我们将来用用他的这个task runtime就可以了
[09:09] 那这个部分呢主要是给各位分享一下我们的这个activity core部分它真正所对应的这个task runtime也好或者是我们的process runtime也好那我们会发现它真正的本身其实就是对于我们activity早期的这样的一堆Service是进行了一个封装对吧好
[09:38] 这部分我们一定要记住的内容跟各位说一下就是我们在使用我们的task runtime之前一定要去引入相关的坐标对吧然后引好坐标我们第二个步骤就是我们要去使用的是ata auto will来实现task runtime真正住值一旦它住好值后面我们只需要去调用它里头的方法就可以来实现我们的
[10:05] 流程的比如说我们要去查询有没有任务对吧我们要去做我们要去做我们的这个任务的拾取或者任务的完成都是调task runtime里头的方法来完成的好这样我们基本上就把activity7的这一堆主要两个API给各位详细说明了一下后面我们就可以直接去使用它了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti7 中 TaskRuntime API 的使用方法，包括如何通过 Spring Boot 项目集成、创建任务、监听任务事件以及查看其底层实现代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“2.5.2 TaskRuntime 接口”，介绍 TaskRuntime API 的作用，并给出 GitHub 示例地址和 Maven 依赖配置。
画面2：展示 GitHub 文档，说明如何使用 TaskRuntime API，包括注入 TaskRuntime Bean 的代码示例和接口定义。
画面3：展示 GitHub 文档，说明如何创建任务的代码示例，以及任务可见性、用户角色权限要求。
画面4：展示 GitHub 文档，说明如何注册 TaskRuntime 事件监听器，以及 ProcessRuntime API 的引入。
画面5：重复画面2的内容，展示 TaskRuntime Bean 注入和接口定义。
画面6：重复画面4的内容，展示 TaskRuntime 事件监听器注册和 ProcessRuntime API。
画面7：展示 IDEA 编辑器中的 TaskRuntime 接口定义代码，包含任务创建、查询、完成等方法。
画面8：展示 IDEA 编辑器中的 TaskRuntimeImpl 类的源码，包含构造函数和任务查询方法。
画面9：展示 IDEA 编辑器中的 TaskRuntimeImpl 类的源码，包含任务完成方法。
画面10：重复画面8的内容，展示 TaskRuntimeImpl 类的构造函数和任务查询方法。
画面11：重复画面9的内容，展示 TaskRuntimeImpl 类的任务完成方法。
画面12：重复画面1的内容，展示 PPT 页面“2.5.2 TaskRuntime 接口”。
画面13：重复画面1的内容，展示 PPT 页面“2.5.2 TaskRuntime 接口”。
画面14：展示 PPT 页面“第3章 Activiti7 与 Spring Boot 整合开发”，总结前文内容并引出下一章。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring-boot-starter</artifactId>
    <version>7.0.0.Beta2</version>
    <scope>import</scope>
    <type>pom</type>
</dependency>
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>

画面2：
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-dependencies</artifactId>
    <version>7.0.0.Beta2</version>
    <scope>import</scope>
    <type>pom</type>
</dependency>

画面3：
taskruntime.create(
    taskPayloadBuilder.create()
        .withName("First Team Task")
        .withDescription("This is something really important")
        .withAssignee("activitiTeam")
        .withPriority(10)
        .build());

画面4：
@Bean
public TaskRuntimeEventListener taskAssignedListener() {
    return taskAssigned -> logger.info(
        ">>> Task Assigned: " + taskAssigned.getTask().getName()
        + " - He can send a notification to the assignee: "
        + taskAssigned.getTask().getAssignee());
}

画面5：
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-dependencies</artifactId>
    <version>7.0.0.Beta2</version>
    <scope>import</scope>
    <type>pom</type>
</dependency>

画面6：
@Bean
public TaskRuntimeEventListener taskAssignedListener() {
    return taskAssigned -> logger.info(
        ">>> Task Assigned: " + taskAssigned.getTask().getName()
        + " - He can send a notification to the assignee: "
        + taskAssigned.getTask().getAssignee());
}

画面7：
public interface TaskRuntime {
    TaskRuntimeConfiguration configuration();
    Task task(String taskId);
    Page<Task> tasks(Pageable var1, GetTasksPayload var2);
    Task create(CreateTaskPayload var1);
    Task claim(ClaimTaskPayload var1);
    Task release(ReleaseTaskPayload var1);
    Task complete(CompleteTaskPayload var1);
    Task update(UpdateTaskPayload var1);
    Task delete(DeleteTaskPayload var1);
    List<VariableInstance> variables(GetTaskVariablesPayload var1);
    void setVariables(SetTaskVariablesPayload var1);
}

画面8：
public TaskRuntimeConfiguration configuration() { return this.configuration; }
public Task task(String taskId) {
    String authenticatedUserId = this.securityManager.getAuthenticatedUserId();
    if (authenticatedUserId == null && this.securityManager.isAuthenticationEnabled()) {
        List<String> userRoles = this.userGroupManager.getUserRoles(authenticatedUserId);
        List<String> userGroups = this.userGroupManager.getUserGroups(authenticatedUserId);
        org.activiti.engine.task.Task internalTask = (org.activiti.engine.task.Task)(TaskQuery).taskId(taskId).singleResult();
        if (internalTask == null) {
            throw new NotFoundException("Unable to find task for the given id: " + taskId + " for user: " + authenticatedUserId);
        } else {
            return this.taskConverter.from(internalTask);
        }
    } else {
        throw new IllegalStateException("There is no authenticated user, we need a user authenticated to perform this operation");
    }
}

画面9：
public List<VariableInstance> variables(GetTaskVariablesPayload getTaskVariablesPayload) {
    return this.variableInstanceConverter.from(this.taskService.getVariables(getTaskVariablesPayload.getTaskId()));
}

public Task complete(CompleteTaskPayload completeTaskPayload) {
    String authenticatedUserId = this.securityManager.getAuthenticatedUserId();
    Task task;
    try {
        task = this.task.completeTaskPayload.getTaskId();
        if (task.getAssignee() != null && !task.getAssignee().isEmpty()) {
            throw new IllegalStateException("You cannot complete the task if you are not assigned to it");
        } else {
            taskImpl computedTaskData = new TaskImpl(task, task.getName(), TaskStatus.COMPLETE);
            this.taskService.completeTask(completeTaskPayload.getTaskId(), computedTaskData);
        }
    } catch (IllegalStateException e) {
        throw new IllegalStateException("The authenticated user cannot complete task" + completeTaskPayload.getTaskId());
    }
}

画面10：
public TaskRuntimeConfiguration configuration() { return this.configuration; }
public Task task(String taskId) {
    String authenticatedUserId = this.securityManager.getAuthenticatedUserId();
    if (authenticatedUserId == null && this.securityManager.isAuthenticationEnabled()) {
        List<String> userRoles = this.userGroupManager.getUserRoles(authenticatedUserId);
        List<String> userGroups = this.userGroupManager.getUserGroups(authenticatedUserId);
        org.activiti.engine.task.Task internalTask = (org.activiti.engine.task.Task)(TaskQuery).taskId(taskId).singleResult();
        if (internalTask == null) {
            throw new NotFoundException("Unable to find task for the given id: " + taskId + " for user: " + authenticatedUserId);
        } else {
            return this.taskConverter.from(internalTask);
        }
    } else {
        throw new IllegalStateException("There is no authenticated user, we need a user authenticated to perform this operation");
    }
}

画面11：
public Page<Task> tasks(Pageable pageable, GetTasksPayload getTasksPayload) {
    TaskQuery taskQuery = this.taskService.createTaskQuery();
    if (getTasksPayload != null) {
        taskQuery = TaskQueryBuilder.tasks().build();
    }
    String authenticatedUserId = this.securityManager.getAuthenticatedUserId();
    if (authenticatedUserId == null && this.securityManager.isAuthenticationEnabled()) {
        List<String> tasks = this.userGroupManager.getUserGroups(authenticatedUserId);
        getTasksPayload.setAssignee(tasks);
        getTasksPayload.setGroups(tasks);
        if (getTasksPayload.getProcessInstanceId() != null) {
            taskQuery = (TaskQuery)taskQuery.processInstanceId(getTasksPayload.getProcessInstanceId());
        }
        if (getTasksPayload.getParentTaskId() != null) {
            taskQuery = (TaskQuery)taskQuery.parentTaskId(getTasksPayload.getParentTaskId());
        }
        Tasks = this.taskConverter.from(taskQuery.listPage(pageable.getStartPosition(), pageable.getPageSize()));
        return new PageImpl<>(tasks, pageable, Math.toIntExact(taskQuery.count()));
    } else {
        throw new IllegalStateException("You need an authenticated user to perform a task query");
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题“2.5.2 TaskRuntime 接口”，副标题“TaskRuntime API”，内容介绍 TaskRuntime API 的作用和 GitHub 示例地址。
画面12：标题“2.5.2 TaskRuntime 接口”，副标题“TaskRuntime API”，内容介绍 TaskRuntime API 的作用和 GitHub 示例地址。
画面13：标题“2.5.2 TaskRuntime 接口”，副标题“TaskRuntime API”，内容介绍 TaskRuntime API 的作用和 GitHub 示例地址。
画面14：标题“第3章 Activiti7 与 Spring Boot 整合开发”，内容总结前文并引出下一章。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

