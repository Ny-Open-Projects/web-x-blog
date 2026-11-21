# 3-HDFS的文件副本机制

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\3-HDFS的文件副本机制【海量资源尽在 ubkz.com】.mp4
- 时长 12分37秒（音频 757s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们来学习HDFS文件副本和block块存储这个什么意思呢我们来画一张图好我们来去先画三个datanode好这是我们的datanode我们画大一点好datanode好有三个datanode好再画一个name node然后呢这些datanode由这个name node来管理好假如说呢我现在呢有一个文件
[00:58] 这个文件呢假如说是还是A.T.A.T它是300兆的大小那300兆的大小这个文件如果我要存在这个集群的HDFS里面它是如何去存储呢我们的HDFS有一个机制这个机制呢是分片机制或者叫分块机制那它呢默认会将这个文件进行切片它怎么切呢默认情况下呢
[01:31] 这个切片一片的大小呢是128兆比如说我300兆的一个文件那它能切多少块呢一块是118再切一块我画一下第一块118那第二块呢也是118的那加起来是256那剩余呢还剩一部分好把它切成三块来我们来标一下稍等这个封一下来我们再看一下
[02:15] 第一块第二块好第三块把它切成三块那这三块呢被称为一个一个的block那第一个呢是一个block这个block是多大呢128兆大家注意我们在Hadoop2.0之上呢我们这个一块呢默认是128兆128兆OK那第二个呢第二个它也是一个block那这个呢
[02:46] 也是118兆把它标一下那第三个呢第三个它不够118兆呢我们也把它称为一个block这个block呢是44兆大家请注意这个block是一个逻辑单位意思就是说比如说我这个文件呢有三个block那么其中呢有两个block它是118兆而剩余的呢它是44兆OK这是一个block切片的问题那默认呢是118兆其实我们是可以做改动的
[03:17] 来我们来看一下我们上一次课给大家配置了一个Hadoop那么在这里边呢有一个配置文件我们来看一下在exportservice里边Hadoop然后呢里边有一个etcHadoop好在这个里边有很多配置文件我们来看一个配置文件就是有一个hdfs site的插门我们来看一下hdfs好site的插门
[03:49] 我们来进来看一下这里边有一个叫block size这个值是单位是字节这个就是128兆你也可以调整这个大小我们采用的是默认那么把它切片之后这个数据怎么去存这个是我们刚才提到过它会把每一块存放在不同的节点上比如说第一块存这里我把它缩小一点太大了这是第一个
[04:20] 那第二块呢我们来存找一个节点来存储好了第三呢我们来找一个节点也来存储好那么这个叫它的一个分块思想好存完之后呢我们在这个HDFS里边还有一个副本机制什么叫副本机制呢你比如说呢我把这个文件切成三部分分别存放在不同的主机上那假如说某一台机子当机了挂掉了
[04:56] 那这个数据就会丢失啊一丢失那么这个文件它是不完整的那这个时候外界访问的时候呢肯定会出问题那怎么保证我这个数据的一个容错性呢这个时候呢HDFS提出了一个副本机制它在存比如说第一块的时候呢它把这一块呢又复制出两份出来分别存放在不同的节点上你比如说这是一个JJ块那么它把这块复制完之后呢
[05:25] 在这里边又存一个一个副本那在这里边又存一个副本那同样的他在存那个第二块的时候呢在这里又存一份好随便画个那在这里呢也存了一份同样的那这个蓝色的的话在这儿存了一份好在这里又存了一份那假如说某一台机子当期了那么因为这一个block呢有三个副本它是不影响这个数据的完整性的好
[05:55] 这就是它的副本机制在默认情况下呢这一个block呢是有三个副本当然这个参数我们也可以调整来我们再看这里边一个配置文件还是刚才这个配置文件hdfs set在这里边呢有一个向下翻有一个参数叫replication我们来向上看这个叫dfs replication这个里边写的是3表示呢每一个block是三个副本
[06:24] 好那么这个呢就是它的副本机制当然了我们存放了三个副本它的代价呢就是它的空间呢就是会占有它的空间当然我们通过空间呢来去换安全好那么现在还有一个问题那么NameNode是干嘛呢NameNode是来存储原数据的就是你每个文件的一些信息你这个文件呢在哪个节点上存放你有几个副本NameNode都清清楚楚
[06:53] 那假如说内门node在存一个A点帖T的时候呢假如它是这样记录的它比如说呢这个block1比如说它有三个block嘛三个block好block1呢它在哪里存呢假如它在node01上存block1你看block1是红色的它又在node02上存然后呢它又在node03上存它是这样记的好那么
[07:24] 也就是说这个第一个block它有三个副本三个副本那假如说呢第一台机子当机了当机了当机了之后呢相当于这个副本是不是丢失了那么也就是说和它原来记录的这个状态不一致了这个时候怎么办呢这个时候没关系我们的name node呢会怎么办呢会去另外某一台机子上再去拷贝个副本然后呢存储在某一台机子上好比如说呢第一台挂了第一台当机了
[07:54] 我们记得吗它当机了好那这个时候呢它会从另外一些机子上呢再去把这个block的副本拷贝一份然后再存出一份依然能够保证呢这个副本是三份这就是快速的一个恢复能力好这是它的一个机制好那我们继续我们来看看什么呢现在有个问题就是说我存着三个副本我存一个我存一个这个第一个block我存三个副本那它存在哪个主机上呢
[08:24] 这个时候呢它有一个有一个模有一个叫机架感知的一个算法机架感知什么叫机架感知呢我们来看一个看一张图片先说什么叫机架比如说我在这里搜一个词叫机架那我们很多的服务器呢是有一堆的机架组成的来我们来看图片比如说这个我们的机房的服务器呢都是由一个一个的机架组成的而每一个机架呢里边呢放了很多的主机
[08:58] 那比如说我在存一个block的副本的时候那这三个副本分别存放在哪台电脑呢它有一个机甲感知那机甲感知呢它是有一个算法每一个Hadoop的版本不一样它的算法也是不太相同的那这里呢我说一个咱们3.0的一个算法来我再画一张图我们来看这个画一张图好比如说呢我把刚才这个图呢给大家复制一下
[09:29] 还是这个文件放在这个位置好比如说这个第一个block那我要去存三个副本那我要去存在哪台主机上呢这个时候我给大家模拟个机架比如说这是一个机架机架呢有一个词叫rackrack1好那这个呢一个机架里边呢有很多的主机咱们就模拟一下主机好这是一个你就认为是一个data node好这里边有
[10:07] 有三台主机这是第一个机甲那再来一个机甲这是第二个机甲叫REC2好 比如说呢我要去存一个block咱们就单独去看这个block假如我这个block呢我这个副本呢这个block要去写到我们的集群里面那我要把这个block放在什么位置呢注意我们这个向服务器写数据的时候呢我们把这个叫客户端客户端client
[10:39] 假如说这个客户端和我的当前的Data Node是在同一个机子上好假如说假如说咱就不说同一个机子假如说我去上传的客户端和我这个机架是在同一个机架里边和我这个Data Node是在同一个机架里边这个时候它会在本机架里边找一个主机随机找一个主机然后存放在某一台Data Node里边去某一台主机里边去OK
[11:12] 当它在这里存了一个副本之后呢接下来它接着会在本机架里面记住它会在本机架里面呢随机找另外一台主机比如说呢找下面这台主机然后呢再去存一个副本OK再存一个副本好这是第二个副本那还有一个副本呢咱们说默认是不是三个呀好当它去存第三个副本的时候注意我把这个标给颜色这是第二个副本
[11:44] 当他去存第三个的时候他不会在本机甲找他会去找他会随机挑另外一个机甲然后呢在这边随机挑一个Datano的把这个副本存进去好到这里呢一共有三份这是他的一个机甲感知也就是他有套自己的一些理论有套自己的算法保证呢我这个副本存的时候呢这个容错性是最高的你比如说呢你这个机子挂掉了
[12:12] 那我还有一台主机比如说你这个整个机架挂掉了那我还有另外一个机架它就通过这种方式来把这些副本分别存在不同的Data NodeOK这些Data Node好 这是它的一个机架感知大家简单了解一下好 关于它的一个副本机制还有它的一些机架感知我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 HDFS 文件副本和 Block 块存储机制，包括文件如何被分割成块、块如何在多个 DataNode 上存储副本、以及副本的分布策略。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 HDFS 文件系统架构，NameNode 存储元数据，DataNode 存储文件内容，以及 Block Replication 的概念图。
画面 2: 展示一个 300M 文件被分割成三个块（128M, 128M, 44M），并由 NameNode 管理，三个 DataNode 作为存储节点。
画面 3: 展示 hdfs-site.xml 配置文件中设置 NameNode 数据目录的配置项。
画面 4: 展示文件块副本机制，每个块分布在不同的 DataNode 上，图示中显示了块的副本分布。
画面 5: 展示 hdfs-site.xml 配置文件中设置 DataNode 数据目录、NameNode HTTP 地址、副本数、权限等配置项。
画面 6: 展示文件块副本机制图，与画面 4 类似，但图示中显示了块的副本分布。
画面 7: 展示百度搜索页面，搜索框中输入“机架”。
画面 8: 展示百度图片搜索结果页面，搜索关键词为“机架”。
画面 9: 展示百度图片搜索结果中的一个服务器机架图片。
画面 10: 展示一个绘图软件界面，图示中显示了 DataNode 的存储块分布。
画面 11: 展示一个空白的绘图软件界面。
画面 12: 展示文件块副本机制图，图示中显示了块的副本分布，并标注了“机架感知”。
画面 13: 展示一个客户端访问 HDFS 的流程图，客户端请求被路由到 rack1 和 rack2 中的 DataNode。
画面 14: 展示文件块副本机制图，图示中显示了块的副本分布。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet type="text/xsl" href="configuration.xsl">
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. See accompanying LICENSE file.
-->
<!-- Put site-specific property overrides in this file. -->
<configuration>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///export/servers/Hadoop-3.1.1/datas/namenode/namenodedatas</value>
  </property>
</configuration>
```

画面 5:
```xml
<property>
  <name>dfs.datanode.data.dir</name>
  <value>file:///export/servers/Hadoop-3.1.1/datas/datanode/datanodeDatas</value>
</property>
<property>
  <name>dfs.namenode.http-address</name>
  <value>node01:50070</value>
</property>
<property>
  <name>dfs.replication</name>
  <value>3</value>
</property>
<property>
  <name>dfs.permissions.enabled</name>
  <value>false</value>
</property>
<property>
  <name>dfs.namenode.checkpoint.edits.dir</name>
  <value>file:///export/servers/Hadoop-3.1.1/datas/dfs/nn/edits</value>
</property>
<property>
  <name>dfs.namenode.secondary.http-address</name>
  <value>node01.Hadoop.com:50090</value>
</property>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“1.4 HDFS 文件副本和 Block 块存储”，图示中 NameNode 指向三个 DataNode。
画面 2: 图示中 NameNode 指向三个 DataNode。
画面 4: 图示中 NameNode 指向三个 DataNode，每个 DataNode 中包含不同颜色的块。
画面 6: 图示中 NameNode 指向三个 DataNode，每个 DataNode 中包含不同颜色的块。
画面 12: 图示中 NameNode 指向三个 DataNode，每个 DataNode 中包含不同颜色的块，并标注了“机架感知”。
画面 13: 图示中 Client 指向 rack1 中的 DataNode，rack1 中的 DataNode 指向 rack2 中的 DataNode。

5) 不要评价画面美观，不要输出与课程无关的内容。

