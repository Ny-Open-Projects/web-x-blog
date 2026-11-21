# 画面线理解：07-Activiti7新API介绍及分析-TaskRuntime分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\07-Activiti7新API介绍及分析-TaskRuntime分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 02:37, 03:15, 04:18, 04:29, 04:44, 05:35, 06:36, 07:05, 07:43, 08:14, 09:10, 09:46, 10:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:34:48

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
画面14：展示 PPT 页面“第3章 Activiti7 与 SpringBoot 整合开发”，总结前文内容并引出下一章。

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
画面14：标题“第3章 Activiti7 与 SpringBoot 整合开发”，内容总结前文并引出下一章。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
