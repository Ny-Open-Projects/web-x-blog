# 17-MapReduce-Reduce端join操作-Reducer阶段代码

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\17-MapReduce-Reduce端join操作-Reducer阶段代码【海量资源尽在 ubkz.com】.mp4
- 时长 4分49秒（音频 289s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 写完这个map阶段之后呢接下来我们来写reducer阶段好reducer呢记成一个reducer好在这里写K2和K3的类型K2那么K2是一个testV2呢也是testK3呢是testV3呢也是test四个呢都是test你看这个导包我就导错了一定要确认一下好打了一个好多普好那这地方呢重写reduce方法在这里呢大家注意
[00:31] 在这里呢因为它把相同件的数据放在同一个集合那这个数据长什么样子呢这个数据来看这个图这个数据呢其实就长这样子我们最终要的效果是呢这个K2呢就变成K3了而我们的V3呢实际上将这个集合中的数据便利便利之后呢把第一个组串和第二个组串合并是不是就可以了好那我们来做这个事情首先呢我们需要去
[01:00] 我们需要去辨这个集合辨这个集合辨这个集合的时候呢我们需要将这个value这个组出呢我们是不是应该应该要进行一个拼接对不对拼接那拼接的时候呢我们要去分清楚谁在前谁在后我们这样我们让这个商品在前然后呢把这个订单呢在后我们要做这么事情那怎么去区分商品商品和订单呢你看
[01:29] 商品的话呢它这个它这个地方呢是一批开头是不是啊那这个P001那我们就这样写你看我们这样写if如果说呢这个地方呢是value.toStream.toStream那它呢这个start位置它表示它是一批开头那表示呢它是一个订单它是一个一个商品啊一个商品那商品的话呢我在这里呢我来定一个变量吧
[01:59] String一个变量我们叫first表示我们组串的第一部分这边我复个空串然后在这里呢我就把谁给first呢把这个value叫toString给firstOK那ios的话呢那它说明它是一个它不是一个商品的一个信息它是一个订单的信息那我再订个变量叫second这是一个技巧大家可以不用按到我这个弦
[02:29] 那这个地方呢我们用这个second来记住value.toString好这个写完之后呢也就是说我们的first和second都有了有了之后呢接下来呢我们来看我们要去把我们的KLV2变成K3V3这个时候我们需要做一件事情那我们呢只需要把first和second拼接那是不是就变成V3了而我们的K3呢
[02:59] 还是原来的k所以说呢我们可以这样想contest.write然后呢这个地方呢我们写什么呢我们来写我们的k这个还是我们的原来的k2变成k3而这个v3呢实际上就是first加上second我们可以这样做我们可以new一个testnew一个test然后呢这里边呢把它俩相加把这两个奏出来相加就是first
[03:28] 加上我可以加个杠T吧杠T然后呢这地方写个second好我们来这样去做一个拼接就行了但是还有一种情况你比如说刚才我们在去核的时候呢有可能呢有些数据呢它是没有这个有些订单它是没有对应的商品那这地方是不是应该补闹啊这个怎么处理呢我们可以这样做如果说呢我判断一下如果说你的first
[03:56] 你的first.ecos它是一个空串就是没有数据没有数据怎么办呢我就给你我就把这个呢再复制一份进来我给你这个first补一个空串囊补一个空串囊那如果说你这个first都有数据呢我就把这两个呢相加这样呢应该就没有问题了这是我们这个代码这个整个的话呢其实就是v3变成k3而这个k2
[04:26] K2变成K3然后把集合的数据编列编列完之后把它的值相加相加完之后做为V3如果说没有商品的这一列那我不成道OK这个代码就写完了写完之后接下来我们来写我们的主方法OK那我先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Hadoop MapReduce 中编写一个 Reduce 端的连接（Join）操作，通过自定义 Reducer 类来处理键值对数据，实现两个数据源的关联。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示项目结构，当前编辑的是 ReduceJoinReducer.java 文件，位于包 cn.itcast.mapreduce_reduce_join 下。
画面 2：在 ReduceJoinReducer.java 中，导入 org.apache.Hadoop.mapreduce.Reducer 并声明类继承 Reducer。
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
import org.apache.Hadoop.mapreduce.Reducer;
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

