# 5.11 Table执行过程分析

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.11 Table执行过程分析_【海量资源尽在 666java.com】.mp4
- 时长 6分22秒（音频 383s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好,下面我们来学习一下Flink Table API和Circle的一个执行过程Flink Table API和Circle它利用的是Apache Call Set的这样的一个查询优化的框架为流逝数据和批数据的一个关系查询保留了统一的一个接口那么使用Call Set作为Circle解析和处理的引擎有很多包括Hive, Drill, Flink, Phoenix和Storm等各种各样的一些平台
[00:29] 主要在大数据领域里边和非结构化的一些数据它作为这种一个优化查询的框架非常的出名那么我们来看一看整个的一个执行过程它大致分成四部分第一部分来讲是一个pass这个pass过程其实就是一个解析的过程那么第二部分是一个validatorvalidator的话它是一个做了一个验证与法一个检验的一个过程optimize这个过程呢
[00:56] 是针对于我们的优化查询的Circle做了一些优化的一些方面的事情那么最后一部分就是一个执行了那么我们来看一看Flink Circle它的一个执行流程那么一个流的Circle语句经过提交提交到我们的Call Set进行解析优化最后到Flink的引擎进行执行一般分成以下几个阶段那么第一个阶段叫Circle PathCircle Path它是将Circle语句
[01:25] 通过java cc解析成一个语法数ast那么coset中使用circle node表示ast那么第二部分是circle的一个validator它结合了数字字典去验证circle的语法也就是说我们提交的circle必须符合circle的语法的如果我用select那么我们的语法器其实就能解析到但是我如果用select1 select2
[01:53] 类似于这样的一个select关键字那么其实是不能够被解析的同样的还有关键字包括insert update等等这些其实都属于它的一些语法那么第三部分来讲的话它会生成逻辑执行计划那么将circle node也就是说第一部分生成的这个circle node是表示的这种语法术转换成逻辑的一个执行计划它是用real node表示的
[02:22] 那第四部分的话是optimized logical plan也就是说他先将我们的call set的一个规则优化去优化我们的逻辑计划然后再基于Flink定制的优化规则去优化我们的逻辑计划那第五部分的话是我们生成Flink的一个物理执行计划这里也是基于Flink里头的一些规则
[02:48] 将我们进行优化后的一些逻辑计划转换成Flink物理执行的计划第六步就是我们将物理执行计划转换成Flink的一个执行计划也就是调用相应的一些translate to plan的方法转换和利用code generator原编成Flink的各种算子也就我们在算子里边的
[03:15] 各种MAP的一些方法那些实际上是属于比较偏底层的那么前边的Circle进行了多次转换之后转换成我们Flink的DataStream和DataSet的一些算子的一些运算那第二部分的话我们看一看Flink Table API的一个执行流程如果是通过Table API传过来的一些任务也会经过Call Set进行优化
[03:40] 基本流程和直接运行circle是比较类似的那第一部分的话是table API的一个解析Flink会把table API表达式的计算逻辑也表示成一棵树这棵树实际上就是我们的语法树用train node来表示在这棵树上的每个节点的计算逻辑都会用expression来表示那第二部分的话是validate它会结合我们的数据字典将树里的每个节点
[04:09] unresolved expression进行绑定然后生成solved expression也就是说是没有解决的一些表达式转换成一个可被解决的表达式那第三部分的话是生成我们的逻辑计划它会依次遍历数的每个节点然后调用construct的方法将原先的train node表达的节点转换成用
[04:34] Calset内部的数据结构Renode来表示即生成逻辑计划用Renode表示这个地方的意思是说我们生成的刚才生成的一个语法的一个数TrainNode那么TrainNode上的节点呢会转换成Calset的Renode第四部分是我们进行了优化的一个逻辑执行计划先基于Calset的一个规则去优化我们的逻辑计划
[05:00] 然后再基于Flink定制的一些优化的规则去优化我们的逻辑计划这个过程和我们的Flink circle的执行流程实际上是一样的那第五部分的话其实就是我们生成Flink的物理执行计划也就是基于Flink里面的一些ruler一些规则然后呢将我们的逻辑的优化执行计划转换成Flink物理执行计划去执行
[05:29] 第六步就是我们将物理执行计划转换成Flink的执行计划也就是调用translate to plan方法转换和利用code 这原编程成Flink的各种算子将来讲的话第一步将无论是API也好还是circle的语法转换解析成call set的语法数
[05:52] 那么第二步来讲的话我们需要经过语法术的一个验证验证它的是否符合我们要求的call set的一个语法那第三步的话是经过一些优化把各个执行计划优化成无论是从逻辑执行计划到我们的物理执行计划那么最后一步的话其实是我们的物理执行了这是我们整个的一个Flink table的一个执行过程的一个分析就讲到这谢谢大家

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Flink SQL 和 Table API 的执行流程，重点是解析、验证、优化和执行阶段，以及与 Apache Calcite 的集成。

2) 按时间顺序列出每张画面的要点：
   画面1: 展示了“2.4 Table执行过程分析”章节，包含一个流程图：Parser → Validate → Optimize → Execute。下方列出“2.4.1 Flink Sql 执行流程”的六个阶段，包括 Sql Parser、Sql Validator、生成Logical Plan、生成 optimized Logical Plan、生成Flink Physical Plan、将物理执行计划转成Flink ExecutionPlan。
   画面2: 画面内容与画面1基本一致，但鼠标光标在“Optimize”节点上，且“2.4.2 Flink Table Api 执行流程”部分开始显示。
   画面3: 画面内容与画面2基本一致，鼠标光标在“2.4.2 Flink Table Api 执行流程”标题处。
   画面4: 画面内容与画面1基本一致，鼠标光标在“Optimize”节点上。
   画面5: 画面内容与画面1基本一致，鼠标光标在“Optimize”节点上。
   画面6: 画面内容与画面1基本一致，鼠标光标在“Optimize”节点上。
   画面7: 画面内容与画面1基本一致，鼠标光标在“Optimize”节点上。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
   画面1、4、5、6、7 中出现的代码：
   ```java
   String[] fieldNames = {"A", "B", "C"};
   TypeInformation[] fieldTypes = {Types.INT, Types.STRING, Types.LONG};
   // 将TableSink注册成表：CsvSinkTable
   tableEnv.registerTableSink("CsvSinkTable", fieldNames, fieldTypes, csvSink);
   ```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
   画面1、4、5、6、7 中出现的流程图：
   - Parser → Validate → Optimize → Execute
   画面1、2、3、4、5、6、7 中出现的标题：
   - 2.4 Table执行过程分析
   - 2.4.1 Flink Sql 执行流程
   - 2.4.2 Flink Table Api 执行流程

5) 无。

