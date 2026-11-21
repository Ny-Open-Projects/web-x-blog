# 25-Ceph集群使用-Rados客户端连接验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就开始呢

采用客户端对Safe集群进行一个连接验证

那之前呢

在讲解Safe集群搭建过程当中

如果大家有些不明白

或者说操作步骤当中有些问题

这个话呢

不必要担心

因为我们在这里呢

主要是册中Safe的基本用法

以及呢

跟项目的基层使用

Safe集群这一块的话呢

如果是大家有能力

或者说有时间的话呢

能够掌握

那是更好

好

那我们呢

就开始对客户端进行一个连接和验证

首先呢

我们要确保安装好JDK

Git以及呢

Maven

那怎么去操作呢

在我们的20.11这台主节点上面

我们就以这台节点呢

作为客户端

对我们Safe集群进行一个连接测试

那确定好JDK

JDK的话呢

建议采用1.8以上的版本

那Git的话呢

我们也可以看一下

Git的话呢

Git

我选Git

这里评错了

Git版本的话呢

1.8以上版本就可以了

Maven的话呢

我们也看一下

Maven的话呢

我们采用3.0以上的一个版本

大家的话呢

按照我们的环境

安装对应的一个版本就可以

安装完成之后呢

我们要将那个

Redox Java的一个原码呢

将它呢下载下来

大家还记不记得

在我们讲解Safe的整个架构的时候呢

我们要先讲一下

我们知道

就是Redox可以进行什么

进行Redox对象存储系统的一些操作

那我们这些的话呢

就是采用这种方式进行一个访问

后面章节当中呢

我们还会给大家讲解

如何是使用那个Safe的API接口

通过Redox GW的网关形式进行访问

好

咱们呢

还是继续回到刚才

将这个Redox Java原码呢

下载完成之后

我们可以看一下

在这里面我们新建的一个目录

这个目录呢

就是source cd

然后呢

在下面会有对应的我们的一个Safe plant测试的Java内

对不对

还有Redox Java的一个主件

好

那么呢

我们就将这个Redox Java下载到source下面的这个目录

好

下载完成之后呢

要进行一个什么

编译安装

那么呢

我们可以看一下进入这个目录

这里都是Java的原码

对吧

通过这个命令进行一个编译安装

然后呢

他会生成一个Redox 0.6.0的一个加包

我们可以看一下

在插起的目录下面

会有一个Redox 0.6.0的一个版本加包

好

我们要创建它对应的一个软链接

因为的话

你运行的时候

他必须要什么

加入class pass对不对

环境变量好

那么怎么创建

这个软链接呢

就是将这个Redox加包呢

指向到我们的JRE

lab下面的EXT扩展目录下面

然后呢

我们还安装一个JNA

这个JNA的话呢

要做一个本地接口的一个调用

对不对

那我们创建一个软链接

软链接怎么创建呢

同样指定user需要java.jna.j

然后呢

扩展那个指向到ext.jna.j

然后呢

我们可以去查看

在这里呢

已经是创建好了

可以看到他的指向是OK的

对不对

如果说指向出现问题了

这个呢

会在不停的会不停的闪动啊

然后的话

我们再看一下下面这个

这个的话呢

也是指向正确的好

指向正确之后呢

我们接下去看一下java的测试类

他怎么进行测试的呢

他整个代码流程来讲呢

也比较简单

首先的话呢

他会去创建一个Redox的测试类

他会去创建一个redox的对象

那这个redox对象的话呢

会给他一个名称

名称的话呢

我们就采用admin就可以了

然后这里会输出一行日志

对不对

就说明了整个集群这个对象呢

他是创建成功的

接着的话呢

我们要去读取系统的配置

读取系统配置呢

要指向我们这个save的配置文件

大家可以看一下

cat

这里面的话呢

会有save的全局配置信息

对不对

比如说他的host的主机地址

然后他的一个网络的网段

在这里呢

他就通过这些信息进行一个连接

那么读取完配置之后呢

他会将这个日志呢

也会打印出来

然后呢

会尝试进行一个连接

那如果连接成功之后呢

他就会打印出这样一个提示语

说明呢

是服务是正常的

可以正常揭露进去

如果是出现错误呢

在这里面就会打印出他的一个错误日志

这点的话呢

这个要清楚

就是整个的一个测试流程

好

那么咱们就来

做一个测试验证

回到我们刚才的目录

然后呢

编辑save demo

编辑save client

java这个类

好

编辑save client测试类

在这下面的话呢

我们可以看到

跟我们讲一当中的代码呢

其实都是一样的

对不对

好

那么呢

咱们要把它编译成为class

对不对

通过java cmini进行一个编译

这点我就不做追溯

那编译呢

我们已经生成了save client class这个类

那我们就可以做一个运行

来测试验证一下

首先确保我们集群是正常的

对不对

它是health ok的一个状态

那么运行测试类

看一下它的一个结果

save client

好

这个时候呢

它已经打印出对应的日志

这个打印了三条日志

跟我们在代码当中的话呢

都是一样的

对不对

首先的话呢

是创建集群的一个对象

然后读取它的配置文件

最后的话呢

就是尝试集群的连接

打印出了连接日志信息

好

那整个的话呢

客户端的连接验证都是ok的

说明了我们这个集群能够正常提供服务

那客户端的一个操作使用呢

也是ok

没有问题

好

这个呢

就是客户端的一个连接验证

采用了多少次方式进行了一个操作测试

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 **Ceph 分布式存储系统** 的技术课程，具体聚焦于 **使用 Java 语言（Rados Java 客户端）验证客户端与 Ceph 集群的连接**。讲师通过在 CentOS 7 系统上，演示了如何从 GitHub 克隆 Rados Java 源码、使用 Maven 构建并安装客户端库，以及编写和运行一个简单的 Java 程序来连接并验证 Ceph 集群。整个过程旨在验证客户端环境的正确性，是 Ceph 项目集成开发前的关键步骤。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:03**：视频开始，展示课程大纲，当前章节为“3.7 客户端连接验证(Rados Java)”。
*   **00:00:03 - 00:00:07**：讲师在 Typora 文档中展示本节内容，包括安装 JDK、Git 和 Maven，以及下载 Rados Java 源码的 Git 地址。
*   **00:00:07 - 00:00:12**：切换到 SecureCRT 终端，演示在 `/usr/local/sources/` 目录下执行 `pwd` 命令，确认下载目录。
*   **00:00:12 - 00:00:16**：在终端中执行 `mvn install -Dmaven.test.skip=true` 命令，进行 Maven 构建并安装，生成 `rados-0.6.0-SNAPSHOT.jar`。
*   **00:00:16 - 00:00:20**：展示构建成功后，`target/` 目录下的文件列表。
*   **00:00:20 - 00:00:24**：讲师在 Typora 文档中展示第 5 节“创建JAVA测试类”，并给出 Java 代码的导入语句和类结构。
*   **00:00:24 - 00:00:28**：在 Typora 文档中展示 Java 代码，包括创建 `Rados` 对象、读取配置文件、连接集群等核心逻辑。
*   **00:00:28 - 00:00:32**：在 Typora 文档中展示 Java 代码的 `catch` 块，用于捕获并打印异常信息。
*   **00:00:32 - 00:00:36**：讲师在 Typora 文档中展示第 6 节“运行验证”，并说明需要在 Linux 环境下运行。
*   **00:00:36 - 00:00:40**：在 SecureCRT 终端中，讲师执行 `javac CephClient.java` 编译 Java 文件。
*   **00:00:40 - 00:00:44**：在终端中执行 `java CephClient` 运行程序，成功输出 Ceph 集群的健康状态和数据信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`3.7 客户端连接验证(Rados Java)`
    *   **步骤 1**：安装 JDK、Git 和 Maven。
    *   **步骤 2**：下载 Rados Java 客户端源码，Git 地址为 `https://github.com/ceph/rados-java.git`。
    *   **步骤 3**：执行 Maven 安装，命令为 `mvn install -Dmaven.test.skip=true`。
    *   **步骤 5**：创建 Java 测试类 `CephClient`。
    *   **步骤 6**：运行验证，需在 Linux 环境下运行。

*   **代码内容**：
    *   **Java 代码**：
        ```java
        import com.ceph.rados.Rados;
        import com.ceph.rados.exceptions.*;
        import java.io.File;

        public class CephClient {
            public static void main(String args[]) {
                try {
                    Rados cluster = new Rados("admin");
                    System.out.println("Created cluster handle.");
                    File f = new File("/etc/ceph/ceph.conf");
                    cluster.confReadFile(f);
                    System.out.println("Read the configuration file.");
                    cluster.connect();
                    System.out.println("Connected to the cluster.");
                } catch (RadosException e) {
                    System.out.println(e.getMessage() + ":" + e.getReturnValue());
                }
            }
        }
        ```
    *   **终端命令**：
        *   `git clone https://github.com/ceph/rados-java.git`
        *   `pwd` (显示当前目录)
        *   `mvn install -Dmaven.test.skip=true`
        *   `javac CephClient.java`
        *   `java CephClient`

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与源码下载**
    *   讲师首先在 Typora 文档中展示本节内容，明确目标是验证客户端连接。
    *   接着切换到 SecureCRT 终端，执行 `pwd` 命令，确认工作目录为 `/usr/local/sources/rados-java`，为后续操作做好准备。

*   **场景二：构建与安装客户端库**
    *   讲师在终端中执行 `mvn install -Dmaven.test.skip=true` 命令，演示了 Maven 构建过程。
    *   构建成功后，终端显示 `target/` 目录下生成了 `rados-0.6.0-SNAPSHOT.jar` 文件，证明客户端库已成功安装。

*   **场景三：编写与运行 Java 测试程序**
    *   讲师在 Typora 文档中展示 Java 代码，重点讲解了 `Rados` 对象的创建、配置文件的读取、集群连接等核心步骤。
    *   代码中包含 `try-catch` 块，用于捕获并处理连接过程中可能出现的异常。
    *   讲师在终端中执行 `javac CephClient.java` 编译代码，然后执行 `java CephClient` 运行程序。
    *   程序成功运行后，终端输出了 Ceph 集群的详细信息，包括集群 ID、健康状态（`health: HEALTH_OK`）、服务节点、OSD 状态和数据池信息，验证了客户端与集群连接成功。

---

以上是根据视频画面进行的结构化分析，旨在清晰地呈现课程内容和关键操作步骤。
