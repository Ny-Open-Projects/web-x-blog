# 画面线理解：02-Activiti系统体系架构图

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\02-Activiti系统体系架构图_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:16, 00:40, 00:50, 01:32, 01:53, 01:58, 02:09, 02:27, 02:58, 04:38, 04:52, 05:35, 05:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:18:40

1) 这一组画面整体在讲如何通过 Java 代码获取 Activiti 流程引擎的各个服务对象，并通过数据库查询验证其对应的表结构。

2) 按时间顺序列出每张画面的要点：
画面1：在 MySQL Workbench 中，选中 act_hi_procinst 表，查询语句为 "1"，显示了该表的字段结构。
画面2：在 IDEA 中，展示 ActivitiTest.java 文件，代码用于创建 ProcessEngineConfiguration 并构建 ProcessEngine 对象。
画面3：IDEA 中，代码高亮显示创建 ProcessEngineConfiguration 的部分，注释说明了配置文件路径。
画面4：PPT 展示了 Activiti 的架构图，ProcessEngineConfiguration 指向 activiti.cfg.xml，ProcessEngine 指向 RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService。
画面5：IDEA 中，代码高亮显示 ProcessEngine 对象的创建部分。
画面6：IDEA 中，通过 ProcessEngine 对象调用 getDynamicBpmnService() 方法，弹出方法列表。
画面7：IDEA 中，光标在 ProcessEngine 对象后，准备调用方法。
画面8：IDEA 中，弹出方法列表，选中 getHistoryService() 方法。
画面9：IDEA 中，光标在 getHistoryService() 方法后，准备调用。
画面10：IDEA 中，代码高亮显示 processEngine.getHistoryService() 方法调用。
画面11：IDEA 中，代码高亮显示 HistoryService historyService = processEngine.getHistoryService(); 的完整语句。
画面12：在 MySQL Workbench 中，选中 act_hi_procinst 表，查询语句为 "domain---dao---service"，显示了该表的字段结构。
画面13：PPT 展示了 Activiti 的架构图，ProcessEngineConfiguration 指向 activiti.cfg.xml，ProcessEngine 指向 RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService。
画面14：在 MySQL Workbench 中，选中 act_hi_procinst 表，查询语句为 "domain---dao---service"，显示了该表的字段结构。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2代码：
```java
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngineConfiguration;
import org.junit.Test;

//测试类
//作用：测试Activiti引擎需要的25张表的生成
public class ActivitiTest {

@Test
public void testGenTable(){
    //1.创建ProcessEngineConfiguration对象  第一个参数：配置文件名称  第二个参数是processEngineConfiguration的
    ProcessEngineConfiguration configuration = ProcessEngineConfiguration
            .createProcessEngineConfigurationFromResource("activiti.cfg.xml", beanName: "process"
    //2.创建ProcessEngine对象
    ProcessEngine processEngine = configuration.buildProcessEngine();
    //3.输出processEngine对象
    System.out.println(processEngine);
}
}
```

画面6代码：
```java
public void testGenTable(){
    //1.创建ProcessEngineConfiguration对象  第一个参数：配置文件名称  第二个参数是processEngineConfiguration的
    ProcessEngineConfiguration configuration = ProcessEngineConfiguration
            .createProcessEngineConfigurationFromResource("activiti.cfg.xml", beanName: "process"
    //2.创建ProcessEngine对象
    ProcessEngine processEngine = configuration.buildProcessEngine();
    //3.输出processEngine对象
    System.out.println(processEngine);
}
```

画面11代码：
```java
HistoryService historyService = processEngine.getHistoryService();
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面4 PPT标题：4.1 activiti.cfg.xml
架构图结构：
- ProcessEngineConfiguration 指向 activiti.cfg.xml
- ProcessEngine 指向 RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService

画面13 PPT标题：4.1 activiti.cfg.xml
架构图结构：
- ProcessEngineConfiguration 指向 activiti.cfg.xml
- ProcessEngine 指向 RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService

5) 无。
