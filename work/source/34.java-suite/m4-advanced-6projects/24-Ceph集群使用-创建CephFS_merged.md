# 24-Ceph集群使用-创建CephFS — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始创建SafeFS

SafeFS是Safe的一个文件系统

集群创建搭建完毕之后

默认它是没有文件系统的

没有文件系统

我们就没办法进行文件的操作和存储

对不对

所以我们需要创建一个SafeFS

让它可以支持对外访问的文件系统

好

我们看一下具体怎么去操作和执行

首先我们要创建两个存储词

这个存储词

一个是它的数据

一个是它的原数据

在这里是它的参数配置

如果我们是少于5个OSD节点

可以把PGNAM

这个就是PGNAM

设置为128

如果OSD数量

它在5到10个之间

可以将它适当放大一点

那么OSD在10到50个节点

就是有50个节点组成这样一个集群的话

那么我们可以将它的PGNAM设置为4096

更大一点

成几何数的一个增长

那OSD数量的话

它大于50

这个就需要计算PGNAM的具体值

好

通过下面命令的话

我们可以列出当前创建的存储词

因为我之前已经做了测试验证

所以在这里都已经搭建完毕

我们来看一下

在这下面的话

就是我们所创建的Safe的存储词

可以看到有SafeFSData

还有一个Metadata

好

创建两个存储词

存储词完毕之后

我们接下来就要创建FS

怎么去创建

通过一下命令

这个就是SafeFS的一个创建命令

然后要去new新建一个

对不对

名称就是FSTest

然后要将刚才创建的两个存储词

做一个关联

这个是它的一个命令的作用

好

在这里执行完成之后

我们就要去查看它的一个状态

怎么去查看

通过SafeFS的命令

然后下面再加上一个参数

就是LS

跟我们Linux

这种LS命令是一样的

我们来看一下

好

这个时候就可以看到

名称为FSTest了

并且原数据连接词是

我们刚才所创建的Metadata

对不对

DataPulse是SafeFSData

这个和刚才创建的都是一样的

好

那么我们可以看一下它的一个状态

是否是正常运行呢

SafeMDSState

这个时候可以看到

它有一个节点正在正常运行

对不对

是一个up激活的一个状态

好

这里要注意一下

如果说我们创建错误了

那么怎么办呢

就是说可能名称创建错误了

或者删除设置错误了

这个时候我们需要做一个删除

怎么去删除呢

通过一下命令

命令也提供出来了

便于大家的一个测试验证

这个就是RM

先删除它的一个名称对不对

注意还要给它一个参数

就是确定你真的是要删除

然后是Delete

Delete是哪些呢

FSTate这个也必须要完全删除

在删除之前

我们一定要确保在Safe Config下面

开启了以下的配置

允许进行数据连接时的一个删除操作

这个就是

如果是出现问题的时候

该怎么去处理

下面我们再看一下

在上面创建完成之后

我们采用Fuse方式进行挂载

这个是怎么操作呢

首先我们要去安装SafeFuse这样一个组件

如果没有

要进行RM的一个安装

安装完成之后

我们可以创建一个挂载目录

就是给它一个目录

可以看到

cd user local

在下面会有一个SafeFS的挂载目录

怎么去挂载呢

通过SafeFuse

然后去指定你的一个密钥信息

然后-m

以及你的连接和端口信息

最后就是我们所挂载的目标目录

这样它就会去创建和挂载

挂载完成之后

就能够查看到它对应的一个磁盘挂载的信息

我们可以看一下

在这里还没有挂载

那么我们来挂载一下

这个已经启动完Fuse

我们再去查看一下

df-h

这个时候是不是可以看到

我们已经将SafeFS这个目录

已经挂载成功了

空间是二次集讯

可用的一个空间

这样就可以看到了

它就可以便于我们去访问和操作

它的一个磁盘数据

这个就是对SafeFS的一个创建和配置

好那这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 Ceph 分布式存储系统中 **CephFS 文件系统** 的创建与挂载教程。讲师在 Ceph 集群已部署完毕后，演示了如何创建两个存储池（metadata 和 data pool），然后创建一个名为 `fs_test` 的 CephFS 文件系统，并通过 `ceph-fuse` 工具将其挂载到本地目录。整个过程包含命令行操作、参数配置说明以及错误处理方法，旨在指导用户完成 CephFS 的基础部署。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，讲师在 Typora 编辑器中展示课程大纲，定位到“3.6 创建Cephfs”章节。
*   **00:00:05 - 00:00:15**: 讲师讲解创建 CephFS 的前提：集群已创建，但默认无文件系统，需要手动创建。
*   **00:00:15 - 00:00:30**: 讲师演示第一步：创建两个存储池。屏幕上显示命令：
    ```bash
    ceph osd pool create cephfs_data 128
    ceph osd pool create cephfs_metadata 64
    ```
    同时，讲师解释了 `pg_num` 参数的推荐值，根据 OSD 数量进行调整。
*   **00:00:30 - 00:00:45**: 讲师演示第二步：创建 CephFS 文件系统。屏幕上显示命令：
    ```bash
    ceph fs new fs_test cephfs_metadata cephfs_data
    ```
*   **00:00:45 - 00:01:00**: 讲师演示第三步：检查文件系统状态。屏幕上显示命令及输出：
    ```bash
    ceph fs ls
    # 输出示例：
    name: fs_test, metadata pool: cephfs_metadata, data pools: [cephfs_data]
    ```
    同时，讲师也展示了 MDS 状态：
    ```bash
    ceph mds stat
    # 输出示例：
    fs_test-1/1 up {0=centos7-1-up:active}
    ```
*   **00:01:00 - 00:01:15**: 讲师讲解如果创建失败，如何删除。屏幕上显示命令：
    ```bash
    ceph fs rm fs_test --yes-i-really-mean-it
    ceph osd pool delete cephfs_data cephfs_data --yes-i-really-really-mean-it
    ```
    并提示需要在 `ceph.conf` 中开启 `mon allow pool delete = true`。
*   **00:01:15 - 00:01:30**: 讲师开始讲解如何挂载 CephFS。屏幕上显示命令：
    ```bash
    yum -y install ceph-fuse
    ```
*   **00:01:30 - 00:01:45**: 讲师演示创建挂载目录：
    ```bash
    mkdir -p /usr/local/cephfs_directory
    ```
*   **00:01:45 - 00:02:00**: 讲师演示使用 `ceph-fuse` 命令挂载文件系统：
    ```bash
    ceph-fuse -k /etc/ceph/ceph.client.admin.keyring -m 10.10.20.11:6789 /usr/local/cephfs_directory
    ```
    屏幕上显示了 `ceph-fuse` 的启动日志。
*   **00:02:00 - 00:02:15**: 讲师演示查看挂载点信息：
    ```bash
    df -h
    ```
    屏幕上显示了 `/usr/local/cephfs_directory` 已成功挂载，大小为 27G。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `3.6 创建Cephfs`
    *   **核心步骤**:
        1.  创建两个存储池：`ceph osd pool create cephfs_data 128` 和 `ceph osd pool create cephfs_metadata 64`。
        2.  创建文件系统：`ceph fs new fs_test cephfs_metadata cephfs_data`。
        3.  查看状态：`ceph fs ls` 和 `ceph mds stat`。
        4.  错误处理：`ceph fs rm fs_test --yes-i-really-mean-it` 和 `ceph osd pool delete cephfs_data cephfs_data --yes-i-really-really-mean-it`。
        5.  挂载：`yum -y install ceph-fuse`，`mkdir -p /usr/local/cephfs_directory`，`ceph-fuse -k ... /usr/local/cephfs_directory`。
    *   **配置说明**:
        *   `mon allow pool delete = true` (需在 `ceph.conf` 中开启)。
    *   **参数说明**:
        *   `pg_num` 的推荐值：少于5个OSD → 128；5-10个OSD → 512；10-50个OSD → 4096；大于50个OSD → 需要计算。

*   **代码/命令**:
    *   **创建存储池**:
        ```bash
        ceph osd pool create cephfs_data 128
        ceph osd pool create cephfs_metadata 64
        ```
    *   **创建文件系统**:
        ```bash
        ceph fs new fs_test cephfs_metadata cephfs_data
        ```
    *   **检查状态**:
        ```bash
        ceph fs ls
        ceph mds stat
        ```
    *   **删除操作**:
        ```bash
        ceph fs rm fs_test --yes-i-really-mean-it
        ceph osd pool delete cephfs_data cephfs_data --yes-i-really-really-mean-it
        ```
    *   **安装与挂载**:
        ```bash
        yum -y install ceph-fuse
        mkdir -p /usr/local/cephfs_directory
        ceph-fuse -k /etc/ceph/ceph.client.admin.keyring -m 10.10.20.11:6789 /usr/local/cephfs_directory
        ```
    *   **配置文件**:
        ```ini
        [mon]
        mon allow pool delete = true
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建存储池 (00:00:15)**
    *   讲师在 Typora 中展示命令行界面，输入并执行了两个 `ceph osd pool create` 命令，分别创建了 `cephfs_data` 和 `cephfs_metadata` 两个存储池，并设置了初始的 `pg_num` 值。
    *   讲师同时在屏幕右侧用文字标注了不同 OSD 数量对应的 `pg_num` 推荐值，强调了配置的重要性。

*   **场景二：创建并验证 CephFS (00:00:30)**
    *   讲师执行 `ceph fs new fs_test cephfs_metadata cephfs_data` 命令，成功创建了名为 `fs_test` 的文件系统。
    *   讲师随后执行 `ceph fs ls` 和 `ceph mds stat` 命令，屏幕上显示了文件系统的名称、元数据池和数据池信息，以及 MDS 状态为 `up`，表明文件系统已正常运行。

*   **场景三：挂载 CephFS (00:01:45)**
    *   讲师演示了 `ceph-fuse` 的挂载过程。屏幕上显示了 `ceph-fuse` 的启动日志，确认了客户端已成功连接到 Ceph 集群。
    *   讲师执行 `df -h` 命令，屏幕上显示了 `/usr/local/cephfs_directory` 已成功挂载，大小为 27G，证明挂载操作成功。

*   **场景四：错误处理 (00:01:00)**
    *   讲师在屏幕上展示了删除命令 `ceph fs rm fs_test --yes-i-really-mean-it` 和 `ceph osd pool delete cephfs_data cephfs_data --yes-i-really-really-mean-it`，并强调了在配置文件中开启 `mon allow pool delete = true` 的必要性，以防止因权限问题导致操作失败。

*   **场景五：多窗口切换 (00:00:50)**
    *   讲师在演示过程中，曾短暂切换到
