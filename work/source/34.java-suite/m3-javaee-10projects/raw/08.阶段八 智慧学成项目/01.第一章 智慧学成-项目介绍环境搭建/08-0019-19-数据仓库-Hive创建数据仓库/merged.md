# 19-数据仓库-Hive创建数据仓库

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\19-数据仓库-Hive创建数据仓库_【海量资源尽在 666java.com】.mp4
- 时长 5分29秒（音频 329s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来学习Hive创建数据仓库通过本章节的学习一定要把数据仓库给建立起来这个地方如果没有创建好的话咱们后面的数据采集数据清洗数据分析就没有办法进行接下来是Hive的介绍Hive是由Facebook开发后来贡献给了阿发奇基金会Hive是建立在Hadoop上面的数据仓库软件使用Lay Circle局
[00:29] 来协助读写管理存储在Hadoop上的数据集接下来呢就是咱们进行数据仓库的创建首先创建数据库接着呢是创建数据库里边的各个表这个地方呢是根据主题划分分为了四个主题库还有一个维度库因为维度是各主题都要使用的所以说把维度给单独拉了出来各主题里边又根据
[00:59] 咱们的数据仓库的分层进行了分层创建咱们的表这里提供了一个统一创建Circle的一个文件这里咱们切换到编辑器这个文件你创建仓库的时候为了省事就可以把这个直接放到咱们HUE里边执行把数据仓库给建立起来下面是咱们各维度表还有咱们各
[01:30] 分层表的一个介绍咱们这块的话主要是以创建为主各数据库还有各表咱们不会详细的介绍你想了解的话下面有上面是表下面有对应的实体的一个解释就是每个字段的解释都在这里咱们这里呢就直接使用咱们这个提供好的统一键表语句键库语句把数据仓库给建立起来
[01:59] 这里建立数据仓库使用的是HUE然后这里是咱们的所有的数据仓库的表和库把它给粘过来粘过来之后这个地方Ctrl加A选择所有点这个小三角或者是Ctrl加回车就会创建下面是有日志的它每创建一个每创建一个它就会执行一下这个地方有一个DataLock
[02:32] 如果遇到锁库的话不用着急咱们创建到哪了就把前面的给删了接着进行创建就行还是全选进行一个创建它正在进行这还在创建的一个过程中一共的话刚才是咱们执行了创建的库创建库之后它出现了一个锁库的一个错误这种错误的话一般是不用管它的
[03:06] 你只用把之前创建过的给删掉然后接着创建就行了也有可能你在执行的过程中没有任何问题一次性就给它创建了好创建完成这个地方已经执行到第28个了咱们回到文档让它来后边执行这里的话咱们维度维度还有咱们那个主切道表是分开的你想了解的话就想了解哪一个表它是什么意思就可以现在来
[03:39] 就是打开这个文档进行一个查看后边在使用过程中会有详细的一个介绍就是咱们使用到哪个维度了或者是使用到哪一个主题库里边的哪一个表了咱们会有一详细的介绍这一块现在以创建数据仓库为主咱们来看一下执行完成没执行到第30个的时候又说了一个数据database use lock的就是数据库被锁这个还是不用管它
[04:09] 咱们来看一下是最后一条是哪一个solar mouse biv就是这个咱们来看一下这个创建成功没如果创建成功了它上面的全部删掉就行了它是在这个库里边然后这张表solar mouse bivOK创建好前面的就可以把它全部给删掉删掉完成之后咱们接着上去
[04:39] Ctrl加A然后点不行好这七个已经全部创建了咱们来看一下最后一个创建好没如果最后一个创建好了就说明都好了最后一个是平台这个主题的它是平台理性分析OK这个已经创建好创建完成之后这个就可以删了下面有咱们历史记录这个地方就是以后咱们写伺服器的地方
[05:12] 咱们来看一下所有的表这是所有的库点进去可以看到所有的表到此咱们数据仓库就已经创建完成OK本章节的内容到此结束

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hive中创建数据仓库的数据库和维度表，包括创建数据库、时间维度表、课程维度表、用户维度表、事实表等，并在Hue和编辑器中执行SQL语句。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容，标题为“4 Hive创建数据仓库”，子标题“4.1 Hive介绍”和“4.2 创建数据库”，并列出创建数据库的SQL语句：// 数据库分层创建，主题 create database data_agency; create database data_course; create database data_platform; create database data_subject;
画面2：在Sublime Text编辑器中显示创建外部表的SQL代码，包括创建course_category_dim表和data_dimen.area_dim表的语句。
画面3：展示PPT内容，标题为“4.3.2.1 时间 - time_dim”，并列出创建time_dim表的SQL语句：CREATE EXTERNAL TABLE IF NOT EXISTS data_dimen.time_dim (time_dim_id String, year String, month String, day String, hour String, week String, week_name String) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' STORED AS TEXTFILE location '/user/Hive/external/data_dimen/time_dim';，以及字段说明。
画面4：展示PPT内容，标题为“4.3.2.2 课程 - course_dim”，并列出创建course_dim表的SQL语句：CREATE EXTERNAL TABLE IF NOT EXISTS data_dimen.course_dim (course_id String, course_name String, course_category_id String, course_grade_id String, course_status_id String, company_id String, user_id String, course_status String, description String) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' STORED AS TEXTFILE location '/user/Hive/external/data_dimen/course_dim';，以及对应实体的注释。
画面5：展示Hue界面，正在编写Hive SQL语句。
画面6：在Hue中执行创建数据库的SQL语句，成功创建了data_agency、data_course、data_dimen、data_platform、data_subject数据库。
画面7：在Hue中执行创建时间维度表的SQL语句，但提示“database is locked”。
画面8：在Hue中执行创建课程维度表的SQL语句，包括创建course_buy_fact表和course_visit_fact表。
画面9：在Hue中执行创建用户维度表的SQL语句，包括创建subject_user_week_biz表和subject_user_month_biz表。
画面10：展示PPT内容，标题为“4.4.1 创建主题表”，并列出创建course_category_dim表的SQL语句：CREATE EXTERNAL TABLE IF NOT EXISTS data_dimen.course_category_dim (course_category_dim_id String, name String, label String, parentid String, isshow String, orderby String, isleaf String) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' STORED AS TEXTFILE location '/user/Hive/external/data_dimen/course_category_dim';，以及对应实体的注释。
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
location '/user/Hive/external/data_dimen/course_dim';

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
location '/user/Hive/external/data_dimen/course_category_dim';

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
location '/user/Hive/external/data_dimen/time_dim';

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
location '/user/Hive/external/data_dimen/course_dim';

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
location '/user/Hive/external/data_dimen/time_dim';

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
location '/user/Hive/external/data_course/course_buy_fact';

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
location '/user/Hive/external/data_course/course_visit_fact';

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

