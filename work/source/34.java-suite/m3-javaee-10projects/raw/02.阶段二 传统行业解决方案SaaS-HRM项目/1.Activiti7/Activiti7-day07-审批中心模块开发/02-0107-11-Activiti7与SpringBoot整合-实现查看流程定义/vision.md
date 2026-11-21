# 画面线理解：11-Activiti7与SpringBoot整合-实现查看流程定义

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\11-Activiti7与SpringBoot整合-实现查看流程定义_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:30, 02:54, 03:48, 05:51, 07:09, 08:11, 09:40, 10:27, 11:24, 12:30, 13:52, 14:58, 15:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:40:24

1) 这一组画面整体在讲如何使用 SpringBoot 整合 JUnit 来测试 Activiti7 的流程定义信息。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PPT 页面“3.4 使用 SpringBoot 整合 Junit 方式测试新特性”，并显示项目结构，其中“3.4.1 创建测试类”部分展示了一个名为 `Activiti7DemoApplicationTests` 的测试类，包含 `processRuntime`、`taskRuntime`、`securityUtil` 三个私有字段。
画面2：展示 IDEA 编辑器中 `ActivitiTest.java` 文件，类名 `ActivitiTest`，使用 `@RunWith(SpringRunner.class)` 和 `@SpringBootTest` 注解，导入了 JUnit 和 Spring Boot 相关的测试类。
画面3：展示 `ActivitiTest` 类中添加了 `@Autowired` 注解的 `processRuntime` 和 `taskRuntime` 字段，并导入了 `org.activiti.api.process.runtime.ProcessRuntime` 和 `org.activiti.api.task.runtime.TaskRuntime`。
画面4：展示 `ActivitiTest` 类中添加了 `@Autowired` 注解的 `securityUtil` 字段，并导入了 `org.springframework.boot.test.autoconfigure.web.client.AutoConfigureWebClient`。
画面5：展示 `ActivitiTest` 类中定义了 `testDefinition()` 方法，使用 `processRuntime.processDefinitions(Pageable.of(startIndex: 0, maxItems: 10))` 获取流程定义分页数据。
画面6：展示 `testDefinition()` 方法中添加了 `System.out.println(processDefinitionPage.getTotalItems());` 用于打印流程定义总数。
画面7：展示 `testDefinition()` 方法中添加了 `for (ProcessDefinition pd : processDefinitionPage.getContent()) { System.out.println(pd); }` 用于遍历并打印每个流程定义。
画面8：展示测试运行失败，控制台输出 `1 test failed` 和异常堆栈信息。
画面9：展示 GitHub 页面，内容为 Activiti7 的示例代码，其中包含 `securityUtil.loginAs("system")` 用于登录系统。
画面10：展示在 `ActivitiTest` 类中添加了 `securityUtil.loginAs("salaboy")` 用于登录用户。
画面11：展示测试运行成功，控制台输出 `1 test passed` 和流程定义信息。
画面12：展示测试运行成功，控制台输出 `1 test passed` 和 Activiti7 启动日志。
画面13：展示测试运行成功，控制台输出 `1 test passed` 和流程定义信息。
画面14：展示 PPT 页面“3.4.2 查看流程定义信息”，并显示了 `processRuntime.processDefinitions(Pageable.of(0, 10))` 的代码示例。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
@ContextConfiguration(classes = Activiti7DemoApplication.class)
public class Activiti7DemoApplicationTests {
    @Autowired
    private ProcessRuntime processRuntime;
    @Autowired
    private TaskRuntime taskRuntime;
    @Autowired
    private SecurityUtil securityUtil;
}
```
画面2：
```java
package com.ithema.activiti;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
@RunWith(SpringRunner.class)
@SpringBootTest
public class ActivitiTest {
}
```
画面3：
```java
import org.activiti.api.process.runtime.ProcessRuntime;
import org.activiti.api.task.runtime.TaskRuntime;
import org.springframework.boot.test.autoconfigure.web.client.AutoConfigureWebClient;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
```
画面4：
```java
import org.springframework.boot.test.autoconfigure.web.client.AutoConfigureWebClient;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
```
画面5：
```java
public void testDefinition(){
    Page processDefinitionPage = processRuntime
            .processDefinitions(Pageable.of(startIndex: 0, maxItems: 10));
}
```
画面6：
```java
System.out.println(processDefinitionPage.getTotalItems());
```
画面7：
```java
for (ProcessDefinition pd : processDefinitionPage.getContent()) {
    System.out.println(pd);
}
```
画面9：
```java
securityUtil.loginAs("system");
```
画面10：
```java
securityUtil.loginAs("salaboy");
```
画面11：
```java
System.out.println(processDefinitionPage.getTotalItems());
for (Object pd : processDefinitionPage.getContent()) {
    System.out.println(pd);
}
```
画面12：
```java
ProcessDefinition(id='1752b335-fa98-11e8-81a4-5f870234484c', name='null', key='null', description='null', version=1)
```
画面14：
```java
processRuntime.processDefinitions(Pageable.of(0, 10));
System.out.println("可用的流程定义数量：" + processDefinitionPage.getTotalItems());
for (org.activiti.api.process.model.ProcessDefinition pd : processDefinitionPage.getContent()) {
    System.out.println(pd);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：标题“3.4 使用 SpringBoot 整合 Junit 方式测试新特性”，子标题“3.4.1 创建测试类”。
画面4：标题“3.4.2 查看流程定义信息”。
画面14：标题“3.4.2 查看流程定义信息”，下方有“北京市昌平区建材西路金燕办公楼一层 电话：400-618-9090”和“黑马程序员 传智播客旗下 高端IT教育品牌 改变中国IT教育，我们正在行动”字样。

5) 无。
