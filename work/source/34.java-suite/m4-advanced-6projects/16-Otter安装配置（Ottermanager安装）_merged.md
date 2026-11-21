# 16-Otter安装配置（Ottermanager安装） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们继续来看我们alt的安装配置

前面呢

我们是已经完成了依赖环境的安装

包括什么呢

JDK还有Docker对吧

然后呢

还有就是MySQL服务的安装

在这呢

我们一共提供了三个对吧

创建了三个MySQL这个容器

然后呢

分别是作为我们的原数据库

还有目标数据库

还有就是alt它的配置数据库

并且呢

我们安装了Docker还有Area

好那么再往下呢

我们需要安装的是alt它的manager

通过这个alt它的架构呢

大家能看到

这个地方是不是有一个manager

这个manager呢

就是负责什么呢

配置同步规则

设置什么数据源啊

同步源啊等等这些

那么它所对应的呢

其实就是一个安装包

然后呢通过安装包呢

我们把这个服务进程跑起来

好

所以说呢

我们接下来呢

要做的就是需要把这个manager

来进行一个安装

包括下边是不是还有node呀

这个node呢

服务进程呢

也是通过我们去下载

安装包

然后呢

把这个服务进程跑起来

然后呢

这样就有了node

就是负责任务处理的

这个节点

好

首先呢

我们先来看这个manager

咱们来看

要安装它的话呢

首先需要去下载

对吧

需要去下载

其实这个安装包的话呢

我提前都已经下载好了

那么我们可以从这个网址

去进行一个下载

我这提前已经下载好了

咱们可以来看一下

这个地方呢

一共涉及到这么两个安装包

一个是manager

还有一个是node

对吧

这两个呢

都是这种踏点gz的

其实就是压缩包

对吧

那么我提前已经这个下载好

并且放在了我们当前

这个root目录下边

一个是manager

还有一个是node

然后呢

我们把它安装到哪去呢

咱们可以安装到opt

alt这个下边

所以我们先把这个目录呢

来创建一下

在咱们opt下边

创建一个alt目录

然后呢

我们进到这个alt目录里边去

进来

对吧

进来之后呢

咱们把这个

把刚才看到的

这个目录呢

把这两个安装包呢

把它拷到我们当前

这个alt目录下边来

直接使用cp命令

在咱们root下边

对吧

一个是manager

这个安装包

放到当前目录

然后呢

把刚才那个

什么node这个也拷过来

一会儿就会安装它

好

这样的话呢

我们这两个安装包呢

都已经拷过来了

我们当前注意看啊

当前是在这个opt

alt这个目录下边

然后在这个目录下边呢

我们再来创建一个manager目录

我们把这个manager

这个安装包呢

进行解压

然后呢

我们就解压到

咱们这个manager目录里边去

好

接下来呢

我们来解压它

通过他命令来进行解压

好

好

解压完了

解压完之后呢

我们进到manager里边来

咱们来看一下

它这里边呢

解压开了这么

解压出来了四个

这么文件夹

对吧

一个是bit

一看的话

这是不是里边放的

就是我们相应的一些执行命令

对吧

可执行的命令

好

config呢

一般就是放配置文件

还有lib呢

一般呢

就是一些这个

依赖的架包

对吧

还有webapp

一般呢

放的就是一些页面呢

还有gs文件呢

图片呢

等等这些

好

咱们呢

可以先进到这个

bin目录下边来看一下

这里边呢

一共有这么三个命令

对吧

一会儿呢

我们会使用这个

startup这个命令来启动

好

然后推出来

进到什么呢

这个config里边来

这里边呢

我们一会儿需要修改这个文件

就是alter.properties

这个属性文件

好

然后呢

再来看

进到这个lib里边来

好

这里边呢

是它依赖的一些架包

对吧

非常多

好

依赖的一些架包

然后呢

我们再退出来

进到什么呢

webapp下边来

好

这里边呢

其实你看

这就是一个典型的一个web项目

对吧

它的一个目录结构

css

imagines

gs

还有什么

那么templates等等这些

好

这个大概看一下就可以了

然后呢

我们退出来

下一步呢

我们要做的就是什么呢

需要去修改它这个配置文件啊

咱们进到这个config下边

刚才看到有一个alter.properties

对吧

那么我们需要打开它

打开这个alter.properties文件

然后呢

我们来改

具体怎么改呢

注意看

好

进入这个插入模式

这儿呢

我们需要来设置一下

大家来看

这个地方呢

是设置我们这个alter.domain name

对吧

然后呢

这个地方需要设置成什么呢

它的这个IP地址

咱们具体到这儿的话

是不是就是这个399960.254

对吧

所以我们在这儿呢

需要来改一下

改成它的公网IP

对吧

3999

然后是60.254

那么各位同学在下边练习的时候呢

你需要改成你自己的

自己的那个服务器的IP

然后呢

端口号呢

就是8080

这个呢

可以改也可以不改

咱们这儿就不动了

然后再往下呢

你看这块的话

这是不是

是在连接我们这个

MySQL数据库

对吧

提供什么呢

这个驱动名

还有URL

UserName

Password

然后驱动名

就不用改了

然后这儿呢

JDPC

这个地方呢

我们需要来改一下

这个它是要连哪个库呢

其实就是来连我们刚才创建的

这个Auter这个数据库

当然Auter这个数据库呢

也是在这儿

对吧

也是399960.254

跟它其实是在同一台服务器上

那么我们把光标移过来

把这个地方来改造一下

也是这个IP

拿过来就可以了

然后后边呢

我们可以再跟上

这么两个参数啊

跟上这么两个参数

就是什么呢

Auto Reconnect

对吧

是否这个什么呢

自动连接对吧

还有Use SSL

等于False

把这两个参数给它加一下

好

直接右键啊

粘贴到这儿

加这么两个参数

然后再往下呢

是不是UserName

是Root

这也不用改

然后Password的话呢

我们是不是需要改成

我们设置的123456

好

这个地方改造一下就可以了

其他的呢

就不用动了

其他的就不用动了

只要改这几个字呢

就不用动了

这个地方就可以了

好

然后呢

我们改完之后呢

咱们来ESC

冒号WQ

保存退出一下

然后呢

我们就可以来启动了

启动的话呢

我们刚才看到了

在它这个

BinMuru里边

是不是有一个

startup.sh

对吧

那么我们直接使用

这个命令来启动

就可以了

好

startup.sh

好

那么这样就跑起来了

那它到底启动成功

没成功呢

我们可以通过什么呢

查看它这个日志啊

刚才我们

其实就是通过这个命令来启动

然后呢

通过这个tail来查看

它的启动日志

看看启动有没有问题

好

那么从这能看到啊

它说这个什么

the manager server is running now

对吧

并且没有报错啊

说明启动应该是没有问题

然后呢

我们就可以通过

它给我们提供的管理界面

也就是浏览器页面

来打开

咱们在这来输入一下

http

然后呢

这个

IP

地址的话呢

是不是就是我们刚才看到的这个公网IP

399960.254

对吧

这个是3999

应该就是这个

60.254

好

那么如果说我们能够看到这个界面的话呢

这就说明咱们这个服务呢

已经启动正常了

对吧

启动正常

然后呢

我们启动完之后呢

是需要登录的

你看我们当前这个呢

其实是一个匿名用户

说白了就是没有登录

对吧

那么我们需要登录的呢

那么我们需要登录的呢

那么我们需要登录的呢

那么我们需要登录的呢

那么我们需要登录的呢

需要登录

那登录的话

需要使用哪个用户来登录呢

注意看啊

我们当时呢

在初始化他这个数据库的时候

这里边你看

是不是有一个user表

对吧

然后呢

这个表里面其实已经插入了什么呢

这么两条数据

分别是两个用户

对吧

一个是admin

还有一个是guest

然后我们现在呢

是希望使用admin这个用户来登录

账号是admin

密码的话呢

你可以看到啊

他这其实是一个加密的

对吧

他的名文其实也是admin

所以说呢

我们都使用admin啊

用户名密码都是admin

我们现在呢

然后呢

我们来登录一下

怎么登录呢

这个地方是不是有这么一个啊

点击这个按钮

他就会调整到这个登录页面

然后呢

我们在这来输入什么呢

admin对吧

密码的话呢

也是admin啊

然后呢

直接点击登录按钮

好

然后我们把这个密码呢

给他保存一下吧

以后呢

就不用自己再输了

能够看到这些这个界面

对吧

你看现在是admin超级管理员

这就说明了我们登录成功了

那么到这儿的话呢

咱们这个automanager呢

就已经

安装完

对吧

当然了

我们需要一会儿呢

需要在这个管理平台

对吧

在他这个界面上呢

进行一系列化的

一系列的这个配置工作

好

那么到这儿的话呢

我们是完成了这个安装

这个工作

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 **Otter 数据库同步工具** 的安装与配置教程。讲师通过在 Linux 服务器终端中演示，详细讲解了如何下载、解压、配置并启动 Otter Manager 服务。核心内容包括：
- **安装步骤**：使用 `wget` 下载 Otter Manager 和 Node 的部署包，解压并创建目录。
- **配置文件修改**：编辑 `/opt/otter/manager/conf/otter.properties` 文件，配置数据库连接（MySQL）、Zookeeper 地址、服务端口等关键参数。
- **服务启动**：使用 `startup.sh` 脚本启动服务。
- **服务验证**：通过浏览器访问 `http://<主机IP>:8080/`，并使用默认账号密码 `admin/admin` 登录，验证服务是否成功运行。

整个过程旨在为后续的数据库同步任务（如设置同步任务、导入同步服务代码）提供一个稳定运行的 Otter Manager 服务环境。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各帧的时间戳，以下章节按画面内容和逻辑顺序排列：

- **00:00:00 - 00:00:05**：课程标题页，显示“第6章 数据聚合服务开发(pd-aggregation)”及“3.5 Otter manager”。
- **00:00:05 - 00:00:15**：讲解 Otter Manager 的安装步骤，展示 PPT 中的安装命令（`mkdir`, `cd`, `wget`, `tar -zxvf`）。
- **00:00:15 - 00:00:30**：在终端中执行安装命令，演示创建目录、下载文件、解压文件的过程。
- **00:00:30 - 00:00:45**：进入解压后的 `manager` 目录，展示目录结构（`bin`, `conf`, `lib`），并进入 `conf` 目录。
- **00:00:45 - 00:01:00**：展示 `otter.properties` 配置文件内容，重点讲解需要修改的配置项，如 `otter.domain.name`、数据库连接 URL、Zookeeper 地址等。
- **00:01:00 - 00:01:15**：演示修改配置文件，将 `otter.domain.name` 设置为服务器 IP 或域名。
- **00:01:15 - 00:01:30**：演示修改数据库连接参数，如 `otter.database.driver.url`、`otter.database.driver.username` 和 `otter.database.driver.password`。
- **00:01:30 - 00:01:45**：演示修改 Zookeeper 集群地址 `otter.zookeeper.cluster.default`。
- **00:01:45 - 00:02:00**：演示启动 Otter Manager 服务，执行 `./startup.sh` 命令。
- **00:02:00 - 00:02:15**：演示查看服务日志，执行 `tail -500f /opt/otter/manager/logs/manager.log` 命令。
- **00:02:15 - 00:02:30**：演示通过浏览器访问服务，打开 `http://<主机IP>:8080/`。
- **00:02:30 - 00:02:45**：展示 Otter Manager 的登录页面，提示使用默认账号 `admin/admin` 登录。
- **00:02:45 - 00:03:00**：讲师在 PPT 中预告下一节内容“3.5.2 配置”，并展示配置 Zookeeper 和 Node 的相关页面。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容：

- **章节标题**：`3.5 Otter manager`，`3.5.1 安装`，`3.5.2 配置`，`3.5.3 说明`。
- **安装命令**：
  ```bash
  mkdir /opt/otter
  cd /opt/otter
  wget https://github.com/alibaba/otter/releases/download/otter-4.2.18/manager.deployer-4.2.18.tar.gz
  wget https://github.com/alibaba/otter/releases/download/otter-4.2.18/node.deployer-4.2.18.tar.gz
  mkdir manager
  tar -zxvf manager.deployer-4.2.18.tar.gz -C manager
  ```
- **配置文件路径**：`/opt/otter/manager/conf/otter.properties`。
- **配置文件说明**：
  - 主要配置四个方面：服务端口、数据库、Zookeeper、邮箱。
  - `otter.domain.name`：域名或 IP 地址。
  - `otter.database.driver.url`：数据库连接 URL。
  - `otter.zookeeper.cluster.default`：Zookeeper 集群地址。
- **启动命令**：`/opt/otter/manager/bin/startup.sh`。
- **查看日志命令**：`tail -500f /opt/otter/manager/logs/manager.log`。
- **访问地址**：`http://<otter主机IP>:8080/`。
- **默认登录凭证**：用户名 `admin`，密码 `admin`。

#### 代码/配置文件内容：

- **配置文件 `otter.properties` 关键配置项**：
  ```properties
  # otter manager domain name
  otter.domain.name = {更改成服务器ip或域名}

  # otter manager database config
  otter.database.driver.class.name = com.mysql.jdbc.Driver
  otter.database.driver.url = jdbc:mysql://127.0.0.1:3306/otter?
  autoReconnect=true&useSSL=false
  otter.database.driver.username = {更改成你的用户名}
  otter.database.driver.password = {更改成你的密码}

  # otter communication port
  otter.communication.manager.port = 1099

  # otter communication payload size (default is 8388608)
  otter.communication.payload = 8388608

  # otter communication pool size
  otter.communication.pool.size = 10

  # default zookeeper address
  otter.zookeeper.cluster.default = 127.0.0.1:2181
  otter.zookeeper.session.timeout = 60s
  otter.zookeeper.connection.timeout = 30s

  # otter manager address
  otter.manager.address = ${otter.domainName}:${otter.communication.manager.port}

  # should run in product mode
  otter.manager.production.mode = true

  # self-monitor enable or disable
  otter.manager.monitor.self.enable = true
  otter.manager.monitor.self.interval = 170
  otter.manager.monitor.recovery.paused = false
  otter.manager.monitor.email.host = smtp.gmail.com
  ```

---

### 4) 关键场景与演示描述

- **场景一：安装环境准备**（00:00:05 - 00:00:15）
  - 讲师在 PPT 上展示 Otter Manager 的安装步骤，强调需要先创建 `/opt/otter` 目录。
  - 在终端中执行 `mkdir /opt/otter` 命令，创建目录。
  - 使用 `wget` 命令下载 Otter Manager 和 Node 的部署包。
  - 使用 `tar -zxvf` 命令解压文件到 `manager` 目录。

- **场景二：配置文件修改**（00:00:45 - 00:01:30）
  - 讲师在 PPT 上展示 `otter.properties` 文件的配置项。
  - 在终端中使用 `vim` 命令打开配置文件。
  - 重点修改 `otter.domain.name` 为服务器 IP 或域名。
  - 修改数据库连接 URL，将 `127.0.0.1` 替换为实际的 MySQL 服务器地址。
  - 修改数据库用户名和密码。
  - 修改 Zookeeper 集群地址。

- **场景三：服务启动与验证**（00:01:45 - 00:02:45）
  - 讲师在终端中执行 `./startup.sh` 命令启动 Otter Manager 服务。
  - 执行 `tail -500f /opt/otter/manager/logs/manager.log` 命令查看服务日志，确认服务已成功启动。
  - 在浏览器中打开 `http://<主机IP>:8080/`，进入 Otter Manager 的登录页面。
  - 在登录
