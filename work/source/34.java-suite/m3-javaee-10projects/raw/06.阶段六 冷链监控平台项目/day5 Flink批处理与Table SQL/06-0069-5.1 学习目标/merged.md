# 5.1 学习目标

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.1 学习目标_【海量资源尽在 666java.com】.mp4
- 时长 2分14秒（音频 135s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好,今天我们学习Flink dataset和table API以及circle的一个编程那么主要包括两大部分,一部分是我们的dataset,一部分是我们的table API和circle那么我们知道数据流
[00:17] 数据的一个处理Flink是非常擅长的他擅长处理流数据和批数据的一些数据那么流数据我们在前面已经给大家讲了就是DataStream它相关的一些开发如何进行开发它的输入源和
[00:32] 数据的转换操作以及它的输出源等等各种各样的一些操作那么dataset呢它是针对于我们的批数据或者说是有界的一个数据集进行了一个处理那么所以我们今天首先的要学习一个dataset的示例通过这个示例呢大家掌握如何开发dataset那么开发dataset这个程序它的一个流程是什么那么第二部分的话我们需要掌握
[00:58] 我们的dataset它的输入源是什么如何设置我们的输入源以及我们dataset进行的转换操作是什么那么还有一部分就是我们如何来掌握掌握我们的dataset它的输出源我们要把我们dataset的计算结果输出到什么地方去那么第四部分的话是我们需要掌握如何来调试我们的程序也就是说dataset的程序那么我们这个调试的过程呢其实不单单是
[01:25] 针对于DataSet针对于DataStream这种流数据那么它的调试过程也是类似的那么第五部分是我们需要掌握我们的Flink Table API和Circle的含义以及它相关的一些原理那么第六部分是我们要了解我们Table的执行过程以及执行计划它是如何来把我们的每一个每一段代码或者说每一个过程如何来进行进行操作的进行执行的它的底层到底是如何来做的
[01:55] 那么最后一部分的话我们需要将我们的datastream啊dataset与我们的table进行相互的一个转换无论是说把datastream转换成table还是说把dataset转换成table或者是反之从table转换成datastream或转换成dataset这是我们今天要学习的一个目标

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Flink DataSet 和 SQL 编程的基础概念与示例代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程标题“Flink DataSet和SQL编程”，左侧为目录结构，内容包括“学习目标”和“1 Flink DataSet编程”章节，其中“1.1 DataSet示例”下展示了一个 Java 类的开头代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
学习目标：
1. 掌握开发DataSet程序的流程
2. 掌握DataSet输入源的常见类型和对应输入源
3. 掌握DataSet转换操作和常用算子
4. 掌握常用模块DataSet程序
5. 了解Flink Table API和SQL的含义和原理
6. 了解Table执行程序的执行计划
7. 掌握如何将DataStream和DataSet与Table进行互相转换

1 Flink DataSet编程
Flink中的DataSet程序实现数据转换的常规程序（例如，过滤，映射，连接，分组）。数据集最初从某些来源（例如，通过文件或数据库）接收，接收可以以流式或批式方式写入到目标中。Flink程序可以在单个VM中执行，也可以在许多计算机的集群上执行。

1.1 DataSet示例
我们以单词统计计数程序为例，演示Flink DataSet程序的开发过程：
public class WordcountExample {
    public static void main(String[] args) throws Exception {

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

