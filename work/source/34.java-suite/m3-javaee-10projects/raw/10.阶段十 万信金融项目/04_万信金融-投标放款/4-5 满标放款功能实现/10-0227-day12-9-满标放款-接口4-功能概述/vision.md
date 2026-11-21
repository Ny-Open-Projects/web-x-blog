# 画面线理解：day12-9-满标放款-接口4-功能概述

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-9-满标放款-接口4-功能概述_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:20, 00:53, 01:55, 02:08, 02:40, 02:43, 02:46, 03:46, 04:02, 04:20, 04:57, 05:09, 05:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:51:18

1) 这一组画面整体在讲还款服务的业务流程与数据库表结构设计，包括接口调用、状态变更和数据持久化。

2) 按时间顺序列出每张画面的要点：
画面1: 展示还款服务的时序图，包含“借款APP”、“交易中心”、“贷款处理中心”、“还款服务”、“存管系统”等角色，描述了从用户发起还款请求到最终状态更新的完整流程。
画面2: 展示时序图中“还款成功”后的状态变更，包括更新交易记录、调整状态、生成还款计划等。
画面3: 展示“还款计划.txt”文件，内容为“还款计划：针对借款人的 保存到表中”。
画面4: 展示“还款计划.txt”文件，内容为“还款计划：针对借款人的 保存到表中”。
画面5: 展示数据库表“repayment_plan”的结构，包含字段如ID、CONSUMER_ID、USER_ID、PROJECT_ID等。
画面6: 展示IDE中“wansingzp-repayment-service”项目的目录结构，包含src/main/java、src/main/resources等。
画面7: 展示“还款计划.txt”文件，内容为“还款计划：针对借款人的 保存到表中”。
画面8: 展示时序图中“还款成功”后的状态变更，包括更新交易记录、调整状态、生成还款计划等。
画面9: 展示数据库表“repayment_plan”的结构，包含字段如ID、CONSUMER_ID、USER_ID、PROJECT_ID等。
画面10: 展示数据库表“receivable_plan”的结构，包含字段如ID、CONSUMER_ID、USER_ID、PROJECT_ID等。
画面11: 展示数据库表“repayment_plan”的结构，包含字段如ID、CONSUMER_ID、USER_ID、PROJECT_ID等。
画面12: 展示时序图中“还款成功”后的状态变更，包括更新交易记录、调整状态、生成还款计划等。
画面13: 展示PPT内容，标题为“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.1 还款方式”，并列出月利率、每月还款额、第n月利息的计算公式。
画面14: 展示PPT内容，标题为“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.2 功能实现”，并列出“在mapper包中定义一个PlanMapper接口”的注释。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5: 表: repayment_plan
Columns (13)
Field Type Comment
ID bigint(20) NOT NULL 主键
CONSUMER_ID bigint(20) NULL 借款人用户标识
USER_ID varchar(50) NULL 借款人用户标识
PROJECT_ID varchar(50) NULL 借款项目标识
NUMBER_OF_PERIODS int(11) NULL 还款期数
INTEREST decimal(10,2) NULL 还款利息
PRINCIPAL decimal(10,2) NULL 还款本金
AMOUNT decimal(10,2) NULL 还款金额
REPAYMENT_STATUS varchar(50) NULL 还款状态
CREATE_DATE datetime NULL 创建时间
COMMISSION decimal(10,2) NULL 平台佣金
Indexes (1)
画面10: 表: receivable_plan
Columns (13)
Field Type Comment
ID bigint(20) NOT NULL 主键
CONSUMER_ID bigint(20) NULL 借款人用户标识
USER_ID varchar(50) NULL 借款人用户标识
PROJECT_ID varchar(50) NULL 借款项目标识
NUMBER_OF_PERIODS int(11) NULL 还款期数
INTEREST decimal(10,2) NULL 还款利息
PRINCIPAL decimal(10,2) NULL 还款本金
AMOUNT decimal(10,2) NULL 还款金额
SHOULD_RECEIVABLE_DATE datetime NULL 应收时间
MENTION_DATE datetime NULL 提醒时间
CREATE_DATE datetime NULL 创建时间
COMMISSION decimal(10,2) NULL 平台佣金
Indexes (1)
画面13: 月利率 = 借款年利率 / 12
每月还款额 = 借款本金 × [月利率 × (1 + 月利率) ^ 借款月数] / [(1 + 月利率) ^ 借款月数 - 1]
第n月利息 = 本金 × 月利率 × (1 + 月利率) ^ (n - 1) / [(1 + 月利率) ^ 借款月数 - 1]
画面14: // 借款人还款计划 Mapper 接口

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1: 时序图，角色包括“借款APP”、“交易中心”、“贷款处理中心”、“还款服务”、“存管系统”，箭头表示调用关系。
画面13: PPT标题“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.1 还款方式”，并列出月利率、每月还款额、第n月利息的计算公式。
画面14: PPT标题“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.2 功能实现”，并列出“在mapper包中定义一个PlanMapper接口”的注释。

5) 不要评价画面美观，不要输出与课程无关的内容。
