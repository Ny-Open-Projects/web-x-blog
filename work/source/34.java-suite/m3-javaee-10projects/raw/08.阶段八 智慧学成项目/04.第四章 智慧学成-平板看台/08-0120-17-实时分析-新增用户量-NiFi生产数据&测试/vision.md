# 画面线理解：17-实时分析-新增用户量-NiFi生产数据&测试

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\17-实时分析-新增用户量-NiFi生产数据&测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:30, 01:10, 01:27, 01:46, 02:12, 02:30, 02:37, 02:53, 03:19, 03:31, 03:48, 04:12, 04:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:48:02

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
// 2. Spark Streaming 获取kafka中的用户行为数据，每秒采集一次
val ssc = new StreamingContext(sc, Seconds(5))
ssc.checkpoint(directory = "/user/hive/external/data_course/today_new_user/checkpoint")
// 3. Spark Streaming 读取kafka中的用户行为数据，每秒采集一次
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
// 2. Spark Streaming 获取kafka中的用户行为数据，每秒采集一次
val ssc = new StreamingContext(sc, Seconds(5))
ssc.checkpoint(directory = "/user/hive/external/data_course/today_new_user/checkpoint")
// 3. Spark Streaming 读取kafka中的用户行为数据，每秒采集一次
val kafkaParam = Map[String, Object]
```

画面14：
```text
3.2.1 统计分析逻辑
数据传输实时采集新用户，实时统计当天的新增用户量。统计规则如下：
1. 手动管理kafka的offset (redis中获取现存的offset，如果没有从(0)开始)
2. Spark Streaming 获取kafka中的用户行为数据，每秒采集一次
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
