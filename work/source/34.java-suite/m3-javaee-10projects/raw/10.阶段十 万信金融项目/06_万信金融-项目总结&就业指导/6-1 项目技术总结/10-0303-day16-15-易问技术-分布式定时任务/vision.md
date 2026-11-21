# 画面线理解：day16-15-易问技术-分布式定时任务

- 阶段：10.阶段十 万信金融项目
- 章节：06_万信金融-项目总结&就业指导/6-1 项目技术总结
- 源文件：10.阶段十 万信金融项目\06_万信金融-项目总结&就业指导\6-1 项目技术总结\day16-15-易问技术-分布式定时任务_【海量资源尽在 666java.com】.mp4
- 抽帧：12 帧 @ 07:48, 07:50, 08:19, 11:13, 11:14, 11:15, 11:16, 11:19, 13:39, 13:40, 13:42, 13:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:48:43

1) 这一组画面整体在讲分布式定时任务（Elastic-job）的背景、分片概念及如何通过Elastic-job实现分布式定时还款任务。

2) 按时间顺序列出每张画面的要点：
画面1:
- 标题：3.5.1 什么是任务调度？什么是分布式定时任务？
- 内容：列举了电商、银行、财务、网站等业务场景，指出其解决方案是任务调度。
- 内容：定义了任务调度是“自动完成特定任务，在约定的特定时刻去执行任务的过程”。
- 内容：指出当前架构转向分布式，引出“分布式任务调度”概念。
- 内容：标题“3.5.2 请说一下分片的概念”出现。

画面2:
- 标题：3.5.2 请说一下分片的概念
- 内容：解释任务分片执行，举例说明如何将作业分片到多台服务器。
- 内容：给出分片逻辑：服务器A处理奇数ID数据，服务器B处理偶数ID数据。
- 内容：提到“前面我们已经把用户还款功能实现了，但是需要通过定时任务去自动触发功能的执行。这里可以采用Elastic-job实现分布式定时还款任务，在查询到期的还款计划时根据NUMBER_OF_PERIODS()函数进行分片。”

画面3:
- 标题：3.5.2 请说一下分片的概念
- 内容：重复画面2内容，强调分片逻辑和Elastic-job实现分片。

画面4:
- 标题：3.5.2 请说一下分片的概念
- 内容：重复画面2内容，强调分片逻辑和Elastic-job实现分片。

画面5:
- 标题：3.5.2 请说一下分片的概念
- 内容：显示代码片段，包含SQL查询语句和Java方法。
- 代码：
```java
// 查询所有到期的还款计划
@return
/*
Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, 'Yy-Mm-dd') = #{date} AND REPAYMENT_STATUS = '0' AND MOD(number_of_periods, #{shardingCount}) = #{shardingItem}")
List<RepaymentPlan> selectDueRepayment(@Param("date") string date, @Param("shardingCount") int shardingCount, @Param("shardingItem") int shardingItem);
```

画面6:
- 标题：3.6 ElasticSearch(ES)+Logstash
- 内容：标题切换，开始介绍ES全文检索原理。
- 内容：标题“3.6.1 请说一下ES进行全文检索的原理？”出现。

画面7:
- 标题：3.6 ElasticSearch(ES)+Logstash
- 内容：标题“3.6.1 请说一下ES进行全文检索的原理？”出现。
- 内容：解释ES全文检索原理：数据被分词存储到内部列表（目录）。

画面8:
- 标题：3.6 ElasticSearch(ES)+Logstash
- 内容：标题“3.6.1 请说一下ES进行全文检索的原理？”出现。
- 内容：解释ES全文检索原理：数据被分词存储到内部列表（目录）。

画面9:
- 标题：3.5.2 请说一下分片的概念
- 内容：显示代码片段，包含SQL查询语句和Java方法。
- 代码：
```java
// 查询所有到期的还款计划
@return
/*
Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, 'Yy-Mm-dd') = #{date} AND REPAYMENT_STATUS = '0' AND MOD(number_of_periods, #{shardingCount}) = #{shardingItem}")
List<RepaymentPlan> selectDueRepayment(@Param("date") string date, @Param("shardingCount") int shardingCount, @Param("shardingItem") int shardingItem);
```

画面10:
- 标题：3.5.2 请说一下分片的概念
- 内容：重复画面2内容，强调分片逻辑和Elastic-job实现分片。

画面11:
- 标题：3.5.2 请说一下分片的概念
- 内容：重复画面2内容，强调分片逻辑和Elastic-job实现分片。

画面12:
- 标题：3.5 分布式定时任务Elastic-job
- 内容：标题“3.5.1 什么是任务调度？什么是分布式定时任务？”出现。
- 内容：列举了电商、银行、财务、网站等业务场景，指出其解决方案是任务调度。
- 内容：定义了任务调度是“自动完成特定任务，在约定的特定时刻去执行任务的过程”。
- 内容：指出当前架构转向分布式，引出“分布式任务调度”概念。
- 内容：标题“3.5.2 请说一下分片的概念”出现。
