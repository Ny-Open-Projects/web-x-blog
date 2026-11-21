# 18-MapReduce-Reduce端join操作-集群测试

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\18-MapReduce-Reduce端join操作-集群测试【海量资源尽在 ubkz.com】.mp4
- 时长 5分55秒（音频 355s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来呢我们来写我们的JobMand好打开JobMand我们还是把以前的这个JobMand的代码直接拿过来然后呢粘到我们那个代码里面OK好在这里呢我们对这里分别做些修改呃第一个这个地方呢这个Job的名字我们来改成ReduceJob这个打加包的时候做的这个配置呢我们用我们自己的JobMandJobMand
[00:35] 好那还有呢这个是不用动这个输入路径呢我们再换一个我们用我们的这个reduce然后呢刚刚join好就这样这个路径呢还是不存在的我待会呢创建它这个mypar呢用我们自己的这个是reduce join mypar这个K2和V2类型呢都是test好都是test而这个分区呢我们不要直接删掉
[01:07] 这个地方是设置Reduce的类这边用我们自己的Reducer直接站在这里好那这个K3和V3也都是Task这个Reduce个数我们不要默认是一个就行了设置输出类这个地方输出路径我们来换一下我们这地方改成一个ReduceJoin然后Out好那后面这个地方我们
[01:38] 在这里我们还是用我们的脚门好那这个基本上就改完了好改完之后呢接下来我们来做一个测试做一个测试好这里改完了怎么测试呢在测试之前呢我得先准备点数据放到我们的集群上打开我们的这个我们的CRT好在这里呢我先去在在我们的集群上建一个输入的一个路径输入一个目录make dir
[02:08] 在input下面呢我们来建一个这边有一个我写的是刚才写的是什么呢写的是reduce干join建一个目录完了之后呢接下来呢我需要把这两个文件上传上去也就这两个文件稍等一下我们把这两个文件先放到桌面上然后呢把它放在export software这个目录下面然后我们来上传到桌面
[02:45] 找到这两个文件上传中我需要把他们俩上传到我们的刚才建的那个目录下面hdfs-putproduct.txt上传到input下面有一个叫reduce然后呢join还有一个是others在这里上传
[03:23] 好上传完了上传完之后呢接下来我们呢把我们的这个代码呢打成一个加包上传上上来清空一下然后呢打包稍等好打包完成之后呢把这个把这个呢拷贝到我们的桌面上替换再来粘一下替换好然后呢把它上传上来先把这个删掉D04-F小小好上完之后呢我们来去
[04:10] 上传一下在这里呢D04这个好上传之后我们来开始运行这个代码Hadoop加然后呢是D04后面呢跟上我们的这个主目录在这里呢点右键copy reference好粘贴那我们来运行稍等我来运行这个程序让它来执行好稍等好MAP执行完了执完之后呢
[04:48] 执行Reduce好执行完毕执行完之后呢接下来我们来看一下这个结果打开我们的HDFS在根目录下面呢有一个outout里边有一个Reduce Join Out我们来点开看这个文件好稍等打开它好打开之后我们来看这个内容你看这样的话呢这样就实现了我们的功能P001这是我们的K3对吧后面呢是将这个
[05:25] 商品表和订单表呢放在一行P02P02P02而P03呢这个是一个NOW然后后面呢跟的是一个订单好了那么到此为止呢我们就实现了订单表和商品表之间的一个联合插序如果你数据量特别大的时候呢用这种方式呢它可以提高你的处理速度和效率好那么关于Reduce的教研操作呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写并配置一个 Hadoop MapReduce 程序，实现 Reduce Join 操作，并在终端中创建 HDFS 输入目录。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 IntelliJ IDEA 中的项目结构，当前选中的是 `JobMain.java` 文件。
- 代码内容为空，仅显示类声明 `public class JobMain { }`。
- 项目结构中可见 `mapreduce_reduce_join` 包下的 `JobMain`、`ReduceJoinMapper`、`ReduceJoinReducer` 等类。

画面 2：
- 展示了 `JobMain.java` 文件的后半部分代码。
- 代码注释说明“第八步：设置输出类”和“设置输出的路径”。
- 代码内容包括：
  ```java
  job.setNumReduceTasks(4);
  job.setOutputFormatClass(TextOutputFormat.class);
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/flowcount_out"));
  boolean b = job.waitForCompletion(true);
  return b ? 0 : 1;
  ```
- `main` 方法中包含启动 Job 的代码：
  ```java
  public static void main(String[] args) throws Exception {
      Configuration configuration = new Configuration();
      //启动 个任务
      int run = ToolRunner.run(configuration, new JobMain(), args);
      System.exit(run);
  }
  ```

画面 3：
- 展示了 `JobMain.java` 文件的前半部分代码。
- 代码注释说明“第一步：设置读取文件的 K1 和 V1”和“第二步：设置 Mapper 类”。
- 代码内容包括：
  ```java
  import org.apache.Hadoop.extends ToolRunner implements Tool {
  @Override
  public int run(String[] strings) throws Exception {
      Job job = Job.getInstance(super.getConf(), "mapreduce_reduce_join");
      //打包放在集群运行时，需要做一个配置
      job.setJarByClass(JobMain.class);
      //第一步：设置读取文件的 K1 和 V1
      job.setInputFormatClass(TextInputFormat.class);
      TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/input/reduce_join"));
      //第二步：设置 Mapper 类
      job.setMapperClass(ReduceJoinMapper.class);
      //设置 Map 阶段输出类型：K2 和 V2 的类型
      job.setMapOutputKeyClass(Text.class);
      job.setMapOutputValueClass(FlowBean.class);
  ```
- 注释说明“第三、四、五、六步采用默认方式（分区、排序、缓存、分组）”。

画面 4：
- 展示了 `JobMain.java` 文件中设置 Reducer 的代码部分。
- 代码注释说明“第七步：设置定义的 Reducer 类”和“设置 Reduce 阶段的输出类型”。
- 代码内容包括：
  ```java
  //第七步：设置定义的 Reducer 类
  job.setReducerClass(ReduceJoinReducer.class);
  //设置 Reduce 阶段的输出类型
  job.setOutputKeyClass(Text.class);
  job.setOutputValueClass(FlowBean.class);
  ```

画面 5：
- 展示了 `JobMain.java` 文件中设置 Reduce 任务数和输出格式的代码部分。
- 代码注释说明“第七步：设置定义的 Reducer 类”和“第八步：设置输出类”。
- 代码内容包括：
  ```java
  //第七步：设置定义的 Reducer 类
  job.setReducerClass(ReduceJoinReducer.class);
  //设置 Reduce 阶段的输出类型
  job.setOutputKeyClass(Text.class);
  job.setOutputValueClass(FlowBean.class);
  //第八步：设置输出类
  job.setOutputFormatClass(TextOutputFormat.class);
  //设置输出的路径
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/reduce_join_out"));
  ```

画面 6：
- 展示了 `JobMain.java` 文件中设置输出格式和路径的代码部分。
- 代码内容包括：
  ```java
  //第八步：设置输出类
  job.setOutputFormatClass(TextOutputFormat.class);
  //设置输出的路径
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/reduce_join_out"));
  boolean b = job.waitForCompletion(true);
  ```

画面 7：
- 展示了终端窗口，执行 HDFS 命令。
- 命令为：
  ```bash
  [root@node01 ~]# hdfs dfs -mkdir /input/reduce_join
  ```
- 该命令用于在 HDFS 上创建输入目录，为后续 MapReduce 程序准备数据输入路径。

