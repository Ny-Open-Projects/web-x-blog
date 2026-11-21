# 25.Spark任务调度之流程说明

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\25.Spark任务调度之流程说明_【海量资源尽在 666java.com】.mp4
- 时长 2分0秒（音频 121s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下任务的一个调度的一个流程那么就是我们所提交我们的应用之后它是如何去做执行的呢其实就是下面的这个图那么首先可以看到在这个图中呢这个是我们的一些RDD Objects那么就是我们所写的一些这种代码然后呢我们去通过我们的RDD呢会生成一个有象无环图DAG
[00:28] 然后我们会通过一个DAG的scandals然后对我们DAG去做一个解析它按照什么按照我们的一些依赖关系去做一个stage的划分那么它所划分的规则就是前面我们所说到的规则那么如果遇到散依赖就放到一个stage中那么如果遇到宽依赖就形成一个新的stage
[00:55] 那么可以看到下面这个描述是不是就是这一部分对吧那么可以看到遇到窄一栏那么就加入到本的state那么如果遇到宽一栏就进行什么state的一个切分那么就完成了一个state划分然后我们这个DAG的一个scanner它会对每一个这个state去生成一个什么task的一个set就是我们的一个任务列表
[01:21] 然后将 task set 去交给谁有一个叫做 task stag做一个什么去做一个调度做一个调度那么我们 task skewder它就具体去针对于我们的每一个任务去做一个任务的一个调度执行然后把这个任务去落到最后我们 worker 节点上面去做一个执行那么这个其实就是前面我们所说的
[01:50] 真正干活的其实就是我们的work这样的一个节点ok好那么关于我们任务的调度流程我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Spark 任务调度流程，重点解释 DAGScheduler 和 TaskScheduler 如何协作将 RDD 的操作图划分为 Stage 并提交任务。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了“6.4.3. 任务调度流程”的架构图，图中包含 RDD Objects、DAGScheduler、TaskScheduler、Worker 四个主要组件，以及它们之间的数据流和功能描述。
画面 2: 在“RDD Objects”部分添加了红色矩形框，强调其在流程中的起点作用。
画面 3: 与画面 2 相同，红色矩形框依然存在。
画面 4: 在“RDD Objects”部分的红色矩形框上添加了红色箭头，指向 DAG。
画面 5: 与画面 4 相同，红色箭头依然存在。
画面 6: 移除了“RDD Objects”部分的红色矩形框和红色箭头，画面恢复到初始状态。
画面 7: 在“说明”部分的第二条文字中，“遇到窄依赖”被红色下划线标出，强调其在 Stage 划分中的作用。
画面 8: 与画面 7 相同，红色下划线依然存在。
画面 9: 移除了“说明”部分的红色下划线，画面恢复到初始状态。
画面 10: 在“TaskScheduler”部分添加了红色横线，强调其在调度流程中的作用。
画面 11: 在“TaskScheduler”部分的红色横线下方添加了红色圆圈，圈住“Task”。
画面 12: 在“Worker”部分添加了红色圆圈，圈住“Worker”。
画面 13: 移除了“TaskScheduler”和“Worker”部分的红色标记，画面恢复到初始状态。
画面 14: 与画面 13 相同，没有红色标记。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
PPT 标题：6.4.3. 任务调度流程
架构图结构：
- RDD Objects → DAG
- DAG → DAGScheduler
- DAGScheduler → TaskScheduler
- TaskScheduler → Worker
- Worker → Task
- Task → Threads / Block manager
- TaskScheduler 与 Worker 之间通过 Cluster manager 交互。
- DAGScheduler 与 TaskScheduler 之间通过 TaskSet 交互。
- TaskScheduler 与 Worker 之间通过 Cluster manager 交互。
表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

