# 画面线理解：06-热门学科排名-用户选课DWD层字段说明&清洗分析

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\06-热门学科排名-用户选课DWD层字段说明&清洗分析_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:16, 00:17, 00:21, 01:28, 01:40, 01:58, 02:00, 02:37, 02:38, 02:41, 02:47, 02:49, 02:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:13:35

1) 这一组画面整体在讲什么（一句话）：
讲解用户选课数据从ODS层到DWD层的清洗过程，包括维度表结构、清洗字段映射及对应的Spark清洗代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“3.4.2 用户选课-数据清洗分析”章节，列出清洗逻辑：原始数据-关联维度-保存到事实表，关联维度包括课程分类维度、用户维度、课程维度、时间维度。下方表格展示“清洗字段说明”，包括字段名、清洗说明、清洗后字段名。
画面2：展示“3.4.3 用户选课-清洗代码”章节，列出Spark清洗代码，包含包导入和类引用。
画面3：展示“3.4.2 用户选课-数据清洗分析”章节，表格中“清洗字段说明”部分显示“course_id”字段的清洗说明。
画面4：展示“3.4.1 用户选课DWD层数据”章节，说明原始数据来自MySQL，清洗后保存到事实表中，表格展示“事实表字段说明”，包括字段名、源数据字段、字段说明。
画面5：展示“3.4.2 用户选课-数据清洗分析”章节，表格中“清洗字段说明”部分显示“choose_time 年”字段的清洗说明。
画面6：展示“3.4.2 用户选课-数据清洗分析”章节，表格中“清洗字段说明”部分显示“choose_time 月”字段的清洗说明。
画面7：展示“3.4.2 用户选课-数据清洗分析”章节，表格中“清洗字段说明”部分显示“choose_time 日”字段的清洗说明。
画面8：展示“3.4.2 用户选课-数据清洗分析”章节，表格中“清洗字段说明”部分显示“course_id”字段的清洗说明。
画面9：展示“3.4.2 用户选课-数据清洗分析”章节，表格中“清洗字段说明”部分显示“user_id”字段的清洗说明。
画面10：展示“3.4 数据清洗”章节，标题为“3.4.1 用户选课DWD层数据”，说明原始数据来自MySQL，清洗后保存到事实表中，表格展示“事实表字段说明”，包括字段名、源数据字段、字段说明。
画面11：展示“3.4.2 用户选课-数据清洗分析”章节，表格中“清洗字段说明”部分显示“course_id”字段的清洗说明。
画面12：展示“3.4.2 用户选课-数据清洗分析”章节，表格中“清洗字段说明”部分显示“status”字段的清洗说明。
画面13：展示“3.4.2 用户选课-数据清洗分析”章节，表格中“清洗字段说明”部分显示“status”字段的清洗说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2代码：
package cn.itcast.xc.analysis.subject.Learn
import cn.itcast.xc.common.PtlEnvironment
import cn.itcast.xc.entity.(CourseMan, LearningCourseFact, LearningCourseSource)
import cn.itcast.xc.utils.DataUtils
import org.apache.spark.sql.SparkSession
//**

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1标题：“3.4.2 用户选课-数据清洗分析”
表格数据：
清洗逻辑：原始数据 - 关联维度 - 保存到事实表，关联的维度如下：
• 课程分类维度
• 用户维度
• 课程维度
• 时间维度
清洗字段说明：
| 清洗字段 | 清洗说明 | 清洗后字段名 |
| --- | --- | --- |
| - | uuid生成用户选课id | learning_course_dim_id |
| course_id | 通过course_id关联到课程分类维度，从而获取课程分类id | course_category_dim_id |
| course_id | course_id 即课程维度id | course_dim_id |
| user_id | user_id 即用户维度id | user_dim_id |
| choose_time | 通过日期格式化计算出时间维度id | time_dim_id |

画面4标题：“3.4.1 用户选课DWD层数据”
表格数据：
事实表字段说明：
| 用户选课事实表字段 | 源数据字段 | 字段说明 |
| --- | --- | --- |
| learning_course_dim_id | - | 用户选课id, uuid生成 |
| course_category_dim_id | 通过course_id关联 | 课程分类维度id |
| course_dim_id | course_id | 课程维度id |
| user_dim_id | user_id | 用户维度id |
| time_dim_id | 通过choose_time计算 | 时间维度id |
| status | status | 选课状态 |
| years | choose_time 年 | 分区年 |
| months | choose_time 月 | 分区月 |
| days | choose_time 日 | 分区日 |

画面10标题：“3.4 数据清洗”
子标题：“3.4.1 用户选课DWD层数据”
表格数据：
事实表字段说明：
| 用户选课事实表字段 | 源数据字段 | 字段说明 |
| --- | --- | --- |
| learning_course_dim_id | - | 用户选课id, uuid生成 |
| course_category_dim_id | 通过course_id关联 | 课程分类维度id |
| course_dim_id | course_id | 课程维度id |
| user_dim_id | user_id | 用户维度id |
| time_dim_id | 通过choose_time计算 | 时间维度id |
| status | status | 选课状态 |
| years | choose_time 年 | 分区年 |
| months | choose_time 月 | 分区月 |
| days | choose_time 日 | 分区日 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
