# 画面线理解：23.查询列表实现的bug修复（测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\23.查询列表实现的bug修复（测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:32, 01:11, 01:45, 01:55, 02:18, 02:26, 02:46, 02:58, 03:08, 03:28, 03:52, 04:00, 04:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:16:42

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Robo 3T 数据库客户端查询 MongoDB 中的评论数据，并结合 Genymotion 模拟器展示前端应用中用户点赞、评论等交互行为，同时涉及 Navicat 数据库管理工具和 Advanced REST Client 的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：桌面环境，显示 Robo 3T 1.2 程序图标，任务栏中可见 Robo 3T 窗口。
画面 2：Robo 3T 窗口，显示数据库集合列表，选中 "quanzi_publish" 集合，执行查询语句：db.getCollection('quanzi_publish').find({})。
画面 3：Robo 3T 窗口，鼠标悬停在 "quanzi_publish" 集合上，查询语句未变化。
画面 4：Robo 3T 窗口显示查询结果（两条记录），右侧 Genymotion 模拟器显示 "FormatException: Invalid number (at character 1)" 错误。
画面 5：Robo 3T 窗口查询结果不变，Genymotion 模拟器切换到“评论”页面，显示用户“波仔”的评论内容。
画面 6：Navicat Premium 窗口，连接到 tb_user@mytanhua 数据库，显示 "tb_user" 表的记录，右侧 Genymotion 模拟器显示“喜欢”页面。
画面 7：Robo 3T 窗口，查询语句执行后，显示 "quanzi_comment" 集合的查询结果。
画面 8：Navicat Premium 窗口，"tb_user" 表中新增了 "updated" 字段，显示记录的更新时间。
画面 9：浏览器中打开 Advanced REST Client，准备发送 HTTP 请求。
画面 10：浏览器中 Advanced REST Client 页面空白。
画面 11：Robo 3T 窗口，显示 "quanzi_comment" 集合的查询结果。
画面 12：Robo 3T 窗口，查询结果不变，Genymotion 模拟器切换到“点赞”页面，显示用户“波仔”点赞了内容。
画面 13：Robo 3T 窗口，查询结果不变，Genymotion 模拟器显示“点赞”页面，内容已更新。
画面 14：Typora 编辑器打开 "day05 满意.md" 文件，显示 Java 代码片段，用于查询评论列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
db.getCollection('quanzi_publish').find({})

画面 7：
// 无代码

画面 11：
// 无代码

画面 14：
@Override
public PageInfo<Comment> queryCommentListByUser(long userId, Integer type,
Integer page, Integer pageSize) {
PageRequest pageRequest = PageRequest.of(page - 1, pageSize,
Sort.by(Sort.Order.desc("created")));
Query query = new Query(Criteria
.where("publishUserId").is(userId)
.and("commentType").is(type)).with(pageRequest);
List<Comment> commentList = this.mongoTemplate.find(query, Comment.class);
PageInfo<Comment> pageInfo = new PageInfo<>();
pageInfo.setPageNum(page);
pageInfo.setPageSize(pageSize);
pageInfo.setRecords(commentList);
pageInfo.setTotal(0); //不提供总数
return pageInfo;
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14：
PPT 标题：day05 满意.md
章节标题：9、公告列表
章节内容：
9.1、查询
9.2、pop

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
