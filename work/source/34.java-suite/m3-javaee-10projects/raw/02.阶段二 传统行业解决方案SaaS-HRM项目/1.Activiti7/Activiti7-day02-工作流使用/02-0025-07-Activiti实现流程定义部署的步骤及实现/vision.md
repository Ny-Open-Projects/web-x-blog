# 画面线理解：07-Activiti实现流程定义部署的步骤及实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\07-Activiti实现流程定义部署的步骤及实现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:50, 01:07, 03:49, 05:04, 06:35, 07:47, 08:28, 08:55, 09:49, 10:02, 10:39, 11:20, 11:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:22:36

1) 这一组画面整体在讲如何使用 Activiti 工具部署一个 BPMN 流程定义并验证其数据库表结构。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Activiti 项目结构和一个名为 "holiday.bpmn" 的流程图，流程包含开始事件、两个用户任务和一个结束事件。
画面2: 显示了项目结构，右键菜单展开，准备进行操作。
画面3: 项目结构视图，显示了资源目录下的 BPMN 文件和 Java 类。
画面4: 编辑器中显示了 ActivitiDeployment.java 文件，代码中导入了 ProcessEngine 和 RepositoryService。
画面5: 代码中展示了 RepositoryService 的方法，用于部署流程。
画面6: 代码中调用 repositoryService.createDeployment() 方法，准备部署流程定义。
画面7: 代码中调用 .addClasspathResource() 方法添加资源。
画面8: 代码中调用 .deploy() 方法部署流程。
画面9: 代码中添加了打印部署信息的语句。
画面10: 右键菜单中选择“Run 'ActivitiDeployment_main()'”。
画面11: 控制台输出了 Activiti 部署过程中的 SQL 语句和表结构信息。
画面12: 控制台输出了部署成功的信息，包括部署名称和 ID。
画面13: MySQL Workbench 中执行了删除数据库和创建数据库的 SQL 语句。
画面14: 代码中添加了打印部署信息的语句，控制台输出了部署成功的信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面4:
```java
package com.ithema.activiti;
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.RepositoryService;
```

画面5:
```java
repositoryService.createDeployment()
activateProcessDefinitionById(String s, boolean b, Date date)
activateProcessDefinitionByKey(String s, String s1)
activateProcessDefinitionByKey(String s, boolean b, Date date, String s1)
addCandidateStarterUser(String s, String s1)
addModelEditorSource(String s, byte[] bytes)
```

画面6:
```java
repositoryService.createDeployment()
.addClasspathResource("diagram/holiday.bpmn")
```

画面7:
```java
DeploymentBuilder deploymentBuilder = repositoryService.createDeployment();
deploymentBuilder
    .addClasspathResource("diagram/holiday.bpmn")
    .addClasspathResource("diagram/holiday.png")
    .deploy();
```

画面8:
```java
Deployment deployment = repositoryService.createDeployment()
    .addClasspathResource("diagram/holiday.bpmn")
    .addClasspathResource("diagram/holiday.png")
    .deploy();
```

画面9:
```java
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```

画面11:
```sql
references ACT_GE_BYTEARRAY (ID_)
references ACT_GE_PROPERTY (ID_)
references ACT_ID_GROUP (ID_)
references ACT_ID_MEMBERSHIP (ID_)
references ACT_ID_USER (ID_)
references ACT_RE_DEPLOYMENT (ID_)
references ACT_RE_MODEL (ID_)
references ACT_RE_PROCDEF (ID_)
references ACT_RU_EXECUTION (ID_)
references ACT_RU_IDENTITYLINK (ID_)
references ACT_RU_JOB (ID_)
references ACT_RU_TASK (ID_)
references ACT_RU_VARIABLE (ID_)
```

画面13:
```sql
drop database activiti;
Create database activiti;
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
