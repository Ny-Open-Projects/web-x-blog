# 06系统集成测试-NiFi采集-清洗-统计分析-离线分析-课程访问量

- 阶段：08.阶段八 智慧学成项目
- 章节：06.第六章 智慧学成-系统集成测试
- 源文件：08.阶段八 智慧学成项目\06.第六章 智慧学成-系统集成测试\06系统集成测试-NiFi采集-清洗-统计分析-离线分析-课程访问量_【海量资源尽在 666java.com】.mp4
- 时长 5分23秒（音频 323s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边呢,已经针对集市查询进行了测试,接下来呢,咱们对离线分析进行测试,离线分析呢,是这三个步骤是非常完整的,因为落地业务库和步骤的联动,就是主要就是针对咱们离线分析的,时日分析呢,咱们放到最后,因为时日分析呢,是没有一个日期的概念,因为它是分析当天的数据,
[00:30] 只要数据来我就进行一个统计分析所以说呢咱把它放到最后接下来呢进行离线分析的操作咱们来切到内排这是离线分析的处理器组来切到这个处理器组内这里呢离线分析一共是三个指标咱们来分指标进行测试首先呢进行课程缓慢量的测试课程缓慢量的测试呢咱们这里
[01:00] 数据的生产还是采用NFI生产的数据生产数据的方式按照咱们生产正常的这个生产流程获取数据获取用户的这个原始数据呢应该是使用采集系统然后用户去访问这个页面得到原始数据但是咱们这个地方要进行测试生产大量的数据你一条一条的去去刷新这个是不太现实的所以说呢咱们采用NFI生产数据的方式
[01:31] 这里呢先生产数据然后进行联动测试咱们执行这个处理器这里呢处理器各个处理器呢已经运行这里课程防御量它是统计当天这个所有课程的防御量是多少咱们这个地方生成数据的时候呢这个脚本它默认是生成1到60天的数据所以说呢咱们这个地方数据稍微生成多一点
[02:03] 到20张左右就行了好已经20张超过20张了这个时候呢就可以把它给停下来它停下来之后呢咱们就可以进行咱们的统计清洗数据清洗统计分析以及咱们的同步到业务库来启动咱们的数据清洗和统计程序这个呢主要是咱们的任务调度这里呢是执行的Spark脚本把昨天这个日期呢
[02:36] 给传过去这个任务任务调度起来之后呢咱们把同步也起了同步起来之后只要上边的执行完成下边的就可以将数据呢同步到咱们的买色号中就是咱们的业务库中这个地方呢还需要说明一点就是咱们数据仓库中的数据是并没有清的咱们呢只是把咱们业务报表系统中的这个数据给清了也就是说最终咱们这个地方在保存的时候
[03:08] 它是slack星它会把咱们数据仓库中原来已有的所有数据都给拿过来这个地方使用查询所有的方式那个查询使用查询所有的这种方式的原因呢也是为了咱们后边数据转示有多条的一个展示不然的话你只有一条它这个图表展示是不是太完美了所以说采用查询所有的方式
[03:36] 程序运行过程中呢,咱们是可以在Spark上面查看它的一个任务进度的,这个地方你可以看到两个都结束了,两个都结束了之后呢,咱们呢,就可以看这个进度当前是走到哪了。
[03:54] OK,同步业务库也已经完成,可以看到有61条数据,咱们来刷新一下。
[04:01] 好,最近的一条呢,就是这个,2019-1216。
[04:06] 因为呢咱们现在这个日期已经是到一期了咱们可以来到咱们那个原始数据进行查看原始数据切换一下sauce这个目录呢是咱们采集的目录这个是当天的数据这个呢是16号是咱们201912-16呢是咱们Netfile程序刚生产的这个数据就是它刚生产的咱们来点入进来
[04:39] 大概是有22兆这个不常看到就行反复一下咱们看这个地方生产是21.97月等于20兆好咱们切回温暖到此咱们使用NiFi调度就是数据统计分析和数据清洗的时候日期采用传递分子的方式就是模拟咱们生产环境整个调度的流程到这里就完成了
[05:09] 由于咱们离线分析的指标比较多咱们一个一个的进行测试课程防御量的测试呢就到此为止这里呢测试已经通过把这个处理系统给停下来好视频呢也到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 NiFi 中配置数据流，从 Hive 表读取数据，经过处理后写入 MySQL 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 NiFi 主界面，包含多个处理器的运行状态面板，如“demo”、“离线分析”、“实时分析”等，显示数据处理的吞吐量和任务时间。
画面 2: 展示 NiFi 流程图，包含三个处理器：1. 数据源-维度表流量统计；2. 数据维度统计-维度表流量；3. 同步到业务库维度表-Hive-To-Mysql。其中，处理器 2 的“From Out”连接到处理器 3 的“To Input”。
画面 3: 展示处理器详情窗口，选中“PROPERTIES”标签页，显示“Script Engine”为 python，“Script Body”包含 Python 代码，用于生成时间戳。
画面 4: 展示处理器详情窗口，选中“PROPERTIES”标签页，显示“Command Arguments”为“$Bin(ToNumber($minval))$format(yyyy-MM-dd HH:mm:ss)”，“Command Path”为“/opt/run/script/course_visit.sh”，“Working Directory”为“/opt/run/script”，“Max Attribute Length”为“256”。
画面 5: 展示 NiFi 流程图，包含“input”、“SelectHiveQL”、“EvaluateJsonPath”和“PutSQL”处理器。其中，“SelectHiveQL”连接到“EvaluateJsonPath”，“EvaluateJsonPath”连接到“PutSQL”。
画面 6: 展示 NiFi 流程图，与画面 5 类似，但“SelectHiveQL”和“EvaluateJsonPath”处理器的属性面板显示“Tasks/Time”为“0/00:00:00.000”。
画面 7: 展示 MySQL 数据库管理工具界面，显示“course_visit”表的结构，包含字段“date_info”和“count”。
画面 8: 展示 NiFi 流程图，与画面 2 类似，但处理器 2 的“Read/Write”显示“22.29 MB / 422.85 MB”，“Out”显示“1 → 0 (0 bytes)”。
画面 9: 展示 NiFi 流程图，包含“input”、“SelectHiveQL”、“EvaluateJsonPath”和“PutSQL”处理器。其中，“SelectHiveQL”连接到“EvaluateJsonPath”，“EvaluateJsonPath”连接到“PutSQL”。处理器“SelectHiveQL”的“Tasks/Time”为“1/00:00:00.945”，“EvaluateJsonPath”的“Tasks/Time”为“0/00:00:00.000”，“PutSQL”的“Tasks/Time”为“0/00:00:00.114”。
画面 10: 展示 Hue 文件浏览器界面，显示“/user/Hive/external/data_course”目录下的文件列表，包括“course_buy_biz”、“course_buy_dim”、“course_hot_month_biz”等。
画面 11: 展示 Hue 文件浏览器界面，显示“/user/Hive/external/data_course/course_visit_source”目录下的文件列表，包括“2019-12-10”、“2019-12-11”等日期文件夹。
画面 12: 展示 Hue 文件浏览器界面，显示“/user/Hive/external/data_course/course_visit_source/2019-12-16”目录下的文件列表，包含一个文件“909226c-8c3a-42a3-81a2-8ac25f6c0381”，大小为 22.0 MB。
画面 13: 展示 Hue 文件浏览器界面，显示“/user/Hive/external/data_course/course_visit_source/2019-12-16”目录下的文件列表，但页面加载中，显示加载图标。
画面 14: 展示 NiFi 主界面，显示空白的流程图，无任何处理器。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 中的 Script Body 代码：
```python
import random
import uuid
import time, datetime
from org.apache.commons import IOUtils
from java.io.ByteArrayInputStream import ByteArrayInputStream
from org.apache.nifi.processor import StandardCharsets
from org.apache.nifi.processor.script import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript

BROWSER = ['Firefox', 'Chrome', '360', '23', 'sougou', 'Robot', 'IE', 'Spark', 'QQ', 'UC', 'Druc']

def datetimestamp():
    now_info = datetime.datetime.now()
    date = datetime.datetime.fromtimestamp(int(time.time()))
    time_info = now_info - delta
    for time_info.strftime("%Y-%m-%d %H:%M:%S")
    times = int(time.mktime(time.strptime(for_time, "%Y-%m-%d %H:%M:%S")))
    return times
```

画面 4 中的 Command Arguments：
```
$Bin(ToNumber($minval))$format(yyyy-MM-dd HH:mm:ss)
```

画面 4 中的 Command Path：
```
/opt/run/script/course_visit.sh
```

画面 4 中的 Working Directory：
```
/opt/run/script
```

画面 4 中的 Max Attribute Length：
```
256
```

画面 7 中的 SQL：
```
SELECT * FROM `business`.`course_visit` LIMIT 0, 1000
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2 中的流程图结构：
- 处理器 1（数据源-维度表流量统计）的“Out”连接到处理器 2（数据维度统计-维度表流量）的“To Input”。
- 处理器 2（数据维度统计-维度表流量）的“Out”连接到处理器 3（同步到业务库维度表-Hive-To-Mysql）的“To Input”。

画面 9 中的流程图结构：
- 处理器“SelectHiveQL”连接到“EvaluateJsonPath”。
- “EvaluateJsonPath”连接到“PutSQL”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

