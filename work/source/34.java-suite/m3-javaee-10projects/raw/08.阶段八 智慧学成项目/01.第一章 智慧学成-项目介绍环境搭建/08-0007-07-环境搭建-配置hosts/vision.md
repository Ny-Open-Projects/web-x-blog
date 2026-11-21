# 画面线理解：07-环境搭建-配置hosts

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\07-环境搭建-配置hosts_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:06, 01:51, 02:26, 02:42, 03:06, 03:18, 03:37, 04:15, 04:50, 05:08, 05:24, 05:40, 06:10, 06:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:31:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Windows 系统中配置 hosts 文件，以便通过域名访问本地部署的 Hadoop、Spark、MySQL 等大数据服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程 PPT 页面，标题为“1.3 配置hosts”。
- 文本内容：配置服务器ip的host为：xc-online，以后访问项目使用：xc-online:端口号 即可。
- 服务器地址：192.168.1.101。
- hosts 文件示例内容：
  192.168.1.101 xc-online
  192.168.1.101 xc-online-hadoop
  192.168.1.101 xc-online-spark
  192.168.1.101 xc-online-mysql
  192.168.1.101 xc-online-yapi
  192.168.1.101 xc-online-es
  192.168.1.101 xc-online-zk
  192.168.1.101 xc-online-kafka
  192.168.1.101 xc-online-reds
  192.168.1.101 xc-online-hbase
- hosts 文件位置：C:\Windows\System32\drivers\etc
- PS：此文件不能直接修改，可复制到桌面修改完成后在复制回去，⚠️需截图
- PS：配置时以你服务器地址为准！

画面 2：
- 展示了 Windows 资源管理器，路径为 C:\Windows\System32\drivers\etc。
- 选中了 hosts 文件。

画面 3：
- 展示了 Sublime Text 编辑器打开 hosts 文件的内容。
- 文件内容为 Windows 系统默认的 hosts 文件注释和示例。

画面 4：
- 展示了 Sublime Text 编辑器，光标位于 hosts 文件的末尾，准备进行编辑。

画面 5：
- 展示了 PPT 页面，内容与画面 1 相同，但光标在 hosts 文件编辑器中。

画面 6：
- 展示了 PPT 页面，内容与画面 1 相同，但光标在 hosts 文件编辑器中。

画面 7：
- 展示了 Docker 容器终端，显示了容器的网络配置信息。
- 容器名称为：xc-online-1。
- 网络接口信息：link eth0 ...。

画面 8：
- 展示了 Sublime Text 编辑器，hosts 文件内容为空。

画面 9：
- 展示了 Windows 资源管理器，路径为 C:\Windows\System32\drivers\etc。
- 选中了 hosts 文件。

画面 10：
- 展示了 Windows 资源管理器，路径为 C:\Windows\System32\drivers\etc。
- 选中了 hosts 文件。

画面 11：
- 展示了 Typora 编辑器，内容为“docker使用教程.md”。
- 文本内容：安装docker社区版，以Ubuntu为例（这里假定已安装Ubuntu虚拟机，如果已有docker环境可不用）。
- PS：选择docker社区版是因为 docker对ubuntu友好，支持ubuntu 16.04 以上64位版本，这里采用的是ubuntu 18.04。
- 查看系统版本：
  lsb_release -a
  # 输出结果
  No LSB modules are available.
  Distributor ID: Ubuntu
  Description: Ubuntu 18.04.2 LTS
  Release: 18.04
  Codename: bionic
- docker新老版本不兼容，安装新版本的卸载老版本：
  sudo apt remove docker docker-engine docker.io containerd runc
- 安装依赖：

画面 12：
- 展示了 Hadoop 的 Web 管理界面，地址为：xc-online:50070。
- 页面标题：Overview “xc-online-hadoop:9000” (active)。
- 信息包括：Started, Version, Cluster ID, Block Pool ID。
- 安全性：Security is off。

画面 13：
- 展示了 Hadoop 的 Web 管理界面，地址为：xc-online:9000。
- 页面标题：Browse Directory。
- 列表显示了目录内容，包括：drwxr-xr-x, drwxrwxr-x 等文件权限和文件名。

画面 14：
- 展示了 PPT 页面，内容与画面 1 相同，但光标在 hosts 文件编辑器中。
