# 画面线理解：16-Activti7+SpringBoot+SpringMVC整合-开发Controller控制器

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\16-Activti7+SpringBoot+SpringMVC整合-开发Controller控制器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:57, 01:55, 02:21, 03:27, 04:06, 05:06, 05:35, 05:49, 06:19, 06:54, 07:32, 08:03, 08:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:45:02

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 Activiti7，通过编写 Controller 类来操作流程任务，包括任务的查询、领取和完成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 标题页“第4章 Activiti7+ SpringBoot+SpringMVC 开发”及子章节“4.1 添加 Controller 类”，并显示了示例代码 `@RestController public class TestController { private Logger logger = LoggerFactory.getLogger(TestController.class); @Autowired private ProcessRuntime processRuntime; }`。
画面2：在 IDE 中创建 `MyController` 类，位于包 `com.ithema.activiti.controller` 下，初始为空。
画面3：在 `MyController` 类中添加 `@RestController` 注解，并引入 Activiti 和 Spring Web 的相关依赖包。
画面4：在 `MyController` 类中添加 `@Autowired` 注解，注入 `ProcessRuntime` 和 `TaskRuntime` 两个对象。
画面5：在 `MyController` 类中编写 `testHello()` 方法，用于查询并处理任务，包括分页查询、任务领取和完成操作。
画面6：弹出“Copy”对话框，提示将 `ActivitiDemoApplication.java` 文件复制到项目中。
画面7：展示 `DemoApplicationConfiguration` 类中的 `myUserDetailsService()` 方法，用于配置内存用户和角色信息。
画面8：在 `MyController` 类中，`testHello()` 方法中添加了 `securityUtil.logInAs("ordemodirois")` 用于模拟用户登录。
画面9：展示 `ActivityTest` 测试类中的 `testStartInstance()` 方法，用于启动流程实例。
画面10：展示 `ActivitiDemoApplication` 类的 `main` 方法和 `@Bean` 注解的 `testConnector()` 方法。
画面11：再次展示 `DemoApplicationConfiguration` 类中的 `myUserDetailsService()` 方法，确认用户和角色配置。
画面12：在 `MyController` 类中，`testHello()` 方法中修改了任务领取的组为 `"activitiTeam"`。
画面13：在 `MyController` 类中，`testHello()` 方法中修改了任务领取的组为 `"activitiTeam"`，并添加了任务完成的打印语句。
画面14：在 `MyController` 类中，`testHello()` 方法中修改了任务领取的组为 `"activitiTeam"`，并添加了任务完成的打印语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@RestController
public class TestController {
    private Logger logger = LoggerFactory.getLogger(TestController.class);
    @Autowired
    private ProcessRuntime processRuntime;
}
```

画面2：
```java
package com.ithema.activiti.controller;

public class MyController {

}
```

画面3：
```java
import org.activiti.api.process.runtime.ProcessRuntime;
import org.activiti.api.task.runtime.TaskRuntime;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;
```

画面4：
```java
@RestController
public class MyController {
    @Autowired
    private ProcessRuntime processRuntime;
    @Autowired
    private TaskRuntime taskRuntime;
    @Autowired
    private SecurityUtil securityUtil;
}
```

画面5：
```java
//查询任务、执行任务
//指定用户
Page<Task> taskPage = taskRuntime.tasks(Pageable.of(startIndex, maxItems)); //分页查询任务列表
if(taskPage.getTotalItems()>0){
    //遍历任务列表
    for(Task task:taskPage.getContent()){
        System.out.println("任务1:"+task);
        //领取任务
        taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
        //执行任务
        taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
    }
}
```

画面6：
```java
Copy file: G:\Activiti\springboot\ActivitiDemoApplication.java
New name: ActivitiDemoApplication.java
To directory: G:\Activiti\springboot\activiti\src\main\java\com\ithema\activiti
```

画面7：
```java
@Bean
public UserDetailsService myUserDetailsService() {
    InMemoryUserDetailsManager inMemoryUserDetailsManager = new InMemoryUserDetailsManager();
    String[][] userGroupsAndRoles = {
        {"salaby", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
        {"ryndousomak", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
        {"erndemodirois", "password", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
        {"other", "password", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
        {"admin", "password", "ROLE_ACTIVITI_ADMIN", ""}
    };
    for (String[] user : userGroupsAndRoles) {
        List<String> authoritiesStrings = Arrays.asList(Arrays.copyOfRange(user, 2, user.length));
        logger.info("Registering new user: " + user[0] + " with the following Authorities: " + authoritiesStrings);
        inMemoryUserDetailsManager.createUser(new User(user[0], passwordEncoder().encode(user[1]), authoritiesStrings.stream().map(s -> new SimpleGrantedAuthority(s)).collect(Collectors.toList())));
    }
    return inMemoryUserDetailsManager;
}
```

画面8：
```java
//查询任务、执行任务
//指定用户
Page<Task> taskPage = taskRuntime.tasks(Pageable.of(startIndex, maxItems)); //分页查询任务列表
if(taskPage.getTotalItems()>0){
    //遍历任务列表
    for(Task task:taskPage.getContent()){
        System.out.println("任务1:"+task);
        //领取任务
        taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
        //执行任务
        taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
    }
}
```

画面9：
```java
public void testStartInstance() {
    securityUtil.logInAs("salaby"); //springsecurity默认工作
    ProcessInstance processInstance = processRuntime
        .start(ProcessPayloadBuilder
            .start()
            .withProcessDefinitionKey("myProcess_1")
            .build());
    System.out.println("流程实例ID：" + processInstance.getId());
}
```

画面10：
```java
package com.ithema.activiti;

@SpringBootApplication(exclude = SecurityAutoConfiguration.class)
public class ActivitiDemoApplication {
    private Logger logger = LoggerFactory.getLogger(ActivitiDemoApplication.class);

    public static void main(String[] args) {
        SpringApplication.run(ActivitiDemoApplication.class, args);
    }

    @Bean
    Connector testConnector() {
        return integrationContext -> {
            logger.info("以调用代码：现在叫连接器被调用啦～");
            return integrationContext;
        };
    }
}
```

画面11：
```java
@Bean
public UserDetailsService myUserDetailsService() {
    InMemoryUserDetailsManager inMemoryUserDetailsManager = new InMemoryUserDetailsManager();
    String[][] userGroupsAndRoles = {
        {"salaby", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
        {"ryndousomak", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
        {"erndemodirois", "password", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
        {"other", "password", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
        {"admin", "password", "ROLE_ACTIVITI_ADMIN", ""}
    };
    for (String[] user : userGroupsAndRoles) {
        List<String> authoritiesStrings = Arrays.asList(Arrays.copyOfRange(user, 2, user.length));
        logger.info("Registering new user: " + user[0] + " with the following Authorities: " + authoritiesStrings);
        inMemoryUserDetailsManager.createUser(new User(user[0], passwordEncoder().encode(user[1]), authoritiesStrings.stream().map(s -> new SimpleGrantedAuthority(s)).collect(Collectors.toList())));
    }
    return inMemoryUserDetailsManager;
}
```

画面12：
```java
//查询任务、执行任务
//指定用户
Page<Task> taskPage = taskRuntime.tasks(Pageable.of(startIndex, maxItems)); //分页查询任务列表
if(taskPage.getTotalItems()>0){
    //遍历任务列表
    for(Task task:taskPage.getContent()){
        System.out.println("任务1:"+task);
        //领取任务
        taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
        //执行任务
        taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
    }
}
```

画面13：
```java
//查询任务、执行任务
//指定用户
Page<Task> taskPage = taskRuntime.tasks(Pageable.of(startIndex, maxItems)); //分页查询任务列表
if(taskPage.getTotalItems()>0){
    //遍历任务列表
    for(Task task:taskPage.getContent()){
        System.out.println("任务2:"+task);
        //领取任务
        taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
        //执行任务
        taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
    }
}
```

画面14：
```java
//查询任务、执行
