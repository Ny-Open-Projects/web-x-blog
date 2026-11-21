# 画面线理解：13-Activiti排他网关示例-请假流程定义

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\13-Activiti排他网关示例-请假流程定义_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:22, 00:25, 00:28, 01:06, 01:09, 02:09, 03:00, 03:42, 04:12, 04:24, 05:10, 05:49, 05:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:21:24

1) 这一组画面整体在讲如何使用 Activiti 工作流引擎中的排他网关（Exclusive Gateway）来实现基于条件的流程分支，并通过代码部署 BPMN 流程定义。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Java 代码文件 ExclusiveGateWayTest01.java，其中包含部署 BPMN 流程定义的代码，路径指向 resources/day05 目录下的 holiday4.bpmn 文件。
画面2: PPT 页面，讲解排他网关的执行逻辑：只选择一个为 true 的分支执行，并对比了不使用排他网关时流程会异常结束的情况。
画面3: PPT 页面，展示使用排他网关决定分支走向的流程图，包含 StartEvent、排他网关、两个任务节点和 EndEvent。
画面4: PPT 页面，展示排他网关流程图的完整版本，包含条件判断和结束事件。
画面5: IDE 中右键点击 resources/day05 目录，弹出菜单，准备运行测试。
画面6: IDE 中显示 ExclusiveGateWayTest01.java 代码，光标位于第 78 行，准备部署流程。
画面7: BPMN 编辑器界面，显示一个简单的流程：StartEvent → 用户任务 → EndEvent。
画面8: BPMN 编辑器界面，添加了一个排他网关（ExclusiveGateway）在用户任务和结束事件之间。
画面9: BPMN 编辑器界面，连接 StartEvent 到用户任务，再连接用户任务到排他网关。
画面10: BPMN 编辑器界面，连接排他网关到“总经理审批”任务。
画面11: BPMN 编辑器界面，连接排他网关到“人事经理存档”任务。
画面12: BPMN 编辑器界面，为排他网关添加条件：holiday_num > 3。
画面13: BPMN 编辑器界面，为排他网关添加另一个条件：holiday_num <= 3。
画面14: BPMN 编辑器界面，完成流程图设计，显示 StartEvent → 用户任务 → 排他网关 → 两个分支任务 → EndEvent。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1 代码：
```java
//1.设置流程定义
//public static void main(String[] args) {
//    //1.创建ProcessEngine实例
//    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//    //2.创建RepositoryService实例
//    RepositoryService repositoryService = processEngine.getRepositoryService();
//    //3.得到部署对象
//    Deployment deployment = repositoryService.createDeployment()
//            .addClasspathResource("diagram/holiday4.bpmn") //添加Bpmn资源
//            .name("请假申请流程") //设置部署名称
//            .deploy();
//    //4.输出部署的一些信息
//    System.out.println(deployment.getName());
//    System.out.println(deployment.getId());
//}
```

画面6 代码：
```java
//1.设置流程定义
//public static void main(String[] args) {
//    //1.创建ProcessEngine实例
//    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//    //2.创建RepositoryService实例
//    RepositoryService repositoryService = processEngine.getRepositoryService();
//    //3.得到部署对象
//    Deployment deployment = repositoryService.createDeployment()
//            .addClasspathResource("diagram/holiday4.bpmn") //添加Bpmn资源
//            .name("请假申请流程") //设置部署名称
//            .deploy();
//    //4.输出部署的一些信息
//    System.out.println(deployment.getName());
//    System.out.println(deployment.getId());
//}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2 PPT 标题：
- “执行到这个网关，所有分支都会判断条件是否为 true，如果为 true 则执行该分支。”
- “注意，排他网关只会选择一个为 true 的分支执行（即使有两个分支条件都为 true，排他网关也会只选择一条分支去执行）”
- “为什么要用排他网关？不用排他网关也可以实现分支，如下图：”

画面2 流程图结构：
- StartEvent → 排他网关（无条件）→ 总经理审批 → 人事经理存档 → EndEvent
- 条件：holiday_num > 3

画面3 流程图结构：
- StartEvent → 排他网关（无条件）→ 总经理审批 → 人事经理存档 → EndEvent
- 条件：holiday_num > 3

画面4 流程图结构：
- StartEvent → 排他网关（无条件）→ 总经理审批 → 人事经理存档 → EndEvent
- 条件：holiday_num > 3

画面12 流程图结构：
- StartEvent → 用户任务 → 排他网关（条件：holiday_num > 3）→ 总经理审批 → 人事经理存档 → EndEvent

画面13 流程图结构：
- StartEvent → 用户任务 → 排他网关（条件：holiday_num <= 3）→ 人事经理存档 → EndEvent

5) 无其他内容。
