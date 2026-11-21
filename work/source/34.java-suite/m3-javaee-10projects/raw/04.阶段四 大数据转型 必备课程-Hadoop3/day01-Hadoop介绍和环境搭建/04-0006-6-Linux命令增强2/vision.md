# 画面线理解：6-Linux命令增强2

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\6-Linux命令增强2【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:45, 04:09, 05:36, 06:08, 06:29, 06:54, 07:09, 07:55, 08:08, 08:30, 09:01, 10:37, 10:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:11:23

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中使用 chmod 和 chown 命令修改文件权限和文件所有者。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 SecureCRT 连接至 node03 的终端界面，提示符为 [root@node03 /]#。
画面 2: 执行 cd /root/ 命令，切换到根目录，显示目录下文件列表。
画面 3: 展示一个关于文件权限的架构图，包含用户、组、文件权限、文件类型等概念，图中显示 a.txt 文件。
画面 4: 在架构图上标注了文件 a.txt 的权限值 767 和 575，同时终端显示了文件列表。
画面 5: 在 /var/spool/mail/root 目录下创建一个名为 a.txt 的文件，并使用 chmod 777 命令修改其权限。
画面 6: 在终端中执行 chmod u-x a.txt 命令，移除文件所有者（user）的执行权限。
画面 7: 执行 chmod g-rwx a.txt 命令，移除组（group）的读、写、执行权限。
画面 8: 执行 chmod g+x a.txt 命令，为组（group）添加执行权限。
画面 9: 执行 chown -R hadoop:hadoop a.txt 命令，将文件所有者和所属组改为 hadoop。
画面 10: 执行 chown -R hadoop:hadoop a.txt 命令，将文件所有者和所属组改为 hadoop。
画面 11: 显示 Typora 文档中关于 Linux 系统服务命令的章节，包括 service 和 chkconfig 命令。
画面 12: 在 Typora 文档中，鼠标光标指向 service iptables stop 命令，用于关闭防火墙。
画面 13: 在 Typora 文档中，鼠标光标指向 service iptables stop 命令，用于关闭防火墙。
画面 14: 在 Typora 文档中，鼠标光标指向 service iptables stop 命令，用于关闭防火墙。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
cd /root/
ls -l
total 44
-rw------- 1 root root 1429 Sep 12 2018 anaconda-ks.cfg
-rw-r--r-- 1 root root 28523 Sep 12 2018 install.log
-rw-r--r-- 1 root root 7570 Sep 12 2018 install.log.syslog

画面 5:
touch a.txt
chmod 777 a.txt

画面 6:
chmod u-x a.txt

画面 7:
chmod g-rwx a.txt

画面 8:
chmod g+x a.txt

画面 9:
chown -R hadoop:hadoop a.txt

画面 11:
chmod 777 a.txt  #表示给某个文件赋予所有人的所有权限
chmod u-x a.txt  #取消a.txt文件，用户“执行”权限
chmod g+x a.txt  #添加a.txt文件，组“执行”权限
chown R hadoop:hadoop a.txt  #改变某个文件或者文件夹的用户以及用户组

画面 12:
service iptables status  #查看防火墙状态
service iptables stop  #关闭防火墙
service --status-all  #查看系统所有的后台服务进程
service sshd status  #查看指定的后台服务进程的状态
service sshd stop
service sshd start
service sshd restart
配置后台服务进程的开机自启或关闭
chkconfig iptables on  #配置防火墙开机开启
chkconfig iptables off  #配置防火墙开机关闭
chkconfig httpd on  #让 httpd 服务开机自启
chkconfig httpd off  #让 httpd 服务开机不要自启

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: 架构图包含三个主要部分：文件权限（u g o）、文件类型（d l c s b）和用户组（root usr）。文件权限部分包含“所有者权限”、“组权限”、“其他用户权限”三个子部分。文件类型部分包含“普通文件”、“目录文件”、“链接文件”、“设备文件”、“套接字文件”等。用户组部分包含“用户”和“组”两个子部分。图中显示 a.txt 文件，其权限值为 767 和 575。
画面 11: PPT 标题为“3.4 系统服务命令”，包含 service 和 chkconfig 命令的使用方法。
画面 12: PPT 标题为“3.4 系统服务命令”，包含 service 和 chkconfig 命令的使用方法。
画面 13: PPT 标题为“3.4 系统服务命令”，包含 service 和 chkconfig 命令的使用方法。
画面 14: PPT 标题为“3.4 系统服务命令”，包含 service 和 chkconfig 命令的使用方法。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
