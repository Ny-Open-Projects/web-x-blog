# 画面线理解：14-MapReduce排序-实现比较器和序列化代码

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\14-MapReduce排序-实现比较器和序列化代码【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:36, 01:03, 02:03, 02:31, 03:36, 04:37, 07:04, 07:52, 08:17, 08:56, 09:23, 09:51, 10:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:08:28

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Hadoop MapReduce 中自定义一个 PairWritable 类，实现按字典序先按 key 排序再按 value 排序的自定义排序规则。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 MapReduce 的 Shuffle 阶段流程图，包含 Map、Shuffle、Reduce 三个阶段，其中 Shuffle 阶段包含“分区、排序、规约、分组”四个步骤。图中还展示了自定义 Map 和 Reduce 函数的逻辑。
画面 2: 展示了 WordCount 项目中关于“自定义排序规则”的 PPT 内容，列出了“要求”和“解决思路”，并指出需要实现 PairWritable 类。
画面 3: 在 IntelliJ IDEA 中，创建了一个名为 SortReducer 的 Java 类。
画面 4: 在 IntelliJ IDEA 中，编辑 PairWritable 类，显示了其继承自 WritableComparable 的结构。
画面 5: 在 IntelliJ IDEA 中，编辑 PairWritable 类，开始实现 compareTo 方法。
画面 6: 在 IntelliJ IDEA 中，编辑 PairWritable 类，实现 toString 方法。
画面 7: 在 IntelliJ IDEA 中，编辑 PairWritable 类，开始实现 compareTo 方法。
画面 8: 在 IntelliJ IDEA 中，编辑 PairWritable 类，实现 setFirst 和 getSecond 方法。
画面 9: 在 IntelliJ IDEA 中，编辑 PairWritable 类，实现 compareTo 方法，先比较 first，再比较 second。
画面 10: 在 IntelliJ IDEA 中，编辑 PairWritable 类，实现 compareTo 方法，先比较 first，再比较 second。
画面 11: 在 IntelliJ IDEA 中，编辑 PairWritable 类，实现 getFirst 和 setFirst 方法。
画面 12: 在 IntelliJ IDEA 中，编辑 PairWritable 类，实现 compareTo 方法，先比较 first，再比较 second。
画面 13: 在 IntelliJ IDEA 中，编辑 PairWritable 类，实现 readFields 方法，使用 dataInput.readUTF() 读取 first。
画面 14: 在 IntelliJ IDEA 中，编辑 PairWritable 类，实现 compareTo 方法，先比较 first，再比较 second。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
TextInputFormat
K1    V1
0     a 1
5     a 9
11    a 3
16    a 7
21    a 8
27    a 10
32    a 5
Map阶段
1:自定义Map逻辑，将K1和V1转为K2和V2
K2    V2
a 1   a 1
a 9   a 9
b 3   b 3
a 7   a 7
b 8   b 8
b 10  b 10
a 5   a 5
Shuffle阶段
分区 排序 规约 分组
自定义排序规则:
class PairWritable implements WritableComparable<PairWritable> {
String first;
int second;
}
新 K2    V2
a 1   <a 1>
a 5   <a 5>
a 9   <a 9>
b 3   <b 3>
b 8   <b 8>
b 10  <b 10>
Reduce阶段
1:自定义Reduce逻辑
将新K2和V2转为K3和V3
```

画面 2:
```
要求
• 第一按字典顺序排序
• 第一相同的时，第二按降序进行排列
解决思路：
• 将 Map 输出的 <key,value> 中的 key 和 value 组合成一个新的 key (newKey) 值不变
• 这里就变成 <(key,value),value>，在针对 newKey 排序的时候，如果 key 相同，就对 value 进行排序
Step 1. 自定义类型和比较器
```

画面 3:
```
package cn.itcast.mapreduce_sort;
public class SortReducer
```

画面 4:
```
public class PairWritable implements WritableComparable<PairWritable> {
    WritableComparator<T> (org.apache.hadoop.io)
    WritableByteChannel (java.nio.channels)
    NonWritableChannelException (java.nio.channels)
```

画面 5:
```
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
public class PairWritable implements WritableComparable<PairWritable> {
@Override
public int compareTo(PairWritable pairWritable) {
    return 0;
}
@Override
public void write(DataOutput dataOutput) throws IOException {
```

画面 6:
```
public int getSecond() {
    return second;
}
public void setSecond(int second) {
    this.second = second;
}
@Override
public String toString() {
    return first + '\t' + second + '\n';
}
```

画面 7:
```
@Override
public String toString() {
    return first + '\t' + second + '\n';
}
//实现排序原则
@Override
public int compareTo(PairWritable other) {
    return 0;
}
```

画面 8:
```
public void setFirst(String first) {
    this.first = first;
}
public int getSecond() {
    return second;
}
public void setSecond(int second) {
    this.second = second;
}
@Override
public String toString() {
    return first + '\t' + second + '\n';
}
```

画面 9:
```
@Override
public String toString() {
    return first + '\t' + second + '\n';
}
//实现排序原则
@Override
public int compareTo(PairWritable other) {
    int result = this.first.compareTo(other.first); //abc abc
    if(result == 0) {
        return this.second - other.second;
    }
    return 0;
}
```

画面 10:
```
@Override
public String toString() {
    return first + '\t' + second + '\n';
}
//实现排序原则
@Override
public int compareTo(PairWritable other) {
    int result = this.first.compareTo(other.first); //abc abc
    if(result == 0) {
        return this.second - other.second;
    }
    return result;
}
```

画面 11:
```
public class PairWritable implements WritableComparable<PairWritable> {
    private String first;
    private int second;
    public String getFirst() {
        return first;
    }
    public void setFirst(String first) {
        this.first = first;
    }
    public int getSecond() {
        return second;
    }
    public void setSecond(int second) {
        this.second = second;
    }
```

画面 12:
```
@Override
public int compareTo(PairWritable other) {
    int result = this.first.compareTo(other.first); //abc abc
    if(result == 0) {
        return this.second - other.second;
    }
    return result;
}
```

画面 13:
```
@Override
public void readFields(DataInput dataInput) throws IOException {
    this.first = dataInput.readUTF();
    this.second = dataInput.readInt();
}
```

画面 14:
```
@Override
public int compareTo(PairWritable other) {
    int result = this.first.compareTo(other.first); //abc abc
    if(result == 0) {
        return this.second - other.second;
    }
    return result;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 架构图，从左到右依次为“诱文件” -> “TextInputFormat” -> “Map阶段” -> “Shuffle阶段” -> “Reduce阶段”。
画面 2: PPT 标题为“Step 1. 自定义类型和比较器”，下方列出“要求”和“解决思路”。
画面 4: 无 PPT 标题，但显示了 PairWritable 类的继承结构。
画面 6: 无 PPT 标题，但显示了 PairWritable 类的 toString 方法。
画面 7: 无 PPT 标题，但显示了 PairWritable 类的 compareTo 方法。
画面 9: 无 PPT 标题，但显示了 PairWritable 类的 compareTo 方法。
画面 10: 无 PPT 标题，但显示了 PairWritable 类的 compareTo 方法。
画面 11: 无 PPT 标题，但显示了 PairWritable 类的 getFirst 和 setFirst 方法。
画面 12: 无 PPT 标题，但显示了 PairWritable 类的 compareTo 方法。
画面 13: 无 PPT 标题，但显示了 PairWritable 类的 readFields 方法。
画面 14: 无 PPT 标题，但显示了 PairWritable 类的 compareTo 方法。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
