# 画面线理解：5.1 学习目标

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.1 学习目标_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:14, 00:24, 00:33, 00:43, 00:52, 01:02, 01:12, 01:21, 01:31, 01:41, 01:50, 02:00, 02:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:21:12

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
