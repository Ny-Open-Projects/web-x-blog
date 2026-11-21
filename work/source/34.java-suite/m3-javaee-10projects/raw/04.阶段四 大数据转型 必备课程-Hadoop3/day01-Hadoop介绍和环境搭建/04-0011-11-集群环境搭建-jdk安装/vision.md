# 画面线理解：11-集群环境搭建-jdk安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\11-集群环境搭建-jdk安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 02:07, 03:35, 04:43, 05:16, 06:00, 06:57, 08:21, 08:42, 08:54, 09:25, 10:08, 10:33, 10:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:25:27

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
jdk1.8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.garbagecollector_1.0.200.v20131115-1210.jar
jdk1.8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.core_2.3.0.v20131211-1531.jar
jdk1.8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.metadata_1.0.4.0.v20140623020002.jar
jdk1.8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.repository_2.3.0.v20131211-1531.jar
jdk1.8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.ui_1.1.200.v20130626-2037.jar
jdk1.8.0_141/lib/missioncontrol/plugins/org.sat4j.core_2.3.5.v201308161310.jar
jdk1.8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.simpleconfigurator.nl_zh_4.0.v20140623020002.jar
jdk1.8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.ui.workbench.addons.swt_1.0.4.0.v20140512-1650.jar
jdk1.8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.touchpoint.eclipse_2.1.200.v20140623020002.jar
jdk1.8.0_141/lib/missioncontrol/plugins/org.eclipse.equinox.p2.core_3.9.1.v20140825-1431.jar
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
