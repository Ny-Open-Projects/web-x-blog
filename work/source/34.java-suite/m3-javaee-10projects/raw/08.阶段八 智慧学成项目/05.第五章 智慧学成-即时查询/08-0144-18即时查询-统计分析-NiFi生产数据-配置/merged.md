# 18即时查询-统计分析-NiFi生产数据-配置

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\18即时查询-统计分析-NiFi生产数据-配置_【海量资源尽在 666java.com】.mp4
- 时长 3分55秒（音频 236s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续。
[00:01] 前面呢,咱们已经编写了统计分析的代码,统计分析的代码呢,一共是分为两步,第一步呢,就是关联相关的维度,然后呢,统计学习时长,第二步呢,就是把数据保存到HBase,然后呢,相关的字段索引到Elasticsearch中。
[00:21] 但是呢,中间出现了一个问题,就是咱们采集的原始数据呢,是使用JS买点采集的。
[00:28] 这里的原始数据呢是UUID生成的生成的ID那个UID生成的字段呢有课程的ID视频的ID包括用户的ID然后在统计分析的时候就是关联维度的时候它不能正常的关联到课程名称用户名称以及视频名称就导致了咱们在保存HBase的时候出现空指针异常然后保存暴露接下来呢咱们
[00:58] 就采用NiFi生产数据的方式这里呢NiFi生产数据它读取的数据呢是来源于MySQL它在MySQL中读取了课程ID视频ID包括用户的ID这些ID呢都是真实的然后来生产这个数据呢就能保证咱们统计分析和保存到HBase进行索引到Elasticsearch中的时候这个数据是正常的
[01:28] 就不会出现控制人这种情况这里呢NiFi生产数据咱们生成脚本生产脚本还是采用Python的脚本这里呢NiFi调度呢咱们在资料中也已经提供了这是咱们NiFi的生产数据的这个Python脚本这里呢是咱们NiFi调度的一个源码以及它的一个流程的示意图咱们呢来切到NiFi把咱们这个
[01:57] NiFi生产数据的调度给配置上这里呢咱们来切到NiFi这个呢是咱们即时查询创建的一个处理系组即时查询相关的调度呢都放到这个处理系组内咱们来把这个生产数据的这个脚本源码给上传进来就是NiFi调度的源码给上传进来OK已经上传成功使用添加模板的方式呢把这个
[02:29] 模板给添加进来这里呢添加进来之后还不能直接使用需要配置相关的参数因为咱们要连接MySQL拿取课程ID视频ID以及用户ID所以呢要配接连接MySQL的连接信息这里呢主要是配置密码密码是123456配置完成之后呢点击update然后呢把这个连接给启用了OK启用完成之后呢刷新
[03:00] 就可以看到咱们处理系组已经OK了通过本节的学习咱们需要理解这个地方为什么要使用NiFi来生产数据咱们使用NiFi生产数据的一个原因就是咱们虽然说既然是买点完全模拟了咱们真实数据生产环境的一个真实的一个材质但是它的一个弊端是咱们前端页面不是一个完整的页面
[03:32] 只是做了一个静态音变进行一个模拟流程上是没有问题的但是数据上有点问题所以说咱们就采用NiFi进行一个生产这个真实的一个数据本节的学习呢还要掌握的是就是能够在NiFi上将咱们生产数据的这个调度给配置好好 视频呢就到这里测试交给下一个视频

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Python 脚本生成用户学习数据，并通过 NiFi 流程调度将数据写入 HDFS。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Python 脚本的开头部分，导入了 random、uuid、time、datetime、java.io、org.apache.commons.io、org.apache.nifi.processor.io 等模块，并定义了 BROWSER 列表和 datetamp() 函数。
画面2: 展示了 Python 脚本的 datetamp() 函数实现，用于生成随机的时间戳。
画面3: 展示了 NiFi 流程图，包含多个处理器（如 ReadFile、SplitJson、EvaluateJsonPath、PutHive、ConvertAvroToJSON、JsonToHiveProcessor）及其连接关系。
画面4: 展示了 NiFi 流程图的详细视图，包括处理器和连接的配置。
画面5: 展示了 NiFi 流程图中 ConvertAvroToJSON 和 JsonToHiveProcessor 的详细信息。
画面6: 展示了 NiFi 流程图的空白状态。
画面7: 展示了文件上传对话框，选择文件“数据生产_用户学习(在线学习)-ToHDFS.xml”。
画面8: 展示了 NiFi 流程图的空白状态。
画面9: 展示了 NiFi 流程图中“数据生产_用户学习(在线学习)-ToHDFS”处理器的详细信息。
画面10: 展示了 NiFi 控制器服务配置界面，配置了数据库连接 URL、驱动类名、用户名、密码等。
画面11: 展示了启用控制器服务的界面，服务名为“Mysql连接”，作用域为“Service only”。
画面12: 展示了 NiFi 流程图的空白状态。
画面13: 展示了 NiFi 流程图的详细视图，包括处理器和连接的配置。
画面14: 展示了 NiFi 流程图中“数据生产_用户学习(在线学习)-ToHDFS”处理器的详细信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```python
import random
import uuid
import time, datetime
import java.io
from org.apache.commons.io import TOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript

BROWSER = ['Firefox', 'Chrome', '360', 'Fz', 'sougou', 'Reboot', 'IE', 'Spark', 'QQ', 'UC', 'Dnuc1', 'Liebao', 'AY']
```

画面2:
```python
def datetamp():
    now_info = datetime.datetime.now()
    delta = datetime.timedelta(random.randint(1, 30))
    time_info = now_info - delta
    for_time = time.time.strftime('%Y-%m-%d %H:%M:%S')
    times = int(time.mktime(time.strptime(for_time, '%Y-%m-%d %H:%M:%S')))
    return times
```

画面3:
```xml
资料中介代码路径：
    - 投资资料
        - 第3章-即时营销
            - nifi
                - 用户学习(在线学习).py
```

画面7:
```xml
<filename>数据生产_用户学习(在线学习)-ToHDFS.xml</filename>
```

画面10:
```properties
Database Connection URL: jdbc:mysql://xc-online:3306/xc_cours...
Database Driver Class Name: com.mysql.cj.jdbc.Driver
Database Driver Location: /root/mysql-connector-java-8.0.16.jar
Database User: root
Password: (No value set)
Max Wait Time: 500 mills
Max Total Connections: 8
Validation query: (No value set)
Minimum Idle Connections: 0
Max Idle Connections: 8
Max Connection Lifetime: -1
Time Between Eviction Runs: -1
Minimum Evictable Idle Time: 10 mins
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面3:
- 标题: 3.3.2 NiFi调度
- 流程图结构:
  - ReadFile → SplitJson → EvaluateJsonPath → PutHive
  - ReadFile → SplitJson → EvaluateJsonPath → ConvertAvroToJSON → JsonToHiveProcessor
  - ReadFile → SplitJson → EvaluateJsonPath → PutHive
  - ReadFile → SplitJson → EvaluateJsonPath → ConvertAvroToJSON → JsonToHiveProcessor
  - ReadFile → SplitJson → EvaluateJsonPath → PutHive
  - ReadFile → SplitJson → EvaluateJsonPath → ConvertAvroToJSON → JsonToHiveProcessor

画面5:
- 表格数据:
  - ConvertAvroToJSON: Read/Write 194.35 KB / 575.31 KB, Tasks/Time 00:00:00.031
  - JsonToHiveProcessor: Read/Write 110 bytes / 116 bytes, Tasks/Time 00:00:02.495

画面10:
- 表格数据:
  - Database Connection URL: jdbc:mysql://xc-online:3306/xc_cours...
  - Database Driver Class Name: com.mysql.cj.jdbc.Driver
  - Database Driver Location: /root/mysql-connector-java-8.0.16.jar
  - Database User: root
  - Password: (No value set)
  - Max Wait Time: 500 mills
  - Max Total Connections: 8
  - Validation query: (No value set)
  - Minimum Idle Connections: 0
  - Max Idle Connections: 8
  - Max Connection Lifetime: -1
  - Time Between Eviction Runs: -1
  - Minimum Evictable Idle Time: 10 mins

5) 无。

