# 画面线理解：12_高级特性-消息追踪

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\12_高级特性-消息追踪_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:53, 02:24, 03:00, 04:00, 04:41, 05:43, 06:27, 07:06, 09:19, 09:48, 10:40, 11:08, 12:05, 12:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:51:32

1) 这一组画面整体在讲什么（一句话）：
演示 RabbitMQ 的消息追踪功能，包括 Firehose 和 rabbitmq_tracing 两种方式的使用与对比。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 标题页，介绍“1.8 消息追踪-Firehose”，并说明其工作原理和相关命令：rabbitmqctl trace_on 和 rabbitmqctl trace_off。
画面 2: 在 RabbitMQ 管理界面的 Queues 页面，显示了多个队列（如 order_queue, test_trace 等）的状态，其中 test_trace 队列状态为 running。
画面 3: 在 RabbitMQ 管理界面，鼠标悬停在 Queues 标签上，显示当前页面为 Queues 页面。
画面 4: 显示 SecureCRT 终端窗口，连接到 RabbitMQ 服务器，准备执行命令。
画面 5: 在 RabbitMQ 管理界面，点击了 test_trace 队列，进入其详细信息页面，显示了消息图表和状态。
画面 6: 在 RabbitMQ 管理界面，查看 test_trace 队列中 Message 5 的详细信息，显示 Exchange 为 amq.rabbitmq.trace，Routing Key 为 deliver.test_trace。
画面 7: 在 RabbitMQ 管理界面，查看 test_trace 队列中 Message 4 的详细信息，显示 Exchange 为 amq.rabbitmq.trace，Routing Key 为 deliver.test_trace。
画面 8: 在 SecureCRT 终端中执行命令 rabbitmq-plugins list，列出已安装的插件，包括 rabbitmq_tracing。
画面 9: 在 RabbitMQ 管理界面，切换到 Admin 标签页，进入 Traces 页面，显示当前运行的追踪和日志文件。
画面 10: 在 RabbitMQ 管理界面，Traces 页面，鼠标悬停在“Delete”按钮上，准备删除日志文件。
画面 11: 在 RabbitMQ 管理界面，Queues 页面，显示了新增的队列 amq.gen-xVO7bnvQrpXRz_I-TsrnGw，其状态为 Excl。
画面 12: 在 RabbitMQ 管理界面，页面空白，可能为切换或加载状态。
画面 13: 在 RabbitMQ 管理界面，点击了 amq.gen-xVO7bnvQrpXRz_I-TsrnGw 队列，进入其详细信息页面，显示了消息图表和状态。
画面 14: 展示 PPT 标题页，介绍“1.8 消息追踪-rabbitmq_tracing”，并说明其与 Firehose 的区别及启用插件的命令：rabbitmq-plugins enable rabbitmq_tracing。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
rabbitmqctl trace_on: 开启Firehose命令
rabbitmqctl trace_off: 关闭Firehose命令

画面 8:
set [--offline] [--online] <plugin> ...
[root@super rabbitmq]# rabbitmq-plugins list
Configured: e = explicitly enabled, e = implicitly enabled
| Status: # = running on rabbit@super
[ e ] amqp client
[ e ] cowboy
[ e ] cootl
[ e ] rabbitmq auth backend ldap
[ e ] rabbitmq auth mechanism ssl
[ e ] rabbitmq consistent hash exchange
[ e ] rabbitmq event exchange
[ e ] rabbitmq federation
[ e ] rabbitmq federation management
[ e ] rabbitmq ims.topic exchange
[ e ] rabbitmq management
[ e ] rabbitmq management.agent
[ e ] rabbitmq recent history exchange
[ e ] rabbitmq sharding
[ e ] rabbitmq shovel
[ e ] rabbitmq shovel.management
[ e ] rabbitmq top
[ e ] rabbitmq trust store
[ e ] rabbitmq web_dispatch
[ e ] rabbitmq web_stomp
[ e ] rabbitmq web_stomp_examples
[ e ] socks
[ e ] webmachine
[ e ] rabbitmq_tracing

画面 14:
启用插件: rabbitmq-plugins enable rabbitmq_tracing

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1. RabbitMQ 高级特性”，子标题为“1.8 消息追踪-Firehose”，内容说明了 Firehose 的工作原理和相关命令。
画面 14: PPT 标题为“1. RabbitMQ 高级特性”，子标题为“1.8 消息追踪-rabbitmq_tracing”，内容说明了 rabbitmq_tracing 与 Firehose 的区别及启用插件的命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
