# 5-MapReduce-流量统计求和-FlowBean和Mapper代码编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\5-MapReduce-流量统计求和-FlowBean和Mapper代码编写【海量资源尽在 ubkz.com】.mp4
- 时长 10分42秒（音频 642s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在讲完这个案例的流程之后呢接下来我们用代码来实现一下来打开我们的ID在这里呢我再建一个包再建一个包这个包呢叫MapReduce然后呢我们写个FlowCount就是流量统计的意思在这里面呢我们需要建立先建立一个Map类吧FlowCountMap就是我们的Map那还有一个Reducer
[00:32] 也叫flow count reducer还有呢我们的一个主类叫jobman那这里边其实还有一个类我们要定义我们在讲流程的时候啊在这里边map阶段的k这个v2是一个自定义的一个加尔并叫flowbin我们需要去定义一下所以说呢还需要写一个flowbinflowbin好这个呢是我们一个自定义的加尔并那我们写代码呢就从这个flowbin开始
[01:08] 这个Flowbin里边呢其实包含了我们的流量的四个字段我们来看一下这四个字段首先呢这个地方呢是一个手机号那后面呢有四个字段这是上行包总数下行包总数上行流量和下行流量也就是我这个图里边你看上行包下行包上行流量好下行流量一次这是四个字段来我们分别来定义一下这个里边的四个字段我就直接把讲义上呢
[01:37] 这四个字段呢直接拿过来放在这个位置那么这是上行包这是下行包上行流量下行流量我们接下来来生成它的一个get和set方法好这个生成完了生成完之后呢我们再生成一个toString这个toString方法呢我们要做一个修改为什么要修改呢是因为呢它在序列化写到文件的时候呢它需要调用这个toString方法所以说我修改成呢
[02:13] 我比较喜欢的一个格式OK这个地方呢我用钢T来分割那这个地方呢也是用钢T来分割再改一下这个地方呢我就把它写完了好写完之后呢我们这个一个加尔并呢普通一个加尔并就写完了写完之后呢我们还要注意一点我们这个flowbin呢在myproduce呢要去做序列化那么要实现这个加尔并的一个序列化的
[02:47] 我们还需要去实现一个接口这个接口呢我们之前用的接口叫什么呢叫WriteableWriteable然后呢还有个叫Compareable大家还记不记得我们上一次实现的是这个接口那我们今天呢我们只实现它的一个序列化我们不进行排序这个时候呢我们可以直接实现这个Writeable就可以了OK实现它的目的呢就是我只做序列化我并不进行排序
[03:17] 那么接下来我们要重写这里面的方法好这里边有两个方法一个是write一个是read这个write方法呢咱们以前写过其实就是将每一个成员变量进行调个write方法就可以了直接我们都是一个什么类型呢我们都是一个integer类型那这样子我们直接用write int就可以了好write int好了那直接把这个地方呢一个是upflow我们依次写一下
[03:48] 还有一个data out一个是一个是什么downflow接下来是data out.write int都是int然后呢这个地方是up count flow好再来一个最后一个是down count flow好写完了那这就是一个序列化的一个方法还有一个方法呢是反序列化这个反序列化呢它的写法呢是前面是this点
[04:21] upflow等于什么呢我们来用这个data input来调一个方法叫readint就可以了来我们一次来把它做一下这个地方是downflow分别调这个readint因为它是整形然后this.upcountflow等于dataint.readint好最后一个this.然后呢是downcountflow然后是data input.readint好了
[04:55] 我们就把这个序列化和反序列化写完了写完之后呢我们这个flowbin呢基本上就完成了完成之后呢接下来我们再写我们的Mapper方法在写这个Mapper的时候呢首先我们需要去干嘛是不是需要去我们需要去去继承一个Mapper对吧OK继承这个mapperMAPP这个Mapper呢有
[05:23] 有四个范型一个是K1 V1一个是K2 V2那K1 V1呢都是固定的我们这里有long retable而V1呢是每一行的文本数据是test关键是K2 V2是什么类型呢我们刚才呢给大家分析了我们的K2呢是一个test也就是一行的这个手机号而我们的V2呢是一个自定义的一个flowbin所以说呢这个地方K2 V2是test的一个flowbin
[05:50] 好这个写完了写完之后呢我们来去重写里边的map方法在这个map方法中呢我们需要做一件事情将我们的k1 v1转成k2 v2要做这么一件事情那么我们来看在这个图k1 v1呢k1我们不管是行偏量而v1呢是一行的数据而我们的k2呢是手机号那所以说要有k2我们是不是只需要在这个一行数据中呢
[06:20] 把手机号呢给它截取出来或者叫拆分出来是不是就可以了而你的V2呢是四个流量字段那我们也需要在这一行数据中呢把这四个字段是不是拆分出来就行了所以说呢我们其实在这个MAP阶段最重要的其实做一个做出来拆分好把手机号拆分出来然后呢把这四段四个字段也拆分出来那这四个字段拆分完之后呢还要做一件事情是把它封装到一个Flowbin里边
[06:49] 是不是作为VR好那咱们接下来就做这个事情第一呢我们要拆分手机号吧拆分手机号拿到这个valuevalue就是一行的文本数据value.split这个split这个地方是value还要叫掉toString方法把它转成一个String然后呢split我们用-t来作为分割符拿到这么一个数组拿到这个数组里边
[07:20] 数组之后呢我们要拆分手机号那手机号呢它在哪一个列呢你看咱们向左看这个是时间戳那这个就是手机号所以说它的索引应该是这是0这是1也就是说我们要在这个数组里边来拿到这个1这个索引那这里边呢其实就是我们的手机号我们叫做phone然后number这个手机号呢其实就是我们的K2
[07:49] 那除了拆分手机号之外呢我们还要拆分呢流量字段拆分我们要去获取吧不能说拆分获取流量四个流量字段好获取完流量字段之后呢我们是不是要把它封装到flowbin里边所以说我们先去new个flowbin好flowbin呢然后呢开始给这个flowbin呢去设置四个字段的值也就是设置四个成员变量的值那么flowbin呢我们直接设置吧
[08:25] 设置一个upflowupflow呢这个值其实就来自这里那么它这个upflow呢是哪一个列呢我们来数一下吧这个是0这是1 2 3 4 5 6应该是6 7 8 9那这个地方呢应该是6 7 8 9好那这个地方就是split这个是6那这个就是upflow这个地方是一个字部串但是它要求的是一个integer类型
[08:54] 我们可以用integer.puzzle把它呢直接放进去就可以了好这是这个这是一个上行上行上行包总数加上呢一个下行包总数叫downflow那这个地方呢这是应该是7好还有呢上行流量和下行流量那再来一个再复制一份这个地方呢是一个upcountflowupcountflow好那么这个地方呢应该是8
[09:27] 最后再来一个应该是9最后来一个下行总量应该是Done这是一个DoneCount Flow好那这里面应该没问题好封装完之后相当于这个Flow Bean就有数据了那接下来第三步我们就是将K2将K2和V2写入上下文中好那么怎么做呢用Counts.Dir
[10:00] 然后呢我们的K2呢其实就是我们的full number但是这个地方要的是test类型所以说我们拗一个test这里边呢我们来写谁呢我们来写full number而这个V2呢它是一个flowbin所以说我们直接写flowbin好到此为止呢我们的map方法就写完了说白了就是将我们的一行数据然后呢进行了一个拆分拆分完之后呢想办法把它
[10:31] 找到一个K2和V2V2呢是一个flowbeam所以说我们要去封装好那么这个map阶段就写完了那我们呢先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Mapper;
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

