# 18-hadoop的安装-配置文件修改

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\18-hadoop的安装-配置文件修改【海量资源尽在 ubkz.com】.mp4
- 时长 14分37秒（音频 878s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来对我们这几个文件进行配置一共有六个我们先看第一个call site的插mail这个文件是我们Hadoop一个核心的配置文件它的配置信息在这里我直接把这个里边的内容直接copy过来然后放在这个位置稍等放在这里直接把这个原来的删掉然后覆盖就可以了好这个文件里边一些配置信息我们简单来看一下第一个呢
[00:31] 来指定我们文件的一个类型文件系统类型我们这个地方用的hdfs 冒号杠杠这个表示用的是分布式文件系统那么我们的这个主节点在哪里呢在node01 8020这个短口好这个大家都统一的第二个呢是临时文件的存储目录临时文件存在哪里呢我们存在这个export servicehadoop3.3.1下边一个data4temp这个目录
[01:00] 这个DETA4这个目录呢还不存在待会呢我们会创建它接下来呢是缓冲区的大小这个里边呢我设了一个8192这个时候呢大家在工作中呢可以根据需求呢自己来设最后一个是开启HDFS垃圾桶机制就隔一段时间啊它呢可以去垃圾桶里边呢回收一些数据那这个里边呢我设了一个间隔呢是110080它的单位是分钟
[01:29] 大概是7天它会这个删除一次OK这是call set的插面配完之后记着一定要按Ctrl加S保存一下好接下来我们来看第二个配置第二个是Hadoop ENV的SH来点开点开之后我们向下翻这个地方唯一需要大家配的是一个什么信息呢我们来看我们需要配置一个加着home
[01:59] 我们来找一下吧你可以在这里搜一下java home找一下这个位置把这个应该是把这个注释呢打开我们来看一下我们要去改一下xpod这个xpod java home把这个后面呢复了一下然后呢去修改这个位置我看到了应该是在这好把它注释打开把我们的这个java home啊它的路径呢
[02:33] 放在这里这个地方一定要确保这个路径是正确的好这个就配好了配好之后呢我们来看第三个HDFSite的插面这个呢文件里边的信息特别多来我们打开这个HDFSite的插面这个主要是配置我们HDFS一些设置信息我把这个里边这个东西先拷过来我们来看一下全部拷过来我拷对了没有
[03:07] 把它复制一下然后呢把原来的覆盖一下走粘贴好粘贴完之后呢我们来看一下它的一些重点参数第一个NameNode的NameData这个是我们这个NameNode的节点呢它的数据存放目录这个是我们原数据的数据存放目录我们给大家简单做一个注释吧把这个注释复制一下好这个是配置配置原NameNode原数据
[03:44] 的存放路径这个原数据呢咱们刚说过这个原数据呢是一个HDFS系统里边呢最核心的数据那这个路径呢就在这里OK那接下来呢还有一个叫block size这个是文件块大小这什么意思呢我们注意我们以后呢在存储一个大文件的时候呢如果这个文件特别大我们需要给它分片分块那么一块是多大呢这个值呢
[04:14] 是118兆所以这个地方是设置设置文件分块的大小这个分块呢有一个有一个叫block也就是block的大小好这是这个接下来呢还有一个我们来看还有一个就datanode data.这个是我们datanode的节点它的数据存放位置我们知道这个hdfs里边呢有一个name node是不是还有一个datanode来看我画的这张图
[04:48] 哪张图呢我们来看一下就这个NameNode来管理原数据而DataNode存放具体的数据所以这个地方是来指定DataNode数据存放目录好在这里我指定了这么一个目录好接下来还有呢看这个这个地方呢我们设置了一个主机和端口这个是我们NameNode通过浏览器访问的一个端口50070
[05:19] 好把它过来这是访问通过浏览器访问HDFS的端口端口这个记者是50070待会我们验证的时候呢我们要去访问这个好那接下来还有一个replication这个也比较重要这个是文件的副本个数这是设置设置文件的副本数这个什么意思呢
[05:53] 就是说我们一个文件存在这个HDFS上那它一个文件它有三个副本为什么要这样做呢其实主要是防止某一个机子当机之后它的数据不会丢失一般在我们HDFS里边一个文件如果说它被切分成多个block之后每个block有三个副本也就是说它会有三份重复的数据即使我一台机子当机
[06:22] 它也不会影响我数据的丢失好那接下来呢还有一个这个权限这个访问权限我把它关闭了这个地方呢我们设置HDFS的访问权限设置HDFS的权限访问好这个地方呢我把它false那么这个false就是关闭它的访问权限OK那接下来呢还有一些这个edits地啊就表示它的日志文件存放目录好这是设置
[06:58] htfs日志文件的存放路径这个日志文件呢叫edits后面呢我们给大家单独讲这个好那接下来看看还有没有其他的一些哦这地方我说错了这个地方是设置这个checkpoint的检查点那个设置这个它的一个编辑它的一个日志文件应该是在这个位置name node edits.r好那接下来呢
[07:29] 我们把这个文件呢就配好了我们来记着保存一下Ctrl加S好 接下来我们继续看我们在配置下面这个Map.setChannel好 我把这个呢直接复制过来好 这些直接过来Map把它直接覆盖好 那么这个文件呢数据也特别多大家在配的时候不需要每个参数都记那么你只需要记住一些重点参数就行了这里边呢
[08:00] 这个地方呢你看第一个表示呢我的这个MapReduce的框架用的什么呢用的是样机群这个地方呢是指定MapReduce的框架注释拷过来指定MapReduce的执行框架稍等执行框架这个呢就是样样机群这个样机群呢有两个东西一个是Resource Manager一个是
[08:39] NodeManager还记不记得ResourceManager是主节点NodeManager是从节点好 想想看这个地方表示内存的一个大小1024好 再想想看看看有没有其他的这个地方呢应该没有别的了这个是我们设置一些路径这个里边的一些参数呢我们就不用管了好 我们把这个也保存一下好 接下来呢看下面这个
[09:08] 这个yard set的插庙这个呢主要是来配置我们的yard集群的把这个复制过来好特别多好复制过来好复制过来之后呢我们接下来把它依然粘到这里好我们来看一下这里边一些重点的核心参数吧我们向下看一下好这里边呢都不用我们管那这里边呢有一个东西就是检查虚拟内存
[09:40] 然后呢这个地方我们把它关闭因为呢这个一二集群对我们默认的内存要求非常大我们把它关闭之后呢它就不会报错好接下来还有一些呢我们看一下看好这里边呢设置一个我们的是一个虚拟内存虚拟内存OK那我们设成1024好这个呢就设置好设置好之后呢我们基本上别的参数就不用再设了好把它保存一下
[10:10] 好保存下之后呢我们来进去看呃向下看呢还有一个worker这个worker呢很重要这个worker呢主要来设置我们的从机的好我把它打开好回到我们这里啊worker这个worker里边呢设置你从机你有几个从机呢我有三个node01node02和node03这是我们以前设过的一个主机名好把它保存一下记着一定要保存看看这里边呢假设我修改完都没保存你看它是红色的
[10:42] 然后保存一下好保存完之后呢基本上我们这些呢就配置好了好配置好了之后呢我们还要干一件事情我们刚才设置的很多文件夹呀都是不存在的你比如说这些文件夹都不存在那怎么办呢我们要去创建要使用的一些文件夹把它们全部复制好然后呢在我们的终端里边直接运行在第一台机子走好回车好就创建好了创建了一些中间使用的一些目录
[11:13] 然后呢接下来我们再回到我们的Service目录把你刚才配置的一些信息分发给其他两台主机这句话解释一下SCP远程拷贝-20拷贝一个文件夹那这个呢是文件夹的名字我要把这个Service下面这个文件夹拷贝到node02它的当前目录下面也就是node02也是在Service下面好我们来拷贝稍等稍等这个文件很大
[12:01] 我们已经拷贝完了拷贝完之后我们接下来还要干一件事情把它拷贝到node03上继续这个时候稍微等待好经过漫长的等待我们拷贝完毕好拷贝完毕之后相当于第二台和第三台里边也有一个Hadoop我们看一下export Service里边有一个Hadoop再看120export Service然后下面
[12:31] 是不是有个HadoopOK那么做完之后呢我们还要做一件事情我们要设置一个环境变量好打开这个ETC profile每个节点都要做ETC profile好在这下面呢加一个Hadoop的环境变量好我们来做一下这个事情OK把这两句话呢直接加在这个后面去也要检查一下Export serviceHadoop 3.3.1OK后面这个呢
[13:05] 是将我们的这个harddop追加到pass的里边去来让它能够生效ok你看这一个是bin一个是sbin都要加进去好保存退出然后这个选一个source让它生效etc profile好那接下来第二台机子我们先来做一下etc profile好这里边呢啊稍等这个地方还是100我推一下好这个是第二台机子那我们来看
[13:42] ETC profile在这里呢我们把这两句话呢拿过来直接呢站在这里好保存退出然后sauceETC profile第三台ETC profile站在这里直接说的直接呢保存退出然后sauceETC profile好把这个做完了
[14:32] 做完之后呢接下来我们来验证我们配置是否正确

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
配置 Hadoop 集群环境，包括修改核心配置文件、设置环境变量和创建必要的目录结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Hadoop 配置文件 configuration.xml 的开头部分，包含 XML 声明和 Apache 许可证信息。
画面2：展示 Hadoop 环境脚本 Hadoop-env.sh 的部分内容，包含设置 HADOOP_OS_TYPE 和 HADOOP_OPTS 的逻辑。
画面3：展示 Typora 中的 Hadoop 安装文档，内容为“Hadoop-env.sh”和“hdfs-site.xml”的配置说明。
画面4：展示 hdfs-site.xml 文件中配置 namenode 和 datanode 的数据目录。
画面5：展示 hdfs-site.xml 文件中配置 dfs.replication 和 dfs.permissions.enabled。
画面6：展示 Typora 中的 Hadoop 安装文档，内容为“mapred-site.xml”的配置说明。
画面7：展示 mapred-site.xml 文件中配置 mapreduce 的内存和任务参数。
画面8：展示 Typora 中的 Hadoop 安装文档，内容为“yarn-site.xml”的配置说明。
画面9：展示 yarn-site.xml 文件中配置 YARN 的日志聚合和资源参数。
画面10：展示 Typora 中的 Hadoop 安装文档，内容为“创建数据和临时文件夹”和“分发安装包到其它机器”的步骤。
画面11：在 SecureCRT 中执行命令，创建 Hadoop 各个组件所需的目录。
画面12：在 SecureCRT 中尝试从镜像站点下载 Hadoop 安装包，但连接被拒绝。
画面13：在 SecureCRT 中设置环境变量，包括 JAVA_HOME、HADOOP_HOME 和 PATH。
画面14：在 SecureCRT 中在 node03 上执行 source /etc/profile 命令，使环境变量生效。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. See accompanying LICENSE file.
<!-- Put site-specific property overrides in this file. -->
</configuration>
```

画面2：
```bash
export HADOOP_OS_TYPE=$(uname -s)
case $HADOOP_OS_TYPE in
Darwin*)
export HADOOP_OPTS="${HADOOP_OPTS} -Djava.security.krb5.realm="
export HADOOP_OPTS="${HADOOP_OPTS} -Djava.security.krb5.kdc="
export HADOOP_OPTS="${HADOOP_OPTS} -Djava.security.krb5.conf="
;;
```

画面3：
```bash
export JAVA_HOME=/export/servers/JDK 8.0_141
```

画面4：
```xml
<configuration>
<property>
<name>dfs.namenode.name.dir</name>
<value>file:///export/servers/Hadoop-3.1.1/data/namenode/namenodedatas</value>
</property>
<property>
<name>dfs.namenode.handler.count</name>
<value>10</value>
</property>
<property>
<name>dfs.datanode.data.dir</name>
<value>file:///export/servers/Hadoop-3.1.1/data/datanode/datanodedatas</value>
</property>
<property>
<name>dfs.namenode.http.address</name>
<value>node01.Hadoop.com:50070</value>
</property>
</configuration>
```

画面5：
```xml
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
<value>file:///export/servers/Hadoop-3.1.1/data/dfs/nn/snn/edits</value>
</property>
<property>
<name>dfs.namenode.secondary.http-address</name>
<value>node01.Hadoop.com:50090</value>
</property>
<property>
<name>dfs.namenode.checkpoint.dir</name>
<value>file:///export/servers/Hadoop-3.1.1/data/dfs/snn/name</value>
</property>
```

画面6：
```xml
<configuration>
<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>
<property>
<name>mapreduce.map.memory.mb</name>
<value>1024</value>
</property>
<property>
<name>mapreduce.reduce.memory.mb</name>
<value>1024</value>
</property>
<property>
<name>mapreduce.map.java.opts</name>
<value>-Xmx512M</value>
</property>
<property>
<name>mapreduce.reduce.java.opts</name>
<value>-Xmx512M</value>
</property>
<property>
<name>mapreduce.task.io.sort.mb</name>
<value>256</value>
</property>
<property>
<name>mapreduce.task.io.sort.factor</name>
<value>100</value>
</property>
<property>
<name>mapreduce.reduce.shuffle.parallelcopies</name>
<value>25</value>
</property>
<property>
<name>mapreduce.jobhistory.address</name>
<value>node01.Hadoop.com:10020</value>
</property>
</configuration>
```

画面7：
```xml
<property>
<name>mapreduce.reduce.memory.mb</name>
<value>1024</value>
</property>
<property>
<name>mapreduce.reduce.java.opts</name>
<value>-Xmx512M</value>
</property>
<property>
<name>mapreduce.task.io.sort.mb</name>
<value>256</value>
</property>
<property>
<name>mapreduce.task.io.sort.factor</name>
<value>100</value>
</property>
<property>
<name>mapreduce.reduce.shuffle.parallelcopies</name>
<value>25</value>
</property>
<property>
<name>mapreduce.jobhistory.address</name>
<value>node01.Hadoop.com:10020</value>
</property>
```

画面8：
```xml
<property>
<name>yarn.nodemanager.vmem-check-enabled</name>
<value>false</value>
</property>
<property>
<name>yarn.nodemanager.resource.memory-mb</name>
<value>1024</value>
</property>
<property>
<name>yarn.nodemanager.resource.detect.hardware.capabilities</name>
<value>true</value>
</property>
<property>
<name>yarn.nodemanager.local-dirs</name>
<value>file:///export/servers/Hadoop-3.1.1/data/nodemanager/nodemanagerDatas</value>
</property>
<property>
<name>yarn.nodemanager.log-dirs</name>
<value>file:///export/servers/Hadoop-3.1.1/data/nodemanager/nodemanagerLogs</value>
</property>
<property>
<name>yarn.nodemanager.log.retain-seconds</name>
<value>10000</value>
</property>
```

画面9：
```xml
<property>
<name>yarn.nodemanager.remote-app-log-dir</name>
<value>/export/servers/Hadoop-3.1.1/data/remoteAppLogs</value>
</property>
<property>
<name>yarn.nodemanager.remote-app-log-dir-suffix</name>
<value>logs</value>
</property>
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
<property>
<name>yarn.log-aggregation.retain-seconds</name>
<value>18144000</value>
</property>
<property>
<name>yarn.log-aggregation.retain-check-interval-seconds</name>
<value>86400</value>
</property>
<property>
<name>yarn.app.mapreduce.am.resource.mb</name>
<value>1024</value>
</property>
```

画面10：
```text
3. 创建数据和临时文件夹
mkdir -p /export/servers/Hadoop-3.1.1/data/dfs/nn/snn/edits
mkdir -p /export/servers/Hadoop-3.1.1/data/namenode/namenodedatas
mkdir -p /export/servers/Hadoop-3.1.1/data/datanode/datanodedatas
mkdir -p /export/servers/Hadoop-3.1.1

