# 8-MapReduce-流量统计求和-排序-FlowBean编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\8-MapReduce-流量统计求和-排序-FlowBean编写【海量资源尽在 ubkz.com】.mp4
- 时长 5分19秒（音频 320s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们在这个案例的基础上又提出一个新的需求什么需求呢我们可以呢按照流量的某个字段呢来进行排序打开我们刚才的这个一个输出的结果那这里呢比如说呢我可以按照这个流量字段中的这一列进行排序排序的话呢我可以按照降序来排好要实现这个功能的话呢我们还需要再写一个myproduce也就是说我们整个案例呢需要两个myproduce
[00:30] 上一个myproduce呢就是刚才写过的那么这是它的一个输出我们需要将上一个它的一个输出呢作为下一个myproduce的一个输入好那接下来呢我们来思考一下如何去做那要去做这么一个排序的话呢首先我们来想一想要实现排序我们之前呢也做过类似的一个案例那么要对这一列排序的话呢其实呢我们可以呢这样做我们可以把后面这个四个字段呢
[00:59] 还是封装一个加尔病封装一个加尔病之后呢我们可以让这个加尔病作为我们的K2一般情况下呢你对谁排序一般呢就要把谁作为K2所以说我们可以把这个呢作为K2而把我们的手机号呢作为V2然后呢进行mypreduce一个计算那接下来呢我们来边写呢边去讲这个功能那接下来我们来看打开我们的ID
[01:29] 在这里呢我们再建一个包这个地方是myproduce然后我们写一个我们来写一个sort稍等sort在这里的话呢我们先这样我们来先写一个写一个类也就是我们的一个java bin类这个java bin呢我们还叫flowbin这个flowbin呢还是有四个成员变量那么和上面这个我们
[02:13] 创建的这个Flowbin基本上是一样的为了节省时间呢我把这个呢给大家直接拷贝过来好拷贝完之后呢我们来思考一个问题那这个地方呢要实现一个接口我们之前实现的一个是一个redable那么这个Flowbin呢和我们之前的应该不太一样我们之前呢只考虑这个加密bin的一个序列化而这里呢我们需要对这个按照某一个这个Flowbin的某一个字段进行排序这个时候呢
[02:47] 我们不能光实现这个接口我们要实现哪个接口呢我们要实现WriteableCompareable好这里边写一个Flowbin要实现这么一个接口然后呢重写这里的一个方法叫Compare to方法为什么要实现这个接口呢因为实现了这个接口我们既可以对我们的Flowbin呢进行一个序列化又呢可以对它进行排序我们要按照它的某一个字段排OK哪个字段呢我们刚才说过了
[03:17] 需要将后面这四个呢作为一个K2然后呢手机号作为V2我们要按照这个上行流量这个上行的一个数据报来进行排序所以说呢我们排序的字段呢就是upflow那如何去指定按照这个字段排序呢我们需要呢在这里重写这里边有个方法叫compare to叫compare to方法这个方法呢其实我们以前也写过怎么写呢我们可以直接return哎反而为什么呢
[03:47] 一个this.upflow然后呢调个方法叫compare to这个地方呢我们以前呢写的是other就是其他的哎和其他的一个upflow呢进行比较other.upflow我们要这样去做好这样子的话呢我们就可以按照它的一个上行包总数来排序OK这个代码就写完了你可以呢在这调个get
[04:17] upflow在这调个getupflow也是可以的好那么这个写完之后呢相当于我们的排序规则就定义好了按照什么排序呢按照按照上行数据包数据包进行排序那么大家注意这个写完之后呢默认它应该是一个什么呢应该是一个应该是一个生序对不对那如果我要是按照降序怎么做呢
[04:52] 我可以在这个值的后面呢我乘一个-1那乘一个-1呢相当于把这个值呢给它倒过来如果你这个地方反为的是一个1那我就乘以-1之后呢变成-1如果你反为的是一个-1那我就反为个1那这样子呢可以改变它的一个排序规则这个类呢写完之后呢那接下来呢我们就可以写我们的myper和reducer了那这样我在这里呢我先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hadoop MapReduce中定义一个自定义的可序列化数据结构FlowBean，使其支持排序功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：显示一个文本文件，内容为多行数字数据，其中第15行数据被选中。
画面2：在画面1的基础上，选中了从第11行到第16行的数据。
画面3：在IDEA中打开项目，显示了项目结构和JobMain.java文件内容，其中包含创建Path对象的代码。
画面4：在IDEA中，右键点击“Add to Favorites”选项。
画面5：显示FlowBean.java文件内容，定义了FlowBean类，包含upFlow、downFlow、upCountFlow、downCountFlow四个私有属性。
画面6：在FlowBean.java文件中，光标位于“implements Writable”后，显示了IDE的自动补全建议。
画面7：在FlowBean.java文件中，选中了“private Integer upFlow;”、“private Integer downFlow;”、“private Integer upCountFlow;”和“private Integer downCountFlow;”四行代码。
画面8：在FlowBean.java文件中，显示了write方法和readFields方法的实现，以及compareTo方法的实现（当前为return 0;）。
画面9：在IDEA中，切换到FlowBean.java文件，显示了FlowBean类的定义，其中implements WritableComparable<FlowBean>。
画面10：在FlowBean.java文件中，光标位于compareTo方法的return语句上，显示了IDE的自动补全建议。
画面11：在FlowBean.java文件中，光标位于compareTo方法的return语句上，显示了IDE的自动补全建议，其中包含“compareTo(FlowBean other)”方法。
画面12：在FlowBean.java文件中，选中了compareTo方法的return语句。
画面13：在FlowBean.java文件中，选中了compareTo方法的return语句，其中内容为“return this.upFlow.compareTo(other.upFlow);”。
画面14：在IDEA中，显示了FlowBean.java文件的内容，其中包含toString方法和write方法的实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
new Path("hdfs://node01:8020/input/fl...class);
画面5：
package cn.itcast.maperduce_flowcount;
import org.apache.Hadoop.io.Writable;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
public class FlowBean implements Writable {
private Integer upFlow;
private Integer downFlow;
private Integer upCountFlow;
private Integer downCountFlow;
public Integer getUpFlow() {
return upFlow;
}
画面6：
public class FlowBean implements Writable {
private Integer upFlow;
private Integer downFlow;
private Integer upCountFlow;
private Integer downCountFlow;
public Integer getUpFlow() {
return upFlow;
}
public void setUpFlow(Integer upFlow) {
this.upFlow = upFlow;
}
画面8：
@Override
public void write(DataOutput dataOutput) throws IOException {
dataOutput.writeInt(upFlow);
dataOutput.writeInt(downFlow);
dataOutput.writeInt(upCountFlow);
dataOutput.writeInt(downCountFlow);
}
@Override
public void readFields(DataInput dataInput) throws IOException {
this.upFlow = dataInput.readInt();
this.downFlow = dataInput.readInt();
this.upCountFlow = dataInput.readInt();
this.downCountFlow = dataInput.readInt();
}
@Override
public int compareTo(FlowBean flowBean) {
return 0;
}
画面9：
package cn.itcast.maperduce_sort;
import org.apache.Hadoop.io.Writable;
import org.apache.Hadoop.io.WritableComparable;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
public class FlowBean implements WritableComparable<FlowBean> {
private Integer upFlow;
private Integer downFlow;
private Integer upCountFlow;
private Integer downCountFlow;
public Integer getUpFlow() {
return upFlow;
}
画面10：
@Override
public void readFields(DataInput dataInput) throws IOException {
this.upFlow = dataInput.readInt();
this.downFlow = dataInput.readInt();
this.upCountFlow = dataInput.readInt();
this.downCountFlow = dataInput.readInt();
}
@Override
public int compareTo(FlowBean flowBean) {
return 0;
}
画面11：
@Override
public int compareTo(FlowBean other) {
return this.upFlow.compareTo(other.upFlow);
}
画面13：
@Override
public int compareTo(FlowBean other) {
return this.upFlow.compareTo(other.upFlow);
}
画面14：
@Override
public String toString() {
return upFlow +
"\t" + downFlow +
"\t" + upCountFlow +
"\t" + downCountFlow;
}
@Override
public void write(DataOutput dataOutput) throws IOException {
dataOutput.writeInt(upFlow);
dataOutput.writeInt(downFlow);
dataOutput.writeInt(upCountFlow);
dataOutput.writeInt(downCountFlow);
}
@Override
public void readFields(DataInput dataInput) throws IOException {
this.upFlow = dataInput.readInt();
this.downFlow = dataInput.readInt();
this.upCountFlow = dataInput.readInt();
this.downCountFlow = dataInput.readInt();
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

