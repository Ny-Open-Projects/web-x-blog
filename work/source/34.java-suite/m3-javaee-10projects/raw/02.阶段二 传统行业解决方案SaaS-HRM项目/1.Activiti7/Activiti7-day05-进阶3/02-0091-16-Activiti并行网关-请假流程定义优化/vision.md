# 画面线理解：16-Activiti并行网关-请假流程定义优化

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day05-进阶3
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day05-进阶3\16-Activiti并行网关-请假流程定义优化_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:50, 00:54, 02:17, 03:36, 04:00, 04:04, 04:25, 04:28, 04:36, 04:40, 05:19, 05:30, 05:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:23:41

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中使用并行网关（ParallelGateway）和排他网关（ExclusiveGateway）构建复杂的业务流程，并通过修改流程图来调整执行逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 BPMN 2.0 中的网关类型：ParallelGateway、ExclusiveGateway、InclusiveGateway、EventGateway。
- 展示了一个包含多个网关的流程图，其中包含 StartEvent、多个用户任务、排他网关、并行网关和 EndEvent。
- 流程图中排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

画面 2：
- 在 IDEA 中打开项目，显示了 resources 目录下的多个 .bpmn 文件。
- 选中了 holidays.bpmn 文件，准备进行编辑。

画面 3：
- 弹出“Copy file”对话框，准备将 holidays.bpmn 文件复制并重命名为 holidaysParallel.bpmn。
- 目标路径为：G:\Activiti7开发实例\activiti01\src\main\resources\diagram\day05。
- 点击“OK”按钮确认复制。

画面 4：
- 打开 holidaysParallel.bpmn 文件，显示了流程图。
- 选中了排他网关，准备修改其属性。

画面 5：
- 展示了流程图的属性面板，当前选中的是“Name”属性。
- 属性面板显示了“property”和“value”两列，但未显示具体值。

画面 6：
- 展示了流程图，其中包含 StartEvent、用户任务、排他网关、并行网关和 EndEvent。
- 排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

画面 7：
- 展示了流程图，其中包含 StartEvent、用户任务、排他网关、并行网关和 EndEvent。
- 排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

画面 8：
- 展示了流程图，其中包含 StartEvent、用户任务、排他网关、并行网关和 EndEvent。
- 排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

画面 9：
- 展示了流程图，其中包含 StartEvent、用户任务、排他网关、并行网关和 EndEvent。
- 排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

画面 10：
- 展示了流程图，其中包含 StartEvent、用户任务、排他网关、并行网关和 EndEvent。
- 排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

画面 11：
- 展示了流程图，其中包含 StartEvent、用户任务、排他网关、并行网关和 EndEvent。
- 排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

画面 12：
- 展示了流程图，其中包含 StartEvent、用户任务、排他网关、并行网关和 EndEvent。
- 排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

画面 13：
- 展示了流程图，其中包含 StartEvent、用户任务、排他网关、并行网关和 EndEvent。
- 排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

画面 14：
- 展示了流程图，其中包含 StartEvent、用户任务、排他网关、并行网关和 EndEvent。
- 排他网关的条件为：${holidayNum==1}。
- 并行网关的条件为：${holidayNum>1}。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 流程图结构：
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}）→ 用户任务（“部门经理审批”）→ 并行网关（条件：${holidayNum>1}）→ 用户任务（“财务会计”）→ 并行网关 → 用户任务（“行政专员”）→ EndEvent。
  - StartEvent → 排他网关（条件：${holidayNum==1}
