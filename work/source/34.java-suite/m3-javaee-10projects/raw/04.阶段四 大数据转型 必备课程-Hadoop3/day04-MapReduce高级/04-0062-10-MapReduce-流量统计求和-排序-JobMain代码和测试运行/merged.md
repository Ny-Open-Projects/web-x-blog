# 10-MapReduce-流量统计求和-排序-JobMain代码和测试运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\10-MapReduce-流量统计求和-排序-JobMain代码和测试运行【海量资源尽在 ubkz.com】.mp4
- 时长 5分39秒（音频 339s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们把这个代码写完我们还需要再写一个焦闷这样我直接把上一个焦闷呢直接拷贝过来好粘在这里然后我们做一些修改就可以了因为这个代码都是重复的没有必要呢再写一次好在这里呢我们来改动一下首先呢这个任务的名字呢我们改成一个flow count thought好这个地方的焦闷用我们自己的这个输入类型这个是一个这个输入路径
[00:30] 大家注意这个输入路径呢应该是上一个MapReduce的一个输出路径所以这里面我写个out上一个输出路径呢是flowCountOut我们来看一下上一个的输出这个是一个out下面一个flowCountOut就这个OK接下来呢我们看Reducer这个Reducer类呢我们用的是flowCountSortMapper这个啊这个Mapper我们用的是一个flowCountSortMapper
[01:02] 这个K2V2的类型呢我们应该用的是一个这个我们的K2应该是一个flow并我们注意flow并用我们自己的一个salt的flow并好这个地方呢你可以把它删掉我看看上面应该之前导过包啊我把这个上一个包里边全部删掉你得小心一点好那这个地方呢用我们自己的也就是salt的flow并看一下这个地方slow并它没有导包也就是我们自己的这是我们的K2
[01:32] 而VR呢是我们的手机号所以这个地方是一个test类型好这是一个test类型那接下来看reducerreducer呢也是一个flow count的salt reducer好这个地方我们的输出类型呢是一个手机号加上一个flow bin这个也没有问题好没有问题之后呢接下来我们再看输出这个输出呀我们指定一个输出入境比如说我指定一个flow count salt然后呢
[02:02] 一个out好这个代码就写完了写完之后再想想看这个焦闷也是我们的焦闷好写完之后呢我们来做一个测试看这个能否实现一个排序好那我接下来呢我clean一下然后呢打个包好重新打个包这个包呢打完了打完之后呢我们把这个包呢直接拷贝一下然后粘贴到桌面上替换在这里呢
[02:37] 我们在这里我把这个D04这个先删掉删掉之后呢我们来上传一下上传之后呢我们来直接来运行来看一下直接把我们以前输入的命令呢直接拿过来拿过来之后呢把后面这个主类的全路径名改一下在这里呢把这个焦闷拿过来粘一下好 粘完之后走稍等好 正在执行
[03:18] 好MAP0%好MAP100%好执行完了执行完了之后呢我们来看这个结果这个结果呢在哪里呢在alt下面刷新一下有一个叫flossaltalt来我们来点开这里边有一个文件来当一下稍等好打开打开之后我们来看一下咱们来看一下这个这个吧
[03:54] 左边是不是手机号呀那我们需要按照呢这个上行数据包呢来进行降序排列你看这个地方呢它就实现了一个降序69 57一直到2说明它是没有问题的没有问题的话呢这里边需要给大家强调几点第一点呢如何实现排序这个排序的方式呢咱们说过了如果按照谁排序咱们需要把谁呢设为K2这里呢我们按照四个字段
[04:24] 它的某一列进行排序这个时候呢我需要把它整体作为K2这是第一点还有一点的话呢如何实现排序呢我们需要自定义一个加入并然后呢让它去实现一个WriteAbleCompareAble接口重写这里的一个方法就CompareTo这CompareTo呢它呢需要去指定一个排序规则在这里呢我利用了一个上行数据包它的一个值呢作为排序规则
[04:54] 我乘以-1的目的是让它实现降序因为默认是一个升序好那么大家在指定排序规则的时候你也可以按照多个字段来排那比如说第一列相同你可以按照第二列第二列相同可以按照第三列我在这里我就指定了一列多列也是一样的那么指定完之后我们去写这个箱的mypro和reducer就可以了那么在这个reducer这个地方我呢
[05:22] 把这个手机号又重新作为一个键而呢把这个flowbin呢又重新作为一只那这样子在打印的时候呢我们的手机号呢保证它在写在最前面的好这就是这个排序的一个案例好关于这个呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写并运行一个 Hadoop MapReduce 程序，包括配置 Job、设置 Mapper/Reducer、提交任务并查看最终输出结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，通过“Copy Class”对话框将 `FlowCountMapper` 类复制为 `JobMain`，目标包为 `cn.itcast.mapreduce_sort`。
画面 2: 展示 `JobMain.java` 文件内容，开始编写 MapReduce 任务，设置输入格式、输入路径、Mapper 类、输出格式、输出路径等。
画面 3: 展示 `JobMain.java` 文件内容，继续编写，设置 Mapper 类和输出类型。
画面 4: 展示 `JobMain.java` 文件内容，设置 Reducer 类和输出类型。
画面 5: 展示 `JobMain.java` 文件内容，设置输出路径并启动任务。
画面 6: 展示 `JobMain.java` 文件内容，设置 Mapper 类和输出类型。
画面 7: 展示 Windows 桌面，右键点击 `day04_mapreduce_combiner.jar` 文件，准备执行。
画面 8: 展示 SecureCRT 连接 Hadoop 集群的终端界面，准备执行命令。
画面 9: 在 IntelliJ IDEA 中，右键点击 `JobMain.java`，选择“Run 'JobMain.main()'”以运行程序。
画面 10: 展示 SecureCRT 终端中 Hadoop 任务提交和运行的日志信息。
画面 11: 展示 HDFS 文件浏览器界面，查看输出文件 `part-r-00000` 的信息。
画面 12: 展示 `FlowBean.java` 文件内容，定义了包含 upFlow、downFlow、downCountFlow 三个字段的可比较类。
画面 13: 展示使用 EditPlus 打开并查看 HDFS 输出文件 `part-r-00000` 的内容。
画面 14: 展示使用 EditPlus 打开并查看 HDFS 输出文件 `part-r-00000` 的内容，其中第 3 列数据被高亮显示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package cn.itcast.mapreduce_flowcount;
import org.apache.Hadoop.io.IOexception;
```
画面 2:
```java
package cn.itcast.mapreduce_sort;
import java.io.IOException;
import org.apache.Hadoop.mapreduce.Job;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.Hadoop.fs.Path;
import org.apache.Hadoop.conf.Configuration;
import org.apache.Hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.Hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.Hadoop.mapreduce.lib.output.FileOutputFormat;
import

