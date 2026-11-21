# 画面线理解：32-热门学科排名-集成测试-报表系统Web展示

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\32-热门学科排名-集成测试-报表系统Web展示_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:29, 00:44, 01:12, 01:25, 01:41, 01:52, 02:07, 02:24, 02:37, 03:05, 03:39, 04:24, 04:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:34:56

1) 这一组画面整体在讲智慧学成Web展示页面的数据可视化效果，以及支撑该页面的数据表结构和ETL流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示“3.7.5 智慧学成Web展示”页面，包含柱状图和数据表格，标注“PS: 我这里测试清洗的数据是7月的”。
画面2：Hue File Browser界面，显示Hive数据目录 /user/hive/external/data_subject 下的多个biz文件。
画面3：智慧学成Web展示页面，显示“销售量”、“学生人数”、“销售额”三个标签页，当前选中“销售量”，下方表格显示“暂无数据”。
画面4：Navicat Premium界面，打开“subject_amount_week.biz”文件，显示课程销售数据，右侧显示表结构信息。
画面5：智慧学成Web展示页面，显示“销售量”标签页下的柱状图和表格数据，表格中“产品管理”排名第一。
画面6：Navicat Premium界面，打开“subject_user_week.biz”文件，显示用户数据，右侧显示表结构信息。
画面7：智慧学成Web展示页面，鼠标悬停在“学生人数”标签上，下方表格显示“暂无数据”。
画面8：智慧学成Web展示页面，显示“学生人数”标签页下的柱状图和表格数据，表格中“产品经理”排名第一。
画面9：Navicat Premium界面，打开“subject_amount_week.biz”文件，显示课程销售数据，右侧显示表结构信息。
画面10：智慧学成Web展示页面，显示“销售额”标签页下的柱状图和表格数据，表格中“产品经理”排名第一。
画面11：同画面1，展示“3.7.5 智慧学成Web展示”页面，包含柱状图和数据表格，标注“PS: 我这里测试清洗的数据是7月的”。
画面12：同画面11，展示“3.7.5 智慧学成Web展示”页面，包含柱状图和数据表格，标注“PS: 我这里测试清洗的数据是7月的”。
画面13：同画面11，展示“3.7.5 智慧学成Web展示”页面，包含柱状图和数据表格，标注“PS: 我这里测试清洗的数据是7月的”。
画面14：展示“3.6.1 业务表结构”和“3.6.2 NiFi调度流程”内容，包含SQL建表语句和ETL流程图。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面14中SQL代码：
CREATE TABLE `subject_sale_week.biz` (
`course_category_dim_id` varchar(255) NOT NULL,
`course_category_name` varchar(255) DEFAULT NULL,
`sale_num` int(11) NOT NULL,
`sale_percent` float(11,4) DEFAULT NULL,
`date_info` varchar(255) DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

画面14中NiFi调度流程图：
数据流向为：Hive → MySQL，使用的NiFi处理节点为：SelectHiveQL → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → EvaluateJsonPath → PutSQL

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14中PPT标题：
3.6.1 业务表结构
3.6.2 NiFi调度流程

画面14中流程图结构：
Hive → SelectHiveQL → ConvertAvroToJSON → SplitJson → EvaluateJsonPath → EvaluateJsonPath → PutSQL

画面14中表格数据：
无表格数据。

5) 无其他内容。
