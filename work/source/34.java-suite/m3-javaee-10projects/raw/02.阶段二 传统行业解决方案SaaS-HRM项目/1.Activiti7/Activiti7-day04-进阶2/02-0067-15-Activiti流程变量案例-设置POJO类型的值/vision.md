# 画面线理解：15-Activiti流程变量案例-设置POJO类型的值

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\15-Activiti流程变量案例-设置POJO类型的值_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:35, 01:53, 02:46, 03:43, 04:30, 05:05, 06:52, 07:31, 08:28, 09:51, 10:36, 11:26, 12:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:01:41

1) 这一组画面整体在讲如何在 Activiti 工作流引擎中部署流程定义、启动流程实例并设置流程变量。

2) 按时间顺序列出每张画面的要点：
画面1：在 IDEA 中编辑 VariableTest.java，代码用于部署名为“请假流程-流程变量”的 BPMN 图文件（holiday4.bpmn）和 PNG 图片资源。
画面2：在 IDEA 中编辑 VariableTest.java，代码用于部署流程定义。
画面3：在 IDEA 中打开 BPMN 图编辑器，显示 holiday4.bpmn 流程图，包含 StartEvent、UserTask、ServiceTask、EndEvent 等节点。
画面4：在 IDEA 中编辑 VariableTest.java，代码用于启动流程实例。
画面5：在 IDEA 中编辑 VariableTest.java，代码用于启动流程实例并设置流程变量。
画面6：在 IDEA 中编辑 VariableTest.java，代码用于启动流程实例并设置流程变量。
画面7：在 IDEA 中打开 BPMN 图编辑器，显示 holiday4.bpmn 流程图，包含 StartEvent、UserTask、ServiceTask、EndEvent 等节点。
画面8：在 IDEA 中编辑 VariableTest.java，代码用于启动流程实例并设置流程变量。
画面9：在 IDEA 中编辑 VariableTest.java，代码用于启动流程实例并输出流程实例 ID。
画面10：在 MySQL Workbench 中执行 SQL 语句，删除数据库 activiti 并创建新数据库 activiti。
画面11：在 MySQL Workbench 中执行 SQL 语句，创建表 act_ge_bytearray 和 act_ru_variable。
画面12：展示 PPT 页面，标题为“3.5.2 流程程度定义”，内容为“请假天数大于等于 3 连续条件”。
画面13：在 MySQL Workbench 中执行 SQL 语句，创建表 act_ge_bytearray 和 act_ru_variable。
画面14：在 IDEA 中编辑 Holiday.java，代码定义了一个实现 Serializable 接口的 Holiday 类，包含 id、holidayName、beginDate、endDate、num、reason、type 等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//启动流程实例：同时部署流程图资源
public static void main(String[] args) {
    //1.获取ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RepositoryService对象
    RepositoryService repositoryService = processEngine.getRepositoryService();
    //3.部署
    Deployment deploy = repositoryService.createDeployment()
            .addClasspathResource("diagram/holiday4.bpmn")
            .addClasspathResource("diagram/holiday4.png")
            .name("请假流程-流程变量")
            .deploy();
    System.out.println(deploy.getId());
    System.out.println(deploy.getName());
}
```

画面4：
```java
public class VariableTest {
    public static void main(String[] args) {
        //1.获取ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key值
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
    }
}
```

画面5：
```java
public class VariableTest {
    public static void main(String[] args) {
        //1.获取ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key值
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(1);
        map.put("holiday", holiday);
    }
}
```

画面6：
```java
public class VariableTest {
    public static void main(String[] args) {
        //1.获取ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key值
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(1);
        map.put("holiday", holiday);
    }
}
```

画面7：
```java
public class VariableTest {
    public static void main(String[] args) {
        //1.获取ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key值
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(1);
        map.put("holiday", holiday);
    }
}
```

画面8：
```java
public class VariableTest {
    public static void main(String[] args) {
        //1.获取ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key值
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(1);
        map.put("holiday", holiday);
    }
}
```

画面9：
```java
public class VariableTest {
    public static void main(String[] args) {
        //1.获取ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.流程定义的key值
        String key = "myProcess_1";
        Map<String, Object> map = new HashMap<>();
        Holiday holiday = new Holiday();
        holiday.setNum(1);
        map.put("holiday", holiday);
    }
}
```

画面10：
```sql
drop database activiti;
create database activiti;
```

画面11：
```sql
create table act_ge_bytearray
```

画面12：
无代码或配置。

画面13：
```sql
create table act_ge_bytearray
```

画面14：
```java
package com.ithemo.day04;
import java.io.Serializable;
import java.util.Date;
public class Holiday implements Serializable {
    private Integer id;
    private String holidayName;//申请人的名字
    private Date beginDate;//开始日期
    private Date endDate;//结束日期
    private Float num;//请假天数
    private String reason;//事由
    private String type;
    public Integer getId() {
        return id;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面12：
PPT 标题：3.5.2 流程程度定义
PPT 内容：请假天数大于等于 3 连续条件

5) 不要评价画面美观，不要输出与课程无关的内容。
