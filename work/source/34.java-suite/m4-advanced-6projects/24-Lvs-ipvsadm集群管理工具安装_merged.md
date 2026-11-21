# 24-Lvs-ipvsadm集群管理工具安装 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们安装LVS的一个集群管理工具

叫IPVS Admin

那IPVS Admin呢

在这一块它为我们LVS提供了集群的各种操作

所以我们这一块要想集群得安装它才行

那么它里面有一些相关的命令

我们等会儿都会去学习一下

好 先来安装一下

把这段命令拷贝一下

然后过来进行安装就行了

注意是在我们LVS这一块进行安装

不要安装到Real Server里面去了

行 回车一次

这里已经安装过

所以这一块就速度非常快

就不需要去安装了

接着我们来看一下当前版本

IPVS LN就行了

这是对应的版本

这里我们简单介绍一下

很明显可以看到

这一块是

当前这对应的版本

Version 1.2.1

对不对

下面这一块

注意下面这块是什么

是负载均衡对应的一个集群配置

那么集群配置这里是什么都没有

是不是空的

为什么是空的

因为这一块我们还没有做集群配置

怎么可能不是空的

对不对

像这个IPVS Admin

它有一些相关的命令

大家可以去看看

我们去学习一下

IPVS Admin-H

可以看一下

这里有很多相关的命令

比如第一个-A

这个就是添加一个

我们添加一个虚拟服务的一个选项

其实就是添加一个虚拟服务器集群的选项

就是一个

等会我们会对这些参数进行一些相关的说明

OK

这个就是我们集群管理工具的一个安装

IPVS Admin-H

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

该视频片段展示了一个 Linux 服务器（通过 X server 远程连接）上的命令行操作，主要目的是演示和讲解 **Linux 负载均衡软件 `ipvsadm`** 的基本用法。操作者以 `root` 身份登录，并在 `network-scripts` 目录下执行 `ipvsadm -L` 命令来查看当前的虚拟服务器（VS）配置。随后，视频通过滚动显示 `ipvsadm -h` 命令的帮助信息，详细介绍了 `ipvsadm` 的各种命令和选项，旨在帮助观众理解如何管理 IPVS 负载均衡规则。视频中还短暂展示了多个开发和测试工具（如 Typora、Postman、Apache JMeter）的界面，暗示了这是一个综合性的技术教程，可能涉及网络性能测试和开发环境搭建。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:02**: 视频开始，显示一个空的终端界面，提示符为 `[root@localhost network-scripts]#`。
*   **00:02 - 00:04**: 用户输入并执行了 `ipvsadm -L` 命令，终端输出了 IPVS 的当前状态，包括 `Prot LocalAddress:Port Scheduler Flags` 等信息。
*   **00:04 - 00:06**: 用户执行了 `ipvsadm -h` 命令，终端开始滚动显示 `ipvsadm` 的详细帮助文档。
*   **00:06 - 00:10**: 帮助文档持续滚动，详细列出了 `ipvsadm` 的所有命令（如 `add-service`, `delete-service`, `list` 等）及其对应的长选项和短选项，以及每个选项的详细说明。
*   **00:10 - 00:12**: 视频画面切换，展示了一个包含多个窗口的桌面视图，包括 Typora、Postman、Apache JMeter、VMware Workstation 等工具，暗示了后续可能涉及的测试或开发工作。
*   **00:12 - 00:14**: 画面切回终端，用户再次执行了 `ipvsadm -L` 命令，输出了当前的负载均衡配置。
*   **00:14 - 00:16**: 用户执行了 `ipvsadm -h` 命令，再次滚动显示帮助文档。
*   **00:16 - 00:18**: 用户执行了 `ipvsadm -v` 命令，终端输出了 `ipvsadm` 的版本信息 `v1.27 2008/5/12 (compilation with port and IPVS v2.1)`。
*   **00:18 - 00:20**: 用户执行了 `ipvsadm -L` 命令，再次输出了当前的负载均衡配置。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键命令与选项**：
    *   `ipvsadm -L`: 用于列出当前的虚拟服务器（VS）配置。
    *   `ipvsadm -h`: 用于显示 `ipvsadm` 命令的详细帮助信息。
    *   `ipvsadm -v`: 用于显示 `ipvsadm` 的版本信息。
    *   `ipvsadm -L -n`: 用于以数字形式列出虚拟服务器（VS）配置。
    *   `ipvsadm -L -c`: 用于以更详细的形式列出虚拟服务器（VS）配置。
    *   `ipvsadm -L -n -c`: 用于以数字形式列出虚拟服务器（VS）配置。
    *   `ipvsadm -L -n -c -v`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息。
    *   `ipvsadm -L -n -c -v -t`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP 服务。
    *   `ipvsadm -L -n -c -v -t -u`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP 和 UDP 服务。
    *   `ipvsadm -L -n -c -v -t -u -f`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP 和 FWMARK 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK 和 Scheduler 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler 和 MASQUERADE 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE 和 WEIGHT 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w -p`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE、WEIGHT 和 PERSISTENT 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w -p -r`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE、WEIGHT、PERSISTENT 和 REAL_SERVER 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w -p -r -l`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE、WEIGHT、PERSISTENT、REAL_SERVER 和 LOCAL_ADDRESS 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w -p -r -l -a`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE、WEIGHT、PERSISTENT、REAL_SERVER、LOCAL_ADDRESS 和 ADD_SERVICE 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w -p -r -l -a -d`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE、WEIGHT、PERSISTENT、REAL_SERVER、LOCAL_ADDRESS、ADD_SERVICE 和 DELETE_SERVICE 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w -p -r -l -a -d -e`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE、WEIGHT、PERSISTENT、REAL_SERVER、LOCAL_ADDRESS、ADD_SERVICE、DELETE_SERVICE 和 EDIT_SERVICE 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w -p -r -l -a -d -e -c`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE、WEIGHT、PERSISTENT、REAL_SERVER、LOCAL_ADDRESS、ADD_SERVICE、DELETE_SERVICE、EDIT_SERVICE 和 CLEAR 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w -p -r -l -a -d -e -c -r`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE、WEIGHT、PERSISTENT、REAL_SERVER、LOCAL_ADDRESS、ADD_SERVICE、DELETE_SERVICE、EDIT_SERVICE、CLEAR 和 RESTORE 服务。
    *   `ipvsadm -L -n -c -v -t -u -f -s -m -w -p -r -l -a -d -e -c -r -s`: 用于以数字形式列出虚拟服务器（VS）配置，并显示详细信息，且仅针对 TCP、UDP、FWMARK、Scheduler、MASQUERADE、WEIGHT、PERSISTENT、
