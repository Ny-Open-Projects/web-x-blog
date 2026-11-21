# 3.RocketMQ研究-Rocket基础-组成结构

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\3.RocketMQ研究-Rocket基础-组成结构【海量资源尽在 666java.com】.mp4
- 时长 4分20秒（音频 260s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来开始学习RocketMQ的基础知识在本次课程当中我们主要是学习RocketMQ的一些比较常用的基础的知识来用于项目的开发首先我们先简单理解一下RocketMQ的组成结构那么这个结构我们先简单粗略的理解一下因为后边我们还会详细的去讲里边的组成结构
[00:24] 理解了这个组成结构呢方便我们去安装rocket amicro以及快速入门程序的编写好那么我们来看啊它总共包括几块各位你告诉我告诉我三块那明显是四个框嘛四个框嘛有时候好多块是吧这里面注意你看上面的标题最左边的是一个叫producercluster那这个呢就是生产者对吧那最右边是一个consumercluster这个是消费者
[00:54] 其实有同学原来学过生产者消费者模式对吧没错那这个消费对联就是基于生产者消费者模式那具体是怎么样生产怎么消费呢来我们往后看首先我们先看一下整个图形它的组成都有哪些然后再看它的一个交互过程生产者呢他负责发消息消费者呢负责接收消息大家理解吧还有Name ServerBroker
[01:23] 看见吗这个内部server是什么呢咱先不管它咱先说brokerbroker就是我们说的消息队列就是咱们刚才说吧说A把消息发到消息队列B从消息队列去接收对吧那么这个消息队列在哪呢就在broker这broker是不是就是A和B他们之间的一个中介没错吧那现在问题来了
[01:52] 这个A如何把消息发到消息队列呢有时候老师那就那就发呗那就发关键是他知道地址吗这个A知道消息队列的地址吗你看他是一个cluster对不对也就是说他有很多节点组成了这么一个集群对不对那这时候呢这个时候A如果要发消息他需要先从name server当中去获取broker的地址获取什么地址因为他有很多节点对吧
[02:22] 他也有很多的消息队列那我具体向哪个节点然后呢向哪个队列发消息这个时候需要先从name server去获取去获取最终要发消息的这个消息队列的这个地址好所以说name server它的作用是什么呢就是来搜集到底有多少broker来提供服务大家理解了吧所以
[02:50] 我们说Name Server呢其实就相当于我们微服务开发当中的注册中心所有Broker的地址包括消息对列的这个情况都在Name Server当中纯属的有那A呢如果想发消息先从Name Server当中去找一个能发消息的消息对列那么B呢就是这个消费者呢他要监听对列那他也是要从Name Server当中找到自己监听的对列一旦有消息他就把消息拿到
[03:19] 懂了吧这就是我们说的四块他们的一个职责那么如果知道了职责的情况下你现在再看流程就比较简单了就是这个broker呢我们刚才说了吧broker要向消息队队发对吧他首先从内部server拿到消息队的地址然后呢向broker发对吧那么各位你看这儿是有一个叫发现broker那这个应该是第一步对吧这个应该是第二步是不是要向broker发消息了对吧那现在呢监听消息的消费者
[03:49] 他是不是也要从这个内部Cyber当中来发现他要去监听的这个消息队列一旦监听到这个消息队列有消息那各位我问你他是不是就可以把消息拿到对这就是我们说的整个的交互过程对所以这就是我们说的Rocket MQ的一个基本组成结构我们先粗略的去理解一下先粗略几点后边呢我们还会详细讲这个组成结构好那个组成结构呢咱们先
[04:18] 讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 RocketMQ 的组成结构，包括 Producer Cluster、NameServer Cluster、Broker Cluster 和 Consumer Cluster 之间的交互流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 RocketMQ 组成结构图，包含 Producer Cluster、NameServer Cluster、Broker Cluster 和 Consumer Cluster，以及交互过程的四个步骤。
画面 2: 鼠标光标在“Producer”节点上，强调生产者集群。
画面 3: 鼠标光标在“Consumer”节点上，强调消费者集群。
画面 4: 鼠标光标在“Broker Cluster”节点上，强调消息中间件集群。
画面 5: 鼠标光标在“Producer Cluster”节点上，强调生产者集群。
画面 6: 鼠标光标在“NameServer Cluster”节点上，强调命名服务集群。
画面 7: 在图上方手写标注“A → [] → R”，表示消息从生产者到消费者经过中间件。
画面 8: 鼠标光标在“Broker Cluster”节点上，强调消息中间件集群。
画面 9: 鼠标光标在“NameServer Cluster”节点上，强调命名服务集群。
画面 10: 鼠标光标在“Consumer Cluster”节点上，强调消费者集群。
画面 11: 鼠标光标在“Broker Cluster”节点上，强调消息中间件集群。
画面 12: 鼠标光标在“Broker Cluster”节点上，强调消息中间件集群。
画面 13: 鼠标光标在“Consumer Cluster”节点上，强调消费者集群。
画面 14: 鼠标光标在“Consumer Cluster”节点上，强调消费者集群。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
PPT 标题：2.1 组成结构
架构图结构：
- Producer Cluster → NameServer Cluster（通过“发现Broker”连接）
- Producer Cluster → Broker Cluster（通过“发送消息”连接）
- NameServer Cluster → Broker Cluster（通过“通信”连接）
- Broker Cluster → Consumer Cluster（通过“推送消息”连接）
交互过程：
1) Broker 定时发送自身状态 到 NameServer。
2) Producer 请求 NameServer 获取 Broker 的地址。
3) Producer 将消息发送到 Broker 中的消息队列。
4) Consumer 订阅 Broker 中的消息队列，通过拉取消息，或由 Broker 将消息推送至 Consumer。
集群角色：
1) Producer Cluster 消息生产者群
   - 负责发送消息，一般由业务系统负责产生消息。
2) Consumer Cluster 消息群
   - 负责消费消息，一般是后台系统负责异步消费。
   - 两种消费模式：

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

