# 3-MapReduce-Combiner规约-代码实现

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\3-MapReduce-Combiner规约-代码实现【海量资源尽在 ubkz.com】.mp4
- 时长 13分33秒（音频 813s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在讲完规约的基本原理和概念之后呢接下来呢我们通过代码的方式给大家演示一下这个案例呢我就还是利用我们讲的这个word count案例来给大家演示一下好了那这个我们先在这里呢建一个model建个model我们来next没有附模块好这里面我写个de04然后呢我们今天还是myproduce
[00:35] 然后我们写一个combiner3m1combiner把这个名字修正一下OK点finish首先我们先把这个POM文件给它拷过来站下去接下来我们是这样的我们直接把上次写的word.com的案例直接拷贝过来OK这个地方我先这样我直接把上次这个代码直接把这个加文这里面的这个包
[01:17] 可以直接拷过来拷过来之后呢粘在我们今天的代码里边稍等这里边就有了有了之后呢这个排序我就不要了这个myproject这就是我们的word count这个分区呢我也不要了那分区不要了之后呢这个地方分区的类我也不再设了好了我们只讲规约好这个代码写完之后呢这个reduce个数我还是设成more than的OK这个写完之后呢是这样的
[01:50] 我先给大家演示一下没有规约的时候它的一个数据的处理的一个方式然后再加上规约之后我们看看它的数据处理呢或者数据传输呢有没有提高它的效率OK那接下来呢我们来做这个事情首先呢这个是原始的一个word count案例我呢在这里呢我看一下有没有需要修改的地方word count out那这个路径呢我就不改了
[02:20] 然后呢我直接把我这个代码呢进行一个打包先清理一下对了我再去打包这个D04这个代码我们在这里我们直接呢对D04打包稍等好稍等好打包完成这个是我们原始的一个一个单次统计我呢把这个包呢直接拷贝一下放在我们的桌面上好接下来呢我们来上传一下在上传之前呢
[03:04] 我看看我的HDFS看一下我的HDFS这个在HDFS里边呢有一个文件我们来看一下好打开这个HDFS在这个里边呢根目录下面我们word count用的是word count里边有word count.txt这个里边的单词呀我给大家稍微做一个修改我先把它删掉HDFSDFS-RM然后呢word count下面一个
[03:34] word count.txt好 我先把它删掉好 删掉之后呢我再新建一个新的word count.txt我在这里呢我们来看hello 倒号word然后呢这个地方hello 倒号然后Hadoop我故意呢多写一些重复的数据word这个地方呢hello然后呢Hadoop然后这个地方呢还有一个什么呢还有wordOK 那我就这样写写完之后呢
[04:07] 我再把它重新上传到这个里边去重新上传到word count重新上传到这个目录稍等好重新上传之后我们来检测一下啊刷新一下好已经有了有了之后呢接下来我开始运行我的程序好在这里呢我们来看我们给它上传一下我们刚才这个包再上传一下这个地方04好上传之后呢我们来开始运行
[04:46] 这个Hadoop加D04然后呢直接写上我们的主类的一个全路径名拷贝一下在这粘贴好大家请看这个输出我们主要是看这个这个地方他说目标目录已经存在了我把它删掉我找一下我刚才这个命令我们要去把word countout这个目录删掉没有写错了
[05:24] 好上完之后呢咱们来开始再来运行走大家主要是看那个日志的一个这个计数器的一个输出稍等好这个地方呢呃稍等他报错了报错之后我来看一下这个为什么错了这地方报了一个错误他说哦这个还是这个还是这个时钟同步的问题应该是一个时钟同步的问题这样我把那个时钟的手动同步一下呃在这里
[06:03] curve table-1里边有这么一句话我手动来执行一下手动手动同步一下稍等我要连个网我们来连个网之后我们来执行一下稍等好同步过了那接下来在这个我们来同步一下好在这个也始终同步一下走好走完之后呢接下来我们来继续把那个输出目录再删一次好删一次之后呢我们再执行这个
[06:40] 这个world count案例这个这次应该也没有问题了稍等好map呢把这摆来让它执行reduce好执行完了执行完之后我们要看哪里呢这是我们原始的一个world count我们向下翻有个计数器这个地方计数器呢你看这个地方有一个reduce input recourse什么意思呢要是这个地方呢我们收集的这个记录数呢是8个8个
[07:12] 而我们输出的是三个注意记住这个reduce input word count是八个我在这里呢我们来截个图大家记住这几个这个数量这个数目啊OK那还有呢把这个呢我先去把它放在这个位置做一个做一个记录上面我们还要看一个什么东西呢我们来看OK那就记住这个我们只记住这个一个reduce一个输出
[07:44] 还有reduce一个输入和输出那接下来呢我们把这个代码呢加上归约归约完之后呢我们再去看这个结果看看有没有把这个效率呢给提高了怎么加归约呢归约咱们刚才说过了我们需要呢去写一个类这个类呢也需要去继承一个reducer所以说我再写个类这个类叫什么名字呢我们来看讲义这个地方呢我们可以写个mycombiner来写个mycmbi
[08:15] N1combiner额点OK那它需要去继承什么呢combiner继承reducer它其实就是reducer那这个地方呢这个reducer里面继承reducer之后呢这个地方要写成K2V2K3和V3的一个类型那我们来看看reducer里面你以前怎么写你可以把这些东西呢直接拷贝过来OK直接拷贝过来好放在这个位置
[08:45] 好考辨完之后呢接下来我们需要重写这里边的reduce方法重写reduce方法重写reduce方法之后呢reduce方法里边干干什么事情呢你可以这样理解我们reduce要干什么事情你可以在这个归约中呢提前把这个事先做一下所以说呢我们认为啊这个reducer中该干的事情呢我们可以直接把它拿过来直接把它拿过来直接全部复制然后呢复制完之后呢
[09:16] 直接粘贴好我们的规约代码就行了这就是规约而这个规约这个代码呢是每一个map task都会执行而刚才你这个reducer呢是在最后一次做一个全局的汇总它的执行位置是不一样的我做完这个之后呢你看我做了什么事呢我去便利这个集合那便利完之后呢我把所有的腰呢进行相加就相当于我画这个图里边呢我将这些所有的腰进行相加相加完之后呢
[09:46] 把这个结果呢直接传给Reduce那它就会减少我们网络传输的一个数据量来 行了 行了之后呢我们接下来再来做一件事情你指定完规约之后呢需要在主方法里边呢在这个D3456的时候呢需要去指定我们的规约类就设置我们的规约类怎么做呢我们可以用job.sidecombinerclass
[10:17] 然后有个mycombiner第二classOK写完了写完之后接下来我们再打个包我们把它clean一下再重新上传好package稍等好打包成功打包成功之后把这个包拷贝一下然后放到桌面上好回到我们的集群里边来我重新给它上传这个D04我就删掉了D04
[11:00] 然后呢这个地方-f直接删掉删掉之后呢把它再重新上传一次好上传完之后呢我们来首先还要把输出目录给删掉我们直接用刚才这个把输出目录删掉好删掉之后呢我们再重新执行还是刚才这个命令一模一样走来这个时候我们来再看它的一个输出结果稍等好mapmap100%稍等
[11:41] 好Reduce version版好接下来咱们又看到一些计数器咱们再来这里看一个计数器我们来看我们来看这个地方好那这个地方呢我截个图来后面刚才的做一个比较应该是OK应该是这个位置应该是这个位置好粘到我们刚才的这个图里边大家看左边呢是我们没有使用规约的时候它的一个情况左边是
[12:14] 没有使用规约而我们右边呢是使用了规约那大家会发现一个明显的一个现象当我没有使用规约的时候呢我们Reduce它收到的一个输入的一个记录数是8条也就是说在网络中传输我拿到的是8条而使用了规约之后呢我们Reduce就在收到的一个记录数是3条那你
[12:45] 可以得出一个很明显的结论相当于我们经过规约之后我们的网络传输的数据量是不是大大减少了有8条那么减少到3条为什么它会减少呢很简单看我刚才我给大家说了本来你这个地方呢是要去这样先后传那么你把它规约了之后呢相当于把这三个合并在一起那这个时候呢它的数据量就大大减少了OK所以说呢我们使用规约之后呢它的效率提升还是很明显的OK我们总结一话
[13:15] 规约可以去减少我们在MAP阶段向Reduce阶段传输的数据量来提高我们网络传输效率OK那么这就是规约的一个整个的一个知识OK关于规约呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Hadoop MapReduce 中 Combiner 的作用、实现步骤及与 Reduce 的区别，并通过代码和流程图对比演示使用 Combiner 前后的数据传输和处理效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了课程 PPT 的标题页，内容为“Hadoop Day 04”，并列出了本节内容：1. MapReduce 中的计数器、2. 约定 Combiner、3. 低置信度。
- PPT 中详细介绍了 Combiner 的作用：对 map 端的输出先做一次合并，以减少 map 和 reduce 节点之间的网络传输，提高网络 IO 性能。
- 列出了 Combiner 的关键点：是 MR 框架中 Mapper 和 Reducer 之外的一种组件；其组件的父类是 Reducer；运行位置在每个 maptask 节点；作用是每个 maptask 输出的中间结果做局部汇总。

画面2：
- 展示了 IntelliJ IDEA 中的 Maven 项目结构，项目名为 “day04_mapreduce_wordcount”。
- 显示了 `pom.xml` 文件中的依赖配置，其中包含：
  ```xml
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>
  <repositories>
      <repository>
          <id>cloudera</id>
          <url>https://repository.cloudera.com/artifactory/cloudera-repos/</url>
      </repository>
  </repositories>
  <dependencies>
      <dependency>
          <groupId>org.apache.Hadoop</groupId>
          <artifactId>Hadoop-common</artifactId>
          <version>3.1.1</version>
          <scope>provided</scope>
      </dependency>
  </dependencies>
  ```

画面3：
- 展示了 `JobMain.java` 文件中的代码，用于设置 MapReduce 作业的配置。
- 代码中设置了 Reducer 类、输出键值类型、输出路径等：
  ```java
  job.setReducerClass(WordCountReducer.class);
  job.setOutputKeyClass(Text.class);
  job.setOutputValueClass(LongWritable.class);
  job.setOutputFormatClass(TextOutputFormat.class);
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount"));
  boolean b = job.waitForCompletion(true);
  ```

画面4：
- 展示了电脑桌面，有“黑马程序员”和“博学谷”的标志，以及一些文件图标，如 `day03_map...`、`MapReduce.bmp` 等。

画面5：
- 展示了 SecureCRT 中的 Linux 命令行界面，用户在 `software` 目录下执行 `rz` 命令上传文件。
- 弹出的文件传输对话框显示了上传文件的选项。

画面6：
- 展示了 SecureCRT 中的错误日志，显示了 Hadoop YARN 的异常堆栈信息，主要涉及 `SerializedExceptionPBImpl` 和 `ContainerLauncherImpl`。

画面7：
- 展示了 SecureCRT 中的命令行界面，用户执行了 `ntpdate` 命令同步时间，并删除了 HDFS 中的 `wordcount_out` 目录：
  ```bash
  crontab: no changes made to crontab
  [root@node01 software]# /usr/sbin/ntpdate ntp4.aliyun.com
  2 May 12:55:27 ntpdate[33435]: step time server 203.107.6.88 offset 40564.628326 sec
  2 May 12:55:37 ntpdate[33438]: adjust time server 203.107.6.88 offset -0.019597 sec
  [root@node01 software]# hdfs dfs -rm -r /wordcount_out
  ```

画面8：
- 展示了 MapReduce 作业的执行结果，显示了 Map 和 Reduce 的输入输出记录数、字节数、GC 时间等统计信息：
  ```
  Map input records=4
  Map output records=8
  Map output bytes=114
  Map output materialized bytes=136
  Input split bytes=107
  Combine input records=0
  Combine output records=0
  Reduce input groups=3
  Reduce input records=8
  Reduce output records=3
  Spilled Records=16
  Shuffled Maps=1
  Failed Shuffles=0
  Merged Map outputs=1
  GC time elapsed (ms)=214
  CPU time spent (ms)=2670
  Physical memory =659763200
  ```

画面9：
- 展示了 IntelliJ IDEA 中的 `JobMain.java` 文件，用户正在创建一个新类 `WordCountReducer`。
- 代码中设置了 MapReduce 作业的配置，包括设置输入输出格式、Mapper 和 Reducer 类等。

画面10：
- 展示了 `WordCountReducer.java` 文件中的代码，用于实现 Reduce 方法。
- 代码中定义了 `reduce` 方法，用于遍历值集合、累加值、写入上下文：
  ```java
  protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException {
      long count = 0;
      //1:遍历values集合
      for (LongWritable value : values) {
          //2:将集合中的值相加
          count += value.get();
          //3:将结果写入上下文中
          context.write(key, new LongWritable(count));
      }
  }
  ```

画面11：
- 展示了 `JobMain.java` 文件中的代码，用户正在设置 Combiner 类。
- 代码中设置了 Combiner 类为 `MyCombiner`，并设置了 Reducer 类和输出键值类型：
  ```java
  //第七步：设置的Reducer类
  job.setReducerClass(WordCountReducer.class);
  //设置Reducer的个数
  job.setNumReduceTasks(1);
  //第八步：设置输出类
  job.setOutputFormatClass(TextOutputFormat.class);
  //设置输出的路径
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount"));
  ```

画面12：
- 展示了 SecureCRT 中的命令行界面，用户执行了 `rm` 命令删除了本地的 JAR 文件，并使用 `rz` 命令上传了新的 JAR 文件。
- 命令行显示了文件传输的进度和最终的文件列表。

画面13：
- 展示了 MapReduce 作业的执行结果，显示了 Map 和 Reduce 的输入输出记录数、字节数、GC 时间等统计信息：
  ```
  Total vcore-milliseconds taken by all reduce tasks=4814
  Total megabyte-milliseconds taken by all map tasks=4472832
  Total megabyte-milliseconds taken by all reduce tasks=4929536
  Map input records=4
  Map output records=8
  Map output bytes=114
  Map output materialized bytes=55
  Input split bytes=107
  Combine input records=0
  Combine output records=3
  Reduce input groups=3
  Reduce input records=8
  Reduce output records=3
  Spilled Records=1
  Failed Shuffles=0
  Merged Map outputs=1
  ```

画面14：
- 展示了流程图，对比了“没有使用规约”和“使用规约”两种情况下的数据传输过程。
- 图中显示了三个数据节点（dn1、dn2、dn3）分别通过 MapTask 处理数据，然后通过网络传输到 ReduceTask。
- “没有使用规约”时，Reduce 输入记录数为 8，输出记录数为 3。
- “使用规约”时，Reduce 输入记录数为 3，输出记录数为 3。
- 图中还显示了 Combiner 在 MapTask 后对数据进行局部汇总，减少了网络传输量。

