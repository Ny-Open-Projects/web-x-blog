# 画面线理解：05-监听器方式实现Activiti的流程assignee设置

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\05-监听器方式实现Activiti的流程assignee设置_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:05, 01:19, 01:23, 02:32, 02:36, 03:01, 03:38, 03:52, 04:06, 04:23, 05:08, 05:23, 05:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:56:20

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中任务监听器（Task Listener）的配置与实现，包括事件类型、代码示例及注意事项。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 Activiti 任务监听器配置界面，说明监听器在任务相关事件触发时执行自定义 Java 逻辑或表达式。
- 任务相关事件包括：Create（任务创建后触发）、Assignment（任务分配后触发）、Delete（任务完成后触发）、All（所有事件发生都触发）。
- 说明 Java 逻辑或表达式参考 UEL 表达式，主要介绍监听类使用。

画面2：
- 与画面1内容相同，为同一幻灯片的延续展示。

画面3：
- 展示了 IntelliJ IDEA 中项目结构，当前打开的是 holidays.bpmn 文件。
- 项目路径：src/main/resources/diagram/holiday3.bpmn。
- 底部控制台显示了 Activiti 执行日志，包括事务提交和连接信息。

画面4：
- 展示了 Activiti Designer 中的 BPMN 图，包含 StartEvent、UserTask、EndEvent。
- 任务名称为 “User Task”，流程名称为 “My process”。
- 右侧工具栏显示了可拖拽的各类任务节点。

画面5：
- 与画面1内容相同，为同一幻灯片的延续展示。

画面6：
- 展示了“黑马程序员”教学幻灯片，标题为“定义任务监听类，且类必须实现 org.activiti.engine.delegate.TaskListener 接口”。
- 代码示例：
  public class MyTaskListener implements TaskListener {
      @Override
      public void notify(DelegateTask delegateTask) {
          //这里指定任务负责人
          delegateTask.setAssignee("张三");
      }
  }

画面7：
- 与画面6内容相同，为同一幻灯片的延续展示。

画面8：
- 展示了 Activiti Designer 中的“Choose Class to Bind”对话框，用于绑定监听器类。
- 界面包含“Search by Name”和“Project”搜索框，下方有“OK”、“Cancel”、“Help”按钮。

画面9：
- 与画面6内容相同，为同一幻灯片的延续展示。

画面10：
- 与画面4内容相同，为同一 BPMN 图的延续展示。

画面11：
- 与画面6内容相同，为同一幻灯片的延续展示。

画面12：
- 与画面6内容相同，为同一幻灯片的延续展示，但幻灯片页码变为 12/48。
- 底部出现“2.2 查询任务”标题。

画面13：
- 与画面6内容相同，为同一幻灯片的延续展示。

画面14：
- 与画面6内容相同，为同一幻灯片的延续展示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6、7、9、11、13、14：
public class MyTaskListener implements TaskListener {
    @Override
    public void notify(DelegateTask delegateTask) {
        //这里指定任务负责人
        delegateTask.setAssignee("张三");
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：
- 流程图结构：
  StartEvent → User Task → EndEvent
- 节点属性：
  - Id: myprocess
  - Name: My process
  - Is Executable: ✓
  - Is Closed: ✗
  - Process Type: None
  - Candidate Starter: （空）
  - Error Definitions: （空）
  - Message Definitions: （空）
  - Signal Definitions: （空）

画面6、7、9、11、13、14：
- PPT 标题：
  定义任务监听类，且类必须实现 org.activiti.engine.delegate.TaskListener 接口
- PPT 子标题：
  2.1.3.1 注意事项
- PPT 内容：
  使用监听器分配方式，按照监听事件去执行监听类的 notify 方法，方法如果不能正常执行也会影响任务的执行。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
