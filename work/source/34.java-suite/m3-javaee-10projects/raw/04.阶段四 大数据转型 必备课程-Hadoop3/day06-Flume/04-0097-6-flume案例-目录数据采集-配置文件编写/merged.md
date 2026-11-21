# 6-flume案例-目录数据采集-配置文件编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\6-flume案例-目录数据采集-配置文件编写【海量资源尽在 ubkz.com】.mp4
- 时长 21分28秒（音频 1288s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那接下来呢我们就按照这个步骤呢来去进行配置OK第一步呢我们需要写一个配置文件那这个配置文件呢我们比如说呢叫什么呢三刊讲义叫一个叫叫sport dr.confOK这么一个文件好在这个文件中呢我们需要做四个配置第一需要配置三个组件的名字咱们一个一个来OK那呢咱们把第一步呢
[00:30] 把每一步分别拿出来好这是第一步我放在这个位置三个组件的名字这个时候我们拿过来来看一下这段配置把它截个图好来放在这个位置好这三个大家不陌生了对吧这个地方A1.sauce它的名字叫REA1是ogint的名字这个名字当我们在启动这个flume实例的时候我们就可以自己命名而sync
[01:06] 叫KE而channel呢叫CEOK这是它的三个名字好这是它三个名字那接下来呢我们来看第二个配置source看第二个配置source那么source很重要source其实是数据源就是我数据从哪里来是数据的源头那我们这个source数据从哪里来呢我刚才说过了它是监控某一个目录下面文件的变化
[01:39] 那这个时候呢这个sauce啊它有一个自己的类型是什么类型呢我们来看一下我把这个呢把这个sauce的配置我们来截一下好回到我们的画图放在这个位置把这个像素拿一点好我们来看那首先呢这个地方呢第一个是RE这个sauce它的type是一个spotia对这个spotia是我们
[02:11] 其中的一个source类型这个名字不能随便写它表示的是呢我就是来监控目录下文件变化才出现的一个source也就是说用它刚好符合我们的要求而且必须写它这是第一个type没什么好说的这是一个固定的一个source类型那接下来我们来看第二个你说你监控一个目录下文件的变化那你是不是得告诉我监控哪一个目录啊所以在第二个呢它是
[02:40] 告诉我们监控目录它的一个路径我在Xpod Service下面点File我要监控这个目录好第三个是是否要加文件的头部信息这个你写处就行了好这是一个固定参数好第二步我们就做完了我们配置好Source了那接下来我们再配置Channel我们第三步也拿过来好第三步那这样我直接把它放在这个位置
[03:15] 稍等再复制一下来我来开配置这个channel打开我们的讲义在这里我们把channel的东西呢拿过来好这是我们的channel好回到我们的画图在这里呢我们来看一下这个channelsource后面是一个通道我们要临时存数据的地方channel那这个channel的第一个type我们数据存在哪里呢我们数据还是存在内存里面memory而这个里边有个
[03:53] capacity这个capacity呢咱们上次提到过一次没有重点给大家说今天我给大家说一下什么叫capacity呢capacity是容量的意思也就是说我们这个channel呢它其实是有容量的那这个容量呢相当于我这个channel中能存多少数据能存多少数据而这个数据的话呢它这个地方呢后面写个1000这个1000呢
[04:21] 表示是1000个event我们刚才说过了我们channel中存数据呢它呢它有个单位单位是event来看我上次画的图这个event呢其实代表每一条数据这个event有两部分一个是hide头部一个是body它的一个正文OK也就是说我这里边我这个channel中最多能存多少数据呢最多能存1000个event啊event那么如果你不理解你可以理解成
[04:51] 一行数据它其实就是一文档比如说我要截取文件文件的一行你可以默认其实就是一个一文档OK 这是capacity的作用我这样我把这个我把这个里边呢把这个channel单独拿下来我们来标一下好吧把这个channel拿下来拿下来之后呢拿下来拿在这个位置我把这个channel专门拿在这里给大家讲清楚这个capacity就是这个channel
[05:24] 它的一个总容量OK那么这个1000个event它最多能存这么多那后面还有个translocationcapacity这是100这是怎么回事呢是这样的你看这是我们的channel这是我们的channel而在channel之前呢它是跟着sauce的sauce的数据呢给它而在channel之后呢它是一个什么呀它是一个sync对吧我们数据要下沉到哪里这是一个sync
[06:01] 好S&K SYNC好那么这个里边呢大家注意我们从channel把数据给SYNC呢其实给的时候不是把这里的数据全部给SYNC而这里边呢有一个对列这里边有一个对列这个对列呢就相当于啊你这里边呢你这个这个channel中有很多的event我用这个椭圆形来表示一个一个的event来我们看一下好这是event
[06:31] 这是event都是有好多event而假如说你有很多event那我一次性要给sync传送多少event呢那这个地方呢有个对列这个对列中呢也可以放一些event这个对列呢表示一次性给sync多少数据而这个对列的大小呢其实就是translocation capacity是这个是这个translocation capacity这样我来标一下它是说的是它的大小那也就是说
[07:02] capacity是整个channel的大小而translocation capacity呢是我一次性向sync传送多少数据的一个大小很明显它俩的关系是capacity肯定要比translocation capacity大一点这个translocation capacity呢你设的合适它呢会提高向sync传送数据的一个效率OK这是它俩的关系我给大家讲清楚了它们的单位都是event好了这是一个channel的一个配置
[07:31] 那咱接下来呢再说这个sync我们来看第四步我们要配置sync好这个sync呢表示我的数据要去往哪里那我现在问大家我们从目录中采集的数据最后要去往哪里呢我们刚才说的非常清楚我们要把这个数据存到HDFS也就是我们的分布式文件系统那所以说呢我们的sync的目的地也是HDFS那来看我们怎么配
[08:02] 好在这里呢我们来看SyncSync在这个位置你看Sync的配置非常非常多这里呢我把它全部把它够复制过来来我们来看一下好打开站在这里它的配置呢非常多好非常多也没有关系我们可以来简单看一下来看一下首先呢第一个是它的一个Type这个Type呢
[08:33] 是表示我们sync的类型是HDFS而这个地方呢这个地方其实应该可以不用这个表示我们sync对应的是哪个channel那我们用的是CE这个channel这句话其实可以在我说的第五步把它们组合在一起的时候这个地方来写这句话OK那你就先记着它的channel是是这个CE那接下来问题是我要把这个采集后的数据呢我要放到HDFS上
[09:02] 那么HDFS上它的路径是哪里呢我要把数据放在HDFS的哪个路径由这个参数来指定你看我要把采集后的数据呢放在HDFS node01这个节点这是我们的name node所在的节点OK然后呢8020在这个根目录下面有一个叫spodia这个目录下面有个files这个文件文件夹然后呢下面呢又有一个文件夹
[09:31] 这个叫%y%m%d是这样的它会自动获取呢年月日以这个年月日呢为文件夹的一个命名方式OK这里会产生一个新的文件夹后面呢又一个文件夹叫%h%m%这个h呢表示hour分这个小时m的minute表示分钟也就是它会在我们的这个HDF呢产生这么多级目录而且后面这呢这两个目录呢会随时发生变化
[10:00] OK就会把数据呢放在这里边来好那这是一个路径问题接下来还有个叫fail prefix这个是文件的前缀就是在切分之后呢这个文件呢都是events 什么什么开头这是一个前缀那接下来呢还有这些东西你看从这个前缀开始呢我把这个呢像图向下拉一下好你想想看从这个地方开始来我来标一下
[10:29] 从这个run的开始一直到一直到这个位置好大家看这个地方啊从这条位置这个地方呢说的是文件的一个滚动什么叫文件的滚动呢你比如说你采集数据你采集了一定量数据之后呢它会在HDFS上产生一些新的文件它不可能把采集后的数据一直放到一个文件它这个文件得更新呢当你数据达到一定量的时候我会产生新的文件
[10:59] 那这个里边呢这些参数就标志啊我什么时候该产生一个新的文件好我们来看一下首先呢这个run呢这个呢表示什么意思呢这个run呢表示我文件是否滚动也就是我是否产生新的文件那这是是的处而这个地方呢这个地方呢我来写一下注释吧好在后面我加一个小注释是否是否采用是否使用
[11:32] 文件滚动也就是我在去采集的时候是否需要让这个文件呢产生新的文件就这么简单那我们采用的是这个参数好那接下来呢第二个他说呢你既然你可以让他产生新的文件那这个run的value是什么意思呢这个run的value和run的unit他其实他俩合在一起呢他其实描述的是我们这个文件夹的一个生成的一个周期
[12:06] 因为我们在生成文件的时候前面有个文件夹那这些文件夹多久更新一次呢这俩合在一起是我们文件夹的一个生成的一个周期我来标一下是HDFS文件夹的滚动周期也就是说这个unit是单位minute是10分钟每隔10分钟我会产生一个新的文件夹是这意思
[12:39] 而文件夹里边放的才是真正的文件内容而后面这个RuleRule开头的它是文件的一个滚动周期所以说上面是文件夹下面是文件而这些文件呢就是采集后的真实数据我们来看一下这个地方有个RuleInterval这个什么意思呢这个呢表示每隔三秒钟产生的新文件这个时间有点短是不是啊每隔每隔三秒产生一个新文件好每隔三秒
[13:14] 所以这个单位是秒那后面这个还有rule size这个是这个文件大小达到20个字节产生新文件文件大小达到20个字节OK产生新文件那他说每隔三秒这个文件的大小这个达到20个字节这个文件指的是什么意思呢就说20个字节的文件呢其实指的是一个临时文件当他采集的数据呢
[13:47] 把它放到HDFS的时候它其实会在HDFS上生成一个临时文件所以这个文件大小达到20个字节这个文件呢实际上指的是临时文件HDFS的临时文件好这个临时文件呢你有时候在操作的时候可以看到也就是说并不是呢我采集完之后会在HDFS上直接产生一个文件而是有个临时文件好来看所以说那接下来还有个叫RuleCount
[14:15] 那这个地方说就是文件这个地方也是HDF的临时文件就是HDFS的临时文件那么它的这个大小呢达到五个eventevent啊这是这个单位是eventokevent是产生新文件好这是这个那么现在就现在问题就来了老师你记说每隔三秒
[14:48] 又说呢达到20个字节又说呢达到5个even呢那到底是按照谁的标准去产生新文件呢那注意这三个条件我们只要有一个触发了那么它就会产生新文件也就是说就看这三个条件谁先触发那当然了你也可以去只设一个那另外两个呢可以采用默认值都行的OK这是这么一个配置最后呢一个叫Batch Size这个Batch Size呢是什么概念呢
[15:17] 其实这个byteSense和我们的这个channel有关系我们来看一下还是看我们刚才的这个我画的这个图这个图里边有两种参数一个是capacity表示整个channel的一个容量一个是叫translocation capacity表示一次性向sync传送的数据量其实还有一个什么呢还有一个是你一次性将这个channel中的数据呢存放到这个对列中的一个大小
[15:45] 你看这里边的对链就是你一次性可以将这个签证中多少个even它放到这里边来这里边也有个大小这个大小其实就是我们刚才说的拜计算子好这个我标一下把它拿过来这个其实就是拜计算子拿到这个位置换句话来讲这个拜计算子表示我一次性可以从签证中比如说这个签这个拜计算子是1表示我一次性只能从这个
[16:25] 签证中拿一个放在这个队列中拿一个再放在队列中当这个队列达到一定大小的时候呢我就可以把它发送给Sync那你这个值呢你设的时候注意它既不能超过TranslocationCapacity的大小也不能超过Capacity的大小那么它们三个的这个大小关系是这样的Batch SizeBatch Size呢它肯定是小于TranslocationTranslocationCapacity
[16:57] 然后呢小于谁呢小于capcity好那么大家在设计设计这些东西的时候一定要注意如果你不小心呢它就会包错OK这些呢它的关系是这样的好我把这个再调小一点好那么这是它们三个的关系badge size是一次性从签证中存多少到这个对列中而这个translocate是对列的大小而这个capcity是整个签证大小OK这个我们就讲清楚这个badge size好那这个呢
[17:32] 我标一下吧就是一次从千兆钟向这个发送对链存入的存入的event个数OK这是它的一个特点好那么最后呢还有一个叫use local time stamp这个什么意思呢这个是否使用时间戳你就写出就行了就是否使用本地的时间戳
[18:14] 就是我使用本地时间的意思本地的时间戳那么这是他们的每个参数就这个sync会有点复杂好了那这是他们之间的一个特点好了那么这个sync配置完之后呢我们还没完呀我们是不是还有第五步啊将source channel sync组合在一起那这个呢其实是一个固定操作我们把这个呢第五步也拿过来好第五步我放在这位置啊好那我们呢
[18:48] 这个图画不下了画不下之后我把这个图片再向下拉一点稍等拉过了拉过之后我们来看看这个组合在一起这个怎么写呢我们回到这里看最后一个这两句话回到我们画图也就是这两句话A1.2Sources的RE的channel是CE也就是说这个SourceRE的Source对应的channel是CE而KE这个Sync呢
[19:22] 它定的千流也是C也是C1OK这个我们就把整个的第一步给大家介绍完了我们实现了一个配置好那么配置完了之后呢那接下来呢我们是不是就可以进行其他操作了那这样子我呢呃直接呢把这个配置文件先先把它生成了好吧那在这里呢我打开这里打开我们的呃服务器在哪里呢我们回到这个apache.flom啊在这里
[19:51] 我们在conf下面我们来建一个配置文件这个配置文件和讲义保持一致这个配置文件叫spd.conf好那这里边这里边已经有了有了我把它删掉吧那这样我把它删掉好删掉之后rmspd.就可能以前的OK那我再来rmspd.
[20:23] 把我们刚才的这些数据全部粘贴进来粘的时候一定要检查一下看从上到下来观察一下看看有没有少粘一些东西这个目录结构呢应该都没问题但是这个目录是不存在的如果不存在我们需要去创建这个目录因为这个呢是表示我们监控的一个目录这个呢它会自动创建那接下来我们再
[20:55] Service下面创建一个drfile来我们来看一下保存退出再这个make dr把这个目录直接复制过来好粘一下那这个前两个目录已经存在了我应该只要建这个就行了好走一下好创建完了好创建完之后呢基本上我们第一步的工作呢就到此结束了好那我们呢把这个视频呢先暂停一下好
[21:24] 那么暂停之后呢我们在下一步进行其他操作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置Flume Agent，将本地目录文件采集并写入HDFS。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了Flume Agent架构图，包含Source、Channel、Sink三个组件。
- 列出实现步骤：1.写配置文件；2.配置Source；3.配置Channel；4.配置Sink；5.组合组件；6.启动Agent；7.运行测试。

画面2：
- 展示了Flume架构图和配置文件的编写步骤。
- 列出Flume配置文件的编写步骤：cd /export/servers/apache-flume-1.8.0-bin/conf，mkdir -p /export/servers/dirfile，vim spooldir.conf。
- 展示了配置文件中定义组件名称的代码：
  # Name the components on this agent
  a1.sources = r1
  a1.sinks = k1
  a1.channels = c1

画面3：
- 继续展示配置文件，添加了Source的配置项。
- 代码：
  # Describe/configure the source
  #注意：不能往监控目录中重复写同名文件
  a1.sources.r1.type = spooldir
  a1.sources.r1.spoolDir = /export/servers/dirfile
  a1.sources.r1.fileHeader = true

画面4：
- 展示了Flume Agent架构图，Source指向Channel，Channel指向Sink。
- 展示了配置文件中Source的配置项：
  a1.sources.r1.type = spooldir
  a1.sources.r1.spoolDir = /export/servers/dirfile
  a1.sources.r1.fileHeader = true

画面5：
- 展示了配置文件中Sink和Channel的配置项。
- 代码：
  # Describe the sink
  a1.sinks.k1.type = hdfs
  a1.sinks.k1.channel = c1
  a1.sinks.k1.hdfs.path = hdfs://node01:8020/spooldir/files/%y-%m-%d/%H%M/
  a1.sinks.k1.hdfs.filePrefix = events
  a1.sinks.k1.hdfs.round = true
  a1.sinks.k1.hdfs.roundValue = 10
  a1.sinks.k1.hdfs.roundUnit = minute
  a1.sinks.k1.hdfs.rollSize = 20
  a1.sinks.k1.hdfs.rollCount = 5
  a1.sinks.k1.hdfs.batchSize = 1
  a1.sinks.k1.hdfs.useLocalTimeStamp = true
  #生成的文件类型，默认是SequenceFile，可用DataStream，则为普通文本
  a1.sinks.k1.hdfs.fileType = DataStream
  # Use a channel which buffers events in memory
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 1000
  a1.channels.c1.transactionCapacity = 100
  # Bind the source and sink to the channel
  a1.sources.r1.channels = c1

画面6：
- 展示了Flume Agent架构图，包含Source、Channel、Sink三个组件。
- 展示了配置文件中Source、Channel、Sink的配置项：
  a1.sources.r1.type = spooldir
  a1.sources.r1.spoolDir = /export/servers/dirfile
  a1.sources.r1.fileHeader = true
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 1000
  a1.channels.c1.transactionCapacity = 100
  a1.sinks.k1.type = hdfs
  a1.sinks.k1.channel = c1

画面7：
- 展示了配置文件中Sink的配置项，高亮显示了hdfs.path和filePrefix。
- 代码：
  a1.sinks.k1.type = hdfs
  a1.sinks.k1.channel = c1
  a1.sinks.k1.hdfs.path = hdfs://node01:8020/spooldir/files/%y-%m-%d/%H%M/
  a1.sinks.k1.hdfs.filePrefix = events
  a1.sinks.k1.hdfs.round = true
  a1.sinks.k1.hdfs.roundValue = 10
  a1.sinks.k1.hdfs.roundUnit = minute
  a1.sinks.k1.hdfs.rollSize = 20
  a1.sinks.k1.hdfs.rollCount = 5
  a1.sinks.k1.hdfs.batchSize = 1
  a1.sinks.k1.hdfs.useLocalTimeStamp = true
  #生成的文件类型，默认是SequenceFile，可用DataStream，则为普通文本
  a1.sinks.k1.hdfs.fileType = DataStream
  # Use a channel which buffers events in memory
  a1.channels.c1.type = memory
  a1.channels.c1.capacity = 1000
  a1.channels.c1.transactionCapacity = 100
  # Bind the source and sink to the channel
  a1.sources.r1.channels = c1

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
cd /export/servers/apache-flume-1.8.0-bin/conf
mkdir -p /export/servers/dirfile
vim spooldir.conf

# Name the components on this agent
a1.sources = r1
a1.sinks = k1
a1.channels = c1

画面3：
# Describe/configure the source
#注意：不能往监控目录中重复写同名文件
a1.sources.r1.type = spooldir
a1.sources.r1.spoolDir = /export/servers/dirfile
a1.sources.r1.fileHeader = true

画面5：
# Describe the sink
a1.sinks.k1.type = hdfs
a1.sinks.k1.channel = c1
a1.sinks.k1.hdfs.path = hdfs://node01:8020/spooldir/files/%y-%m-%d/%H%M/
a1.sinks.k1.hdfs.filePrefix = events
a1.sinks.k1.hdfs.round = true
a1.sinks.k1.hdfs.roundValue = 10
a1.sinks.k1.hdfs.roundUnit = minute
a1.sinks.k1.hdfs.rollSize = 20
a1.sinks.k1.hdfs.rollCount = 5
a1.sinks.k1.hdfs.batchSize = 1
a1.sinks.k1.hdfs.useLocalTimeStamp = true
#生成的文件类型，默认是SequenceFile，可用DataStream，则为普通文本
a1.sinks.k1.hdfs.fileType = DataStream
# Use a channel which buffers events in memory
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
# Bind the source and sink to the channel
a1.sources.r1.channels = c1

画面6：
a1.sources.r1.type = spooldir
a1.sources.r1.spoolDir = /export/servers/dirfile
a1.sources.r1.fileHeader = true
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
a1.sinks.k1.type = hdfs
a1.sinks.k1.channel = c1

画面7：
a1.sinks.k1.type = hdfs
a1.sinks.k1.channel = c1
a1.sinks.k1.hdfs.path = hdfs://node01:8020/spooldir/files/%y-%m-%d/%H%M/
a1.sinks.k1.hdfs.filePrefix = events
a1.sinks.k1.hdfs.round = true
a1.sinks.k1.hdfs.roundValue = 10
a1.sinks.k1.hdfs.roundUnit = minute
a1.sinks.k1.hdfs.rollSize = 20
a1.sinks.k1.hdfs.rollCount = 5
a1.sinks.k1.hdfs.batchSize = 1
a1.sinks.k1.hdfs.useLocalTimeStamp = true
#生成的文件类型，默认是SequenceFile，可用DataStream，则为普通文本
a1.sinks.k1.hdfs.fileType = DataStream
# Use a channel which buffers events in memory
a1.channels.c1.type = memory
a1.channels.c1.capacity = 1000
a1.channels.c1.transactionCapacity = 100
# Bind the source and sink to the channel
a1.sources.r1.channels = c1

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：
- 标题：Flume架构图
- 架构图：Source → Channel → Sink
- 标注：Agent

画面2：
- 标题：Flume架构图
- 标题：Flume 配置文件
- 标题：Step 1: Flume 配置文件
-

