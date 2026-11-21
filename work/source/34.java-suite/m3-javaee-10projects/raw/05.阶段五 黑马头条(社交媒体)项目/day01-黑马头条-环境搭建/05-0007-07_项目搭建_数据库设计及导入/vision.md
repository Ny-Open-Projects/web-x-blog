# 画面线理解：07_项目搭建_数据库设计及导入

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\07_项目搭建_数据库设计及导入【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:20, 01:28, 01:49, 02:06, 02:17, 02:31, 02:45, 03:53, 04:53, 05:11, 06:20, 07:22, 07:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:28:53

1) 这一组画面整体在讲什么（一句话）：
讲解黑马头条项目数据库设计，包括ER图设计、分库设计、核心数据流、冗余设计及导入数据库等环节。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示数据库设计章节目录，包含ER图设计、分库设计、冗余设计等内容，提及数据库设计规范文档《黑马头条-数据库规范设计说明书.md》及PowerDesigner工具使用文档。
画面2：讲解索引约束，列出6条强制与推荐规则，如唯一索引、联合索引、排序与范围查询等。
画面3：讲解建表约束，列出6条强制规则，包括字段命名规范、表名规范、禁止使用保留字、主键命名、小数类型使用等。
画面4：展示PowerDesigner软件界面，左侧为文档目录，右侧为软件界面，包含“PowerDesigner125 Crack”文件。
画面5：讲解PowerDesigner创建表操作，点击“表”图标可创建表，编辑表信息时，表名可中文，字段名必须英文。
画面6：讲解设置表关联，用户表与订单表为一对多关系，通过“FK_Reference_1”外键关联。
画面7：展示PowerDesigner生成SQL文件界面，设置数据库为MySQL，生成SQL文件名为“t_order.sql”，并显示生成的SQL代码。
画面8：展示分库设计，项目采用分库设计，包含AppInfo、Behavior、WebMedia、Crawlers、Admin五个库。
画面9：展示核心数据流图，包含CSDN、用户、App、管理、爬虫、文章等模块，数据流向从CSDN到App，再到管理，最后到爬虫和文章。
画面10：讲解冗余设计，传统设计需关联查询，冗余设计可直接查询，无需关联。
画面11：继续讲解冗余设计，展示冗余设计的表结构，用户表包含用户ID和用户名，订单表包含订单ID和用户ID。
画面12：展示文件资源管理器，右键点击“heima_leadnews.sql”文件，选择“用记事本打开”。
画面13：在Navicat for MySQL中，选择“heima_leadnews.sql”文件，点击“打开”按钮。
画面14：在Navicat for MySQL中，显示数据库结构，包含多个表，如ap_article、ap_user_feedback、migration_qtz_calendars等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7 SQL代码：
drop table if exists t_order;
drop table if exists t_user;
/* Table: t_order */
create table t_order (
  id int not null auto_increment comment '主键自增',
  t_u_id int comment '用户ID',
  order_name varchar(100) comment '订单名称',
  order_status int comment '订单状态',
  create_time datetime comment '创建时间',
  update_time datetime comment '更新时间',
  primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

画面13 SQL文件名：
heima_leadnews.sql

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8 PPT标题：4.2 分库设计
架构图结构：
- AppInfo app信息库 → 存储用户信息、文章信息、用户动态、用户评论、用户认证等
- Behavior 用户行为库 → 存储用户行为，包括用户的转发、点赞、评论行为等
- WebMedia 文章库 → 存储多媒体文章数据，账号相关数据等
- Crawlers 爬虫库 → 存储从网络上爬取的文章信息等
- Admin 后台管理库 → 存储后台管理信息

画面9 核心数据流图结构：
- CSDN → 用户 → App → 管理 → 爬虫 → 文章
- CSDN → 用户 → App → 管理 → 爬虫 → 文章

画面10 表格数据：
传统设计：
用户表：
- 用户ID
- 用户名称
订单表：
- 订单ID
- 用户ID
冗余设计：
用户表：
- 用户ID
- 用户名称
订单表：
- 订单ID
- 用户ID

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
