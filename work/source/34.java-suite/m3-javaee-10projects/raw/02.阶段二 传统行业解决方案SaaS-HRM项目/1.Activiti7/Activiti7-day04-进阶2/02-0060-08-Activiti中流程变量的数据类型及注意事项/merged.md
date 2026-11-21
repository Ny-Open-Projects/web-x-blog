# 08-Activiti中流程变量的数据类型及注意事项

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\08-Activiti中流程变量的数据类型及注意事项_【海量资源尽在 ubkz.com】.mp4
- 时长 3分15秒（音频 196s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面我们就一起进一步来学习我们的这个流程变量的类型刚刚呢,我们在这个图中给各位分析了我们的这个流程变量存在在很多这个流程在实现我们的这个峰值结构的时候呢那我们的流程变量存在其实是很有必要的,对吧那我们的流程变量既然很有必要存在那这个变量既然就
[00:26] 既然涉及到流程变量它也是变量既然涉及到变量我们就会有我们变量的数据类型现在我们可以一起给各位来看一下我们流程变量的数据类型有哪些各位可以看到我们这边所支持的数据类型包括像我们的实践Integer Short Long和我们Double GooglingDataBinary以及CelRez
[00:55] Sale Rezible注意这个部分也是告诉我们将来如果我们要存对象的话那我们的这个对象就需要去实现我们的这个Sale Rezible接口这样我们就可以将一个具体的对象直接给它存入到我们的这个流程变量中去各位关于我们的这个流程变量这个部分对于我们而言其实呢并没有太多的难度对吧这个地方主要就是要注意一点
[01:24] 就是我们的这个变量将来在设置的时候就说如果我将来有一个变量需要在需要设置到我们的这个流程运行的过程中去啊那我们对应的这个变量呢将来如果是一个对象的话那这个对象我们在写它的时候各位啊这个地方就有一个很重要的条件了对吧那我们比如说我这个时候有个publicpublic class
[01:51] 比如说我这个时候有一个叫做叫做holiday这样的一个对象那注意啊按照我们刚才给各位讲的啊我们的这个对象就需要去实现一个叫做serizable对吧就需要去实现一个实现一个我们的这个serizableserizableserizable对吧就需要去实现一个这样的接口啊这一点呢是各位要注意的这一点各位要注意一下啊
[02:31] 我们要去实现的是cell right这部接口否则的话你将来放一个对象的话它应该就会给各位抛出异常这个后面呢我们在测试的时候也可以给各位演示出演示出相关的这个效果吧然后呢这样做主要的目标就是让我们的这个POJO的这个对象就可以做到序列化对不对实现这个序列化接口我们实现序列化接口之后我们将来呢
[03:01] 最好要去把它的这个叫Serializable Version UID你可以生成一下对吧这一点呢我们把这个数据类型这个部分就给各位简单介绍了一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

