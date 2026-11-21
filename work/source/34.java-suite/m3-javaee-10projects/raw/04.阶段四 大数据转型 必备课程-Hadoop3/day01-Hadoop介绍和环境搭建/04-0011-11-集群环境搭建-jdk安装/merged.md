# 11-集群环境搭建-jdk安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\11-集群环境搭建-jdk安装【海量资源尽在 ubkz.com】.mp4
- 时长 11分8秒（音频 668s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们给虚拟机安装些辅助软件第一个我们要给每台机器安装一个JDK我们来开始首先要查一下你这个机子里面是否有些自带的JDK有的话我们要把它卸载先看第一台走一下这里边没有记住如果你有的话一定要把它卸载那怎么卸载呢我这里边有这么一个命令rpm-1后面是跟上你
[00:29] 自带JDK的一个名字你就照这个模板来去执行一下这个命令就可以了好了咱们看看第二台看里边有没有自带的一些JDK第二台走这里边好像有一个是不是这里边有一个有一个的话我这个写错了加吧没有再看第三台加吧走这里也没有没有的话我们接下来我们把这个JDK
[01:01] 给大家装一下安装安装之前呢我们要上传我们自己的GPK安装包那么在上传到哪里呢我希望大家能够建两个文件夹对我们的软件呢作为一个统一管理我们可以make a diagamc然后呢在根目录下面创建文件夹叫export然后呢在export里面呢创建一个子文件夹子目录叫software这个software呢里边专门放我们的
[01:32] 压缩包走我们还要创建文件夹呢呃叫Service啊Service这个Service里面呢是存放我们安装的一些呃安装的一些软件ok我创建完了创建完之后呢接下来我们要干一件事情把我们的JDK啊上传到这个software里边来啊怎么上传呢有很多种方式你可以使用一些工具
[02:00] 你也可以利用CRT里边一些自带的一些工具都可以在这里呢我已经把这个JDK放在我们今天的资料里边了我用的是GDK8.0的OK那么我要把它上传进来怎么办呢我这里有个命令叫RZ-1用这个命令使用这个命令的前提给大家说一下有的同学可能用不了这个命令你需要装一个软件yom-y install
[02:28] 这个软件的名字叫LRZSZ只要装这个软件我们就可以使用这个命令我已经装过了来RZ-1我们找到这个软件我们来在哪里在我的这个机盘里边有一个Hadoop Lens D01资料让这里边GDK8.0走稍等给它点时间
[02:55] 已经上传成功那么上传成功之后它存放在哪里呢我们ls一下你看我刚才是在根目录去执行这个命令那么它就存放在根目录这个呢大家下次记着我们需要将这个压缩包放在这个放在哪个目录呢我move一下把它移到我们的export下面一个software我要把它放在这个目录下面去好我们来进export software那么我要把它移到这里
[03:25] 那下一次如果你还想上传其他的压缩包你可以在这个software这个目录呢运行这个RZ-E那这样子你上传的文件啊它默认就保存在这个目录大家注意好我已经上传了好上传完之后呢接下来我们看我们要干什么事情呢我们呢需要对它的进行解压解压完之后呢解压到哪里呢解压到一个Service这个目录
[03:54] 我们来解压他ZXVF是解压解压谁呢解压JDK这个压缩包把它解压到哪里解压到上一级目录有一个Service这个Service呢就是我刚才创建的一个目录好回车稍等好这个地方呢他说没有发现有效的这个文件我来看看是什么原因这个地方呢software
[04:25] 他XVF他杠Z啊他说呢可能是这个压缩包有问题啊这个压缩包哦知道了这个地方呢你要解压到其他目录应该加个参数就刚C大写的C这样应该就可以了来我们来解压一下好解压完之后呢大家注意我们回到这个export下面一个Service我们已经解压到这个目录好解压完之后呢这就是我们解压好的JDK
[04:58] 接下之后呢我们还要做一件事情来配置它的一个环境面量在ETC下面有文件叫profile我们来修改一下ETC下面有个profile在这个里面呢我们要加两个环境面量环境面量那一个呢是这么一个啊一个是这个文件这个export.java.home这个地方呢要指定你JDK所在的目录你看我这个路径就不对我们的JDK在哪里
[05:28] 我们的JDK在ETC下面Export的一个Service对不对下面有一个什么呢我把这个路径呢给大家复制一下稍等我们呢在JDK我们的路径是这个千万别搞错了把这个呢复制到这个位置好这是我JDK的路径而且呢要把我们的这个Java Home呢添加到Path里面这样它才能生效好我把这两行呢直接复制
[05:59] 好直接复制完之后呢放在我这里边来再打开粘在这个位置一定要保证这个路径是对的OK那么做完之后呢我们呢为了让它生效啊我们来还要sauce一下然后呢etc profile好这个时候呢我们的JDK呢也装好了好安装好之后呢这个时候呢我们再看其他的主机那我们来看怎么给这个其他主机也配置这个JDK好第一台配完之后呢
[06:31] 第二台和第三台呢也是同样的一个步骤我们来先建文件夹MAC第二杠Pexport然后呢这个地方一个Service然后export一个software好了这两个呢我们来分别复制一下在第三台呢也做一下Service然后呢这地方是software做完之后呢注意我们第一台呢已经解码完了之后呢我们可以把这个文件夹呢分发给其他主机
[07:09] 怎么做呢我们回到Service这个目录然后呢我输个命令叫scp-2这个scp呢是远程拷贝命令我们可以把这个文件夹呀拷贝到其他另外两台主机ok JDK拷贝拷贝给谁呢我可以拷贝给node02这个主机它的哪个目录呢我们可以这样写我们可以写这个export然后呢这个一个Service
[07:38] 那么这样写这样写的话呢还有一个简化的写法就是一个$PWD这个$PWD呢相当于我访问这个环境变量这个环境变量的名字是PWD它可以获取我当前所在的目录也就是这个Service目录换句话来讲呢它可以把这个文件夹拷贝到Node02这台机子的当前目录那也就是说Node02这个目录呢和我当前目录是同一级目录
[08:08] 好了我们来这样做一下走一下稍等让它拷贝好拷贝完之后呢咱们再拷贝把这个东西呢拷贝给第三台主机也是这样子node03拷贝到当前目录走稍等好拷贝完之后呢咱们回到第二台来看一下cd export Service里边你发现已经有了一个JDK了那么还不行我们还得配置它的etc profile它的环境面量我们要配一个JDK环境面量
[09:07] 好了那么把这两句话呢重新复制一下啊重新复制一下走这个一定要去的这个路径是没问题的export Service然后JDK我们来看一下啊export Service然后呢JDK好一定要保证这个路径和这个路径是一致的好拷贝完之后呢接下来我们再做第三台对了忘了一件事情做完之后一定要source一下让它生效
[09:39] ETC profile好来看第三台第三台也是一样回到Export Service它已经过来了那么咱们来配置ETC profile大家会发现这句话非常的烦人这是一个邮件检测就是你每次操作它有时候会你发的邮件信息这是邮件的一些提醒如果你不想去做这个邮件教验你可以在profile里面来加一句话这句话叫ansight
[10:10] 叫mailcheck也就是说邮箱检测我不检测好咱们接下来配置咱们的咱们的这个pass环境变量把这个给它复制一下好粘在这个位置最后保存退出不要忘了source etc profile好到此为止呢我们把这个配完了配完之后呢我们三台讯息的JDK呢就可以使用了
[10:41] 好关于JDK的配置呢你看这里还有一个有限提醒我们依然可以在etc profile里边呢我们来加一句话加什么呢加在哪个位置都可以unsite mail check好保存对注再来source一下哎你看它就没有那个提醒了这个也是一样好做完之后呢我们先把这个停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在多台 Linux 服务器上安装和配置 JDK 环境变量，为后续部署 Hadoop 等大数据组件做准备。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 登录到 node01 服务器，终端处于空命令行状态。
画面 2: 在 node01 上执行命令 `rpm -qa | grep java` 查询已安装的 Java 包，并创建目录 `/export/software`。
画面 3: 在 node01 上使用 `rz` 命令上传 JDK 压缩包，解压后移动文件。
画面 4: 显示解压后的 JDK 目录结构，包含多个插件和库文件。
画面 5: 在 node01 上编辑 `/etc/profile` 文件，设置环境变量 `MYENV`。
画面 6: 在 node01 上编辑 `/etc/profile` 文件，设置环境变量 `JAVA_HOME` 和 `PATH`，并提示执行 `source /etc/profile` 生效。
画面 7: 登录到 node03 服务器，终端处于空命令行状态。
画面 8: 显示解压后的 NetBeans 相关文件列表。
画面 9: 显示解压后的 GNOME 相关文件列表。
画面 10: 登录到 node02 服务器，终端处于空命令行状态。
画面 11: 在 node02 上编辑 `/etc/profile` 文件，设置环境变量 `JAVA_HOME` 和 `PATH`，并执行 `source /etc/profile` 生效。
画面 12: 在 node03 上编辑 `/etc/profile` 文件，设置环境变量 `JAVA_HOME` 和 `PATH`，并执行 `source /etc/profile` 生效。
画面 13: 登录到 node03 服务器，终端处于空命令行状态。
画面 14: 在 node02 上编辑 `/etc/profile` 文件，设置环境变量 `JAVA_HOME` 和 `MAILCHECK`，并执行 `source /etc/profile` 生效。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```bash
[root@node01 /]# rpm -qa | grep java
[root@node01 /]# mkdir -p /export/servers
```

画面 3:
```bash
[root@node01 /]# rz -E
rz waiting to receive.
?# zmodem '??'. Ctrl+C ??
[root@node01 /]# ls
[root@node01 /]# cd /export/software
[root@node01 software]# rz
rz waiting to receive.
?# zmodem '??'. Ctrl+C ??
```

画面 4:
```
JDK 8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.garbagecollector_1.0.200.v20131115-1210.jar
JDK 8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.core_2.3.0.v20131211-1531.jar
JDK 8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.metadata_1.0.4.0.v20140623020002.jar
JDK 8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.repository_2.3.0.v20131211-1531.jar
JDK 8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.ui_1.1.200.v20130626-2037.jar
JDK 8.0_141/lib/missioncontrol/plugins/org.sat4j.core_2.3.5.v201308161310.jar
JDK 8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.simpleconfigurator.nl_zh_4.0.v20140623020002.jar
JDK 8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.ui.workbench.addons.swt_1.0.4.0.v20140512-1650.jar
JDK 8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.touchpoint.eclipse_2.1.200.v20140623020002.jar
JDK 8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.core_3.9.1.v20140825-1431.jar
```

画面 5:
```bash
umask 022
fi
for i in /etc/profile.d/*.sh ; do
  if [ -r "$i" ]; then
    if [ "x$*" != "x" ]; then
      echo "x$*" > /dev/null 2>&1
    else
      echo "x$*" > /dev/null 2>&1
    fi
  fi
done
unset i
unset -f pathmunge
export MYENV=/root/lib/demo
```

画面 6:
```bash
rpm -e java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x86_64 tdata java-2016 java-1.8.0-openjdk-1.8.0.141-1.13.13.1.el6_8.x

