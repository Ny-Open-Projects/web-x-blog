# 17-实时分析-新增用户量-NiFi生产数据&测试

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\17-实时分析-新增用户量-NiFi生产数据&测试_【海量资源尽在 666java.com】.mp4
- 时长 4分56秒（音频 297s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边已经编写了新登用互联的实时统计分析的代码,咱们也采用手动插入数据的方式,来往这个MySQL中添加数据,添加完成之后数据呢,咱们这里有一个NiFi上的调度脚本,NiFi的调度脚本就可以实时的采集到MySQL的数据并且放到卡普卡中,放到卡普卡中之后呢,咱们这个统计分析程序就读到了数据进行实时的统计。
[00:30] 并且把结果保存到Redis中保存到Redis中之后就是流程算完成了但是咱们手动的插入数据一条一条的插入这个是非常慢的接下来咱们就采用NiFi生产数据的方式批量的生产数据保存到MySQL中保存到MySQL中之后咱们还有另外一个NiFi的处理器是实时的采集MySQL的数据保存到卡普卡中
[00:58] 就可以生成大量的数据进行一个测试这个NetFi生产数据这个调度咱们也已经上传到了咱们的NetFi中它是和咱们这里的NetFi实时采集是一起的所以说这里咱们登录到咱们的NetFi切换到咱们的NetFi直接对它进行一个配置就行了这个就是咱们生产数据的处理系组咱们来对它进行配置
[01:28] 这里需要配置的就是买伺服的链接因为咱们生成的数据是要保存在买伺服中的这个地方需要配置密码配置完成密码之后把它给启用了密码是123456配置完密码之后把它给启用好这里已经启用完成启用完成之后咱们就可以直接对它处理系统进行一个启动因为其他项都是配置好的这里直接启动咱们可以看到这个地方生成了
[01:59] 大概是60多条数据咱们来刷新一下看这个数据过来没显示的是33再刷咱们再来刷新因为它这个处理器呢咱们来切到温度每次的话它是随机生成10到50条数据它这个地方呢显示是64条咱们在脚本里边是有控制的咱们来看一下脚本这个地方呢是有一个Fall循环Fall循环的话
[02:35] 它是10-50它这个地方显示显示60多条肯定显示的有问题咱们来重新启动这个地方是91这个地方显示的还是不对咱们来数据库进行一个验证就行了现在是159条咱们来看这个地方结局完之后这个是160条因为数据库我之前删过一条数据它160对了这个地方是159
[03:05] 它等于159加1就行了因为我之前删过一条数据这个呢咱们再次启动把它给停了再启动再让它生成一批数据生成一批数据呢这个地方显示90咱不管它它这个地方咱们来以数据库新增的为准这是159刷新198198的话咱们说了198应该加1的咱们Release中的结果呢应该是199刷新走199
[03:35] 这里咱们内发生产数据就是没有问题了但是它这个地方显示条数可能多少有点问题咱们不用管它咱们是以数据库中的为主的好咱们切回问了到此咱们使用内发生产数据并且使用内发实时采集生产的数据因为咱们生产的数据保存在买搜狗中这里实时采集也是采集的买搜狗
[04:03] 采集后的买搜会的数据呢是保存到Kafka中把它发送到Kafka中之后呢咱们的实时统计程序是在工作中的就是咱们的开发工具中还在运行它呢这里就实时的进行一个统计并且将结果呢来保存到咱们的redis中这里呢只要你有新增的数据这里你保存就可以保存成功好到此呢咱们新增用户量数据的采集以及统计分析就完成了咱们呢为了
[04:34] 生产大量的数据呢还使用NiFi调度生产数据的方式就是调度脚本生产数据的方式来生产批量生产数据进行一个测试这里呢测试也是没有问题的到此呢咱们新增用户量这个整个指标的一个内容就完成了视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 NiFi 实时采集用户数据并写入 MySQL，同时展示配套的 Spark Streaming 代码和 Redis 检查点机制。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Navicat Premium 中 MySQL 数据库表 xc_user 的数据，包含用户信息，用于验证数据写入结果。
画面2：展示 IntelliJ IDEA 中的 Scala 代码，用于实时处理用户数据，包含 Redis 检查点配置和 Kafka 参数。
画面3：展示 NiFi 文档页面，说明数据生产流程的 XML 文件可直接导入，包含流程图和代码路径。
画面4：在 NiFi 的 Controller Services 页面，配置 MySQL 连接池，名称为 "MySQL连接"，类型为 "DBCPConnectionPool 1.9.2"，状态为 "Disabled"。
画面5：在 NiFi 的 Controller Services 页面，将 "MySQL连接" 的状态从 "Disabled" 改为 "Enabling"。
画面6：展示 NiFi 流程图，包含 ExecuteScript、EvaluateJsonPath、SplitJson 和 PutSQL 四个处理器，数据流向为：ExecuteScript → Name split → SplitJson → PutSQL。
画面7：在 NiFi 中配置 ExecuteScript 处理器，设置 Import random、Import uuid、Import time、datetime 等模块。
画面8：在 NiFi 中配置 ExecuteScript 处理器的 Script Body，编写 Python 代码用于生成随机用户数据。
画面9：在 RedisView 中，选择数据库 db15，设置字段 new_user_data 的值为 133。
画面10：展示 Navicat Premium 中 MySQL 数据库表 xc_user 的数据，包含用户信息，用于验证数据写入结果。
画面11：在 RedisView 中，选择数据库 db15，设置字段 new_user_data 的值为 160。
画面12：展示 NiFi 流程图，数据流向与画面6相同，但数据处理后的结果已更新。
画面13：展示 IntelliJ IDEA 中的 Scala 代码，用于实时处理用户数据，包含 Redis 检查点配置和 Kafka 参数。
画面14：展示 NiFi 文档页面，说明统计分析逻辑和代码，包含数据采集、实时计算、保存到 Redis 等步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```scala
val redis = new RedisUtils
val offsets = redis.getLatestCommittedOffsets("c_u_offset", topicName, partitions = 1)
// 2. Spark Streaming 获取Kafka中的用户行为数据，每秒采集一次
val ssc = new StreamingContext(sc, Seconds(5))
ssc.checkpoint(directory = "/user/Hive/external/data_course/today_new_user/checkpoint")
// 3. Spark Streaming 读取Kafka中的用户行为数据，每秒采集一次
val kafkaParam = Map[String, Object]
```

画面3：
```text
资料中代码路径：
  - 提交资料
    - 第一章-实时分析
      - nifi
        - 配置
          - 很快访问到-Kafka实时.xml
PS: 数据生产的NiFi流程 实时采集的流程放在了一个XML中，只导入一次即可！
```

画面6：
```text
Name success
Name split
Name matched
```

画面7：
```text
Import random
Import uuid
Import time, datetime
```

画面8：
```python
times = int(time.time() - 3600 * 8)
return times

class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass
    def process(self, inputStream, outputStream):
        id = []
        for i in range(1, random.randint(1, 50)):
            id = str(uuid.uuid4()).replace("-", "")
            username = str(uuid.uuid4()).replace("-", "")
            name = random.choice(1) + random.choice(2) + random.choice(3)
            ip = str(random.randint(1, 200)) + "." + str(random.randint(1, 200)) + "." + str(random.randint(1, 200)) + "." + str(random.randint(1, 200))
            create_time = datetime.now()
            oo = {}
            oo['id'] = id
            oo['username'] = username
            oo['name'] = name
            oo['ip'] = ip
            oo['create_time'] = create_time
            arr.append(oo)
```

画面13：
```scala
// 1. 初始化 Redis
val redis = new RedisUtils
val offsets = redis.getLatestCommittedOffsets("c_u_offset", topicName, partitions = 1)
// 2. Spark Streaming 获取Kafka中的用户行为数据，每秒采集一次
val ssc = new StreamingContext(sc, Seconds(5))
ssc.checkpoint(directory = "/user/Hive/external/data_course/today_new_user/checkpoint")
// 3. Spark Streaming 读取Kafka中的用户行为数据，每秒采集一次
val kafkaParam = Map[String, Object]
```

画面14：
```text
3.2.1 统计分析逻辑
数据传输实时采集新用户，实时统计当天的新增用户量。统计规则如下：
1. 手动管理Kafka的offset (redis中获取现存的offset，如果没有从(0)开始)
2. Spark Streaming 获取Kafka中的用户行为数据，每秒采集一次
3. 根据用户id，实时计算新增用户量
4. 统计结果存入redis，供业务使用
5. redis中保存当前offset进度
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
标题：3.3.3 测试
架构图：ExecuteScript → Name split → SplitJson → PutSQL
表格数据：无

画面6：
架构图：ExecuteScript → Name split → SplitJson → PutSQL
表格数据：无

画面12：
架构图：ExecuteScript → Name split → SplitJson → PutSQL
表格数据：无

5) 不要评价画面美观，不要输出与课程无关的内容。

