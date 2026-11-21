# 11-sqoop安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\11-sqoop安装【海量资源尽在 ubkz.com】.mp4
- 时长 5分42秒（音频 343s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来安装scope我们刚才说过呢scope有两个版本一个是scope1一个是scope2那我们在这里呢安装的是scope1因为呢这个版本在企业中用的最多那么这里边呢有一个下载地址下面呢还给大家提供了一个详细的下载地址这个呢是scope1的我们用的是scope1.4.7这个版本下面是scope2的有兴趣的同学呢可以自己去下载
[00:30] 好那么接下来我们来装scope1这个安装包呢我已经下载过了我呢把它上传到我们的集群上来打开我们的Linux我回到exportsoftware这个目录好在这里呢我来上传一个在桌面上好在这里呢有一个叫scope1.4.7好添加一下稍等好添加完之后呢
[01:01] 我们需要将它解压解压到Service目录照着这个scope解压到-c然后点点-Service目录稍等解压完之后我们回到Service目录接下来呢就对这个scope进行配置来我们来看讲义看怎么配置首先第二步来配置配置的话呢我们需要配置一个文件叫scopeenv.sh它在conf目录下面
[01:33] 我们来看一下在这里我们进到这个进到这个Scope下面进到之后呢我们再进入这个Scope这个目录在这个Scope目录下面呢有一个有一个Scope Invert我们来看一下有没有这里没有这里没有的话呢我们需要将一个模板拷贝一下这个模板就是它我们来拷一下CP Scope Invert
[02:04] 然后呢sh我们来考一个scope因为好把后面的去掉然后呢.sh应该是这个文件我们来看一下好拷贝成scope-envy然后呢去配置Hadoop-comment-home还有Hadoop-my-predic-home还有have-home我们来分别来做一下好在这里的话我们打开这个文件scope因为.sh进来进来之后呢我们先找到
[02:36] Hadoop Common Home这个地方呢我们要去把Hadoop的一个路径呢拷在这里来我打开这个我们来进入这个Export ServiceHadoop好这个我们要把这个路径呢拷贝法一定要确认它没有问题放在后面好那接下来还有一个Export的MapreadExport的HadoopMapread Home这个呢和上面这个路径是一样的我们也拷到这里
[03:12] 搞错了好站在它的后面好站在这个位置那接下来呢还有一个这个是HBs我们不管我们没有配还有一个Hive Home那这个很显然我们要去指定Hive所在的位置OK那我们来找一下Hive回到上一集我们的Hive在哪里呢我们的Hive来找一下这个R87 HiveR87 Hive 3.31应该是这个我们来看一下
[03:46] 好把这个路径呢也复制一下回来站在这里好那么到这里的话呢我们把这个三个参数已经配好了好配好之后我们来保存推出好之后呢接下来我们来进行下一步回到讲义在这里的话呢我们还要加入两个额外的依赖包一个是JavaJSON包一个是一个是这个我们的MySQL的驱动包我们要把这两个加包呢放在scope的一个lab下面
[04:16] 来我们来看一下回到上一集进到这个lab下面这里边呢我们要去导入两个包这两个包我已经放在桌面了我直接把它导进来在桌面上一个是java json一个是mycircle的驱动包我来添加一下OK已经添加成功添加成功之后呢我们来看下一步那这个地方呢我们就做完了做完之后呢我们来验证一下我们这个
[04:47] scope的一个启动这里边呢这个地方不对我再改一下吧把这个路径呢给它复制一下应该是这个路径把它放在这个位置我们要进到这个路径然后呢在这下面运行一个binscope version就可以了来回到上一集进到这个主目录下面然后在这个主目录下面运行一个bin好把它给我删掉再复制一份回来在这里运行bin
[05:23] 稍等好那么这个时候呢你看这个地方呢出现了这么多信息基本上呢相当于我们这个Hive呢就这个我们这个scope呢就配置成功了那么关于呢scope的安装呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Linux服务器上安装并配置Sqoop工具，包括下载解压、修改配置文件和添加依赖包。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Sqoop安装章节，列出下载地址和解压命令。
画面2：在SecureCRT中，用户正在传输sqoop-1.4.7.bin_hadoop-2.6.0.tar.gz文件。
画面3：在SecureCRT中，用户列出并进入sqoop解压后的目录。
画面4：在SecureCRT中，用户进入sqoop的scripts目录。
画面5：在SecureCRT中，用户进入sqoop的conf目录。
画面6：在SecureCRT中，用户进入Hadoop的mapreduce目录。
画面7：在SecureCRT中，显示Hadoop环境变量配置文件的开头部分。
画面8：在SecureCRT中，用户正在编辑Hadoop环境变量配置文件，设置HIVE_HOME。
画面9：在SecureCRT中，用户完成编辑并保存了sqoop-env.sh配置文件。
画面10：在SecureCRT中，用户正在使用rz命令传输文件，弹出Zmodem传输窗口。
画面11：展示PPT页面，说明Sqoop需要添加mysql和java-json的依赖包，并给出验证启动命令。
画面12：展示PPT页面，说明Sqoop需要添加mysql和java-json的依赖包，并给出验证启动命令。
画面13：在SecureCRT中，用户进入sqoop的lib目录。
画面14：在SecureCRT中，用户执行sqoop-version命令，显示Sqoop版本信息和警告信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
http://archive.apache.org/dist/sqoop/1.4.7
http://archive.apache.org/dist/sqoop/1.4.7_bin_hadoop-2.6.0.tar.gz
http://archive.apache.org/dist/sqoop/1.99.6/sqoop-1.99.6-bin_hadoop200.tar.gz
我们这里使用sqoop1的版本，下载之后上传到/export/export/software目录下，然后进行解压
cd /export/servers/Hadoop-3.1.1/conf

画面2：
rz waiting to receive.
Transferring sqoop-1.4.7.bin_hadoop-2.6.0 (1).tar.gz...

画面3：
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/bin/Hive.cmd
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/createOnlyImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/customOverwriteImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/decimalMapImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/failingImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/fieldWithNewlineImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/incrementalHiveAppend10.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/incrementalHiveAppend20.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/incrementalHiveAppendEmpty.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/normalImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/numericImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/partitionImport.q

画面4：
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/Hive/scripts/partitionImport.q
[root@node03 software]# cd ../servers/
[root@node03 servers]# ls
apache-flume-1.8.0-bin
azkaban-solo-server-0.1.0-SNAPSHOT.tar.gz
azkaban-web-server-0.1.0-SNAPSHOT.tar.gz
azkaban-exec-server-0.1.0-SNAPSHOT.tar.gz
create-all-sql-0.1.0-SNAPSHOT.sql
sqoop-1.4.7.bin_hadoop-2.6.0
Hadoop-3.1.1-bin
Hive sql
taillog
ZooKeeper-3.4.9

画面5：
[root@node03 servers]# cd /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/
[root@node03 sqoop-1.4.7.bin_hadoop-2.6.0]# cd conf/
[root@node03 conf]# ls
oraop-site-template.cmd
sqoop-env-template.sh
sqoop-site.xml
sqoop-env.sh

画面6：
[root@node03 share]# cd Hadoop/
[root@node03 Hadoop]# s
-bash: s: command not found
[root@node03 Hadoop]# ls
client common hdfs mapreduce tools yarn
[root@node03 mapreduce]# ls
Hadoop-mapreduce-client-shuffle-3.1.1.jar
Hadoop-mapreduce-client-3.1.1.jar
Hadoop-mapreduce-client-core-3.1.1.jar
Hadoop-mapreduce-client-hs-plugins-3.1.1.jar
Hadoop-mapreduce-client-jobclient-3.1.1-tests.jar
Hadoop-mapreduce-client-nativetask-3.1.1.jar

画面7：
# limitations under the License.
# included in all the Hadoop scripts with source command
# should not be executable directly
# also should not be passed any arguments, since we need original $*
# Set Hadoop-specific environment variables here.
#Set path to where bin/Hadoop is available
export HADOOP_COMMON_HOME=/export/servers/Hadoop-3.1.1
#Set path to where Hadoop-*core.jar is available
export HADOOP_MAPRED_HOME=/export/servers/Hadoop-3.1.1
#Set the path to where bin/hbase is available
#export HBASE_HOME=

画面8：
# should not be executable directly
# also should not be passed any arguments, since we need original $*
# Set Hadoop-specific environment variables here.
#Set path to where bin/Hadoop is available
export HADOOP_COMMON_HOME=/export/servers/Hadoop-3.1.1
#Set path to where Hadoop-*core.jar is available
export HADOOP_MAPRED_HOME=/export/servers/Hadoop-3.1.1
#Set the path to where bin/hbase is available
#export HBASE_HOME=
#Set the path to where bin/Hive is available
export HIVE_HOME=

画面9：
#Set the path to where bin/Hive is available
export HIVE_HOME=/export/servers/apache-Hive-3.1.1-bin
"sqoop-env.sh" 35L, 1435C written
[root@node03 conf]#

画面11：
mysql-connector-java-5.1.40.jar
java-json.jar
将这两个jar也添加到sqoop的lib目录下
4、验证启动
cd /export/servers/sqoop-1.4.6-cdh5.14.0
bin/sqoop-version

画面14：
Warning: /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/bin/../hbase does not exist! HBase imports will fail.
Please set $HBASE_HOME to the root of your HBase installation.
Warning: /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/bin/../hcatalog does not exist! HCatalog jobs will fail.
Warning: /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/bin/../accumulo does not exist! Accumulo imports will fail.
Please set $ACCUMULO_HOME to the root of your Accumulo installation.
Warning: /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/bin/../ZooKeeper does not exist! Accumulo imports will fail.
Please set $ZOOKEEPER_HOME to the root of your Zookeeper installation.
2019-05-12 19:57:59,375 INFO sqoop: Sqoop: Running Sqoop version: 1.4.7
git commit id 2328971411f57f0cb683db79d44d195d88
Compiled by maugli on Thu Dec 21 15:59:58 STD 2017

4) 出现的 PPT 标题、架构图/流程图

