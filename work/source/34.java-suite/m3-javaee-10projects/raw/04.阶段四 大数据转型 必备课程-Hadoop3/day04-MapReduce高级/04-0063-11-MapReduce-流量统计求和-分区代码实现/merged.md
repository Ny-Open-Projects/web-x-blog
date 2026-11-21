# 11-MapReduce-流量统计求和-分区代码实现

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\11-MapReduce-流量统计求和-分区代码实现【海量资源尽在 ubkz.com】.mp4
- 时长 9分45秒（音频 585s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来看下一个需求这个需求是这样的它说在需求一的基础上呢继续完善将不同的手机号分到不同的数据文件中实现一个自定义分区这个自定义分区呢其实我们以前呢做过在这里呢它要求以以下数字开头的手机号进行分开数据的分开比如说135呢我开头的手机号呢我放了一个分区文件136开头的手机号呢
[00:29] 另外一个分区137然后呢除了这三个之外呢剩余的手机号呢放在其他分区好我们要做这个事情记着我们是在需求一的基础上那么要去做自定义分区呢其实很简单我们需要写一个类比如这个类叫flow partition它需要去继承一个类这个类呢是partitioner然后呢这里边写的是K2和V2的类型接下来呢重写一个get partition方法
[00:59] 好在这个方法的内部呢我们需要根据不同的手机号啊来去返回对应的Reduce编号就行了那大家还记不记得这个是K2V2而最后一个参数呢表示Reduce的个数那你返回的这些01,2,3它其实就是Reduce的一个编号啊那么比如说呢01,2,3说明我有四个Reduce好那接下来呢我们就来实现这样的一个代码
[01:28] 好我们打开我们的ID在这里呢我们在基础在这个需求1的基础上呢进行修改这样子我呢再把这个包啊再复制一份把这个上面这个代码直接复制过来然后进行修改我们呢这个地方这个包contract加Ccontract加V来直接拿过来拿过来之后呢我们来flow count我们来改个名字这个呢
[01:55] 我们再改个名字flow count我再加一个partitionp-a-r-t-i-t-o-n好那这个呢就多出来一个包这样子我们把这个把这个呢复制完之后还不行我把它直接拉到这里好这样就可以了好那做完之后呢接下来呢我们需要在这个基础上呢进行修改好首先呢我们要做一件事情我们在这里需要写一个类
[02:30] 这个类呢就是my或者叫叫partition我们用flow partition好flow partition它需要去继承一个partitioner类这个地方是我们的kl和vr在我们第一个需求案例里边呢大家注意我们的kl呢是手机号大家还记不记得而我们的vr呢是一个flow bin也就是说它包含四个字段的一个flow bin好我把这里导一个包在这内部呢
[03:01] 我们需要去重写一个方法这个方法叫getPotention而在这个方法的内部呢就是判断手机号判断手机号1什么开头1哪个数字哪个数字开头然后然后返回不同的分区编号就行了好怎么去做呢我们知道手机号呢其实就是这个test
[03:33] 我们可以拿这个test来判断if如果这个test.toString以什么开头就start with如果是135开头那这个时候呢我的分析编号呢就是0把它放在0号边这个分区然后呢else if如果呢这个test.toString它呢是start with136136那我呢给它放在1号边
[04:04] 这个分区那就是1然后呢elseif如果返回的是test the toString.start位置如果是137好那这个是我们给它返回这个2号分区如果其他的就是else我们return几呢我们return了3ok这个代码就写完了好写完之后呢我们这个分区也写完了大家注意
[04:37] 这个地方呢我们设了四个分区那待会呢你要做一件事情你设reduce的个数的时候呢要设成4或者说比4更多都可以好这个写完之后呢接下来我们要去改动我们的焦闷这个焦闷里边怎么改呢我们这个任务的名字我们也改一下或者加上一个partition好而这个输入的路径呢我就还是用这个输入路径好这个地方呢我们基本上都不变
[05:11] 我看一下这个地方基本都不变然后呢这个地方要设一个reduce的个数我们要去设一下这个地方是job.site number稍等一个site numberreduce tasks这地方我们设计呢你设四个因为我们有四个分区好 设完之后呢接下来这个输出呀这个路径呢你可以
[05:37] 你可以用这个路径待会呢这个路径还不能存在我们把它删掉好这个就写完了基本上分区呢就是加两个东西一个是我们自己写的一个分区的一个类还有呢我们要指定Reduce的个数对了还有一件事忘记了我们要设置我们分区的一个类这地方忘了一步这job.setpartition bus我们要设置分区类这个分区类呢我们要设成什么呢
[06:06] 叫flowflow partition然后呢dir class好这样一设哎这个就写完了写完之后我们来做一个测试首先呢我们回到这个地方先清空一下清空完之后呢接下来我们来打包再次打包好打包完毕打包完毕之后呢把这个地方呢直接拷贝一下然后呢放在桌面上好放在桌面上之后呢把它放到我们的这个
[06:36] 集群里面去首先呢在这里呢我们先把这个D04先删掉好删掉之后呢来上传一下好上传完之后呢接下来我们来去做测试直接我们来看直接Hadoop用刚才这个命令就行了我们来找到把后面这个主方法这个名字换一下就可以了点这个地方点右键Copy Reference然后在这里好
[07:11] 那这里边呢我要注意一个小问题因为呢我们这个输出路径是存在的我需要呢先把它删掉hdfs dfs-rm-r在这个out下面有一个叫word count然后word count然后一个out先把它删掉这里说呢它说这个目录不存在删错了应该是在根目录下面有一个word count不是word count是这个
[07:44] 叫什么呢我们来看一下吧在我这个代码里边我怎么写的呢我代码里边写的输出路径是这个flowcountout在out下面那我们再把这个地方呢改一下在根目录下面有一个叫out下面一个flowcountout把这个删掉好删掉完之后呢我们来继续运行我们刚才的命令好直接粘一下来回撤
[08:19] 我们来测一下好稍等好map阶段好map百分百接下来reduce好reduce百分之五十你看我这个设的分区设的四个你看它是零二十五百分之五十OK完了完成了我们来去在这里呢我们来去看一下这个输出吧在out下面呢有一个有一个flow count out如果不出意外的话呢这里边应该有四个文件
[09:05] 分别是对应不同分区的一个结果文件我们点开这边有四个第一个分区呢放的是135的我们来看一下是不是我们想要的一个值稍等打开一下这里边就是135那其他的我就不打开了也就是这里边呢就实现了一个分区所有的分区呢就是将满足不同条件的数据呢放在不同的Reduce中而每一个Reduce呢就会产生一个结果文件这是我们分区的目的
[09:39] 那关于这个分区的代码呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Hadoop MapReduce 中自定义分区器，将不同开头的手机号码分配到不同的输出文件中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示需求三“手机号码分区”的说明，以及自定义分区器 FlowPartition 的代码框架。
画面2：展示项目结构，选中 JobMain.java 文件，显示其内容为 MapReduce 作业的主入口。
画面3：在 IDE 中，用户正在编辑 FlowPartition.java 文件，准备编写自定义分区逻辑。
画面4：在 IDE 中，用户正在编写 FlowPartition.java 文件的 getPartition 方法，准备判断手机号开头。
画面5：在 IDE 中，用户正在编写 FlowPartition.java 文件的 getPartition 方法，准备添加 else if 判断。
画面6：在 IDE 中，完成 FlowPartition.java 文件的 getPartition 方法，包含对 135、136、137 开头手机号的判断逻辑。
画面7：在 IDE 中，展示 JobMain.java 文件中设置 Mapper、Reducer、输入输出格式等配置。
画面8：在 IDE 中，展示 JobMain.java 文件中设置 Reducer 的类、输出类型、Reduce 任务数和输出路径。
画面9：在 IDE 中，展示在 Maven 中执行 clean 命令，准备打包项目。
画面10：在 Linux 终端中，用户正在解压 day04_mapreduce_combiner-1.0-SNAPSHOT.jar 文件。
画面11：在 Linux 终端中，用户正在 HDFS 上删除旧的输出目录。
画面12：在 Linux 终端中，用户执行了 Hadoop jar 命令提交 MapReduce 作业。
画面13：在浏览器中，展示 HDFS 上输出文件 part-r-00000 的块信息，显示其分布在 node01、node02、node03 三个节点上。
画面14：再次展示需求三“手机号码分区”的说明和自定义分区器 FlowPartition 的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public class FlowPartition extends Partitioner<Text,FlowBean> {
@Override
public int getPartition(Text text, FlowBean flowBean, int i) {
String line = text.toString();
if (line.startsWith("135")){
return 0;
}else if(line.startsWith("136")){
return 1;
}else if(line.startsWith("137")){
return 2;
}else{
return 3;
}
}
}
```

画面2：
```java
package cn.itcast.mr.flowcount_partition;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Partitioner;

public class FlowPartition extends Partitioner<Text,FlowBean> {
@Override
public int getPartition(Text text, FlowBean flowBean, int i) {
//为手机号以哪个数字开头然后返回不同的分区编号
if(text.toString().startsWith("135")){
return 0;
}else if(text.toString().startsWith("136")){
return 1;
}else if(text.toString().startsWith("137")){
return 2;
}else{
return 3;
}
}
}
```

画面7：
```java
//第一步：设置读取文件的类：K1 和V1
TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/input/flowcount"));
//第二步：设置Mapper类
job.setMapperClass(FlowCountMapper.class);
//设置Map阶段的输出类型：K2 和V2的类型
job.setMapOutputKeyClass(Text.class);
job.setMapOutputValueClass(FlowBean.class);
//第三、四、五、六步采用默认方式（分区、排序、规约、分组）
//第七步：设置文的Reducer类
job.setReducerClass(FlowCountReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(FlowBean.class);
```

画面8：
```java
//第七步：设置文的Reducer类
job.setReducerClass(FlowCountReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(FlowBean.class);
//设置Reduce的个数
job.setNumReduceTasks(4);
//第八步：设置输出的路径
TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/flowcount"));
```

画面10：
```bash
[root@node01 software]# rz waiting to receive.
```

画面11：
```bash
[root@node01 software]# Hadoop jar day04_mapreduce_combiner-1.0-SNAPSHOT.jar cn.itcast.mr.flowcount_partition.JobMain
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“需求三：手机号码分区”，下方列出需求步骤。
画面14：PPT 标题为“需求三：手机号码分区”，下方列出需求步骤。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

