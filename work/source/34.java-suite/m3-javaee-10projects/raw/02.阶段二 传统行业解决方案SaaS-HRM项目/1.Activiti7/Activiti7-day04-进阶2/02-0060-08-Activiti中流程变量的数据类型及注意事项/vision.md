# 画面线理解：08-Activiti中流程变量的数据类型及注意事项

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\08-Activiti中流程变量的数据类型及注意事项_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:35, 00:36, 00:40, 00:44, 00:51, 01:08, 01:22, 01:28, 01:42, 02:13, 02:34, 03:09, 03:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:57:58

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中流程变量的类型和作用域。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示一个流程图，包含“开始”、“请假流程审批”、“判断”、“出差审批”、“结束”等节点，旁边有红色文字注释“流程运行过程中，加入流程变量 holidayNum 5”。
画面 2: 显示 PPT 页面，标题为“3.2 流程变量类型”，下方是“Table 15.9. Variable Types”，列出了变量类型（Type name）和描述（Description）。
画面 3: PPT 页面，标题“3.2 流程变量类型”，表格内容与画面 2 相同。
画面 4: PPT 页面，标题“3.2 流程变量类型”，表格内容与画面 2 相同。
画面 5: PPT 页面，标题“3.2 流程变量类型”，表格内容与画面 2 相同，下方出现注释“注意：如果将 pojo 存储到流程变量中，必须实现序列化接口 serializable，为了防止由于新增字段无法反序列化，需要生成 serialVersionUID。”
画面 6: PPT 页面，标题“3.2 流程变量类型”，表格内容与画面 2 相同，下方注释与画面 5 相同。
画面 7: PPT 页面，标题“3.3 流程变量作用域”，下方是“注意：如果将 pojo 存储到流程变量中，必须实现序列化接口 serializable，为了防止由于新增字段无法反序列化，需要生成 serialVersionUID。”
画面 8: PPT 页面，标题“3.3 流程变量作用域”，下方注释与画面 7 相同。
画面 9: 展示一个流程图，与画面 1 相同，包含“开始”、“请假流程审批”、“判断”、“出差审批”、“结束”等节点，旁边有红色文字注释“流程运行过程中，加入流程变量 holidayNum 5”。
画面 10: 展示一个流程图，与画面 1 相同，但“出差审批”节点右侧出现一个虚线框，框内有“<8”字样。
画面 11: PPT 页面，标题“3.3 流程变量作用域”，下方文字说明：“流程变量的作用域默认是一个流程实例(processInstance)，也可以是一个任务(task)或一个执行实例(execution)。这三个作用域流程实例的范围最大，可以称为 global 变量；任务和执行实例仅仅是针对一个任务和一个执行实例范围，范围没有流程实例大，称为 local 变量。”
画面 12: PPT 页面，标题“3.3 流程变量作用域”，下方文字说明与画面 11 相同。
画面 13: PPT 页面，标题“3.3 流程变量作用域”，下方文字说明与画面 11 相同。
画面 14: PPT 页面，标题“3.2 流程变量类型”，表格内容与画面 2 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
PPT 标题：
- 画面 2、3、4、6、7、8、11、12、13、14：标题为“3.2 流程变量类型”或“3.3 流程变量作用域”。
表格数据：
- 画面 2、3、4、5、6、7、8、11、12、13、14：表格标题为“Table 15.9. Variable Types”，内容如下：
  Type name | Description
  string | Value is threaded as a java.lang.String Raw JSON-1
  integer | Value is threaded as a java.lang.Integer. When writing text.
  short | Value is threaded as a java.lang.Short. When writing text.
  long | Value is threaded as a java.lang.Long. When writing text.
  double | Value is threaded as a java.lang.Double. When writing text.
  boolean | Value is threaded as a java.lang.Boolean. When writing text.
  date | Value is treated as a java.util.Date. When writing, the Binary variable, threaded as an array of bytes. The value stream.
  binary | Serialized representation of a Serializable Java-object serializable URL pointing to the raw binary stream. All serializable variable of this type.
  注意：如果将 pojo 存储到流程变量中，必须实现序列化接口 serializable，为了防止由于新增字段无法反序列化，需要生成 serialVersionUID。
  画面 11、12、13：下方文字说明：“流程变量的作用域默认是一个流程实例(processInstance)，也可以是一个任务(task)或一个执行实例(execution)。这三个作用域流程实例的范围最大，可以称为 global 变量；任务和执行实例仅仅是针对一个任务和一个执行实例范围，范围没有流程实例大，称为 local 变量。”

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
