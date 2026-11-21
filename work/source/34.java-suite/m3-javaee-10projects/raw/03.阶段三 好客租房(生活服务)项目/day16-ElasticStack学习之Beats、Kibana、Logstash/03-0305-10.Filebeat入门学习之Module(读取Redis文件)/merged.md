# 10.Filebeat入门学习之Module（读取Redis文件）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\10.Filebeat入门学习之Module（读取Redis文件）【海量资源尽在 ubkz.com】.mp4
- 时长 19分37秒（音频 1177s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们来看一下failbit中的module那么在前面的我们去读取日志文件的都是我们去做的手动的一个配置比如说呢我们现在想要去读取mycircle的日志的文件或者说我们去读取redis的日志的文件啊等等那么比如说我们要去做的话那我肯定要按照之前的一种配置方式是不是去做一个配置啊大家想一下这个是不是就在不断的重复的去做这个事情
[00:29] 为什么呢比如说你现在有这个需求那么你需要去手动配置一下那么我现在有这个需求是不是也是需要去手动配置一下对吧因为你用release跟我用release咱们都是一样的产出的日志都是一样的对不对所以说呢其实它是有很多的一些通用的一些这个配置
[00:47] 然后去可以把它抽取出来所以这个就是这个module那么其实在failbit中它提供了有这种大量的module来供我们使用其实就可以简化我们的配置那么直接拿来用就可以了不需要做任何的配置OK好那么下面我们来看一下那么我们通过一个这个命令就是failbit然后modules然后list然后就可以去查看我们现有的一些module
[01:12] 那么来看一下那么我们进入到浩克下面有一个BIS一个failbit然后在这个下面我们去执行一下这个命令看来module有哪些那么可以看到module有这么多可以看到有熟悉的像是有什么ApacheElite Search还有Kafka对吧Kabana还有什么MongoDBMySQLJax都是我们非常熟悉的一些这样的一些软件
[01:39] 但是我们会发现那么下面这一堆它都是处于一个什么状态disable这个状态都是禁用的并没有启用而上面这个是enable发现并没有对吧所以说默认情况下面它所自带的一些module都是被什么disable那么所以需要我们先把它请起来
[02:00] 那我们启用谁呢我们接下来呢演示呢我们以这个Redis日志为例啊所以呢我们要启用这个Redis那么怎么样启用呢我们来看一下通过这个failbitmodules然后呢来一个enableRedis就可以了那么可以看到下面这个Redis它本身处于的是disable这个状态那我们来把它启用一下我们来看一下这个效果到这走好那么可以发现是不是已经启用了那么下面呢我们再来查询一下
[02:29] 那么会发现是不是inable里面是不是就有了这个readys了ok好那么就已经就把它启用了好那么我们下面来看一下那么这个module它是存在我们的目录哪个里面呢其实在下面有一个这个module还有一个module是.d那么这两个目录有什么区别我们来看一下那么要注意的是这个module这个目录它所存放的是我们的一些这个module它本身的一些这个配置本身的配置
[02:57] 而下面这个点D的这个目录它所配置的是我们这个module是否有启用的一些相关的配置那么我们可以看一下在module.d下面来看一下那么就这个module.d下面然后我们来看一下你会发现那么除了这个radius.yaml文件之外
[03:19] 其他的全部都是什么呢disable是不是以这个disable结尾那么他呢是不是就没有这个disable了所以我们刚刚的启用他其实就是把这个disable给他去掉这样的意思啊把这个去掉那么是不是就启用了那么当我们去读取配置文件的时候那我是不是就可以读取到这个modules.d下面的新点那么这样的话是不是我们就能够读取到这个文件对吧
[03:45] 好那么接下来呢我们来看这样我们还是去看一下看一下我redis这个配置文件那么在这里面可以发现它呢其实就跟我们刚刚的这个配置很非常的相似就是说我们配置了一个这个module是一个redis然后呢它的一个logo是奇佑然后呢在这个位置需要指定的是它的一个这个日志的一个文件日志文件
[04:09] 然后下面的这个是一个slowlog就是一个慢查询那么在release里面也有这个慢查询这个概念如果我们需要去读取慢查询的一些日志的话我们需要去连接到release然后输这个slowlog才能够去做一个查询那么一会我们来做一个演示一会我们这个就不做演示我们演示上面它就可以了OK好那么我们退出然后我们进入到这个modulesmodules中我们来看一下
[04:36] 在module中是不是有很多的一些这个所对应的module的具体的一些内容那么我们进入redis可以来看一下那么在redis下面有三个一个也三个文件两个目录一个文件然后打开module样本文件那么这个里面是指定它的一些deskboard的一些信息ID fail等等然后我们可以看到在log下面log下面又有一些相关的一些这样的一些
[05:05] 配置比如说看一下它的config等等可以打开看一下那么这个是他的一些写的一些这样的配置配置信息好嘞好那么然后我们继续再往回去看那么像这个man这个要没有文件中是不是也是配置的一些相关的这样的一些信息ok好那么这个就是他具体的一些信息具体信息我们就不去看了我们直接拿来用就可以了
[05:32] 那么当然了在我们讲义中是不是也对这个module这个目录做了一个tree的一个操作然后呢把这个按照一个数的结构把它去展现出来ok这个就是redis的一个module那么接下来呢我们就需要在我们的redis的module中去做一些配置主要是配置谁呢主要是配置我们的这个就是我们redis所产生的这个日志的文件主要是配置它但是呢我们现在有一个问题就是我们现在并没有
[06:00] 我们的Redis并没有去产生日志因为Redis在默认情况下面它是不生成日志的对吧所以需要我们去做一个配置好那么接下来我们先让我们的Redis产生了文件产生文件产生日志文件然后我们再去修改这个位置来OK好那么下面我们来看一下我们去修改Redis的一个Docker的容器
[06:22] 因为我们现在的redis是通过doctor容器去做一个运行的那么我们需要给它去做一个这样的一个设置怎么样设置呢其实也是非常简单的那么我们需要在这个位置来指定一个log fail
[06:35] 就可以了那么指定log fail那么它就能够去生成我们的文件生成日记文件那么生成到哪里它生成到前面我们所指定的一个目录叫date目录当然了它应该是在这个目录下面就node01这个下面ok好那么我们来看一下那么在这个位置我们并且还指定了一个它的log的一个级别我们设置的是一个debug那么在redis中它的一个
[07:03] 日志的级别呢大概有这么四种啊这么四种但是其中这个信息量最大的就是这个debug那么我们往往在做开发和测试的时候呢一般会采用这个debug的方式那么我们为了去获取了更多的一些日志的信息呢那么我们就把它的这个级别呢设置为一个debug级别哎OK好那么下面我们来操作一下好那么我们来把它先把之前的先停掉啊就是ready死可能现在是不是就没跑起来呢我看一下啊
[07:32] 那么现在并没有运行只运行的是我们的ES好那么我们先把它删除掉就Docker,Remote然后Radius-01,Radius-02,Radius-03把这三个先删除掉然后我们来看一下我们进入我们Data目录下面有一个叫做Radius的Data目录然后有三个对吧然后我看一下
[07:57] 这里面有没有日志文件你发现是有这个是我之前做测试的时候去生成的那么咱们把这个删除掉新点log好那么我们再进入到node-cdnode-node-0node-02下面然后我们现在再去做一个remote然后我们再去进入到node
[08:17] 03下面再去做一个remote那么把这三个里面的日志文件的全部给它删除掉然后我们再去做一个操作那我们把这个命令拷贝过来注意这个命令其实就是在我们原有的那个命令的基础之上加了一个log这个配置ok好那么我们把它放到这然后要注意的是这个回车加一个空格然后这个也要注意了这样没有问题了好那么下面这个
[08:44] 也是相同的这个道理然后呢往下面走到这走然后呢这个呢也是一样了那么往下面走走然后呢到这到这走好那么这样的话呢我们三个这个容器的一个创建脚本或者命令就写好了下面呢我们直接对这个地方我们去做一个什么呢做一个创建好那么这样的话呢我们这三个容器呢是不是就创建好了创建好之后呢我们先来检查一下吧
[09:12] 在我们目录中对吧肯定都没有日志文件对不对那么node01它也没有没有任何问题我们去检查一下这个命令应该是没有问题的应该是没有问题好那么我们是不是就可以启动了来一个Docker然后start radius-01radius-02然后radius-03好那么我们把这三个去
[09:41] 我们看一下它叫什么叫名字我们写错了叫做node01node02,node03那么我们扫了个node那么加一个node01然后node02然后node03node03好那我把这三个去跑起来跑起来之后来查看一下日志你会发现这个目录中是不是就多了一个日志的内容我们cat一下node01.log走
[10:04] 那么可以看到这个是不是就是它的日志的输出对吧有不断的有新的日志输出那我们来看一下它的一个文件的大小那么你发现现在是63kb那么就ll吧63是不是在做增长看到了吗不断在做增长那么这个日志文件不断在做刷新那么我们来去通过我们的failbit去做一个这个日志的一个采集好那么接下来呢我们就要回到前面的这个步骤就是我们去修改一下我们这个module的一个配置那么回到我们的hawk这个下面的
[10:34] bit failbit下面有一个叫做modules.d这个目录然后进入然后我们直接打开readies央妙文件那么在下面我们可以看到这个就我们这个log设置为true然后下面的这个来看一下那么这个我们是把这个注释打开然后这个目录路径要注意了那么路径的话那么我们是不是应该这样去做一个配置因为我们有三个
[11:01] 我们就都给他去做一个配置因为你可以看到他是不是是一个宿主对不对好我们来配置那么我们在这个里面我们去找到目录叫做浩克叫date下面的redis date下面的node01下面的这样是不是就可以是这个下面我们看怎么写那就这么来写那就是这个目录
[11:28] 对吧下面的新点log就可以了然后呢这个目录下面新点log这样的话是不是就OK了然后呢我们是不是还可以这样去写然后呢这个02下面的新点log然后呢再写一个就是下面的03下面的新点log
[11:50] OK好那么这样的话我们是不是就配置完成了那么前面说我们这个slow这个log我们不做一个测试了那么我们就给它直接设置一个什么的force那么这样的话就不会再启用了对吧好那么这样的话我们是不是就能够把它去做一个保存了好那么保存完成之后要注意那保存完成之后我们只是把这个配置是不是就已经配置好了那么接下来我们来启动我们的failbit
[12:16] 当然要想启动我们的filebit我们必须还得去做一个测试那么这样咱们把这个先去创建一个配置文件别跟我们之前的搞混那么我们去创建一个它然后把这个内容我们拷贝过来我们来看一下然后我们做一个拷贝那么这个格式显然肯定是有问题的看一下那么这个都是有一个就是缩进的然后我们去给它加一个缩进然后这个这样
[12:47] 然后它是这样ok然后这个是我们看一下set它在这个没有缩进这个是有缩进那么这个没有这个有这个有那么这个没有然后这个有
[13:04] 检查一下这样的话是不是ok好的我们来看一下这个里面的配置那么就是这个是他的import输入那么输入的是一个log其实这个我们不写这个我们现在我们这个目录下面其实并没有任何的一些内容这个其实我们重点不是去读取它重点我们是要去干嘛呢是下面我们来看一下当然了其实我们这个可以不需要去有我们先把这个拿掉这个我们就不要了好那么
[13:32] 这个控制台的输出那么也可以去输出那么也可以去输出的我们的Alexis中都是一样的那么这样我们先让他在控制台里面去做一个输出然后下面这个就是重点那么这个重点是我们去需要配置他的一个modules然后要指定他的一个path
[13:52] 指定 pass指定路径那么是不是可以看到是不是就是在modules.d这个目录下面的新典yaml文件那么我们刚刚所启用的readiesyaml文件是不是就可以得到一个读取到对吧也用不掉好然后保存保存一下那么接下来我们就可以去做一个启动了那么还是我们刚刚启动的命令对吧failfailbit然后-e-c然后指定后刻readies这个文件
[14:20] 然后我们去做一个执行看他会不会在我们控制台打印出来那么你会发现他是不是已经在不断的在我们控制台里面去打印相关的一些日志的一些内容OK那么我们这样我们就把这个先停掉我们来看一下那么这个注意这个message是不是就是我们刚刚所做的我们真正的日志文件中的内容你看发现这个内容对吧是不是就是我们release中的一些日志的一些信息OK
[14:48] 那么我们来看一下它的其他的信息包括有正式时间这是MathData这个没有问题然后我们Bit的信息host的信息然后这个是我们的source就是来源来源于哪里你发现是不是来源于这个文件对吧就是我们刚刚所生成的文件然后这个是它的片一量offset然后这个是具体的一个内容
[15:10] 然后呢下面有一个input是一个log这个没有问题然后呢这个是fairlist然后它module呢采用的是这个redis的一个module去做一个读取你会发现我们并没有去读取这个里面内容是不是我们只是去启用了我们的一个module那么它自动会去完成这样的一个日志内容的一个读取
[15:31] OK那么到这里我们其实已经就成功的去读取到了我们这个数据对不对那么接下来我们可以去把我们这个数据内容我们给它写入到我们的ELAC设置中我们再来做一个测试把它停掉然后我们这样我们先去看一下我们在前面是不是有一个文件叫做浩克ES YAML文件那么我们其实需要是拷贝的是这个内容
[15:58] 对吧这个内容把它拷贝过来然后呢我们去修改一下release然后呢我们来看一下这个把这个就拿掉了这个拿掉这个拿掉然后呢我们就配到下面最下面吧到这然后呢去粘贴一下好那么这样的话呢我们是不是就已经指定了我们的这个elag search对不对好那么我们就来做一个测试那么我们先好那么这样的话呢我们就
[16:27] 搞定了对吧然后呢我们先来看一下我们的elag设置中它的现有的一些索引的数据是不是有这三个对吧然后呢我们再来去做一个测试啊再来去启动它然后呢我们启动它走好你会发现现在它已经连接到我们的elag设置中那我们刷新一下看效果啊那么你会发现呢我们这个索引呢并没有去增加还是我们这个什么呢failbit这个索引过然后呢但是我们看一下它的一个数据啊
[16:54] 那么你会发现它的数据就多了非常多对吧非常多的数据那么我们可以去我们去找一下然后我们看一下刷新一下这个数据是不是就非常多了你看它命中了有29817个数据刷新一下来看一下它的这个数据我们来看来源来源是不是我们redis的数据往下面走这个看能看到吗
[17:23] 那么我们来看一下我们还是把它刷新一下我们看一下这个效果然后在这个里面我们选择这个failbit那么你会发现这个位置注意在这个位置是不是有个source你会发现我们的来源是不是都是我们redis里面这个数据对吧那么就说明我们现在是不是已经就成功的去把我们这个redis的日志的数据就导入到我们的这个elag设置中了是不是非常的简单非常简单
[17:49] 那么现在它是不是就源源不断的去抖进来那么我们其实只是给大家去演示了一种这个module的用法那么其实官方的还有一些其他一些module我们可以打开来看一下那么大概会有这么多对吧这么多包括每一种这个module用法其实都有比如说你现在想要去启用的是Kafka这个module那么你就参考这个里面的一个内容对吧大致的看一下那么在这个里面可以看到它这个是是不是做一个这个enable先启用对吧
[18:18] 启用这个卡不卡那么启用完成之后呢我们去他是需要做一个这个setup这个我们后面也回去做后面我们再说然后呢我们可以看一下去把我们的failbit去跑起来跑起来就可以了为什么他这个位置直接跑就可以了呢原因是在默认注意那么原因是在这个默认的这个failbitfailbit这个配置文件中啊他已经就读取了我们这个module
[18:45] 那么这个下面我们去搜索一下叫做mod然后module然后去搜一下你会发现在这个位置它是不是已经就去加载了我们这个modules的这个d目录下面的一个这个新点压编文件那么所以说可以看到它这个里面的这个玩法直接去启动就可以了你看这启动它不需要修改配置因为默认就已经去读取到这个里面的配置文件了OK
[19:09] 好那么这样的话呢我们是不是就完成了这个module的一个使用啊你会发现是不是也是非常的简单啊哎非常简单那么你需要哪些你直接去启用然后去运行就可以了包括这个熟悉的像什么mycircle啊Nginx啊mongodb啊哎ok那么这个呢我们在后面去做部署的时候也可以去尝试的去把这几个我们也去搭建一下对吧哎ok好嘞那么关于这个module的一个讲解那么就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Filebeat 的 Redis 模块配置并监控 Redis 集群日志，并将数据发送至 Elasticsearch。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于 Filebeat Module 的介绍，提到可以简化配置。
画面 2: 在终端中执行命令 `./filebeat modules list`，列出已启用和禁用的模块。
画面 3: 展示 `redis.yml` 配置文件内容，包含 `enabled: true`、`var.paths` 和 `var.hosts` 等配置项。
画面 4: PDF 文档中展示 `cd modules.d/` 和 `vim redis.yml` 的命令，以及 `redis.yml` 文件内容。
画面 5: 在终端中查看 Redis 数据目录结构，进入 `node01` 目录并列出日志文件。
画面 6: 在终端中执行 `Docker create` 命令，创建三个 Redis 容器 node02、node03、node04。
画面 7: 终端显示 Redis 容器连接失败的错误日志，提示 "Connection refused"。
画面 8: 在终端中查看 `modules.d/` 目录，列出所有模块的 `.disabled` 文件。
画面 9: 在终端中进入 `modules.d/` 目录，编辑 `redis.yml` 文件。
画面 10: PDF 文档中展示 Filebeat 版本列表和测试发现的模块配置位置。
画面 11: 终端显示 Filebeat 成功连接到 Elasticsearch 的日志。
画面 12: 在浏览器中查看 Elasticsearch 的 Kibana 界面，展示索引列表。
画面 13: 浏览器中展示 Filebeat Kafka 模块的文档，包含不同平台的启动命令。
画面 14: PDF 文档中展示 Filebeat 支持的模块列表，包括 Redis、MySQL、Nginx 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
./filebeat modules list
Enabled:
Disabled:
apache2
auditd
Elasticsearch
haproxy
icinga
iis
Kafka
kibana
logstash
mongodb
mysql
Nginx
osquery
postgresql
redis
suricata
system
traefik
```

画面 3:
```
module: redis
log:
enabled: true

# Set custom paths for the log files. If left empty,
# Filebeat will choose the paths depending on your OS.
#var.paths: ['/var/log/redis/redis-server.log']

# Slow logs, retrieved via the Redis API (SLOWLOG)
slowlog:
enabled: true

# The Redis hosts to connect to.
#var.hosts: ['localhost:6379']

# Optional, the password to use when connecting to Redis.
#var.password:
```

画面 4:
```
cd modules.d/
vim redis.yml

module: redis
log:
enabled: true

# Set custom paths for the log files. If left empty,
# Filebeat will choose the paths depending on your OS.
#var.paths: ['/var/log/redis/redis-server.log']

# Slow logs, retrieved via the Redis API (SLOWLOG)
slowlog:
enabled: false

# The Redis hosts to connect to.
#var.hosts: ['localhost:6379']

# Optional, the password to use when connecting to Redis.
#var.password:
```

画面 5:
```
root@itcast01:redis-data# cd node01
-bash: cd: node01: No such file or directory
root@itcast01:redis-data# cd node01
root@itcast01:node01# ll
total 256560
drwxr-xr-x 2 root root 4096 Jan 14 12:02 .
drwxr-xr-x 5 root root 4096 Jan 14 12:03 node01
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node02
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node03
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node04
root@itcast01:node01# ll
total 256560
drwxr-xr-x 2 root root 4096 Jan 14 12:02 .
drwxr-xr-x 5 root root 4096 Jan 14 12:03 node01
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node02
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node03
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node04
root@itcast01:node01# ll
total 12
drwxr-xr-x 2 root root 4096 Jan 15 19:41 .
drwxr-xr-x 5 root root 4096 Jan 15 19:30 ..
-rw-r--r-- 1 root root 364 999 262695185 Jan 15 17:03 nodes-node-01.conf
```

画面 6:
```
Docker create --name redis-node02 -v /data/redis-data/node02/data -p 6380:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --loglevel debug --logfile nodes-node-02.log
Docker create --name redis-node03 -v /data/redis-data/node03/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --loglevel debug --logfile nodes-node-03.log
Docker create --name redis-node04 -v /data/redis-data/node04/data -p 6382:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-04.conf --loglevel debug --logfile nodes-node-04.log
```

画面 8:
```
total 80
drwxr-xr-x 2 root root 4096 Jan 15 19:36 ./
-rw-r--r-- 1 root root 175 Dec 18 04:21 apache2.yml.disabled
-rw-r--r-- 1 root root 845 Dec 18 04:21 auditd.yml.disabled
-rw-r--r-- 1 root root 268 Dec 18 04:21 Elasticsearch.yml.disabled
-rw-r--r-- 1 root root 546 Dec 18 04:21 haproxy.yml.disabled
-rw-r--r-- 1 root root 371 Dec 18 04:21 icinga.yml.disabled
-rw-r--r-- 1 root root 396 Dec 18 04:21 iis.yml.disabled
-rw-r--r-- 1 root root 188 Dec 18 04:21 Kafka.yml.disabled
-rw-r--r-- 1 root root 361 Dec 18 04:21 logstash.yml.disabled
-rw-r--r-- 1 root root 368 Dec 18 04:21 mongodb.yml.disabled
-rw-r--r-- 1 root root 369 Dec 18 04:21 mysql.yml.disabled
-rw-r--r-- 1 root root 388 Dec 18 04:21 Nginx.yml.disabled
-rw-r--r-- 1 root root 192 Dec 18 04:21 osquery.yml.disabled
-rw-r--r-- 1 root root 463 Dec 18 04:21 postgresql.yml.disabled
-rw-r--r-- 1 root root 190 Dec 18 04:21 redis.yml.disabled
-rw-r--r-- 1 root root 192 Dec 18 04:21 suricata.yml.disabled
-rw-r--r-- 1 root root 199 Dec 18 04:21 system.yml.disabled
-rw-r--r-- 1 root root 574 Dec 18 04:21 traefik.yml.disabled
```

画面 9:
```
root@itcast01:modules.d# cd
root@itcast0

