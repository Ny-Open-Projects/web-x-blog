# 32-RocketMQ-控制台安装配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们讲解LockitMQ远程连接的配置,以及Lockit Console控制台的配置安装。

LockitMQ Blocker默认是通过私有IP启动的,外部客户端是没办法进行远程连接。

那么我们要去修改它的配置文件,绑定能够对外访问的IP地址。

咱们在上面章节当中,对LockitMQ安装配置就已经是采用了对外访问的IP地址。

如果是有多块网卡的话,那么在这里面的IP就是需要你指定的能够对外访问的物理网卡。

咱们可以看一下LockitMQ的配置文件。

在这里我们可以看到它的地址就是指向本机的局域网地址。

10.10,20.251。

下面是MQ Blocker的启动脚本。

在这里面我们要加上一个参数,或者在配置文件当中去配置也是可以的。

这个参数的作用也就是说,如果咱们在LockitMQ当中,这个topic不存在,它就会自行进行创建。

如果不加这个参数,那么消费端或者服务发送端进行topic的发送。

可能就会报出印铲。

接着咱们就开始安装Lockit Control控制台。

Lockit Control地址在上面章节也已经提供出来。

大家可以看到,这个是在GitHub下面。

下载到本地之后,要进行MainWin的打包编译。

打包成功之后,会在Touch的目录下面生成一个可执行的架。

这个架就是LockitMQ Control的控制台。

如果Lockit的Console安装包已经是编译打包完成,咱们就可以直接跳到第五个步骤进行了配置和运行。

在这里我们就不重新进行编译,因为整个编译打包需要较长的时间。

在这里我们将生成完的架包直接上传到虚拟机当中,然后去配置和运行。

好,那咱们回到虚拟机。

好,那咱们回到虚拟机。

在这里,咱们已经进行了编译打包完成。

我们将LockitMQ Control它的运行后台上传到虚拟机里面。

咱们进行一个解压,Enable.

Console。

解压完成之后,它会产生一个新的架包文件。

咱们先在这里新建一个目录。

LockitMQ Control。

将这个架包放置该目录下面。

这样便于咱们的管理。

进入。

咱们刚才创建了目录。

LockitMQ Control。

那这是一个可执行的架。

如何去修改它的运行配置呢?

咱们回到讲义当中。

它其实是一个SplitBoot的应用程序。

咱们需要新建一个ApplicationProperties配置文件和架包放在同一个目录。

具体的配置信息只需要修改两项。

一个是修改它的运行端口。

另外一个是要配置LockitMQ NameServer的IP信息。

那咱们就来创建一下VIApplication.

Prop.

对这个配置文件的名称不要写错了。

咱们将它的配置内容拷贝进去。

这里的NameServer就在本机上面。

所以咱们是117.0.0.1。

配置完成之后,咱们就可以启动LockitMQ Control控制后台。

NoHalfMini加码档架。

这个在当前控制框口不需要输出日志。

将日志禁闭掉。

运行完成之后咱们查看一下进程是否存在。

进程已经启动成功。

咱们接着来访问LockitMQ的Ctrl控制后台。

这个就直接访问它的IP和端口就可以了。

咱们让它call一下。

注意一下这个IP咱们虚拟器是做了调整。

要指向咱们虚拟器说。

我们的IP,可以访问一下。

可以看到咱们就已经成功进入了LockitMQ Control的控制后台。

这里面它提示整个日期是存在问题。

让咱们将日期做一个同步。

然后再去重启下这个后台服务。

咱们通过NTP命令去同步虚拟器上面的时间。

指向阿里云的地址。

同步完成之后咱们重启下LockitMQ的控制台。

将进程结束。

再次检查一下。

接着咱们再去启动LockitMQ控制后台。

检查一下进程。

重启控制台完成之后咱们再次访问下。

发信者的界面。

这样就没有出现刚才的提示。

如果是之前测试的时候出现这种情况。

要检查这个时间日期是否正确。

同时也要检查它的时区设置。

在这里面的话要确保这个时间跟咱们系统的时间是一致的。

这样就不会出现刚才的错误提示。

在Lockit的控制后台当中我们可以看到它有很多的一些功能。

比如这个是它的控制台以表盘。

里面对整个LockitMQ机器有个整体的监控。

包括像Blockup信息、Publico等相关的使用信息。

然后上面有Cluster集群的一些信息监控。

下面是Topic。

针对于Topic控制后台可以进行相应的维护。

比如说可以删除某一个Topic。

可以去重置它的一个消费的位点。

也就是消费的进度。

也可以去查看Topic它当前运行的状态。

在这里面都会有一些详细的记录。

然后还包括什么。

然后还包括像Consume的消费信息。

Producer生产者的一些信息。

Message消息的一些管理。

更多的功能大家有兴趣可以在自行去研究和摸索。

那在这里咱们就完成了Lockit的控制后台的安装和配置。

这一讲咱们就先讲到这里。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为“Day11”系列的一部分，主要讲解如何在 Linux 系统上安装、配置并验证 RocketMQ 4.4.0 版本及其配套的 RocketMQ Console 控制台。课程内容按步骤进行，首先配置 RocketMQ 服务使其支持远程连接，然后安装并配置 RocketMQ Console 控制台，最后通过浏览器访问控制台并验证其功能。整个过程以命令行操作为主，辅以文档和网页界面演示，旨在为学习者提供一个完整的 RocketMQ 环境搭建实践。

---

### 2) 按时间顺序的章节（带时间点）

*   **3.5 远程连接配置 (00:00:00 - 00:00:15)**
    *   介绍 RocketMQ 默认通过私有 IP 启动，外部客户端无法连接。
    *   需要修改配置文件 `conf/broker.conf`，将 `namesrvAddr` 和 `brokerIP1` 修改为服务器对外的实际 IP 地址。
    *   演示了启动命令：`sh bin/mqbroker -n 127.0.0.1:9876 autoCreateTopicEnable=true -c /usr/local/rocketmq_4.4.0/conf/broker.conf &`

*   **3.6 安装 Rocket Console 控制台 (00:00:15 - 00:00:30)**
    *   介绍 RocketMQ Console 是一个 Web 管理界面，用于监控和管理 RocketMQ 服务。
    *   演示了如何解压控制台的安装包 `rocketmq-console-ng-1.0.0.zip`。
    *   如果系统没有 Maven 环境，演示了通过 `yum -y install maven` 命令进行安装。

*   **3.7 验证 (00:00:30 - 00:00:45)**
    *   演示了如何在解压后的目录中新建 `application.properties` 配置文件。
    *   在配置文件中设置 `server.port=9800` 和 `rocketmq.config.namesrvAddr=127.0.0.1:9876`。
    *   使用 `nohup java -jar rocketmq-console-ng-1.0.0.jar > /dev/null 2>&1 &` 命令启动控制台服务。

*   **3.8 其他命令 (00:00:45 - 00:00:55)**
    *   演示了如何通过 `ps -ef | grep console` 命令查看控制台进程是否已成功启动。
    *   通过 `kill -9 <PID>` 命令终止进程。

*   **3.9 FAQ (00:00:55 - 00:01:00)**
    *   未在画面中展示具体内容，但章节标题已出现。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容:**
    *   **章节标题:** `3.5 远程连接配置`, `3.6 安装 Rocket Console 控制台`, `3.7 验证`。
    *   **配置文件内容:**
        ```text
        namesrvAddr=10.10.20.15:9876
        brokerIP1=10.10.20.15
        ```
    *   **启动命令:**
        ```bash
        sh bin/mqbroker -n 127.0.0.1:9876 autoCreateTopicEnable=true -c /usr/local/rocketmq_4.4.0/conf/broker.conf &
        ```
    *   **控制台配置文件内容:**
        ```properties
        server.port=9800
        rocketmq.config.namesrvAddr=127.0.0.1:9876
        ```
    *   **启动控制台命令:**
        ```bash
        nohup java -jar rocketmq-console-ng-1.0.0.jar > /dev/null 2>&1 &
        ```

*   **图表:**
    *   在 `3.7 验证` 章节中，PPT 展示了 RocketMQ 控制台的仪表盘（Dashboard）页面，包含多个图表，如“Broker TOP 10”、“Broker Send trend”等，用于展示 RocketMQ 服务的运行状态和性能指标。

---

### 4) 关键场景与演示描述

*   **场景一：配置 RocketMQ 服务 (00:00:00 - 00:00:15)**
    *   **演示:** 在终端中，用户通过 `vi conf/broker.conf` 命令打开配置文件，并修改 `namesrvAddr` 和 `brokerIP1` 的值。
    *   **关键操作:** 修改配置文件后，用户执行 `sh bin/mqbroker -n 127.0.0.1:9876 autoCreateTopicEnable=true -c /usr/local/rocketmq_4.4.0/conf/broker.conf &` 命令启动 RocketMQ 服务。

*   **场景二：安装 RocketMQ Console (00:00:15 - 00:00:30)**
    *   **演示:** 用户在终端中执行 `unzip rocketmq-console-1.0.0.zip` 命令解压安装包。
    *   **关键操作:** 如果系统没有 Maven，用户执行 `yum -y install maven` 命令安装 Maven。

*   **场景三：配置并启动 RocketMQ Console (00:00:30 - 00:00:45)**
    *   **演示:** 用户在解压后的目录中创建 `application.properties` 文件，并编辑其内容。
    *   **关键操作:** 用户执行 `nohup java -jar rocketmq-console-ng-1.0.0.jar > /dev/null 2>&1 &` 命令启动控制台服务。

*   **场景四：验证控制台 (00:00:45 - 00:00:55)**
    *   **演示:** 用户在终端中执行 `ps -ef | grep console` 命令，查看控制台进程是否已成功启动。
    *   **关键操作:** 用户执行 `kill -9 <PID>` 命令终止进程。

*   **场景五：访问控制台 (00:00:55 - 00:01:00)**
    *   **演示:** 用户在浏览器中输入 `http://10.10.20.251:9800/#/` 地址，访问 RocketMQ Console。
    *   **关键操作:** 用户成功访问控制台，页面显示了多个 Topic 的列表和操作按钮，如“STATUS”、“ROUTER”、“SEND MESSAGE”等。
