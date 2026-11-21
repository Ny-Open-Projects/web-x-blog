# 画面线理解：11-Activiti网关-基本概述

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\11-Activiti网关-基本概述_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:17, 00:20, 00:25, 00:26, 01:02, 01:14, 01:32, 01:53, 01:54, 02:20, 02:26, 02:37, 02:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:20:15

1) 这一组画面整体在讲什么（一句话）：
讲解工作流引擎中排他网关（XOR网关）的概念、作用及在流程图中的应用，并通过代码演示如何操作任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT第5章“网关”中的5.1.1节“什么是排他网关”，解释排他网关用于流程决策，当流程序执行到该网关时，所有分支都会判断条件是否为true，如果为true则执行该分支。注意：排他网关只会选择一个为true的分支执行。
画面2：展示Java代码，用于执行任务，包括创建任务查询、设置负责人、执行任务等操作。
画面3：展示Java代码，与画面2相同，但显示了项目结构，包含resources目录下的holiday.bpmn文件。
画面4：展示项目结构，选中了holiday.bpmn文件。
画面5：展示BPMN流程图，包含StartEvent、用户任务、排他网关、用户任务和EndEvent。
画面6：展示BPMN流程图，排他网关的条件设置为“${holiday.num>3}”。
画面7：展示BPMN流程图，排他网关的条件设置为“${holiday.num>3}”。
画面8：展示PPT第5章“网关”中的5.1.1节“什么是排他网关”，与画面1相同。
画面9：展示PPT第5章“网关”中的5.1.1节“什么是排他网关”，与画面1相同。
画面10：展示BPMN流程图，排他网关的条件设置为“${holiday.num>3}”。
画面11：展示PPT第5章“网关”中的5.1.1节“什么是排他网关”，与画面1相同。
画面12：展示PPT第5章“网关”中的5.1.1节“什么是排他网关”，与画面1相同。
画面13：展示BPMN流程图，排他网关的条件设置为“${holiday.num>3}”。
画面14：展示PPT第5章“网关”中的5.1.1节“什么是排他网关”，与画面1相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public static void main(String[] args) {
    String key = "myProcess_1";
    String assignee = "lisi";
    //4.执行查询
    Task task = taskService.createTaskQuery()
            .processDefinitionKey(key)
            .taskAssignee(assignee) //设置任务的负责人
            .singleResult();
    //5.执行当前的任务
    if(task!=null){
        taskService.complete(task.getId());
        System.out.println("任务执行完毕！");
    }
    //6.当前的用户查询自己的任务
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //7.得到TaskService对象
    TaskService taskService = processEngine.getTaskService();
}
```

画面4：
```
resources
├── diagram
│   ├── holiday.bpmn
│   └── holiday2.bpmn
└── holiday.bpmn
```

画面5：
```
StartEvent → 用户请假申请 → 排他网关(${holiday.num>3}) → 部门经理审批 → 总经理审批 → EndEvent
```

画面6：
```
Condition: ${holiday.num>3}
```

画面7：
```
Condition: ${holiday.num>3}
```

画面10：
```
Condition: ${holiday.num>3}
```

画面13：
```
Condition: ${holiday.num>3}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、8、9、11、12、14：
标题：第5章 网关
子标题：5.1 排他网关
内容：
排他网关（也叫异或（XOR）网关，或叫基于数据的排他网关），用来在流程中实现决策。当流程执行到这个网关，所有分支都会判断条件是否为true，如果为true则执行该分支。
注意：排他网关只会选择一个为true的分支执行。
为什么要用排他网关？不用排他网关也可以实现分支，如下图：
流程图：
StartEvent → 用户请假申请 → 排他网关(${holiday.num>3}) → 部门经理审批 → 总经理审批 → EndEvent

画面5、6、7、10、13：
流程图：
StartEvent → 用户请假申请 → 排他网关(${holiday.num>3}) → 部门经理审批 → 总经理审批 → EndEvent

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
