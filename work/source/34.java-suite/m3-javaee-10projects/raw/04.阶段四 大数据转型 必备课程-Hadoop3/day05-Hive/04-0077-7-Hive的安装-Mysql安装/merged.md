# 7-Hive的安装-Mysql安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\7-Hive的安装-Mysql安装【海量资源尽在 ubkz.com】.mp4
- 时长 4分59秒（音频 299s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来呢我们来安装这个Hive那么安装Hive呢首先要去得到一个一个压缩包那这个呢是一个压缩包的一个下载地址我们用的是Hive 3.1.1这个版本大家请注意我们的Hadoop呢用的是3.0以上版本那么我们的Hive也应该使用3.0以上版本否则呢它会出现版本不兼容问题有了这个压缩包之后呢
[00:29] 我们要将它呢上传到我们的服务器上然后上传到XPOW的software这个目录然后呢给它解压解压到我们的XPOW的Service目录好那在这里呢我已经把这个压缩包呢提前下载好了我们直接来上传好我的压缩包呢在我们的桌面上我把它呢直接上传一下在这里好稍等这个呢有几百兆的大小所以说需要一定时间
[00:59] 我们稍等好已经上传成功之后呢我们来解压我们的解压到export Service这个目录来我们来做他svf apache然后呢-c...Service这个目录稍等好解压完之后呢我们回到Service这个目录好来到这里之后呢我们来进到apache have这个目录进到这个目录之后呢
[01:32] 相当于我们这个压缩包呢已经解压完了解压完之后呢接下来我们要做下一步我们要装一个mycircle为什么需要装这个mycircle呢因为我们的Hive呢它是有原数据的我们的原数据呢要存在这个mycircle里边其实呢Hive有一个默认的一个存放原数据的一个数据库叫derby那个呢数据库有一个缺陷所以说呢我们用mycircle来替换掉它
[02:00] 那么怎么去装MySQL呢我们在这里呢采用的是在线安装好我们来一步一步来做先看第一步需要装了这么一些一些组件来我们把它直接复制然后呢在这里直接安装好回上稍等它正在安装好开始了这个安装的速度呢跟你的网速呢是相关的好这里呢它说需要12兆那我先yes好
[02:33] 说个Y稍等它开始下载好那么下载完之后继续去下载别的一些包让它安装好经过漫长的等待呢我们这个终于安装好了MySQL安装好之后呢我们还要去做一些这个配置我们先来启动这个服务来启动我们的MySQL服务来在这里稍等启动完服务之后呢接下来我们要去通过MySQL自带的脚本对它进行设置
[03:16] 来我们来这里来看一下好在这里呢我们来直接运行这个自带脚本他说呢需要输入现在的密码我们装完之后他是没有密码的没有密码的直接回车OK好了他说是否要设置密码yes在这里呢我们的新密码123456好再输入密码123456他这个地方他说是否要移除匿名用户我们可以输个y
[03:46] 好他说呢不允许root远程访问我们写个一定要写个n就no的意思允许他远程远程登录好那接下来他说移除这个测试数据库呢to test也可以写nook他说呢重新加载这个表的重新加载权限表你可以说yesok这个我们就设置完了好设置完了之后呢我们来接下来我们需要呢
[04:16] 进到mycircle里边呢做一些授权来我们在这里mycircle-uroot-p这个密码123456好回来回来之后呢我们做一个授权就是把它的远程访问权限给开启好在这里呢直接回车就行了好回车完之后呢我们在这里呢刷新一下这个权限OK来那这个时候呢
[04:46] 基本上我们的MySQL就配置完了我们来退出好那么MySQL配置完了之后呢接下来我们需要对Hive进行配置好那么我们先来暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 Linux 服务器上安装 Hive 3.1.1 及其依赖的 MySQL 数据库环境。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Typora 文档中“2.5 Hive 的安装”章节，内容包括 Hive 下载地址、安装步骤（上传并解压安装包、安装 MySQL）。
- 文档中列出的命令：
  cd /export/software/
  tar zxvf apache-Hive-3.1.1-bin.tar.gz -C /export/software/
- 文档中列出的 MySQL 安装命令：
  yum install mysql mysql-server mysql-devel
  /etc/init.d/mysql start

画面 2：
- 展示了 Hive 安装包解压后目录下的部分 JAR 文件列表，包括 flatabuffers、arrow-memory、netty-buffer、Hadoop-bundle、Hive-metastore、commons-collections、commons-pool、antlr-runtime、derby、datanucleus-core、datanucleus-rdbms 等。

画面 3：
- 展示了在服务器上切换目录至 /servers/，并进入 Hive 安装目录的命令：
  [root@node03 software]# cd ../servers/
  [root@node03 servers]# cd apache-Hive-3.1.1-bin/

画面 4：
- 展示了 Typora 文档中“2.5 Hive 的安装”章节，内容包括 Hive 下载地址、安装步骤（上传并解压安装包、安装 MySQL）。
- 文档中列出的 MySQL 安装命令：
  yum install mysql mysql-server mysql-devel
  /etc/init.d/mysql start

画面 5：
- 展示了在服务器上执行 yum 安装 MySQL 及其依赖包的命令：
  [root@node03 apache-Hive-3.1.1-bin]# yum install mysql mysql-server mysql-devel

画面 6：
- 展示了 yum 安装过程中的事务摘要：
  Transaction Summary
  Install  11 Package(s)
  Upgrade  4 Package(s)
  Total download size: 12 M
  Is this ok [y/N]: y

画面 7：
- 展示了 yum 安装完成后，系统提示“Complete!”，并显示已安装的 MySQL 相关包及更新的依赖包列表，包括 mysql、mysql-devel、mysql-server、keyutils-libs-devel、libcom_err、libsepol-devel、perl-DBD-MySQL、krb5-devel、libselinux-devel、openssl-devel、libss 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
cd /export/software/
tar zxvf apache-Hive-3.1.1-bin.tar.gz -C /export/software/
yum install mysql mysql-server mysql-devel
/etc/init.d/mysql start

画面 2：
apache-Hive-3.1.1-bin/lib/flatabuffers-1.2.0-3f79e055.jar
apache-Hive-3.1.1-bin/lib/arrow-memory-0.8.0.jar
apache-Hive-3.1.1-bin/lib/netty-buffer-4.1.17.Final.jar
apache-Hive-3.1.1-bin/lib/netty-common-4.1.17.Final.jar
apache-Hive-3.1.1-bin/lib/hppc-0.7.2.jar
apache-Hive-3.1.1-bin/lib/opencv-2.3.jar
apache-Hive-3.1.1-bin/lib/parquet-Hadoop-bundle-1.10.0.jar
apache-Hive-3.1.1-bin/lib/Hive-metastore-3.1.1.jar
apache-Hive-3.1.1-bin/lib/Hive-standalone-metastore-3.1.1.jar
apache-Hive-3.1.1-bin/lib/bonecp-0.8.0.RELEASE.jar
apache-Hive-3.1.1-bin/lib/HikariCP-2.6.1.jar
apache-Hive-3.1.1-bin/lib/commons-collections-3.2.2.jar
apache-Hive-3.1.1-bin/lib/commons-collections-3.2.2.jar
apache-Hive-3.1.1-bin/lib/commons-pool-1.5.4.jar
apache-Hive-3.1.1-bin/lib/antlr-runtime-3.5.2.jar
apache-Hive-3.1.1-bin/lib/derby-10.14.1.0.jar
apache-Hive-3.1.1-bin/lib/datanucleus-api-jdo-4.2.4.jar
apache-Hive-3.1.1-bin/lib/datanucleus-core-4.1.17.jar
apache-Hive-3.1.1-bin/lib/datanucleus-rdbms-4.1.19.jar

画面 3：
[root@node03 software]# cd ../servers/
[root@node03 servers]# cd apache-Hive-3.1.1-bin/

画面 4：
yum install mysql mysql-server mysql-devel
/etc/init.d/mysql start

画面 5：
[root@node03 apache-Hive-3.1.1-bin]# yum install mysql mysql-server mysql-devel

画面 6：
Transaction Summary
Install  11 Package(s)
Upgrade  4 Package(s)
Total download size: 12 M
Is this ok [y/N]: y

画面 7：
Verifying : e2fsprogs-1.41.12-23.el6.x86_64
Verifying : libcom_err-1.41.12-23.el6.x86_64
Verifying : libsepol-1.41.12-23.el6.x86_64
Verifying : e2fsprogs-libs-1.41.12-23.el6.x86_64
Verifying : libcom_err-1.41.12-23.el6.x86_64
Verifying : libsepol-1.41.12-23.el6.x86_64
Verifying : e2fsprogs-libs-1.41.12-23.el6.x86_64
Installed:
mysql.x86_64 0:5.1.73-8.el6_8
mysql-devel.x86_64 0:5.1.73-8.el6_8
mysql-server.x86_64 0:5.1.73-8.el6_8
Dependency Installed:
keyutils-libs-devel.x86_64 0:1.4-5.el6
libcom_err.x86_64 0:1.41-12-24.el6
libsepol-devel.x86_64 0:2.0.41-4.el6
perl-DBD-MySQL.x86_64 0:4.013-3.el6
krb5-devel.x86_64 0:1.10.3-65.el6
libselinux-devel.x86_64 0:2.0.94-7.el6
openssl-devel.x86_64 0:1.0.1e-57.el6
libss.x86_64 0:1.41.12-24.el6
Dependency Updated:
e2fsprogs.x86_64 0:1.41.12-24.el6
e2fsprogs-libs.x86_64 0:1.41.12-24.el6
libcom_err.x86_64 0:1.41.12-24.el6
libss.x86_64 0:1.41.12-24.el6

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

