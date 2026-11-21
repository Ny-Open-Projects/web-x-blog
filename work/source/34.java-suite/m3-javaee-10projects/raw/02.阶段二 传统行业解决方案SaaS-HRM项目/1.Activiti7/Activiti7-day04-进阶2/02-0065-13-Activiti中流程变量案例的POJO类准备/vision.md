# 画面线理解：13-Activiti中流程变量案例的POJO类准备

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\13-Activiti中流程变量案例的POJO类准备_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:00, 01:46, 02:43, 03:12, 04:19, 05:23, 06:14, 07:31, 08:07, 09:00, 09:46, 10:35, 12:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:00:22

1) 这一组画面整体在讲如何在 Activiti 工作流中设置和使用全局流程变量，包括启动流程时设置变量和任务办理时设置变量，并通过 Java 代码实现。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 BPMN 流程图，包含 StartEvent、用户任务、排他网关、用户任务和 EndEvent。右侧工具栏显示了 BPMN 元素类型。
画面2: PPT 页面标题为“3.5.3 设置 global 流程变量”，子标题“3.5.3.1 启动流程时设置”，内容说明启动流程时设置流程变量，变量值为请假单信息，作用域为整个流程实例。
画面3: PPT 页面展示 Java 代码，用于启动流程并设置变量，变量名为“num”，值为 holiday.getNum()。
画面4: PPT 页面标题为“3.5.3.2 任务办理时设置”，内容说明在完成任务时设置流程变量，变量作用域为整个流程实例。
画面5: 展示了 BPMN 流程图，与画面1类似，但“请假单审批”任务节点被选中。
画面6: 展示了 Java 类 Holiday 的定义，包含 id、holidayName、beginDate、endDate、num 字段。
画面7: 展示了 Java 类 Holiday 的定义，增加了 reason、type 字段，并添加了 Serializable 接口。
画面8: 展示了 BPMN 流程图，与画面1类似，但“请假单审批”任务节点被选中。
画面9: 展示了 BPMN 流程图，与画面1类似，但“请假单审批”任务节点被选中。
画面10: 展示了“Save as image”对话框，用于保存流程图图片。
画面11: 展示了“Copy”对话框，用于将流程图图片复制到项目资源目录。
画面12: PPT 页面展示 Java 代码，用于启动流程并设置变量，变量名为“num”，值为 holiday.getNum()。
画面13: 展示了 Java 类 Holiday 的定义，包含 id、holidayName、beginDate、endDate、num、reason、type 字段，并添加了 Serializable 接口。
画面14: PPT 页面展示 Java 代码，用于启动流程并设置变量，变量名为“num”，值为 holiday.getNum()。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3代码：
```java
Holiday holiday = new Holiday();
holiday.setNum(3);
// 定义流程变量
Map<String, Object> variables = new HashMap<String, Object>();
// 变量名是num，变量值是holiday.getNum()，变量名也可以是一个对象
variables.put("num", holiday.getNum());

RuntimeService runtimeService = processEngine.getRuntimeService();
ProcessInstance processInstance = runtimeService
    .startProcessInstanceByKey(processDefinitionKey, variables);

System.out.println("流程实例Id:" + processInstance.getProcessInstanceId());
```

画面4代码：
```java
@Test
public void completTask() {
    //任务id
    String taskId = "";
    TaskService taskService = processEngine.getTaskService();
    Holiday holiday = new Holiday();
    holiday.setNum(4);
    // 定义流程变量
    Map<String, Object> variables = new HashMap<String, Object>();
```

画面6代码：
```java
package com.ithema.day04;

import java.util.Date;

/**
 * 情况没说清
 */
public class Holiday {
    private Integer id;
    private String holidayName;//申请人名字
    private Date beginDate;//开始日期
    private Date endDate;//结束日期
    private Float num;//请假天数
    private String reason;//事由
    private String type;//请假类型
}
```

画面7代码：
```java
package com.ithema.day04;

import java.io.Serializable;
import java.util.Date;

/**
 * 情况没说清
 */
public class Holiday implements Serializable {
    private Integer id;
    private String holidayName;//申请人名字
    private Date beginDate;//开始日期
    private Date endDate;//结束日期
    private Float num;//请假天数
    private String reason;//事由
    private String type;//请假类型
}
```

画面13代码：
```java
package com.ithema.day04;

import java.io.Serializable;
import java.util.Date;

/**
 * 情况没说清
 */
public class Holiday implements Serializable {
    private Integer id;
    private String holidayName;//申请人名字
    private Date beginDate;//开始日期
    private Date endDate;//结束日期
    private Float num;//请假天数
    private String reason;//事由
    private String type;//请假类型

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getHolidayName() {
        return holidayName;
    }

    public void setHolidayName(String holidayName) {
        this.holidayName = holidayName;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2: PPT 标题“3.5.3 设置 global 流程变量”，子标题“3.5.3.1 启动流程时设置”，内容说明启动流程时设置流程变量，变量值为请假单信息，作用域为整个流程实例。
画面4: PPT 标题“3.5.3.2 任务办理时设置”，内容说明在完成任务时设置流程变量，变量作用域为整个流程实例。
画面12: PPT 页面展示 Java 代码，用于启动流程并设置变量，变量名为“num”，值为 holiday.getNum()。
画面14: PPT 页面展示 Java 代码，用于启动流程并设置变量，变量名为“num”，值为 holiday.getNum()。

5) 不要评价画面美观，不要输出与课程无关的内容。
