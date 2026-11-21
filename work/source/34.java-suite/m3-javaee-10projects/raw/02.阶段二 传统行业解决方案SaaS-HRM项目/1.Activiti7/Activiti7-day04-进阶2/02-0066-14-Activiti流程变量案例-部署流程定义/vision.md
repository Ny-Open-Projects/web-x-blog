# 画面线理解：14-Activiti流程变量案例-部署流程定义

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\14-Activiti流程变量案例-部署流程定义_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:02, 01:28, 02:10, 02:25, 03:01, 03:18, 03:57, 04:17, 04:28, 04:38, 04:51, 05:19, 05:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:00:52

1) 这一组画面整体在讲如何通过 Java 代码部署 Activiti 工作流定义（BPMN 图）到数据库中。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Activiti 项目结构，右侧是 BPMN 流程图，包含“开始事件”、“用户任务”、“排他网关”、“结束事件”等节点，右侧工具栏列出所有可用的 BPMN 元素。
画面2: 显示 `VariableTest.java` 文件，代码中注释“流程变量的测试”，并展示 `Object` 类的继承结构。
画面3: 在 `VariableTest.java` 中，代码注释“1. 模拟流程引擎”，并调用 `ProcessEngines.getDefaultProcessEngine()` 获取默认流程引擎。
画面4: 在 `VariableTest.java` 中，代码注释“2. 模拟RepositoryService”，并调用 `processEngine.getRepositoryService()` 获取仓库服务。
画面5: 在 `VariableTest.java` 中，代码注释“3. 部署”，并调用 `repositoryService.createDeployment()` 开始部署。
画面6: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。
画面7: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。
画面8: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。
画面9: 在 MySQL GUI 中，执行 SQL 语句 `drop database activiti;`，但提示错误“Table activiti.act_ge_bytearray doesn't exist”。
画面10: 在 `VariableTest.java` 中，右键点击 `ProcessEngine` 变量，选择“Run 'VariableTest.main()'”。
画面11: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。
画面12: 在 MySQL GUI 中，执行 SQL 语句 `create database activiti;`，并成功创建数据库。
画面13: 在 MySQL GUI 中，执行 SQL 语句 `create database activiti;`，并成功创建数据库。
画面14: 在 `VariableTest.java` 中，代码注释“2.2. 添加BPMN模型”，并调用 `DeploymentBuilder.addBpmnModel()` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3:
```java
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
```
画面4:
```java
RepositoryService repositoryService = processEngine.getRepositoryService();
```
画面5:
```java
repositoryService.createDeployment()
```
画面6:
```java
DeploymentBuilder.addBpmnModel()
```
画面7:
```java
DeploymentBuilder.addBpmnModel()
```
画面8:
```java
Deployment deploy = repositoryService.createDeployment()
    .addClasspathResource("diagram/holiday4.bpmn")
    .name("请假流程-流程变量")
    .deploy();
```
画面9:
```sql
drop database activiti;
```
画面10:
```java
// Run 'VariableTest.main()'
```
画面11:
```java
Deployment deploy = repositoryService.createDeployment()
    .addClasspathResource("diagram/holiday4.bpmn")
    .name("请假流程-流程变量")
    .deploy();
```
画面12:
```sql
create database activiti;
```
画面13:
```sql
create database activiti;
```
画面14:
```java
Deployment deploy = repositoryService.createDeployment()
    .addClasspathResource("diagram/holiday4.bpmn")
    .name("请假流程-流程变量")
    .deploy();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
