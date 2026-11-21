# 9-Hive的安装-Hive的交互方式

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\9-Hive的安装-Hive的交互方式【海量资源尽在 ubkz.com】.mp4
- 时长 7分9秒（音频 430s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在安装完Hive之后呢接下来我们来看一下Hive的交互方式先看第一种来我们呢先进到我们的Hive的一个主目录然后呢接下来我们在这并Hive然后呢回车这个时候呢它可以进到一个类似于Shell的一个交互页面稍等启动会有点慢好我们已经进来了进来之后呢你看这里有一个提示符你可以把这个呢
[00:29] 当成了我们mycircle中的一个输入circle命令的一个终端在这里比如说呢我想去查看我们的数据仓库中呢有哪些数据库我们可以用一个show data base4你会发现呢这个和我们这个circle命令基本是一样的来我们回程稍等你会发现呢这里边我们查到了一个数据库叫default这个default呢是我们Hive的一个默认的一个数据库
[00:58] 好那我们呢可以在这里呢对我们的数据仓库呢进行一些操作那我们做什么操作呢我们可以在这里呢创建一个数据库来看create database if not exist myhive就是如果没有myhive这个数据库我就来创建那我们呢直接来复制一下然后粘贴放在这里走我们就可以创建一个myhive数据库那怎么证明呢我们来看我们可以show
[01:27] data base4你看一下是不是多了一个myhive数据库那我们还可以在这个数据库中呢创建一些表比如说我用个use就是使用这个数据库myhive然后呢我来创建一个表创建表呢和我们circle是一样的created table比如说我创建一个表呢叫t-test这个表然后呢后面呢跟上这个表的一些字段和类型比如说id呢
[01:57] 是一个int类型然后呢再加上一个name这个地方呢是string类型好那我们回车创建一个表好这个时候我们来show一个tables你会发现这里边有一个表好当你做了这些操作之后呢其实呢在我们这个表和真实的数据之间呢有一个映射关系这些映射关系被称为原数据这些原数据保存在哪里呢
[02:26] 其实保存在我们刚才安装的MySQL里面来我们打开我们的MySQL来看一下怎么打开呢我们可以用一个SQL样格来登录一下在这里呢我去输一个我们的一个IP地址192.168.174.120这是第三台主机我是120用户root密码是123456
[02:54] 好我们来连接一下登录稍等让他登录他说是否要保存的更改点是好点完是之后呢你会发现呢这里边呢有四个有四个数据库其中呢这个Hive呢其实他是自动给我们创建的他来保存原数据信息而剩余的这三个呢是他呢去一个默认的一些数据库比如说他是来测试的而这两个呢是放的一些核心数据OK
[03:26] 我们的原数据信息呢就在Hive里面保存好说明了我们这个Hive和我们的MySQL呢已经建立了关联好那有了这个之后呢我们把这个Hive呢退出好退出退出了之后呢我们和Hive的交互呢还可以有第二种方式第二种方式就是说我们不进入Hive的客户端然后呢直接去执行Hive的一个Late Circle命令那怎么做呢我们来看
[03:56] 我们还是进入这个Hive的一个安装目录然后用一个binhive一个-1后面呢跟上一个一个circle命令来我们来试一下在这里呢我们来运行这个地方呢我就不用mytask我用myhive我们来试一下好myhive走稍等让它来运行好稍等已经运行完了运行完之后我们来开始查一下比如说我再进入binhive
[04:33] 稍等好在这里呢我们来查一下我们还是用刚才这个show database哎你看是不是有多了一个myhive好那么这个有什么用呢这个其实它的作用呢第一个用的比较少它的作用主要是用第二种第二种的话呢我们可以不进入这个Hive的一个客户端我们可以写一个脚本哎这个有一个Hive.circle这样的脚本然后把我们的要去写的一些hql这个
[05:04] 指令呢放在这个脚本里面然后呢可以通过这个Hive-f这个命令呢来去一次性运行我们整个脚本我们来测试一下比如说呢在这里我先建一个脚本在哪里在export Service我们来试一下好我们先退出吧我们回到这个export Service在这呢建一个Hive.circle好在这里呢我们可以把
[05:34] 你想要执行的一些HQL这个命令呢放在这里比如说这里面呢我创建一个数据库我换一个叫mytest2好吧mytest2然后呢如果不存在我就去创建然后呢我去用这个mytest2然后呢我再创建一张表OK就这三条命令好把它保存完之后呢我可以不进到我们的Hive客户端我就可以执行它怎么执行呢用个Hive-f
[06:04] 然后呢后面告诉我你的脚本在哪里我就可以执行来我们来试一下进的还是进入到这个A87 Hive里边来走好我们来运行我来试一下走好他说这个Hive命令未发现我们来看一下未发现我们应该这样写我们应该写bin Hivebin下面的Hive走来加个bin就可以了来稍等一下好也执行完了
[06:35] 执行完之后呢我们再去查看一下来我们再去查看一下binhive好在这里好我们来show tabledatabase稍等好这里边是不是多了一个mytester好了那么到此为止呢我们这个整个数据库呢就基本上就测试完了也就是说说明我们的数据仓库的搭建是没有任何问题的好那么搭建完之后呢接下来我们就开始进行Hive的一些基本操作好
[07:05] 关于它的一个交互方式呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过命令行和 SQL 脚本两种方式在 Hive 中创建数据库和表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 Notepad++ 编辑器中的 Hive 交互方式文档，包含两种交互方式：
  第一种交互方式：bin/Hive
  第二种交互方式：使用 sql 语句或者 sql 脚本进行交互
- 文档中提供了创建数据库的命令：
  create database if not exists myhive;
- 文档中提供了通过 SQL 脚本创建数据库的命令：
  cd /export/servers/apache-Hive-3.1.1-bin
  bin/Hive -e "create database if not exists mytest;"

画面2：
- 展示了 Notepad++ 编辑器中的 Hive 交互方式文档，内容与画面1相同。
- 文档中提供了通过 SQL 脚本创建数据库并创建表的命令：
  cd /export/servers/apache-Hive-3.1.1-bin
  vim Hive.sql
  create database if not exists mytest;
  use mytest;
  create table stu (id int, name string);

画面3：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 执行了以下命令：
  Hive> show databases;
  Hive> create database if not exists myhive;
  Hive> show databases;
  Hive> use myhive;

画面4：
- 展示了 SQLyog Ultimate 的“连接 MySQL 主机”对话框。
- 对话框中显示了连接信息：
  MySQL 主机地址：192.168.174.120
- 对话框提示：“You have changed your connection details. Click OK to save changes.”

画面5：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 执行了以下命令：
  Hive> create table t_test(id int, name string);
  Hive> show tables;
  Hive> exit;

画面6：
- 展示了 SecureCRT 中的终端界面。
- 执行了命令：
  bin/Hive -e "create database if not exists myhive;"
- 输出了 SLF4J 日志绑定信息。

画面7：
- 展示了 SecureCRT 中的 Hive 命令行界面。
- 执行了命令：
  Hive> show databases;
- 输出了数据库列表：
  default
  myhive
- 当前 Hive 会话 ID：ab13d01a-b9ba-4bf4-abe9-ff4bea22b0d

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
cd /export/servers/apache-Hive-3.1.1-bin
bin/Hive
create database if not exists myhive;
cd /export/servers/apache-Hive-3.1.1-bin
bin/Hive -e "create database if not exists mytest;"

画面2：
cd /export/servers/apache-Hive-3.1.1-bin
vim Hive.sql
create database if not exists mytest;
use mytest;
create table stu (id int, name string);

画面3：
Hive> show databases;
Hive> create database if not exists myhive;
Hive> show databases;
Hive> use myhive;

画面5：
Hive> create table t_test(id int, name string);
Hive> show tables;
Hive> exit;

画面6：
bin/Hive -e "create database if not exists myhive;"

画面7：
Hive> show databases;
default
myhive

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

