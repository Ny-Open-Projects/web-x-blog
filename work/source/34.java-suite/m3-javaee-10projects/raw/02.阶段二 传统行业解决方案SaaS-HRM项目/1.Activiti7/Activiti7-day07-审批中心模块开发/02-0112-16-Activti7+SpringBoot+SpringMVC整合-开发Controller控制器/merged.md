# 16-Activti7+SpringBoot+SpringMVC整合-开发Controller控制器

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\16-Activti7+SpringBoot+SpringMVC整合-开发Controller控制器_【海量资源尽在 ubkz.com】.mp4
- 时长 8分34秒（音频 515s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 做完这些测试现在我们可以来实现我们的activity7与sprintboot再把我们的这个control部分引入进来就是我们的sprintmac把我们的sprintmac加入进来我们现在可以来添加我们的这个control类再次回到我们的这个工程中我可以进入到我们的project在这里边我可以再去新建一个新的class比如说
[00:29] 我是放在我们的这个control点然后呢我这里边给它起一个名字啊比如说叫做叫做我们的这个mycontrol好ok那这样我就可以啊按我们的这种按我们的这个要求给它把我们相关的这个依赖啊都给它注入进来啊那现在我们就开始啊进到这里边这是我们的这个啊
[01:01] 控制器的这个类那它呢第一个是我们的这个要去加入一个叫做rest control对吧好这是我们的这个注解然后下一个呢我们作为这个control它的这个主要目标是完成我们的这个任务主要是我们的任务执行主要是做这个工作那
[01:28] 我们要去做这个工作的话首先呢我们可以将我们所需要依赖的这样的一些啊这样的一些类给它注入进来啊比如说我们需要去依赖的还有一个是我们的process runtime对吧加入进来啊叫process runtime除了这个我们还有一个啊是叫做我们的autoware我们需要再去添加一个啊就是我们的这个task对吧task runtime
[01:57] 把它加入进来然后我们还可以去把我们的这个secret secreta 油条把它加入进来是eta auto weld然后再去添加的是我们的secret油条对吧把它加入进来这样我们这个类基本上就已经结构出来了结构出来我们可以再去写上我们真正
[02:27] 要去完成的任务啊你比如说我这个时候这样做啊public void那我们真正要去做的是我们的这个测试比如说啊来完成一个任务的发布啊好这个地方我可以啊主要是查询啊任务查询任务啊然后呢如果有任务的话那我们就执行任务啊执行任务那这样的代码呢我就不去啊从头到尾去漏了啊
[02:59] 那我们开始了在早期的这个部分啊其实我们是做过这种测试的啊那这样我就可以直接啊copy是吧直接这样来啊control c啊然后再次扔到我的这个my control就扔到这里边那我基本上啊就完成了我们的这个编码的工作啊那这个认证的认证的工作呢我现在可以去掉啊那下一个环节呢我可以在这里边去给它加上我们所对应的这个注释啊
[03:28] 比如说叫做request mapping对吧然后呢就是我写上一个啊Hilo这样我们基本上啊就可以来做我们的这个测试了啊好为了能够执行我们的这个测试啊现在呢我需要把我们的这个Spring Boot的这个引导类啊需要加入进来那Spring Boot引导类呢我们可以直接啊到我们的这个第六天啊资料啊在这个里头有一个啊基本的资料
[03:59] 我们去找到整合里头有一个application这个我们可以拿过来你也可以自己去写因为这里头没几行代码然后第一个是我们的注解Splint Boot Application要注意我们这一次要加上这个部分这样的话我们Splint Secure就不会去自动扫描它的配置文件了为什么呢因为我们的Splint Secure它所对应的
[04:27] 杀索对应的这个权限信息是我们自己在这里头通过内加载的对吧所以我们不需要经过它的这个它的这个扫描机制去扫描我们把它去除掉然后呢这个mine方法里头写的这样的内容对于咱们来说没有什么挑战性对吧supreme application的run方法一调用就可以了好那现在我们直接就可以测试来跑一下我们最终的效果现在我
[04:57] run去启动它启动它然后我们来观察我们来观察现在我们就可以看到它已经启动成功了那启动成功了我们其实按道理就可以直接来访问了对吧但是各位要注意因为我们之前这个流程已经完全跑完了对吧所以现在你想去执行任务的时候你想一想咱们现在有没有一个任务说
[05:29] 正要去可以执行现在显然是没有任务可以去执行的对吧所以我们可以这样做在这边呢我们再把我们早期启动流程实例的这个代码呢再去执行一遍这样的话我们就可以相当于又重新再去开启了一次我们的这个流程实例要不然的话我们的这个task任务表中是没有任务的对不对
[05:58] 我们的execution表过一回看啊目前呢它还没有跑完啊好现在已经跑完了那跑完我们又可以回到我们的execution表中对吧那这个时候又相当于有任务了啊那有任务了我们就可以去执行这个任务了对吧那刚才我们的这个split boot啊已经也启动成功了所以说我现在呢可以直接啊点开然后呢在这里面啊我去输入我们的这个localhost的啊
[06:27] 然后走那这个部分各位一定要注意啊它要求我们输入我们的这个用户信息那这个用户信息是谁给了一个这样的界面啊这一点呢各位也要注意是我们的Spring Secure给的对吧然后要求我们去输入啊我们的这个用户信息那对于我们而言因为我们这一次这个用户信息主要是放在我们的这个配置文件中啊Configure这个Java内容啊
[06:56] 那现在我呢就可以直接在这里面输对吧好比如说Count V扔过来这是第一个然后它的密码是我们的password对吧我们把password的这个密码也给它输入过来好那现在呢我们输完了我们可以登录一下对吧那登录结束后因为整个这个界面本来就不会有任何的输出因为我们这边呢直接给它仿佛的是一个 void对吧所以页面是保留空白
[07:25] 那我们应该控制台会有我们相应的这个任务的信息输出对吧所以说我们这个时候也可以再次回到这个部分来我们来关注一下是否有我们的这个任务信息好现在我们就可以看到有一个任务一对吧任务一其实是我们的force的节点而当我们的force的节点完成任务之后我们再去查询我们的任务来可以看一下当我们的这个任务一完成了这个任务之后
[07:56] 它再次查询任务的时候那这次查询的就应该是我们的任务二对不对所以呢我们这个任务二应该会输出的是second的这个信息对吧那我们可以看到这是我们的任务二它输出的是我们的这个任务等于second的这个信息啊整体上呢我们就啊实现了我们的这个Sprite MVC的control引路进来之后也一样可以啊跑我们整个这个流程啊
[08:26] 那这样我们基本上啊就把我们这一次最基础性的工作给各位的介绍到这里边啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 Activiti7，通过编写 Controller 类来操作流程任务，包括任务的查询、领取和完成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 标题页“第4章 Activiti7+ Spring Boot+SpringMVC 开发”及子章节“4.1 添加 Controller 类”，并显示了示例代码 `@RestController public class TestController { private Logger logger = LoggerFactory.getLogger(TestController.class); @Autowired private ProcessRuntime processRuntime; }`。
画面2：在 IDE 中创建 `MyController` 类，位于包 `com.ithema.activiti.Controller` 下，初始为空。
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
package com.ithema.activiti.Controller;

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
Copy file: G:\Activiti\Spring Boot\ActivitiDemoApplication.java
New name: ActivitiDemoApplication.java
To directory: G:\Activiti\Spring Boot\activiti\src\main\java\com\ithema\activiti
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

