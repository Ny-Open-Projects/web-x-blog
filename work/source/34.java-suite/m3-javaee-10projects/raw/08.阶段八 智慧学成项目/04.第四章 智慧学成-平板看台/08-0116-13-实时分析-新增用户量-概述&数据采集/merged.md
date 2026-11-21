# 13-实时分析-新增用户量-概述&数据采集

- 阶段：08.阶段八 智慧学成项目
- 章节：04.第四章 智慧学成-平板看台
- 源文件：08.阶段八 智慧学成项目\04.第四章 智慧学成-平板看台\13-实时分析-新增用户量-概述&数据采集_【海量资源尽在 666java.com】.mp4
- 时长 6分51秒（音频 411s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,前边已经完成了今日访问量这个指标的数据采集以及数据的实时分析,接下来咱们学习新增用户量这个指标,通过新增用户量这个指标的学习,咱们需要掌握能够采集新增用户量的原始数据,能够编写新增用户量的实时统计分析程序,能够将结果保存到Redis中。
[00:29] 咱们首先对数据采集进行学习这里数据采集是使用NiFi进行采集使用NiFi采集是监控MySQL的binlog然后采集用户表的数据只要有insert数据就是说只要有新增用户数据就把它给采集过来放到卡普卡中这里采集的流程咱们在咱们的资料中已经准备好这里咱们来切到NiFi
[00:58] 将咱们准备好的代码上传上去上传上去之后通过相应的配置咱们就可以对它进行相应的采集咱们来切到来发这里咱们现在是实时分析咱们新建一个处理区组就叫新增用户量进入处理区组内咱们把新增用户量的采集给上传上来这里新增用户量to Kafka实时这就是咱们的采集
[01:32] 准备好的采集代码点击upload进行上传上传成功之后呢使用添加模板的方式把它给添加进来好进入这个处理器组这个处理器组内呢你可以看到它又有两个第一个呢是生产数据第二个呢是实时的一个采集咱们呢现在是使用采集的程序只用配置咱们采集就行了等咱们清洗代码写完咱们再使用生产数据放到mycircle然后呢这个地方进行实时的一个采集
[02:02] 咱们是在进行一个实时的计算在redis里边呢来观看那个结果咱们现在只用关心咱们数据采集即可对它进行相应的配置这里呢它需要缓存服务咱们缓存服务之前已经配置好这里呢它用缓存服务呢需要缓存的客户端咱们把这个客户端给启用了即可好已经启动完成已经启用完成启用完成之后呢还得对它进行一个配置
[02:34] 咱们呢要读取MySQL的配置这里呢是监控的MySQL的binlog监控MySQL的binlog呢它的密码是在这个处理器上进行配置的一定不要忘记密码呢是123456配置完成之后呢咱们就可以启动这个处理器了这里呢启动这个处理器之后它监控数据是把MySQL的所有binlog都会拿过来这里呢先暂停一下因为MySQL的binlog呢
[03:03] 之前的binlog有很多这里呢咱们需要把这个binlog给清一下等它读完因为这个地方还有一个进程在执行它那是还在读取这个binlog等它读取完成之后呢咱们把这个队列给清了就行咱们来切到文档咱们启动完咱们的测试之后呢测试在下边启动完启动这个Netfile进行测试的时候呢咱们是可以使用这个命令来查看咱们topic中的内容这里呢
[03:35] 我已经切换到Kafka的容器中在Kafka的闭门楼下准备好了命令把这个命令给执行一下咱们现在Kafka中还没有放数据这个地方模拟的消费者他会在这里进行一个阻塞咱们来切到温暖上面有咱们这里Kafka的配置以及过滤数据表和库的配置咱们在代码中就是NiFi的代码中已经配置好这里简单的了解一下就行
[04:05] 主要就是咱们的broker地址以及咱们主题名这是咱们需要了解的客户单名称是随意起的还有上面是咱们过滤数据库和表的名称都在咱们处理器中进行一个相应的配置咱们来切断内徽看这里采集完美它处理器已经将所有的binlog给拿过来这里直接清了就行因为很多binlog对咱们来说是没用的咱们是监控的新用户
[04:36] 等会在这里边添加新的用户来观察咱们的一个采集就行把垃圾数据清完之后咱们再次启动咱们的处理器组启动完成之后你可以看到这个地方它在有任务但是它并没有读到数据是因为咱们没有对message进行操作没有产生binlog所以说它不能读到数据这里咱们随机的复制一条复制为insert语句
[05:05] 对它进行一个修改这个地方把主件给改了改短一点这个地方我就随意改了名字也改一下这个名字就叫测试好运行这个地方你可以看到它已经插入成功了咱们来回到这里刷新一下好在这里已经插入成功咱们来切到内饭上这个地方刷新一下你可以看到这个地方它已经有一个
[05:40] 然后把它给放到了卡普卡中咱们来切到卡普卡这个地方你可以看到有一个用户ID咱们这里统计新增用户量只需要它的ID就行了因为ID是唯一的你可以看到这个ID和这个ID是一样的到此咱们使用NiFi咱们使用NiFi采集MySQL数据库中用新增用户数据就测试OK了咱们来切到文档
[06:11] 本节咱们概述了新增用户量需要掌握的内容以及使用NetFi采集了咱们新增用户所需要的原始数据好 视频就到这里通过学习需要掌握咱们能够使用NetFi采集到新增用户的原始数据并将那个数据保存到卡普卡中还有就是咱们通过学习新增用户量需要掌握哪些内容
[06:38] 第一呢就是数据的采集第二呢就是统计代码的编写第三呢就是把这个数据呢保存到咱们的redis中进行实时的一个查看好视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 NiFi 实时采集 MySQL 中的用户数据，并通过过滤和路由写入 Kafka。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程大纲，当前章节为“3.1 数据采集”，子章节“3.1.1 NiFi采集流程”，并附带 NiFi 流程图，图中包含 CaptureChangeMySQL、Insert、EvaluateAttribute、PublishKafka 等组件。
画面2：在 NiFi 界面中弹出“Add Process Group”对话框，输入名称“新用户”后点击 ADD。
画面3：新建的 Process Group 界面为空白画布。
画面4：在 NiFi 界面中，已添加两个处理器：左侧为“0.数据生产-新增用户ToMySQL”，右侧为“1.数据采集-新增用户-Mysql-ToKafka实时采集”。
画面5：NiFi 流程图中，CaptureChangeMySQL 组件的输出连接到 Insert 组件，Insert 组件的输出连接到 EvaluateAttribute 组件，EvaluateAttribute 组件的输出连接到 PublishKafka 组件。
画面6：NiFi 流程图中，EvaluateAttribute 组件的输出连接到 PublishKafka 组件，同时 Insert 组件的输出连接到 EvaluateAttribute 组件。
画面7：在 NiFi 界面中，显示“3.1.3 NiF调度Kafka配置”页面，配置处理器的属性中，“Known Brokers”为“xc-online-Kafka:9092”，“Topic Name”为“NEW_USER”，“Client Name”为“publish_course_buy”。
画面8：在 NiFi 界面中，显示“3.1.3 NiF调度Kafka配置”页面，配置处理器的属性中，“Known Brokers”为“xc-online-Kafka:9092”，“Topic Name”为“NEW_USER”，“Client Name”为“publish_course_buy”。
画面9：在 NiFi 界面中，显示“3.1.3 NiF调度Kafka配置”页面，配置处理器的属性中，“Known Brokers”为“xc-online-Kafka:9092”，“Topic Name”为“NEW_USER”，“Client Name”为“publish_course_buy”。
画面10：在 NiFi 界面中，弹出“Empty Queue”对话框，提示“274,164 FlowFiles (203.06 MB) were removed from the queue”。
画面11：在 Navicat Premium 中，显示 MySQL 数据库“xc_online”的“xc_user”表，其中包含多条用户记录。
画面12：在 Navicat Premium 中，选中“xc_user”表中的一条记录，点击“删除”按钮。
画面13：在 Navicat Premium 中，选中“xc_user”表中的一条记录，点击“删除”按钮。
画面14：在 NiFi 界面中，显示“3.1.2 NiF调度过滤指定数据库和表配置”页面，配置处理器的属性中，“Database”为“xc_user”，“Table Name”为“xc_user”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面7：
Known Brokers: xc-online-Kafka:9092
Topic Name: NEW_USER
Client Name: publish_course_buy

画面14：
Database: xc_user
Table Name: xc_user

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PPT 标题为“3 新增用户量”，子标题为“3.1 数据采集”，并附带 NiFi 流程图，图中包含 CaptureChangeMySQL、Insert、EvaluateAttribute、PublishKafka 等组件。
画面5：NiFi 流程图中，CaptureChangeMySQL 组件的输出连接到 Insert 组件，Insert 组件的输出连接到 EvaluateAttribute 组件，EvaluateAttribute 组件的输出连接到 PublishKafka 组件。
画面6：NiFi 流程图中，EvaluateAttribute 组件的输出连接到 PublishKafka 组件，同时 Insert 组件的输出连接到 EvaluateAttribute 组件。
画面14：PPT 标题为“3.1.2 NiF调度过滤指定数据库和表配置”，并附带配置处理器的属性表，表中包含“Database”和“Table Name”字段。

5) 无。

