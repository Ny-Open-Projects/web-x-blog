# 5.5 DataSet输出流

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.5 DataSet输出流_【海量资源尽在 666java.com】.mp4
- 时长 5分4秒（音频 305s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好下面呢我们来给大家介绍Flink dataset的输入源我们在前面给大家介绍了Flink dataset的输入源
[00:09] 它是对接了我们不同的数据比如我们的文本数据或者是我们某一些数据集合这些有限的数据集作为我们的输入源那么我们对于这些输入源转做了一些很多的一些转换操作无论是map flat map filter等各种各样的一些转换合并等各种各样的一些操作那么操作完之后呢下一步我们要把数据进行输出输出到不同的地方去这个过程呢其实叫做输出源
[00:38] 那么我们Flink dataset的输出源包含哪些类型呢我们来看一下首先的话我们有一个方法叫write as text那么从这个字面意义上来理解的话就相当于是我们把一个dataset输出到一个文本文件里边去那么这个文本文件的话我们是按照在原始的这种dataset里边的顺序来顺序的写入到我们的文件里边那么第二个来讲的话叫
[01:07] write as formatted text这个呢和第一个方法相比来讲的话它是提供了一个顺序或者提供了一个字符帅的一个顺序那么相应的我们会按照我们自定义的这个顺序来写入我们的文本文件第三个方法叫做write as csv那么它是将我们的原组写为一逗号分割的这样的一个文件比如我们的原组数据tompo2或tompo3
[01:37] 等等这种原组数据我们要写到CSS文件里边去我们可以调用这种方法那么第四个方法叫printprint和print to arrow那么print是什么意思print就是和打印就是打印的一个意思对吧我们在标准输出上输出我们的数据print arrow的话是把错误输出错误流给它标准输出去那么第五种的话是一个write方法write方法它是自定义文件输出的方法
[02:07] 我们支持自定义的一个对象到自节流的一个转换第六个的话是我们的一个outputoutput大多数一个通用的一个输出方法它用于对于非基于文件的数据的一个接收器我们比如我们可以写我们的基于GDPC的一个输出输出到我们的官邢数据库里面去那么下面呢我们来演示一下如何做我们的输出我们打开我们的一个iDia工具然后我们新创建一个类
[02:36] 这个类叫做syncdemo而这个syncdemo里边我们先添加我们的main函数我们首先呢我们可以定义我们的environment设置环境那么这个环境呢叫executionenvironmentenv等于executionenvironment的我们要getenvironment
[03:09] 那第二步来讲的话我们要设置我们的输入源对吧我们前面已经给他讲给大家讲过我们要设置输入源而这个输入源呢我们可以用简单的方式比如说用list一个java的list每个list呢list中的对象呢是一个字符串等于new arrow list那么我们给这个list添加一些字符串
[03:46] 这个字符帅比如说abclist.adddf我们添加完了这个字符帅之后下一步我们就直接能够把我们这个java的list对象给它复制成我们的一个dataset而这个dataset呢是一个string类型的txt等于env.fromcollectionlist
[04:23] 那此时我们就已经复制好了那下一步的时候我们需要把我们的这个dataset的一个数据的流给它转换成或者说保存到我们的文本文件里边我们直接用txt.write as text那么write as text的我们下一步需要输入什么输入一个地址这个地址比如我们放在第一盘的1.txt文件那么
[04:53] 此时我们要执行一下我们这个程序因为点execute执行我们执行程序那么我们需要用trahl开始或者

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中编写一个 Flink 批处理程序，通过创建一个包含数据源的 DataSet 并调用 execute() 方法来执行作业。

2) 按时间顺序列出每张画面的要点：
画面1: 选中并打开名为 "SinkDemo.java" 的 Java 文件，准备编写代码。
画面2: 在项目结构中右键点击 "src" 目录，弹出创建新文件的菜单。
画面3: 在编辑器中，光标位于 "SinkDemo" 类的 main 方法内，准备编写代码。
画面4: 在 main 方法内输入 "Execu"，IDE 提供了 "ExecutionEnvironment" 的自动补全建议。
画面5: 在 main 方法内输入 "ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();"，完成环境设置。
画面6: 在 main 方法内输入 "//2. 设置输入源"，并开始编写代码。
画面7: 在 main 方法内输入 "List"，IDE 提供了 "List" 类型的自动补全建议。
画面8: 在 main 方法内输入 "List<String> list = new ArrayList<>()"，并开始添加数据。
画面9: 在 main 方法内输入 "list.add("abc")"，并继续添加数据。
画面10: 在 main 方法内输入 "DataSet<String> cdt = env.fromCollection(list)"，并开始调用 execute() 方法。
画面11: 在 main 方法内输入 "env.execute()"，IDE 提供了 "execute()" 方法的自动补全建议。
画面12: 在 main 方法内输入 "env.execute()"，并完成代码编写。
画面13: 在 main 方法内输入 "env.execute()"，并完成代码编写。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1: 无代码。
画面2: 无代码。
画面3: 无代码。
画面4: 无代码。
画面5: 无代码。
画面6: 无代码。
画面7: 无代码。
画面8: 无代码。
画面9: 无代码。
画面10: 无代码。
画面11: 无代码。
画面12: 无代码。
画面13: 无代码。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

