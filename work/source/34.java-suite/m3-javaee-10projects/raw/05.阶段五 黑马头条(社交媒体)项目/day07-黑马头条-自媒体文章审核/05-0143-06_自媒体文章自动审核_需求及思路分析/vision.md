# 画面线理解：06_自媒体文章自动审核_需求及思路分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\06_自媒体文章自动审核_需求及思路分析【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:31, 00:41, 00:47, 01:58, 03:28, 03:55, 04:19, 04:36, 05:34, 06:21, 06:43, 06:53, 07:08, 07:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:18:58

1) 这一组画面整体在讲自媒体文章审核的业务流程和数据库表结构设计。

2) 按时间顺序列出每张画面的要点：
画面1：展示文档目录结构，当前章节为“2.2 自媒体文章审核”，并显示数据库表“wm_news”的字段结构（如：id, title, content_id, etc.）。
画面2：流程图开始，自媒体发布文章 → MQ → 获取文章信息 → 判断文章状态是否为4。
画面3：流程图继续，判断文章状态是否为4 → 若否，则判断状态是否为1且发布时间小于当前时间。
画面4：流程图继续，判断状态是否为1 → 若是，则判断标题与内容是否匹配 → 若不匹配，则转人工审核或拒绝。
画面5：流程图继续，判断标题与内容是否匹配 → 若匹配，则进入审核文本步骤。
画面6：流程图继续，审核文本 → 审核图片 → 判断发布时间是否大于当前时间。
画面7：流程图继续，判断发布时间是否大于当前时间 → 若否，则保存数据（涉及表：wp_article_config, wp_article, wp_article_content, wp_author）。
画面8：流程图继续，判断发布时间是否大于当前时间 → 若是，则创建索引。
画面9：流程图继续，创建索引 → 修改wp_news文章表结构（如：添加字段、修改字段）。
画面10：流程图继续，修改wp_news文章表结构 → 保存数据。
画面11：流程图继续，判断文章状态是否为4 → 若否，则判断状态是否为1且发布时间小于当前时间。
画面12：流程图继续，判断状态是否为1 → 若是，则判断标题与内容是否匹配 → 若不匹配，则转人工审核或拒绝。
画面13：流程图继续，判断标题与内容是否匹配 → 若匹配，则进入审核文本步骤。
画面14：流程图继续，审核文本 → 审核图片 → 判断发布时间是否大于当前时间。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面1：
Table Properties - 自媒体文章内容信息表 (wm_news)
| Name | Code | Comment | Default Value | Data Type | Length | Position | 
| --- | --- | --- | --- | --- | --- | --- |
| id | id | 主键 | | int(11) | 11 | 1 |
| title | title | 标题 | | varchar(50) | 50 | 2 |
| content_id | content_id | 文章ID | | varchar(50) | 50 | 3 |
| author_id | author_id | 作者ID | | varchar(50) | 50 | 4 |
| type | type | 类型 | | varchar(20) | 20 | 5 |
| status | status | 状态 | | int(11) | 11 | 6 |
| publish_time | publish_time | 发布时间 | | datetime | 0 | 7 |
| update_time | update_time | 更新时间 | | datetime | 0 | 8 |
| create_time | create_time | 创建时间 | | datetime | 0 | 9 |
| delete_flag | delete_flag | 删除标识 | 0 | int(11) | 11 | 10 |
| content | content | 内容 | | longtext | 0 | 11 |
| cover_url | cover_url | 封面图地址 | | varchar(255) | 255 | 12 |
| tags | tags | 标签 | | varchar(255) | 255 | 13 |
| views | views | 浏览量 | 0 | int(11) | 11 | 14 |
| likes | likes | 点赞数 | 0 | int(11) | 11 | 15 |
| comments | comments | 评论数 | 0 | int(11) | 11 | 16 |
| share_times | share_times | 分享次数 | 0 | int(11) | 11 | 17 |
| is_top | is_top | 是否置顶 | 0 | int(11) | 11 | 18 |
| is_recommend | is_recommend | 是否推荐 | 0 | int(11) | 11 | 19 |
| is_hot | is_hot | 是否热门 | 0 | int(11) | 11 | 20 |
| is_deleted | is_deleted | 是否删除 | 0 | int(11) | 11 | 21 |
| is_draft | is_draft | 是否草稿 | 0 | int(11) | 11 | 22 |
| is_locked | is_locked | 是否锁定 | 0 | int(11) | 11 | 23 |
| is_spam | is_spam | 是否垃圾 | 0 | int(11) | 11 | 24 |
| is_sensitive | is_sensitive | 是否敏感 | 0 | int(11) | 11 | 25 |
| is_deleted | is_deleted | 是否删除 | 0 | int(11) | 11 | 26 |
| is_draft | is_draft | 是否草稿 | 0 | int(11) | 11 | 27 |
| is_locked | is_locked | 是否锁定 | 0 | int(11) | 11 | 28 |
| is_spam | is_spam | 是否垃圾 | 0 | int(11) | 11 | 29 |
| is_sensitive | is_sensitive | 是否敏感 | 0 | int(11) | 11 | 30 |

画面7：
保存数据涉及表：
wp_article_config
wp_article
wp_article_content
wp_author

4) 出现的 PPT 标题、架构图/流程图的结构：
画面2-14：流程图结构：
自媒体 → 发布文章 → MQ → 获取文章信息 → 判断文章状态是否为4 → 若否，则判断状态是否为1且发布时间小于当前时间 → 若是，则判断标题与内容是否匹配 → 若不匹配，则转人工审核或拒绝 → 若匹配，则审核文本 → 审核图片 → 判断发布时间是否大于当前时间 → 若否，则保存数据 → 创建索引 → 修改wp_news文章表结构 → 保存数据。

5) 无。
