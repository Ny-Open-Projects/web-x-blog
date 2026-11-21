# 11-MapReduce分区-代码实现

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\11-MapReduce分区-代码实现【海量资源尽在 ubkz.com】.mp4
- 时长 11分31秒（音频 691s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们就通过代码的方式呢给大家实现这个分区技术好我们来打开ID那如何去实现分区呢要实现分区啊这里边有个非常重要的类这个类我们可以按住Ctrl加N我们来搜一下这个Ctrl类的叫PartnerP-A-R-T-I-T-I-O-N-E-R这么一个类我们来看一下这个类呢它是一个抽象类
[00:30] 我们按住Ctrl加H可以看到这个类呢有很多的一些子类这里面呢其中有一个子类叫HashiPartner这个HashiPartner其实就是我们的默认的一个分区规则我们可以点一下看一下好 我们来看这个HashiPartner呢它有两个范形那这个范形其实就是K2和V2这个类型它继承了一个Partner这里边有个方法叫Geta Partition这个Geta Partition呢
[01:00] 有三个参数这个是K2的类型这个是V2还有呢一个第三个参数这个参数是我们Reduce的一个个数它里边怎么实现的呢它是这样的它拿到这个K2之后呢来获取它的哈希值然后和一个整形最大的值相余余完之后呢再对这个Reduce的个数取模那这样子的话呢你看如果你的K2不一样
[01:29] 那它的哈希值也是不一样的那余上这个整形之后呢它得到一个值得到一个值之后呢接下来呢它对这个Reduce个数取模之后那它会产生一个整形值这个整形值其实就是我们Reduce的一个编号来我们来看假如说你的Reduce个数是三个那它取模之后呢任何数对这个三取模那它的余数是不是都是012OK 012那
[01:57] 假如说呢我的Reduce个数100个那你取模之后呢我的编号就是0到99这个数字呢其实就是我们Reduce的一个编号那这个地方为什么要对这个整形取模呢你可以这样理解这个哈希值呢有可能是一个负数取模之后呢它会把这个哈希值啊变成一个正数好这是一个规则那这个规则符不符合我们的要求呢很显然是不符合的因为我们要统计每个单词出现的次数而且呢我要求呢
[02:27] 当你的单词长度大于5放在一个分区而小于5放在另外一个分区如果用这种方式来讲如果你的单词不一样那你的k是不一样那好那单词不一样它就会产生不一样的一个整形值那产生一个整形值之后那它去去磨之后那它可能会去产生多个分区这个是不符我们要求的我们只要求两个分区一个是0一个是1
[02:56] 接下来我们需要去改变这个规则那改变这个规则怎么办呢很简单我们只需要再去继承partner然后重写getpartition方法就可以了所以说我们来接下来做这个事情首先要实现分区第一步在这里我们来建一个类这个类比如说我们自己写个叫partnerp-i-t-i-o-n-e-r叫own就是我自己的一个partner然后我们也去继承
[03:27] 继承一个partner一个pmtl这个partner一个类接下来我们要指定我们的kl和vr的类型我们的klv什么类型呢我们来看一下kl是一个走串而vr是一个long retable来我们指定一下它是一个test的类型long retable好这个地方倒个包倒包倒包之后呢需要重写这里面的一个guideconpartition一个方法
[03:57] 好这个方法有三个参数我们来分别来解释一下这个text呢表示K2的类型K2这个long retable表示V2好还有一个叫I这个I呢其实是一个reduce的个数这个个数怎么去获取呢这个个数待会呢我们可以通过主方法去设置它
[04:28] 好那比如说我们现在是两个分区那这个值呢就是2那这个里边怎么写呢你看这个方法的返回值是一个int类型你只需要呢告诉我什么时候返回0什么时候返回1就行了为什么返回0和返回1呢因为我们的reduce个数是两个它的编号要么是0要么是1那好来我们来指定规则我们的规则是这样的如果单词的长度OK
[04:58] 单词的长度是大于等于5单词长度啊大于等于5那这个时候呢我们是进入第一个分区那第一个分区呢其实就交给了第一个reduce交给了第一个reducereduce task也就是我们的reduce好那这个时候呢我们注意如果单词的长度大于等于5那是第一个分区交给第一个reduce task那这个reduce它的编号呢
[05:31] 它的编号你认为就是0稍等这个reduce编号是0OK就这么理解那我们来写一下if如果你的这个这是一个kr吗如果kr就是单词吗如果你的kr这个把它变成纵串.length.length如果大于等于5那这个时候呢我们
[06:01] 要去返回一个reduce的编号也就是0我们直接return 0就可以了那else呢else表示呢你小于5那这个时候呢我们来再记一下如果单侧长度是小于5的那这个时候呢我们要进入第二个分区第二个分区呢就第二个reduce task那这个时候呢它的编号是1放大一下ok这个编号1那这个时候我们return什么呢1就可以了好把这个呢
[06:34] 给它干掉好那这样子我们的代码就写完了分区就这么简单只需要告诉我什么时候返回一个0什么时候返回1就行了当然了如果你的reduce tag是三个那你可以返回0 1 2但是你这里只有两个你只能返回0或者1好这个写完之后呢接下来我们还要做一件事情你这个分区虽然写了但是你是不是得告诉我们的教部也就是我们的任务你怎么去分区的
[07:04] 这个时候我们要回到我们的主方法在这个主方法中呢我们要去在第三四五六步呢我们要去做一个设置就是设置我们的分区类就是我们怎么分区的你要告诉我那这个地方呢我们就有一个教步有个方法叫site partition class把我们刚才这个partition old their class
[07:33] 给他OK他就知道我们是在这里做了一个分区规则那么这里还不行因为我们分区是两个分区那两个分区就要用到两个radius接下来我们还要做一件事情还要去设置我们的radius的个数设置radius的个数这个个数呢你可以设几个呢两个那这个地方呢我们用job.set有个叫numberReduceTask这个地方我们写个2
[08:01] 这个呢就可以设置我们Reduce的个数好把这个工作做完之后呢基本上我们的代码就写完了一共三步第一写个类去继承Partener重写这个方法这是第一步第二步呢在MEM方法中呢设置我们的设置我们的Partention的对象这个类OK然后呢接下来第三步我们要去设置Reduce的个数好做完之后呢
[08:27] 我们需要将这个代码重新打成加包然后放在集群上运行接下来我们来打个包先把它以前的清一下clean稍等来我们来打一个加包打完之后我们把这个直接复制一下放在桌面上把它替换替换之后我们来上传到这个software里边RD-1回到这个桌面
[09:09] 把它拿上来好拿上来之后呢我们来开始运行我们的这个jar 包怎么运行呢我们来看我们可以这样子Hadoop架然后呢后面跟上这个jar 包的一个名字后面呢跟上我们这个主类的一个全路径名OK好直接回车我们来运行稍等这个是我们经过分区的一个代码稍等
[09:47] OKMAP正在走这个分区之后呢MAP呢是100%那咱接下来呢就等这个REDUCE好REDUCE也100%OK完成了完成了之后呢我们来看我们的HDFS如果不出意外的话呢我们会出现什么效果呢我们会在这个WORD COUNT里边呢会有两个文件OK你看这个是PART-R00这是PART-R001
[10:24] 上面这个呢其实是什么呢其实是我们的第一个分区下面是我们的第二个分区那么不出意外第一个分区里边放的是不是应该是我们单词长度大于1.5的一个统计结果下面呢是小于5的一个单词统计结果来我们看上面这个来我们当一下稍等把它打开好打开之后我们来看是不是大于1.5OK这里边的单词是不是都是大于1.5
[10:58] 那再看下边这个下边这个我们来点一下再打开看这里边是不是小于5小于5的你看一个Hive一个tom这不是小于5的单次统计说明我们的分区是没有任何问题的OK分区呢其实就是将同一个分区的数据放在同一个radius然后呢不同的radius呢可以产生不同的结果文件好那么关于分区呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过自定义 Partitioner 实现 Hadoop MapReduce 任务中按单词长度进行数据分区，使长度大于等于5的单词分到一个Reduce任务，小于5的分到另一个Reduce任务。

2) 按时间顺序列出每张画面的要点：
画面1：展示单词统计任务的逻辑，输入文件a.txt（300M），要求将单词长度>=5的统计结果放在一个文件中，长度<5的放在另一个文件中。图示了三个数据节点（dn1, dn2, dn3）分别经过MapTask处理后，数据流向ReduceTask，最终输出结果（hello 3, world 2, Hadoop 1）。
画面2：展示Hadoop源码中HashPartitioner类的定义，用于默认的分区逻辑。
画面3：展示自定义Partitioner类PartitionOwn的初始代码框架，继承自Partitioner。
画面4：在PartitionOwn类中，开始编写getPartition方法，使用text.toString().length()判断单词长度。
画面5：完成getPartition方法的逻辑，根据单词长度判断返回0或1，分别对应第一个或第二个ReduceTask。
画面6：在JobMain类中，设置输入格式、Mapper类、输出键值类型。
画面7：在JobMain类中，设置自定义的Partitioner类PartitionOwn。
画面8：展示PartitionOwn类的完整代码，包括字段声明和getPartition方法。
画面9：在JobMain类中，设置Reducer类、输出键值类型，并设置Reduce任务数量为2。
画面10：在终端中使用rz命令上传编译好的jar包到Hadoop集群。
画面11：在终端中查看Hadoop任务提交日志，显示任务执行过程和完成状态。
画面12：在HDFS浏览器中查看文件part-r-00000，显示其Block信息，包括Block ID、Block Pool ID、大小和可用节点。
画面13：在HDFS浏览器中查看文件part-r-00001，显示其Block信息，包括Block ID、Block Pool ID、大小和可用节点。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2：
```java
package org.apache.Hadoop.mapreduce.lib.partition;
import ...
@Public
@EStable
public class HashPartitioner<K, V> extends Partitioner<K, V> {
    public HashPartitioner() {
    }
    @Override
    public int getPartition(K key, V value, int numReduceTasks) {
        return (key.hashCode() & 0x7fffffff) % numReduceTasks;
    }
}
```

画面3：
```java
package cn.itcast.mapreduce;
import org.apache.Hadoop.mapreduce.Partitioner;
public class PartitionerOwn extends Partitioner {
}
```

画面4：
```java
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Partitioner;
public class PartitionerOwn extends Partitioner<Text, LongWritable> {
    Text text; // 表示K1
    LongWritable longWritable; // 表示V2
    int reduce个数;
    @Override
    public int getPart...
    if(text.toString().length() >= 5){
        return 0;
    }else{
        return 1;
    }
}
```

画面5：
```java
@Override
public int getPartition(Text text, LongWritable longWritable, int i) {
    if(text.toString().length() >= 5) {
        return 0;
    } else {
        return 1;
    }
}
```

画面6：
```java
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_wordcount");
        //打包放在私有空间时，需要做一个配置
        job.setInputFormatClass(TextInputFormat.class);
        //第一步：设置输入文件的路径
        TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/wordcount"));
        //第二步：设置Mapper类
        job.setMapperClass(WordCountMapper.class);
        //设置Map阶段的输出类型：K2 和V2的类型
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);
        //第三、四、五、六步采用默认方式（分区，排序，规约，分组）
        //设置我们的分区类
        job.setPartitionerClass(PartitionerOwn.class);
```

画面7：
```java
//第七步：设置文的Reducer类
job.setReducerClass(WordCountReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(LongWritable.class);
//第八步：设置输出类
job.setOutputFormatClass(TextOutputFormat.class);
```

画面8：
```java
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Partitioner;
public class PartitionerOwn extends Partitioner<Text, LongWritable> {
    Text text; // 表示K1
    LongWritable longWritable; // 表示V2
    int reduce个数;
    @Override
    public int getPartition(Text text, LongWritable longWritable, int i) {
        //如果单词的长度 >= 5,进入第一个分区 ——第一个reduceTask ——reduce编号是0
        if(text.toString().length() >= 5){
            return 0;
        }else{
            //如果单词的长度 < 5,进入第二个分区 ——第二个reduceTask ——reduce编号是1
            return 1;
        }
    }
}
```

画面9：
```java
//第七步：设置文的Reducer类
job.setReducerClass(WordCountReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(LongWritable.class);
//第八步：设置输出类
job.setOutputFormatClass(TextOutputFormat.class);
//设置Reduce的个数
job.setNumReduceTasks(2);
```

画面10：
```bash
[root@node01 software]# rz -E
rz waiting to receive.
? a? zmodem ??.
Ctrl+C ??
Transferring day03_mapreduce_wordcount-1.0-SNAPSHOT.jar...
100% 6 KB 6 KB/s 00:00:01 0 ?
```

画面11：
```bash
2019-05-01 11:11:02,835 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/Hadoop-yarn/staging/root/.staging/job_1556425124335_0013
2019-05-01 11:11:03,193 INFO input.FileInputFormat: Total input files to process : 1
2019-05-01 11:11:03,345 INFO mapreduce.JobSubmitter: number of splits:1
2019-05-01 11:11:03,387 INFO Configuration: deprecation: system.metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2019-05-01 11:11:03,615 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1556425124335_0013
2019-05-01 11:11:03,617 INFO mapreduce.JobSubmitter: Executing with tokens: []
2019-05-01 11:11:03,619 INFO conf.Configuration: resource-types.xml not found
2019-05-01 11:11:03,909 INFO impl.YarnClientImpl: Submitted application application_1556425124335_0013
2019-05-01 11:11:04,054 INFO mapreduce.Job: Running job: job_1556425124335_0013
2019-05-01 11:11:04,056 INFO mapreduce.Job: Job job_1556425124335_0013 running in uber mode : false
2019-05-01 11:11:04,056 INFO mapreduce.Job:  map 0% reduce 0%
2019-05-01 11:11:21,496 INFO mapreduce.Job:  map 100% reduce 100%
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：架构图，展示数据从dn1、dn2、dn3流向MapTask，再流向ReduceTask，最终输出结果。
画面6：代码注释中提到“第二步：设置Mapper类”、“第三、四、五

