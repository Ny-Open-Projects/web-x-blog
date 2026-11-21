# 4-HDFS的块缓存和访问权限

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\4-HDFS的块缓存和访问权限【海量资源尽在 ubkz.com】.mp4
- 时长 5分26秒（音频 326s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来看一下HDFS其他的一些特点第一个是快缓存这什么意思呢就是说我们在访问一个HDFS数据的时候如果有些数据是频繁访问因为这个数据是放在DataNode里边那这个时候呢经常被访问的块就会被缓存在DataNode内存里边来我们来看这个图比如说呢假如说我们去访问这个A.TAT
[00:29] A点天赋里面呢比如说我要访问这一块这个块呢经常被访问那这个时候呢他就会想办法把这一块呢放在内存中去放在一个区域这个区域是内存放在这里边有什么好处呢很明显可以提高我们的读取速度这就是所谓的块缓存我们来看这里边有一句话比如说我们以后呢
[01:06] 去操作我们的这个数据的时候呢有个join操作那这个时候呢就会用到core缓存这个呢当我们讲到map reduce的时候呢重点给大家讲解好还有呢你看它下面有句话它说如果一个文件是130兆它会被分成两个block因为什么因为一个block是128兆那即使你多两兆它也是一个block那么这个block呢一个是128兆
[01:34] 那另外一个block你说它是占118兆呢还是只占2兆呢那这个时候大家注意另外一个block只会占2兆你看它说实际占的空间还是130兆而不是说呢每个占118两个占256不会这样子的因为block它只是一个逻辑单位就是我说你这个文件是几个block那这个就说明了你这个文件被切成了几块那你文件具体是多大
[02:03] 要看你文这个文件实际的大小OK这是这个接下来还有一个HDFS文件的权限验证这个什么意思呢就说HDFS它也是一个文件系统它这个文件系统长什么样子呢我们可以简单给大家看一下这个HDFS文件系统呢和我们Linux很类似它也是一个根目录然后根目录下面呢有很多的子目录比如说呢这个有一个目录叫tas1
[02:32] 然后有Test2这么一个目录然后呢这个Test1里面呢又有很多子目录比如说Demo1Demo2好这么一个方式这里边呢比如说是Demo1好Demo2好那么这么一个文件系统呢它有自己的一个访问权限那这个访问权限呢我们来看一下比如说呢我打开这个浏览器我们来访问我们的HDFS还记不记得Node01
[03:03] 50070我们来访问好访问之后呢点这里有个browser的failsystem好进来进来之后稍等我们进入它的一个根目录好那这里边呢就是我们的一个目录在这里边呢你看它呢有很多的一些目录那这些目录的话呢这里边大家看一下左边一个permission这个就是它的一个权限权限可读可写可执行这个和我们links是一样的
[03:34] 而这里边是一个所有者文件的拥有者root它所在的组OK那如果你不符合这个权限要求你是不能访问的OK这是一个权限问题那接下来还有一个什么呢还有一个叫secondary name node这个是什么意思呢好这个呢我先给大家提一下待会我们再详细讲解这个来我们来看这张图我们说name node是干嘛呢是存储我们的原数据的
[04:03] 那么存原数据呢它的很多的数据呢都是在内存里面都在内存里面内存里面的数据意味着掉电了之后呢这个数据呢就没有了那所以说呢每次在启动这个NameNode的时候呢它需要将这个原数据从硬盘上的某些文件中要恢复到内存里面那每次去做这个事情啊它非常的累或者说或者说压力非常的大那这个时候呢又有一个东西
[04:33] 有一个进程叫什么叫Secondary Name NodeS-E-C-O-N-DSecondarySecondary Name Node这个Secondary Name Node是干嘛呢它并不是Name Node的一个备份它只是来帮助Name Node去干一些事情做一些辅助性的事情然后呢减轻Name Node的压力记着这个Secondary Name Node是为了减轻它的压力好那么在Name Node和Secondary Name Node之间呢
[05:04] 有两个文件我们一会儿呢给大家讲解什么文件呢有一个文件叫fsimage有一个文件叫edits好这两个文件呢它是我们磁盘上的一个文件它专门来记录一些元数据的信息OK好这是secondary那我们先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 HDFS 的块存储机制、文件权限验证以及元信息管理（SecondaryNameNode）。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 HDFS 文档目录结构，当前位于“1.4.3 HDFS 文件权限验证”章节，内容包括块缓存、文件权限验证等。
画面 2: 手绘图解 HDFS 副本机制，展示文件 a.txt 被分割成三个块，分别存储在三个 DataNode 上，箭头从 namenode 指向各 DataNode。
画面 3: 文档页面，内容与画面 1 相同，显示“1.4.3 HDFS 文件权限验证”部分。
画面 4: 文档页面，滚动至“1.5 HDFS 的元信息和 SecondaryNameNode”章节，开始介绍元信息存储。
画面 5: 手绘图解，标注“内存”指向其中一个 DataNode 上的块，说明块数据在内存中的状态。
画面 6: 手绘图解，添加了“test1”、“demo1”等文件名，同时在任务栏显示一个 SecureCRT 窗口，其中包含命令行内容。
画面 7: 浏览器搜索结果页面，搜索框内输入“node01:50070”，下方显示“Namemode information - node01:50070/dfshealth.html”链接。
画面 8: 浏览器打开的 Hadoop 网页，显示“Hadoop, 2018.”，页面顶部有导航菜单。
画面 9: 文档页面，滚动至“1.5 HDFS 的元信息和 SecondaryNameNode”章节。
画面 10: 文档页面，显示“1.5 HDFS 的元信息和 SecondaryNameNode”章节内容，包含 XML 配置片段。
画面 11: 文档页面，聚焦于 XML 配置片段，显示 namenode 的 name.dir 和 edits.dir 路径。
画面 12: 手绘图解，与画面 6 类似，但未显示 SecureCRT 窗口。
画面 13: 文档页面，显示“1.5 HDFS 的元信息和 SecondaryNameNode”章节内容。
画面 14: 手绘图解，添加了“SecondaryNameNode”节点，箭头从 SecondaryNameNode 指向 namenode，表示其与主节点的关系。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 10、11、13 中的 XML 配置：
<property>
  <name>dfs.namenode.name.dir/name>
  <value>file:///export/servers/Hadoop-3.1.1/dats/namenode/namenodedatas</value>
</property>
<property>
  <name>dfs.namenode.edits.dir/name>
  <value>file:///export/servers/Hadoop-3.1.1/dats/dfs/nm/edits</value>
</property>

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 2、5、6、12、14 中的手绘图：
- namenode 指向三个 DataNode。
- 在画面 5、6、12 中，一个 DataNode 上的块被标注“内存”，并有箭头指向该块。
- 在画面 14 中，SecondaryNameNode 有箭头指向 namenode。

5) 无。

