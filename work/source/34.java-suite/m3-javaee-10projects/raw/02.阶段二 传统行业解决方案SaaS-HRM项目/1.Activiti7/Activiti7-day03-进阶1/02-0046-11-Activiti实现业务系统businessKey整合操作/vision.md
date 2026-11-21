# 画面线理解：11-Activiti实现业务系统businessKey整合操作

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\11-Activiti实现业务系统businessKey整合操作_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:12, 00:52, 02:33, 03:02, 03:36, 05:08, 08:03, 08:26, 09:21, 09:45, 10:48, 12:30, 13:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:43:33

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中如何通过 businessKey 启动流程实例，并演示了相关的 Java 代码和数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Java 代码，用于查询正在运行的流程实例，获取其 ID、所属流程定义 ID 和是否执行完成状态。
画面2：展示 PPT 内容，说明开始一个任务时会向 act_ru_task 和 act_hi_actinst 表插入记录。
画面3：展示 PPT 内容，解释 businessKey 的概念及其在 Activiti 中的存储方式，并展示数据库表中 businessKey 的值。
画面4：展示 IntelliJ IDEA 中的项目结构，包含 src、resources 等目录，以及 BusinessKeyAdd.java 文件。
画面5：展示 BusinessKeyAdd.java 文件的初始状态，仅包含 package 和 class 声明。
画面6：展示在 BusinessKeyAdd.java 中调用 ProcessEngine 的 getRuntimeService() 方法，弹出方法签名提示。
画面7：展示在 BusinessKeyAdd.java 中调用 RuntimeService 的 startProcessInstanceByKey() 方法，准备启动流程实例。
画面8：展示 MySQL Workbench 中的 SQL 语句，用于删除 activiti 数据库并创建新数据库。
画面9：展示在 BusinessKeyAdd.java 中调用 startProcessInstanceByKey() 方法，第一个参数为流程定义 key "holiday"。
画面10：展示在 BusinessKeyAdd.java 中调用 startProcessInstanceByKey() 方法，第二个参数为 businessKey "1001"。
画面11：展示在 BusinessKeyAdd.java 中导入 Spring 相关的 XML Schema。
画面12：展示在 BusinessKeyAdd.java 中完成代码编写，包含启动流程实例和打印 businessKey 的逻辑。
画面13：展示在 BusinessKeyAdd.java 中运行成功，终端输出了流程实例的 businessKey 值。
画面14：展示 PPT 内容，再次强调 businessKey 的作用，并展示数据库表中 businessKey 的值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Test
public void queryProcessInstance() {
    // 流程定义key
    String processDefinitionKey = "holiday";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    List<ProcessInstance> list = runtimeService
            .createProcessInstanceQuery()
            .processDefinitionKey(processDefinitionKey)
            .list();

    for (ProcessInstance processInstance : list) {
        System.out.println("------------------------");
        System.out.println("流程实例Id：" + processInstance.getProcessInstanceId());
        System.out.println("所属流程定义Id：" + processInstance.getProcessDefinitionId());
        System.out.println("是否执行完成：" + processInstance.isEnded());
    }
}
```

画面2：
```sql
SELECT * FROM act_ru_task;  # 任务历史表，记录所有任务
SELECT * FROM act_hi_actinst; # 活动历史表，记录所有活动
```

画面3：
```java
// 根据流程定义的key启动一个流程实例
ProcessInstance processInstance = runtimeService
        .startProcessInstanceByKey(processDefinitionKey,
        businessKey);
```

画面4：
```
src
├── main
│   └── java
│       └── com
│           └── ithema
│               └── day03
│                   └── activiti
│                       └── BusinessKeyAdd.java
└── resources
    ├── diagram
    │   ├── holiday.hpmn
    │   ├── holiday.png
    │   └── holiday.bpmn
```

画面6：
```java
RuntimeService runtimeService = processEngine.getRuntimeService();
```

画面7：
```java
runtimeService.startProcessInstanceByKey();
```

画面8：
```sql
1 drop database activiti;
3 create database activiti;
```

画面9：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", 
```

画面10：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", "1001");
```

画面11：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context-3.0.xsd
        http://www.springframework.org/schema/tx
        http://www.springframework.org/schema/tx/spring-tx-3.0.xsd">
```

画面12：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", "1001");
System.out.println(processInstance.getBusinessKey());
```

画面13：
```java
System.out.println(processInstance.getBusinessKey());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
标题：开始一个任务，不仅在 act_ru_task 表插入记录，也会在历史任务表插入一条记录，任务历史表的主键就是任务 id，任务完成此表记录不删除。
表格数据：
| 表名 | 说明 |
|------|------|
| act_ru_task | 任务历史表，记录所有任务 |
| act_hi_actinst | 活动历史表，记录所有活动 |

画面3：
标题：Businesskey：业务标识，通常为业务表的主键，业务标识和流程实例一一对应。
表格数据：
| ID | REV | PROC_INST_ID | BUSINESS_KEY | PARENT_ID | PROC_DEF_ID |
|----|-----|--------------|---------------|-----------|-------------|
| 1401 | 1 | 1401 | 1001 | (NULL) | purchasingFlow:1.1:1 |
| 1501 | 1 | 1501 | 1001 | (NULL) | purchasingFlow:1.1:1 |

画面14：
标题：Businesskey：业务标识，通常为业务表的主键，业务标识和流程实例一一对应。
表格数据：
| ID | REV | PROC_INST_ID | BUSINESS_KEY | PARENT_ID | PROC_DEF_ID |
|----|-----|--------------|---------------|-----------|-------------|
| 1401 | 1 | 1401 | 1001 | (NULL) | purchasingFlow:1.1:1 |
| 1501 | 1 | 1501 | 1001 | (NULL) | purchasingFlow:1.1:1 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
