# 画面线理解：05-Activiti7学习文档及Example示例下载

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\05-Activiti7学习文档及Example示例下载_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:45, 01:40, 03:13, 04:34, 04:57, 05:08, 05:37, 06:28, 07:12, 08:20, 08:50, 09:12, 09:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:32:58

1) 这一组画面整体在讲什么（一句话）：
本课程介绍 Activiti7 的核心组件与入门指南，重点讲解 Activiti Core 的 API 使用和示例项目。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在百度搜索“flowable”，搜索结果中包含“Flowable官网 - Java Business Process Engines”和“Docs | Flowable”等链接。
画面2：展示PPT第2.2节“下载官网资源”，列出三个资源链接：Activiti-Core学习向导页、Activiti-Core示例、资料所在位置。
画面3：展示Activiti官网下载页面，标题为“Download Activiti Now!”，列出用户将获得的内容。
画面4：展示GitHub上的Activiti开发者指南页面，标题为“Getting Started”，说明Activiti分为Activiti Core和Activiti Cloud两类。
画面5：展示GitHub页面，页面内容为空白。
画面6：展示GitHub上的Activiti开发者指南页面，内容为“TaskRuntime API”部分，包含代码片段和依赖配置。
画面7：展示GitHub上的Activiti开发者指南页面，内容为“ProcessRuntime API”部分，包含接口定义。
画面8：展示Windows资源管理器，路径为“SaaS-IHRM项目-Activiti7”，选中文件“SaaS-IHRM项目-Activiti7特性.pdf”。
画面9：展示GitHub上的Activiti开发者指南页面，内容为“Getting Started with Activiti Core”部分。
画面10：展示GitHub上的Activiti示例项目仓库页面，列出多个示例模块和配置文件。
画面11：展示GitHub上的Activiti开发者指南页面，内容为“Getting Started”部分。
画面12：展示GitHub上的Activiti开发者指南页面，内容为“TaskRuntime API”部分，包含依赖配置和接口定义。
画面13：展示PPT第2.4节“Activiti7的组成部分”，说明Activiti分为Activiti Core和Activiti Cloud两类。
画面14：展示PPT第2.4节“Activiti7的组成部分”，内容为“Activiti Cloud 简单介绍”，列出四个基础构建块：Activiti Cloud Runtime Bundle、Activiti Cloud Query、Activiti Cloud Audit、Activiti Cloud Connectors。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6：
```java
@bean
public TaskRuntimeEventListener taskAssignedListener() {
    return taskAssigned;
}
```
```xml
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-dependencies</artifactId>
    <version>7.0.0.Beta1</version>
    <scope>import</scope>
    <type>pom</type>
</dependency>
```
画面7：
```java
public interface ProcessRuntime {
    ProcessRuntimeConfiguration configuration();
    ProcessDefinition processDefinition(String processDefinitionId);
    Page processDefinitions(Pageable pageable);
    Page processDefinitions(Pageable pageable);
    ProcessInstance start(StartProcessPayload payload);
    Page processInstances(Pageable pageable);
    Page processInstances(Pageable pageable);
    GetProcessInstancePayload payload);
}
```
画面12：
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-dependencies</artifactId>
            <version>7.0.0.Beta1</version>
            <scope>import</scope>
            <type>pom</type>
        </dependency>
    </dependencies>
</dependencyManagement>
```
```java
@autowired
private TaskRuntime taskRuntime;
```
```java
public interface TaskRuntime {
    TaskRuntimeConfiguration configuration();
    Task task(String taskId);
    Page tasks(Pageable pageable, StartTasksPayload payload);
    Task create(CreateTaskPayload payload);
    Task claim(ClaimTaskPayload payload);
    Task release(ReleaseTaskPayload payload);
    Task complete(CompleteTaskPayload payload);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题“2.2 下载官网资源”，内容为三个资源链接。
画面4：PPT标题“Getting Started”，内容为Activiti分为Activiti Core和Activiti Cloud两类。
画面13：PPT标题“2.4 Activiti7的组成部分”，内容为Activiti分为Activiti Core和Activiti Cloud两类。
画面14：PPT标题“Activiti Cloud 简单介绍”，内容为四个基础构建块：Activiti Cloud Runtime Bundle、Activiti Cloud Query、Activiti Cloud Audit、Activiti Cloud Connectors。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
