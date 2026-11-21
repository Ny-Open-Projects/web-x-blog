# 画面线理解：5-MapReduce-流量统计求和-FlowBean和Mapper代码编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\5-MapReduce-流量统计求和-FlowBean和Mapper代码编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:41, 01:36, 02:54, 03:44, 04:02, 04:32, 04:50, 05:08, 05:50, 07:08, 08:23, 09:40, 10:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:25:56

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Hadoop 中自定义一个用于统计手机上下行流量的 FlowBean 对象，并实现其 Writable 和 WritableComparable 接口，用于 MapReduce 作业的键值对处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 MapReduce 作业的 Map 阶段和 Reduce 阶段的数据流转示意图，其中 Map 阶段输入为手机号和四个流量值，输出为手机号和四个流量值的组合（K2, V2），Reduce 阶段对相同手机号的流量值进行聚合。
画面2：在 IntelliJ IDEA 中，用户正在创建一个新的 Java 类 FlowCountReducer。
画面3：展示需求文档，明确任务是统计手机上下行流量，并定义了自定义的 FlowBean 对象，用于在 Map 阶段输出。
画面4：在 FlowBean 类中，用户正在实现 WritableComparable 接口，通过鼠标悬停查看接口方法。
画面5：在 FlowBean 类中，用户正在编写 toString 方法，用于格式化输出四个流量值。
画面6：在 FlowBean 类中，用户正在编写 write 方法，用于将四个流量值写入 DataOutput。
画面7：在 FlowBean 类中，用户正在编写 readFields 方法，用于从 DataInput 读取四个流量值。
画面8：在 FlowBean 类中，用户正在编写 getDownFlow 方法，用于获取下行流量值。
画面9：在 IntelliJ IDEA 中，用户选中了 FlowCountMapper 类，准备编写 Map 函数。
画面10：在 FlowCountMapper 类中，用户正在导入必要的 Hadoop 包，并查看 Mapper 类的继承结构。
画面11：在 FlowCountMapper 类中，用户正在编写 map 方法，准备处理输入的键值对。
画面12：在 FlowCountMapper 类中，用户正在编写 map 方法，将输入的文本按制表符分割，并提取手机号和四个流量值。
画面13：在 FlowCountMapper 类中，用户正在编写 map 方法，创建 FlowBean 对象并设置四个流量值。
画面14：在 FlowCountMapper 类中，用户正在编写 map 方法，将手机号和 FlowBean 对象写入上下文。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
public class FlowBean implements Writable {
    private Integer upFlow;
    private Integer downFlow;
    private Integer upCountFlow;
    private Integer downCountFlow;

    @Override
    public void write(DataOutput out) throws IOException {
        out.writeInt(upFlow);
        out.writeInt(downFlow);
        out.writeInt(upCountFlow);
        out.writeInt(downCountFlow);
    }

    @Override
    public void readFields(DataInput in) throws IOException {
        this.upFlow = in.readInt();
        this.downFlow = in.readInt();
        this.upCountFlow = in.readInt();
        this.downCountFlow = in.readInt();
    }
}
```

画面4：
```java
public class FlowBean implements WritableComparable<T> {
    private Integer upFlow;
    private Integer downFlow;
    private Integer upCountFlow;
    private Integer downCountFlow;
    ...
}
```

画面5：
```java
public String toString() {
    return
        upFlow + "\t" + downFlow + "\t" +
        upCountFlow + "\t" + downCountFlow;
}
```

画面6：
```java
@Override
public void write(DataOutput dataOutput) throws IOException {
    dataOutput.writeInt(upFlow);
    dataOutput.writeInt(downFlow);
    dataOutput.writeInt(upCountFlow);
    dataOutput.writeInt(downCountFlow);
}
```

画面7：
```java
@Override
public void readFields(DataInput dataInput) throws IOException {
    this.upFlow = dataInput.readInt();
    this.downFlow = dataInput.readInt();
    this.upCountFlow = dataInput.readInt();
    this.downCountFlow = dataInput.readInt();
}
```

画面8：
```java
public Integer getDownFlow() {
    return downFlow;
}
```

画面10：
```java
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;
```

画面11：
```java
public class FlowCountMapper extends Mapper<LongWritable, Text, Text, FlowBean> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        value = value.toString();
    }
}
```

画面12：
```java
@Override
protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    String[] split = value.toString().split("\t");
    String phoneNum = split[0];
```

画面13：
```java
FlowBean flowBean = new FlowBean();
flowBean.setUpFlow(Integer.parseInt(split[1]));
flowBean.setDownFlow(Integer.parseInt(split[2]));
flowBean.setUpCountFlow(Integer.parseInt(split[3]));
flowBean.setDownCountFlow(Integer.parseInt(split[4]));
```

画面14：
```java
context.write(new Text(phoneNum), flowBean);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图/流程图结构：
- Map 阶段：输入数据（手机号和四个流量值）→ 输出数据（手机号和四个流量值的组合 K2, V2）
- Reduce 阶段：输入数据（手机号和四个流量值的组合 K2, V2）→ 输出数据（手机号和四个流量值的总和）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
