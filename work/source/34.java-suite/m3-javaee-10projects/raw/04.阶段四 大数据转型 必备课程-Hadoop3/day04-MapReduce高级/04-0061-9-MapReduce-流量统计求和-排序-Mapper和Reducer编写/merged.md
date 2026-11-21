# 9-MapReduce-流量统计求和-排序-Mapper和Reducer编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\9-MapReduce-流量统计求和-排序-Mapper和Reducer编写【海量资源尽在 ubkz.com】.mp4
- 时长 6分52秒（音频 412s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们再写我们的Mapper和reducer我们来先建一个类这个类叫flow count然后sort Mapper在这里我们需要继承我们的Mapper这个ke是我们的long writableve是一行文本数据test而我们的klvr呢kl是我们的什么是我们这四个字段因为我们需要对这个四个字段的某一个列进行排序
[00:32] 所以说我们需要把这四个字段封装成一个flowbin那么这个时候作为K2所以说K2是flowbin而我们的V2我们可以写成手机号这是我们的手机号V2拿到之后我们来重写map方法在这个内部我们需要将K1V1转成K2V2首先这个地方我们先去拿到这个flowbin我们先去new一个flowbin
[01:05] 这个flowbin如何去获取呢是不是需要从这个一行的文本数据进行截取然后呢把它封装到这个flowbin里边就可以了好 那我们怎么做呢我们可以拿到这个value也就是一行数据变成兜串来split的切割我们切割成杠T拿到这个split的之后呢我们先去切割一个手机号出来然后呢再切割出四个字段出来
[01:37] 好我们来签是拆分是获取手机号那作为什么呢作为K2作为V2好那这地方呢我们来看一下用split谁呢用split0索引就是我们的手机号我们单独保存一下吧然后呢分number好那么这个接下来呢我们再获取我们再获取流量的其他字段好接下来再获取
[02:16] 其他流量字段怎么获取呢我们需要还是用这个split这个流量字段呢分别是1 2 3 4那么获取完之后呢我们需要给它封装到flowbin里面去所以说我们来直接调flowbin它的set方法点set一个是upflow然后呢这个地方我们用split的解呢1然后呢这个地方我们可以调个integer
[02:48] 点posint把它扔进来好然后呢依次类推那么再来一个flowbin点setdownflowinteger点posint然后split2再看第三个flowbin点setupcounterflowinteger点posint这里split的解呢是3好再flowbin点setdowncounterflow
[03:25] 那这个地方呢是一个是一个4好那么这个呢我们就把它这个地方是一个Split4那这样子的话呢我们就把这个Flowbeam呢封装好了封装好之后呢这个Flowbeam呢做我们的K2所以这个地方呢获取流量阻断封装Flowbeam作为K2好这个完了之后呢接下来我们做第三步就是将K2和V2
[03:59] 然后呢写入上下文中用说contest.writeK2呢是我们的flowbinV2呢是我们的手机号就是new一个test好直接复文number好那么这个呢我们的map方法就写完了写完之后呢接下来我们来写我们的reducer来在这里呢我们还需要再建一个类这个呢我们来reducer那这个地方呢我们
[04:30] 写一个叫flow count然后呢sort然后呢reducer还是来继承reducer那这个地方呢我们的K2呢是我们的一个flowbinflowbin而我们的V2呢是代表一个手机号task关键是我们的K3和V3怎么去设呢同志们我们来看这个其实在这里呢reducer这个地方呢其实不需要做什么事情因为排序呢
[05:03] 我们已经指定好规则它可以自己排而这个Reducer呢只需要将我们的K2 V2的数据呢写入我们的上下文中是不是就可以了所以说呢大家来想一下这个地方是K2这个手机号是V2那到这个Reduce的时候呢我们可不可以反过来将手机号作为我们的K2然后呢让我们让我们这个作为V那这样的话呢它的好处是什么呢
[05:31] 我们可以把手机号写到前面去然后呢这一列呢中间这一列呢就排好序了所以说我们来这样我们可以把这个地方呢把这个手机号作为k3吧把这个手机号作为k3然后呢我们的flowbin做我们的v3我们的反过来好这样我们来试一下好首先呢在这里写个reduce叫reduce我们来直接用context.write写的时候呢谁是k3呢
[06:02] 这个地方K3其实就是我们刚才的手机号所以说也就是这个我们的手机号我们来看一下我们可以便利集合便利集合来在这里便利一下便利的时候注意这个地方这是一个flowbin而这里边存放的就是手机号这里我们可以只用context.write那么这个value其实就是手机号
[06:32] 而这个这个输出呢这个V3呢其实就是我们的key也就是我们的flowbinOK我们这样来去把它写到我们的上下文中那这样代码应该就可以了好这是我们的reducer那么这样呢我们先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 MapReduce 编写一个对流量数据进行分组和排序的程序，重点是自定义的 FlowBean 类和 Mapper/Reducer 的实现。

2) 按时间顺序列出每张画面的要点：
画面1: 在项目中右键点击 "day04_mapeuduce_combiner" 目录，选择 "Delete" 选项，准备删除该模块。
画面2: 编辑 FlowCountSortMapper.java 文件，定义了 Mapper 类，继承自 Mapper<LongWritable, Text, FlowBean, Text>，并导入了必要的包。
画面3: 在 Mapper 类的泛型中，将输出的 Value 类型从 Text 改为 FlowBean。
画面4: 显示了一个 Excel 文件，内容是原始的流量数据，包含手机号、流量、上下行等字段。
画面5: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面6: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面7: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面8: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面9: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面10: 在 FlowCountSortMapper.java 中，为 FlowBean 类添加了 import 语句。
画面11: 编辑 FlowCountSortReducer.java 文件，定义了 Reducer 类，继承自 Reducer<FlowBean, Text, FlowBean, Text>。
画面12: 在 FlowCountSortReducer.java 中，将 Reducer 的泛型从 Reducer<FlowBean, Text, FlowBean, Text> 改为 Reducer<FlowBean, Text, FlowBean, Text>。
画面13: 在 FlowCountSortReducer.java 中，为 Reducer 类添加了 import 语句。
画面14: 在 FlowCountSortReducer.java 中，为 Reducer 类添加了 import 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面2:
```java
package cn.itcast.mapeuduce_sort;
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mrpackage.Mapper;

public class FlowCountSortMapper extends Mapper<LongWritable, Text, FlowBean, Text> {
}
```

画面3:
```java
package cn.itcast.mapeuduce_sort;
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mrpackage.Mapper;

public class FlowCountSortMapper extends Mapper<LongWritable, Text, FlowBean, Text> {
}
```

画面5:
```java
import org.apache.Hadoop.mrpackage.FlowBean;
```

画面6:
```java
import org.apache.Hadoop.mrpackage.FlowBean;
```

画面7:
```java
import org.apache.Hadoop.mrpackage.FlowBean;
```

画面8:
```java
import org.apache.Hadoop.mrpackage.FlowBean;
```

画面9:
```java
import org.apache.Hadoop.mrpackage.FlowBean;
```

画面10:
```java
import org.apache.Hadoop.mrpackage.FlowBean;
```

画面11:
```java
package cn.itcast.mapeuduce_sort;
import org.apache.Hadoop.mrpackage.Reducer;
public class FlowCountSortReducer extends Reducer<FlowBean, Text, FlowBean, Text> {
}
```

画面12:
```java
package cn.itcast.mapeuduce_sort;
import org.apache.Hadoop.mrpackage.Reducer;
public class FlowCountSortReducer extends Reducer<FlowBean, Text, FlowBean, Text> {
}
```

画面13:
```java
import java.io.IOException;
```

画面14:
```java
import java.io.IOException;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

