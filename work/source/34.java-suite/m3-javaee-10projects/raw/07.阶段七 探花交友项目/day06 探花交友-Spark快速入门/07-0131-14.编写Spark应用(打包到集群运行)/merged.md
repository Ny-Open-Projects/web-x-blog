# 14.编写Spark应用（打包到集群运行）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\14.编写Spark应用（打包到集群运行）_【海量资源尽在 666java.com】.mp4
- 时长 12分10秒（音频 730s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么我们接着继续啊那么前面呢我们已经呢是把我们的WordCon的程序呢就写好了那么我们之前呢所写好的这个程序呢是在本地呢去做一个运行那么这个结果呢是符合我们预期的那么接下来呢我们就需要呢把我们刚刚啊所写的这个WordCon的程序呢去提交到我们的Spark的集群去做一个运行那么接下来呢我们来看一下如何去做运行
[00:29] 那么首先我们需要把我们刚刚所写好的应用去做一个打包那么首先我们需要去修改一下我们的POM文件那么我们是需要在POM文件中在我们的Spark的依赖中我们添加一个它的什么呢Scope改成什么呢Provider
[00:51] 那么为什么要去改成它呢原因就是那么我们这个程序呢我们在最终提交到我们的Spark集群运行的时候那么集群呢已经就为我们提供了这样的一个环境那我们就不需要再把这个相关的依赖的jar 包呢去打到这个包里面来了那么如果要是打进去的话那么就会产生这个冲突这一点大家要注意一下好那么接下来我们来看一下
[01:19] 那么在我们代码这个位置需要做一点小的一些调整那么我们就以它为例那么我们需要把我们set master这个注释掉那么这个是我们在提交到集群之后会自动去我们需要去指定master所以在这一块我们需要把它就去掉我们把代码就注释掉然后加一个分号
[01:45] 好那么这个代码呢这个地方就OK了对吧那么还有一个位置呢是在这个位置去指定我们的这个文件的一个路径啊那么在Linux平台跟Windows的平台的路径呢是不一样的那么我们呢是在这个目录下面是不是在我们的这个根目录下面的itcast下面有这样的一个有这样的一个文件对吧那么我们呢就可以去做这样的一个指定啊比如说我们就可以这样来写
[02:14] 写一个根目录下面的一个itcast下面一个order一个text这样的一个目录但是大家可以想一下如果我们这样去写的话那么是不是我们就把这个路径是不是就写死到我们的代码中了那么比如说我们后面的想要去换一个其他的一些这个目录和文件的话那么是不是就
[02:38] 需要再去修改我们的源码然后再进行编译之后的才可以对不对所以呢这个显然是
[02:45] 不合理了对吧那么我们应该怎么去做呢那么我们是不是来看一下那么这个是我们这个man方法man方法里中呢是不是会有一个参数叫做ax它呢是一个字符创的一个数组那么我们是不是就可以在外部去运行我们这个程序的时候呢来指定这个参数由参数来决定我们的这个文件路径是在哪里那么我们这样的话是不是就
[03:11] 不把我们这个路径呢去印编码到我们的代码中了对不对所以呢这个位置我们是不是应该这样来玩那么就是来一个什么呢args来一个0那么这样的话呢我们就是去传入这个路径就可以了第一个路径呢其实是在我们的这个输入这个位置那么在最后呢其实我们是需要一个输出的那这样吧我们把这个去拷贝一下吧拷贝一下然后呢我们再去做一个修改
[03:39] 那么我们把这个拿掉返回返回吧那么我们把这个呢去给大家来备份一下啊那么这个我们改成这个3吧那么我们就到这个3里面来做一个这个修改吧那把它呢注射掉把这个位置打开然后呢在这呢我们需要改成什么呢改成一个arcsarcs0
[04:02] OK好那么在最后呢我们这个计算的一个结果呢我们其实呢是让他需要去帮我们去输出到一个指定的目录的啊或者说文件啊并不是去做一个控制台的一个打印那么这个时候呢我们来看一下应该怎么去做呢那么在这个位置呢我们就不能够使用这个connect它了啊因为这个呢是去搜集这个最终的数据的那么我们就需要把这个呢就拿掉了那么我们加一个注释啊
[04:30] 叫做保存我们的结果到我们那些指定的目录或者说文件这样的一个操作那么应该怎么做呢就拿到我们上面的这个radiusbykrdd然后点一个叫做salesale as textfile那么同样的它也是需要一个
[04:53] 那么这个路径呢我们也有我们的这个args去做一个传入啊一那么也就意味着我们运行我们这个应用的话至少你是不是需要传入两个参数啊那么第一个参数那就是我们的一个输入就是说我们指定我们这个单词的所在的这个文件的目录在哪里那么第二个呢就是指定我们最后计算完成的一个结果的一个输出
[05:20] OK那么这两个呢我们是需要的好嘞好那么到这里呢我们这个代码呢就修改完成了那么其实可以看一下我们的讲义啊那么讲义中的代码跟我们刚刚所写代码呢基本上呢是一样的那么是在这个位置是不是第一个这个参数在这呢是第二个参数那么接下来呢我们就需要通过我们这个manage去对我们的工程呢做一个打包那么我们来找一下在这个位置呢
[05:45] 找到我们这个生命周期然后呢下面呢有个package那么我们双击一下它那么它呢就会对我们这个项目呢去做一个打包那么打包完成之后呢就会去有一个这样的一个jar 包了那么是在这对吧那我们就可以把这个jar 包呢去上传到我们的这个比如说我们就上传到这个82这个机器上面的根目录下面Lightcast这样的一个目录那么我们来找一下这个目录
[06:13] 找一下这个目录然后呢我们去把它来拷贝一下然后呢我们是不是就去我们看一下啊这个对那么我们就把我们的这个目录去这个文件啊我们来找一下这个文件那么这个文件呢其实呢我们是在这个位置来对吧那么那这样的话我们这样来上传吧那用RJ上传吧这样会比较方便一点然后呢我们去
[06:43] 去发送一个文件那么我们到这然后呢选择啊选择它哎呃我们到这然后呢回撤一下然后呢我们去选择它那我们等待它传输啊那么现在已经传输结束了那么其实可以看到呢在这个位置呢是有是有一个jar 包啊那么这个jar 包呢就是我们自己啊所写的这样的一个代码了好那么接下来我们来看一下如何去做一个这个提交任务呢
[07:14] 那我们就需要使用到Spark所提供的一个Spark一个submit这样的一个脚本然后去做一个提交那么在这个位置我们需要去通过杠杠master来指定我们的Spark的一个master的一个地址那么我们需要来找一下就是我们地址是node1还是node2还是node3那么一会我们来看一下
[07:38] 那么这是第一个这个参数那么第二个这个参数呢通过一个杠杠class来指定我们所要运行的我们的一个这个类运行这个类然后呢再往后面走呢我们需要跟一个我们的这个jar 包的一个全路径然后呢注意再往后面走这个位置呢它呢将会传递两个参数
[07:58] 那么参数之间的用空格去做一个分割那么第一个这个参数呢就是我们的一个文件的一个输入那么第二个这个参数呢就是我们的一个这个计算结果的一个输出那么接下来呢我们把这个命令呢我们来做一个拷贝然后呢我们去做一些这个调整啊那么我们来看一下那么呃首先呢我们来确定我们Spark的一个must的一个位置或者他的一个呃组啊组是谁呢
[08:28] 来刷新一下那么其实可以看到呢当前我们这个集群的这个node1它呢就是我们的一个主要的一个master对吧然后呢我们来看一下node2它呢是一个什么呢备用的一个master这个呢也是一个备用master那么显然呢我们就需要在这个位置改成什么呢是不是node17077这样的一个地址然后呢我们所运行的这个类
[08:53] 那么来看一下那么我们刚刚所修改的这个类呢它的名字啊注意它的全路径啊我们来直接拷贝吧拷贝它的一个全路径那么我们拷贝到这个位置来注意要留这个空格OK那么这个呢是不是就是它的一个路径啊再往后面走呢其实这个位置到下一个命令这个位置呢是有个空格的啊这个要注意一下然后呢我们这个jar 包的一个路径那么就是在我们的根目录下面的有一个itcast
[09:23] 这样的一个目录那么我们把这个价包的这个名字呢也来拷贝一下哎是一样的然后呢来看一下后面两个输出那么一个呢就是itcast下面一个wordtext有没有呢同样是有然后呢我们还需要指定一个输出啊就是这样一个输出了然后呢我们把这个命令来做一个拷贝那我们去做一个执行啊那我们需要进入到Spark的这个目录然后呢我们去进入到这个bin这个目录
[09:52] 在并目录下面我们是需要来看一下有这个命令叫做Spark的一个submit那么我们来看一下Spark submit是不是有这样的一个脚本命令所以说我们直接去调用它就可以了那么我们需要来操作一下把这个命令拷贝一下那么去做一个执行走好我们来等待它的一个执行OK那么到这里我们计算结果就已经结束了
[10:22] 那么接下来我们来看一下这个目录进入到根目录下面有一个itcast然后有一个wc然后可以看到有这个wc这个目录就代表着我们计算结果是不是已经就完成了对吧然后我们再来去看一下我们的一个目录的标识是不是它有个下滑线一个success那么就代表着
[10:47] 我们这个任务是不是已经成功了那么下面我们来看一下这两个文件啊叫做part000啊然后呢还有个0001啊这样的一个这两个文件然后呢我们通过一个cat命令来输出这两个文件中的一个内容那么其实可以看到一个对应的一个结果是不是就是我们之前在我们的控制台所看到的这样的一个结果啊对吧那么这样的话呢我们是不是就已经啊
[11:10] 把我们所编写的一个我们的一个word count的程序是不是提交到我们的集群中去做一个运行了那我们回头看一下我们那个Spark这个这个中啊那么其实可以看到在我们的这个所完成的一个application中那么第一条这个是不是就是我们刚刚所写的一个
[11:31] WordContent一个APP这样的一个名字所以说在我们的程序中那么我们在这个位置所设置的APPName其实会在这个位置是不是去做一个这样的一个体现对吧那么同样的从这个位置我们可以看到有这样的一条记录那就说明我们的这个任务是不是已经提交到集群去做一个计算并且已经是计算完成了
[11:54] OK好那么这样的话呢我们是不是已经就实现了将我们自定义或者说自己所编写的我们Spark的应用去提交到集群去做一个运行呢OK好那么关于这个集群的运行那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在集群中打包并运行一个基于 Spark 的 Java WordCount 应用程序。

2) 按时间顺序列出每张画面的要点：
画面1：在 Typora 中查看课程笔记，内容为“5.3.1. 修改pom文件”，并展示了修改后的 pom.xml 文件内容，其中 Spark Core 依赖版本为 2.4.3。
画面2：在 IntelliJ IDEA 中展示项目结构，选中 pom.xml 文件，显示其内容，其中 Spark Core 依赖版本为 2.4.3，且 scope 为 provided。
画面3：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，正在设置 SparkConf 并创建 JavaSparkContext，读取本地文件。
画面4：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，将文件路径从硬编码改为从命令行参数 args[0] 读取。
画面5：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，实现 flatMap 操作，按空格分割字符串。
画面6：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，实现 mapToPair 操作，将单词映射为 (单词, 1) 的元组。
画面7：在 IntelliJ IDEA 中展示 WordCountApp.java 代码，实现 reduceByKey 操作，对相同单词的计数进行累加。
画面8：在 Xshell 中登录到 Spark 集群的节点，查看本地文件夹，确认 Spark-2.4.3-bin-hadoop2.7.tgz 文件存在。
画面9：在 Xshell 中执行 tar -zxvf 命令解压 Spark 安装包。
画面10：在浏览器中打开 Spark Master 的 Web UI，显示集群状态为 Standby，无运行或已完成的应用。
画面11：在 EditPlus 中编写 Spark-submit 命令，用于提交 WordCount 应用到 Spark 集群。
画面12：在 Xshell 中进入 Spark 的 bin 目录，列出可执行命令。
画面13：在 Xshell 中执行 Spark-submit 命令，提交 WordCount 应用，并在终端中查看输出结果。
画面14：在 Typora 中查看课程笔记，内容为“5.3.2. 修改代码”，并展示了 WordCountApp.java 的代码结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependencies>
    <dependency>
        <groupId>org.apache.Spark</groupId>
        <artifactId>Spark-core_2.12</artifactId>
        <version>2.4.3</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```
画面2：
```xml
<dependencies>
    <dependency>
        <groupId>org.apache.Spark</groupId>
        <artifactId>Spark-core_2.12</artifactId>
        <version>2.4.3</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```
画面3：
```java
public static void main(String[] args) {
    SparkConf sparkConf = new SparkConf()
        .setAppName("WordCountApp");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<String> fileRdd = jsc.textFile(path: "F:/code/word.txt");
    JavaRDD<String> flatMapRdd = fileRdd.flatMap(new FlatMapFunction<String, String>() {
        @Override
        public Iterator<String> call(String s) throws Exception {
            String[] ss = s.split(regex: " ");
            return Arrays.asList(ss).iterator();
        }
    });
```
画面4：
```java
JavaRDD<String> flatMapRdd = fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(regex: " ");
        return Arrays.asList(ss).iterator();
    }
});
```
画面5：
```java
JavaPairRDD<Object, Integer> mapToPairRdd = flatMapRdd.mapToPair(new PairFunction<String, Object, Integer>() {
    @Override
    public Tuple2<Object, Integer> call(String s) throws Exception {
        return new Tuple2<>(s, 1);
    }
});
```
画面6：
```java
JavaPairRDD<Object, Integer> reduceByKeyRdd = mapToPairRdd.reduceByKey(new Function2<Integer, Integer, Integer>() {
    @Override
    public Integer call(Integer v1, Integer v2) throws Exception {
        return v1 + v2;
    }
});
```
画面7：
```java
// 保存结果到指定的目录或文件
reduceByKeyRdd.saveAsTextFile(args[1]);
```
画面11：
```bash
./Spark-submit --master Spark://node1:7077 --class cn.itcast.Spark.WordCountApp3 /itcast/my-Spark-test-1.0-SNAPSHOT.jar itcast/word.txt itcast/wc
```
画面13：
```bash
19/04/18 13:11:40 INFO ShutdownHookManager: Deleting directory /tmp/Spark-bf747d11-6790-4ce2-82b2-f4844aa6a06b
[root@itcast Spark]# cd /itcast/
[root@itcast itcast]# ll
总用量 8
-rw-r--r-- 1 root root 28 4月 18 13:11 part-00000
-rw-r--r-- 1 root root 21 4月 18 13:11 part-00001
-rw-r--r-- 1 root root 0 4月 18 13:11 _SUCCESS
[root@itcast itcast]# cat part-00000 part-00001
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“5.3.1. 修改pom文件”。
画面14：PPT 标题为“5.3.2. 修改代码”。

5) 不要评价画面美观，不要输出与课程无关的内容。

