# 画面线理解：03-Activiti流程定义信息删除的注意事项

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\03-Activiti流程定义信息删除的注意事项_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:24, 01:34, 01:50, 02:07, 02:24, 03:27, 03:56, 04:16, 04:42, 05:15, 05:22, 05:42, 06:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:37:05

1) 这一组画面整体在讲如何通过 Java 代码删除已部署的 Activiti 流程定义，并展示相关数据库表结构和流程图元素。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IDEA 编辑器中 DeleteProcessDefinition.java 文件，包含 package 声明和类定义，下方运行日志显示成功删除部署。
画面2：展示 MySQL Workbench 中的 SQL 脚本，用于创建 activiti 数据库和列出相关表结构。
画面3：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，注释说明获取 ProcessEngine 和 RepositoryService。
画面4：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面5：展示 PPT 页面，标题为“6.4 流程定义删除”，内容为 deleteDeployment() 方法的 Java 代码，包含注释说明。
画面6：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面7：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面8：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面9：展示 Activiti Designer 中的 BPMN 流程图，包含 StartEvent、UserTask、EndEvent 等元素，右侧为元素面板。
画面10：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面11：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1")。
画面12：展示 PPT 页面，标题为“删除已经部署成功的流程定义”，内容为 deleteDeployment() 方法的 Java 代码，包含注释说明。
画面13：展示 MySQL Workbench 中的 SQL 脚本，用于创建 activiti 数据库和列出相关表结构，下方显示了表数据。
画面14：IDEA 中展示 DeleteProcessDefinition.java 的 main 方法，高亮显示 repositoryService.deleteDeployment("1", true)。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
package com.itheima.day03.activiti;
import ...
//我已经写好的流程定义
//后面讲解删除
public class DeleteProcessDefinition {

画面3：
public static void main(String[] args) {
    //1.得到ProcessEngine对象
    ProcessEngine processEngine = ProcessEngine.getDefaulltProcessEngine();
    //2.创建RepositoryService对象
    RepositoryService repositoryService = processEngine.getRepositoryService();
    //3.执行删除流程定义，参数代表流程部署的id
    repositoryService.deleteDeployment("1");
}

画面5：
public void deleteDeployment() {
    // 流程部署Id
    String deploymentId = "8801";
    // 通过流程引擎获取repositoryService
    RepositoryService repositoryService = processEngine
        .getRepositoryService();
    //删除流程定义，如果该流程定义已有流程实例启动则删除时出错
    repositoryService.deleteDeployment(deploymentId);
    //设置true 级联删除流程定义，即使该流程有流程实例自动也可以删除，设置为false非级联删除方式，如果流程
    //repositoryService.deleteDeployment(deploymentId, true);
}

画面12：
public void deleteDeployment() {
    // 流程部署Id
    String deploymentId = "8801";
    // 通过流程引擎获取repositoryService
    RepositoryService repositoryService = processEngine
        .getRepositoryService();
    //删除流程定义，如果该流程定义已有流程实例启动则删除时出错
    repositoryService.deleteDeployment(deploymentId);
    //设置true 级联删除流程定义，即使该流程有流程实例自动也可以删除，设置为false非级联删除方式，如果流程
    //repositoryService.deleteDeployment(deploymentId, true);
}

画面14：
repositoryService.deleteDeployment("1", true);

画面2：
drop database activiti;
create database activiti;
act_re_deployment 部署信息
act_re_procdef 流程定义的一些信息
act_re_bytearray 流程定义的bpmn文件及png文件
#背后影响的表：
act_hi_actinst 已完成的活动信息
act_hi_identitylink 参与者信息
act_hi_procinst 流程实例
act_hi_taskinst 任务实例
act_ru_execution 执行表

画面13：
drop database activiti;
create database activiti;
act_re_deployment 部署信息
act_re_procdef 流程定义的一些信息
act_re_bytearray 流程定义的bpmn文件及png文件
#背后影响的表：
act_hi_actinst 已完成的活动信息
act_hi_identitylink 参与者信息
act_hi_procinst 流程实例
act_hi_taskinst 任务实例
act_ru_execution 执行表

4) PPT 标题、架构图/流程图的结构、表格数据：
画面5：
标题：6.4 流程定义删除
内容：public void deleteDeployment() { ... } 方法代码，包含注释说明。
画面12：
标题：删除已经部署成功的流程定义
内容：public void deleteDeployment() { ... } 方法代码，包含注释说明。
画面9：
流程图结构：StartEvent → UserTask → EndEvent
元素面板：StartEvent, EndEvent, UserTask, ScriptTask, ServiceTask, ManualTask, BusinessRuleTask, SubProcess, Lane, ParallelGateway, ExclusiveGateway, InclusiveGateway, EventGateway, IntermediateCatchingEvent, IntermediateThrowingEvent。
画面13：
表格数据：包含 PROC_DEF_ID_, DEPLOYMENT_ID_, ACT_ID_, TASK_ID_, ACT_NAME_, ACT_TYPE_, ASSIGNEE_, START_, END_ 等列，显示了多行数据。

5) 无。
