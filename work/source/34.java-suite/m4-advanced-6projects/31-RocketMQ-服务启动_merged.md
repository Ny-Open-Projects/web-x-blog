# 31-RocketMQ-服务启动 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就来启动LockitMQ服务

首先我们要启动NameServer

NameServer的作用呢

之前咱们也做了讲解

它是存储当前集群所有的Blockers信息

所以呢

咱们要先将NameServer启动

才能启动Blocker

首先去执行MQ NameServer的启动命令

为了跟讲义当中的命令保持一致

咱们也将LockitMQ安装目录呢

做一个调整

将它从命名改成LockitMQ-10.4

好

从命名完成之后

咱们就来启动NameServer

直接copy

然后运行

注意这条命令

NoHub呢

是以后台方式运行

日志呢

是从令下DWIN2

也就是说不进行日志的记录和输出

如果大家在启动时候

遇上问题

可以将这一段去除

也是NoHub

以及后面日志屏蔽这一段

给它去除

看一下它具体的报酬信息

然后再做对应的排查处理

咱们首先去运行一下

脚本执行完成之后

检查一下服务是否正常运行

好

可以看到

MQ NameServer呢

这个进程已经启动成功

那咱们也可以检查一下

它的启动日志

6

-f

这个是在当前用户顾顾下面

LockitMQ

这个是一个专门用于LockitMQ日志记录的文件夹

找到NimServer的日志文件

可以看到它打印出来

启动成功的提示

咱们退出

日志文件呢

跟上面这个日志是不一样的

上面这个日志呢

它是直接输入在咱们的控制终端

这样不便于咱们命令的交互

所以呢

我们将控制终端的这个日志记录

呢

停闭掉了

停闭掉之后呢

但是LockitMQ

它实质上还是会记录它的运行日志的

这个路径呢

大家要清楚是哪个用户启动

它就会在相应的用户目录下面去生成它的日志文件

启动完NimServer之后

咱们就来启动Blocker

上面启动的NimServer呢

它默认端口是9876

咱们可以看一下通过net

state-apn

端口是9876

这个端口呢

是正常监听

它整个服务呢

NimServer这个服务呢

是启动成功的

那么咱们就来启动Blocker

在启动命令当中呢

要去指定NimServer的地址和端口

咱们启动一下

启动完成之后

咱们查看一下它的输出日志

可以看到Blocker呢

它成功注册到NimServer上面

那咱们就实现了

NimServer以及Blocker的启动

接下来咱们还要掌握一下

它的相关管理命令

比如说如何去停止Blocker

停止命令可以通过

闭目录自带的脚本去完成

咱们可以执行一下

去关闭Blocker

好,它提示呢

Blocker已经关闭完成

接下来再以关闭NimServer

注意关闭的顺序跟启动的顺序呢

是相反的

启动的时候呢

咱们要先启动NimServer才能启动Blocker

那么关闭的时候呢

就要反过来

先关闭Blocker

再关闭NimServer

有时候大家经常去操作呢

可能会忘记了它的顺序

那么咱们可以去做一个封装

自立LockitMQ的启动与关闭脚本

咱们先Copy下启动脚本内容

回到终端

进入它的Bin目录

在下面呢

我们去创建一个StataApp

我们先把我们的脚本

然后将内容扩幅进来

接着给它赋予一个权限

777是最大的一个权限

然后咱们再去封装它的关闭脚本

vi shutdown.sh

将它粘连进来

wq进行保存

同样也加上它最大的权限

好

咱们就完成了

它的启动以及关闭的自立脚本

好

我们再去装它的关闭脚本

那咱们来测试一下

先检查一下

进程是否正常运行

那咱们就先执行了关闭脚本

点杠

shutdown

好

它提示呢已经关闭完成

咱们再来看一下

可以看到LockitMQ进程呢就已经消失

咱们再启动一下

我们检查一下它的进程LockitMQ

好

我们可以看到呢

LockitMQ进程呢

都已经成功启动

那咱们自定义封装的启动与关闭脚本呢

是能够正常执行的

在这里咱们就完成了LockitMQ服务的管理

并且呢

封装了自定义的启动和关闭脚本

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 **RocketMQ 4.4.0 版本的安装与服务管理** 的技术教程。讲师通过在 Linux 环境下操作，演示了如何启动和停止 RocketMQ 的核心服务组件：**Name Server** 和 **Broker**。主要内容包括：
- **启动服务**：详细展示了启动 Name Server 和 Broker 的命令行操作，并说明了如何通过 `tail -f` 命令实时查看日志以确认服务是否成功启动。
- **停止服务**：演示了如何使用 `mqshutdown` 命令分别停止 Broker 和 Name Server。
- **自定义脚本**：讲解了如何编写一个 `shutdown.sh` 脚本，以简化服务的关闭流程。
- **远程连接配置**：在演示停止服务后，讲师开始介绍如何修改配置文件，使 Broker 服务能够对外提供远程连接，这是后续操作的前置条件。

整个过程以命令行操作为主，旨在教授学员如何在实际环境中部署和管理 RocketMQ 服务。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取视频的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

- **3.4 启动服务 (0:00 - 0:30)**
    - **1. 启动 Name Server**：演示了启动命令 `nohup /usr/local/rocketmq_4.4/bin/mqnamesrv > /dev/null 2>&1 &`。
    - **查看日志**：使用 `tail -f ~/logs/rocketmqlogs/namesrv.log` 查看启动日志。
    - **成功提示**：日志中出现 `The Name Server boot success. serializeType=JSON` 表示启动成功。

- **3.4 启动服务 (0:30 - 1:00)**
    - **2. 启动 Broker**：演示了启动命令 `nohup /usr/local/rocketmq_4.4/bin/mqbroker -n 127.0.0.1:9876 > /dev/null 2>&1 &`。
    - **查看日志**：使用 `tail -f ~/logs/rocketmqlogs/broker.log` 查看启动日志。
    - **成功提示**：日志中出现 `The broker[localhost.localdomain, 10.10.20.10:10911] boot success. serializeType=JSON and name server is 127.0.0.1:9876` 表示启动成功。

- **3.4 启动服务 (1:00 - 1:30)**
    - **3. 停止命令**：演示了停止命令 `mqshutdown broker` 和 `mqshutdown namesrv`。
    - **4. 自定义启动与关闭脚本**：讲解了如何编写 `shutdown.sh` 脚本。

- **3.5 远程连接配置 (1:30 - 2:00)**
    - 讲师开始介绍如何修改配置文件，使 Broker 服务能够对外提供远程连接。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

- **PPT 内容**：
    - **章节标题**：`3.4 启动服务`。
    - **子章节**：
        - `1. 启动 Name Server`
        - `2. 启动 Broker`
        - `3. 停止命令`
        - `4. 自定义启动与关闭脚本`
        - `3.5 远程连接配置`
    - **关键提示文本**：
        - `The Name Server boot success. serializeType=JSON`
        - `The broker[localhost.localdomain, 10.10.20.10:10911] boot success. serializeType=JSON and name server is 127.0.0.1:9876`
        - `出现以下提示，代表启动成功：`
        - `停止脚本：`
        - `脚本内容：`
        - `增加执行权限：`

- **代码/命令**：
    - **启动 Name Server**：
        ```bash
        nohup /usr/local/rocketmq_4.4/bin/mqnamesrv > /dev/null 2>&1 &
        ```
    - **查看 Name Server 日志**：
        ```bash
        tail -f ~/logs/rocketmqlogs/namesrv.log
        ```
    - **启动 Broker**：
        ```bash
        nohup /usr/local/rocketmq_4.4/bin/mqbroker -n 127.0.0.1:9876 > /dev/null 2>&1 &
        ```
    - **查看 Broker 日志**：
        ```bash
        tail -f ~/logs/rocketmqlogs/broker.log
        ```
    - **停止 Broker**：
        ```bash
        /usr/local/rocketmq_4.4/bin/mqshutdown broker
        ```
    - **停止 Name Server**：
        ```bash
        /usr/local/rocketmq_4.4/bin/mqshutdown namesrv
        ```
    - **自定义脚本 `shutdown.sh`**：
        ```bash
        #!/bin/sh
        echo "============shutdown broker ============"
        /usr/local/rocketmq_4.4/bin/mqshutdown broker
        echo "============shutdown name server ============"
        /usr/local/rocketmq_4.4/bin/mqshutdown namesrv
        ```
    - **增加脚本执行权限**：
        ```bash
        chmod 777 *.sh
        ```

---

### 4) 关键场景与演示描述

- **场景一：启动 Name Server**
    - 讲师在终端中输入启动命令 `nohup /usr/local/rocketmq_4.4/bin/mqnamesrv > /dev/null 2>&1 &`。
    - 随后，讲师使用 `tail -f ~/logs/rocketmqlogs/namesrv.log` 命令实时监控日志。
    - **关键演示**：日志中出现 `The Name Server boot success. serializeType=JSON`，表明 Name Server 已成功启动。

- **场景二：启动 Broker**
    - 讲师在终端中输入启动命令 `nohup /usr/local/rocketmq_4.4/bin/mqbroker -n 127.0.0.1:9876 > /dev/null 2>&1 &`。
    - 随后，讲师使用 `tail -f ~/logs/rocketmqlogs/broker.log` 命令实时监控日志。
    - **关键演示**：日志中出现 `The broker[localhost.localdomain, 10.10.20.10:10911] boot success. serializeType=JSON and name server is 127.0.0.1:9876`，表明 Broker 已成功启动。

- **场景三：停止服务**
    - 讲师在终端中输入 `mqshutdown broker` 命令停止 Broker。
    - 随后，讲师输入 `mqshutdown namesrv` 命令停止 Name Server。
    - **关键演示**：终端输出 `Shutdown broker` 和 `Shutdown name server`，表示服务已成功停止。

- **场景四：编写自定义脚本**
    - 讲师在 PPT 上展示 `shutdown.sh` 脚本的代码内容。
    - 讲师在终端中使用 `vi shutdown.sh` 命令创建并编辑脚本。
    - 讲师使用 `chmod 777 *.sh` 命令为脚本增加执行权限。
    - **关键演示**：脚本内容清晰地展示了如何通过一行命令同时关闭 Broker 和 Name Server。

- **场景五：远程连接配置**
    - 讲师在 PPT 上展示 `3.5 远程连接配置` 章节。
    - 讲师指出，Broker 默认通过 IP 启动，外部客户端无法远程连接。
    - **关键演示**：讲师开始讲解如何修改配置文件（如 `broker.conf`），将 `brokerIP1` 设置为对外 IP 地址，以实现远程连接功能。
