# 画面线理解：08_RabbitMQ管控台使用

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\08_RabbitMQ管控台使用_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:43, 01:14, 01:38, 02:39, 02:58, 03:07, 03:23, 03:37, 04:36, 04:57, 05:08, 05:18, 05:41, 05:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:34:45

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 RabbitMQ 管理界面创建虚拟主机并设置用户权限，同时展示在 Linux 命令行中配置和重启 RabbitMQ 服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 进入 RabbitMQ 管理界面的“Connections”页面，显示当前无连接。
画面 2: 切换到“Admin”标签页，显示“Users”页面，列出用户“guest”。
画面 3: 在“Admin”标签页下，点击“Virtual Hosts”选项，进入虚拟主机管理页面。
画面 4: 进入虚拟主机“/itcast”的详情页，提示“无用户有权访问此虚拟主机”，并提供“Set permission”按钮。
画面 5: 在“Set permission”界面，选择用户“guest”，并设置其“Configure vhost”、“Write vhost”和“Read vhost”权限为“.*”，然后点击“Set permission”按钮。
画面 6: 返回“Virtual Hosts”列表页，显示已存在两个虚拟主机：“/”和“/itcast”。
画面 7: 切换到“Overview”页面，显示集群总览信息，包括“Connections: 0”、“Channels: 0”、“Exchanges: 15”、“Queues: 0”、“Consumers: 0”。
画面 8: 在“Overview”页面，鼠标悬停在“Totals”上，准备查看详细统计。
画面 9: 切换到 SecureCRT 命令行界面，显示当前目录为“/usr/share/doc/rabbitmq-server-3.6.5/”，并列出文件。
画面 10: 命令行界面中，用户执行了“cd /usr/share/doc/rabbitmq-server-3.6.5/”命令，进入文档目录。
画面 11: 在 RabbitMQ 管理界面中，显示了多个窗口的分屏视图，包括管理界面、命令行、PPT 文件等。
画面 12: RabbitMQ 管理界面空白，可能为页面刷新或加载中。
画面 13: 在 SecureCRT 命令行界面中，用户执行了“cp ./rabbitmq.config.example /etc/rabbitmq/rabbitmq.config”命令，并执行“service rabbitmq-server restart”命令，重启服务。
画面 14: RabbitMQ 管理界面的“Overview”页面，显示“Last update: 2019-08-11 23:48:00”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 9 和 10:
```
[root@Super rabbitmq-server-3.6.5]# cd /usr/share/doc/rabbitmq-server-3.6.5/11
```
画面 13:
```
# cp ./rabbitmq.config.example /etc/rabbitmq/rabbitmq.config
# service rabbitmq-server restart
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 11: 显示了 PPT 文件“RabbitMQ第一天.ppt”，但未展示具体幻灯片内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
