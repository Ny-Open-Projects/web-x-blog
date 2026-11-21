# 画面线理解：5-Linux命令增强

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\5-Linux命令增强【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 01:29, 02:29, 03:10, 04:21, 05:07, 06:23, 08:16, 09:32, 10:28, 11:10, 12:34, 13:39, 16:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:08:53

1) 这一组画面整体在讲什么（一句话）：
演示在Linux环境下使用grep、find、locate等命令进行文件搜索，并演示用户管理操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，讲解Linux常用命令，重点是grep命令的使用方法，如ps -ef | grep sshd。
画面2：在node01节点的SecureCRT终端中，执行ls命令查看根目录下的文件夹。
画面3：在node02节点的SecureCRT终端中，执行cd /和ls命令，查看根目录结构。
画面4：展示PPT内容，讲解修改IP地址的命令：vim /etc/sysconfig/network-scripts/ifcfg-eth0。
画面5：在node01节点的SecureCRT终端中，执行ps命令查看系统进程。
画面6：在node03节点的SecureCRT终端中，执行ps -ef | grep sshd命令，查看SSH服务进程。
画面7：展示PPT内容，讲解find命令和locate命令的使用方法。
画面8：在node03节点的SecureCRT终端中，执行find命令查找所有.log文件。
画面9：在node03节点的SecureCRT终端中，执行find命令查找大小大于100M的文件。
画面10：在Windows系统中，打开SecureCRT的安装目录，显示安装文件列表。
画面11：在node03节点的SecureCRT终端中，执行yum -y install mlocate命令安装mlocate软件包。
画面12：展示PPT内容，讲解locate命令的使用方法，以及用户管理命令。
画面13：在node03节点的SecureCRT终端中，执行useradd hadoop命令创建用户hadoop。
画面14：在node03节点的SecureCRT终端中，执行passwd hadoop命令为用户hadoop设置密码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
修改IP地址
vim /etc/sysconfig/network-scripts/ifcfg-eth0
修改主机名(需重启永久生效)
vi /ect/sysconfig/network
HOSTNAME=node01
设置ip和域名映射
vim /etc/hosts

画面7：
find命令
使用实例：
find . -name "*.log" -ls 在当前目录查找以.log结尾的文件，并显示详细信息。
find /root/ -perm 777 -ls 查找/root目录下权限为777的文件
find . -size +100M 查找当前目录下大于100M的文件

画面11：
[root@node03 /]# yum -y install mlocate
Loaded plugins: fastestmirror, security
Setting up Install Process
base
base/primary_db
extras
extras/primary_db
updates
updates/primary_db
Package mlocate-0.22.2-6.e16.x86_64 already installed and latest version
Nothing to do
You have new mail in /var/spool/mail/root
You have new mail in /var/spool/mail/root
[root@node03 /]# locate /etc/sh
/etc/shadow
/etc/shadow-
/etc/shells

画面13：
[root@node03 /]# useradd hadoop
You have new mail in /var/spool/mail/root
[root@node03 /]# cd /home/
[root@node03 home]# passwd hadoop
Changing password for user hadoop.
New password:
BAD PASSWORD: it is too simplistic/systematic
Retype new password:

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：Hadoop01-入门到实战环境搭建
今日内容：
1. Hadoop介绍
   问题一：大文件怎么存储？
   问题二：大数据怎么计算？
   问题三：如何将这些计算任务部署到集群？
2. 环境搭建
   就绪虚拟机
   1. 网络模式详解
   2. 存储设置
   3. 集群规划
   4. 设置IP和Mac地址
   3. Linux常用的命令
   3.1 直接命令
   3.2 用户管理命令
   配置辅助软件
   安装 Hadoop

画面4：
标题：修改IP地址
命令：vim /etc/sysconfig/network-scripts/ifcfg-eth0
命令：vi /ect/sysconfig/network
HOSTNAME=node01
命令：vim /etc/hosts

画面7：
标题：3.1 直接命令
grep命令：grep [option] pattern [file] 可使用—help 查看更多参数。使用实例：
ps -ef | grep sshd 查找指定 ssh 服务进程
ps -ef | grep -v grep 查找指定服务进程，排除 grep 本身
grep -n 'hello' a.txt 从文件中查找关键词，并显示行号

标题：find命令
使用实例：
find . -name "*.log" -ls 在当前目录查找以.log结尾的文件，并显示详细信息。
find /root/ -perm 777 -ls 查找/root目录下权限为777的文件
find . -size +100M 查找当前目录下大于100M的文件

标题：Locate命令
locate 让使用者可以很快速的搜寻系统内是否有指定的档案。其方法是先建立一个包括系统内所有档案名称及路径的数据库。之后当寻找时就只需查询这个数据库（/var/lib/locate）。
Linux 系统会自动创建这个数据库，取每天自动更新一次。所以使用 locate 命令查不到最新变动的文件。为了避免这种情况，可以在使用 locate 之前，先使用 updatedb 命令，手动更新数据库。
yum -y install mlocate
使用实例：
locate /etc/sh
搜索 etc 目录下所有以 sh 开头的文件
locate pwd
查找和 pwd 相关的所有文件

标题：3.2 用户管理命令
添加普通用户
useradd hadoop # 这个表示我们创建了一个普通用户
password hadoop # 表示我们需要给hadoop这个普通用户分配一个密码，密切换用户：
su - 用户名

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
