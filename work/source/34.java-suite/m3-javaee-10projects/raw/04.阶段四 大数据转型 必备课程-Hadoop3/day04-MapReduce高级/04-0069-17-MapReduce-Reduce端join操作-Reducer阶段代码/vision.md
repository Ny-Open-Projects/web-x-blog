# 画面线理解：17-MapReduce-Reduce端join操作-Reducer阶段代码

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\17-MapReduce-Reduce端join操作-Reducer阶段代码【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:13, 00:20, 00:37, 00:58, 01:26, 01:44, 02:09, 02:30, 02:55, 03:27, 03:50, 04:11, 04:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 05:06:15

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Hadoop MapReduce 中编写一个 Reduce 端的连接（Join）操作，通过自定义 Reducer 类来处理键值对数据，实现两个数据源的关联。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示项目结构，当前编辑的是 ReduceJoinReducer.java 文件，位于包 cn.itcast.mapreduce_reduce_join 下。
画面 2：在 ReduceJoinReducer.java 中，导入 org.apache.hadoop.mapreduce.Reducer 并声明类继承 Reducer。
画面 3：导入 java.xml.soap.Text，并将 Reducer 的泛型参数设置为 Text, Text, Text。
画面 4：展示一个图示，说明 Map 阶段如何将 products.txt 和 orders.txt 的数据进行分组和映射，输出 K2 和 V2。
画面 5：在 ReduceJoinReducer.java 中，重写 reduce 方法，并调用 super.reduce(key, values, context)。
画面 6：展示 Reduce 阶段的图示，说明如何将 V2 数据按 K3 分组，输出 V3。
画面 7：在 ReduceJoinReducer.java 中，为 reduce 方法的 for 循环添加 if 语句。
画面 8：在 ReduceJoinReducer.java 中，为 reduce 方法的 for 循环添加 else 语句。
画面 9：在 ReduceJoinReducer.java 中，为 reduce 方法的 for 循环添加变量 first 和 second 的初始化语句。
画面 10：在 ReduceJoinReducer.java 中，为 reduce 方法的 for 循环添加变量 first 和 second 的赋值语句。
画面 11：在 ReduceJoinReducer.java 中，为 reduce 方法添加 context.write(key, new Text(...)) 语句。
画面 12：在 ReduceJoinReducer.java 中，为 reduce 方法添加 context.write(key, new Text(first + "\t" + second)) 语句。
画面 13：在 ReduceJoinReducer.java 中，为 reduce 方法添加 if (first.equals("")) 语句。
画面 14：在 ReduceJoinReducer.java 中，为 reduce 方法添加 else 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
package cn.itcast.mapreduce_reduce_join;
画面 2：
import org.apache.hadoop.mapreduce.Reducer;
public class ReduceJoinReducer extends Reducer<...> {
画面 3：
import java.xml.soap.Text;
public class ReduceJoinReducer extends Reducer<Text, Text, Text, Text> {
画面 5：
@Override
protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
    super.reduce(key, values, context);
}
画面 9：
String first = "";
String second = "";
for (Text value : values) {
    if (value.toString().startsWith("p")) {
        first = value.toString();
    } else {
        second = value.toString();
    }
}
画面 11：
context.write(key, new Text(...));
画面 12：
context.write(key, new Text(first + "\t" + second));
画面 13：
if (first.equals("")) {
    context.write(key, new Text("NULL\t" + second));
} else {
    context.write(key, new Text(first + "\t" + second));
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4：
标题：Map 阶段
图示：
products.txt → K1 → V1 → K2 → V2
orders.txt → K1 → V1 → K2 → V2
图示下方：
p0001,小米5,1000,2000 → p0001 → p0001,小米5,1000,2000
p0002,锤子T1,1000,3000 → p0002 → p0002,锤子T1,1000,3000
画面 6：
标题：Reduce 阶段
图示：
V2 → K3 → V3
图示下方：
p0001,小米5,1000,2000 → p0001 → p0001,小米5,1000,2000
p0002,锤子T1,1000,3000 → p0002 → p0002,锤子T1,1000,3000
p0003, NULL → p0003 → p0003, NULL

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
