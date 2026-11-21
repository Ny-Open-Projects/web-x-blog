# 09.容器停止与启动和目录挂载

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\09.容器停止与启动和目录挂载_【海量资源尽在 666java.com】.mp4
- 时长 6分11秒（音频 371s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢给大家讲解了啊是创建容器和查看容器那么我们说创建的容器启动起来怎么去停掉呢啊那这时候呢我们给大家讲解两个命的一个是启动啊一个是停止一个是启动啊啊首先我们来看一下这个停止啊那么停止就是死到啊这个很容易记那么启动就是死大啊就这么简单那么咱们给大家演示一下
[00:30] 首先我们通过Docker ps-a来查看一下当前我们所有的容器那么当前的有一个容器是运行的有一个容器是停止的运行的是mycentos2那么停止的是mycentos那首先我们来看一下停止容器停止容器的话我们将这个mycentos2给它停掉叫Docker stop然后是mycentos2就是我们容器的名称
[01:00] 当然你这里头也可以什么呢可以去指定我们的容器ID也是可以的这两种讯号都可以我们现在将它停掉那么停止的这个时间比启动要稍微的慢一点要稍微慢一点好我们看一下好我们看一下现在已经停掉了停了之后我们现在可以用Docker ps-a来查看一下
[01:31] 刚才的这个容器呢买4.2就已经停掉了啊就已经停掉了那么停掉的容器我们怎么再把它启动起来呢啊那这时候我们就用这个Docker start然后呢是我们的容器id或者是容器的名称这都可以啊那么我们现在来回车好我们看一下现在启动起来了那么启动起来之后我们再通过Docker ps-a来查看一下啊这个容器呢
[02:01] 又被启动起来了好这就是容器的停止与启动那么容器的停止与启动之后呢我们接下来再看一下下面这个命令啊下面这个命令呢叫文件拷贝啊那么这个文件拷贝呢这个命令也很长什么时候会用它呢我们通常呢会说到把某些文件或者目录拷到容器里对吧你比如说你像容器里要安装一个什么软件对吧
[02:33] 你肯定是要把东西要烤上去那么还有一种情况就是要把容器里的东西再烤出来那么这个烤背呢这个命令也好记叫什么叫CP那么前面这个部分呢你要指定你要烤背的是什么那么后面那部分呢你要指定的目标第一个是圆第二个就是目标那么我们看一下怎么去把这个文件烤到容器里咱们给大家演示一下我们还是用mysendos2给大家演示
[03:03] 那么我们首先看一下这个当前有什么文件啊咱们就就地取材啊当前目录呢正好有这么一个文件是吧你别管这文件是什么对吧那你就去把这文件考进去咱们咱们来做一个测试啊叫Docker什么呢CP然后呢你这里的文件这时候我要指定这个名称吧指定这个名称空格然后接下来什么你的目标是什么目标是考到买Centrum S2上好那你这里就指定买
[03:33] centosr接下来我们这里有冒号容器名称后面是冒号当然这个容器名称你也可以用容器ID这两个都是可以通用的有容器名称后边加上一个什么叫什么uusrusr local他肯定会有这么一个目录对吧那好了我就将这个文件本机的速度机的这个文件当前目录这个文件
[04:08] 考到我们的容器这个买新的s2这个容器的user的local目向回车这时候呢我们看一下啊他现在已经执行完了没有报错呢就是成功了对吧没有报错就成功了那么怎么来验证他这个东西考进去了呢你肯定是要进去对吧啊所以说我们在进入的容器用什么esit然后杠什么啊这个啊叫指定什么叫杠it啊
[04:37] -it然后呢指定这个名称mycentosr-b-bash好进去之后呢我们现在呢啊就先进到这个目录里啊usr老考对吧进到这个目录之后呢我们我们来DR一下我们会发现啊这个文件是不是就考进来了啊这个文件就考了这个文件呢就是我们从速度机拷贝过来的啊好我们esit退出来啊
[05:10] 退出来之后呢我们说这个文件拷贝啊就给他拷出来了拷进去了啊那么拷进之后呢你怎么可得拷出来呢这时候你就不写写成反的就行了啊cp那么你要拷什么拷就是还是刚才这个文件啊就是指定买send sr这个容器我要把这个容器的东西拷出来怎么办咱们还是拷刚才那个文件啊因为这个刚才文件呢呃就在这个公路下对吧所以这个文件肯定是存在的
[05:40] 你把它考出来当前目录本身就有这么一个文件对吧那所以说我可不可以给它改个名呢是吧我可以指定我考出来之后叫什么名那我给它改个二是吧好回车这时候呢我们再看一下啊当前目录是不是就有这个就有这个文件了是吧那就考上了好关于我们这个文件的这个拷贝啊咱们就给大家讲解到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 命令管理容器，包括启动、停止、查看状态以及文件拷贝操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在终端中执行 `Docker exec -it mycentos2 /bin/bash` 进入容器，随后执行 `exit` 退出容器，并使用 `Docker ps` 查看容器状态，显示容器名为 mycentos2，状态为 Up。
画面2：执行 `Docker ps -a` 查看所有容器，显示 mycentos2 状态为 Up，另一个容器 mycentos 状态为 Exited (0)。随后执行 `Docker stop 74294a69b021` 停止容器。
画面3：执行 `Docker ps -a` 查看所有容器，显示 mycentos2 状态为 Exited (137)，mycentos 状态为 Exited (0)。随后执行 `Docker start 74294a69b021` 启动容器。
画面4：执行 `Docker ps` 查看容器，显示 mycentos2 状态为 Up。随后执行 `Docker ps -a` 查看所有容器，显示 mycentos2 状态为 Up，mycentos 状态为 Exited (0)。
画面5：显示 Typora 文档中关于“文件拷贝”的内容，包含命令 `Docker cp` 的用法示例。
画面6：执行 `Docker ps` 查看容器，显示 mycentos2 状态为 Up。随后执行 `Docker ps -a` 查看所有容器，显示 mycentos2 状态为 Up，mycentos 状态为 Exited (0)。
画面7：执行 `Docker cp anacoda-ks.cfg mycentos2:/usr/local` 将文件拷贝到容器内，随后执行 `cd /usr/local` 进入目录。
画面8：执行 `Docker ps -a` 查看所有容器，显示 mycentos2 状态为 Exited (137)，mycentos 状态为 Exited (0)。随后执行 `Docker start 74294a69b021` 启动容器。
画面9：执行 `cd /usr/local` 进入目录，显示目录内容。
画面10：执行 `Docker exec -it mycentos2 /bin/bash` 进入容器，随后执行 `cd /usr/local` 进入目录。
画面11：执行 `Docker exec -it mycentos2 /bin/bash` 进入容器，随后执行 `cd /usr/local` 进入目录。
画面12：执行 `Docker exec -it mycentos2 /bin/bash` 进入容器，随后执行 `cd /usr/local` 进入目录。
画面13：执行 `Docker cp anacoda-ks.cfg mycentos2:/usr/local` 将文件拷贝到容器内，随后执行 `cd /usr/local` 进入目录。
画面14：显示 Typora 文档中关于“停止与启动容器”的内容，包含命令 `Docker stop` 和 `Docker start` 的用法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
[root@localhost ~]# Docker exec -it mycentos2 /bin/bash
[root@localhost ~]# exit
[root@localhost ~]# Docker ps
```
画面2：
```bash
[root@localhost ~]# Docker ps -a
[root@localhost ~]# Docker stop 74294a69b021
```
画面3：
```bash
[root@localhost ~]# Docker ps -a
[root@localhost ~]# Docker start 74294a69b021
```
画面4：
```bash
[root@localhost ~]# Docker ps
[root@localhost ~]# Docker ps -a
```
画面5：
```bash
Docker cp 源文件路径 目标容器:容器目录
Docker cp 容器名称:容器目录 源文件路径
```
画面6：
```bash
[root@localhost ~]# Docker ps
[root@localhost ~]# Docker ps -a
```
画面7：
```bash
[root@localhost ~]# Docker cp anacoda-ks.cfg mycentos2:/usr/local
[root@localhost ~]# cd /usr/local
```
画面8：
```bash
[root@localhost ~]# Docker ps -a
[root@localhost ~]# Docker start 74294a69b021
```
画面9：
```bash
[root@localhost ~]# cd /usr/local
```
画面10：
```bash
[root@localhost ~]# Docker exec -it mycentos2 /bin/bash
[root@localhost ~]# cd /usr/local
```
画面11：
```bash
[root@localhost ~]# Docker exec -it mycentos2 /bin/bash
[root@localhost ~]# cd /usr/local
```
画面12：
```bash
[root@localhost ~]# Docker exec -it mycentos2 /bin/bash
[root@localhost ~]# cd /usr/local
```
画面13：
```bash
[root@localhost ~]# Docker cp anacoda-ks.cfg mycentos2:/usr/local
[root@localhost ~]# cd /usr/local
```
画面14：
```bash
Docker stop 容器名称(或容器ID)
Docker start 容器名称(或容器ID)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：PPT标题为“3.2.4 文件拷贝”，内容包括命令 `Docker cp` 的用法示例。
画面14：PPT标题为“3.2.3 停止与启动容器”，内容包括命令 `Docker stop` 和 `Docker start` 的用法。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

