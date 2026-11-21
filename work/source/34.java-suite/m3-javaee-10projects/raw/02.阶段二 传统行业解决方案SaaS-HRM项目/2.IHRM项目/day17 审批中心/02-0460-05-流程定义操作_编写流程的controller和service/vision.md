# 画面线理解：05-流程定义操作：编写流程的controller和service

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\05-流程定义操作：编写流程的controller和service_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:49, 01:58, 02:52, 04:41, 05:29, 05:56, 06:22, 07:13, 08:09, 10:13, 10:50, 11:35, 12:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:03:23

1) 这一组画面整体在讲如何通过代码实现对工作流（流程定义）的部署、查询和挂起/激活操作。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了测试类 ProcessTest.java 中的 testSuspend 方法，用于测试挂起流程定义。
- 代码中调用了 repositoryService.suspendProcessDefinitionById 方法挂起流程。
- 代码中也调用了 repositoryService.activateProcessDefinitionById 方法激活流程。
- 画面下方的测试结果表明测试通过。

画面2：
- 展示了一个“审批设置”界面，用于查看和操作流程定义。
- 界面包含三个按钮：“请假”、“加班/出差”、“离职”。

画面3：
- 展示了“审批设置”界面，三个按钮分别被选中，显示为“请假”、“加班/出差”、“离职”。
- 界面下方新增了“2.点击按钮控制流程是否可用”的说明。

画面4：
- 展示了测试类 ProcessTest.java 中的 findall 方法，用于查询流程定义。
- 代码中使用 repositoryService.createProcessDefinitionQuery() 创建查询对象，并设置查询条件。
- 代码中调用了 query.latestVersion().list() 获取最新版本的流程定义列表。

画面5：
- 展示了控制器类 ProcessController.java 中的 deployProcess 方法，用于部署流程定义。
- 代码中接收文件和公司ID参数，调用 processService.deployProcess 方法进行部署。
- 代码中返回 Result.SUCCESS 表示部署成功。

画面6：
- 展示了服务类 ProcessService.java 中的 getProcessDefinitionList 方法，用于获取流程定义列表。
- 代码中使用 repositoryService.createProcessDefinitionQuery() 创建查询对象，并设置查询条件。
- 代码中调用了 query.latestVersion().list() 获取最新版本的流程定义列表。

画面7：
- 展示了控制器类 ProcessController.java 中的 definitionList 方法，用于查询流程定义列表。
- 代码中调用 processService.getProcessDefinitionList(companyId) 获取流程定义列表。
- 代码中返回 Result.SUCCESS 表示查询成功。

画面8：
- 展示了控制器类 ProcessController.java 中的 definitionList 方法，用于查询流程定义列表。
- 代码中调用 processService.getProcessDefinitionList(companyId) 获取流程定义列表。
- 代码中返回 Result.SUCCESS 表示查询成功。

画面9：
- 展示了“审批设置”界面，三个按钮分别被选中，显示为“请假”、“加班/出差”、“离职”。
- 界面下方新增了“规则”说明：
  - 如果流程已经激活：设置为挂起
  - 如果流程以及挂起：设置为激活

画面10：
- 展示了控制器类 ProcessController.java 中的 suspendProcess 方法，用于挂起流程定义。
- 代码中接收 processKey 参数，调用 processService.suspendProcess 方法进行挂起。
- 代码中返回 Result.SUCCESS 表示挂起成功。

画面11：
- 展示了服务类 ProcessService.java 中的 suspendProcess 方法，用于挂起流程定义。
- 代码中使用 repositoryService.createProcessDefinitionQuery() 创建查询对象，并设置查询条件。
- 代码中调用了 query.processDefinitionKey(processKey).processDefinitionTenantId(companyId).latestVersion().singleResult() 获取流程定义对象。

画面12：
- 展示了控制器类 ProcessController.java 中的 suspendProcess 方法，用于挂起流程定义。
- 代码中接收 processKey 参数，调用 processService.suspendProcess 方法进行挂起。
- 代码中返回 Result.SUCCESS 表示挂起成功。

画面13：
- 展示了服务类 ProcessService.java 中的 suspendProcess 方法，用于挂起流程定义。
- 代码中使用 repositoryService.createProcessDefinitionQuery() 创建查询对象，并设置查询条件。
- 代码中调用了 query.processDefinitionKey(processKey).processDefinitionTenantId(companyId).latestVersion().singleResult() 获取流程定义对象。
- 代码中判断 definition.isSuspended() 是否为真，如果是则调用 activateProcessDefinitionById 方法激活流程，否则调用 suspendProcessDefinitionById 方法挂起流程。

画面14：
- 展示了服务类 ProcessService.java 中的 suspendProcess 方法，用于挂起流程定义。
- 代码中使用 repositoryService.createProcessDefinitionQuery() 创建查询对象，并设置查询条件。
- 代码中调用了 query.processDefinitionKey(processKey).processDefinitionTenantId(companyId).latestVersion().singleResult() 获取流程定义对象。
- 代码中判断 definition.isSuspended() 是否为真，如果是则调用 activateProcessDefinitionById 方法激活流程，否则调用 suspendProcessDefinitionById 方法挂起流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
System.out.println(list.size());
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程定义状态
//流程状态
//流程
