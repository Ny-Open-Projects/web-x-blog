# 画面线理解：day15-8-定时还款任务-基础配置

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-6 实现定时还款任务
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-6 实现定时还款任务\day15-8-定时还款任务-基础配置_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:34, 01:47, 02:09, 02:23, 02:53, 03:47, 03:56, 04:24, 04:40, 05:46, 06:06, 06:40, 06:50, 06:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:34:59

1) 这一组画面整体在讲如何使用 Elastic-job 实现定时还款任务的分布式调度，并配置 Apollo 配置中心。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目目录结构，包含“day15”文件夹及子目录如“elasticsearch-7.7”、“img”、“资料”等。
画面2：展示一个流程图，描述还款计划处理流程，包含多个步骤如“生成还款明细”、“保存交易记录”、“处理成功”等，流程图中包含一个“60%”的进度指示。
画面3：在 SQLyog 中打开数据库“p2p_repayment”，显示“p2p_repayment”数据库的表结构，包括“t_user”、“t_account”、“t_deposit”等表。
画面4：在 SQLyog 中执行 SQL 查询，查询“t_repayment”表，显示还款计划数据，包括“PROJECT_ID”、“INTEREST”、“REPAYMENT_DATE”等字段。
画面5：在 Word 文档中显示“7 定时还款任务”章节，其中“7.1 分布式任务调度Elastic-job”和“7.2 功能实现”部分，包含依赖配置代码。
画面6：在 IntelliJ IDEA 中打开“wansin2p-repayment-service”项目，显示项目结构，包括“mapper”、“service”、“model”等包。
画面7：在 Word 文档中显示“7.2 功能实现”部分，包含 Elastic-job 依赖配置代码。
画面8：在 Apollo 配置中心网页界面，显示“还款-service”项目，包含“uaa-service”、“depository-agent-service”等服务。
画面9：在 Apollo 配置中心网页界面，显示“micro_service.elasticjob”配置项，包含“p2p.zookeeper.connString”、“p2p.job.namespace”、“p2p.job.count”、“p2p.job.cron”等配置。
画面10：在 Word 文档中显示“micro_service.elasticjob”配置内容，包括“# zookeeper服务地址”、“# 分片空间”、“# cron表达式(定时策略)”等注释和配置。
画面11：在 IntelliJ IDEA 中打开“pom.xml”文件，显示 Elastic-job 依赖配置。
画面12：在 Apollo 配置中心网页界面，显示“micro_service.elasticjob”配置项，包含“p2p.zookeeper.connString”、“p2p.job.namespace”、“p2p.job.count”、“p2p.job.cron”等配置。
画面13：在 Word 文档中显示“micro_service.elasticjob”配置内容，包括“# zookeeper服务地址”、“# 分片空间”、“# cron表达式(定时策略)”等注释和配置。
画面14：在 Word 文档中显示“application.yml”配置文件内容，包括“app.id: repayment-service”、“apollo.bootstrap: true”、“apollo.namespaces: micro_service.elasticjob, micro_service.spr”等配置。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面5：
```xml
<dependency>
    <groupId>com.dangdang</groupId>
    <artifactId>elastic-job-lite-spring</artifactId>
    <version>2.1.5</version>
</dependency>
```

画面7：
```xml
<dependency>
    <groupId>com.dangdang</groupId>
    <artifactId>elastic-job-lite-spring</artifactId>
    <version>2.1.5</version>
</dependency>
```

画面10：
```properties
# zookeeper服务地址
p2p.zookeeper.connString = localhost:2181
# 分片空间
p2p.job.namespace = p2p-elastic-job
# 分片数
p2p.job.count = 2
# cron表达式(定时策略)
p2p.job.cron = 0/5 * * * * ?
```

画面11：
```xml
<dependency>
    <groupId>com.dangdang</groupId>
    <artifactId>elastic-job-lite-spring</artifactId>
    <version>2.1.5</version>
</dependency>
```

画面13：
```properties
# zookeeper服务地址
p2p.zookeeper.connString = localhost:2181
# 分片空间
p2p.job.namespace = p2p-elastic-job
# 分片数
p2p.job.count = 2
# cron表达式(定时策略)
p2p.job.cron = 0/5 * * * * ?
```

画面14：
```yaml
app:
  id: repayment-service
apollo:
  bootstrap: true
  namespaces: micro_service.elasticjob, micro_service.spr
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2：流程图结构（从左到右）：
- 1.1 生成还款计划 → 1.2 生成还款明细 → 1.3 生成签名及数据 → 1.4 保存交易记录 → 1.5 保存处理结果 → 1.6 处理成功 → 1.7 通知还款金额
- 2.1 通知接收成功 → 2.2 确认还款处理 → 2.3 收款确认成功
- 3.1 通知接收成功 → 3.2 确认还款处理 → 3.3 收款确认成功
- 4.1 通知接收成功 → 4.2 确认还款处理 → 4.3 收款确认成功
- 5.1 通知接收成功 → 5.2 确认还款处理 → 5.3 收款确认成功
- 6.1 通知接收成功 → 6.2 确认还款处理 → 6.3 收款确认成功
- 7.1 通知接收成功 → 7.2 确认还款处理 → 7.3 收款确认成功
- 8.1 通知接收成功 → 8.2 确认还款处理 → 8.3 收款确认成功
- 9.1 通知接收成功 → 9.2 确认还款处理 → 9.3 收款确认成功
- 10.1 通知接收成功 → 10.2 确认还款处理 → 10.3 收款确认成功
- 11.1 通知接收成功 → 11.2 确认还款处理 → 11.3 收款确认成功
- 12.1 通知接收成功 → 12.2 确认还款处理 → 12.3 收款确认成功
- 13.1 通知接收成功 → 13.2 确认还款处理 → 13.3 收款确认成功
- 14.1 通知接收成功 → 14.2 确认还款处理 → 14.3 收款确认成功
- 15.1 通知接收成功 → 15.2 确认还款处理 → 15.3 收款确认成功
- 16.1 通知接收成功 → 16.2 确认还款处理 → 16.3 收款确认成功
- 17.1 通知接收成功 → 17.2 确认还款处理 → 17.3 收款确认成功
- 18.1 通知接收成功 → 18.2 确认还款处理 → 18.3 收款确认成功
- 19.1 通知接收成功 → 19.2 确认还款处理 → 19.3 收款确认成功
- 20.1 通知接收成功 → 20.2 确认还款处理 → 20.3 收款确认成功
- 21.1 通知接收成功 → 21.2 确认还款处理 → 21.3 收款确认成功
- 22.1 通知接收成功 → 22.2 确认还款处理 → 22.3 收款确认成功
- 23.1 通知接收成功 → 23.2 确认还款处理 → 23.3 收款确认成功
- 24.1 通知接收成功 → 24.2 确认还款处理 → 24.3 收款确认成功
- 25.1 通知接收成功 → 25.2 确认还款处理 → 25.3 收款确认成功
- 26.1 通知接收成功 → 26.2 确认还款处理 → 26.3 收款确认成功
- 27.1 通知接收成功 → 27.2 确认还款处理 → 27.3 收款确认成功
- 28.1 通知接收成功 → 28.2 确认还款处理 → 28.3 收款确认成功
- 29.1 通知接收成功 →
