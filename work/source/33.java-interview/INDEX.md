# Java 后端面试全景 · 总索引（对标阿里 P10）

> 本文件由 `InterviewGuideGenerator` 自动生成，重新运行 `mvn compile exec:java` 可刷新统计。

| 章节 | 题目数 | 中文字数(约) | 预计学习时长 |
|------|--------|--------------|--------------|
| [第 1 章 Java 语言基础与集合](docs/01-java-fundamentals/README.md) | 13 | 5586 | 4 小时 |
| [第 2 章 并发编程与 JUC](docs/02-jvm-concurrency/README.md) | 15 | 5859 | 4 小时 |
| [第 3 章 JVM 与性能调优](docs/03-jvm/README.md) | 13 | 6206 | 4 小时 |
| [第 4 章 Spring 与主流框架生态](docs/04-spring-ecosystem/README.md) | 15 | 5678 | 4 小时 |
| [第 5 章 MySQL 与存储](docs/05-mysql-storage/README.md) | 13 | 5467 | 4 小时 |
| [第 6 章 Redis 与缓存体系](docs/06-redis-cache/README.md) | 12 | 4935 | 3 小时 |
| [第 7 章 消息队列与异步化](docs/07-messaging/README.md) | 14 | 4773 | 3 小时 |
| [第 8 章 分布式理论与微服务](docs/08-distributed-microservices/README.md) | 13 | 5331 | 4 小时 |
| [第 9 章 亿级高并发系统设计与真实场景题](docs/09-system-design/README.md) | 7 | 3717 | 2 小时 |
| [第 10 章 AI 时代：LLM、Agent 与 AI 应用架构](docs/10-ai-agent/README.md) | 12 | 5495 | 4 小时 |
| [附录 A-D](docs/11-appendix/README.md) | 12 | 2873 | 2 小时 |
| [第 12 册 Arthas 线上诊断实操手册](docs/12-arthas-lab/README.md) | 0 | 1531 | 1 小时 |
| [第 13 册 手写代码题全解](docs/13-coding-lab/README.md) | 10 | 1721 | 1 小时 |
| [第 14 册 模拟面试实战剧本](docs/14-mock-interview/README.md) | 0 | 2951 | 2 小时 |
| [第 15 册 快问快答冲刺卡](docs/15-rapid-fire/README.md) | 0 | 2039 | 1 小时 |
| [第 16 册 90 天每日打卡任务清单](docs/16-daily-plan/README.md) | 0 | 1962 | 1 小时 |
| [第 17 册 阿里职级体系与面试流程解析](docs/17-process/README.md) | 0 | 1552 | 1 小时 |
| [第 18 册 示例面试实录](docs/18-annotated-transcript/README.md) | 0 | 2504 | 2 小时 |
| [第 19 册 二面 / 三面实录精简版](docs/19-transcript-r2r3/README.md) | 0 | 2964 | 2 小时 |
| [第 20 册 源码逐行精读](docs/20-source-code/README.md) | 0 | 1893 | 1 小时 |
| [第 21 册 四面（总监面）与 HR 面实录](docs/21-transcript-final/README.md) | 0 | 2272 | 2 小时 |
| [第 22 册 面试官视角 · 由浅入深追问地图与补漏合集](docs/22-interviewer-coverage/README.md) | 0 | 4473 | 3 小时 |
| [第 23 册 全卷对话版](docs/23-dialog/README.md) | 0 | 139 | 1 小时 |
| [第 24 册 笔试题库](docs/24-written-exam/README.md) | 0 | 3743 | 2 小时 |
| [第 25 章 MongoDB 与文档数据库](docs/25-mongodb/README.md) | 7 | 2393 | 2 小时 |

**合计**：25 个章节，156 道题，正文约 8.8 万字。

- **[总交付说明（先读这个）](DELIVERY.md)**——全库导览与训练路径
- [大纲与章节结构](docs/00-outline.md)
- **[全卷速记卡合订本（考前一小时专用）](SPEED-CARDS.md)**
- [学习进度打卡表](STUDY-TRACKER.md)
- [Arthas 实战沙盘](notes/arthas-practice/README.md)（需 JDK，安装见 tools/）
- **[面试话术检索手册（HTML 可搜索）](notes/quiz/exams/interview-manual.html)**——5580 题话术背诵利器
- **[Agent 手写大题套卷](docs/agent-written-exam/README.md)**——十题完整版（题目+参考实现+评分细则+追问）
- **[笔试题库总览](notes/quiz/README.md)**——6145 题生成题库（11 域，知识点矩阵驱动）
  - 各域笔试卷：`notes/quiz/out/<域名>/quiz-bank.md`（java-basics/concurrency/jvm/spring/mysql/redis/mongodb/mq/distributed/ai/algorithm）
  - 各域面试题卷：`notes/quiz/out/<域名>/interview-bank.md`（【面试官】+【标准回答话术】+【评分点】，P1-P10 分层）
  - 题号格式 `Q<域名>-<序号>`（如 Qmysql-1514），跨域引用不歧义

## 学习路径建议

1. **零基础起步**：先读每章的“零基础卡片”小节，配合第 16 册 30/60/90 天打卡计划；
2. **主线推进**：第 1→2→3 章是 Java 内功，第 4→5→6→7 章是中间件，第 8→9 章是架构，第 10 章是差异化加分；
3. **冲刺背诵**：只用各章“一页速记卡”+ 合订本滚动复习；
4. **模拟实战**：第 9 章五步法 + 附录 A 软实力题 + 第 18/19/21 册实录范文对照演练。
