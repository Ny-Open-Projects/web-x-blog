# 12-课程分析-课程访问量分析-使用NiFi将课程访问量分析结果同步到MySQl

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\12-课程分析-课程访问量分析-使用NiFi将课程访问量分析结果同步到MySQl_【海量资源尽在 666java.com】.mp4
- 时长 6分24秒（音频 380s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面呢,咱们已经将课程访问量的业务数据保存到咱们数据仓库中。
[00:07] 接下来呢,咱们业务报表系统需要使用时,是在MySQL中进行读取的。
[00:14] 这里呢,咱们接下来的操作,就是将MySQL中的数据同步到MySQL中。
[00:21] 这里呢,同步操作是使用的NiFi。
[00:25] 通过本节的学习呢,咱们需要能够使用NiFi。
[00:30] 将课程访问量的业务数据存汉误同步到MySQL中咱们来首先看一下这个MySQL业务表的表结构这里呢它只有两个字段一个是DataInfo一个是Counter就是某一天某一天的访问量只有这两个字段和咱们那个汉误里边它具体的一个区别是少了一个分区的一个概念
[01:00] 少了一个分区的一个数据因为咱们MySQL只做一个数据的展示就是前端报表系统通过读取MySQL进行一个展示不需要其他的一个操作就是说需要哪些数据我同步哪些数据即可这里我使用Navcat来连接一下咱们的数据库咱们智慧学程的数据库
[01:28] 这个Business这个数据库呢在咱们导入学程在线业务库的时候就是下面这几个业务库的时候已经呢将它给导入进来也就是说所需要的表呢也同步的导入进来这个呢CosplayDataBIZ就是咱们与数据仓库相对应的一个业务库业务表接下来呢咱们就是使用NiFi进行一个同步操作
[01:57] 这里呢,调度的代码以及调度的流程咱们文档里边都有展示代码呢,在咱们授课资料中就是第三章,Nefi目录下的课程访问量目录内,然后有一个课程访问量Hive to MyCircle的一个XML这是咱们Nefi调度的一个源码咱们来先看一下调度的流程看完调度流程呢,咱们就
[02:22] 登录NetFi直接进行源码的一个导入导入完成之后开始一个调度的测试咱们NetFi调度流程也是非常简单的首先就是从Hive中读取出来数据读取的数据就是咱们当前的课程访问量统计分析完成之后的一个业务数据读出来的数据它是AVRO格式的这里不能直接使用需要使用转换
[02:52] 转换AVRO的处理器将数换成JSON转换成JSON之后这里通过对JSON的一个切割切割完成之后获取JSON对应的数据获取完数据之后这里到put circle这个处理器就是把咱们这个JSON里边获取到的数据保存到mycircle中这就是
[03:21] 咱们NetFi调度的一个流程接下来呢咱们切到NetFi进行一个数据的导入这里呢咱们NetFi是端口号是58080来登录咱们的NetFi直接点击集合或者你等待5秒咱们离线分析呢现在只有课程访问量咱们呢直接点到咱们离线分析课程访问量这个流程里边把咱们所需要的
[03:51] 源码给上传进来这里呢就是课程缓慢量还有无图埋搜的源码然后进行一个上传操作上传完成之后呢使用添加模板的方式找到课程缓慢量还有无图埋搜这个处理器组然后把它给添加进来添加进来之后呢这个地方有两个感叹号是需要咱们是需要咱们配置的这个配置呢在咱们配置维度数据的时候已经操作过
[04:21] 这个配置方式是一样的,Hive就直接启用即可MySQL需要设置对应的密码这里启用完成把窗口关掉这里MySQL设置一下密码密码是123456设置完成之后点击Play然后点击启用好,这里启用完成之后咱们来刷新一下看到已经没有感叹号了咱们登录,不是登录,咱们点击进入处理器组得到咱们这个
[04:54] 可以看到不是得到是可以看到咱们整个调度流程是从这开始的通过这个箭图的一个转换到这里咱们呢就直接进行一个启动然后进行调度这里可以看到数据在这呢这也有然后再刷一下可以看到这里呢进入了60个数据因为咱们在这里统计分析的时候不是统计对咱们在统计分析的时候得到的是60个数60条数据这里呢
[05:24] 也处理了60条数据说明咱们MySQL已经有了这里使用内容开采来刷新一下好可以看得到咱们数据已经全部进来一共是60条咱们来切到文档这里业务数据存汉误到MySQL使用NiFi调度咱们代码已经导入而且这里测试也已经通过使用NiFi然后调度使用NiFi调度
[05:57] 把数据仓库中课程访问量的业务数据同步到mySQL到这里就完成了咱们视频就到这里通过你学习你需要掌握使用NiFi这个调度将数据进行一个同步的操作好 视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 NiFi 将 Hive 数据同步到 MySQL，包括创建业务表、配置数据流和编写 NiFi 流程 XML 代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录结构，当前章节为“1.2 业务数据从Hive到MySQL”，右侧显示 Hive 表结构和 SQL 创建语句。
画面2：在 Navicat Premium 中展示数据库结构，选中了 `xc_learning` 数据库下的 `business` 数据库。
画面3：展示 NiFi 数据流设计，包含 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程。
画面4：展示 NiFi 流程图，包含 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程。
画面5：在 Hive 的 Table Browser 中展示 `course_visit_biz` 表的数据。
画面6：浏览器打开 NiFi 界面，页面为空白。
画面7：在 NiFi 界面中弹出“Upload Template”对话框，点击“LOAD”按钮。
画面8：弹出“Add Template”对话框，选择模板“课程访问量-Hive-To-Mysql”。
画面9：在 NiFi 的“课程访问量-Hive-To-Mysql Configuration”页面，显示“GENERAL”标签页，包含 Hive 和 MySQL 的连接池配置，状态为“Disabled”。
画面10：在 NiFi 的“课程访问量-Hive-To-Mysql Configuration”页面，显示“GENERAL”标签页，Hive 连接池状态已改为“Enabled”，MySQL 连接池状态仍为“Disabled”。
画面11：在 NiFi 流程图中，显示 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程，各组件的属性已配置。
画面12：在 NiFi 流程图中，显示 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程，各组件的属性已配置。
画面13：展示 NiFi 数据流设计，包含 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程。
画面14：展示 NiFi 流程图，包含 `SelectHiveSQL` → `ConvertAvroToSQL` → `SplitJson` → `EvaluateJsonPath` → `PutSQL` 的流程，各组件的属性已配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```sql
-- 在导入业务数据时，business数据库需导入
CREATE TABLE 'course_visit_biz' (
    'date_info' date NOT NULL COMMENT '天，某一天的访问量',
    'count' int(11) NOT NULL COMMENT '当前访问计数'
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

画面3：
```text
-- 导入业务数据时，business数据库需导入
CREATE TABLE 'course_visit_biz' (
    'date_info' date NOT NULL COMMENT '天，某一天的访问量',
    'count' int(11) NOT NULL COMMENT '当前访问计数'
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

画面4：
```text
nifi 流程xml代码路径：
    资源资料
        第3章-课程分析
            nifi/课程访问量-课程访问量-Hive-To-Mysql.xml
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

画面11：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

画面12：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

画面13：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

画面14：NiFi 数据流流程图，结构为：
SelectHiveSQL → ConvertAvroToSQL → SplitJson → EvaluateJsonPath → PutSQL

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

