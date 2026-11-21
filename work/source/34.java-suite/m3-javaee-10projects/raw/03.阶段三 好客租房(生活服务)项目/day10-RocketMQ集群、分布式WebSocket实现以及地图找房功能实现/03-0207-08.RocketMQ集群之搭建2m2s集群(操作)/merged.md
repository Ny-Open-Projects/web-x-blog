# 08.RocketMQ集群之搭建2m2s集群（操作）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\08.RocketMQ集群之搭建2m2s集群（操作）【海量资源尽在 ubkz.com】.mp4
- 时长 10分33秒（音频 633s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就动手的来操作一下那么首先呢我们先来搭建我们的两个组那么OK那么我们可以看到这个它的两个命令对吧我们把它直接拷贝过来那么我们这样我们还是先拷贝到我们的一个文本文件中检查一下命令有没有问题我们再去做一个拷贝因为从PDF拷贝呢可能会存在一些问题啊
[00:22] 那么我们大致的来看一下应该也没有什么太大的一些这个问题应该没有太大问题好那我们就这个是我们的第一个这个name server那我们来看一下我们第二个这个name server那么这个呢是第二个name server是一样的没有任何问题那么咱们就把它执行一下到这个里面当然了我们需要先把我们现在
[00:46] 所运行的这两个一个是RMQ broker还有一个RMQ name server那么咱们把这个给它先停掉来一个dock什么的stop把它停掉然后把下面这个也停掉那么停止之后我们把那两个命令我们拷贝过来那么等待它的一个停止好现在已经停掉了检查一下Docker ps那么现在显然是不是就没有了对吧
[01:19] OK好那么下面呢我们来做这个操作把它靠过来粘贴走好那么第一个这个Nameserver是不是就已经OK了那么我们来看第二个好那么第二个是不是也创建好了那我们接着继续往下面看那么下面呢我们来创建啊我们的这个Broker那这个是我们的第一个这个Broker依然是拷贝出来这是我们的Broker01啊Broker01
[01:50] 那么在这个里面需要注意的是这个配置文件我们需要先给它创建好所以我们先需要给它创建一个目录下面的这两个目录不需要创建那么它会自动创建但是上面这个不行所以我们需要先创建一个杠P对吧然后创建这样的一个目录然后我们再到这个目录下面再创建这样的一个文件应该是对的然后我们到这然后来一个
[02:21] 创建文件那么我们把下面的文件的内容呢我们也拷贝过来就在这把它拷贝一下然后呢到这粘贴那么基本上大致的看一下应该是没有问题对吧然后呢保存退出OK好那么现在呢这个文件是不是就搞定了对吧这个文件就搞定文件搞定之后呢我们就可以去创建我们的第一个啊这个master第一个这个master这个Docker容器走
[02:51] 好创建成功了那么我们紧接着呢需要去创建后面的几个啊咱们一个一个的来一下啊那么这个呢我们还是需要先把这个命令我们先拷出来这是我们的第二个组把它拷贝一下那么同样的也需要去把这个目录先给它创建出来那么我们还是来操作一下make dir-p然后呢把这个目录创建好然后呢我们再去
[03:23] 编写这样的一个文件那么把它贴过来然后呢把这个具体的配置项的内容拷贝过来然后到这粘贴那么检查一下这个是broker02然后它是10811OK保存退出好嘞那么这个我们第二个是不是也搞定了那么我们就可以去执行我们这个命令了然后到这执行走好那么第二个这个must也搞定了那么我们接下来就要去
[03:53] 玩的呢就是第一个啊这个组的那个sleep他的仇能把这个命令也拷贝过来那么拷贝到哎ok好的我们来看一下那么我们依然呢是把这个目录啊把这个目录给他创建好-c把目录创建好然后呢我们来给他创建这个文件好然后呢我们vim来创建一下这个文件那么依然呢是把这个
[04:24] 把这个文件的内容我们拷贝过来拷贝它然后呢到这拷贝然后呢下面还有那么把这个呢给它贴过来那我们来检查一下这个配置项有没有问题那么它的名字呢叫broke01这个是OK的那么brokeid是要设置为大于0的一个数字然后呢下面这个呢是监听的这个端口没有问题OK搞定
[04:49] 保存退出好那么第三个我们是不是也搞定了那我们把这个容器给它创建出来好那么创建完成那么接下来呢我们就需要创建我们的第四个也就是我们的第二个组的它的一个sleeve那么把这个文件把这个命令我们拷贝出来同样的把这个目录创建好-p
[05:21] 然后我们去把编写这个文件中的一些配置项好那么我们把这个配置项的内容也拷贝过来那么在下面的这个位置把它拷过来好那么他大概来检查一下这个是broke02那个brokeid等于1然后监听的端口是10611他的角色是165这个角色好保存退出
[05:49] 那么现在呢我们就需要再把这个容器呢也给他创建出来是我们这个RMQ这个RMQ block04啊然后呢我们去执行好那么到目前为止呢我们是不是已经就把我们的四个这个block这个容器是不是就创建好了那么接下来呢我们先启动我们的name server启动name server然后呢启动好name server是不是就已经启动ok了那么接下来呢我们把我们的这四个啊这个
[06:19] 四个这个broker给它跑起来走OK跑起来了那么我们接下来就需要对我们这个集群做一个测试看我们这个集群是否是OK的好那么下面我们来测试一下看它是否是OK的那么打开浏览器我们来看一下那么172然后呢下面有一个8082走那么是否可以访问到我们这个UI的管理工具然后呢我们进入我们这个
[06:43] class先切换一下语言找中文我们来看一下这个集群那么点击这个集群其实可以发现我们现在是不是可以我们这个集群是不是有四个这个节点那么它是这个你可以看到这个是block01那么block01它们的之间关系这个是master这个是sleeve然后我们可以看到那么这个是block02
[07:08] 然后呢它的一个这个角色呢这个是01这个是master这个是sleeve那么他们的端口呢是不是刚才我们所这个配置这个端口那OK是不是没有问题啊可以看一下它的一些配置啊状态啊都可以去查看一下这个是它里面的一些这个配置像那么OK好那么这个没有问题那么看一下它的配置配置呢应该也没有什么问题就显示出它的一些内置的一些这种配置啊配置像
[07:38] OK好那么接下来我们来测试一下我们这个集群是否可用呢我们怎么测呢我们是不是可以这样去做一个测试那么我们就用我们这个代码吧去做一个测试那么在前面我们所写这个代码中只要我们能够正常的去发送我们这个数据和接收数据是不是就OK了那我们先来找一下找到我们这个就拿它为例吧
[08:04] 看我们是否能够正常去发送这个消息当然我们现在是不是只连接了一个我们这个name server你可以给他设置多个那么就通过这个封号去做一个分割那么改成9877对吧有两个这样的一个服务好那么我们来走来看一下是否能够去把这个消息发送成功呢等待他的一个执行那么OK现在我们可以看到这个消息他已经发送成功了
[08:32] 那么他所发送的我们的目标的一个Block是Block01那么这个QID是2那我们来看一下在我们这个里面能不能看到那么Block01那么Block01上面其实可以看到在这个位置是不是已经产生了这个消息数对吧产生这个消息数那么我们来看一下这个消息我们来看这个消息那我们来找到我们这个topictopic叫做mytesttopic找到这个mytesttopic来看一下走
[09:01] 是不是已经有一条这个消息了对吧OK他可能是delete那么他可能是delete没有问题那我们来看一下我们的消费者那么消费者是不是也要去去拿这个消息那么这样我们来找一个消费者找一下我们这个消费者消费者他们他的一个topic那就他然后呢我们给topic那这样我们还原吧把它注视掉把这个打开那么我们给他去
[09:32] 订阅新那么就是接收所有的消息然后把这个消息打印出来然后返回的是一个success好然后我们执行走那么我们可以看到在这个位置他是不是也接收到了我们这个消息那么那就说明我们现在整个集群的功能是不是有是ok的那么集群搭建完成那么包括我们刚刚已经测试了功能都是ok的
[09:59] 好嘞那么到目前为止呢我们是不是就已经成功了将我们的RockMQ的一个集群就已经搭建完成了那么并且我们搭建的是一个2M2S这样的一个架构那么如果在我们以后的这个工作过程中啊我们需要搭建一些其他的集群模式比方说有什么呢NMOS
[10:21] 那么这个方式和我们这个搭建2M2S的方式呢基本上是一样的无非就是再多几个节点而已好嘞那么关于我们这个集群的一个搭建我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Docker 搭建 RocketMQ 的多 Broker 集群，并编写 Java 代码进行消息生产和消费测试。

2) 按时间顺序列出每张画面的要点：
画面1：EditPlus 编辑器打开，空白，准备编写或查看配置文件。
画面2：远程终端连接到服务器 172.16.55.185，准备执行命令。
画面3：在终端中执行 Docker create 命令，创建名为 rmqserver01 的容器，配置了端口映射、环境变量和挂载目录。
画面4：EditPlus 中显示了创建 rmqserver01 和 rmqserver02 容器的完整 Docker 命令。
画面5：终端界面空白，准备执行下一步命令。
画面6：EditPlus 中高亮显示了创建 rmqbroker02 容器的 Docker 命令，用于配置 broker。
画面7：终端中显示了 RocketMQ 集群的配置信息，包括 brokerId、namesrvAddr、deleteWhen 等参数。
画面8：EditPlus 中高亮显示了创建 rmqbroker03 容器的 Docker 命令。
画面9：终端中执行了创建 rmqbroker03 容器的命令，并创建了配置文件目录。
画面10：浏览器打开 Google 搜索页，可能用于查找资料或准备下一步操作。
画面11：RocketMQ 控制台页面，显示了 broker01 的配置信息，包括 maxHashSlotNum、transactionTimeOut 等参数。
画面12：IntelliJ IDEA 中显示了 Java 代码，用于创建生产者并发送消息到 topic "my-test-topic"。
画面13：IntelliJ IDEA 中显示了 Java 代码，用于创建消费者并接收消息。
画面14：Adobe Reader 中显示了 PDF 文档，标题为“2.2、搭建2m2s集群”，并展示了创建 2m2s 集群的 Docker 命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
Docker create -p 9876:9876 --name rmqserver01 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/mq/rmqserver01/logs:/opt/logs \
-v /haoke/mq/rmqserver01/store:/opt/store \
foxiswho/RocketMQ:server-4.3.2

画面4：
Docker create -p 9877:9876 --name rmqserver02 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/mq/rmqserver02/logs:/opt/logs \
-v /haoke/mq/rmqserver02/store:/opt/store \
foxiswho/RocketMQ:server-4.3.2

Docker create --net host --name rmqbroker01 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/mq/rmqbroker01/conf/broker.conf:/etc/RocketMQ/broker.conf \
-v /haoke/mq/rmqbroker01/logs:/opt/logs \
-v /haoke/mq/rmqbroker01/store:/opt/store \
foxiswho/RocketMQ:broker-4.3.2

画面6：
Docker create --net host --name rmqbroker02 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/mq/rmqbroker02/conf/broker.conf:/etc/RocketMQ/broker.conf \
-v /haoke/mq/rmqbroker02/logs:/opt/logs \
-v /haoke/mq/rmqbroker02/store:/opt/store \
foxiswho/RocketMQ:broker-4.3.2

画面8：
Docker create --net host --name rmqbroker03 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/mq/rmqbroker03/conf/broker.conf:/etc/RocketMQ/broker.conf \
-v /haoke/mq/rmqbroker03/logs:/opt/logs \
-v /haoke/mq/rmqbroker03/store:/opt/store \
foxiswho/RocketMQ:broker-4.3.2

画面12：
DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "haoke");
producer.setNamesrvAddr("172.16.55.185:9876;172.16.55.185:9877");
producer.start();

//发送消息
String msg = "我的第一个消息61!";
Message message = new Message(topic: "my-test-topic", tags: "delete", msg.getBytes(charset: "UTF-8"));
SendResult sendResult = producer.send(message);
System.out.println("消息id：" + sendResult.getMsgId());
System.out.println("消息队列：" + sendResult.getQueueOffset());
System.out.println(sendResult);

画面13：
#创建2m2s集群
Docker create -p 9876:9876 --name rmqserver01 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/mq/rmqserver01/logs:/opt/logs \
-v /haoke/mq/rmqserver01/store:/opt/store \
foxiswho/RocketMQ:server-4.3.2

#nameserver2
Docker create -p 9877:9876 --name rmqserver02 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/mq/rmqserver02/logs:/opt/logs \
-v /haoke/mq/rmqserver02/store:/opt/store \
foxiswho/RocketMQ:server-4.3.2

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：PDF 文档标题为“2.2、搭建2m2s集群”，内容包含创建 2m2s 集群的 Docker 命令。

5) 不要评价画面美观，不要输出与课程无关的内容。

