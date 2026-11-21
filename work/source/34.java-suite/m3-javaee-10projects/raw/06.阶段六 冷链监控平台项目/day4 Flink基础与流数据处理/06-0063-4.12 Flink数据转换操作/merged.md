# 4.12 Flink数据转换操作

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.12 Flink数据转换操作_【海量资源尽在 666java.com】.mp4
- 时长 5分46秒（音频 346s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来看一看我们针对于数据的一个操作我们刚才也提到了对于我们的DataStream或DataSet这种数据来讲的话我们需要对它进行一些数据的转换操作我们来看一看我们的这张图里边假设我现在有一个DataStream那么这个DataStream呢它可以做什么样的一些操作呢那么这个DataStream首先它可以转换成一个Connected这种DataStream
[00:29] 比如说它可以用我们的connect方法它通过connect方法把转换成我们的connect streamconnected stream那么它还可以通过我们的比如说像split方法把它转换成一个split stream也就是说这个过程是由datestream的split方法进行转换的而由datestream
[01:12] 到这种connected stream是由什么方法来来转换的呢它是通过connect方法而另外一个的话是我们通过这种split stream也可以转换成det stream那么这个方法其实是split stream的这个select方法那同样的我们如果把我们的connect stream可以把它转换成一个
[01:47] 这个方法呢其实就叫做call map方法这是我们的这种转换而datastream作为初始的一个数据流或者说这样的一个数据流它可以转换成一个叫all window streamall windowwindow的stream这种转换呢是通过我们的一个window all方法
[02:30] 来实现的而实现这种反向的比如说从all window的stream可以通过什么来实现呢可以通过applyapply方法来实现这个datastream然后还有一个非常非常重要的一个一个类叫做kidkidstream也就是说我的整个的这个数据流这个数据流呢其实是我们可以把它给拆成了
[03:13] 不同的一小段一小段的而这一小段一小段的呢我其实可以对它进行一个分组而分组之后就变成了AM一个关键主键来进行分组的这样的一个数据流这个方法呢其实就叫K的K8K8方法而这个K8方法是DataStream拥有的一个方法那反向的话它可以通过Reduce把我们的一个K的Stream
[03:48] 转换成一个data streamreduce那同样道理还有一个另外一个比较重要的就是叫做window的streamwindow的stream这个window的stream呢和all window的stream实际上比较类似那么它的是通过它是通过我们的叫做一个window方法把一个k的stream给它转换过来的window方法转换过来的而
[04:26] 针对于我们的window的方法我们可以转换成我们的datastream这个datastream就是用也是用apply方法来对它进行转换的我们可以简单的看一下整体的看一下那么我们的一个数据流比如说一个datastream那么它通过datastream的各个方法比如说像connect方法或者split方法或者是windowall方法或者kby方法
[04:59] 可以转换成另外类型的这种数据流而另外类型的数据流呢也可以把也可以从其他的数据流比如说像K的Stream那像我们的DataStream或者Windows的Stream进行一个转换这个呢其实就是我们对于数据流的一个转换操作比如我们看一下我们这个这个这个这个图这个图也比较形象的来
[05:23] 给它展示了就是刚才我们说的这个过程当然了还有一个就是我们的DataStream就是数据流可以通过Map方法转化成另外一个DataStream这些DataStream呢提供了这种转换操作那么基本可以满足所有的这种日常的一些使用场景这是我们对于数据的一些操作转换的一个讲解

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Flink 流处理中的数据流操作与转换关系，通过手绘流程图逐步构建核心概念模型，并最终展示官方文档中的标准架构图。

2) 按时间顺序列出每张画面的要点：
画面 1: 空白画布，准备开始绘制。
画面 2: 绘制第一个节点“DataStream”，并用箭头指向一个矩形框，框内有“0”、“1”等占位符，表示数据流的初始状态。
画面 3: 将目标框重命名为“ConnectedStream”，并添加一个下方的“SplitStream”节点。
画面 4: 从“DataStream”节点引出一条带“split”标签的向下箭头指向“SplitStream”节点。
画面 5: 从“ConnectedStream”节点引出一条带“connect”标签的向左箭头，指向“SplitStream”节点。
画面 6: 在“DataStream”节点上方添加一个带“coMap”标签的向左箭头。
画面 7: 在“DataStream”节点左侧添加一个“AllWindowsStream”节点，并用带“select”标签的箭头指向“SplitStream”节点。
画面 8: 从“AllWindowsStream”节点引出两条带“apply”和“windowAll”标签的箭头指向“DataStream”节点。
画面 9: 在“DataStream”节点上方添加一个“KeyedStream”节点，并用带“keyBy”标签的向上箭头指向“DataStream”节点。
画面 10: 在“KeyedStream”节点右侧添加一个带“reduce”标签的向下箭头。
画面 11: 在“KeyedStream”节点上方添加一个“WindowedStream”节点，并用带“window”标签的向左箭头指向“KeyedStream”节点。
画面 12: 在“WindowedStream”节点下方添加一个带“apply”标签的向左箭头指向“DataStream”节点。
画面 13: 在“DataStream”节点左侧添加一个“KeyedStream”节点，并用带“keyBy”标签的向上箭头指向“DataStream”节点。
画面 14: 展示官方文档中的标准架构图，包含“DataStream”、“ConnectedStream”、“SplitStream”、“AllWindowsStream”、“KeyedStream”、“WindowedStream”等节点，以及“apply”、“windowAll”、“select”、“keyBy”、“reduce”、“coMap”、“connect”等操作标签。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
PPT 标题：3.3 数据的操作
架构图结构：
- “DataStream”节点：
  - 向上通过“keyBy”指向“KeyedStream”。
  - 向右通过“connect”指向“ConnectedStream”。
  - 向下通过“split”指向“SplitStream”。
  - 向左通过“apply”指向“AllWindowsStream”。
  - 向左通过“windowAll”指向“AllWindowsStream”。
- “KeyedStream”节点：
  - 向下通过“reduce”指向“ConnectedStream”。
  - 向左通过“window”指向“WindowedStream”。
- “AllWindowsStream”节点：
  - 向右通过“apply”指向“DataStream”。
  - 向右通过“windowAll”指向“DataStream”。
- “ConnectedStream”节点：
  - 向左通过“coMap”指向“DataStream”。
- “SplitStream”节点：
  - 向上通过“select”指向“AllWindowsStream”。
- “WindowedStream”节点：
  - 向左通过“apply”指向“DataStream”。
  - 向左通过“keyBy”指向“DataStream”。

5) 无。

