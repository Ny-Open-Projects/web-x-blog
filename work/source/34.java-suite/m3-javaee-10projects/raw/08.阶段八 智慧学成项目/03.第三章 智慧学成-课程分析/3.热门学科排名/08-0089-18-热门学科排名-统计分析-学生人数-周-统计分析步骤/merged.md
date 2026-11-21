# 18-热门学科排名-统计分析-学生人数-周-统计分析步骤

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\18-热门学科排名-统计分析-学生人数-周-统计分析步骤_【海量资源尽在 666java.com】.mp4
- 时长 3分2秒（音频 182s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边咱们已经统计分析了热门学科排名中的销售量的数据,分别统计了时间维度中的周还有月。
[00:10] 接着咱们对学生人数进行统计分析,这里也是统计时间维度中的周和月,咱们首先来看周的统计分析。
[00:21] 这里学生人数采用的数据是咱们用户选课清洗后的数据,保存在DW层。
[00:29] 这里呢,咱们直接拿来使用即可。
[00:32] 增幅的计算方式呢,也是采用同比的计算方式。
[00:36] 咱们来看统计分析的步骤。
[00:39] 这个统计分析的步骤呢,和咱们前边销售量按周的统计的步骤是一样的。
[00:45] 首先来看,第一个,就是获取当前周区间的数据。
[00:50] 这里呢,当前周是以你传过来的日期为准的。
[00:54] 你如果传到2018年的日期,那肯定按2018年。
[00:58] 那个具体的日期为维度为一个基准点然后呢进行一个当前周的一个日期的一个计算这里获取上周日期的一个区间也是根据咱们传过来的日期为基准然后计算的咱们上周的区间是多少当前周的区间是多少上周的区间也对应应该是多少有了区间的数据之后呢再根据区间数据来获取本周的数据还有上周的数据
[01:29] 有了这两项数据,咱们就可以进行第五步,然后增幅的一个计算,这里呢是采用同比的计算方式。
[01:37] 增幅的计算完成之后呢,接下来咱们就是对相关维度的关联。
[01:42] 关联之后呢,咱们就得到了最终的一个结果数据,咱们就可以再次保存到咱们的数据仓库中。
[01:50] 这个数据呢,就是咱们后期业务可以使用的一个数据。
[01:55] 咱们来看这里的数据结构,就是咱们最终保存的数据结构。
[01:59] 这里有注释,咱们直接看注释即可首先是课程分类的ID这个其实就是咱们认为学科的ID接下来是课程分类的名称对应咱们认为学科的名称接下来是用户数也就是你当前这个州具体的选客人数是多少具体的学生人数是多少接下来是它的一个涨幅这里涨幅就是咱们这里说的增幅接下来是分区年这个没什么好说然后是分区州
[02:30] 周的话就是年终的第几周你第30周还是第40周还是第50周就是年终的第几周通过本节的学习呢咱们需要理解咱们统计分析的步骤以及呢咱们使用的基础数据是哪一个最终呢保存到咱们数据仓库中的APP层的这个数据结构呢是什么样的咱们就保存哪些数据通过本节的学习理解这些就行好本节呢讲解就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解学生人数统计分析的步骤和APP层数据表结构，包括Hive表定义和Scala实体类定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“3.5.2.1.1 统计分析步骤”列表，包含7个步骤，其中第1步为“获取当前周的时间区间，例：周1 至 周5”，第2步为“获取上周的相同时间区间，例：上周1 至 上周5”，第3步为“获取本周的数据”，第4步为“获取上周的数据”，第5步为“计算增幅”，第6步为“根据维度id获取相关数据”，第7步为“保存结果”。同时展示“3.5.2.1.2 APP层数据结构”的Hive表创建语句。
画面2：与画面1内容相同，仅光标位置不同。
画面3：与画面1内容相同，仅光标位置不同。
画面4：展示“3.5.2.1.2 APP层数据结构”的Hive表创建语句，并在下方新增“对应实体：”部分，显示注释“//热门课程-学生人数(选课)-周”，以及字段注释，如“@param course_category_dim_id 课程分类id”、“@param course_category_name 课程分类名”、“@param user_num 用户数”、“@param user_percent 比例”、“@param years 分区年”、“@param week_of_year 分区年中的周”。
画面5：与画面4内容相同，仅光标位置不同。
画面6：与画面4内容相同，仅光标位置不同。
画面7：与画面4内容相同，仅光标位置不同。
画面8：与画面4内容相同，仅光标位置不同。
画面9：展示“3.5.2.1.1 统计分析步骤”列表，光标位于第1步“获取当前周的时间区间，例：周1 至 周5”。
画面10：与画面9内容相同，仅光标位置不同。
画面11：与画面9内容相同，仅光标位置不同。
画面12：与画面9内容相同，仅光标位置不同。
画面13：与画面4内容相同，仅光标位置不同。
画面14：与画面4内容相同，仅光标位置不同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1-3：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_user_week_biz
(course_category_dim_id String,
course_category_name String,
user_num Int,
user_percent FLOAT)
PARTITIONED BY (years String, week_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/Hive/external/data_subject/subject_user_week_biz';

画面4-8,13-14：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_user_week_biz
(course_category_dim_id String,
course_category_name String,
user_num Int,
user_percent FLOAT)
PARTITIONED BY (years String, week_of_year String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/Hive/external/data_subject/subject_user_week_biz';

对应实体：
/*
热门课程-学生人数(选课)-周
*/
@param course_category_dim_id 课程分类id
@param course_category_name 课程分类名
@param user_num 用户数
@param user_percent 比例
@param years 分区年
@param week_of_year 分区年中的周

case class SubjectLearnUserWeekBiz(course_category_dim_id: String,
course_category_name: String,
user_num: Int,
user_percent: Float,
years: String,
week_of_year: String)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

