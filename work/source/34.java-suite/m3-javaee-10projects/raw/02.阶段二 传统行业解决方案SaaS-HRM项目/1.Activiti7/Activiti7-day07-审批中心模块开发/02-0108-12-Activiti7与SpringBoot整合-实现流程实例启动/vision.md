# 画面线理解：12-Activiti7与SpringBoot整合-实现流程实例启动

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\12-Activiti7与SpringBoot整合-实现流程实例启动_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:01, 01:27, 02:34, 02:52, 03:29, 04:03, 04:12, 04:19, 04:57, 05:37, 06:00, 06:36, 07:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:41:07

1) 这一组画面整体在讲如何通过代码启动 Activiti 流程实例，并演示了相关测试和源码分析。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 PDF 文档中“3.4.3 启动流程实例”的代码示例，包含 `testStartProcess()` 方法，用于启动流程实例并打印流程实例 ID。
画面2: 在 IDEA 中展示 `ActivityTest.java` 文件，`testDefinition()` 方法用于查询流程定义，打印流程定义的个数和名称。
画面3: IDEA 中 `ActivityTest.java` 文件，`testDefinition()` 方法被注释，显示了流程定义查询的代码。
画面4: 浏览器中显示 GitHub 上的 Activiti 示例代码，包含 `processText()` 方法和 `ProcessInstance` 启动代码。
画面5: IDEA 中 `ActivityTest.java` 文件，`testStartInstance()` 方法用于启动流程实例，使用 `ProcessRuntime` 和 `ProcessInstance`。
画面6: PDF 文档中“3.4.3 启动流程实例”的代码示例，与画面1相同。
画面7: IDEA 中 `ActivityTest.java` 文件，`testStartInstance()` 方法，使用 `ProcessRuntime` 启动名为 "myProcess_1" 的流程实例。
画面8: IDEA 中 `ActivityTest.java` 文件，`testStartInstance()` 方法，显示了启动流程实例的代码。
画面9: IDEA 中 `ActivityTest.java` 文件，`testStartInstance()` 方法，显示了启动流程实例的代码。
画面10: IDEA 中 `ActivityTest.java` 文件，`testStartInstance()` 方法，显示了启动流程实例的代码。
画面11: IDEA 中 `ActivityTest.java` 文件，`testStartInstance()` 方法，显示了启动流程实例的代码。
画面12: IDEA 中 `ProcessRuntimeImpl.java` 文件，`start()` 方法的源码，用于启动流程实例。
画面13: IDEA 中 `ProcessRuntimeImpl.java` 文件，`start()` 方法的源码，显示了流程定义 ID 或 Key 的校验逻辑。
画面14: IDEA 中 `ActivityTest.java` 文件，`testStartInstance()` 方法，显示了启动流程实例的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
/**
 * 启动流程实例
 */
@Test
public void testStartProcess() {
    securityUtil.loginAs("system");
    ProcessInstance processInstance = processRuntime
            .start(ProcessPayloadBuilder.start()
                    .withProcessDefinitionKey("myProcess")
                    .build());
    System.out.println("流程实例 ID：" + processInstance.getId());
}
```

画面2:
```java
public void testDefinition() {
    securityUtil.loginAs(username: "salaby"); // springsecurity 的认证工作
    Page processDefinitionPage = processRuntime
            .processDefinitionPage(Pageable.of(startIndex: 0, maxItems: 10));
    System.out.println("流程定义的个数：" + processDefinitionPage.getTotalItems());
    for (Object pd : processDefinitionPage.getContent()) {
        System.out.println("流程定义：" + pd);
    }
}
```

画面4:
```java
@Scheduled(initialDelay = 1000, fixedDelay = 1000)
public void processText() {
    securityUtil.logInAs("system");
    String content = this.simpleDateFormat.format(new Date());
    logger.info("Processing content：" + content);
    ProcessInstance processInstance = processRuntime
            .start(ProcessPayloadBuilder
                    .start()
                    .withProcessDefinitionKey("categorizeProcess")
                    .withContent(content)
                    .build());
}
```

画面5:
```java
public void testStartInstance() {
    securityUtil.loginAs(username: "salaby"); // springsecurity 的认证工作
    ProcessInstance processInstance = processRuntime
            .start(ProcessPayloadBuilder
                    .start()
                    .withProcessDefinitionKey("categorizeProcess")
                    .build());
}
```

画面7:
```java
public void testStartInstance() {
    securityUtil.loginAs(username: "salaby"); // springsecurity 的认证工作
    ProcessInstance processInstance = processRuntime
            .start(ProcessPayloadBuilder
                    .start()
                    .withProcessDefinitionKey("myProcess_1")
                    .build());
    System.out.println("流程实例ID：" + processInstance.getId());
}
```

画面12:
```java
public ProcessInstance start(ProcessRuntimeConfiguration configuration) { return this.configuration; }
public ProcessInstance start(StartProcessPayload startProcessPayload) {
    ProcessDefinition processDefinition = null;
    if (startProcessPayload.getProcessDefinitionId() != null) {
        processDefinition = this.processDefinition(startProcessPayload.getProcessDefinitionId());
    }
    if (processDefinition == null && startProcessPayload.getProcessDefinitionKey() != null) {
        processDefinition = this.processDefinition(startProcessPayload.getProcessDefinitionKey());
    }
    if (processDefinition == null) {
        if (this.securityPolicyManager.canWrite(processDefinition.getKey())) {
            throw new ActivitiForbiddenException("Operation not permitted for " + processDefinition.getKey() + " due security policy violation");
        } else {
            return this.processInstanceConvert.from(this.runtimeService.createProcessInstanceBuilder()
                    .processDefinitionId(startProcessPayload.getProcessDefinitionId())
                    .processDefinitionKey(startProcessPayload.getProcessDefinitionKey())
                    .build());
        }
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: PPT 标题为“3.4.3 启动流程实例”，内容包含代码示例。
画面6: PPT 标题为“3.4.3 启动流程实例”，内容与画面1相同。
画面4: 浏览器中显示 GitHub 页面，包含代码示例和说明文字。

5) 无。
