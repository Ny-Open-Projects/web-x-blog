# 画面线理解：08-Activiti历史信息的查询

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\08-Activiti历史信息的查询_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 01:06, 02:01, 02:33, 03:16, 04:12, 05:46, 06:35, 07:27, 08:12, 08:34, 09:35, 10:23, 10:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:40:58

1) 这一组画面整体在讲如何通过 Java 代码查询 Activiti 工作流的历史实例数据，并在 MySQL 数据库中验证结果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 MySQL GUI 工具中查询到的 activiti 历史表数据，包含流程实例ID、执行ID、任务ID、活动名称等字段。
画面2：在 MySQL GUI 工具中，用户点击“刷新”按钮，重新加载数据。
画面3：切换到 IntelliJ IDEA 开发环境，显示项目结构和主界面。
画面4：在 IntelliJ IDEA 中打开 HistoryQuery.java 文件，代码中初始化 ProcessEngine 对象。
画面5：在 IntelliJ IDEA 中，代码光标位于 HistoryService 的声明处，准备获取历史服务。
画面6：在 IntelliJ IDEA 中，代码光标位于创建历史活动实例查询对象处。
画面7：在 MySQL GUI 工具中，用户点击“刷新”按钮，重新加载数据。
画面8：在 IntelliJ IDEA 中，代码光标位于创建历史活动实例查询对象处，准备执行查询。
画面9：在 IntelliJ IDEA 中，代码光标位于 for 循环中，准备打印历史活动实例的详细信息。
画面10：在 IntelliJ IDEA 中，右键点击代码，弹出“Copy Reference”菜单，准备复制方法或类。
画面11：在 IntelliJ IDEA 中，运行 HistoryQuery.java，终端输出历史活动实例的详细信息。
画面12：在 IntelliJ IDEA 中，代码光标位于设置流程实例ID处，准备执行查询。
画面13：在 IntelliJ IDEA 中，代码光标位于 for 循环中，准备打印历史活动实例的详细信息。
画面14：在 MySQL GUI 工具中，用户点击“刷新”按钮，重新加载数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```java
package com.ithema.day03.activiti;

import ...

public class HistoryQuery {

    public static void main(String[] args) throws IOException {
        //1.博学谷流程引擎对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.博学谷历史服务
        HistoryService historyService = processEngine.getHistoryService();
        //3.博学谷历史实例查询对象
        HistoricActivityInstanceQuery historicActivityInstanceQuery = historyService.createHistoricActivityInstanceQuery();
        //4.执行查询
        List<HistoricActivityInstance> list = historicActivityInstanceQuery.list();
        //5.遍历查询结果
        for (HistoricActivityInstance instance : list) {
            System.out.println(instance.getActivityId());
            System.out.println(instance.getProcessDefinitionId());
            System.out.println(instance.getProcessInstanceId());
            System.out.println("==================");
        }
    }
}
```

画面6：
```java
//3.博学谷历史实例查询对象
HistoricActivityInstanceQuery historicActivityInstanceQuery = historyService.createHistoricActivityInstanceQuery();
//4.执行查询
List<HistoricActivityInstance> list = historicActivityInstanceQuery.list();
//5.遍历查询结果
for (HistoricActivityInstance instance : list) {
    System.out.println(instance.getActivityId());
    System.out.println(instance.getProcessDefinitionId());
    System.out.println(instance.getProcessInstanceId());
    System.out.println("==================");
}
```

画面11：
```java
2018-10-29 11:09:24,510 2516 [main] DEBUG wpl.interceptor.LogInterceptor - 
StartEvent
holiday114
2501

审批任务
holiday114
2501

结束任务
holiday114
2501
```

画面12：
```java
//4.执行查询
List<HistoricActivityInstance> list = historicActivityInstanceQuery.processInstanceId("2501");//设置流程实例的id
//5.遍历查询结果
for (HistoricActivityInstance instance : list) {
    System.out.println(instance.getActivityId());
    System.out.println(instance.getProcessDefinitionId());
    System.out.println(instance.getProcessInstanceId());
    System.out.println("==================");
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
