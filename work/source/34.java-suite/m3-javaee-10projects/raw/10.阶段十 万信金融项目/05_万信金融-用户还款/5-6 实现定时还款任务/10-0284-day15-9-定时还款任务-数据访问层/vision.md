# 画面线理解：day15-9-定时还款任务-数据访问层

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-6 实现定时还款任务
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-6 实现定时还款任务\day15-9-定时还款任务-数据访问层_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:37, 01:33, 01:46, 01:58, 02:06, 02:13, 02:47, 04:07, 04:47, 05:04, 05:14, 05:27, 05:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:35:30

1) 这一组画面整体在讲如何在还款服务中使用 Elastic-job 实现分布式定时任务，通过分片查询来处理到期还款计划。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程PPT的“7.1 分布式任务调度Elastic-job”章节，以及左侧的目录结构，其中“7.2 功能实现”部分提到“采用Elastic-job实现分布式定时还款任务”。
画面2: 展示了IDEA项目结构，选中了“application.yml”文件，准备进行配置。
画面3: 展示了“PlanMapper.java”文件中的SQL语句，用于查询到期还款计划。
画面4: 展示了课程PPT的“7.1 分布式任务调度Elastic-job”和“7.2 功能实现”章节，强调使用Elastic-job实现定时还款任务。
画面5: 展示了“application.yml”配置文件中的内容，包括服务ID、Apollo配置等。
画面6: 展示了“PlanMapper.java”文件中的SQL语句，用于查询到期还款计划。
画面7: 展示了“PlanMapper.java”文件中的SQL语句，用于查询到期还款计划。
画面8: 展示了数据库管理工具中的“p2p_repayment”表结构，包括字段和类型。
画面9: 展示了“PlanMapper.java”文件中的SQL语句，用于查询到期还款计划。
画面10: 展示了“PlanMapper.java”文件中的SQL语句，用于查询到期还款计划。
画面11: 展示了“PlanMapper.java”文件中的SQL语句，用于查询到期还款计划。
画面12: 展示了“PlanMapper.java”文件中的SQL语句，用于查询到期还款计划。
画面13: 展示了“PlanMapper.java”文件中的SQL语句，用于查询到期还款计划。
画面14: 展示了“PlanMapper.java”文件中的SQL语句，用于查询到期还款计划。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5中的application.yml配置：
app:
  id: repayment-service
apollo:
  bootstrap:
    enabled: true
  namespaces: micro_service.elasticjob micro_service.spr

画面3中的SQL语句：
SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE,'%Y-%m-%d') = #{date} AND REPAYMENT_STATUS = '0'

画面7中的SQL语句：
SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE,'%Y-%m-%d') = #{date} AND REPAYMENT_STATUS = '0'

画面11中的SQL语句：
SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE,'%Y-%m-%d') = #{date} AND REPAYMENT_STATUS = '0'

画面12中的SQL语句：
SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE,'%Y-%m-%d') = #{date} AND REPAYMENT_STATUS = '0' AND MOD(NUMBER_OF_PERIODS,#{shardingCount})=#{shardingItem}

画面13中的SQL语句：
SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE,'%Y-%m-%d') = #{date} AND REPAYMENT_STATUS = '0' AND MOD(NUMBER_OF_PERIODS,#{shardingCount})=#{shardingItem}

画面14中的SQL语句：
SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE,'%Y-%m-%d') = #{date} AND REPAYMENT_STATUS = '0' AND MOD(NUMBER_OF_PERIODS,#{shardingCount})=#{shardingItem}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4中的PPT标题：
7.1 分布式任务调度Elastic-job
7.2 功能实现

画面1中的PPT标题：
6.6 功能测试
7 定时还款任务
7.1 分布式任务调度Elastic-job
7.2 功能实现

画面5中的PPT标题：
7.2 功能实现
3. 在PlanMapper接口中再增加一个selectDueRepayment方法，用来进行分片查询

5) 不要评价画面美观，不要输出与课程无关的内容。
