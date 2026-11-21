# 13-Activiti7与SpringBoot整合-任务分页查询

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\13-Activiti7与SpringBoot整合-任务分页查询_【海量资源尽在 ubkz.com】.mp4
- 时长 6分52秒（音频 413s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 已经启动了这个流程实例啊那现在我们可以接着来做下一个事情啊就是让我们的这个任务继续往后完成对不对要去查看我们的这个任务的话啊我们可以去看我们的这个RU Excusing表啊那各位可以看到目前我们的这个Excusing表中呢已经有两个两条记录啊其中第一条记录是我们的这个Start开始节点啊第二条记录呢是我们的这个是我们的这个
[00:29] 真正要去完成的这个force的任务啊好我们可以再再次看一下我们的这个bpmn文件来找一下啊因为我们start event已经开始走了那现在目前正在走的这个节点对不对但是这个节点上并没有任务并没有任何的一个用户去执行这个任务对不对所以说他并没有啊他并没有这个往后走啊那我们现在可以呢
[00:56] 去给当前的这个任务分配一个真正的这个执行人对不对让他去拾取这个任务当他拾取完任务完成这个任务是不是流程就接着走到这个任务上面来了所以说现在我可以啊继续来走这个工作啊那现在我们要做的事情就是叫做叫做先我们可以去查询一下啊查询我们的这个流程查询我们的这个任务啊然后呢并完成并完成任务
[01:24] 可以吧,这就是我要做的工作一样的我们可以把这个代码给它复制一下好,contrary,lendl再来针对这里头的内容我们都给它去掉这个地方我们主要就是叫做test task完成我们的任务具体按照什么样的方式来完成我们的任务我们这个地方需要去关注一下我们真正的操作步骤我们可以一起来看一下,叫做
[01:52] 查询并完成自己的任务大致的步骤是这样的首先我们也一样需要解决SplitSecret认证的这个问题然后下一个环节我们就需要去解决的是我们的这个TaskRuntime的通过这个TaskRuntime的Task来完成我们任务的查询查询完任务后面就可以去拾取任务同时可以去完成任务
[02:18] 当我们这个工作做完下一个工作我就会再次来查询我们的这个任务信息对不对好那这个地方呢我们现在啊就可以按照这个具体的步骤大致来操作一把那我们回到回到我们这边来啊那第一个我们还是一样的要去解决的是我们的这个认证的问题对不对那这是我们的第一个啊要解决的是认证啊
[02:44] 认证我们还是用我们的Circuit的油条子里头的logic-ize这个方法这一次我可以写入我们的这个configuration中的另外的一个名称可以吗比如说我用它我让它来执行来获取我们的这个任务大致是这个意思所以说我把它设置进来它主要就是指定指定我们的用户
[03:13] 用户认证信息啊认证信息认证信息啊就是说将来将来这个用户就相当于已经登录进来了啊那他登录进来他就可以完成他自己的任务对不对那他要完成任务的话首先他可以去完成自己任务的一个查询对吧这次我们查主要是他查我们的这个task任务啊查到我们的task好比如说我这边就可以来一个叫task配置啊当然我们在写的时候呢也可以先写后面啊那就那就直接写后面吧
[03:44] 写后面的话我们可以通过我们的task runtime点里头有一个task z通过这个方法然后再去调用我们的这个枫叶的pageant对不对off里头就可以去指定比如说我们是从哪条记录开始对不对然后查多少条对吧是这个意思好当我把这个内容指定好那我们呢就可以就可以再次给它比如说生成一下
[04:13] 这样不更简单一些吗这样我就可以拿到一个叫做task page这个地方是叫做枫叶查询任务列表这样我们就可以查到当前的用户具有哪样的一些任务可以去执行好,后面我们就可以继续用if如果我们的task page.getTotalIntom值是大于0的话那这个说明
[04:42] 说明有任务对不对如果有任务的话那我们这个时候就可以让他去完成他的一系列任务对吧好那这个时候我就可以去让他完成他的任务那我们就可以来一个任务是task对不对好真正的我们是调用我们的task配置里头的get content对吧这样我们就可以取出任务信息这个段就是
[05:11] 便利我们的任务列表便利任务列表当我们便利完任务列表下一个部分我们就可以来输出我们的这些任务对不对这个地方我们可以输出这个任务大致是怎么搞比如说我现在先这样比如说我先测一下任务好具体我就可以来输出我们的 task.比如说get
[05:39] 我在这里头直接输出整个这个task信息,可以吧那我们先可以测试看一下效果这个不没写完我们先来测试一下这样我们就可以完成当前的这个任务的查看工作对不对好,看一下啊好,现在已经执行完了我们这个时候就可以看到有一个真正的任务,对不对是我们哪个任务呢?
[06:06] 我们任务名称是叫做force的对吧,这个任务就是正在
[06:12] 我们正在当前要去做的一个任务这样我们其实基本上就完成了我们的这个任务的查询对不对将来任务查询怎么做主要是通过Task Runtime的这个Task方法对吧通过这个方法我们就可以完成我们的任务完成任务的查询主要是这样做对不对Task方法这样就可以完成好我们
[06:42] 下一个环节我们就要去做这个任务的完成对不对要去完成具体的某一个任务啊就是任务查询啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 Activiti 工作流引擎，演示了启动流程实例、查询任务并完成任务的代码逻辑。

2) 按时间顺序列出每张画面的要点：
画面1：展示 MySQL 数据库中 activiti7-Spring Boot 相关表结构，查询到流程实例数据。
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

