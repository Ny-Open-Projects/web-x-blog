# 画面线理解：12-Activiti排他网关概述及场景引入

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\12-Activiti排他网关概述及场景引入_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 02:39, 04:54, 05:28, 06:34, 07:07, 07:49, 08:24, 09:14, 09:46, 10:29, 11:06, 12:42, 13:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:20:51

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中排他网关（Exclusive Gateway）的概念、流程图示例及 Java 代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面，标题为“5.1.1 什么是排他网关”，解释排他网关用于流程中实现决策，只选择一个 true 分支执行。
画面2：展示流程图，说明排他网关的逻辑：当 holiday.num=3 时执行“总经理审批”，否则执行“人事经理审批”。
画面3：在 IDEA 中打开项目，展示 BPMN 图形界面，显示排他网关流程图。
画面4：展示 Java 代码文件 ExclusiveGatewayTest01.java，用于测试排他网关。
画面5：在 IDEA 中打开 holiday4.bpmn 文件，显示排他网关流程图。
画面6：在 IDEA 中浏览项目结构，显示 day05 目录下的多个 BPMN 文件。
画面7：在 IDEA 中打开 ExclusiveGatewayTest01.java，展示部署流程定义的代码。
画面8：在 IDEA 中展示代码，显示创建 Holiday 对象并设置属性。
画面9：在 IDEA 中展示代码，显示创建流程实例并打印 ID。
画面10：桌面截图，显示“holiday4.bpmn”文件被选中。
画面11：在 IDEA 中展示流程图，显示排他网关的条件设置。
画面12：在 SQLyog 中执行 SQL 语句，创建数据库 activiti。
画面13：展示 PPT 页面，标题为“5.1.1 什么是排他网关”，解释排他网关用于流程中实现决策，只选择一个 true 分支执行。
画面14：在 IDEA 中展示流程图，显示排他网关的条件设置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```java
package com.ithema.day05;

//排他网关存在的意义
public class ExclusiveGatewayTest01 {
    //1. 填写任务的业务说明
    //public static void main(String[] args) {
    //2. 得到ProcessEngine实例
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //3. 得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
    //4. 查询当前用户任务
    Task task = taskService.createTaskQuery()
            .processDefinitionKey("myProcess_1")
            .taskAssignee("xiaoZhang")
            .singleResult();
    //5. 完成当前用户任务列表的某项操作的话，任务ID.task.getId()
    if(task != null){
        taskService.complete(task.getId());
        System.out.println("用户任务执行完毕。");
    }
}
```

画面7：
```java
//1. 需要定义流程
//public static void main(String[] args) {
//2. 得到ProcessEngine实例
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//3. 得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//4. 部署流程
Deployment deployment = repositoryService.createDeployment()
        .addClasspathResource("diagram/holiday4.bpmn")
        .name("请假审批流程")
        .deploy();
//5. 输出部署的一些信息
System.out.println("部署ID：" + deployment.getId());
System.out.println("部署名称：" + deployment.getName());
```

画面8：
```java
//2. 启动流程引擎
public static void main(String[] args) {
    //1. 得到ProcessEngine实例
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2. 得到RuntimeService对象
    RuntimeService runtimeService = processEngine.getRuntimeService();
    Holiday holiday = new Holiday();
    holiday.setNum(3);
    //3. 创建流程实例，定义的key需要一致
    Map<String, Object> map = new HashMap<>();
    map.put("holiday", holiday);
    //4. 启动流程实例
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("myProcess_1", map);
    //5. 输出流程实例的相关信息
    System.out.println("流程定义ID：" + processInstance.getProcessDefinitionId()); //holiday:1:4
    System.out.println("流程实例ID：" + processInstance.getId()); //2501
}
```

画面12：
```sql
drop database activiti;
create database activiti;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题“5.1.1 什么是排他网关”，内容解释排他网关用于流程中实现决策，只选择一个 true 分支执行。
画面2：流程图结构：StartEvent → 排他网关（条件：holiday.num=3） → 总经理审批 → 人事经理审批 → EndEvent。
画面3：BPMN 图形界面，显示排他网关流程图。
画面5：BPMN 图形界面，显示排他网关流程图。
画面7：BPMN 图形界面，显示排他网关流程图。
画面11：BPMN 图形界面，显示排他网关流程图。
画面14：BPMN 图形界面，显示排他网关流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
