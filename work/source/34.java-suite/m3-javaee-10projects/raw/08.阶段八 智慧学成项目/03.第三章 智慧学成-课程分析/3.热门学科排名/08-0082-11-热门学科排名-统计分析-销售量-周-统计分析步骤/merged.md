# 11-热门学科排名-统计分析-销售量-周-统计分析步骤

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\11-热门学科排名-统计分析-销售量-周-统计分析步骤_【海量资源尽在 666java.com】.mp4
- 时长 3分38秒（音频 218s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来咱们对热门学科排名中的销售量进行统计分析在时间维度中又分了周月年咱们是对周和月进行统计首先是对周进行统计分析通过本节的学习咱们需要知道咱们统计分析是基于的数据来源是什么统计分析的步骤是什么通过本节的学习掌握这些即可
[00:29] 首先咱们来看数据来源这里呢数据来源是使用的课程购买量章节已经清洗后的这个DWM层的数据咱们直接使用DWM层的数据进行聚合就行这里呢聚合步骤如下首先呢是获取当前周的区间然后根据这个区间呢进行获取数据这是咱们当前周的是一和三
[01:01] 然后呢咱们是同比计算增幅的根据同比计算增幅根据同比计算增幅呢还需要获取上周对应的时间以及他上周的一个数据这是咱们第二条获取上周相同的时间本周的话是周一到周五上周的话也是要获取周一到周五有了这个时间区间之后呢咱们再根据这个时间区间呢获取上周的数据有了本周的数据和上周的数据之后呢
[01:30] 咱们根据数据聚合出来的结果就是这五天的数据周一到周五这五天的数据聚合出来它的销售量是多少再根据聚合出来的销售量呢来计算涨幅计算完涨幅之后呢这里还不算结束因为呢咱们还需要关联相关的维度数据这里呢根据咱们的计算结果再关联维度数据关联好维度数据才算结束这个时候呢就把咱们这里统计分析的
[01:59] 结果保存到数据仓库中保存到数据仓库呢之后呢咱们这个统计分析就算完成了这是咱们的统计分析步骤咱们来看就是最终保存的这个数据结构这个数据结构呢是理解这个数据结构呢是能帮助咱们理解咱们的一个统计分析的一个过程因为咱们这个是最终的一个结果咱们以上操作这些步骤呢都是为咱们这个结果服务的
[02:29] 咱们最终保存到有学科的ID学科的名称销售量涨幅这个涨幅是根据本周和上周的数据计算出来的这些销量和学科名都是本周的数据以及咱们的分区分区年这里咱们是以周为单位为统计这个地方咱们的分区就是年终的周比如说这就是一年终的第40周
[02:58] 或者是这周是一年中的第50周就是这样好以上呢就是咱们销售量按周统计分析的一个步骤以及呢他这里最终保存的一个结果就是说咱们在维度关联这个步骤计算涨幅和维度关联这两个步骤就是做了哪些事这两个这两个步骤做的事呢就是咱们为咱们最终保存那个结果进行服务的第五步是计算涨幅计算涨幅完成之后呢
[03:29] 根据维度ID获取关联数据这里主要就是选革命好本节就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解统计分析步骤中APP层数据表的结构定义及其对应的实体类定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“3.5.1.1 周”章节下的“3.5.1.1.1 统计分析步骤”和“3.5.1.1.2 APP层数据结构”内容，其中APP层数据结构部分显示了CREATE EXTERNAL TABLE语句。
画面2：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面3：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分，下方显示了“对应实体”部分的注释和case class代码。
画面4：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分，下方显示了“对应实体”部分的注释和case class代码。
画面5：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分，下方显示了“对应实体”部分的注释和case class代码。
画面6：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分，下方显示了“对应实体”部分的注释和case class代码。
画面7：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面8：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面9：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面10：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面11：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面12：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面13：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。
画面14：画面1的延续，光标在CREATE EXTERNAL TABLE语句的字段定义部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1-14中出现的SQL语句：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_sale_week_biz
(course_category_dim_id String,
course_category_name String,
sale_num INT,
sale_percent FLOAT)
PARTITIONED BY (years String, week_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/Hive/external/data_subject/subject_sale_week_biz';

画面1-14中出现的case class代码：
/*
热门学科-销量-周
*/
@Param course_category_dim_id 学科id
@Param course_category_name 学科名
@Param sale_num 销售量
@Param sale_percent 张数
@Param years 分区年
@Param week_of_year 分区年中的周
/
case class SubjectSaleweekBiz(course_category_dim_id: String,
course_category_name: String,
sale_num: Int,
sale_percent: Float,
years: String,
)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

