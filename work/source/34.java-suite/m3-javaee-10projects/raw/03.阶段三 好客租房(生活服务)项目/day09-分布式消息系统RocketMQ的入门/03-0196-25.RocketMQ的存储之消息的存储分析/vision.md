# 画面线理解：25.RocketMQ的存储之消息的存储分析

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\25.RocketMQ的存储之消息的存储分析【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 02:39, 03:30, 03:35, 03:41, 03:56, 04:25, 04:49, 05:00, 05:16, 05:30, 05:44, 06:01, 06:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:09:30

1) 这一组画面整体在讲 RocketMQ 消息存储的底层结构，包括 CommitLog、ConsumeQueue 的文件组织方式和实际数据内容。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中 RocketMQ 存储章节，说明消息存储采用 mmap + write 方式，文件系统为 Linux Ext4。
画面2：展示架构图，说明 Consumer1 和 Consumer2 从 CommitLog 读取消息，CommitLog 包含 CommitLog Offset、Size、Message Tag Hashcode。
画面3：展示 PDF 文档中目录结构，突出 commitlog 目录下的文件内容，其中 commitlog 文件内容为 000000000000000000。
画面4：终端中显示 RocketMQ 服务的 Docker 容器状态，包括 console 和 server 两个容器。
画面5：终端中执行 docker restart 命令重启 RocketMQ 服务，然后进入 store 目录查看文件。
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
docker ps
COMMAND NAMES CREATED STATUS
dcb74ff401y foxishwho/rocketmq/broker-4.3.2 "bin/sh -c 'cd $..." 17 hours ago Up 17 h
d2b012e2b715 foxishwho/rocketmq/broker-4.3.2 "bin/sh -c 'cd $..." 17 hours ago Up 17 h
ours 0.0.0.0:9876->9876/tcp rmqserver
root@ilcast:conf# docker restart rmqbroker

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
