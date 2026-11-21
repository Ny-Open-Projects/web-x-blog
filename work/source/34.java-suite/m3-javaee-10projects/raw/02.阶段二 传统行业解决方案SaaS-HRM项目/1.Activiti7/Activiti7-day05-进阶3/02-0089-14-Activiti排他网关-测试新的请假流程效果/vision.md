# 画面线理解：14-Activiti排他网关-测试新的请假流程效果

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\14-Activiti排他网关-测试新的请假流程效果_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:58, 01:49, 02:32, 03:10, 04:03, 04:41, 05:20, 05:58, 06:33, 08:04, 08:50, 09:42, 11:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:22:17

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Activiti 工作流引擎部署 BPMN 流程定义，并通过 Java 代码启动流程实例、处理任务，以及在流程图中配置排他网关的条件分支。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 代码：在 `ExclusiveGateWayTest01.java` 中，使用 `repositoryService.createDeployment()` 方法部署流程定义，指定资源文件路径为 `diagram/holiday4.bpmn` 和 `diagram/holiday4.png`，并设置部署名称为“请假申请流程”。
- 代码：部署完成后，打印部署名称和 ID。

画面2：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面1类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面3：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面2类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面4：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面3类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面5：
- 代码：在 `Activiti-7` 的 SQL 客户端中，显示了 BPMN 流程定义的 XML 内容，包括流程定义 ID、名称、版本、活动定义等信息。

画面6：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面5类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面7：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面6类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面8：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面7类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面9：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面8类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面10：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面9类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面11：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面10类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面12：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面11类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面13：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面12类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

画面14：
- 代码：在 `ExclusiveGateWayTest02.java` 中，代码结构与画面13类似，但部署的资源文件路径改为 `diagram/day05/holiday5.bpmn` 和 `diagram/day05/holiday5.png`，部署名称为“请假申请流程”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1.部署流程定义
//2.得到ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//3.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//4.进行部署
Deployment deployment = repositoryService.createDeployment()
		.addClasspathResource("diagram/holiday4.bpmn") //添加bpmn资源
		.addClasspathResource("diagram/holiday4.png") //添加图片资源
		.name("请假申请流程")
		.deploy();
//5.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getDeploymentId());
```

画面2：
```java
//1.部署流程定义
//2.得到ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//3.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//4.进行部署
Deployment deployment = repositoryService.createDeployment()
		.addClasspathResource("diagram/day05/holiday5.bpmn") //添加bpmn资源
		.addClasspathResource("diagram/day05/holiday5.png") //添加图片资源
		.name("请假申请流程")
		.deploy();
//5.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getDeploymentId());
```

画面3：
```java
//1.部署流程定义
//2.得到ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//3.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//4.进行部署
Deployment deployment = repositoryService.createDeployment()
		.addClasspathResource("diagram/day05/holiday5.bpmn") //添加bpmn资源
		.addClasspathResource("diagram/day05/holiday5.png") //添加图片资源
		.name("请假申请流程")
		.deploy();
//5.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getDeploymentId());
```

画面4：
```java
//1.部署流程定义
//2.得到ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//3.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//4.进行部署
Deployment deployment = repositoryService.createDeployment()
		.addClasspathResource("diagram/day05/holiday5.bpmn") //添加bpmn资源
		.addClasspathResource("diagram/day05/holiday5.png") //添加图片资源
		.name("请假申请流程")
		.deploy();
//5.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getDeploymentId());
```

画面5：
```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
	xmlns:activiti="http://activiti.org/bpmn" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd
		http://activiti.org/bpmn activiti.xsd">
	<process id="holiday" name="ExclusiveGateWay" isExecutable="true">
		<startEvent id="startEvent" name="开始事件"></startEvent>
		<userTask id="userTask" name="部门经理审批" activiti:assignee="wangwu"></userTask>
		<exclusiveGateway id="exclusiveGateway" name="排他网关" activiti:default="true">
			<sequenceFlow id="flow1" sourceRef="userTask" targetRef="endEvent"></sequenceFlow>
			<sequenceFlow id="flow2" sourceRef="userTask" targetRef="endEvent"></sequenceFlow>
		</exclusiveGateway>
		<endEvent id="endEvent" name="结束事件"></endEvent>
		<sequenceFlow id="flow3" sourceRef="startEvent" targetRef="userTask"></sequenceFlow>
		<sequenceFlow id="flow4" sourceRef="userTask" targetRef="exclusiveGateway"></sequenceFlow>
		<sequenceFlow id="flow5" sourceRef="exclusiveGateway" targetRef="endEvent"></sequenceFlow>
	</process>
</definitions>
```

画面6：
```java
//1.部署流程定义
//2.得到ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcess
