# 画面线理解：17-Activti7新特性总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\17-Activti7新特性总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:16, 00:21, 00:49, 00:53, 01:18, 01:24, 01:26, 01:30, 01:41, 01:52, 02:32, 02:54, 03:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:45:49

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 SpringBoot 项目中集成 Activiti7，包括启动类编写、依赖配置、流程实例启动与任务查询完成等核心开发步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 标题“4.3 编写 SpringBoot 启动类”，并显示了启动类代码片段：
```java
@SpringBootApplication(exclude = SecurityAutoConfiguration.class)
public class ActivitiDemoApplication {
    private Logger logger = LoggerFactory.getLogger(ActivitiDemoApplication.class);
    public static void main(String[] args) {
        SpringApplication.run(ActivitiDemoApplication.class, args);
    }
}
```

画面2：展示 PPT 标题“3.4.1 Activiti7 与 SpringBoot 整合”，并显示了 Maven 依赖配置片段：
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
1. 添加 SpringBoot 整合 Activiti7 的坐标
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

画面6：展示 PPT 标题“3.1 SpringBoot 整合 Activiti7 的配置”，并显示了父依赖配置：
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

画面9：展示 PPT 标题“第4章 Activiti7+SpringBoot+SpringMVC 开发”，并显示了任务完成的代码片段：
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
