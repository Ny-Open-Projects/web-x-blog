# 06-课程分析-课程购买量-NiFi生产订单数据保存到MySQL&并进行实时采集

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\06-课程分析-课程购买量-NiFi生产订单数据保存到MySQL&并进行实时采集_【海量资源尽在 666java.com】.mp4
- 时长 5分33秒（音频 334s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面呢咱们已经测试了使用NiFi采集买Circle中课程购买量的数据也就是业务数据中的订单数据但是呢在咱们现在的测试阶段中你手动的往数据库中插入一条两条数据这也是不现实的因为咱们需要大量的数据进行一个测试接下来呢就使用NiFi生产数据这里呢生产数据是批量生产生产完成数据生产的数据呢
[00:27] 直接保存到咱们买Circle中也就是直接保存到这张表中保存到这张表中之后呢咱们的前面的这个处理器就是这个买Circlebinlog补货这个处理器呢就会将你生产的数据保存到咱们的数据仓库中也实现了就是咱们的一个采集这个时候呢就是数据也有了采集也有了这个流程上呢也就会更完整一点这里呢咱们接下来就是
[00:57] 使用NiFi生产数据这里生产的数据就是咱们订单的一个数据这里生产订单的生产数据生产订单数据的原代码NiFi调度的原代码也已经配置好了在咱们资料中接下来咱们直接将代码给导入进来然后咱们测试一下咱们的生产数据好咱们来进行一个配置首先是将咱们的备份好的
[01:29] 模板代码给导进来这里有一个课程过不了NiFi造数据这个造数据再强调一遍它是造的是买Circle的数据咱们这个还是补货买Circle的Binlog而不是直接保存到哪不是直接保存到Hive中不是直接保存到数据仓库中这里咱们也是模拟真实的一个企业生产中的一个环境这里咱们来把这个给配置一下它有两个感叹号也就是两项需要配置
[01:59] 第一个呢是这个上面呢它需要一个缓存服务这个缓存服务已经有了第二个呢是咱们的mycirclemycircle呢同样一定不要忘记把密码给配置了密码呢是123456OK然后启用OK启用完成之后呢咱们可以看到这里呢已经没有感叹号了没有感叹号呢咱们接下来就可以进行测试走起这里呢
[02:35] 这里这个地方说明一下,咱们为了尽量保证数据的真实性,咱们直接是从数据库中拿了一个课程的ID,根据课程ID生成咱们的订单数据,这里你可以看到对列中已经有多少条数据了,已经生产了4000多条数据了,这里还在生产5000多条了,6000多条,对列里边你可以看到这对列里加起来应该有几万条数据了,咱们这个时候已经突破1万,咱们就把它给停了。
[03:07] 停完之后呢后期如果你在想用的时候你可以因为咱们对链里边有数据你可以单独启动我这个时候呢把咱们最后一个处理器给启开启起来之后呢它就会把对链中的数据给消耗掉这个时候呢你可以看到已经生产了多少条数据这里边也要对链有数据你还可以把这个给启动起来然后把对链里的数据给消耗而不用把全部的处理器给启动掉这个一共是18000多条数据呢好测试呢
[03:37] 这么多就差不多了咱们来看MySQL这里边咱们捕获了多少这里呢可以看到队列中呢已经这里任务呢输出了有这是14000多1400多个任务但是呢读取了多少条数据啊它输出了往外输出了2万多条数据这里呢通过处理之后它也是读取了1万多条数据这里呢咱们其实开始来数据仓库中来看一下刷走
[04:08] 这里呢咱看能不能找到总条数找不到总条数的情况下咱们是不是可以做另外一件事啊使用circle把它给查一下咱们来查询一下这种生产数据的方式呢就可以大量大量的生产数据咱们来查一下目前这两边有多少条数据了这里呢捕获操作还在进行如果你还想生产数据把前边的就是把咱们生产数据的
[04:45] 给开开就行了它就会自动的进行一个补货咱们来看执行完成没这里呢查询局还在执行这里呢已经生产了一万八千多条数据比咱们在这里一条一条的插入是不是要快捷方便很多呢那肯定是的了好咱们呢再切到文档这里呢使用NiFi生产数据测试演示呢就到这里这里边有一个Python脚本就是咱们生产数据的逻辑
[05:15] 感兴趣可以去了解一下但是呢不建议因为咱们这里呢造出来数据就行了咱们后边的重头戏是什么呀是对数据的一个清洗操作好这里呢咱们那一排生产数据就讲解到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Nifi 实时采集 MySQL 订单数据并写入 Hive，涉及数据源配置、流程设计、Python 脚本处理及测试验证。

2) 按时间顺序列出每张画面的要点：
画面1：在 Navicat Premium 中执行 SQL 插入语句，向 xc_orders 表插入一条订单记录，显示受影响行数为1。
画面2：在 Navicat Premium 中查看 xc_orders 表的数据，显示了多条订单记录，包括 order_number、initial_price、start_time 等字段。
画面3：在 Typora 编辑器中展示 Nifi 数据流设计文档，包含 Nifi 流程图和 Python 代码片段。
画面4：在 Nifi 界面中弹出“Upload Template”对话框，用于上传模板。
画面5：在 Nifi 界面中弹出“Add Template”对话框，选择“课程购买量-到MySQL”模板。
画面6：在 Nifi 界面中显示“0. 数据生产：课程购买量-ToMySQL Configuration”配置页面，包含 DistributedMapCacheServer 和 MySQL 连接池服务。
画面7：在 Nifi 界面中展示数据流图，包含 QueryDatabaseTable、ConvertAvroToJSON、SplitJson、EvaluateJsonPath、ReplaceText、ExecuteScript、PutSQL 等处理器。
画面8：在 Nifi 界面中展示数据流图，包含 QueryDatabaseTable、ConvertAvroToJSON、SplitJson、EvaluateJsonPath、ReplaceText、ExecuteScript、PutSQL 等处理器，并显示右键菜单选项。
画面9：在 Hue 界面中展示 course_orders_source 表的数据，显示了多条订单记录。
画面10：在 Hue 界面中展示 course_orders_source 表的数据，显示了多条订单记录。
画面11：在 Hue 界面中执行 SQL 查询，显示查询结果为 18642。
画面12：在 Typora 编辑器中展示 Nifi 数据流设计文档，包含 Nifi 流程图和 Python 代码片段。
画面13：在 Typora 编辑器中展示 Python 代码，用于生成模拟订单数据并写入流文件。
画面14：在 Typora 编辑器中展示测试步骤，包括启动服务、验证数据写入 Hive 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```sql
INSERT INTO `xc_order`.`xc_orders` (`order_number`, `initial_price`, `start_time`, `end_time`, `status`, `user_id`, `details`, `old_status`)
VALUES ('2901226', 0.81, '2018-04-05 10:32:33', '2018-04-05 21:32:33', 401002, '68769ff7579411a9a3464d438d4e88', '[{"itemId":"2901226","itemNum":1,"itemPrice":"0.81","orderNumber":"2901226"}]', 401002);
```

画面3：
```text
QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → SplitJson → EvaluateJsonPath → PutSQL
```

画面7：
```text
QueryDatabaseTable
ConvertAvroToJSON
SplitJson
EvaluateJsonPath
ReplaceText
ExecuteScript
PutSQL
```

画面13：
```python
dist['status'] = str(pay_status)
dist['order_time'] = str(datetamp())
dist['user_id'] = str(user_id)
dist['details'] = json.dumps(data)
arr.append(dist)

outputStream.write(bytearray(json.dumps(arr), encoding="utf-8"))
```

画面14：
```text
所有的配置量完成之后，按下运行程序进行了测试，启动之前需要确认的服务已启动，这里依赖了MySQL、Hadoop、Hive，请确认已启动，最终在MySQL订单表中产生订单，Nifi把数据实时采集到Hive中，测试成功，测试步骤如下：
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
标题：2.3.3.2.2 流程代码
流程图结构：
QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → SplitJson → EvaluateJsonPath → PutSQL

画面7：
流程图结构：
QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → PutSQL

画面12：
标题：2.3.3.2.2 流程代码
流程图结构：
QueryDatabaseTable → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → ReplaceText → ExecuteScript → SplitJson → EvaluateJsonPath → PutSQL

5) 不要评价画面美观，不要输出与课程无关的内容。

