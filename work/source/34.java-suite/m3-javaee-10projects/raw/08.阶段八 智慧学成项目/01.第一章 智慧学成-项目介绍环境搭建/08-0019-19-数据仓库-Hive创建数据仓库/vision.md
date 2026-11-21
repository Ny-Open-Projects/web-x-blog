# 画面线理解：19-数据仓库-Hive创建数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\19-数据仓库-Hive创建数据仓库_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:41, 01:17, 01:33, 01:45, 02:09, 02:24, 02:35, 02:54, 03:18, 03:32, 04:10, 04:44, 05:05, 05:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:39:31

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hive中创建数据仓库的数据库和维度表，包括创建数据库、时间维度表、课程维度表、用户维度表、事实表等，并在Hue和编辑器中执行SQL语句。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容，标题为“4 Hive创建数据仓库”，子标题“4.1 Hive介绍”和“4.2 创建数据库”，并列出创建数据库的SQL语句：// 数据库分层创建，主题 create database data_agency; create database data_course; create database data_platform; create database data_subject;
画面2：在Sublime Text编辑器中显示创建外部表的SQL代码，包括创建course_category_dim表和data_dimen.area_dim表的语句。
画面3：展示PPT内容，标题为“4.3.2.1 时间 - time_dim”，并列出创建time_dim表的SQL语句：CREATE EXTERNAL TABLE IF NOT EXISTS data_dimen.time_dim (time_dim_id String, year String, month String, day String, hour String, week String, week_name String) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' STORED AS TEXTFILE location '/user/hive/external/data_dimen/time_dim';，以及字段说明。
画面4：展示PPT内容，标题为“4.3.2.2 课程 - course_dim”，并列出创建course_dim表的SQL语句：CREATE EXTERNAL TABLE IF NOT EXISTS data_dimen.course_dim (course_id String, course_name String, course_category_id String, course_grade_id String, course_status_id String, company_id String, user_id String, course_status String, description String) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' STORED AS TEXTFILE location '/user/hive/external/data_dimen/course_dim';，以及对应实体的注释。
画面5：展示Hue界面，正在编写Hive SQL语句。
画面6：在Hue中执行创建数据库的SQL语句，成功创建了data_agency、data_course、data_dimen、data_platform、data_subject数据库。
画面7：在Hue中执行创建时间维度表的SQL语句，但提示“database is locked”。
画面8：在Hue中执行创建课程维度表的SQL语句，包括创建course_buy_fact表和course_visit_fact表。
画面9：在Hue中执行创建用户维度表的SQL语句，包括创建subject_user_week_biz表和subject_user_month_biz表。
画面10：展示PPT内容，标题为“4.4.1 创建主题表”，并列出创建course_category_dim表的SQL语句：CREATE EXTERNAL TABLE IF NOT EXISTS data_dimen.course_category_dim (course_category_dim_id String, name String, label String, parentid String, isshow String, orderby String, isleaf String) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' STORED AS TEXTFILE location '/user/hive/external/data_dimen/course_category_dim';，以及对应实体的注释。
画面11：在Hue中执行创建agency_amount_week_biz表的SQL语句，但提示“database is locked”。
画面12：在Hue中执行创建platform_offline_biz表的SQL语句。
画面13：在Hue中执行创建platform_offline_biz表的SQL语句，成功执行。
画面14：展示PPT内容，标题为“4 Hive创建数据仓库”，子标题“4.1 Hive介绍”和“4.2 创建数据库”，并列出创建数据库的SQL语句：// 数据库分层创建，主题 create database data_agency; create database data_course; create database data_platform; create database data_subject;。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
// 数据库分层创建，主题
create database data_agency;
create database data_course;
create database data_platform;
create database data_subject;

画面2：
st_name String,
company_id String,
company_name String,
users String,
status String,
status_name String,
description String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
location '/user/hive/external/data_dimen/course_dim';

CREATE EXTERNAL TABLE
IF NOT EXISTS data_dimen.course_category_dim
(course_category_dim_id String,
name String,
label String,
parentid String,
isshow String,
orderby String,
isleaf String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
location '/user/hive/external/data_dimen/course_category_dim';

画面3：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_dimen.time_dim
(time_dim_id String,
year String,
month String,
day String,
hour String,
week String,
week_name String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
location '/user/hive/external/data_dimen/time_dim';

画面4：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_dimen.course_dim
(course_id String,
course_name String,
course_category_id String,
course_grade_id String,
course_status_id String,
company_id String,
user_id String,
course_status String,
description String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
location '/user/hive/external/data_dimen/course_dim';

画面5：
无代码内容。

画面6：
create database data_agency;
create database data_course;
create database data_dimen;
create database data_platform;
create database data_subject;

画面7：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_dimen.time_dim
(time_dim_id String,
year String,
month String,
day String,
hour String,
week String,
week_name String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
location '/user/hive/external/data_dimen/time_dim';

画面8：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_course.course_buy_fact
(course_buy_fact_id String,
course_id String,
course_name String,
course_category_id String,
course_grade_id String,
company_id String,
user_id String,
price String,
visit_time String,
status String,
description String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/hive/external/data_course/course_buy_fact';

CREATE EXTERNAL TABLE
IF NOT EXISTS data_course.course_visit_fact
(course_visit_fact_id String,
course_id String,
course_name String,
course_category_id String,
course_grade_id String,
company_id String,
user_id String,
visit_time String,
visit_count Int,
visit_duration Int,
status String,
description String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS PARQUET
location '/user/hive/external/data_course/course_visit_fact';

画面9：
CREATE EXTERNAL TABLE
IF NOT EXISTS data_subject.subject_user_week_biz
(course_category_dim_id String,
course_id String,
course_name String,
course_grade_id String,
company_id String,
user_id String,
user_name String,
user_phone String,
user_email String,
user_status String,
user_create_time String,
user_update_time String,
user_login_time String,
user_login_count Int,
user_visit_count Int,
user_comment_count Int,
user_like_count Int,
user_share_count Int,
user_collect_count Int,
user_follow_count Int,
user_fans_count Int,
user_following_count Int,
user_level String,
user_points Float,
user_integral Float,
user_balance Float,
user_recharge_count Int,
user_recharge_amount Float,
user_consume_count Int,
user_consume_amount Float,
user_gift_count Int,
user_gift_amount Float,
user_coupon_count Int,
user_coupon_amount Float,
user_voucher_count Int,
user_voucher_amount Float,
user_redpacket_count Int,
user_redpacket_amount Float,
user_activity_count Int,
user_activity_amount Float,
user_task_count Int,
user_task_amount Float,
user_award_count Int,
user_award_amount Float,
user_bonus_count Int,
user_bonus_amount Float,
user_reward_count Int,
user_reward_amount Float,
user_refund_count Int,
user_refund_amount Float,
user_return_count Int,
user_return_amount Float,
user_exchange_count Int,
user_exchange_amount Float,
user_transfer_count Int,
user_transfer_amount Float,
user_withdraw_count Int,
user_withdraw_amount Float,
user_deposit_count Int,
user_deposit_amount Float,
user_loan_count Int,
user_loan_amount Float,
user_investment_count Int,
user_investment_amount Float,
user_borrow_count Int,
user_borrow_amount Float,
user_repay_count Int,
user_repay_amount Float,
user_interest_count Int,
user_interest_amount Float,
user_penalty_count Int,
user_penalty_amount Float,
user_fine_count Int,
user_fine_amount Float,
user_commission_count Int,
user_commission_amount Float,
user_dividend_count Int,
user_dividend_amount Float,
user_bonus_count Int,
user_bonus_amount Float,
user_reward_count Int,
user_reward_amount Float,
user_refund_count Int,
user_refund_amount Float,
user_return_count Int,
user_return_amount Float,
user_exchange_count Int,
user_exchange_amount Float,
user_transfer_count Int,
user_transfer_amount Float,
user_withdraw_count Int,
user_withdraw_amount Float,
user_deposit_count Int,
user_deposit_amount Float,
user_loan_count Int,
user_loan_amount Float,
user_investment_count Int,
user_investment_amount Float,
user_borrow_count Int,
user_borrow_amount Float,
user_repay_count Int,
user_repay_amount
