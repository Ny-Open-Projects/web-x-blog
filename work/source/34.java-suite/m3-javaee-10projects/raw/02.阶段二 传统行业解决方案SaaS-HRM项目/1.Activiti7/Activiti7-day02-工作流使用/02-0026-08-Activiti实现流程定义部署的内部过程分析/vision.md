# 画面线理解：08-Activiti实现流程定义部署的内部过程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\08-Activiti实现流程定义部署的内部过程分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:25, 00:37, 03:57, 04:06, 04:30, 05:12, 05:17, 06:21, 06:28, 06:39, 07:12, 07:16, 07:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:23:15

1) 这一组画面整体在讲如何通过 Java 代码部署一个 Activiti 工作流流程定义（BPMN 文件）到数据库中。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 ActivitiDeployment.java 代码，其中创建 ProcessEngine 实例并获取 RepositoryService，然后调用 createDeployment() 方法，添加 BPMN 文件和 PNG 图片资源，最后调用 deploy() 方法部署流程定义。
画面2: 在 MySQL Workbench 中执行 SQL 语句，先删除名为 'activiti' 的数据库，然后创建同名数据库。
画面3: 在 MySQL Workbench 中，选中了 'act_re_procdef' 表，准备查看或操作流程定义相关数据。
画面4: 在 MySQL Workbench 的 "Import/Update Blob Field" 窗口中，显示了 BPMN 文件的 XML 内容，其中包含多个 <bpmn:SequenceFlow> 和 <bpmn:StartEvent> 等元素。
画面5: 在 IntelliJ IDEA 中，显示了 BPMN 图形化流程图，包含 StartEvent、用户任务、服务任务和 EndEvent，流程从 StartEvent 开始，依次经过三个任务，最后到达 EndEvent。
画面6: 在 MySQL Workbench 的 "Import/Update Blob Field" 窗口中，显示了 BPMN 文件的 XML 内容，其中包含多个 <bpmn:SequenceFlow> 和 <bpmn:StartEvent> 等元素。
画面7: 在 IntelliJ IDEA 中，显示了 BPMN 图形化流程图，右侧是 BPMN 元素库，包括 StartEvent、EndEvent、UserTask、ServiceTask 等。
画面8: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中导入了 org.activiti.engine.repository.Deployment 包。
画面9: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。
画面10: 在 MySQL Workbench 中，执行 SQL 语句，创建了 'activiti' 数据库，并查询了 'act_re_procdef' 表，显示了部署的流程定义信息。
画面11: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。
画面12: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。
画面13: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。
画面14: 在 IntelliJ IDEA 中，展示了 ActivitiDeployment.java 代码，其中注释说明了流程定义的部署。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
public class ActivitiDeployment {
    public static void main(String[] args) {
        //1.创建ProcessEngine实例
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService实例
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.进行部署
        Deployment deployment = repositoryService.createDeployment()
                .addClasspathResource("diagram/holiday.bpmn") //添加BPMN配置
                .addClasspathResource("diagram/holiday.png") //添加图片
                .name("请假申请单流程")
                .deploy();
        //输出部署的一些信息
        System.out.println(deployment.getName());
        System.out.println(deployment.getId());
    }
}
```

画面2:
```sql
drop database activiti;
create database activiti;
```

画面4:
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<bpmn:definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:activiti="http://activiti.org/bpmn" xmlns:flowable="http://flowable.org/bpmn" id="Definitions_1" targetNamespace="http://www.omg.org/spec/BPMN/20100524/MODEL" typeLanguage="http://www.omg.org/spec/BPMN/20100524/MODEL" expressionLanguage="http://www.w3.org/1999/xpath">
  <bpmn:startEvent id="StartEvent_1" name="StartEvent" />
  <bpmn:userTask id="UserTask_1" name="请假申请" />
  <bpmn:serviceTask id="ServiceTask_1" name="审批" />
  <bpmn:endEvent id="EndEvent_1" name="EndEvent" />
  <bpmn:sequenceFlow id="SequenceFlow_1" sourceRef="StartEvent_1" targetRef="UserTask_1" />
  <bpmn:sequenceFlow id="SequenceFlow_2" sourceRef="UserTask_1" targetRef="ServiceTask_1" />
  <bpmn:sequenceFlow id="SequenceFlow_3" sourceRef="ServiceTask_1" targetRef="EndEvent_1" />
</bpmn:definitions>
```

画面10:
```sql
drop database activiti;
create database activiti;
act_re_deployment
act_re_procdef
act_ge_bytearray
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面7: BPMN 元素库，包含 StartEvent、EndEvent、UserTask、ServiceTask、ManualTask、BusinessRuleTask、CallActivity、ReceiveTask、BoundaryEvent、EventGateway、SubProcess、Lane、ParallelGateway、ExclusiveGateway、InclusiveGateway、IntermediateCatchingEvent、IntermediateThrowingEvent、Annotation 等元素。

5) 无。
