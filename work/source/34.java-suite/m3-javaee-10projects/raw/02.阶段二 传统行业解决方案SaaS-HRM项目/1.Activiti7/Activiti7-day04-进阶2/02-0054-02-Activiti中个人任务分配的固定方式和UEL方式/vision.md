# 画面线理解：02-Activiti中个人任务分配的固定方式和UEL方式

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\02-Activiti中个人任务分配的固定方式和UEL方式_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:22, 01:40, 01:54, 02:05, 02:34, 04:30, 05:23, 05:30, 05:34, 05:42, 06:10, 06:16, 06:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:54:11

1) 这一组画面整体在讲 Activiti 工作流中任务分配的两种方式：固定分配和表达式分配（UEl），并演示了如何在 BPMN 图中配置。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PPT 页面“2.1.1 固定分配”，图中 BPMN 流程图包含 StartEvent → 用户任务 → 用户任务 → EndEvent，左侧 properties 窗口显示 Assignee 属性值为 "lisi"，并用红色框高亮。
画面2: 展示 IntelliJ IDEA 中的 BPMN 图编辑界面，流程图与画面1相同，右侧为 BPMN 元素面板。
画面3: 与画面1内容相同，PPT 页面“2.1.1 固定分配”，Assignee 属性值为 "lisi" 被高亮。
画面4: PPT 页面“2.1.1.1 注意事项”，文字说明“在 properties 视图中，填写 Assignee 项为任务负责人”，下方显示“2.1.1.1 注意事项”标题。
画面5: PPT 页面“2.1.1.1 注意事项”后切换至“2.1.2 表达式分配”，并进入子标题“2.1.2.1 UEL 表达式”，页面底部有“黑马程序员”和地址电话信息。
画面6: PPT 页面“2.1.2.1 UEL 表达式”，内容为“Activiti 使用 UEL 表达式，UEL 是 java EE6 规范的一部分，UEL（Unified Expression Language）即”，下方有“黑马程序员”和地址电话信息。
画面7: 展示 IntelliJ IDEA 中的 BPMN 图编辑界面，流程图与画面1相同，右侧为 BPMN 元素面板。
画面8: PPT 页面“2.1.2.1 UEL 表达式”，内容为“统一表达式语言，activiti 支持两个 UEL 表达式：UEL-value 和 UEL-method”，并列出“UEL-value 定义如下：”，下方有“黑马程序员”和地址电话信息。
画面9: PPT 页面“2.1.2.1 UEL 表达式”，内容为“assignee 这个变量是 activiti 的一个流程变量，成：”，下方有“黑马程序员”和地址电话信息。
画面10: PPT 页面“2.1.2.1 UEL 表达式”，内容为“user 也是 activiti 的一个流程变量，user.assignee 表示通过调用 user 的 getter 方法获取值。”，下方有“黑马程序员”和地址电话信息。
画面11: PPT 页面“2.1.2.1 UEL 表达式”，内容为“user 也是 activiti 的一个流程变量，user.assignee 表示通过调用 user 的 getter 方法获取值。”，下方有“黑马程序员”和地址电话信息。
画面12: PPT 页面“2.1.2.1 UEL 表达式”，内容为“user 也是 activiti 的一个流程变量，user.assignee 表示通过调用 user 的 getter 方法获取值。”，下方有“黑马程序员”和地址电话信息。
画面13: PPT 页面“2.1.2.1 UEL 表达式”，内容为“Assignee”属性值被设置为“${user.deptName}”，下方有“黑马程序员”和地址电话信息。
画面14: PPT 页面“2.1.2.1 UEL 表达式”，内容为“Activiti 使用 UEL 表达式，UEL 是 java EE6 规范的一部分，UEL（Unified Expression Language）即”，下方有“黑马程序员”和地址电话信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
- PPT 标题：
  - 画面1: “2.1.1 固定分配”
  - 画面4: “2.1.1.1 注意事项”
  - 画面5: “2.1.2 表达式分配”
  - 画面6: “2.1.2.1 UEL 表达式”
  - 画面8: “2.1.2.1 UEL 表达式”
  - 画面10: “2.1.2.1 UEL 表达式”
  - 画面13: “2.1.2.1 UEL 表达式”
  - 画面14: “2.1.2.1 UEL 表达式”
- 流程图结构：
  - 画面1、2、3、7、8、9、10、11、12、13: StartEvent → 用户任务 → 用户任务 → EndEvent
  - 画面6、8、14: StartEvent → 用户任务 → EndEvent
- 表格数据：
  - 画面1、3、6、8、9、10、11、12、13: properties 窗口显示：
    ```
    Id: 4
    Name: 请假申请单
    Documentation: 
    Asynchronous: 
    Exclusive: 
    Multi Instance: 
    Assignee: lisi
    Candidate Users: 
    Candidate Group: 
    Due Date: 
    Form Key: 
    Priority: 
    Task Listeners: 
    Execution Listeners: 
    Form: 
    ```
  - 画面13: properties 窗口显示：
    ```
    Id: 4
    Name: 请假申请单
    Documentation: 
    Asynchronous: 
    Exclusive: 
    Multi Instance: 
    Assignee: ${user.deptName}
    Candidate Users: 
    Candidate Group: 
    Due Date: 
    Form Key: 
    Priority: 
    Task Listeners: 
    Execution Listeners: 
    Form: 
    ```

5) 无。
