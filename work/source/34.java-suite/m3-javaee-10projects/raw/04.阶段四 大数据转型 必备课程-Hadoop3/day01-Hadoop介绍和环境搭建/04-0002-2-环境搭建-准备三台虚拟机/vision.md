# 画面线理解：2-环境搭建-准备三台虚拟机

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\2-环境搭建-准备三台虚拟机【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:20, 01:50, 02:25, 03:16, 03:56, 04:19, 04:59, 05:39, 06:58, 07:22, 07:39, 08:07, 08:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:00:53

1) 这一组画面整体在讲什么（一句话）：
在 VMware Workstation 中创建并配置 CentOS 虚拟机，为后续 Hadoop 环境搭建做准备。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示课程 PPT 第 2 页“环境搭建”，内容包括创建虚拟机、配置宿主机、安装 CentOS、组成集群等步骤。
画面 2: 展示 Windows 文件资源管理器中“centos6.9-clean-machine”文件夹，内含多个 CentOS 6.4 的 .vmx、.vmdk、.vmsd 文件。
画面 3: 显示 VMware Workstation 的“服务”窗口，其中“VMware Authorization Service”、“VMware DHCP Service”等服务状态为“已启动”。
画面 4: 显示 VMware Workstation 的“服务”窗口，其中“VSS”服务状态为“已停止”，其他服务如“WLAN Service”、“WarpItTool”等状态为“已启动”。
画面 5: 显示 VMware Workstation 的“NAT 设置”窗口，网络模式为“NAT”，子网掩码为“255.255.255.0”，网关为“192.168.174.1”，IP 地址为“192.168.174.10”。
画面 6: 显示课程 PPT 第 4 页“安装 Hadoop”，内容包括下载并解压、修改配置、分发到每个节点、格式化 HDFS、启动集群等步骤。
画面 7: 显示 Windows 系统“网络连接”窗口，其中“以太网 4”状态为“已连接”，速度为“100.0 Mbps”。
画面 8: 显示 Windows 系统“网络连接”窗口，其中“以太网 4”状态为“已连接”，速度为“100.0 Mbps”，并显示“VMware Virtual Ethernet Adapter for VMnet8”等虚拟网卡信息。
画面 9: 显示 Windows 文件资源管理器，路径为“LENOVO (D:)”，包含“develop”、“instantclient_12_1”、“ssh”、“true install”等文件夹。
画面 10: 显示 VMware Workstation 主界面，包含“创建新的虚拟机”、“虚拟化物理机”、“软件更新”等选项。
画面 11: 显示 Windows 文件资源管理器，路径为“LENOVO (D:)”，包含“linux_install”文件夹，内含“install.jdk”、“install.jps”等文件。
画面 12: 显示 VMware Workstation 界面，包含“node03”、“node02”、“node01”三个虚拟机，其中“node03”正在安装 CentOS 6.4。
画面 13: 显示 VMware Workstation 界面，包含“node03”、“node02”、“node01”三个虚拟机，其中“node03”正在安装 CentOS 6.4。
画面 14: 显示 VMware Workstation 界面，包含“node03”、“node02”、“node01”三个虚拟机，其中“node03”正在安装 CentOS 6.4。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2: 环境搭建”，内容包括：
1. 创建虚拟机
   1. 安装虚拟机 VMware
   2. 创建虚拟机
   3. 安装 CentOS
   4. 组成集群
2. 配置宿主机
   1. 关闭防火墙
   2. 关闭 SELinux
   3. 设置主机名
   4. 重启
   5. 设置时钟同步服务
   6. 配置用户权限
   7. 免密登录
3. 安装辅助软件
   1. JDK
   2. Zookeeper
画面 6: PPT 标题为“4. 安装 Hadoop”，内容包括：
1. 下载并解压
2. 修改配置
3. 分发到每个节点
4. 格式化 HDFS
5. 启动集群
画面 10: PPT 标题为“VMware Workstation 10”，包含“创建新的虚拟机”、“虚拟化物理机”、“软件更新”等选项。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
