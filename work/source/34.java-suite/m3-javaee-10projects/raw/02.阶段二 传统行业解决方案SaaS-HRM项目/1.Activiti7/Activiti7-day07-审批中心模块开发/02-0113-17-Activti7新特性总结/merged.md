# 17-Activti7新特性总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\17-Activti7新特性总结_【海量资源尽在 ubkz.com】.mp4
- 时长 3分25秒（音频 206s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们就一起简单整结一下这一次我们主要是完成了我们的activity与spleen整合如果说某一个公司他没有用spleen boot的话我们可以使用activity与spleen整合的这种方式来完成我们的简化我们的开发过程这是一种方式这个咱们是需要掌握的然后我们第二个又给各位介绍了一下activity7的线状
[00:29] 当然我们工作流部分还是以我们的activity5和6是为主的也是市面上现在做工作流最主要的一个应该说最主要的一个引擎我们最后一部分给各位介绍的是我们的activity7与sprintboot整合这个部分我们的这个类做了一个更新主要用的是process runtime和task runtime
[00:57] 对吧,那这个也不是很难啊,但它内部本身呢,就是封装了我们所对应的那些Service,对吧比如说,封装了我们的这个,封装了我们的这个Runtime serviceTask Service,对吧好,那再往后走呢,我们就用对应的这个Spring Boot和Activity整合之后啊完成了我们一个最基本的啊,这个查看流程信息啊,对吧,来实现启动我们的流程实例啊
[01:27] 完成我们的任务以及我们的这个任务的拾取最后一个我们是把activity7和我们split boot, mvc完全整合到一起这样我们就可以开发我们的Controller对吧在Controller的部分我们将来就可以正儿八经的说我们将来可以正式去开发我们的这个工作流应该说一切前提条件完全都具备
[01:55] 那我这次课程呢基本上也就给各位啊大致上说到这里边那后面呢我们应该还会有啊我们的这个activity和我们的sprintboot在原有的这个整合的这个架构上啊我们的再去引入完全的微博页面啊在页面上的我们再去实现我们的这个流程的发布啊
[02:20] 然后张三登录进来完成自己的任务对吧李四登录进来完成自己的任务这一次我们在做操作用界面给各位展示出来所以说这也是我们最终极的目标对吧这个部分我们应该会在我们的SaaS项目学完差不多的时候我们会推出我们的SaaS项目中的审批中心对吧
[02:47] 因为审批中心就是要去完成各种审批工作比如说我们请假需要审批对吧那将来我们走的完全是用页面来展示而不是用控制台来做了这一点后续我们再回去做一个完全的整合那个部分各位同学就感觉到或者感受到我们之前所做的这些准备工作在后面完全都可以用到好那我们这一次
[03:16] 关于activity7的新特性大致上给各位就说到这里面同学们再见

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Boot 项目中集成 Activiti7，包括启动类编写、依赖配置、流程实例启动与任务查询完成等核心开发步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 标题“4.3 编写 Spring Boot 启动类”，并显示了启动类代码片段：
```java
@SpringBootApplication(exclude = SecurityAutoConfiguration.class)
public class ActivitiDemoApplication {
    private Logger logger = LoggerFactory.getLogger(ActivitiDemoApplication.class);
    public static void main(String[] args) {
        SpringApplication.run(ActivitiDemoApplication.class, args);
    }
}
```

画面2：展示 PPT 标题“3.4.1 Activiti7 与 Spring Boot 整合”，并显示了 Maven 依赖配置片段：
```xml
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-engine</artifactId>
    <version>7.0.0.Beta1</version>
</dependency>

<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring</artifactId>
    <version>7.0.0.Beta1</version>
</dependency>

<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring-model</artifactId>
    <version>7.0.0.Beta1</version>
</dependency>

<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring-converter</artifactId>
    <version>7.0.0.Beta1</version>
</dependency>
```

画面3：展示 PPT 标题“1.2.2 执行流程分析”，并显示了 XML 配置片段及注释：
```xml
<bean id="processEngineConfiguration" class="org.activiti.spring.SpringProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
    <property name="transactionManager" ref="transactionManager"/>
    <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
    <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
    <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
    <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
</bean>
```
注释：通过工厂方法方式创建 ProcessEngine，配置文件 activiti-spring.xml，该配置文件又会加载。

画面4：展示 PPT 标题“Activiti7 发布正式版之后，它与 SpringBoot2.x 已经完全支持整合开发”，并列出整合步骤：
1. 添加 Spring Boot 整合 Activiti7 的坐标
2. 添加 SpringSecurity 安全框架的整合配置信息
3. 使用 Activiti7 新支持的类来实现工作流开发
   - ProcessRuntime 接口
   - TaskRuntime 接口

画面5：在画面4基础上补充了第4步：
4. 使用新的 API 实现工作流开发，主要包括：
   - 流程定义查询
   - 启动流程实例
   - 任务的查询
   - 任务的完成

画面6：展示 PPT 标题“3.1 Spring Boot 整合 Activiti7 的配置”，并显示了父依赖配置：
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.0.RELEASE</version>
    <relativePath/>
</parent>
```

画面7：展示 PPT 标题“3.4.3 启动流程实例”，并显示了测试方法代码：
```java
@Test
public void testStartProcess() {
    securityUtil.loginAs("system");
    ProcessInstance pi = processRuntime.start(ProcessPayLoadBuilder.start().withProcessDefinitionKey("myProcess").build());
    System.out.println("流程实例 ID: " + pi.getId());
}
```

画面8：在画面7基础上，展示了“3.4.4 查询并完成任务”的标题，并显示了任务查询方法的代码：
```java
public void testTask() {
    securityUtil.loginAs("ryandawsonuk");
}
```

画面9：展示 PPT 标题“第4章 Activiti7+Spring Boot+SpringMVC 开发”，并显示了任务完成的代码片段：
```java
taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
```
注释：使用 TaskRuntime 接口的 tasks() 方法实现任务的查询。使用 TaskRuntime 接口的 claim() 方法实现任务的领取。使用 TaskRuntime 接口的 complete() 方法实现任务的完成。

画面10：展示 PPT 标题“4.2 实现任务完成”，并显示了控制器类 TestController 的代码：
```java
public class TestController {
    private Logger logger = LoggerFactory.getLogger(TestController.class);
    @Autowired
    private ProcessRuntime processRuntime;
    @Autowired
    private TaskRuntime taskRuntime;
    @Autowired
    private SecurityUtil securityUtil;
}
```

画面11：展示 PPT 标题“4.2 实现任务完成”，并显示了控制器方法的代码：
```java
@RequestMapping(value = "/hello")
public void hello() {
    Page<ProcessDefinition> processDefinitionPage = processRuntime.processDefinitions(Pageable.of(0, 10));
    if (processDefinitionPage.getTotalItems() > 0) {
        for (ProcessDefinition definition : processDefinitionPage.getContent()) {
            logger.info("流程定义信息：" + definition);
        }
    }
}
```

画面12：在画面11基础上，展示了流程启动和任务查询的完整代码：
```java
// 启动流程
for (ProcessDefinition definition : processDefinitionPage.getContent()) {
    logger.info("流程定义信息：" + definition);
    processRuntime.start(ProcessPayLoadBuilder.start().withProcessDefinitionId(definition.getId()).build());
}

// 查询当前任务，最多 10 个
Page<Task> taskPage = taskRuntime.tasks(Pageable.of(0, 10));
if (taskPage.getTotalItems() > 0) {
    for (Task task : taskPage.getContent()) {
        logger.info("任务信息：" + task);
    }
}
```

画面13：展示浏览器访问 localhost:8080/hello 的空白页面。

画面14：展示 IDE 中的 MyController.java 文件内容，包含任务查询和完成的完整代码：
```java
@Test
public void testTask() {
    taskPage = taskRuntime.tasks(Pageable.of(0, 10)); // 查询任务列表
    if (taskPage.getTotalItems() > 0) {
        for (Task task : taskPage.getContent()) {
            logger.info("任务信息：" + task);
        }
    }
}
```
注释：// 领取任务，完成自己的任务
```java
taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build());
taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build());
```
注释：// 重新查询任务
```java
taskPage = taskRuntime.tasks(Pageable.of(startIndex, maxItems)); // 重新查询任务列表
if (taskPage.getTotalItems() > 0) {
    for (Task task : taskPage.getContent()) {
        logger.info("任务信息：" + task);
    }
}
```
注释：// 打印任务信息
```java
System.out.println("任务2：" + task);
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
已在上文第2点中完整列出。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
已在上文第2点中完整列出。

5) 不要评价画面美观，不要输出与课程无关的内容。
已完成。

