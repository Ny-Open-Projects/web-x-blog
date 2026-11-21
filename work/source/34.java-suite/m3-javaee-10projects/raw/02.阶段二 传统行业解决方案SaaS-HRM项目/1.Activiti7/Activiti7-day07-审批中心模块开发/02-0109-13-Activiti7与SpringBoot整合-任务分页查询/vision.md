# 画面线理解：13-Activiti7与SpringBoot整合-任务分页查询

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\13-Activiti7与SpringBoot整合-任务分页查询_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:37, 01:30, 01:55, 02:20, 02:35, 02:52, 03:45, 03:55, 05:03, 05:36, 05:50, 05:59, 06:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:42:01

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 Activiti 工作流引擎，演示了启动流程实例、查询任务并完成任务的代码逻辑。

2) 按时间顺序列出每张画面的要点：
画面1：展示 MySQL 数据库中 activiti7-springboot 相关表结构，查询到流程实例数据。
画面2：展示 Activiti 流程图，包含 Start Event、User Task、Service Task、End Event，以及 IDE 中的项目结构。
画面3：展示 ActivitiTest.java 中的 testStartInstance() 方法，用于启动流程实例。
画面4：展示 PPT 内容，讲解如何查询任务并完成任务，代码片段为 testTask() 方法。
画面5：展示 PPT 内容，继续讲解 testTask() 方法，包含任务完成和分页查询逻辑。
画面6：展示 ActivitiTest.java 中 testTask() 方法的初始状态，未添加任何代码。
画面7：展示 DemoApplicationConfiguration.java 中的 myUserDetailsService() 方法，用于配置内存用户和角色。
画面8：展示 ActivitiTest.java 中 testTask() 方法的初始状态，未添加任何代码。
画面9：展示 ActivitiTest.java 中 testTask() 方法的初始状态，未添加任何代码。
画面10：展示 ActivitiTest.java 中 testTask() 方法，添加了获取任务分页数据的代码。
画面11：展示 ActivitiTest.java 中 testTask() 方法，添加了遍历任务列表并打印的代码。
画面12：展示 ActivitiTest.java 中 testTask() 方法，完整代码已编写，包含登录、查询、遍历和打印任务。
画面13：展示 ActivitiTest.java 中 testTask() 方法，代码已编写，终端显示编译成功。
画面14：展示 ActivitiTest.java 中 testTask() 方法，代码已编写，终端显示执行成功并输出任务信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```sql
SELECT * FROM act_ru_execution;
```

画面2：
```java
// 启动流程实例
ProcessInstance processInstance = processRuntime
    .start(ProcessPayloadBuilder
        .start()
        .withProcessDefinitionKey("myProcess_1")
        .build());
System.out.println("流程实例ID：" + processInstance.getId());
```

画面3：
```java
@Test
public void testStartInstance(){
    securityUtil.loginAs("salaboy");//springsecurity的认证工作
    ProcessInstance processInstance = processRuntime
        .start(ProcessPayloadBuilder
            .start()
            .withProcessDefinitionKey("myProcess_1")
            .build());//启动流程实例
    System.out.println("流程实例ID：" + processInstance.getId());
}
```

画面4：
```java
public void testTask() {
    securityUtil.loginAs("ryandawsonuk");
    Page<Task> taskPage = taskRuntime.tasks(Pageable.of(0, 10));
    if (taskPage.getTotalItems() > 0) {
        for (Task task : taskPage.getContent()) {
            taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
            System.out.println("任务：" + task);
        }
    }
}
```

画面5：
```java
taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());

Page<Task> taskPage2 = taskRuntime.tasks(Pageable.of(0, 10));
if (taskPage2.getTotalItems() > 0) {
    for (Task task : taskPage2.getContent()) {
        System.out.println("任务：" + task);
    }
}
```

画面6：
```java
@Test
public void testTask() {
}
```

画面7：
```java
@Bean
public UserDetailsService myUserDetailsService() {
    InMemoryUserDetailsManager inMemoryUserDetailsManager = new InMemoryUserDetailsManager();

    String[][] usersGroupsAndRoles = {
        {"salaboy", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
        {"ryandawsonuk", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
        {"ordenedeiro", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
        {"other", "password", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
        {"admin", "password", "ROLE_ACTIVITI_ADMIN", "GROUP_admin"}
    };

    for (String user : usersGroupsAndRoles) {
        List<String> authoritiesStrings = Arrays.asList(Arrays.copyOfRange(user, 2, user.length));
        logger.info("Registering new user: " + user[0] + " with the following Authorities: " + authoritiesStrings + "]");
        inMemoryUserDetailsManager.createUser(new User(user[0], passwordEncoder().encode(user[1]), authoritiesStrings.stream().map(s -> new SimpleGrantedAuthority(s)).collect(Collectors.toList())));
    }

    return inMemoryUserDetailsManager;
}
```

画面8：
```java
@Test
public void testTask() {
    securityUtil.loginAs("ryandawsonuk");//指定用户认证信息
}
```

画面9：
```java
@Test
public void testTask() {
    securityUtil.loginAs("ryandawsonuk");//指定用户认证信息
}
```

画面10：
```java
@Test
public void testTask() {
    securityUtil.loginAs("ryandawsonuk");//指定用户认证信息
    Page<Task> taskPage = taskRuntime.tasks(Pageable.of(0, 10));
    if (taskPage.getTotalItems() > 0) {
        for (Task task : taskPage.getContent()) {
            System.out.println("任务：" + task);
        }
    }
}
```

画面11：
```java
@Test
public void testTask() {
    securityUtil.loginAs("ryandawsonuk");//指定用户认证信息
    Page<Task> taskPage = taskRuntime.tasks(Pageable.of(0, 10));
    if (taskPage.getTotalItems() > 0) {
        for (Task task : taskPage.getContent()) {
            System.out.println("任务：" + task);
        }
    }
}
```

画面12：
```java
@Test
public void testTask() {
    securityUtil.loginAs("ryandawsonuk");//指定用户认证信息
    Page<Task> taskPage = taskRuntime.tasks(Pageable.of(0, 10));
    if (taskPage.getTotalItems() > 0) {
        for (Task task : taskPage.getContent()) {
            System.out.println("任务：" + task);
        }
    }
}
```

画面13：
```java
@Test
public void testTask() {
    securityUtil.loginAs("ryandawsonuk");//指定用户认证信息
    Page<Task> taskPage = taskRuntime.tasks(Pageable.of(0, 10));
    if (taskPage.getTotalItems() > 0) {
        for (Task task : taskPage.getContent()) {
            System.out.println("任务：" + task);
        }
    }
}
```

画面14：
```java
@Test
public void testTask() {
    securityUtil.loginAs("ryandawsonuk");//指定用户认证信息
    Page<Task> taskPage = taskRuntime.tasks(Pageable.of(0, 10));
    if (taskPage.getTotalItems() > 0) {
        for (Task task : taskPage.getContent()) {
            System.out.println("任务：" + task);
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
- PPT 标题：Activiti 与 Spring Boot 集成
- 架构图：Start Event → User Task → Service Task → End Event
- 表格数据：无

画面4：
- PPT 标题：Activiti 与 Spring Boot 集成
- 表格数据：无

画面5：
- PPT 标题：Activiti 与 Spring Boot 集成
- 表格数据：无

5) 不要评价画面美观，不要输出与课程无关的内容。
