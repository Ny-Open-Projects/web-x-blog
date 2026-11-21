# 画面线理解：01-Activiti流程定义信息查询

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\01-Activiti流程定义信息查询_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:31, 01:13, 01:45, 02:39, 03:18, 04:37, 07:26, 08:29, 09:58, 11:10, 12:15, 13:47, 14:10, 14:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:35:28

1) 这一组画面整体在讲如何通过 Activiti 的 RepositoryService 查询已部署的流程定义，并输出其基本信息。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 PPT 页面“6.3 流程定义查询”，代码示例为查询流程定义的 Java 方法，其中定义了流程定义键为 "holiday"，并获取 RepositoryService。
画面2: 展示了 PPT 页面“6.4 流程定义删除”，代码示例为遍历查询结果并打印流程部署 ID、流程定义 ID、名称、键和版本。
画面3: 展示了 PPT 页面“6.3 流程定义查询”，代码示例与画面1相同，但底部有黑马程序员的联系方式。
画面4: 展示了 PPT 页面“6.3 流程定义查询”，代码示例与画面1相同。
画面5: 展示了 IntelliJ IDEA 的项目结构，选中了“holiday.bpmn”文件，准备进行操作。
画面6: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，包含 main 方法，用于获取默认的 ProcessEngine。
画面7: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中获取了 RepositoryService。
画面8: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中创建了 ProcessDefinitionQuery。
画面9: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中设置了查询条件，指定流程定义键为 "holiday"。
画面10: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中调用 .orderByProcessDefinitionVersion().desc() 对查询结果按版本降序排列。
画面11: 展示了 PPT 页面“6.4 流程定义删除”，代码示例为遍历查询结果并打印流程部署 ID、流程定义 ID、名称、键和版本。
画面12: 展示了 MySQL Workbench，显示了 activiti 数据库的表结构，其中 act_hi_procinst 表被选中，下方显示了 holiday 流程定义的记录。
画面13: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中执行了查询并打印了结果。
画面14: 展示了 IntelliJ IDEA 中的 Java 类 QueryProcessDefinition，main 方法中执行了查询并打印了结果，终端输出了查询到的流程定义信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
// 流程定义查询
@Test
public void queryProcessDefinition() {
    // 流程定义key
    String processDefinitionKey = "holiday";
    // 获取repositoryService
    RepositoryService repositoryService = processEngine
            .getRepositoryService();
    // 查询流程定义
    ProcessDefinitionQuery processDefinitionQuery = repositoryService
            .createProcessDefinitionQuery();
    // 遍历查询结果
    List<ProcessDefinition> list = processDefinitionQuery
            .processDefinitionKey(processDefinitionKey)
```

画面2:
```java
.orderByProcessDefinitionVersion().desc().list();
for (ProcessDefinition processDefinition : list) {
    System.out.println("------------------");
    System.out.println("流程部署id：" + processDefinition.getDeploymentId());
    System.out.println("流程定义Id：" + processDefinition.getId());
    System.out.println("流程定义名称：" + processDefinition.getName());
    System.out.println("流程定义key：" + processDefinition.getKey());
    System.out.println("流程定义版本：" + processDefinition.getVersion());
}
```

画面6:
```java
package com.ithema.day03.activiti;
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
```

画面7:
```java
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
RepositoryService repositoryService = processEngine.getRepositoryService();
```

画面8:
```java
ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
```

画面9:
```java
processDefinitionQuery.processDefinitionKey("holiday")
```

画面10:
```java
processDefinitionQuery.processDefinitionKey("holiday")
.orderByProcessDefinitionVersion().desc()
```

画面13:
```java
List<ProcessDefinition> list = processDefinitionQuery.processDefinitionKey("holiday")
.orderByProcessDefinitionVersion().desc().list();
for(ProcessDefinition processDefinition : list){
    System.out.println("流程定义ID：" + processDefinition.getId());
    System.out.println("流程定义名称：" + processDefinition.getName());
    System.out.println("流程定义的Key：" + processDefinition.getKey());
    System.out.println("流程定义的版本号：" + processDefinition.getVersion());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1: 标题为“6.3 流程定义查询”，副标题为“查询部署的流程定义”。
画面2: 标题为“6.4 流程定义删除”。
画面3: 标题为“6.3 流程定义查询”，底部有黑马程序员的联系方式。
画面4: 标题为“6.3 流程定义查询”，副标题为“查询部署的流程定义”。
画面11: 标题为“6.4 流程定义删除”，代码示例为遍历查询结果并打印流程部署 ID、流程定义 ID、名称、键和版本。
画面12: 表格数据为 activiti 数据库的表结构，其中 act_hi_procinst 表被选中，下方显示了 holiday 流程定义的记录。

5) 不要评价画面美观，不要输出与课程无关的内容。
