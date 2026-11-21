# 16-HDFS的API操作-访问权限问题

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\16-HDFS的API操作-访问权限问题【海量资源尽在 ubkz.com】.mp4
- 时长 11分47秒（音频 707s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 学习完HDFS的文件上传和下载之后接下来我们来看一下HDFS的文件的访问权限问题好 我们来看一下HDFS在这里每一个文件它的前面都有一个访问权限你比如说这个timer.txt它是当前所属用户可读可写所属用户组可以读而其他用户也是可以读的其实这个权限对我们来讲是没有任何意义的
[00:29] 为什么呢是因为当初呀我们在配置Hadoop的时候我们把这个访问权限已经给关闭了那怎么说呢我们来看在我们的这个Hadoop export serviceHadoop里边呢有一个目录ETC下面一个Hadoop那这里边呢有个配置文件叫HDFSset插面我们来看在这里有一个DFS permission.enable
[00:57] 这地方我们设的是false也就是说关闭它的权限检查所以说呢你刚才设的任何权限对我们来访问是没有任何影响的那不行我们来试一下那比如说啊我去修改这个timertxt我把它的可读权限都给去掉那我们来试一下hdfs dfs-chini-mod修改权限我狠一点我把它的所有权限都给去掉设成三个零然后呢
[01:27] 这个地方是timer.tst我们来试一下我们来直接回撤回撤之后呢我们来看一下这个地方呢刷一下你会发现这个文件的所有权限都没有了没有了之后呢你说我们能不能对这个文件进行操作呢其实是可以的来我们来看一下比如说我打开刚才这个代码这个里面有个文件的下载我还是去下载这个文件你只要能下载
[01:58] 说明你可以对这个文件是不是进行操作OK那这里呢我一盘里边应该有已经有了这个文件我修改成time2time2来我们看能不能下载执行稍等好没有问题没有问题之后呢咱们回到一盘来看这多了一个time2的2的txtOK文件内容也没有问题说明呢你刚才的设的这个权限对我毫无影响原因很简单就是我们刚才说过了
[02:35] 这个权限根本就没有打开那接下来呢我们可不可以把这个文件权限打开呢是可以的但是打开这个文件权限之前呀我们需要做一件事情需要把我们的这个集群呢给它停止因为呢只有停止重启之后呢它才能生效好接下来呢我把我的这个集群呢给它停一下好在这里呢我来看在export Service Hadoop在这里边我们来输一个
[03:04] 说一个什么呢SB下面呢有一个有一个stop有一个stop DFSSH我们把它停止好 稍等它在停止NameNodeDataNodeSecondNameNodeGPS一下好 这个时候呢我们把它停了停了之后呢这个地方还有一个jobHistory是吧那这个地方我们可以只用q-9然后呢这个地方3915go
[03:39] 把它杀死了好也没有了没有之后呢咱们再停止这个ERG去Sbin下面有个stopERSH停止好稍等我们GPS一下就剩一个Zokeper来接下来我们看第二台GPS好这里边也剩一个Zokeper第三台GPS好也剩一个Zokeper好停止了停止之后呢接下来我们要修改那个配置文件
[04:12] 我们回到ETC下面有一个Hadoop进来我们来打开刚才的权限就是HDFS set的插庙HDFS的插庙进来好进来之后呢把这个位置呢修改成除就行了改成除好改成除了之后呢你这一台机子改了另外两台机子是不是要跟着改所以说我接下来我要将这个文件分发SCP把这个HDFS的插庙呢
[04:42] 分发给node02这个机子然后呢$pwd分发给它OK我要给它分发这个第三台机子好分发完了之后呢接下来我要把这个机群重新启动来重新启动回到我们的上一机回到我们这里主目录SB下面呢有一个有一个什么呢start dfs sh好启动一下
[05:18] 稍等稍等它正在启动已经启动完了启动完之后咱GPS一下好Name nodeData nodeSecondary name node已经起来了好起来之后呢我们再看这一台GPS好Data node再看这一台GPS好Data node也已经起来了好起来之后呢咱再启动这个Yard继续Stamp Yard启动这个好稍等好起来起来就GPS一下
[06:14] 好这个地方呢是resource managernode manager看这一台gps好起来node manager再看gps好node manager没有问题好起完起来之后呢接下来呢我们相当于把刚才的权限访问给开启了开启之后呢大家注意这个文件呢稍等我来刷新一下这个文件是没有任何访问权限的那么我们来试一下再次访问的时候看他能不能哎访问
[06:44] 那这个地方呢我给它修改成timersunder.txt我们来运行这段代码走稍等稍等你会发现它报错了报错的原因呢很简单就是因为我们的权限不够的问题你看这地方有个permission denied就是权限拒绝也就是说我们刚才对这个权限的修改是不是引起作用了OK这就是它这个权限问题好那么这个权限问题有了之后呢
[07:18] 你如何能够访问这个文件呢很简单我们需要去修改它的权限你比如说呢我们可以给它加个权限hdfs然后hdfs然后呢这个地方是dfs-chengji-mod比如说呢我现在是root用户我要想访问这个权限访问这个文件呢我的所属用户是root我只需要给它加个读写权限是不是就可以了比如说我chengji-mod-什么呢这个读写
[07:48] rw是600ok600然后呢是一个timer.tst我们来试一下给它加一个可读可写ok好加完之后呢我们来再刷新一下走来刷新一下刷新之后呢我们来再运行刚才的程序来执行一下看可不可以操作稍等好这地方它还是它还是报错还是说什么呢你看
[08:23] 他说呢这个地方呃我的访问拒绝哎你看有个问题他刚才这个地方呢他说有一个user是RFT然后呢权限是是只读这个什么意思呢大家注意你看我这个文件呢我的所属用户是rote那这个权限表示只有是rote用户是不是才能对这个文件进行可可读可写但是我现在在温度的平台运行的而我温度的平台的用户呢
[08:52] 它不是肉糖它是什么呢它是RFT我的温度的系统我的用户是RFT所以说你看他在这说了他说你的用户是RFT你是不能对这个文件进行权限访问的那好了那接下来我们需要怎么做呢我们需要再给他加权限比如说我加三个6意思就是说当前的所属用户和其他用户呢都具有可读可写的一个权限来那这时候呢我们来再看
[09:21] 来我们再执行这个代码走稍等哎你看没有问题也就是说呢我把它全线修改完之后呢我虽然是用户是LFT来访问但是呢你只需要给他加了这个全线那他是不是依然可以访问呀好接下来我们把它全线再改回去我就改成600就改成也就是说只有肉头用户才能访问我的这个文件那么现在问题又来了
[09:56] 我现在呢我只有所属用户才可以可读可写但是我现在的用户是RFT我就想访问怎么办呢这里边有一个伪造用户的问题什么意思呢就是说我可以root用户的身份呢去访问这个文件那怎么做呢我们来看讲义这里边呢有一个有一个参数就是说我们呢在这个获取这个文件对象的时候呢fail system这个对象的时候呢我们可以在后面加一个参数
[10:24] 这个参数就是你以谁的身份去访问那这个地方呢我们可以加个参数比如说呢我可以在我的这个代码里面呢在获取这个fail system对象的时候这边可以加个参数加什么参数呢route用户我以route用户的方式呢去访问那这个时候即使呢我是LFT用户那我说我以route用户的身份去访问那这个就叫伪造用户这个呢
[10:53] 也是可以的我们来试一下你看现在呢只有Root用户才能访问我现在呢伪造一个Root用户来我们来试一下走来试一下稍等你发现也没有问题也就是说如果你访问HDFS上的一个文件那要想访问要保证权限没有问题有两种做法第一种呢你在这里呢通过清洁Mode去修改对应的权限另外一种做法呢你可以通过
[11:28] 代码的方式来伪造一个用户来同样也可以去访问但是前提呢你的这个配置文件这个总权限呢要打开就是刚才我说过的这个权限呢要收为处它才能生效好了这就是它的权限访问问题我们呢就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过修改Hadoop配置文件hdfs-site.xml启用文件权限控制，并演示了因权限不足导致的文件下载失败案例。

2) 按时间顺序列出每张画面的要点：
画面1：显示HDFS文件系统浏览器界面，列出根目录下的文件，包括a.txt、app、export、hello.txt、test、timer.txt、tmp、user等文件，所有文件的Owner和Group信息可见。
画面2：IDEA中显示Java代码，演示如何通过FileSystem对象下载HDFS文件到本地，代码中使用了URI("hdfs://node01:8020")。
画面3：SecureCRT终端中显示hdfs-site.xml配置片段，包含dfs.replication=3、dfs.permissions.enabled=false、dfs.namenode.checkpoint.edits.dir配置，以及执行了chmod命令修改timer.txt权限。
画面4：SecureCRT终端中显示cd进入Hadoop-3.1.1/sbin目录，执行了ls命令列出脚本文件，随后执行了jps命令查看进程，显示了NameNode、DataNode等进程。
画面5：SecureCRT终端中显示cd进入etc/Hadoop目录，ls命令列出配置文件，其中hdfs-site.xml被高亮选中。
画面6：SecureCRT终端中显示scp命令将hdfs-site.xml复制到node02和node03节点，随后cd ..并执行ls命令。
画面7：SecureCRT终端中显示在node02节点上执行jps命令，输出了DataNode进程信息。
画面8：IDEA中显示Java代码，演示下载文件，但运行结果提示测试失败，错误信息显示“Process finished with exit code -1”。
画面9：SecureCRT终端中显示启动SecondaryNameNode、NameNode、ResourceManager、NodeManager等进程，随后执行hdfs dfs -chmod命令。
画面10：IDEA中显示Java代码，演示下载文件，但运行结果提示测试失败，错误信息显示“AccessControlException: Permission denied: user=ift, access=READ, inode='timer.txt':root:supergroup:rw-------”。
画面11：IDEA中显示Java代码，演示下载文件，但运行结果提示测试失败，错误信息显示“AccessControlException: Permission denied: user=ift, access=READ, inode='timer.txt':root:supergroup:rw-------”。
画面12：HDFS文件系统浏览器界面，显示文件列表，其中timer.txt的Owner为root。
画面13：HDFS文件系统浏览器界面，显示文件列表，其中timer.txt的Owner为root。
画面14：SecureCRT终端中显示hdfs-site.xml配置片段，其中dfs.permissions.enabled被修改为true，随后执行了scp命令将配置文件复制到node02和node03节点。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面3：
```xml
<value>node01:50070</value>
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
<value>file:///export/servers/Hadoop-3.1.1/datafs/nm/snn/edits</value>
</property>
```
画面5：
```bash
[root@node01 Hadoop-3.1.1]# ls
capacity-scheduler.xml httpfs-log4j.properties mapred-site.xml
configuration.xml httpfs-site.xml ssl-client.xml.example
core-site.xml kms-acls.xml ssl-server.xml.example
Hadoop-env.cmd kms-log4j.properties user_ec_policies.xml.template
Hadoop-env.sh kms-site.xml yarn-env.cmd
Hadoop-metrics2.properties log4j.properties yarn-env.sh
Hadoop-policy.xml mapred-env.cmd yarn-Service-log4j.properties
hdfs-site.xml mapred-queues.xml.template yarn-site.xml
```
画面6：
```bash
"hd fs-site.xml" 65L, 2031C written
[root@node01 Hadoop]# scp hdfs-site.xml node02:$PWD
100% 2031 2.0KB/s 00:00
[root@node01 Hadoop]# scp hdfs-site.xml node03:$PWD
100% 2031 2.0KB/s 00:00
[root@node01 etc]# ls
abc.txt a.txt bin dates etc include lib libexec LICENSE.txt logs NOTICE.txt README.txt sbin share
```
画面14：
```xml
<value>node01:50070</value>
<property>
<name>dfs.replication</name>
<value>3</value>
</property>
<property>
<name>dfs.permissions.enabled</name>
<value>true</value>
</property>
<property>
<name>dfs.namenode.checkpoint.edits.dir</name>
<value>file:///export/servers/Hadoop-3.1.1/datafs/nm/snn/edits</value>
</property>
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无

5) 画面里出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无

