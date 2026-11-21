# 21-实时分析-今日购买量-NiFi生产数据&测试

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\21-实时分析-今日购买量-NiFi生产数据&测试_【海量资源尽在 666java.com】.mp4
- 时长 4分59秒（音频 300s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边已经对订单数据进行了实时的采集,并且咱们编写了实时的统计分析程序,咱们经过测试,实时统计分析程序,指功能是没有问题的,它可以把结果实时的保存到咱们的Redis中,但是整个测试过程中,咱们在生产数据的时候,这个地方是使用
[00:27] 手动的一条一条的往那个买测课中插入数据这个呢效率是非常低的咱们呢接下来是使用NetFi批量生产数据的方式把这个数据呢生产到买测课中生产到买测课中之后呢咱们这个咱们这个订单表就可以有相应的数据订单表有了相应的数据咱们这个地方是有NetFi上呢是对咱们课程购买量这个订单表是实时采集的就可以把这个数据呢放到卡普卡上
[00:57] 放到卡发上之后呢咱们现在这里呢今日这个购买量的实时分析程序呢也在运行着呢它就可以把结果呢实时的保存到咱们的redis中接下来呢咱们就是对NiFi那个进行一个调度调用脚本来生产咱们的一个课程购买量这个数据也就是订单数据其实呢这个调度在第三章离线分析那个课程购买量这个章节呢已经生产过数据
[01:27] 这里呢咱们只是把那个处理器组给重新的复制了一份来保存到来使用就是来复用在这里呢咱们再进行一个配置就行了这个呢咱们在前前面导入咱们今日购买量采集的时候已经把这个生产数据呢在一起导入进去咱们来切到内发上对它进行一个配置这里呢就是数据生产咱们呢直接使用它就行了
[01:57] 首先是MySQL的连接因为它订单数据需要一些真实的数据比如说课程的ID这些相关数据它需要连接MySQL获取到课程ID的数据完了之后配置完成之后配置MySQL密码配置完成之后把它启用MySQL密码一定不要忘记启用不要忘记配置如果你忘了的话这个处理系统就没法正常的运行这个配置完成之后咱们接下来就是直接运行它了
[02:28] 运行了之后你可以看到这里呢已经有大量的数据在往那个买测课中写这里你可以看到已经写入了一千多条两千多条了现在已经三千多条了这个呢实时的写咱们呢程序也在实时的统计分析咱们来看因为是咱们的程序是五秒统计一次但是呢这个地方呢是实时的在写咱们来看现在那个redis中是多少条数据了放心
[03:01] 已经9000多条数据了咱们可以看到咱们来刷新一下这个这个因为有一会没刷新了12000多条数据再刷新它现在13000咱们再刷这个也已经超过13000了它已经15000了咱们把它给停下来来看现在有多少现在是16000多条咱们来看咱们的实时统计1603条这个结果是没有问题的因为呢之前咱们在这个地方呢
[03:29] 使用手动插入的方式是插入了三条插入了三条呢咱们这里又使用NiFi生产了16660条加上原来的三条现在Redis咱们实时统计的就是16663条咱们这里实时统计也是没有问题的咱们切回文档这里呢咱们使用NiFi生产数据的方式批量的生产的数据并且呢咱们
[04:00] 内海的调度上面还有一个实时采集咱们订单的数据通过实时的采集把这个数据发送到Kafka上咱们呢统计分析程序通过读取Kafka中的数据进行一个实时的统计分析并且呢将结果保存到redis中咱们呢通过验证整个凉城没有任何问题好到此呢咱们今日购买量这个指标的全部内容就完成了这全部内容包括呢
[04:29] 数据的一个采集这里是实时采集保存到卡普卡中然后呢编写统计分析的代码进行实时的统计分析由于咱们生产数据呢之前这个生产数据呢是使用手动插入订单表这种方式它呢效率比较慢咱们呢接下来呢又使用了NiFi生产数据的方式调度脚本批量生产数据通过测试呢这里也是没有问题了好视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 NiFi 工具生成模拟订单数据并写入 MySQL 数据库，同时展示相关的 Python 脚本和 Spark 实时分析代码。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 Typora 文档，标题为“4.3 NiFi生产数据”，子标题“4.3.1 生产数据脚本”，展示 Python 代码片段，导入模块包括 random、uuid、time、datetime、json、java.io，以及 org.apache.nifi.processors.script 的 ExecuteScript。
画面2: 显示 Navicat Premium 中的 MySQL 数据库表 xc_order，包含 order_number、initial_price、start_time、end_time、status、user_id、details 字段，数据行数为 21647。
画面3: 显示 IntelliJ IDEA 中的 Scala 项目，运行日志显示 Spark 作业执行过程，包括 DStreamGraph、SparkContext、DAGScheduler 等信息，最终结果为 ResultStage 42。
画面4: 显示 Typora 文档，标题为“4.3 NiFi生产数据”，子标题“4.3.1 生产数据脚本”，展示 Python 代码片段，定义了 datestamp 函数，用于生成随机时间戳。
画面5: 显示 NiFi 流编辑器界面，空白画布，准备创建数据流。
画面6: 显示 NiFi 流编辑器界面，弹出“Enable Controller Service”对话框，服务名称为“Mysql连接”，作用域为“Service only”，引用组件包括“PutSQL”和“QueryDatabaseTable”。
画面7: 显示 NiFi 流编辑器界面，已构建的数据流，包含 In、ExecuteScript、SplitJson、ReplaceText、PutSQL 等处理器，数据流向清晰。
画面8: 显示 NiFi 流编辑器界面，弹出“RodView Community v1.7.0”窗口，显示数据库表结构，字段为“course buy d...”。
画面9: 显示 NiFi 流编辑器界面，数据流已构建完成，处理器包括 In、ExecuteScript、SplitJson、ReplaceText、PutSQL，数据流向清晰。
画面10: 显示 Navicat Premium 中的 MySQL 数据库表 xc_order，执行 SQL 语句，INSERT INTO 语句插入数据，影响行数为 1。
画面11: 显示 Typora 文档，标题为“4.3 NiFi生产数据”，子标题“4.3.1 生产数据脚本”，展示 NiFi 流架构图，包含 In、ExecuteScript、SplitJson、ReplaceText、PutSQL 等处理器，以及资料中调度代码路径。
画面12: 显示 IntelliJ IDEA 中的 Scala 项目，运行日志显示 Spark 作业执行过程，包括 DStreamGraph、SparkContext、DAGScheduler 等信息，最终结果为 ResultStage 42。
画面13: 显示 Navicat Premium 中的 MySQL 数据库表 xc_order，执行 SQL 语句，INSERT INTO 语句插入数据，影响行数为 1。
画面14: 显示 Typora 文档，标题为“4.3 NiFi生产数据”，子标题“4.3.1 生产数据脚本”，展示 Python 代码片段，定义了 datestamp 函数，用于生成随机时间戳。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
```python
import random
import uuid
import time, datetime
import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript
```

画面4:
```python
import random
import uuid
import time, datetime
import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript

def datestamp():
    now_info = datetime.datetime.now()
    delta = datetime.timedelta(random.randint(1, 60))
    time_info = now_info - delta
    for_time = time_info.strftime('%Y-%m-%d %H:%M:%S')
    times = int(time.mktime(time.strptime(for_time, '%Y-%m-%d %H:%M:%S')))
    return times
```

画面10:
```sql
INSERT INTO `xc_order` (`order_number`, `initial_price`, `price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`) VALUES ('00042860926e4c1', 1201.00, 1201.00, '2019-10-08 09:22:03', '2019-10-08 09:22:03', 401002, '73501356444405b74', NULL, 401002);
```

画面13:
```sql
INSERT INTO `xc_order` (`order_number`, `initial_price`, `price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`) VALUES ('00042860926e4c1', 1201.00, 1201.00, '2019-10-08 09:22:03', '2019-10-08 09:22:03', 401002, '73501356444405b74', NULL, 401002);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面11:
- PPT 标题：4.3 NiFi生产数据
- 子标题：4.3.1 生产数据脚本
- 架构图：In → ExecuteScript → SplitJson → ReplaceText → PutSQL
- 资料中调度代码路径：
  - 资源资料
    - 第1章 实时分析
      - nifi
        - 代码
          - 如此实现 - tokafta-实时.xml
- PS: 数据生产的 NiFi 流程实时采集的流程放在了一个 XML 中，只导入一次即可！

5) 无

