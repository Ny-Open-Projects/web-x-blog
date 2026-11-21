# 17-hadoop的安装-准备工作

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\17-hadoop的安装-准备工作【海量资源尽在 ubkz.com】.mp4
- 时长 5分50秒（音频 350s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来讲一下Hadoop的安装Hadoop安装分成五个步骤第一 上传并解压第二 修改配置文件第三 分发安装包第四 格式化HDFS第五 启动机群咱们先看第一个上传并解压这个Hadoop的安装包我们可以从Abaqi官网去下载这里我已经下载好了我们直接把它上传到我们Export Software这个目录
[00:29] 我们来看在这里呢我在第一台机子上我进到Xbox的software好在这里呢我直接RZ-1然后呢找到我安装包的位置我在机盘然后呢这里有一个Hadoop lesson第01资料好在这里我用的是3.1.1好上传稍等这个需要花点时间上传已经完成
[01:00] 完成了之后呢我们来看这是一个压缩包接下来我给它解压解压到我们的Service目录xvfhadoop解压到我们的上一级-c上一级的Service目录经过漫长的等待我们已经解压完成解压完成之后呢我们进到这个Service这个目录进去之后呢我们来进这个Hadoop来看一下这里边呢
[01:51] 有一些目录比如说这个bin放的是一些可执行文件ETC放配置文件这里边还有个label放的一些库我们进入这个ETC里边好在ETC里边一个Hadoop这里边有很多的配置文件我们接下来要去配置这些文件怎么配置文件呢我们这里边有一个详细的文档我们来看一下一共有六个文件需要我们来配置
[02:18] 那这六个文件配的时候呢如果你直接在这用VM打开那这个时候呢它这个文件呢很容易乱你比如说我随便打开一个12.env.sh好你在这配的话操作起来非常不方便我们怎么去做呢我们可以使用我nodepad++可以使用这个好这个里边有个工具叫NTPNTP FTP这个工具
[02:47] 这工具呢我点一下那它呢可以和我们的Linux呢之间呢建立连接好这个呢大家如果没有这个的话呢你可以装一个插件在哪里呢在这里有一个插件插件里边一个Plugin Manager然后Show Plugin Manager稍等这里边呢可以列出来它所有可以安装的插件你找一个插件呢这个插件的名字呢叫你可以找一下叫我这里已经装了应该它没有给我提醒
[03:17] 这个叫NPP FTP你可以在这找到来你看把光标放在这里NPP FTP然后找到之后把它安装就可以了安装之后我们可以在这里边有个齿轮我们可以点设置选第二个Profile setting好这里我已经建过了比如说我要是在新建点ADD6比如说给它起个名字192.168.2
[03:46] 174.110我点OK那这个时候呢这个地方输入你的IP就行了192.168.174.110好这个地方是你的用户名然后root好这个地方是你的密码123456好这时候呢直接应该就可以了可以之后呢我们点close好这个时候你会发现有三个比如说我要去连第一个
[04:16] 点一下稍等那这时候我们和第一台主机呢已经建立关联了那我要想修改它的配置文件我可以找到我们的稍等让它刷新一下我可以找到我们的export在哪里呢在Source里面有个Hadoop 3.1.1在这个ETC下面ETC下面有一个Hadoop好这里边全是一些配置文件这些配置文件呢我们要去修改
[04:47] 一共有六个我们来一个来修改第一个是call set的插面这个呢是一个核心的配置文件来我们打开这是第一个好第二个呢第二个呢是我们的这个hadoopenv.sh我们来找一下hadoopenv.sh那第三个呢是我们的hdfs set的插面好hdfs set插面好第四个呢是我们的这个
[05:19] mypreedset的插面我们找一下mypreedset的插面是这个好这是几个了四个了是吧还有两个还有一个呢是year set的插面还有一个最后一个worksyear set的插面还有一个worksOK我们把这六个文件呢分别打开那可以呢就在这里进行配置好我们先停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Hadoop 3.1.1 版本的安装过程，重点是上传解压、修改配置文件（core-site.xml 和 hdfs-site.xml）以及 YARN 的配置（yarn-site.xml）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Typora 文档，内容为“8.2 Hadoop的安装”章节，列出安装步骤：上传并解压、修改配置文件、分发安装包、格式化HDFS、启动集群。其中“上传并解压”步骤下有命令：cd /export/software 和 tar zxvf Hadoop-3.1.1.tar.gz -C ../servers。
画面 2: SecureCRT 会话窗口，显示 Hadoop 3.1.1 的客户端 jar 包路径列表。
画面 3: SecureCRT 会话窗口，显示 Hadoop 3.1.1 的共享缓存管理器相关文档路径。
画面 4: SecureCRT 会话窗口，显示 Hadoop 3.1.1 的 ResourceManager API 文档路径。
画面 5: SecureCRT 会话窗口，显示 Hadoop 3.1.1 的 ResourceManager 预留资源相关 API 文档路径。
画面 6: SecureCRT 会话窗口，显示在 node01 节点上，用户进入 /servers/Hadoop-3.1.1/ 目录并列出其内容。
画面 7: Typora 文档，内容与画面 1 相同，展示“8.2 Hadoop的安装”章节。
画面 8: Notepad++ 编辑器界面，显示“Plugin Manager”菜单项，用于管理插件。
画面 9: Notepad++ 编辑器界面，显示远程连接到 192.168.174.100 的文件目录结构，包含多个 Hadoop 配置文件。
画面 10: Notepad++ 编辑器界面，显示 core-site.xml 文件内容，包含 Apache License 2.0 的声明和注释“Put site-specific property overrides in this file.”。
画面 11: Typora 文档，展示 core-site.xml 文件内容，其中包含 <property> 标签对，如 <name>fs.defaultFS</name> 和 <value>hdfs://node01:8020</value>。
画面 12: Typora 文档，展示 hdfs-site.xml 文件内容，包含 <property> 标签对，如 <name>dfs.namenode.name.dir</name> 和 <value>file:///export/Hadoop/data/namenodedatas</value>。
画面 13: Typora 文档，展示 yarn-site.xml 文件内容，包含 <property> 标签对，如 <name>yarn.resourcemanager.address</name> 和 <value>node01:8032</value>。
画面 14: Notepad++ 编辑器界面，显示 core-site.xml 文件内容，与画面 10 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
1. 上传并解压
2. 修改配置文件
3. 分发安装包
4. 格式化HDFS
5. 启动集群
1. 上传并解压
1. 上传压缩包到/export/software目录
2. cd /export/software
3. tar zxvf Hadoop-3.1.1.tar.gz -C ../servers
画面 6:
[root@node01 software]# cd ../servers/
[root@node01 servers]# cd Hadoop-3.1.1/
[root@node01 Hadoop-3.1.1]# ls
bin  etc  include  lib  LICENSE.txt  NOTICE.txt  README.txt  sbin  share
[root@node01 etc]# cd Hadoop/
[root@node01 Hadoop]#
画面 11:
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://node01:8020</value>
  </property>
</configuration>
画面 12:
<configuration>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///export/Hadoop/data/namenodedatas</value>
  </property>
  <property>
    <name>dfs.blocksizet</name>
    <value>134217728</value>
  </property>
  <property>
    <name>dfs.namenode.handler.count</name>
    <value>18</value>
  </property>
</configuration>
画面 13:
<configuration>
  <property>
    <name>yarn.resourcemanager.address</name>
    <value>node01:8032</value>
  </property>
  <property>
    <name>yarn.resourcemanager.scheduler.address</name>
    <value>node01:8030</value>
  </property>
  <property>
    <name>yarn.resourcemanager.resource-tracker.address</name>
    <value>node01:8031</value>
  </property>
  <property>
    <name>yarn.resourcemanager.admin.address</name>
    <value>node01:8033</value>
  </property>
  <property>
    <name>yarn.resourcemanager.webapp.address</name>
    <value>node01:8088</value>
  </property>
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>node01</value>
  </property>
  <property>
    <name>yarn.scheduler.minimum-allocation-mb</name>
    <value>1024</value>
  </property>
</configuration>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

