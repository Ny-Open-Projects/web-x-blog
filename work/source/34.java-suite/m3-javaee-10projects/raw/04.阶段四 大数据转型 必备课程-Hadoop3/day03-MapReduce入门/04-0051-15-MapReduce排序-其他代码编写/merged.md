# 15-MapReduce排序-其他代码编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\15-MapReduce排序-其他代码编写【海量资源尽在 ubkz.com】.mp4
- 时长 13分0秒（音频 780s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好实现这个比较规则之后呢接下来我们来把这个剩余代码写完先写Mapper这个Mapper呢首先我们要去继承一个Mapper这里边呢有四个范形前两个是K1和V1那K1呢那这就是我们的行片音量是什么呢是Long WriteableOK那么V1呢是每行的数据是不是test关键是这个K2和V2怎么写来看这个图
[00:33] 我们的K2是一个加热并对象V2是一行数据所以说这个K2是我们刚才写的pairpair writeable这是我们的K2而我们的V2是一行数据叫testOK这是我们的K2K1V1K2V2好拿到这个之后我们来重写map方法这是我们的K这是我们的V接下来关键是什么呢
[01:02] 我们如何将我们的K1和V1转成K2和V2大家请看K1V1是这个而K2V1是这个那怎么去把它变成K2呢你看我们拿到这个V1之后我们是不是可以做一个组串切割对不对做一个组串切割之后呢我可以把这两个值是不是分别封装成一个加热并对象作为K2OK 咱就这样做咱拿到这个
[01:31] 这个是一个value其实就是一行数据来我们来对每一行数据对每一行数据进行拆分拆分然后封装到pairpair-refable对象中就行了然后呢作为谁作为kr好那我们来做value来拆分一下splitvalue我们要先变成字幕串
[02:09] 点toString然后点split用什么拆分呢我们可以用杠T比如说我们放到这个文本中的数据放到我们的数据我们可以用杠T来做分割OK那这里边拆分拆分完之后这里边有两个数据两个成员那把它分别封装到这个对象里边去我们来new这么一个对象new这个对象叫new个pair-writablenew个pair-writable
[02:42] OK拿到这个对象之后呢接下来呢我们来开始去给它封装数据那pair writableset我们来先set firstfirst是不是就是我们的split几啊0对吧从这里边拆分完之后呢每一行数据两部分第一部分是first那第二呢是secondpair writable第二set second好这个是split1
[03:12] 好这样就封装好了好这个地方呢它报错因为我们拆完之后它是一个字符串是吧它是一个综串要把它变成整数咱调个integer.parthint好把这个综串扔进来就可以了好扔进来之后呢就封装完了封装完之后呢接下来第二步将将什么将k2和v2写入上下文中写入上下文中
[03:44] OK就是context.write首先care谁呢care就是pair就是我们的pair write tablev2呢v2你可以把我们这一行的文本数据给它value可以写这一行的文本数据还是这一行的文本数据OK那到这里为止呢我们的map就写完了就这么简单其实就是把我们的kv封装成一个对象变成k2和v2
[04:14] 好写完之后呢接下来咱们再写这个reducer这个reducer我们要去继承一个什么呢reducerreducer那我reducer呢我们的K2和V2还有K3V3的类型K2呢是我们的pair是我们的pairpair rate table那V2呢是我们的test也就是一行的数据而我们的K3呢先打个包啊我们的K3呢同学们
[04:46] 看我们的K3和V3我们的K3和V3呢分别是这个加入并对象还有个NORETABLE来咱们来继续写那就是PAIR这个地方呢PAIR然后呢写个NORETABLE这个NORETABLE呢其实就是一个空类型没有什么意义就是一个占位符OK 写完之后呢我们来重写REDUCE方法在这里呢大家注意在这个REDUCE方法里面呢其实我们呢
[05:17] 不需要干太多事情我们只需要啊将我们这个K2V2转成K3V3直接写到上下文中就可以了来我们来context.write直接把我们的这个什么呢直接把我们的一个K向后写然后这个这个value呢直接写个now这个直接写的什么呢写一个我们来看写个now write table你还不能直接写write table
[05:47] 要调一个方法叫get这个get呢其实就是获取这个类的一个对象也就是个空对象OK这样一写呢实际上我们的k3呢就是原来的k2对不对而我们的v3呢其实就是个空这个radius就写完了就这么简单好写完了之后呢这里还有一个小问题什么小问题呢我们来看假如说呢同学们假如说这个地方有两个a1那有两个a1如果有两个a1的话呢
[06:17] 那这个时候呢注意这个集合中是不是也有两个A1啊就相同的键呢它会放在同一个集合那我们在输出的时候呢输出的时候注意这里边应该是只有一个A1只有一个A1所以说呢如果说你有多个相同重复的一些K3呢为了让它们都输出呢我在这里可以这样做这不有个集合吗你看如果你有两个A1这个数据什么样子呢我们来简单描述一下比如说呢A1
[06:46] 这是一个加弯并对象然后呢OK那再一个AE再一个AE那注意这两个AE呢会合并成一个集合这个合并成一个集合之后呢集合长这样子就是AE你可以认为逗号AE这样子那好这样子的话呢意味着呢AE有两个那如果说你直接这样向后写的话其实只写了一个那怎么样把这两个都写出来呢我们可以变这个集合变了一个
[07:16] 那我们呢就写一次K变了一个我们就写一次K这样子你不管有多少个重复的AE我是不是都能输出啊所以说我们这样子还是这样子我们去变了一下这个集合好这个集合里面呢其实并不重要它的内容并不重要那么我们重要的是呢我们需要将这个K啊多写几次是不是就可以了OK那我们就先写到这里这个时候就完成了完成了之后呢接下来呢
[07:45] 我们把这个呢写完之后我们还需要写一个主方法把这个呢串在一起这个主方法是一个固定的模板我们先去继承一个configure的然后呢需要去实现一个接口叫to这个to这个接口OK好实现这个接口之后需要重写一个方法然后还要写一个写一个主方法那在主方法中写什么代码呢这个代码呢首先呢我们有个类
[08:14] 叫toRunner这个方法叫Run它要启动启动一个任务那这里边有一个Configuration我们在这里呢需要去new一个Configuration对象好然后呢生成一个Configuration把这个Configuration放在这里那这个地方呢它需要一个什么呢它需要一个我们来看它需要一个to这是一个接口它的实现类对象好稍等回到这里所以说呢我们这个
[08:44] 交波闷刚好是这个to的接口实现类所以说我new一个交波闷就可以了而第三个呢它需要一个一些参数我可以把args直接传给它好给它给它之后呢我们来生成一个抛个异常我们来生成返回值这个返回值呢表示我的任务执行成功还是失败那这个地方我们再写个程序的一个进程推出exit如果说你是0表示正常如果非0表示异常
[09:14] 我就把run给他OK这个man方法就写完了写完之后呢我们开始写这个run方法因为你启动这个任务的时候他就会掉这个run而这个run方法的写法呢和我们之前呢是一样的之前是一样的所以说呢我们可以把之前的代码呢全部拷贝过来全部拷贝过来当然我可以再给大家写一下比如说第一步干嘛呢我们需要去通过一个叫步来去创建一个任务对象
[09:44] 叫get instance那这个地方呢这个configuration呢其实就是你这里的configuration如何获取呢我们可以通过复利shopper.getconf而这个是任务的名字这个任务的名字你可以随便写比如说我写个map reduce consultOK那么这样子我们就获得了一个job对象拿到这个job对象之后呢我们需要对这个job呢做一些一连串的一些设置
[10:14] 也就是一共有八个步骤这里呢我可以把之前这个Job呢里边一些东西呢直接拷贝过来我们来看好我把这个全部拷贝过来好拿过来之后呢我们直接粘在这里把后边这个干掉好我们来看这里边呢哪些需要修改打包的时候呢在集群运行时需要做个配置这个就是set加byclass这个地方呢我们要写我们自己的这个Job们所以说呢
[10:44] 我们这个地方应该干掉我们要去写我们自己的教门OK就是它好写完这个之后呢接下来我们看我们的input format我们设置读取文文件的类呢就是这个test input format而我们读取文件的位置呢这个地方我们要改改比如说我们在集群的哪个目录呢我们来写个目录吧比如说input下面有一个叫sort好吧我待会给大家创建这么一个目录
[11:15] 叫sort排序的意思好这是改完了改完之后呢接下来我们看设置Mapper我们的Mapper叫什么呢我们的Mapper叫sort Mapper我拷问一下这叫sort Mapper而我们的K2和V2的类型呢我们来看一下我们K2是一个什么类型呢K2是一个加热并V2是一个test所以说呢K2应该是这样写pairpair writeable第二classV2呢是一个test
[11:45] OK也是一行的数据我们这里要跟着改而这个地方呢我们这里没有用分区我可以把这个分区呢做点这个排序呢你不用设它会自动去进行排序的所以说不用做任何设置而这个Reducer呢我们的Reducer呢是这个Sort Reducer我们直接把它改一下Sort Reducer我们的这个K3 V3呢我们的K3呢还是PairPair呢这个地方Retable
[12:15] 也是这个加完并对象而我们的V3呢是一个not readableOK写完了写完之后呢reduce个数呢我们因为没有分区所以说我们reduce个数不用设把它干掉不用设默认是一个设置输出呢还是这个而设置这个输出的路径呢这个我们还可以用我们应该换一个比如说我在根目录下边呢创建一个创建一个out
[12:44] out下面有一个叫sortOK这个就写完了写完之后呢接下来我们只需要把这个代码呢放在集群上然后呢打包运行就可以了好那这个代码呢我就先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Hadoop MapReduce 编写一个自定义排序程序，包括自定义 Mapper、Reducer 和 Job 配置。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，当前编辑的是 SortMapper.java 文件，位于 cn.itcast.mrproduce_sort 包下。
画面2：在 SortMapper.java 中导入 Hadoop 相关包，并定义类 SortMapper 继承 Mapper<LongWritable, Text, PairWritable, Text>。
画面3：展示 MapReduce 的执行流程图，包括 Map、Shuffle、Reduce 阶段，以及自定义的 PairWritable 类实现 WritableComparable 接口。
画面4：在 SortMapper.java 中编写 map 方法，对输入的每一行按空格分割，将第一个字段作为 key，第二个字段作为 value，封装成 PairWritable 对象。
画面5：在 SortReducer.java 中定义类 SortReducer 继承 Reducer<PairWritable, Text, PairWritable, NullWritable>。
画面6：在 SortReducer.java 中设置输入和输出类型，输入为 PairWritable 和 Text，输出为 PairWritable 和 NullWritable。
画面7：展示 MapReduce 执行流程图，包括 Map、Shuffle、Reduce 阶段，以及自定义的 PairWritable 类实现 WritableComparable 接口。
画面8：在 JobMain.java 中导入 Hadoop 相关包，并定义类 JobMain 继承 Configured implements Tool。
画面9：展示 ToolRunner 类的源码，用于解析命令行参数并设置 Configuration。
画面10：在 JobMain.java 中编写 run 方法，创建 Job 实例并设置相关配置。
画面11：在 JobMain.java 中编写 main 方法，创建 Configuration 实例，调用 ToolRunner.run 方法执行 Job。
画面12：在 JobMain.java 中设置 Mapper 类为 SortMapper，设置 Map 阶段的输出类型为 K2 和 V2。
画面13：在 JobMain.java 中设置 Reducer 类为 SortReducer，设置 Reduce 阶段的输出类型为 K3 和 V3。
画面14：在 JobMain.java 中设置 Reducer 类为 SortReducer，设置 Reduce 阶段的输出类型为 K3 和 V3。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Mapper;
```
画面4：
```java
protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    //对每一行数据进行拆分，然后分别找到PairWritable对象，作为key和value
    String[] split = value.toString().split("\t");
    PairWritable pairWritable = new PairWritable();
    pairWritable.setFirst(split[0]);
    pairWritable.setSecond(Integer.parseInt(split[1]));
    //将K1和V2写入上下文中
```
画面5：
```java
import org.apache.Hadoop.mapreduce.Reducer;
```
画面6：
```java
import org.apache.Hadoop.mapreduce.Reducer;
```
画面8：
```java
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.conf.Configured;
import org.apache.Hadoop.util.Tool;
import org.apache.Hadoop.util.ToolRunner;
```
画面10：
```java
public int run(String[] strings) throws Exception {
    Job job = Job.getInstance(super.getConf(), "mapreduce_sort");
    job.setJarByClass(JobMain.class);
    job.setInputFormatClass(TextInputFormat.class);
    TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/input/sort"));
    job.setMapperClass(SortMapper.class);
    job.setMapOutputKeyClass(PairWritable.class);
    job.setMapOutputValueClass(Text.class);
    job.setPartitionerClass(PartitionerOwn.class);
    job.setReducerClass(SortReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(LongWritable.class);
    job.setNumReduceTasks(2);
    job.setOutputFormatClass(TextOutputFormat.class);
    TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount_out"));
    boolean b = job.waitForCompletion(true);
    return b ? 0 : 1;
}
```
画面11：
```java
public static void main(String[] args) throws Exception {
    Configuration configuration = new Configuration();
    int run = ToolRunner.run(configuration, new JobMain(), args);
    System.exit(run);
}
```
画面12：
```java
//第二步，设置Mapper类
job.setMapperClass(SortMapper.class);
//设置Map阶段的输出类型：K2 和V2的类型
job.setMapOutputKeyClass(PairWritable.class);
job.setMapOutputValueClass(Text.class);
//第三、四、五、六步采用默认方式（分区，排序，规约，分组）
job.setPartitionerClass(PartitionerOwn.class);
```
画面13：
```java
//第七步，设置定义的Reducer类
job.setReducerClass(SortReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(LongWritable.class);
//设置Reduce的个数
job.setNumReduceTasks(2);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：标题为“MapReduce执行流程图”，包含输入文件、Map阶段、Shuffle阶段、Reduce阶段。
输入文件指向 Map 阶段，Map 阶段指向 Shuffle 阶段，Shuffle 阶段指向 Reduce 阶段。
画面7：标题为“MapReduce执行流程图”，包含输入文件、Map阶段、Shuffle阶段、Reduce阶段。
输入文件指向 Map 阶段，Map 阶段指向 Shuffle 阶段，Shuffle 阶段指向 Reduce 阶段。

5) 不要评价画面美观，不要输出与课程无关的内容。

