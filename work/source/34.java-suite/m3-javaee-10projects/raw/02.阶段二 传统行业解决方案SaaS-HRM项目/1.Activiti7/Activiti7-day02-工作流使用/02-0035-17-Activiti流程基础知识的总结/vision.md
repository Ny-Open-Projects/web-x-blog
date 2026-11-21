# 画面线理解：17-Activiti流程基础知识的总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\17-Activiti流程基础知识的总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:20, 02:29, 02:51, 05:02, 06:49, 09:45, 11:16, 11:34, 12:19, 13:40, 14:09, 14:41, 15:16, 16:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:30:26

1) 这一组画面整体在讲如何使用 Activiti 工作流引擎，通过 Java 代码部署 BPMN 流程定义、启动流程实例、查询并完成任务。

2) 按时间顺序列出每张画面的要点：
画面1：打开一个空白的 Word 文档，准备编写说明文档。
画面2：在 IntelliJ IDEA 中打开 activiti01 项目，展示 ActivitiCompleteTask.java 文件内容，包含获取 ProcessEngine、TaskService 的代码。
画面3：在 Word 文档中输入“Activiti的架构说明”等文字，介绍 ProcessEngine、RepositoryService、RuntimeService、TaskService。
画面4：在 Word 文档中继续输入内容，同时弹出一个小型窗口，显示一个文本编辑器。
画面5：在 Activiti Designer 中展示 holiday.bpmn 流程图，包含 StartEvent → 请假申请审批 → 通知领导 → EndEvent。
画面6：在 Activiti Designer 中，对流程图进行编辑，调整“通知领导”节点的文本。
画面7：在 Activiti Designer 中，对流程图进行编辑，调整“通知领导”节点的文本。
画面8：在 IntelliJ IDEA 中展示 ActivitiDeployment.java 文件内容，包含部署流程定义的代码。
画面9：在 IntelliJ IDEA 中展示 ActivitiStartInstance.java 文件内容，包含启动流程实例的代码。
画面10：在 IntelliJ IDEA 中展示 ActivitiStartInstance.java 文件内容，包含启动流程实例的代码。
画面11：在 Word 文档中继续输入内容，列出 Activiti 的核心接口和部署流程的代码。
画面12：在 IntelliJ IDEA 中展示 ActivitiCompleteTask.java 文件内容，包含获取 TaskService、查询任务、完成任务的代码。
画面13：在 Word 文档中继续输入内容，列出 Activiti 的核心接口和部署流程的代码。
画面14：在 Word 文档中继续输入内容，列出 Activiti 的核心接口和部署流程的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2：
```java
package com.ithema.activiti;

import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.task.Task;

/**
 * 处理当前用户的任务
 */
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService服务
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户的任务
        Task task = taskService.createTaskQuery()
                .processDefinitionKey("holiday")
                .singleResult();
        //4.处理任务
        taskService.complete(task.getId());
    }
}
```

画面8：
```java
public static void main(String[] args) {
    //1.获取ProcessEngine对象
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.得到RepositoryService服务
    RepositoryService repositoryService = processEngine.getRepositoryService();
    //3.读取InputStream流
    InputStream is = ActivitiDeployment.class.getClassLoader().getResourceAsStream("diagram/holiday.bpmn");
    ZipInputStream zipInputStream = new ZipInputStream(is);
    //4.部署流程定义
    Deployment deployment = repositoryService.createDeployment()
            .addInputStream("holiday.bpmn", zipInputStream)
            .name("请假申请流程")
            .deploy();
    System.out.println("部署ID：" + deployment.getId());
}
```

画面9：
```java
public class ActivitiStartInstance {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到RuntimeService服务
        RuntimeService runtimeService = processEngine.getRuntimeService();
        //3.创建流程实例
        ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
        //4.输出流程相关参数
        System.out.println("流程部署ID：" + processInstance.getDeploymentId());//null
        System.out.println("流程定义ID：" + processInstance.getProcessDefinitionId());//holiday:1:4
        System.out.println("流程实例ID：" + processInstance.getId());//2501
        System.out.println("活动ID：" + processInstance.getActivityId());//null
    }
}
```

画面12：
```java
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.task.Task;

/**
 * 处理当前用户的任务
 */
public class ActivitiCompleteTask {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到TaskService服务
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户的任务
        Task task = taskService.createTaskQuery()
                .processDefinitionKey("holiday")
                .singleResult();
        //4.处理任务
        taskService.complete(task.getId());
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面5：流程图结构：
StartEvent → 请假申请审批 → 通知领导 → EndEvent
画面6：流程图结构：
StartEvent → 请假申请审批 → 通知领导 → EndEvent
画面7：流程图结构：
StartEvent → 请假申请审批 → 通知领导 → EndEvent
画面11：PPT 内容：
1. Activiti的架构说明
   - ProcessEngineConfiguration：主要作用是加载activiti.cfg.xml配置文件
   - ProcessEngine：作用是获取RuntimeService、RepositoryService、TaskService等服务
   - RepositoryService：作用：可以完成流程定义的部署
   - RuntimeService：作用：可以启动流程实例
   - TaskService：作用：可以完成任务的查询、完成
2. BPMN流程图
   - 用 Activiti Designer 工具绘制
3. 部署流程定义
   - 方式一：多个文件（.bpmn、.png文件）
   - 方式二：单个文件（.zip文件）
   - 用 Activiti 最终是以单个文件的形式部署，用 repositoryService 进行了部署工作
   - Deployment deployment = repositoryService.createDeployment()
           .addClasspathResource("diagram/holiday.bpmn") // 添加bpmn流程
           .addClasspathResource("diagram/holiday.png") // 添加png图片
           .name("请假申请流程")
           .deploy();
4. 启动流程实例
   - RuntimeService startProcessInstanceByKey("key")
5. 查询任务
   - TaskService taskService.createTaskQuery()
6. 完成任务
   - TaskService taskService.complete(task.getId());//参数为任务ID

5) 不要评价画面美观，不要输出与课程无关的内容。
