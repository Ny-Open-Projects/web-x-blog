# 5-Azkaban-two_server模式-安装1

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\5-Azkaban-two_server模式-安装1【海量资源尽在 ubkz.com】.mp4
- 时长 9分58秒（音频 598s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习阿兹卡班的另外一种安装模式也叫To Server模式OK 这个模式的安装需要七步第一步我们需要去做一个准数据库的准备工作OK 那我们来去做一下首先我们需要登录MySQL数据库这个MySQL数据库的作用是用来存储我们阿兹卡班中产生的一些中间数据OK 我们来登录登录完之后给它复一些
[00:29] 全线来我们来做一下在这里我们打开我们的服务器好在这里我们拿到这个来登录我们的mycircle密码123456接下来呢我们需要去在这个里面创建一个数据库叫azkaban直接复制我来好创建完数据库之后呢我们来看我们需要创建一个用户创建一个用户这个用户呢是一个azkaban
[01:07] 然后呢给这个用户付所有权限来把它复制一下好这个地方找了一个东西我们来看一下这个应该是放在一起好给它付所有权限走好付完权限之后呢我们把这个权限刷新一下刷新一下来走一下然后呢我们接下来呢需要做一件事情在这个里边呢我们选择阿兹卡班这个数据库阿兹卡班
[01:48] 选择完这个数据库之后呢我们需要执行一个脚本这个脚本呢是我们编译后生成的一个脚本我们来找一下这个脚本编译完之后呢这个脚本我们把它复制到Export Software 4这个目录来我们打开另外一个中段在这里我们的脚本应该在哪里呢我们来找一下吧回到我的主目录好在这里应该是AzKaban一个DB我们来看一下
[02:18] 阿兹卡班这里边有一个dbdb这个目录进来进来之后应该有一个build我们来看一下是不是在这里build下面下面有一个install我们来进install在这个install里边有阿兹卡班db进来这里边应该有一个叫create all是这个吧我们来确认一下是一个create all circle0.1.0create all circle
[02:50] 我们需要把这个脚本呢我们拷贝到softwarexport software下面来cp一下create然后呢放到xport software下面去好拷贝完之后我们再回到刚才我们可以执行那个脚本执行完脚本之后呢它会在我这个阿兹卡班数据库中呢创建一些表我们来看一下把这个呢复制一下
[03:19] 这个src命令就是执行export software 4我们刚才拷贝的脚本前提是你这个脚本一定要拷到目录下面好 我们来回车它说这个地方不能执行不能执行的原因是什么呢应该是这个路径不能打开我看看我刚才拷的时候是software这个地方是software 4多了一个4这个地方路径不太一样
[03:47] 那我就直接回车好这样我们就把这个脚本执行完了执行完之后我们来看一下这里边一些表shoot table 4看一下你发现它给我们创建了很多表这些呢就是刚才那个脚本创建的好在这个文档里边呢我把这个地方改成software好这个第一步数据库的准备工作就做完了做完之后呢我们来做第二步解压压缩报解压什么呢我们
[04:15] 解压一个阿兹卡班web server和解压一个阿兹卡班esc serverok我们需要呢将这个两个压缩包呢分别放到software这个目录那么这两个压缩包在哪里呢我们来找一下好在这里在这里首先呢我们回到主目录回到我们的export Service这个地方阿兹卡班然后呢3.5.1好在这里好在这里的话呢我们
[04:47] 进到这个ESC ServerASKabanESC Server进到这里边进到这里边有个buildbuild里面有个distribution我们应该用的就是这个压缩包把它放在我们的software目录CP ASKaban然后呢这个地方是TR.gzcopy export software放在这个目录那么还要去copy一个东西copy一个东西ASKaban 3.5.1
[05:21] 好再进到这个web server也copy他那个压缩宝azkabanweb server好进来再进到build里边再进到distributions也把这个web server呢copy到software目录下面去cpazkaban贴压点gzcopy到export software好也拷进来了拷进来之后
[05:51] 我们去Sport Software看一下这个时候呢这个是我们刚才的一个这个是我们刚才的ESCC这个是我们刚才的这个Web Server我们拷过来拷过来之后呢分别解压怎么解压呢我们来看讲义那么拷贝完之后呢这个地方呢我们先解压把它解压到Service目录并且重命名一下好那我们来解压一下XVAF先解压ASKaban ESC Server
[06:23] 解压到我们的上一级目录Service这个目录走好解压完之后呢我们再来继续我们再解压一个阿兹卡曼web server然后呢解压到上一级的Service目录走好解压完之后呢我们回到上一级的Service目录好来了之后呢这个web server和esr都有了都有了之后呢我们分别对它进行重命名
[06:54] 这个名字太长我们重命名一下来我们来看首先第一个web server重命名web server 3.51.0来我们重命一下走那接下来再重命名一个这个esc server走重命名一下好那么来看一下这个时候一个是esc一个是web server这个重命完之后我们回到讲义接下来我们还需要安装一个
[07:28] SSH安全认证这个SSH呢是网络通信中的一个一种协议它保证我们网络通信的安全性那么装了这个安全协议之后呢我们以后再访问阿兹卡巴那个web服务的时候呢我们可以采用https这种方式而不是采用httpOK这个那接下来怎么做呢我们先回到这个主目录回到这个主目录来在这里回到主目录之后呢
[07:57] 我们需要运行这个命令这个命令呢把它拷贝过来我们要做一个安全认证这个K2呢是一个安全认证的一个工具来走一下回车好这个时候呢它让我输入这个密码这个K2的密码这个K2是一个安全认证的一个文件我们这个密码呢这里呢我们输密码的时候我们要输阿兹卡班这个地方一定要小心一点输完密码它是看不见的我们一个一个输
[08:27] 阿兹卡班好我说完了说完之后回车回车之后让你重复你刚才的密码阿兹卡班OK回车好这个时候呢它让你输入一些自己的信息那这个地方呢你可以直接回车它说你输入这个first and last name来回车一下那它说你输入你组织的名字OK回车回车好直接回车让你输入你所在的城市
[09:00] 回车所在的省可以回车好国家的一些这个什么两位数的编码走这地方呢他说呢他说你说的输的这些东西是否正确你这地方要输个yesok正确好走稍等然后接下来呢他又让你输入这个密码这个密码的话呢我们呢还是输入阿兹卡班要小心一点阿兹卡班好回车阿兹卡班
[09:30] 回车好如果输错的话呢可以重新运行这个命令好输完之后呢我们LS一下你会发现这里多了一个case到文件这个文件中呢存出了一些SSH它的一些安全的一些证书还有它的密钥都存在这个目录OK那到这里的话呢我们就把这个SSH安全认证呢给大家装好了OK那么我们把这个视频呢先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 环境下为 Azkaban 3.5.1.0 版本准备数据库、解压软件包并生成相关配置文件，为后续服务安装做准备。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 当前页面是课程 PPT，标题为“2.3 Azkaban 两个服务模式安装与使用”。
- 当前章节为“Step 1: 数据库准备”。
- 展示了 Azkaban 数据库安装目录下的 SQL 文件列表，其中 `create-all-sql-0.1.0-SNAPSHOT.sql` 文件被高亮选中。
- 提示文字：“Step 1: 数据库准备 进入mysql的客户端执行以下命令”。

画面 2：
- PPT 内容继续展示“Step 1: 数据库准备”和“Step 2: 解压软件包”。
- “Step 1”部分列出在 mysql 客户端执行的 SQL 命令：
  CREATE DATABASE azkaban;
  CREATE USER 'azkaban'@'%' IDENTIFIED BY 'azkaban';
  GRANT all privileges ON azkaban.* to 'azkaban'@'%' identified by 'azkaban' WITH GRANT OPTION;
  flush privileges;
  use azkaban;
  source /export/software/create-all-sql-0.1.0-SNAPSHOT.sql;
- “Step 2”部分列出“解压软件安装包”，并具体到“解压 azkaban-web-server”。

画面 3：
- PPT 内容与画面 2 相同，仅鼠标光标位置不同。

画面 4：
- 展示了在 SecureCRT 中执行 SQL 命令的终端界面。
- 命令执行结果：
  mysql> CREATE DATABASE azkaban;
  Query OK, 1 row affected (0.00 sec)
  mysql> CREATE USER 'azkaban'@'%' IDENTIFIED BY 'azkaban';
  Query OK, 0 rows affected (0.02 sec)
  mysql> GRANT all privileges ON azkaban.* to 'azkaban'@'%' identified by 'azkaban' WITH GRANT OPTION;
  Query OK, 0 rows affected (0.01 sec)
  mysql> flush privileges;
  Query OK, 0 rows affected (0.00 sec)
  mysql> use azkaban;
  Database changed
  mysql>

画面 5：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-3.5.1.0。
- 执行了命令：cd azkaban-exec-server/。
- 列出了 azkaban-exec-server 目录下的文件和子目录，包括 build.gradle、src、az-core、az-examples 等。

画面 6：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-db。
- 执行了命令：cp create-all-sql-0.1.0-SNAPSHOT.sql /export/software/。
- 列出了 azkaban-db 目录下的 SQL 文件列表。

画面 7：
- 展示了在 SecureCRT 中的终端界面。
- 显示了 SQL 命令执行后的结果，均为“Query OK, 0 rows affected (0.00 sec)”或“Query OK, 0 rows affected (0.01 sec)”。

画面 8：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-db。
- 执行了命令：cd ..。
- 列出了 azkaban-db 目录下的 SQL 文件列表。

画面 9：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-exec-server。
- 执行了命令：cd distributions/。
- 执行了命令：cp azkaban-exec-server-0.1.0-SNAPSHOT.tar.gz /export/software/。
- 列出了 distributions 目录下的文件。

画面 10：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 azkaban-web-server。
- 执行了命令：cd distributions/。
- 执行了命令：cp azkaban-web-server-0.1.0-SNAPSHOT.tar.gz /export/software/。
- 列出了 /export/software/ 目录下的文件，包括 azkaban-web-server-0.1.0-SNAPSHOT.tar.gz。

画面 11：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 /export/software。
- 执行了命令：mv azkaban-web-server-0.1.0-SNAPSHOT/ azkaban-web-server-3.5.1.0。
- 列出了 /servers/ 目录下的文件，包括 apache-flume-1.8.0-bin、azkaban-3.5.1.0、azkaban-exec-server-3.5.1.0 等。

画面 12：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 /servers。
- 执行了命令：cd /export/servers/azkaban-web-server-3.5.1.0。
- 列出了 /export/servers/azkaban-web-server-3.5.1.0 目录下的文件。

画面 13：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 /export/servers/azkaban-web-server-3.5.1.0。
- 执行了命令：keytool -keystore keystore -alias jetty -genkey -keyalg RSA。
- 系统提示输入密码和组织信息。

画面 14：
- 展示了在 SecureCRT 中的终端界面。
- 当前目录为 /export/servers/azkaban-web-server-3.5.1.0。
- 系统提示确认组织信息，用户输入“yes”。
- 系统提示输入密钥库密码，用户输入“RETURN”。
- 系统提示“Is CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown correct?”，用户输入“yes”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
- 无代码或配置。

画面 2：
- SQL 命令：
  CREATE DATABASE azkaban;
  CREATE USER 'azkaban'@'%' IDENTIFIED BY 'azkaban';
  GRANT all privileges ON azkaban.* to 'azkaban'@'%' identified by 'azkaban' WITH GRANT OPTION;
  flush privileges;
  use azkaban;
  source /export/software/create-all-sql-0.1.0-SNAPSHOT.sql;

画面 4：
- SQL 命令：
  mysql> CREATE DATABASE azkaban;
  Query OK, 1 row affected (0.00 sec)
  mysql> CREATE USER 'azkaban'@'%' IDENTIFIED BY 'azkaban';
  Query OK, 0 rows affected (0.02 sec)
  mysql> GRANT all privileges ON azkaban.* to 'azkaban'@'%' identified by 'azkaban' WITH GRANT OPTION;
  Query OK, 0 rows affected (0.01 sec)
  mysql> flush privileges;
  Query OK, 0 rows affected (0.00 sec)
  mysql> use azkaban;
  Database changed
  mysql>

画面 5：
- 命令：
  [root@node03 azkaban-3.5.1.0]# cd azkaban-exec-server/
  [root@node03 azkaban-exec-server]# ls
  build.gradle  src
  az-core/
  az-examples/
  az-exec-util/
  az-flow-trigger-dependency-plugin/
  az-flow-trigger-dependency-type/
  az-Hadoop-jobtype-plugin/
  az-hdfs-viewer/
  az-intellis-style.xml
  az-jobsummary/
  azkaban-common/
  azkaban-db/
  azkaban-exec-server/
  azkaban-Hadoop-security-plugin/
  azkaban-solo-server/
  azkaban-web-server/
  az-reportal/

画面 6：
- 命令：
  [root@node03 azkaban-db]# cp create-all-sql-0.1.0-SNAPSHOT.sql /export/software/
  [root@node03 azkaban-db]#

画面 7：
- 无代码或配置。

画面 8：
- 命令：
  [root@node03 azkaban-db]# cd ..
  [root@node03 azkaban-db]#

画面 9：
- 命令：
  [root@node03 azkaban-exec-server]# cd distributions/
  [root@node03 distributions]# cp azkaban-exec-server-0.1.0-SNAPSHOT.tar.gz /export/software/
  [root@node03 distributions]#

画面 10：
- 命令：
  [root@node03 az

