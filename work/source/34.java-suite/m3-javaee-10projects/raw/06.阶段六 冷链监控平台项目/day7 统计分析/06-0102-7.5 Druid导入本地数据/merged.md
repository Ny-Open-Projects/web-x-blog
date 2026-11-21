# 7.5 Druid导入本地数据

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.5 Druid导入本地数据_【海量资源尽在 666java.com】.mp4
- 时长 8分30秒（音频 511s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,Zoe的作为一个数据库它和我们的MySQL不太一样但是呢,它的一些操作方式和操作的内容大致类似的一种方式是说,或者一类操作是属于我们把数据存储到数据库里边那么另外一类操作是我们如何来查询数据库那么现在呢,我们来看一看如何把数据导入了我们Zoe的里边那么导入了Zoe的又分成两类数据一类的叫做离线数据
[00:29] 那么另外一类的叫实时的数据那离线数据的一个导入我们现在主要讲离线数据的导入那么我们访问我们的Droid服务器它的一个管理页面那管理页面里边有一个load data而这种load data里边它有一个叫batch load也就是批处理的一个导入那么批处理导入我们可以把文件某一个文件导入进来那么我们打开我们local disk也就是说local disk这个按钮我们点开它
[00:57] 点开来之后呢我们看到右侧的时候其实它是有我们的有我们的这个什么呢有我们的一些需要填写的东西那么左边的话它其实是属于我们整个的一个把本地文件导入到JIT里边所要操作的几个步骤比如说一个叫connect就是连接第二个叫是pass data是我们的要解析data第二个是
[01:23] PastTime要把某一个时间字段来对它进行解析然后对它进行转换然后进行过滤然后编辑我们的这个数据模型然后进行分区和进行提交上去那我们现在把本地的一个文件来导入进来当然这个本地文件并不是说我们用户自己当前操作的一个电脑而是我们DRAI的服务器那么DRAI的服务器里边我们
[01:52] 来看一看我们这的服务器这的服务器它在我们的opt下面的有一个叫quick startquick start下面有一个total real这个目录而这个目录下面的话呢我们可以看到这里边有一个示例的一个文件就叫做wikitickerwikiticker-2015-09-12-simple这样的一个json文件
[02:24] 这个json文件我们看一看一看这个json文件里面的内容那它其实是就是一条一条的一个json对象对吧json字符帅而这个json字符帅其实就属于我们在我们的这个怎么说呢每一条数据每个json字符帅就是一个一条记录而这个记录实际上是记录的是vk里边以前的一个vkvk里边的数据的一个内容那么我们把这个数据
[02:54] 给它导入到我们的我们的这个叫什么我们的这个quick追到里面去我们先把这个路径拷贝过来那么我选择的类型是local那么选择的相对路径就是我们quick start然后后边的total那么filter就是我们这个文件的名字我们把文件名字拷过来拷过来之后呢我们可以看到我们的这个进行
[03:25] 我们点解析按钮当前我的浏览器的大小会有一点影响浏览器有可能下边这两个按钮看不到但是我们把它往下拉一拉就能看到了或者按type键我点这个的时候按type键我就能找到找到这个到底是哪一个了在这个地方那么我们点了完之后我们看到它把我们的这个json
[03:53] 文件给他解析了一遍解析之后是一条一条的记录而这条记录里边就是有一些字段嘛对吧比如说像timer timer字段然后channel字段然后我们的城市comments或者说是这个country ISO的一个code啊就是国家这个编码那么我们再点这个菜单点这个按钮就是next就是passed it我们要把这个数据进行解析那我们的这个jade就会自动的把
[04:23] 这个json文件里边的内容给它解析出来解析成按照这样的一个格式看起来比较容易解析的一个格式那么它的解析的解析的这个类型呢就是一个json的对吧我们要把json的那下一步的话就是我们要解析中间的一个时间字段解析时间字段那么我们它自动的话就找到我们的一个时间字段这个时间字段就是开始Time我们这个时间字段的话我们会把它
[04:54] 创当作坠的一个表里边的有一个默认的一个字段叫双下滑线的一个time那解析完了之后呢我们的时间其实是可以把它解析成我们想要的一个格式的解析成我们的这个我们把它解析成www-mm-dd然后sh-mm和ss对吧我们把它解析成这样的一个
[05:24] 这样的一个格式那么下一步的时候我们再点击转换OK那在下一步的话我们点击选择那么我们看它的转换是不是有问题时间上的一个我们使用的是ISO我们看看ISO的一个事情OK用ISO的这种日期类型给它转换这是没问题的刚才转换的那个日期类型不对因为我们原来的
[06:02] 原始的这个数据类型它不是一个不是一个那种什么YYYY-MM的不是那种类型的最开始的类型数据类型是属于我看一下它是这样的一个数据类型这样的一个数据类型中间注意它实际上是有一个T它实际上是一个ISO的一个数据类型数据类型我们给它选的时候我们就选ISO的数据类型那点Next是Transfer然后再点
[06:32] 就是一步一步的往下走其实就OK了然后下一步的话我点这个Sky码这个Sky码的话将基本上也是按照这种方式吧我们再点下一步的是进行分区而分区的话它有一个时间的力度我到底是按小时按按天还是说按分钟那么我们现在选择了一个按小时然后再点分区分区之后我的这个进行Segment的
[07:00] 我分区我按照小时来进行分区那我们再把它进行一个publish然后数据库的数据库的名字啊那就是这个数据表的名字呃叫wiki吧然后我点击next然后点击submitok那此时就会把我们的这个wiki的表来添加进来了我们刷新一下刷新一下查找到我们的datasource我们看一看我们的任务
[07:40] 这个任务还在running因为它的数据啊其实有不少的数据嗯看一看哈还是在执行应该需要几十秒来执行完成嗯这样的话它经过了一分多钟啊接近两分钟的时间把我们的这个啊离线文件里面的数据就导入了导入进来了那么这个任务呢其实相应的就是一个啊一个success一个成功的一个状态我们再看datasource里边
[08:12] 它其实就有两个这种DataSource了而这两个DataSource第二个DataSource就是刚才我们导入进来的这个离线的数据那这个其实就是我们通过离线的方式来导入到我们的把我们数据导入到我们的这个对的里面去

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Apache Druid 的图形化界面完成数据的加载、转换和发布流程。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示 Druid 数据加载器的初始界面，提示用户选择原始数据的位置，提供 HTTP(s)、AWS S3、Google Cloud Storage 和 Local disk 等选项。
画面 2: 在终端中执行命令，尝试创建目录并查看 JSON 文件，但提示文件或目录不存在。
画面 3: 在终端中显示了 JSON 数据的样本内容，包含时间戳、频道、评论等字段。
画面 4: 终端中继续显示 JSON 数据样本，包含更多评论记录。
画面 5: Druid 数据加载界面，处于“Connect and parse raw data”阶段，右侧显示“Firehose type”为 local，“Base directory”为 /path/to/files，提示路径必须在所有 Druid 服务器的本地文件系统上。
画面 6: 数据加载界面，已选择“local”作为 Firehose type，Base directory 为 /path/to/tutorial，File filter 为空，右侧显示警告信息“此路径必须在所有 Druid 服务器的本地文件系统上”。
画面 7: 数据加载界面，处于“Transform and configure schema”阶段，提示用户选择解析器（Parser to use）为 json，并提供“Add column flattening”和“Preview”按钮。
画面 8: 数据加载界面，处于“Transform and configure schema”阶段，提示用户可以添加列过滤器（Add column filter）和全局过滤器（Add global filter），并提供“Preview”按钮。
画面 9: 数据加载界面，处于“Transform and configure schema”阶段，提示用户可以添加列转换（Add column transform），并提供“Preview”按钮。
画面 10: 数据加载界面，处于“Transform and configure schema”阶段，显示了数据列的预览表，包括 time、added、channel、cityName、comment、countryCode、countryName、deleted、delta、isAno 等列，并配置了时间戳规范（Timestamp spec），从“time”列提取，格式为“ISO”。
画面 11: 数据加载界面，处于“Publish configuration”阶段，显示数据源名称为“tutorial”，并设置“Append to existing”为 False。
画面 12: 数据源页面，显示“Datasources”标题，下方无数据源信息，有“Refresh”、“Go to SQL”和“Show disabled”按钮。
画面 13: 任务页面，显示“Supervisors”和“Tasks”两个部分，Supervisors 中有一个名为“all_device_message”的 Kafka 数据源，状态为“Running”。
画面 14: 数据加载界面，处于“Connect and parse raw data”阶段，显示了数据样本，右侧显示“Firehose type”为 local，“Base directory”为 /path/to/tutorial，File filter 为空，提示路径必须在所有 Druid 服务器的本地文件系统上。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 2:
```bash
[root@node2-w06 tutorial]# bash quickstart/tutorial
bash quickstart/tutorial: No such file or directory
[root@node2-w06 tutorial]# quickstart/tutorial
quickstart/tutorial: No such file or directory
[root@node2-w06 tutorial]# bash quickstart/tutorial
bash quickstart/tutorial: No such file or directory
[root@node2-w06 tutorial]# cat wikipedia-top-pages.json
{
  "queryType": "topk",
  "dataSource": "wikipedia",
  "intervals": ["2025-09-12/2025-09-13"],
  "granularity": "all",
  "dimension": "page",
  "metric": "count",
  "threshold": 10,
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。

