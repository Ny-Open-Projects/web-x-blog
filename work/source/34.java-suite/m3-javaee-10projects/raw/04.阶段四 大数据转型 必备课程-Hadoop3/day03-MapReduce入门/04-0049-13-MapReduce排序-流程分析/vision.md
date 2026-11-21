# 画面线理解：13-MapReduce排序-流程分析

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\13-MapReduce排序-流程分析【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:09, 00:33, 00:42, 05:06, 09:24, 09:28, 09:49, 13:13, 15:13, 15:18, 15:53, 15:57, 16:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:05:34

1) 这一组画面整体在讲什么（一句话）：
讲解 Hadoop MapReduce 中自定义序列化和排序的实现方法，通过自定义 Key 类实现按字典序和数值升序排序。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前章节为“6. MapReduce序列化和排序”，并介绍 Java 序列化和 Hadoop Writable 接口。
画面 2: 展示数据格式，要求按第一列字典序、第二列数值升序排序。
画面 3: 展示数据格式，要求按第一列字典序、第二列数值升序排序。
画面 4: 展示绘图软件界面，准备绘制流程图。
画面 5: 绘制 MapReduce 流程图，展示源文件经 TextInputFormat 读取后，Map 阶段将 K1 和 V1 转换为 K2 和 V2。
画面 6: 展示数据格式，要求按第一列字典序、第二列数值升序排序。
画面 7: 绘制 MapReduce 流程图，展示 Shuffle 阶段的“分区、排序、规约、分组”过程。
画面 8: 展示数据格式，要求按第一列字典序、第二列数值升序排序。
画面 9: 绘制 MapReduce 流程图，展示 Shuffle 阶段的“分区、排序、规约、分组”过程，并添加“自定义排序规则”代码片段。
画面 10: 绘制 MapReduce 流程图，展示 Reduce 阶段将 K2 和 V2 转换为 K3 和 V3。
画面 11: 绘制 MapReduce 流程图，展示 Reduce 阶段将 K2 和 V2 转换为 K3 和 V3。
画面 12: 绘制 MapReduce 流程图，展示 Reduce 阶段将 K2 和 V2 转换为 K3 和 V3，并添加 TextOutputFormat 输出到文件。
画面 13: 绘制 MapReduce 流程图，展示 Shuffle 阶段的“分区、排序、规约、分组”过程，并添加“自定义排序规则”代码片段。
画面 14: 绘制 MapReduce 流程图，展示 Shuffle 阶段的“分区、排序、规约、分组”过程，并添加“自定义排序规则”代码片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 9:
```
自定义排序规则:
class PairWritable implement WritableComparable {
String first;
int second;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5:
- 源文件 → TextInputFormat → K1 V1 → Map阶段 → K2 V2
- Map阶段内容: “1.自定义Map逻辑，将K1和V1转为K2和V2”

画面 7:
- 源文件 → TextInputFormat → K1 V1 → Map阶段 → K2 V2 → Shuffle阶段 → 分区 排序 规约 分组

画面 9:
- Shuffle阶段 → 新 K2 V2 → Reduce阶段 → K3 V3
- Shuffle阶段内容: “分区 排序 规约 分组”
- 新 K2 V2 内容: “a 1 <a 1>”、“a 5 <a 5>”、“a 9 <a 9>”、“b 3 <b 3>”、“b 8 <b 8>”、“b 10 <b 10>”
- Reduce阶段内容: “1.自定义Reduce逻辑，将新K2和V2转为K3和V3”

画面 10:
- Map阶段 → K2 V2 → Reduce阶段 → K3 V3
- Reduce阶段内容: “1.自定义Reduce逻辑，将新K2和V2转为K3和V3”

画面 12:
- Map阶段 → K2 V2 → Reduce阶段 → K3 V3 → TextOutputFormat → 文件
- Reduce阶段内容: “1.自定义Reduce逻辑，将新K2和V2转为K3和V3”

画面 13:
- 源文件 → TextInputFormat → K1 V1 → Map阶段 → K2 V2 → Shuffle阶段 → 分区 排序 规约 分组 → 新 K2 V2 → Reduce阶段 → K3 V3
- Shuffle阶段内容: “分区 排序 规约 分组”
- 新 K2 V2 内容: “a 1 <a 1>”、“a 5 <a 5>”、“a 9 <a 9>”、“b 3 <b 3>”、“b 8 <b 8>”、“b 10 <b 10>”
- Reduce阶段内容: “1.自定义Reduce逻辑，将新K2和V2转为K3和V3”

画面 14:
- 源文件 → TextInputFormat → K1 V1 → Map阶段 → K2 V2 → Shuffle阶段 → 分区 排序 规约 分组 → 新 K2 V2 → Reduce阶段 → K3 V3
- Shuffle阶段内容: “分区 排序 规约 分组”
- 新 K2 V2 内容: “a 1 <a 1>”、“a 5 <a 5>”、“a 9 <a 9>”、“b 3 <b 3>”、“b 8 <b 8>”、“b 10 <b 10>”
- Reduce阶段内容: “1.自定义Reduce逻辑，将新K2和V2转为K3和V3”
