# 画面线理解：06-Activiti7的新API介绍与分析_ProcessRuntime分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\06-Activiti7的新API介绍与分析_ProcessRuntime分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:43, 02:31, 03:41, 04:57, 06:38, 07:31, 08:24, 09:05, 10:02, 13:19, 13:40, 14:24, 15:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:33:52

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 7 新的 ProcessRuntime API 的使用方法，包括如何通过注入该对象来操作流程定义，并涉及 Spring Security 的集成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面，标题为“2.5 Activiti 新的 API 介绍”，内容指出要学习 ProcessRuntime 接口和 TaskRuntime 接口。
画面2：展示 GitHub 页面，链接为 https://github.com/Activiti/activiti-developers-guide/blob/master/getting-started/getting-started-activiti-core.md，标题为“Getting Started with Activiti Core”。
画面3：展示 GitHub 页面，显示 ProcessRuntime 接口的 Java 代码定义，包括方法如 processDefinition(String processDefinitionId)、start(StartProcessPayload payload) 等，并提示需要角色“ACTIVITI_USER”。
画面4：展示 PPT 页面，内容提到使用 ProcessRuntime 时需要 Spring Security，并给出代码示例链接：https://github.com/Activiti/Activiti-examples/blob/master/activiti-api-basic-process-example/src/main/java/org/activiti/examples/DemoApplication.java#132。
画面5：展示 GitHub 页面，显示 Java 代码，使用 ProcessRuntime.start(ProcessPayloadBuilder).start() 启动流程实例，并设置变量。
画面6：展示 GitHub 页面，显示 Java 代码，通过 processRuntime.processDefinitions(Pagable.of(0, 10)) 获取流程定义列表，并提示流程定义需放置在 /src/main/resources/processes/ 目录下。
画面7：展示 GitHub 页面，内容与画面6类似，再次强调流程定义需放置在 /src/main/resources/processes/ 目录下。
画面8：展示 Windows 文件资源管理器，显示文件夹“Activiti7-day03”下的 PDF 文档。
画面9：展示 PPT 页面，内容与画面4相同，强调需要 Spring Security。
画面10：展示 IntelliJ IDEA 的代码编辑器，显示 ProcessRuntimeImpl 类的源码，包含 import 语句和类定义。
画面11：展示 IntelliJ IDEA 的代码编辑器，显示 Activiti7DemoApplicationTests 类的测试代码，包含 @Autowired 注解注入 ProcessRuntime 和 TaskRuntime。
画面12：展示 IntelliJ IDEA 的代码编辑器，显示 Activiti7DemoApplicationTests 类的测试代码，将 TaskRuntime 注解改为 RuntimeService。
画面13：展示 IntelliJ IDEA 的代码编辑器，显示 Activiti7DemoApplicationTests 类的测试代码，注释为“查看流程定义”。
画面14：展示 IntelliJ IDEA 的代码编辑器，显示 ProcessRuntimeImpl 类的源码，弹出“CantRun”对话框，显示“已运行”状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
public interface ProcessRuntime {
    ProcessRuntimeConfiguration configuration();
    ProcessDefinition processDefinition(String processDefinitionId);
    Page processDefinitions(Pageable pageable);
    Page processDefinitions(Pageable pageable);
    ProcessInstance start(StartProcessPayload payload);
    Page processInstances(Pageable pageable);
    ProcessInstance processInstance(String processInstanceID);
    ProcessInstance suspend(SuspendProcessPayload payload);
    ProcessInstance resume(ResumeProcessPayload payload);
    ProcessInstance delete(DeleteProcessPayload payload);
    void signal(SignalPayload payload);
    ...
}
```
画面4：
```java
@Authored
private ProcessRuntime processRuntime;
@Authored
private SecurityUtil securityUtil;
```
画面5：
```java
@Scheduled(initialDelay = 1000, fixedDelay = 1000)
public void processText() {
    securityUtil.logInAs("system");
    String content = pickRandomString();
    SimpleDateFormat formatter = new SimpleDateFormat("dd-MM-yy HH:mm:ss");
    logger.info("Processing content: " + content);
    ProcessInstance processInstance = processRuntime
            .start(ProcessPayloadBuilder
                    .start()
                    .withProcessDefinitionKey("categorizeProcess")
                    .withVariable("content", content)
                    .build());
    logger.info(">>> Created Process Instance: " + processInstance);
}
```
画面6：
```java
Page processDefinitionPage = processRuntime
        .processDefinitions(Pagable.of(0, 10));
logger.info("> Available Process definitions: " + processDefinitionPage.getTotalItems());
for (ProcessDefinition pd : processDefinitionPage.getContent()) {
    logger.info("c : Process definition: " + pd);
}
```
画面10：
```java
import org.activiti.api.common.spring.security.policies.SecurityPolicyAccess;
import org.activiti.api.engine.RepositoryService;
import org.activiti.api.engine.RuntimeService;
import org.activiti.api.runtime.model.ProcessDefinition;
import org.activiti.api.runtime.model.ProcessInstance;
import org.activiti.api.runtime.model.VariableInstance;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload;
import org.activiti.api.runtime.model.VariableInstancePayload
