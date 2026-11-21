# 2-flume案例-网络数据采集-Flume安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\2-flume案例-网络数据采集-Flume安装【海量资源尽在 ubkz.com】.mp4
- 时长 5分4秒（音频 305s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在了解完Flume的一些概念和运行机制之后呢接下来我们来看一个案例这个案例呢是这样的有两台主机一个是Mini 1一个是Mini 2那么Mini 1呢向Mini 2呢通过网络呢来发送数据比如说通过Terranet来发送发送的时候呢我们的Mini 2呢在这个端口叫52052这个端口来监听数据
[00:28] 那我们这个时候呢我们就可以在mini2这台主机上部署一个flom的实例也就是flom agent然后这个flom呢就盯着这个端口当这个端口有数据过来的时候呢它就负责数据的采集然后呢把采集后的数据啊通过日志的方式打印到我们屏幕上我们要做这么一个案例好 做这么一个案例的话呢咱们要怎么做呢首先呢
[00:56] 我们是得先安装Floom我们现在还没有Floom所以说呢为了衍射压力我们先搞第一步就是Floom的一个安装Floom的安装呢非常简单我们只需要呢下载一个安装包然后做一个简单的配置就行了来我们看这个呢有一个下载地址那在这里呢我们用的是Floom的1.8.0那这个包呢我已经提前给它下载好了然后呢
[01:26] 把我们的包呢上传到我们的呃第三台机器我们是用第三台机器来安装做一个简单的配置就可以了那接下来我一步一步来做那我们来先做第一步把我们的这个包啊先上传到我们的第三台机子来我们来连接一下好连接完之后呢接下来我们来上传我们的一个福隆门压缩包啊我已经把这个压缩包呢放在桌面上啊这个是
[01:55] Flume 1.8.0我把它放在哪里呢我们还是放到Export Software这个目录放在这里上传找到我们的Flume在这个位置稍等上传完毕上传完毕之后呢接下来我们需要做一件事情就是把我们这个压缩包解压解压到我们的Service目录我们来做一下它XVF
[02:32] apache-c加上一级的Service目录稍等好我们回到上一级的Service目录好在这里有一个叫什么呢有一个叫apache-flom1.8.0刚并然后我们来进来我们来看一下flom好进来之后呢我们需要修改它的一些配置文件我们来看讲义在这里呢我们需要修改叫
[03:02] flomenv.sh它在conf目录来我们进入conf这个目录稍等好进入conf进来之后在这里有一个叫flomenv我们看一下这边叫flomenv把env.shtemplate给它复制一份env.sh这个来我们来cp
[03:31] flomenv.sh的template复制成一个flom-env.shOK应该是这个好复制完之后呢我们对它做一个修改env.sh那怎么修改呢我们只需要配置一个JDK的路径就行了来我们来看一下打开讲义我们需要在这里呢配置一个java home也就是我们JDK的路径我们呢
[04:02] 把这个路JDK的路径呢复制一份过来保证它没有问题可能一个呃我这样我在这里呢克隆一个绘画好回到我们的XPOW的serviceGDK这里把这个路径呢重新复制一下好在这里呢我们来改这里XPOW的后面呢把我刚才复制的直接粘贴好放在这位置好放在这之后呢我们保存退出那么到这里的话呢
[04:36] 我们这个flume呢就配置完了OK就配置完毕就这么简单好配置完了之后呢接下来呢我们开始进行我们刚才的案例我们刚才呢需要去某一个端口来收集我们的网络数据那这个时候呢我们需要对flume做一个配置那怎么配置呢我们先把这个视频先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 服务器上下载、解压并配置 Apache Flume 1.8.0 的安装环境。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- PPT 标题：2. Flume 实战案例
- 内容：案例描述：使用网络 telnet 命令向一台机器发送一些网络数据，然后通过 flume 采集网络接口数据。
- 架构图：左侧 mini1 机器上“业务程序”通过“发网络消息”并“send to mini2 52052”连接到右侧 mini2 机器上的 flume_agent。
- flume_agent 内部结构：包含 socket source、console sink（标注“console - 屏幕”）。
- PPT 左侧导航：2.1 Flume 的安装部署，包含 Step 1: 下载解压修改配置文件、Step 2: 开发配置文件、Step 3: 启动 Flume、Step 4: 安装 Telnet 检测测试。
- 文本：Step 1: 下载解压修改配置文件，下载地址：http://archive.apache.org/dist/flume/1.8.0/apache-flume-1.8.0-bin.tar.gz

画面 2：
- PPT 标题：2.1. Flume 的安装部署
- 内容：Flume 的安装非常简单，只要解压即可，当然，前提是已有 Hadoop 环境。上传安装包到数据源所在节点上。这里我们采用第三台机器来进行安装。
- 文本：Step 2: 开发配置文件
- 屏幕下方显示：192.168.174.120 未连接 - SecureCRT

画面 3：
- 屏幕内容：空白的 SecureCRT 窗口，无任何命令或输出。

画面 4：
- SecureCRT 窗口显示登录后的命令行界面。
- 命令行内容：
  ```
  [root@node03 ~]# cd /export/software/
  [root@node03 software]# ls
  [root@node03 software]# rz -E
  rz waiting to receive.
  ?a? zmodem ??. Ctrl+C ??
  Transferring apache-flume-1.8.0-bin.tar.gz...
  ```

画面 5：
- SecureCRT 窗口显示解压后访问的 Flume API 文档目录。
- 文本内容：
  ```
  apache-flume-1.8.0-bin/docs/apidocs/org/apache/flume/annotations/class-use/InterfaceAudience.html
  apache-flume-1.8.0-bin/docs/apidocs/org/apache/flume/annotations/class-use/InterfaceAudience.LimitedPrivate.html
  apache-flume-1.8.0-bin/docs/apidocs/org/apache/flume/annotations/class-use/InterfaceAudience.Private.html
  apache-flume-1.8.0-bin/docs/apidocs/org/apache/flume/annotations/class-use/InterfaceAudience.Public.html
  apache-flume-1.8.0-bin/docs/apidocs/org/apache/flume/annotations/class-use/InterfaceStability.html
  apache-flume-1.8.0-bin/docs/apidocs/org/apache/flume/annotations/class-use/InterfaceStability.Evolving.html
  apache-flume-1.8.0-bin/docs/apidocs/org/apache/flume/annotations/class-use/InterfaceStability.Stable.html
  apache-flume-1.8.0-bin/docs/apidocs/org/apache/flume/annotations/class-use/Recyclable.html
  apache-flume-1.8.0-bin/docs/apidocs/org/apache/flume/annotations/Disposable.html
  ```

画面 6：
- SecureCRT 窗口显示解压后访问的 Flume 文档目录。
- 命令行内容：
  ```
  apache-flume-1.8.0-bin/docs/images/network-server.png
  apache-flume-1.8.0-bin/docs/images/package-x-generic.png
  apache-flume-1.8.0-bin/docs/images/remove.gif
  apache-flume-1.8.0-bin/docs/images/rss.png
  apache-flume-1.8.0-bin/docs/images/update.gif
  apache-flume-1.8.0-bin/docs/images/window-new.png
  apache-flume-1.8.0-bin/docs/index.html
  apache-flume-1.8.0-bin/docs/issue-tracking.html
  apache-flume-1.8.0-bin/docs/apache-maven-fluido.min.js
  apache-flume-1.8.0-bin/docs/license.html
  apache-flume-1.8.0-bin/docs/mail-lists.html
  apache-flume-1.8.0-bin/docs/objects.inv
  apache-flume-1.8.0-bin/docs/project-info.html
  apache-flume-1.8.0-bin/docs/project-reports.html
  apache-flume-1.8.0-bin/docs/search.html
  apache-flume-1.8.0-bin/docs/searchindex.js
  apache-flume-1.8.0-bin/docs/team-list.html
  [root@node03 software]# cd ../servers/
  [root@node03 servers]#
  ```

画面 7：
- SecureCRT 窗口显示进入 Flume 安装目录。
- 命令行内容：
  ```
  [root@node03 servers]# ls
  apache-flume-1.8.0-bin
  apache-flume-3.1.0-bin
  Hadoop-3.1.1
  Hive sql
  JDK 8.0_141
  ZooKeeper-3.4.9
  [root@node03 servers]# cd apache-flume-1.8.0-bin/
  [root@node03 apache-flume-1.8.0-bin]# ls
  bin CHANGELOG conf DEVNOTES doap_Flume.rdf docs lib LICENSE NOTICE README.md RELEASE-NOTES tools
  ```

