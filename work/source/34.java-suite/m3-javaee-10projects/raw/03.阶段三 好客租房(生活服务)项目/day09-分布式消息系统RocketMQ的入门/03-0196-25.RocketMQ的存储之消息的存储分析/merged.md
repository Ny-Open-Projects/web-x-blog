# 25.RocketMQ的存储之消息的存储分析

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\25.RocketMQ的存储之消息的存储分析【海量资源尽在 ubkz.com】.mp4
- 时长 6分26秒（音频 386s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对RockMQ的一些存储的机制呢做一些基本的一些了解那么我们知道RockMQ的速度是不是非常快啊速度是非常快那么他是如何去做到这么去既保证了我的消息的可靠性因为他是保存到文件对不对那么又如何做到他的一个这个速度快呢那么其实呢跟他的存储是有很大的一个关系的啊我们做一个简单的一个了解
[00:28] 那么首先它底层的采用的是一种零拷贝的技术这个零拷贝技术就不展开了就省去了两次的一个拷贝那么就导致我们去读取这个操作文件就速度比较快那么它文件系统采用的是Linux上面的一个exe4一个文件系统这个我们也不做一个展开了那么这个两项这个技术大家可以去简单的去了解一下就OK那么我们关键要去看一下它的这个消息的一个存储那么在RockMQ中
[00:58] 这个我们的消极数据保存到磁盘呢我们为了保证它的一个为了保证它的一个性能吧尤其它这个写入的一个性能那么我们知道对于硬盘而言那么往往是读取的这个速度要大于我们写入的速度是不是所以我们需要更好地去保证我们的一个写入的一个速度那么这个时候呢Rock Diamond Q必须要玩的一个玩法呢就是
[01:23] 我要保证我的一个顺序的写入因为我们那个硬盘那么如果你是去一个顺序的写入要比隐私一个随机的写入效率要高很多很多所以说他要保证是一个顺序的写入再让他再插一嘴就是有很多同学就会认为说我保存我只要我的数据我一旦保存到我的硬盘那我速度就肯定比较慢那保存到内存就比较快其实这种说法有点太
[01:53] 绝对啊太绝对那么往往如果说我们能够保证你是顺序写入到我硬盘的话其实他的写入速度也是非常可观的啊OK那么在我们的底层呢这个log的MQ呢他的存储呢是由两块来完成的啊一个叫做consumer queue一个叫做committer log这两个文件去配合完成的那么其中呢这个committer log呢是我们真正存储我们的数据的一个文件而这个
[02:20] consumer的一个consumer的一个Q的话它是一个索引的文件它用于去指向到哪些数据存储到我们的这个物理文件的位置就是说在这个里面它存的是索引它是指向到这个文件中的一个位置好那么我们接着继续往下面看那么下面我们来看一下这个图这个图在这个图上面我们可以看到这是我们的生产者
[02:45] 他能去提交我们这个数据提交我们数据到我们的一个对列到我们对列那么到我们对列之后在底层的存储他其实是要存储到我们一个文件叫做commit log的一个文件中存到这个里面来
[03:01] 那么在这个里面来到我们的一些用户这是我们的用户Consumer那么Consumer呢想要去读取我们的这个文件中的一些这个数据就是我们的消息的数据那么他就需要先通过我们的一个这个索引文件通过索引文件去查找到我们的一些这个文件这个消息数据所在的一个位置然后呢再去我们这个Commit Log中再去查找我们这个数据去他是这样的一个过程
[03:30] 那么我们其实可以可以在我们的这个他的存储中找到这两个文件啊那我们来找一下那么我们进入到cd点点回去然后呢来看一下在这个store存储中那么我们可以看到在这个位置是不是有一个叫commit log那么commit log呢其实就是读了叫做commit log那么这个里面呢我们可以看到啊他呢是他
[04:02] 这个呢,0000这个就是一个文件啊就这个文件我们可以打开来看一下啊那么这个里面保存的是二进制的一些内容那么打开呢我们可能会看到是一些这种像乱码的一些东西啊其实它并不是一些乱码哎里面没有内容吗没有内容不是没有内容可能是会比较慢啊我们来大概大概我们来浏览一下这里面的内容啊那么这个里面内容呢其实我们有一些应该能够去认识吧比如说
[04:32] 这个Hello Rocket MQ1这个是不是我们之前所发送的一个这个消息啊比如说我们还有一些其他消息比如说像我们发送这个这个topic test对吧OK然后呢还有一些其他内容吗有没有大概能够认识的一些内容啊OK那么基本上呢我们可以啊
[04:53] 可以有一个认知呢就是我们这个里面所存储的就是我们的消息的数据对不对啊那么我们再继续回去在这个下面呢还有个叫做consumer consumer queue这样的一个文件那么在这个里面呢就是按照我们的这个topic去做一个这个目录啊去做一个存储比如说我们进入有个叫做pay topic然后呢这个里面的又去划分一些这个文件比如说进入这个里面来
[05:21] 那么这个文件代表什么呢其实就代表我们几个这个对列啊几个对列那么前面我们是不是说过你看这个就是往上面看啊那么这个呢是我们的一个主题对吧那么主题下面是不是有对列那么可以看到在这个位置是不是对应的有墨渊是不是有四个对列啊然后呢我们进入到这个0这个目录在这个0这个目录下面呢又会有这样的一个000这样的一个文件那我们打开这个文件可以来看一下
[05:50] 在这个里面我们看见他的一些这个内容他所存储的其实就是我们的一些这个索引的一些数据啊由于是他是二进制的一些内容所以我们看不到啊看不出来里面一些内容啊那么这个所存储的是一个二进制的一些数据那么就是说当我们去读取消息的时候呢先要通过他
[06:09] 去查找到我们这个消息所在的一个位置然后呢再去到我们的这个commit这个log中的文件再去查找一个数据它是这样的一个逻辑OK那么大家呢对它有一个这样的一个基本的一个认知就可以了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 RocketMQ 消息存储的底层结构，包括 CommitLog、ConsumeQueue 的文件组织方式和实际数据内容。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中 RocketMQ 存储章节，说明消息存储采用 mmap + write 方式，文件系统为 Linux Ext4。
画面2：展示架构图，说明 Consumer1 和 Consumer2 从 CommitLog 读取消息，CommitLog 包含 CommitLog Offset、Size、Message Tag Hashcode。
画面3：展示 PDF 文档中目录结构，突出 commitlog 目录下的文件内容，其中 commitlog 文件内容为 000000000000000000。
画面4：终端中显示 RocketMQ 服务的 Docker 容器状态，包括 console 和 server 两个容器。
画面5：终端中执行 Docker restart 命令重启 RocketMQ 服务，然后进入 store 目录查看文件。
画面6：终端中显示 RocketMQ 消息消费日志，包含 TopicTest 和消息内容。
画面7：终端中显示 RocketMQ 消息消费日志，包含 TopicTest 和消息内容。
画面8：终端中进入 commitlog 目录，查看 commitlog 文件内容。
画面9：终端中进入 consumequeue 目录，查看 topics 目录下的子目录。
画面10：终端中进入 pay_topic 目录，查看其下文件。
画面11：终端中在 pay_topic 目录下执行命令时出现语法错误。
画面12：终端中在 pay_topic 目录下执行命令时出现语法错误。
画面13：展示 PDF 文档中目录结构，突出 consumequeue 目录下的 testCreateTopic3 文件内容。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面3：
commitlog
000000000000000000

画面4：
Docker ps
COMMAND NAMES CREATED STATUS
dcb74ff401y foxishwho/RocketMQ/broker-4.3.2 "bin/sh -c 'cd $..." 17 hours ago Up 17 h
d2b012e2b715 foxishwho/RocketMQ/broker-4.3.2 "bin/sh -c 'cd $..." 17 hours ago Up 17 h
ours 0.0.0.0:9876->9876/tcp rmqserver
root@ilcast:conf# Docker restart rmqbroker

画面5：
root@ilcast:conf# cd store/
root@ilcast:store# ll
total 32
drwxr-xr-x 5 root root 4096 Dec 18 23:57 .
drwxr-xr-x 6 root root 4096 Dec 18 23:57 ..
drwxr-xr-x 5 root root 4096 Dec 18 23:57 abort
drwxr-xr-x 2 root root 4096 Dec 18 23:57 checkpoint
drwxr-xr-x 2 root root 4096 Dec 18 23:57 commitlog/
drwxr-xr-x 10 root root 4096 Dec 18 23:57 config/
drwxr-xr-x 3 root root 4096 Dec 18 23:57 consumequeue/
drwxr-xr-x 4 root root 4096 Dec 18 23:57 index/
drwxr-xr-x 4 root root 4096 Dec 18 23:57 lock
root@ilcast:store# cd commitlog/

画面8：
root@ilcast:commitlog# ll
total 104856
drwxr-xr-x 2 root root 4096 Dec 18 23:57 .
drwxr-xr-x 6 root root 4096 Dec 18 23:57 ..
-rw-r--r-- 2 root root 1073741824 Dec 18 21:42 00000000000000000000000000000000
root@ilcast:commitlog# cd ..

画面9：
root@ilcast:consumequeue# ll
total 40
drwxr-xr-x 7 root root 4096 Dec 18 23:57 .
drwxr-xr-x 6 root root 4096 Dec 18 23:57 ..
drwxr-xr-x 10 root root 4096 Dec 18 23:57 haoko_order_topic/
drwxr-xr-x 5 root root 4096 Dec 18 23:57 my.topic-filter/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic/
drwxr-xr-x 7 root root 4096 Dec 18 23:57 my.topic-2/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-3/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-4/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-5/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-6/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-7/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-8/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-9/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-10/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-11/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-12/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-13/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-14/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-15/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-16/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-17/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-18/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-19/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-20/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-21/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-22/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-23/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-24/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-25/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-26/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-27/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-28/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-29/
drwxr-xr-x 6 root root 4096 Dec 18 23:57 my.topic-30/

