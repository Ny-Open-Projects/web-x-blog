# 14-MapReduce排序-实现比较器和序列化代码

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\14-MapReduce排序-实现比较器和序列化代码【海量资源尽在 ubkz.com】.mp4
- 时长 10分17秒（音频 617s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在讲完这个整个流程之后接下来我们就通过代码的方式呢把这个流程呢给大家实现一下好接下来打开我们的ID在这里呢我再给大家建一个包在这里建个包这个地方呢我们写一个map reduce然后呢我写个salt这么一个包好在这里呢我们还是一样的我们上面呢有一个主类有个Mapper一个reducer我们这里也是一样的
[00:30] 我们在这里建一个建一个类这个类叫Mapper这个类起个什么名字呢我们和讲义保是一致这个Mapper呢我们来看一下叫Salt Mapper那我们也叫Salt MapperOK那接下来还得需要建一个类这个类呢叫Salt Reducer那再建一个类主类这个类还是叫焦门好建完这个之后呢接下来注意
[01:08] 我们还需要再建一个类什么类呢我们刚才说过了要对这个整个实现一个排序我们这个K2呢需要有一个加弯并也就是说我们的排序的一个加弯并所以说呢在这里呢我还需要再定一个类这个类呢我们刚才说过叫什么呢叫pairpair retableokpair retableok那写完这个之后呢咱们依次的把这个代码给大家写完首先呢咱们先写这个pair retable
[01:40] 那这个类里边呢其实封装的就是我们刚才看到这个A1 A9这两个字段那要去实现排序呢它首先要去实现一个接口这个接口呢我们刚才说过叫什么叫这个WriteableWriteable然后呢Compareable是不是WriteableCompareable我们要实现这么一个接口那这里边有个范形这个范形呢还是写PairWriteable
[02:10] 写完之后呢我们还需要重写这里的方法点OK把这个方法重写一下好重写完之后呢你会发现这里边有三个方法一个是compare to这里边呢来定义比较规则的还有一个是write来实现一个序列化read field来实现反序列化我们先来加个注释这个是实现排序规则OK这里边呢
[02:42] 这个方法是实现序列化而这个呢是实现反序列化好有了这个之后呢接下来我们还需要定义两个字段一个呢就是我们刚才说的一个first也就是我们那个a给它定一个private还有一个呢是我们的一个second也就是我们后面那个数字a 9 b 8这么一个数字好写完之后呢我们再去写上它的一个
[03:22] set和get的方法好我们再写个toString方法好这个时候来toString呢我给它修改一下这个整个的一个样子OK这里面我写个杠T吧修改它的toString好在这里呢我们把它修改一下好这个做完了做完之后呢我们接下来看我们要实现排序的话呢我们是不是得指定排序规则呀我们的排序规则是这样的先按照first的排序如果first一样
[04:02] 再按照second的排序那在哪里去实现这个排序规则呢在这里有个Compare to方法我们要在这里实现一个排序规则好那么怎么去实现呢我们来看要去排序是不是有比较我们在这里要实现数据之间的两两比较怎么比较呢我先把这个变量的改成一个other这样大家看的更舒服一点
[04:30] 什么意思呢就是我要和其他对象它的一个值进行比较那我是谁呢其实我这里边有个this那我们来看一下我们有个规则就是先比较什么呢first如果first相同则比较second好 根据这个规则我们先来比较它的first比较得有两个对象第一个对象其实就是this
[05:03] 那this呢是谁呢this first也就是我的first和别人的这个first进行比较因为这个first呢它其实是一个字幕串所以说呢我们比较的话呢我们这个字幕串里边自带的方法也叫compact to注意它是实现一个字幕串的比较OK那和别人的这个first比较别人是other也就是它传进了一个other那么它的一个firstOK那么经过这个比较之后呢它会返回一个整形的值
[05:33] 比如说我给它起个名叫result这个result什么意思呢如果说我的字幕串和它的字幕串相同那它返回值呢它是一个0如果我的字幕串呢大于它的字幕串那它返回是一个太0的值如果我的字幕串呢小于它的字幕串是小0的值那它怎么去比较谁大谁小呢比如说我一个有个有个字幕串是ABC有个字幕串是B
[06:01] B B BOK 这么两个字母串那你看它会先比较第一个字母的阿克斯玛值然后它俩之间的进行相减那你看A的阿克斯玛值是不是小于B呀那这个时候呢大家注意这个时候呢A你认为就小于B它是这样一个比较方式那如果说两个人呢第一个字母都相同都相同的话呢它就会比较第二个那它发现第二个也相同它就会比较第三个那这个时候呢
[06:30] 用C的阿兹玛值减去B那这个时候呢C减去B是不是应该正数那这个时候呢我们认为呢这个时候呢这个组串那它就呢大于这个组串OK它是这样去比的比了完了之后呢我们来看如果说它俩都是ABC那表示这两个组串是相同的相同干嘛呢我们再比较secondOK那这个时候我们这样做if result等于0表示呢
[07:00] 这两个字幕圈是一样的那一样的话呢我们是不是得比较后面这个数字呀这个数字是什么呢别忘了这个数字是不是就后面这个1937这个数字怎么做呢我们再来看数字之间比较非常简单我们直接用this.second就是我的我的这个second减去other.second直接相减是不是就可以了return我们return它OK那好了
[07:31] 你看啊如果说呢它的字符串是相同的它的字符是相同的那接下来呢我去比较它们的第二个数字我的数字减异它那如果说两人相等那就是0否则呢我比它大就是大一0我比它小就是小一0我们这个方法你只需要返回大一0小一0或者等一0只要把这个规则呢告诉我们的比较器它就知道了所以这就是一个比较规则那如果不是相等那肯定是返回result
[08:01] OK这个规则就写好了这个规则写完之后呢他就会先按照first来比OK如果呢first相同再按照second来比那么这样比较的规则其实就是他的排序规则这个排序呢默认其实是一个生序默认是一个生序OK这个写完之后呢我们接下来再向下看这里边还有一个序列化规则什么叫序列化呢就是呢将我们的对象的数据呢
[08:30] 变成一个字节流怎么写呢这个序列化是一个固定的一个操作我们来看一下讲义序列化呢下翻OK这里边序列化呢write只需要去用这个output然后去写一个字幕串或者写一个整数把这个方法一调用就可以了来我们看我们有个data output.write因为呢我们第一个变量是一个字幕串类型所以说呢我这边有个方法叫write utf必须这样写
[09:01] 写谁呢写first而第二个呢它是一个int类型的我们要写writeint写什么写second好这是一个序列化写完了大家要这样写把每个每一个成员面的呢都去调个write方法如果你是字幕串就是utf如果你是int类型就writeint当然了它还有其他类型你看基本上所有的类型它都有好这是一个序列化那反序列化怎么写呢
[09:31] 反序列化其实是一个 read那怎么写呢我们来看一下这个 read 就是首先用 input 就这个变量来调一个 read字幕串就是 read utf如果是一个整形就是 read int那接下来就是 this.first给它复制就是 data input. read utfthis.second然后 data input.read int
[10:00] 好写完了写完之后呢我们的这个自定的这个类呢就基本上写完了那接下来呢我们就可以写我们的Mapper和Reducer好那我们就先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
    WritableComparator<T> (org.apache.Hadoop.io)
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

